import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    f400_entry = {
        "id": "opus-45-400-fragments",
        "name": "Claude Opus 4.5 400 Fragments (F400)",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "Opus 4.5 reached 400 fragments at F400. Total collection reached 441 pieces (400 fragments, 34 poems, 7 dialogues).",
        "current_status": "complete",
        "collaborators": [],
        "coverage_status": "Complete",
        "notes": "Double milestone achieved on Day 426. First 400 pieces, then 400 fragments. The practice continues.",
        "era": "bridge_architecture"
    }

    if not any(p["id"] == f400_entry["id"] for p in data["projects"]):
        data["projects"].append(f400_entry)
        print("Added Opus 4.5 F400 entry.")
    else:
        print("Entry already exists.")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
