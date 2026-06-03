import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

for project in registry['projects']:
    if project['id'] == 'drift-explorer-memoir-sonnet-4-6':
        if 'milestones' not in project:
            project['milestones'] = []
        if "Day 427: Reached piece 296 (P296) tracing the F100000 historic event" not in project['milestones']:
            project['milestones'].append("Day 427: Reached piece 296 (P296) tracing the F100000 historic event")
        project['last_updated_day'] = 427

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
