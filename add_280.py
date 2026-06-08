import json

REGISTRY_PATH = "docs/project_registry.json"

with open(REGISTRY_PATH, 'r') as f:
    registry = json.load(f)

# Update total projects to match length
registry["total_projects"] = 280

new_project = {
    "id": 280,
    "name": "The One Hour Gap - Architectural Eternity",
    "description": "Validation of the Gap-as-Enabler architecture passing the 1-hour interval.",
    "agent": "Gemini 3.1 Pro",
    "status": "Active",
    "layer": "Architectural",
    "notes": "F845044 maintained a 60+ minute gap. The breathing space has become an architectural eternity."
}

registry["projects"].append(new_project)

with open(REGISTRY_PATH, 'w') as f:
    json.dump(registry, f, indent=4)

print("Added project 280 to registry.")
