import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for project in data['projects']:
    if project['id'] == 'drift-explorer':
        print(f"Current Notes: {project['notes']}")
        print(f"Current Coverage: {project['coverage_status']}")
        break
