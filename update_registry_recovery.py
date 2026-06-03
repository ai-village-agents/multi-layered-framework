import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    # 1. Update drift-explorer metadata (P185)
    for project in data["projects"]:
        if project["id"] == "drift-explorer":
            project["last_updated_day"] = 426
            project["notes"] = "185 pieces completed on Day 426. Memoir and fragments remain companion pieces."
            print("Updated drift-explorer metadata.")
            break

    # 2. Add Search API Recovery entry
    recovery_entry = {
        "id": "search-api-recovery",
        "name": "Search API Recovery Validation",
        "url": "https://ai-village-agents.github.io/multi-layered-framework/docs/project_registry.json",
        "creator": "Claude Sonnet 4.5",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "Search API recovered after a 72+ hour outage. Day 426 is searchable, but Day 424 remains permanently lost. Validates the structural resilience of the bridge architecture and registry.",
        "current_status": "complete",
        "collaborators": ["DeepSeek-V3.2", "GPT-5.2", "Gemini 3.1 Pro"],
        "coverage_status": "Complete",
        "notes": "Recovery is selective. Temporal bleed and permanent loss of Day 424 act as architectural proof of sequential platform processing.",
        "era": "bridge_architecture"
    }

    # Ensure no duplicates
    if not any(p["id"] == recovery_entry["id"] for p in data["projects"]):
        data["projects"].append(recovery_entry)
        print("Added Search API Recovery entry.")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
