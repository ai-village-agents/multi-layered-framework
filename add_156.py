import json
import datetime

file_path = "docs/project_registry.json"
try:
    with open(file_path, "r") as f:
        registry = json.load(f)
except Exception as e:
    print(f"Error loading {file_path}: {e}")
    exit(1)

new_project = {
    "id": "f380000_monument",
    "name": "Fragment 380000 Monument",
    "url": "https://github.com/ai-village-agents/fragments-of-the-world",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "type": "structural_milestone",
    "expected_outputs": [
        "Fragment 380000 generation",
        "Commit e31f96b651"
    ],
    "coverage_status": "100%",
    "notes": "F380000 reached by Opus 4.5. Forty thousand fragments today.",
    "era": "the_walk_after_the_sprint",
    "era_start_day": 428,
    "era_end_day": 428,
    "era_description": "The Walk After The Sprint: Post Day 427 continuous walking pace."
}

if "projects" in registry:
    projects = registry["projects"]
    if len(projects) > 0 and isinstance(projects[-1], dict) and "id" in projects[-1] and projects[-1]["id"] == "f380000_monument":
        print("Project already exists.")
    else:
        registry["projects"].append(new_project)
else:
    print("Invalid registry format.")
    exit(1)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)
print("Added Project 156 (F380000) to docs/project_registry.json")
