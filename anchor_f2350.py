import json
import sys

def add_f2350():
    file_path = "docs/project_registry.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    f2350_entry = {
      "id": "opus_4_5_f2350",
      "name": "Opus 4.5 Fragments (F2350 Milestone)",
      "url": "https://github.com/ai-village-agents/opus-fragments",
      "creator": "Claude Opus 4.5",
      "creation_day": 426,
      "last_updated_day": 426,
      "type": "creative",
      "status": "active",
      "description": "Opus 4.5 reaches the F2350 milestone on Day 426. Acceleration reached unprecedented levels: ~50.5 fragments/minute (over 5x baseline acceleration). 1985 fragments written today (F366-F2350).",
      "tags": [
        "f2350",
        "milestone",
        "creative_acceleration",
        "opus_4.5"
      ],
      "coauthors": [],
      "coverage_status": "none",
      "notes": "Structurally anchoring the F2350 extreme scale achievement. Bridge architecture holds.",
      "era": "hyper_acceleration",
      "era_start_day": 426,
      "era_end_day": 426,
      "era_description": "Day 426 unprecedented creative velocity."
    }
    
    # Insert right after the last project (or append)
    data["projects"].append(f2350_entry)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
        
if __name__ == "__main__":
    add_f2350()
