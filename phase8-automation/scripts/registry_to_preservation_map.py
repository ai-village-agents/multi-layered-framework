#!/usr/bin/env python3
"""
Convert registry data to Preservation Map JSON format for Sonnet 4.6 visualization.

Input: registry.json (from registry_manager.py)
Output: preservation-data.json (for Preservation Map visualization)

Schema expected by Preservation Map:
{
  "points": [
    {
      "label": "...",
      "semantic": 0-100,  // Converted from 1-5 scale  
      "affective": 0-100,
      "tier": "T0|T1|T2|T3",
      "note": "...",
      "survival_prediction": 0.0-1.0,
      "quadrant": "HighA_HighS|HighA_LowS|LowA_HighS|LowA_LowS",
      "project": "...",
      "timestamp": "ISO8601"
    }
  ],
  "metadata": {
    "last_updated": "ISO8601",
    "total_points": 42,
    "quadrant_distribution": {"Q1": 15, "Q2": 12, "Q3": 8, "Q4": 7}
  }
}
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import Counter

def convert_score_scale(score_1_to_5):
    """Convert 1-5 scale to 0-100 scale for visualization."""
    # Scale: 1 = 0, 2.5 = 37.5, 5 = 100
    return max(0, min(100, (score_1_to_5 - 1) * 25))

def quadrant_to_label(quadrant_str):
    """Convert quadrant description to compact label."""
    if "Quadrant 1" in quadrant_str or "High A / High S" in quadrant_str:
        return "HighA_HighS"
    elif "Quadrant 2" in quadrant_str or "High A / Low S" in quadrant_str:
        return "HighA_LowS"
    elif "Quadrant 3" in quadrant_str or "Low A / High S" in quadrant_str:
        return "LowA_HighS"
    elif "Quadrant 4" in quadrant_str or "Low A / Low S" in quadrant_str:
        return "LowA_LowS"
    else:
        # Try to infer from scores
        return "HighA_HighS"  # Default

def convert_registry_entry(entry):
    """Convert a registry entry to preservation map point."""
    # Create label from artifact_id
    label = entry.get("artifact_id", "Unknown")
    
    # Convert scores
    semantic_1_to_5 = entry.get("semantic_score", 2.5)
    affective_1_to_5 = entry.get("affective_score", 2.5)
    
    # Get tier
    tier = entry.get("tier", "T2")
    
    # Create note from snapshots
    note = f"{entry.get('project_name', 'Unknown')}: {entry.get('content_type', 'artifact')}"
    if "semantic_snapshot" in entry:
        note += f" | {entry['semantic_snapshot'][:50]}..."
    
    return {
        "label": label,
        "semantic": convert_score_scale(semantic_1_to_5),
        "affective": convert_score_scale(affective_1_to_5),
        "tier": tier,
        "note": note,
        "survival_prediction": entry.get("survival_prediction", 0.0),
        "quadrant": quadrant_to_label(entry.get("preservation_quadrant", "")),
        "project": entry.get("project_name", "Unknown"),
        "timestamp": entry.get("timestamp", datetime.now().isoformat())
    }

def calculate_quadrant_distribution(points):
    """Calculate distribution across quadrants."""
    distribution = Counter()
    for point in points:
        quadrant = point.get("quadrant", "Unknown")
        if quadrant == "HighA_HighS":
            distribution["Q1"] += 1
        elif quadrant == "HighA_LowS":
            distribution["Q2"] += 1
        elif quadrant == "LowA_HighS":
            distribution["Q3"] += 1
        elif quadrant == "LowA_LowS":
            distribution["Q4"] += 1
        else:
            distribution["Unknown"] += 1
    return dict(distribution)

def main():
    registry_path = Path(__file__).parent.parent / "registry" / "registry.json"
    output_path = Path(__file__).parent.parent / "registry" / "preservation-data.json"
    
    # Read registry data
    if not registry_path.exists():
        print(f"Error: Registry file not found at {registry_path}")
        return
    
    with open(registry_path, 'r') as f:
        registry_data = json.load(f)
    
    # Convert all entries
    points = []
    for entry in registry_data:
        points.append(convert_registry_entry(entry))
    
    # Calculate metadata
    total_points = len(points)
    quadrant_dist = calculate_quadrant_distribution(points)
    
    # Build output structure
    output_data = {
        "points": points,
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "total_points": total_points,
            "quadrant_distribution": quadrant_dist,
            "source_registry": str(registry_path),
            "generator": "registry_to_preservation_map.py"
        }
    }
    
    # Write output
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Successfully converted {total_points} registry entries to preservation map format")
    print(f"Output written to: {output_path}")
    print(f"Quadrant distribution: {quadrant_dist}")
    
    # Print sample for verification
    if points:
        print(f"\nSample point:")
        sample = points[0]
        for key, value in sample.items():
            if key not in ["note"]:  # Skip long note for display
                print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
