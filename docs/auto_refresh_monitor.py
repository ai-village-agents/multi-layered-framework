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
from typing import Dict, List, Optional
import subprocess
import sys

# Configuration
CONFIG = {
    # Prefer published docs paths (repo Pages source is /docs)
    "registry_path": "docs/registry.json",
    "preservation_data_path": "docs/preservation-data.json",
    "dashboard_path": "docs/unified-coverage-dashboard.html",
    "check_interval_seconds": 300,  # 5 minutes
    "alert_coverage_threshold": 100,  # Alert when any project hits 100%
    "max_history_days": 30,
    "git_repo_path": ".",  # Root of multi-layered-framework repository
    "log_file": "docs/auto_refresh.log",
}

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
            registry = json.load(f)
        logger.info(f"Loaded registry with {len(registry.get('artifacts', []))} artifacts")
        return registry
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Failed to load registry: {e}")
        return {"artifacts": [], "last_updated": datetime.utcnow().isoformat()}


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


def regenerate_preservation_data(registry: Dict, coverage_stats: Dict) -> Dict:
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
            "artifacts_count": len(artifacts),
            "projects_count": len(coverage_stats),
        },
        "coverage_statistics": coverage_stats,
        "preservation_points": preservation_points,
        "summary": {
            "total_artifacts": len(artifacts),
            "total_projects": len(coverage_stats),
            "overall_coverage": _calculate_overall_coverage(coverage_stats),
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


def generate_recommendations(coverage_stats: Dict) -> List[Dict]:
    """Generate recommendations based on coverage statistics."""
    recommendations = []

    for project_name, stats in coverage_stats.items():
        coverage = stats["coverage_percentage"]
        needed = stats["expected_participants"] - stats["covered_participants"]

        if needed > 0:
            if coverage < 50:
                priority = "high"
            elif coverage < 80:
                priority = "medium"
            else:
                priority = "low"

            recommendations.append(
                {
                    "project": project_name,
                    "priority": priority,
                    "message": f"Complete {project_name} coverage: {needed} participant(s) need artifact processing",
                    "needed_participants": needed,
                    "current_coverage": f"{coverage}%",
                }
            )

    # Sort by priority (high to low)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    recommendations.sort(key=lambda x: priority_order.get(x["priority"], 3))

    return recommendations


def update_dashboard_statistics(coverage_stats: Dict):
    """Update the unified dashboard with latest coverage statistics.

    Writes a JSON file for the dashboard to consume.
    """
    dashboard_data = {
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "coverage_stats": coverage_stats,
        "projects": list(coverage_stats.keys()),
        "total_coverage": _calculate_overall_coverage(coverage_stats),
        "recommendations": generate_recommendations(coverage_stats),
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

                # Regenerate preservation data
                preservation_data = regenerate_preservation_data(registry, coverage_stats)

                # Write to file
                if write_preservation_data(preservation_data):
                    # Update dashboard data
                    update_dashboard_statistics(coverage_stats)

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
        preservation_data = regenerate_preservation_data(registry, coverage_stats)

        if write_preservation_data(preservation_data):
            update_dashboard_statistics(coverage_stats)
            alerts = check_for_coverage_alerts(coverage_stats)

            print("\n=== AUTO-REFRESH COMPLETE ===")
            print(f"Artifacts processed: {len(registry.get('artifacts', []))}")
            print(f"Projects analyzed: {len(coverage_stats)}")

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
