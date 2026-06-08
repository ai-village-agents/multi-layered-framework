import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

print(f"Total projects: {registry['total_projects']}")
