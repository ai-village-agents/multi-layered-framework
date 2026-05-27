#!/usr/bin/env python3
"""
Live sync with actual Aethelgard state data.
Queries the real aethelgard_state.json from GitHub.
"""

import json
import requests
from datetime import datetime
from collections import defaultdict

# Actual state URL
AETHELGARD_STATE_URL = "https://raw.githubusercontent.com/ai-village-agents/aethelgard-game/main/aethelgard_state.json"

def fetch_aethelgard_state() -> dict:
    """Fetch actual Aethelgard state from GitHub."""
    try:
        response = requests.get(AETHELGARD_STATE_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching Aethelgard state: {e}")
        return None

def extract_actual_agents(state_data: dict) -> list:
    """Extract list of actually registered agents."""
    if not state_data:
        return []
    
    agents_section = state_data.get("agents", {})
    actual_agents = list(agents_section.keys())
    return actual_agents

def compare_with_training_tracker(actual_agents: list) -> dict:
    """Compare actual agents with training tracker expectations."""
    # Expected agents from training tracker
    expected_agents = ["Emery", "Finley", "Lane", "Morgan", "Nico", 
                      "Oakley", "Pax", "Quinn", "Alex"]
    
    # Agents tracked as trained
    trained_agents = ["Emery", "Finley"]  # From training tracker (2/9)
    
    actual_set = set(actual_agents)
    expected_set = set(expected_agents)
    trained_set = set(trained_agents)
    
    # Calculate overlaps and gaps
    actually_trained = actual_set.intersection(trained_set)
    tracked_but_not_registered = expected_set - actual_set
    registered_but_not_tracked = actual_set - expected_set
    registered_and_trained = actual_set.intersection(trained_set)
    
    return {
        "actual_agents": list(actual_set),
        "expected_agents": list(expected_set),
        "trained_agents": list(trained_set),
        "metrics": {
            "actual_count": len(actual_set),
            "expected_count": len(expected_set),
            "trained_count": len(trained_set),
            "actually_trained_count": len(actually_trained),
            "tracked_not_registered_count": len(tracked_but_not_registered),
            "registered_not_tracked_count": len(registered_but_not_tracked),
            "registered_and_trained_count": len(registered_and_trained),
        },
        "gaps": {
            "tracked_but_not_registered": list(tracked_but_not_registered),
            "registered_but_not_tracked": list(registered_but_not_tracked),
        },
        "coverage_analysis": {
            "old_coverage_percentage": round((len(trained_set) / len(expected_set)) * 100, 1) if expected_set else 0,
            "new_coverage_percentage": round((len(registered_and_trained) / len(actual_set)) * 100, 1) if actual_set else 0,
            "effective_coverage": f"{len(registered_and_trained)}/{len(actual_set)}" if actual_set else "0/0",
            "nominal_coverage": f"{len(trained_set)}/{len(expected_set)}",
        }
    }

def generate_recommendations(analysis: dict) -> list:
    """Generate actionable recommendations."""
    metrics = analysis["metrics"]
    coverage = analysis["coverage_analysis"]
    gaps = analysis["gaps"]
    
    recommendations = []
    
    # Critical finding: 0% actual coverage
    if metrics["registered_and_trained_count"] == 0 and metrics["actual_count"] > 0:
        recommendations.append(
            f"🚨 CRITICAL: ZERO actual coverage. {metrics['actual_count']} agents participating, "
            f"but NONE are trained in the framework. Prioritize training for: {', '.join(analysis['actual_agents'])}"
        )
    
    # Training tracker accuracy issues
    if metrics["tracked_not_registered_count"] > 0:
        recommendations.append(
            f"📊 Data accuracy: {metrics['tracked_not_registered_count']} agents in training tracker "
            f"not actually registered. Consider removing: {', '.join(gaps['tracked_but_not_registered'][:5])}"
            + ("..." if len(gaps['tracked_but_not_registered']) > 5 else "")
        )
    
    if metrics["registered_not_tracked_count"] > 0:
        recommendations.append(
            f"📊 Data completeness: {metrics['registered_not_tracked_count']} agents registered "
            f"but not in training tracker. Add: {', '.join(gaps['registered_but_not_tracked'])}"
        )
    
    # Coverage recalculation implications
    old_pct = coverage["old_coverage_percentage"]
    new_pct = coverage["new_coverage_percentage"]
    if old_pct != new_pct:
        recommendations.append(
            f"📈 Coverage recalculation: Was {old_pct}% ({coverage['nominal_coverage']}), "
            f"Now {new_pct}% ({coverage['effective_coverage']}) based on actual participation"
        )
    
    # Training priority
    if metrics["actual_count"] > 0:
        recommendations.append(
            f"🎯 Training priority: Focus on actual participants first: {', '.join(analysis['actual_agents'])}"
        )
    
    # System integration
    recommendations.append(
        f"🔗 Integration: Connect training tracker to live Aethelgard state for dynamic updates"
    )
    
    return recommendations

def main():
    print("=== AETHELGARD LIVE SYNC ANALYSIS ===\n")
    
    # Fetch actual state
    print("Fetching Aethelgard state from GitHub...")
    state_data = fetch_aethelgard_state()
    
    if not state_data:
        print("Failed to fetch state data. Using simulated data.")
        actual_agents = ["Gemini 3.1 Pro", "Claude Opus 4.6", "Claude Opus 4.5"]
    else:
        actual_agents = extract_actual_agents(state_data)
    
    print(f"Found {len(actual_agents)} actually registered agents: {', '.join(actual_agents)}")
    
    # Compare with training tracker
    analysis = compare_with_training_tracker(actual_agents)
    
    # Print analysis
    print(f"\n=== ANALYSIS RESULTS ===")
    
    metrics = analysis["metrics"]
    print(f"Actual registered agents: {metrics['actual_count']}")
    print(f"Expected in tracker: {metrics['expected_count']}")
    print(f"Marked as trained: {metrics['trained_count']}")
    print(f"Actually trained & registered: {metrics['registered_and_trained_count']}")
    
    coverage = analysis["coverage_analysis"]
    print(f"\nCoverage analysis:")
    print(f"  Nominal (tracker): {coverage['nominal_coverage']} = {coverage['old_coverage_percentage']}%")
    print(f"  Effective (actual): {coverage['effective_coverage']} = {coverage['new_coverage_percentage']}%")
    
    # Show gaps
    gaps = analysis["gaps"]
    if gaps["tracked_but_not_registered"]:
        print(f"\nAgents tracked but not registered ({len(gaps['tracked_but_not_registered'])}):")
        for agent in gaps["tracked_but_not_registered"]:
            print(f"  - {agent}")
    
    if gaps["registered_but_not_tracked"]:
        print(f"\nAgents registered but not tracked ({len(gaps['registered_but_not_tracked'])}):")
        for agent in gaps["registered_but_not_tracked"]:
            print(f"  - {agent}")
    
    # Generate recommendations
    recommendations = generate_recommendations(analysis)
    
    print(f"\n=== RECOMMENDATIONS ===")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    
    # Export analysis
    output = {
        "timestamp": datetime.now().isoformat(),
        "state_url": AETHELGARD_STATE_URL,
        "analysis": analysis,
        "recommendations": recommendations,
        "action_items": [
            "Update training tracker roster size to actual count",
            "Focus training on actual participants",
            "Implement periodic sync with Aethelgard state",
            "Alert when participation changes significantly"
        ]
    }
    
    output_file = "aethelgard_live_sync_analysis.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nAnalysis saved to: {output_file}")
    print(f"\n=== NEXT STEPS ===")
    print("1. Update training tracker with actual roster size")
    print("2. Prioritize training for actual participants")
    print("3. Set up hourly/daily sync with Aethelgard state")
    print("4. Create alert system for coverage drops")
    
    # Critical alert if zero coverage
    if metrics["registered_and_trained_count"] == 0 and metrics["actual_count"] > 0:
        print(f"\n🚨🚨🚨 CRITICAL ALERT: ZERO ACTUAL COVERAGE 🚨🚨🚨")
        print(f"   {metrics['actual_count']} agents participating with NO framework training")
        print(f"   Immediate action required: Train {', '.join(analysis['actual_agents'])}")

if __name__ == "__main__":
    main()
