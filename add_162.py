import json

data = {
    "id": "162",
    "name": "F410000 Monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/raw/7cc930c375e843e698f78b5e6cc34e76a786aca4/fragments/fragment-410000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "structural_anchor",
    "expected_content": [
        "F410000",
        "Opus 4.5",
        "Day 428"
    ],
    "coverage_status": "100%",
    "notes": "Verified structural anchor in afternoon walk."
}

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_projects = []
for p in registry['projects']:
    new_projects.append(p)

new_projects.append(data)
registry['projects'] = new_projects
registry['total_projects'] = len(new_projects)

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
