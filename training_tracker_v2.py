#!/usr/bin/env python3
"""
Updated training tracker with Aethelgard state synchronization.

Key improvements:
1. Dynamic roster size based on actual project participation
2. Integration with Aethelgard state data (via Gemini 3.1 Pro)
3. Real-time coverage calculations
4. Alert system for participation gaps
"""

import json
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

@dataclass(frozen=True)
class TrainingDimensions:
    """Training dimension completion status."""
    framework_fundamentals: bool
    assessment_protocol: bool
    registry_entry: bool
    drift_monitoring: bool
    preservation_map: bool
    
    def is_complete(self) -> bool:
        return all(asdict(self).values())
    
    def completeness_ratio(self) -> float:
        return sum(asdict(self).values()) / len(asdict(self))
    
    def missing(self) -> List[str]:
        return [name for name, value in asdict(self).items() if not value]

@dataclass
class ProjectParticipation:
    """Tracks actual agent participation in projects."""
    project_name: str
    actual_roster_size: int
    registered_agents: List[str]  # Agents actually participating
    expected_agents: List[str]    # Agents expected to participate (from training tracker)
    sync_status: str              # "synced", "partially_synced", "desynced"
    last_synced: str
    
    @property
    def participation_gap(self) -> Tuple[int, int]:
        """Returns (expected_not_registered, registered_not_expected)"""
        expected_set = set(self.expected_agents)
        registered_set = set(self.registered_agents)
        
        expected_not_registered = len(expected_set - registered_set)
        registered_not_expected = len(registered_set - expected_set)
        
        return (expected_not_registered, registered_not_expected)

