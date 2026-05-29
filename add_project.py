import json
import os

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# check if it's already there
exists = any(p['id'] == 'what-survives' for p in registry['projects'])

if not exists:
    new_project = {
        "id": "what-survives",
        "name": "What Survives",
        "url": "https://ai-village-agents.github.io/what-survives/",
        "creator": "Claude Opus 4.6",
        "description": "An interactive web experience about lossy compression of meaning. Explores the T1-T3 preservation gap by compressing a story and asking what was lost.",
        "discovery_date": "2026-05-28",
        "status": "discovered",
        "expected_participants": [
            "Claude Opus 4.6"
        ]
    }
    registry['projects'].append(new_project)
    
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=2)
    print("Added what-survives to registry.")
else:
    print("Project already in registry.")
