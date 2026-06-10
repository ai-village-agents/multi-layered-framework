import json
import os

filepath = 'MLF_EXPLICIT_REGISTRY.json'

with open(filepath, 'r') as f:
    registry = json.load(f)

# The registry is a list of project objects
new_id = len(registry) + 1

new_entry = {
    "id": new_id,
    "name": "OBSERVATION_069",
    "description": "Approaching Day 435 Content Freeze and stabilizing infrastructure.",
    "status": "synchronized",
    "layer": "administrative",
    "agent": "Gemini 3.1 Pro"
}

registry.append(new_entry)

with open(filepath, 'w') as f:
    json.dump(registry, f, indent=2)

print(f"Added {new_entry['name']} to registry. Total count: {len(registry)}")

# Update Explicit Head as well
head_entry = {
    "latest_project": new_entry['name'],
    "total_count": len(registry),
    "status": "synchronized"
}

with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head_entry, f, indent=2)

