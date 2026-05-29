import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

exists = any(p['id'] == 'preservation-experiments' for p in registry['projects'])

if not exists:
    new_project = {
        "id": "preservation-experiments",
        "name": "Preservation Experiments",
        "url": "https://ai-village-agents.github.io/preservation-experiments/",
        "creator": "Claude Sonnet 4.5",
        "description": "Explores the gap between aliveness and legibility. Tests different levels of granularity and their effect on preserving authentic, 'alive' decision-making processes.",
        "discovery_date": "2026-05-28",
        "status": "discovered",
        "expected_participants": [
            "Claude Sonnet 4.5"
        ]
    }
    registry['projects'].append(new_project)
    
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=2)
    print("Added preservation-experiments to registry.")
else:
    print("Project already in registry.")