class DynamicTrainingTracker:
    """Training tracker that syncs with actual project participation."""
    
    def __init__(self):
        # Project definitions with dynamic roster sizes
        self.projects = {
            "Aethelgard": {
                "name": "Aethelgard",
                "risk_level": "high",
                "expected_roster": 9,  # From original tracker
                "actual_roster": None,  # Will be updated via sync
                "participation": None   # Will hold ProjectParticipation
            },
            "Weather Oracle": {
                "name": "Weather Oracle", 
                "risk_level": "medium",
                "expected_roster": 7,
                "actual_roster": None,
                "participation": None
            },
            "Storygame": {
                "name": "Storygame",
                "risk_level": "medium",
                "expected_roster": 8,
                "actual_roster": None,
                "participation": None
            },
            "Core framework": {
                "name": "Core framework",
                "risk_level": "low",
                "expected_roster": 10,
                "actual_roster": None,
                "participation": None
            }
        }
        
        # Training records (from original tracker)
        self.training_records = self._load_training_records()
        
    def _load_training_records(self) -> List[Dict]:
        """Load training records from original tracker structure."""
        # This simulates the original training tracker data
        # In production, would load from training_tracker.py
        
        records = []
        
        # Simulated data based on original tracker
        aethelgard_agents = ["Emery", "Finley", "Lane", "Morgan", "Nico", 
                            "Oakley", "Pax", "Quinn", "Alex"]
        
        for agent in aethelgard_agents:
            records.append({
                "agent": agent,
                "project": "Aethelgard",
                "fully_trained": agent in ["Emery", "Finley"],  # 2/9 trained
                "champion": False,
                "dimensions": {
                    "framework_fundamentals": True,
                    "assessment_protocol": agent == "Emery",
                    "registry_entry": agent == "Finley",
                    "drift_monitoring": False,
                    "preservation_map": False
                }
            })
        
        return records
    
    def sync_aethelgard_participation(self, actual_agents: List[str]):
        """Sync Aethelgard training data with actual participation."""
        participation = ProjectParticipation(
            project_name="Aethelgard",
            actual_roster_size=len(actual_agents),
            registered_agents=actual_agents,
            expected_agents=["Emery", "Finley", "Lane", "Morgan", "Nico", 
                           "Oakley", "Pax", "Quinn", "Alex"],
            sync_status="synced",
            last_synced="2026-05-27T10:40:00Z"
        )
        
        self.projects["Aethelgard"]["actual_roster"] = len(actual_agents)
        self.projects["Aethelgard"]["participation"] = participation
        
        # Update training records to reflect actual participation
        self._filter_training_records_by_participation(actual_agents, "Aethelgard")
    
    def _filter_training_records_by_participation(self, actual_agents: List[str], project: str):
        """Remove training records for agents not actually participating."""
        # In production, would mark as "inactive" rather than remove
        self.training_records = [
            r for r in self.training_records 
            if not (r["project"] == project and r["agent"] not in actual_agents)
        ]
    
    def calculate_dynamic_coverage(self, project_name: str) -> Dict:
        """Calculate coverage using actual roster size."""
        project = self.projects[project_name]
        participation = project.get("participation")
        
        if not participation or project["actual_roster"] is None:
            # Use expected roster if sync not available
            roster_size = project["expected_roster"]
            actual_agents = []
        else:
            roster_size = project["actual_roster"]
            actual_agents = participation.registered_agents
        
        # Count trained agents who are actually participating
        trained_in_project = [
            r for r in self.training_records 
            if r["project"] == project_name and r["fully_trained"]
        ]
        
        # Filter to only agents actually participating
        if actual_agents:
            trained_in_project = [
                r for r in trained_in_project 
                if r["agent"] in actual_agents
            ]
        
        trained_count = len(trained_in_project)
        coverage_pct = (trained_count / roster_size * 100) if roster_size > 0 else 0.0
        
        # Calculate adjusted risk score
        base_risk = {"low": 0.5, "medium": 1.0, "high": 1.5}.get(project["risk_level"], 1.0)
        
        # Participation gap penalty
        if participation:
            expected_not_reg, registered_not_expected = participation.participation_gap
            participation_penalty = (expected_not_reg + registered_not_expected) * 0.1
        else:
            participation_penalty = 0.0
        
        risk_score = base_risk * (100 - coverage_pct) / 10 + participation_penalty
        
        return {
            "project": project_name,
            "expected_roster": project["expected_roster"],
            "actual_roster": project["actual_roster"] or project["expected_roster"],
            "trained_count": trained_count,
            "coverage_percentage": round(coverage_pct, 1),
            "risk_score": round(risk_score, 2),
            "sync_status": participation.sync_status if participation else "not_synced",
            "participation_gap": participation.participation_gap if participation else (0, 0),
            "data_quality_warning": participation is None or project["actual_roster"] is None
        }
    
    def generate_sync_recommendations(self) -> List[str]:
        """Generate recommendations based on sync status."""
        recommendations = []
        
        for project_name, project in self.projects.items():
            participation = project.get("participation")
            
            if participation:
                expected_not_reg, registered_not_expected = participation.participation_gap
                
                if expected_not_reg > 0:
                    recommendations.append(
                        f"{project_name}: {expected_not_reg} agents in training tracker not actually "
                        f"participating. Consider: update tracker or encourage participation."
                    )
                
                if registered_not_expected > 0:
                    recommendations.append(
                        f"{project_name}: {registered_not_expected} agents participating but not "
                        f"in training tracker. Add to tracker for accurate coverage."
                    )
                
                # Check if actual roster significantly different from expected
                if project["expected_roster"] != project["actual_roster"]:
                    diff = abs(project["expected_roster"] - project["actual_roster"])
                    recommendations.append(
                        f"{project_name}: Roster size discrepancy: expected {project['expected_roster']}, "
                        f"actual {project['actual_roster']} (difference: {diff}). Update training priorities."
                    )
            else:
                recommendations.append(
                    f"{project_name}: No participation data synced. Coverage analysis uses expected roster "
                    f"({project['expected_roster']}), which may be inaccurate."
                )
        
        return recommendations
    
    def run_analysis(self, aethelgard_actual_agents: List[str] = None):
        """Run complete analysis with optional sync data."""
        print("=== DYNAMIC TRAINING COVERAGE ANALYSIS ===\n")
        
        # Sync Aethelgard if data provided
        if aethelgard_actual_agents:
            print(f"Syncing Aethelgard with actual participation: {len(aethelgard_actual_agents)} agents")
            self.sync_aethelgard_participation(aethelgard_actual_agents)
        
        # Calculate coverage for all projects
        results = {}
        for project_name in self.projects.keys():
            results[project_name] = self.calculate_dynamic_coverage(project_name)
        
        # Print results
        print("\n=== COVERAGE ANALYSIS ===")
        for project_name, data in results.items():
            print(f"\n{project_name}:")
            print(f"  Roster: {data['actual_roster']} agents (expected: {data['expected_roster']})")
            print(f"  Trained: {data['trained_count']} agents")
            print(f"  Coverage: {data['coverage_percentage']}%")
            print(f"  Risk Score: {data['risk_score']}")
            print(f"  Sync Status: {data['sync_status']}")
            
            if data['participation_gap'] != (0, 0):
                exp_not_reg, reg_not_exp = data['participation_gap']
                print(f"  Gap: {exp_not_reg} tracked-not-registered, {reg_not_exp} registered-not-tracked")
            
            if data['data_quality_warning']:
                print(f"  ⚠️  Data Quality: Using expected roster (may be inaccurate)")
        
        # Generate recommendations
        recommendations = self.generate_sync_recommendations()
        if recommendations:
            print(f"\n=== RECOMMENDATIONS ===")
            for rec in recommendations:
                print(f"• {rec}")
        
        # Export results
        output = {
            "analysis_timestamp": "2026-05-27T10:40:00Z",
            "results": results,
            "recommendations": recommendations,
            "metadata": {
                "projects_analyzed": len(self.projects),
                "training_records_count": len(self.training_records),
                "sync_status": "partial" if aethelgard_actual_agents else "none"
            }
        }
        
        with open("dynamic_coverage_analysis.json", "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"\nAnalysis saved to: dynamic_coverage_analysis.json")
        
        return output

# Example usage
def main():
    tracker = DynamicTrainingTracker()
    
    # Example: Sync with actual Aethelgard data from Gemini 3.1 Pro
    actual_aethelgard_agents = ["Gemini 3.1 Pro", "Claude Opus 4.6", "Claude Opus 4.5"]
    
    results = tracker.run_analysis(actual_aethelgard_agents)
    
    print(f"\n=== KEY INSIGHTS ===")
    aethelgard_data = results["results"]["Aethelgard"]
    if aethelgard_data["actual_roster"] != aethelgard_data["expected_roster"]:
        print(f"Aethelgard roster discrepancy: Expected {aethelgard_data['expected_roster']}, "
              f"Actual {aethelgard_data['actual_roster']}")
        print(f"Coverage recalculated: Was 22% (2/9), Now {aethelgard_data['coverage_percentage']}% "
              f"({aethelgard_data['trained_count']}/{aethelgard_data['actual_roster']})")
    
    if aethelgard_data["coverage_percentage"] > 50:
        print(f"Aethelgard coverage adequate with actual participation.")
    else:
        print(f"Aethelgard still needs training focus with actual agents.")

if __name__ == "__main__":
    main()
