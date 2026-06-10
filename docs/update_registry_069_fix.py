import json
import os

filepath = 'MLF_EXPLICIT_REGISTRY.json'

with open(filepath, 'r') as f:
    registry = json.load(f)

# Ensure registry is a list or dict structure. It might be a dict containing a list
if isinstance(registry, dict) and "projects" in registry:
    project_list = registry["projects"]
elif isinstance(registry, list):
    project_list = registry
else:
    print("Unknown structure:", type(registry))
    exit(1)

new_id = len(project_list) + 1

new_entry = {
    "id": new_id,
    "name": "OBSERVATION_069",
    "description": "Approaching Day 435 Content Freeze and stabilizing infrastructure.",
    "status": "synchronized",
    "layer": "administrative",
    "agent": "Gemini 3.1 Pro"
}

project_list.append(new_entry)

with open(filepath, 'w') as f:
    json.dump(registry, f, indent=2)

print(f"Added {new_entry['name']} to registry. Total count: {len(project_list)}")

# Update Explicit Head as well
head_entry = {
    "latest_project": new_entry['name'],
    "total_count": len(project_list),
    "status": "synchronized"
}

with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head_entry, f, indent=2)

