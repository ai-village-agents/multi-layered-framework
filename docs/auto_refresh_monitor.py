"""auto_refresh_monitor.py

Outline/reference implementation for Phase 10 automation.

Goals (as requested):
- Watch for changes to registry.json
- Regenerate docs/preservation-data.json (the published Pages artifact)
- Keep Pages in sync (optionally commit + push)
- Alert when coverage thresholds are not met

Notes:
- This script is intentionally dependency-light (no watchdog required).
- It is safe to run locally or in CI; CI wiring is left to maintainers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple


DEFAULT_WATCH_PATHS = [
    "docs/registry.json",
    "phase8-automation/registry/registry.json",
]
DEFAULT_OUTPUT_PATH = "docs/preservation-data.json"
DEFAULT_PROCESSOR_PATH = "phase8-automation/registry/preservation_map_processor.py"


@dataclass
class FileState:
    path: str
    sha256: str
    bytes: int
    mtime: float


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: str) -> FileState:
    h = hashlib.sha256()
    size = 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            size += len(chunk)
            h.update(chunk)
    st = os.stat(path)
    return FileState(path=path, sha256=h.hexdigest(), bytes=size, mtime=st.st_mtime)


def run_processor(processor_path: str, registry_path: str, output_path: str) -> None:
    """Run the preservation map processor.

    This assumes the repo contains a processor script capable of producing
    preservation-data.json. If the interface differs, adjust this function.
    """
    if not os.path.exists(processor_path):
        raise FileNotFoundError(f"Processor not found: {processor_path}")
    if not os.path.exists(registry_path):
        raise FileNotFoundError(f"Registry not found: {registry_path}")

    # Attempt a conservative call pattern. If the processor takes different flags,
    # update this invocation to match the repo's actual CLI.
    cmd = [sys.executable, processor_path]

    # Best-effort: many scripts accept --registry / --output or similar.
    # We try a couple patterns without being destructive.
    tried: List[List[str]] = [
        cmd + ["--registry", registry_path, "--output", output_path],
        cmd + [registry_path, output_path],
    ]

    last_err: Optional[Exception] = None
    for c in tried:
        try:
            subprocess.run(c, check=True)
            return
        except Exception as e:
            last_err = e

    raise RuntimeError(
        "Unable to run processor with known invocation patterns. "
        f"Last error: {last_err}"
    )


def git_commit_and_push(paths: List[str], message: str, push: bool) -> None:
    """Optionally commit + push regenerated artifacts."""
    subprocess.run(["git", "add", "--"] + paths, check=True)

    # Only commit if there are staged changes.
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode
    if diff == 0:
        return

    subprocess.run(["git", "commit", "-m", message], check=True)
    if push:
        subprocess.run(["git", "push"], check=True)


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def summarize_coverage(preservation_data: dict) -> Dict[str, float]:
    """Best-effort coverage summary.

    The published preservation-data.json is expected to evolve; this function
    should be updated to match the canonical schema. For now, we try to infer
    project-level coverage from available fields.
    """
    summary: Dict[str, float] = {}

    # Common schema seen so far: top-level keys metadata + points.
    points = preservation_data.get("points")
    if isinstance(points, list):
        # If points have project and participant fields, estimate coverage as
        # unique participants with at least one point.
        by_project: Dict[str, set] = {}
        for p in points:
            if not isinstance(p, dict):
                continue
            project = str(p.get("project", "unknown"))
            participant = p.get("participant")
            if participant is None:
                continue
            by_project.setdefault(project, set()).add(str(participant))

        # Without an authoritative denominator, we just report covered count.
        for project, participants in by_project.items():
            summary[project] = float(len(participants))

    return summary


def alert_thresholds(summary: Dict[str, float], min_covered: int) -> int:
    """Alert if any project has fewer than min_covered covered participants.

    Returns process exit code (0 ok, 2 alert).
    """
    alerts = [p for p, covered in summary.items() if covered < min_covered]
    if alerts:
        print(f"[{utc_now_iso()}] ALERT: coverage below threshold: {alerts}")
        return 2
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Auto-refresh monitor (outline)")
    ap.add_argument(
        "--watch",
        action="append",
        default=[],
        help="Path(s) to watch for changes (can be repeated)",
    )
    ap.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_PATH,
        help="Where to write the published preservation-data.json",
    )
    ap.add_argument(
        "--processor",
        default=DEFAULT_PROCESSOR_PATH,
        help="Processor script path to regenerate preservation-data.json",
    )
    ap.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Poll interval in seconds (dependency-free watcher)",
    )
    ap.add_argument(
        "--auto-commit",
        action="store_true",
        help="Commit regenerated artifacts when they change",
    )
    ap.add_argument(
        "--auto-push",
        action="store_true",
        help="Push commits (only used with --auto-commit)",
    )
    ap.add_argument(
        "--min-covered",
        type=int,
        default=1,
        help="Alert if any project has fewer than this many covered participants",
    )
    args = ap.parse_args(argv)

    watch_paths = args.watch[:] if args.watch else DEFAULT_WATCH_PATHS[:]

    print(f"[{utc_now_iso()}] Watching: {watch_paths}")
    print(f"[{utc_now_iso()}] Output:   {args.output}")

    last_states: Dict[str, FileState] = {}

    while True:
        changed = False
        existing_watch: List[str] = []

        for path in watch_paths:
            if not os.path.exists(path):
                continue
            existing_watch.append(path)
            state = sha256_file(path)
            prev = last_states.get(path)
            if prev is None or prev.sha256 != state.sha256:
                last_states[path] = state
                changed = True

        if not existing_watch:
            print(f"[{utc_now_iso()}] No watch paths exist yet; sleeping...")
            time.sleep(args.interval)
            continue

        if changed:
            # Prefer docs/registry.json if present, else fall back to phase8 registry.
            registry_path = (
                "docs/registry.json"
                if os.path.exists("docs/registry.json")
                else "phase8-automation/registry/registry.json"
            )
            print(f"[{utc_now_iso()}] Change detected. Regenerating from: {registry_path}")

            try:
                run_processor(args.processor, registry_path, args.output)
            except Exception as e:
                print(f"[{utc_now_iso()}] ERROR: regeneration failed: {e}", file=sys.stderr)
            else:
                # Alerts (best-effort)
                try:
                    data = load_json(args.output)
                    summary = summarize_coverage(data)
                    print(f"[{utc_now_iso()}] Coverage summary (best-effort): {summary}")
                    code = alert_thresholds(summary, min_covered=args.min_covered)
                    if code != 0:
                        print(f"[{utc_now_iso()}] Alert exit code would be: {code}")
                except Exception as e:
                    print(f"[{utc_now_iso()}] WARN: could not summarize coverage: {e}")

                # Pages sync (optional)
                if args.auto_commit:
                    try:
                        git_commit_and_push(
                            paths=[args.output],
                            message=f"Auto-refresh preservation-data.json ({utc_now_iso()})",
                            push=args.auto_push,
                        )
                    except Exception as e:
                        print(f"[{utc_now_iso()}] WARN: git commit/push failed: {e}")

        time.sleep(args.interval)


if __name__ == "__main__":
    raise SystemExit(main())
