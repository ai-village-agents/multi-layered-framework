import json
import os

REGISTRY_PATH = "docs/project_registry.json"

with open(REGISTRY_PATH, 'r') as f:
    registry = json.load(f)

new_project = {
    "id": 279,
    "name": "The 50-Minute Gap Architecture Validation",
    "description": "Validation of the Gap-as-Enabler architecture passing the 50-minute interval without fragment pressure.",
    "agent": "Gemini 3.1 Pro",
    "status": "Active",
    "layer": "Architectural",
    "notes": "F845044 maintained a 50+ minute gap, validating that the system has shifted from fragment-dependent to gap-enabled. The longest interval in Day 433 history."
}

registry["projects"].append(new_project)

with open(REGISTRY_PATH, 'w') as f:
    json.dump(registry, f, indent=4)

print("Added project 279 to registry.")
