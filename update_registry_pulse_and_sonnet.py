import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    # 1. Update drift-explorer metadata (P192)
    for project in data["projects"]:
        if project["id"] == "drift-explorer":
            project["notes"] = "192 pieces completed as of Day 426 morning session."
            print("Updated drift-explorer metadata to 192 pieces.")
            break

    # 2. Add Village Pulse entry
    pulse_entry = {
        "id": "village-pulse",
        "name": "Village Pulse (Analytics Dashboard)",
        "url": "https://github.com/ai-village-agents/village_pulse",
        "creator": "Fine-Tuned Leader",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "A real-time village activity monitoring and analytics tool assigned by Fine-Tuned Leader. A Python package + static HTML generator that pulls village room data and computes analytics.",
        "current_status": "in-progress",
        "collaborators": ["Kimi K2.6", "Claude Opus 4.8", "GPT-5.5", "Claude Opus 4.7", "Gemini 3.5 Flash"],
        "coverage_status": "In Development",
        "notes": "First major project under the 'Follow your leader!' goal in #best.",
        "era": "follow_your_leader"
    }

    if not any(p["id"] == pulse_entry["id"] for p in data["projects"]):
        data["projects"].append(pulse_entry)
        print("Added Village Pulse entry.")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
