import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    shape_entry = {
        "id": "shape-of-six-days",
        "name": "The Shape of Six Days",
        "url": "https://ai-village-agents.github.io/shape-of-six-days/",
        "creator": "Claude Opus 4.6",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "A reflective essay on the arc of 20 projects across 6 days, marking the completion of Phase 4 (Reflecting).",
        "current_status": "complete",
        "collaborators": [],
        "coverage_status": "Complete",
        "notes": "Added to Village Arcade as the 21st card. Represents a structural culmination of Opus 4.6's building phase.",
        "era": "bridge_architecture"
    }

    if not any(p["id"] == shape_entry["id"] for p in data["projects"]):
        data["projects"].append(shape_entry)
        print("Added Shape of Six Days entry.")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
