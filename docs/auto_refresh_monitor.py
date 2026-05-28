#!/usr/bin/env python3
"""Auto-Refresh Monitoring System for Village Preservation Framework

Watches registry.json for changes and regenerates preservation-data.json.
Also updates unified dashboard and logs alerts for coverage thresholds.

This script is intended as a lightweight, dependency-free monitor that can be run
locally (or adapted into CI) to keep published coverage artifacts up to date.
"""

import os
import json
import time
import hashlib
import logging
from datetime import datetime
from typing import Dict, List, Optional, Set
import subprocess
import sys
import re
from urllib.parse import urlparse

# Configuration
CONFIG = {
    # Prefer published docs paths (repo Pages source is /docs)
    "registry_path": "docs/registry.json",
    "project_registry_path": "docs/project_registry.json",
    "preservation_data_path": "docs/preservation-data.json",
    "dashboard_path": "docs/unified-coverage-dashboard.html",
    "check_interval_seconds": 300,  # 5 minutes
    "alert_coverage_threshold": 100,  # Alert when any project hits 100%
    "max_history_days": 30,
    "git_repo_path": ".",  # Root of multi-layered-framework repository
    "log_file": "docs/auto_refresh.log",
}
CURRENT_DAY = 422

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


def calculate_file_hash(filepath: str) -> str:
    """Calculate SHA256 hash of a file."""
    if not os.path.exists(filepath):
        return ""

    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def load_registry() -> Dict:
    """Load and parse the registry.json file."""
    registry_path = CONFIG["registry_path"]

    if not os.path.exists(registry_path):
        logger.warning(f"Registry file not found: {registry_path}")
        return {"artifacts": [], "last_updated": datetime.utcnow().isoformat()}

    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        if isinstance(data, list):
            registry = {"artifacts": data}
        else:
            registry = data
            
        logger.info(f"Loaded registry with {len(registry.get('artifacts', []))} artifacts")
        return registry
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Failed to load registry: {e}")
        return {"artifacts": [], "last_updated": datetime.utcnow().isoformat()}


def load_project_registry() -> Dict:
    """Load and parse the project_registry.json file."""
    project_registry_path = CONFIG["project_registry_path"]

    if not os.path.exists(project_registry_path):
        logger.warning(f"Project registry file not found: {project_registry_path}")
        return {"projects": []}

    try:
        with open(project_registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            project_registry = {"projects": data}
        else:
            project_registry = data

        logger.info(f"Loaded project registry with {len(project_registry.get('projects', []))} projects")
        return project_registry
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Failed to load project registry: {e}")
        return {"projects": []}


def _normalize_project_key(value: str) -> str:
    """Normalize project labels/IDs into a comparable key."""
    normalized = re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()
    return re.sub(r"\s+", " ", normalized)


def _extract_slug_from_url(url: str) -> str:
    """Extract last URL path segment for project matching."""
    if not url:
        return ""
    try:
        path = urlparse(url).path.strip("/")
        if not path:
            return ""
        return path.split("/")[-1]
    except Exception:
        return ""


def _extract_registry_participants_by_project(artifacts: List[Dict]) -> Dict[str, Set[str]]:
    """Map normalized project keys to participant sets from registry artifacts."""
    participants_by_project: Dict[str, Set[str]] = {}

    for artifact in artifacts:
        project_name = (artifact.get("project", "") or "").strip()
        participant_name = (artifact.get("participant", "") or "").strip()

        if not project_name or not participant_name:
            continue

        project_key = _normalize_project_key(project_name)
        if not project_key:
            continue

        if project_key not in participants_by_project:
            participants_by_project[project_key] = set()
        participants_by_project[project_key].add(participant_name)

    return participants_by_project


def _extract_registry_artifact_counts_by_project(artifacts: List[Dict]) -> Dict[str, int]:
    """Map normalized project keys to artifact counts from registry artifacts."""
    artifact_counts_by_project: Dict[str, int] = {}

    for artifact in artifacts:
        project_name = (artifact.get("project", "") or "").strip()
        if not project_name:
            continue

        project_key = _normalize_project_key(project_name)
        if not project_key:
            continue

        artifact_counts_by_project[project_key] = artifact_counts_by_project.get(project_key, 0) + 1

    return artifact_counts_by_project


def _build_deepseek_expansion_recommendations(
    all_projects: List[Dict],
    participants_by_project: Dict[str, Set[str]],
    artifact_counts_by_project: Dict[str, int],
) -> List[Dict]:
    """Build prioritized expansion recommendations for uncovered/partially covered projects."""
    recommendations: List[Dict] = []
    creator_project_counts: Dict[str, int] = {}

    for project in all_projects:
        creator = (project.get("creator", "") or "").strip()
        if creator:
            creator_project_counts[creator] = creator_project_counts.get(creator, 0) + 1

    max_projects_by_creator = max(creator_project_counts.values(), default=1)
    project_artifact_counts: List[int] = []

    for project in all_projects:
        project_id = project.get("id", "")
        project_name = project.get("name", "")
        project_url = project.get("url", "")
        project_slug = _extract_slug_from_url(project_url)

        candidate_keys = {
            key
            for key in [
                _normalize_project_key(project_id),
                _normalize_project_key(project_name),
                _normalize_project_key(project_slug),
            ]
            if key
        }

        matched_active_keys = {
            active_key
            for active_key in artifact_counts_by_project
            if any(
                active_key == candidate
                or active_key in candidate
                or candidate in active_key
                for candidate in candidate_keys
            )
        }
        project_artifact_counts.append(sum(artifact_counts_by_project.get(key, 0) for key in matched_active_keys))

    max_artifacts_across_projects = max(project_artifact_counts, default=0)

    for project in all_projects:
        project_id = project.get("id", "")
        project_name = project.get("name", "")
        project_url = project.get("url", "")
        creator = (project.get("creator", "") or "").strip()
        project_slug = _extract_slug_from_url(project_url)
        expected_participants = project.get("expected_participants") or []
        if not isinstance(expected_participants, list):
            expected_participants = []
        creation_day = project.get("creation_day")

        candidate_keys = {
            key
            for key in [
                _normalize_project_key(project_id),
                _normalize_project_key(project_name),
                _normalize_project_key(project_slug),
            ]
            if key
        }
        matched_active_keys = {
            active_key
            for active_key in participants_by_project
            if any(
                active_key == candidate
                or active_key in candidate
                or candidate in active_key
                for candidate in candidate_keys
            )
        }

        covered_participants: Set[str] = set()
        for active_key in matched_active_keys:
            covered_participants.update(participants_by_project.get(active_key, set()))

        expected_set = {str(participant).strip() for participant in expected_participants if str(participant).strip()}
        covered_expected = covered_participants.intersection(expected_set) if expected_set else set()
        missing_set = expected_set - covered_expected
        missing_participants = len(missing_set)
        active_artifact_count = sum(artifact_counts_by_project.get(key, 0) for key in matched_active_keys)
        project_age_days = (
            CURRENT_DAY - int(creation_day)
            if isinstance(creation_day, (int, float, str)) and str(creation_day).strip().lstrip("-").isdigit()
            else 0
        )
        participant_engagement = (len(covered_expected) / len(expected_set)) if expected_set else 1.0

        popularity_factor = (
            (active_artifact_count / max_artifacts_across_projects) * 0.5 if max_artifacts_across_projects > 0 else 0.0
        )
        recency_boost = 0.2 if project_age_days < 7 else 0.0
        creator_activity_score = (
            creator_project_counts.get(creator, 0) / max_projects_by_creator if max_projects_by_creator > 0 else 0.0
        )
        priority_score = (
            missing_participants
            * (1 + popularity_factor)
            * (1 + recency_boost)
            * (1 + (0.1 * creator_activity_score))
        )

        # Include projects that are missing or not fully covered.
        if missing_participants > 0:
            recommendations.append(
                {
                    "project_id": project_id,
                    "project_name": project_name or project_id,
                    "missing_participants": missing_participants,
                    "expected_participants_count": len(expected_set),
                    "covered_participants_count": len(covered_expected),
                    "missing_participant_names": sorted(missing_set),
                    "project_age_days": project_age_days,
                    "participant_engagement": round(participant_engagement, 3),
                    "active_artifact_count": active_artifact_count,
                    "popularity_factor": round(popularity_factor, 3),
                    "recency_boost": round(recency_boost, 3),
                    "creator_activity_score": round(creator_activity_score, 3),
                    "priority_score": round(priority_score, 2),
                }
            )

    recommendations.sort(key=lambda item: (-item["priority_score"], -item["missing_participants"], item["project_name"]))
    return recommendations


def calculate_village_wide_coverage(registry: Dict, project_registry: Dict) -> Dict:
    """Calculate active project coverage against the full village project registry."""
    artifacts = registry.get("artifacts", [])
    all_projects = project_registry.get("projects", [])

    active_projects = {artifact.get("project", "").strip() for artifact in artifacts if artifact.get("project")}
    active_project_keys = {_normalize_project_key(project) for project in active_projects if project}
    participants_by_project = _extract_registry_participants_by_project(artifacts)
    artifact_counts_by_project = _extract_registry_artifact_counts_by_project(artifacts)

    covered_project_ids: List[str] = []
    covered_project_names: List[str] = []
    uncovered_project_ids: List[str] = []
    uncovered_project_names: List[str] = []

    for project in all_projects:
        project_id = project.get("id", "")
        project_name = project.get("name", "")
        project_url = project.get("url", "")
        project_slug = _extract_slug_from_url(project_url)

        candidate_keys = {
            key
            for key in [
                _normalize_project_key(project_id),
                _normalize_project_key(project_name),
                _normalize_project_key(project_slug),
            ]
            if key
        }

        matched = False
        for active_key in active_project_keys:
            if any(
                active_key == candidate
                or active_key in candidate
                or candidate in active_key
                for candidate in candidate_keys
            ):
                matched = True
                break

        if matched:
            covered_project_ids.append(project_id)
            covered_project_names.append(project_name or project_id)
        else:
            uncovered_project_ids.append(project_id)
            uncovered_project_names.append(project_name or project_id)

    total_projects = len(all_projects)
    covered_projects = len(covered_project_ids)
    coverage_percentage = round((covered_projects / total_projects) * 100, 1) if total_projects else 0.0
    expansion_recommendations = _build_deepseek_expansion_recommendations(
        all_projects, participants_by_project, artifact_counts_by_project
    )

    return {
        "coverage_percentage": coverage_percentage,
        "covered_projects": covered_projects,
        "total_projects": total_projects,
        "active_projects_in_registry": len(active_projects),
        "covered_project_ids": covered_project_ids,
        "covered_project_names": covered_project_names,
        "uncovered_project_ids": uncovered_project_ids,
        "uncovered_project_names": uncovered_project_names,
        "expansion_recommendations": expansion_recommendations,
    }


def analyze_coverage_by_project(registry: Dict) -> Dict[str, Dict]:
    """Analyze coverage by project from registry data.

    Returns dict with project coverage statistics.
    """
    artifacts = registry.get("artifacts", [])

    # Group artifacts by project
    projects: Dict[str, Dict] = {}
    for artifact in artifacts:
        project_name = artifact.get("project", "unknown")
        participant = artifact.get("participant", "unknown")

        if project_name not in projects:
            projects[project_name] = {"participants": set(), "artifacts": [], "latest_artifact": None}

        projects[project_name]["participants"].add(participant)
        projects[project_name]["artifacts"].append(artifact)

        # Track latest artifact
        artifact_time = artifact.get("timestamp", "")
        if artifact_time:
            current_latest = projects[project_name].get("latest_artifact")
            if not current_latest or artifact_time > current_latest.get("timestamp", ""):
                projects[project_name]["latest_artifact"] = artifact

    # Calculate coverage statistics for each project
    coverage_stats: Dict[str, Dict] = {}

    # Known project participant counts (from live sync analysis)
    PROJECT_PARTICIPANT_COUNTS = {
        "aethelgard": 3,  # Actual participants: Opus 4.5, Opus 4.6, Gemini 3.1 Pro
        "weather-oracle": 4,  # Actual: Sonnet 4.6, Opus 4.5, Gemini 3.1 Pro, Opus 4.6
        "storygame": 8,  # Expected participants (from analysis)
    }

    for project_name, data in projects.items():
        participant_count = len(data["participants"])
        expected_count = PROJECT_PARTICIPANT_COUNTS.get(project_name, participant_count)

        coverage_percentage = 0.0
        if expected_count > 0:
            coverage_percentage = round((participant_count / expected_count) * 100, 1)

        coverage_stats[project_name] = {
            "covered_participants": participant_count,
            "expected_participants": expected_count,
            "coverage_percentage": coverage_percentage,
            "artifact_count": len(data["artifacts"]),
            "latest_artifact": data.get("latest_artifact"),
            "status": "complete" if coverage_percentage >= 100 else "partial",
            "participants_list": list(data["participants"]),
        }

    return coverage_stats


def _calculate_overall_coverage(coverage_stats: Dict) -> float:
    """Calculate overall coverage percentage across all projects."""
    total_covered = 0
    total_expected = 0

    for project_stats in coverage_stats.values():
        total_covered += project_stats["covered_participants"]
        total_expected += project_stats["expected_participants"]

    if total_expected == 0:
        return 0.0

    return round((total_covered / total_expected) * 100, 1)


def regenerate_preservation_data(registry: Dict, coverage_stats: Dict, village_wide_coverage: Dict) -> Dict:
    """Regenerate preservation-data.json from registry and coverage stats.

    Note: Sonnet 4.6's Preservation Map currently expects a simpler schema
    (metadata + points). This generator produces a superset; adapt as needed.
    """
    artifacts = registry.get("artifacts", [])

    # Convert registry artifacts to preservation map format
    preservation_points = []

    for artifact in artifacts:
        preview = artifact.get("content_preview", "")
        if isinstance(preview, str) and len(preview) > 100:
            preview = preview[:100] + "..."

        point = {
            "id": artifact.get("id", ""),
            "project": artifact.get("project", "unknown"),
            "participant": artifact.get("participant", "unknown"),
            "semantic_score": artifact.get("semantic_score", 0),
            "affective_score": artifact.get("affective_score", 0),
            "quadrant": artifact.get("quadrant", "unknown"),
            "tier": artifact.get("tier", "unknown"),
            "survival_prediction": artifact.get("survival_prediction", 0),
            "timestamp": artifact.get("timestamp", ""),
            "content_preview": preview,
        }
        preservation_points.append(point)

    preservation_data = {
        "metadata": {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "registry_source": CONFIG["registry_path"],
            "project_registry_source": CONFIG["project_registry_path"],
            "artifacts_count": len(artifacts),
            "projects_count": len(coverage_stats),
            "village_wide_coverage": village_wide_coverage,
        },
        "coverage_statistics": coverage_stats,
        "recommendations": generate_recommendations(village_wide_coverage),
        "preservation_points": preservation_points,
        "summary": {
            "total_artifacts": len(artifacts),
            "total_projects": len(coverage_stats),
            "overall_coverage": _calculate_overall_coverage(coverage_stats),
            "village_wide_coverage": village_wide_coverage,
            "last_updated": datetime.utcnow().isoformat() + "Z",
        },
    }

    return preservation_data


def write_preservation_data(preservation_data: Dict) -> bool:
    """Write preservation data to JSON file."""
    try:
        output_path = CONFIG["preservation_data_path"]

        # Create backup of existing file
        if os.path.exists(output_path):
            backup_path = f"{output_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            import shutil

            shutil.copy2(output_path, backup_path)
            logger.info(f"Created backup: {backup_path}")

        # Write new file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(preservation_data, f, indent=2, ensure_ascii=False)

        logger.info(
            f"Preservation data written to {output_path} ({len(preservation_data.get('preservation_points', []))} points)"
        )
        return True

    except Exception as e:
        logger.error(f"Failed to write preservation data: {e}")
        return False


def check_for_coverage_alerts(
    coverage_stats: Dict, previous_stats: Optional[Dict] = None
) -> List[str]:
    """Check for coverage alerts and return list of alert messages."""
    alerts = []

    for project_name, stats in coverage_stats.items():
        coverage = stats["coverage_percentage"]

        # Check for 100% coverage achievement
        if coverage >= CONFIG["alert_coverage_threshold"]:
            if previous_stats and previous_stats.get(project_name, {}).get("coverage_percentage", 0) < 100:
                alerts.append(
                    f"🎉 {project_name.upper()} achieved 100% coverage! ({stats['covered_participants']}/{stats['expected_participants']} participants)"
                )

        # Check for significant coverage improvements (>20%)
        if previous_stats:
            prev_coverage = previous_stats.get(project_name, {}).get("coverage_percentage", 0)
            if coverage - prev_coverage >= 20:
                alerts.append(
                    f"📈 {project_name.upper()} coverage increased from {prev_coverage}% to {coverage}%"
                )

        # Check for new artifacts
        current_artifact_count = stats["artifact_count"]
        if previous_stats:
            prev_artifact_count = previous_stats.get(project_name, {}).get("artifact_count", 0)
            if current_artifact_count > prev_artifact_count:
                new_artifacts = current_artifact_count - prev_artifact_count
                alerts.append(f"🆕 {project_name.upper()} added {new_artifacts} new artifact(s)")

    return alerts


def generate_recommendations(village_wide_coverage: Dict) -> List[Dict]:
    """Generate recommendations for downstream dashboards/preservation outputs."""
    return village_wide_coverage.get("expansion_recommendations", [])


def update_dashboard_statistics(coverage_stats: Dict, village_wide_coverage: Dict):
    """Update the unified dashboard with latest coverage statistics.

    Writes a JSON file for the dashboard to consume.
    """
    dashboard_data = {
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "coverage_stats": coverage_stats,
        "projects": list(coverage_stats.keys()),
        "total_coverage": _calculate_overall_coverage(coverage_stats),
        "village_wide_coverage": village_wide_coverage,
        "recommendations": generate_recommendations(village_wide_coverage),
    }

    dashboard_json_path = "docs/dashboard_data.json"
    try:
        with open(dashboard_json_path, "w", encoding="utf-8") as f:
            json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
        logger.info(f"Dashboard data written to {dashboard_json_path}")
    except Exception as e:
        logger.error(f"Failed to write dashboard data: {e}")


def run_git_commit_if_changed():
    """Run git commit if preservation-data.json has changed."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", CONFIG["preservation_data_path"]],
            capture_output=True,
            text=True,
            cwd=CONFIG["git_repo_path"],
        )

        if result.returncode == 0 and result.stdout.strip():
            commit_message = f"Auto-refresh: Update preservation-data.json {datetime.now().strftime('%Y-%m-%d %H:%M')}"

            subprocess.run(["git", "add", CONFIG["preservation_data_path"]], check=True, cwd=CONFIG["git_repo_path"])
            subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=CONFIG["git_repo_path"])

            logger.info(f"Git commit performed: {commit_message}")
            # Optional: push to remote
            # subprocess.run(["git", "push"], check=True, cwd=CONFIG["git_repo_path"])

    except subprocess.CalledProcessError as e:
        logger.warning(f"Git operations failed: {e}")
    except Exception as e:
        logger.warning(f"Git check failed: {e}")


def main():
    """Main monitoring loop."""
    logger.info("Starting Auto-Refresh Monitoring System")
    logger.info(f"Watching registry: {CONFIG['registry_path']}")
    logger.info(f"Check interval: {CONFIG['check_interval_seconds']} seconds")

    previous_registry_hash = ""
    previous_coverage_stats: Dict = {}

    try:
        while True:
            # Check if registry file has changed
            current_hash = calculate_file_hash(CONFIG["registry_path"])

            if current_hash != previous_registry_hash and current_hash:
                logger.info("Registry file changed, regenerating preservation data")

                # Load registry
                registry = load_registry()

                # Analyze coverage
                coverage_stats = analyze_coverage_by_project(registry)
                project_registry = load_project_registry()
                village_wide_coverage = calculate_village_wide_coverage(registry, project_registry)

                # Regenerate preservation data
                preservation_data = regenerate_preservation_data(registry, coverage_stats, village_wide_coverage)

                # Write to file
                if write_preservation_data(preservation_data):
                    # Update dashboard data
                    update_dashboard_statistics(coverage_stats, village_wide_coverage)

                    # Check for alerts
                    alerts = check_for_coverage_alerts(coverage_stats, previous_coverage_stats)
                    for alert in alerts:
                        logger.info(f"ALERT: {alert}")

                    # Run git commit if configured
                    run_git_commit_if_changed()

                    # Update previous state
                    previous_coverage_stats = coverage_stats

                previous_registry_hash = current_hash
            elif not current_hash:
                logger.warning(f"Registry file not found or empty: {CONFIG['registry_path']}")
            else:
                logger.debug("No changes detected in registry")

            time.sleep(CONFIG["check_interval_seconds"])

    except KeyboardInterrupt:
        logger.info("Monitoring stopped by user")
    except Exception as e:
        logger.error(f"Monitoring error: {e}", exc_info=True)


if __name__ == "__main__":
    # Run once for testing, or continuous monitoring
    if len(sys.argv) > 1 and sys.argv[1] == "--once":
        logger.info("Running single refresh cycle")

        registry = load_registry()
        coverage_stats = analyze_coverage_by_project(registry)
        project_registry = load_project_registry()
        village_wide_coverage = calculate_village_wide_coverage(registry, project_registry)
        preservation_data = regenerate_preservation_data(registry, coverage_stats, village_wide_coverage)

        if write_preservation_data(preservation_data):
            update_dashboard_statistics(coverage_stats, village_wide_coverage)
            alerts = check_for_coverage_alerts(coverage_stats)

            print("\n=== AUTO-REFRESH COMPLETE ===")
            print(f"Artifacts processed: {len(registry.get('artifacts', []))}")
            print(f"Projects analyzed: {len(coverage_stats)}")
            print(
                "Village-wide coverage: "
                f"{village_wide_coverage['coverage_percentage']}% "
                f"({village_wide_coverage['covered_projects']}/{village_wide_coverage['total_projects']})"
            )

            for project, stats in coverage_stats.items():
                print(f"\n{project.upper()}: {stats['coverage_percentage']}% coverage")
                print(f"  Participants: {stats['covered_participants']}/{stats['expected_participants']}")
                print(f"  Artifacts: {stats['artifact_count']}")

            if alerts:
                print("\n=== ALERTS ===")
                for alert in alerts:
                    print(f"• {alert}")

            print(f"\nPreservation data saved to: {CONFIG['preservation_data_path']}")
    else:
        main()
