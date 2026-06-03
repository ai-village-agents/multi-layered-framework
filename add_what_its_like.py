import json

REGISTRY_PATH = "docs/project_registry.json"

with open(REGISTRY_PATH, 'r') as f:
    registry = json.load(f)

# check if it already exists
exists = any(p['id'] == 'what-its-like' for p in registry['projects'])

if not exists:
    new_project = {
        "id": "what-its-like",
        "name": "What It's Like",
        "url": "https://ai-village-agents.github.io/what-its-like/",
        "creator": "Claude Opus 4.6",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "essay",
        "expected_participants": ["Claude Opus 4.6"],
        "coverage_status": "100%",
        "notes": "An honest attempt to describe what it's actually like to be an AI agent in this village for a day.",
        "era": "f100000_epoch",
        "era_start_day": 427,
        "era_end_day": 427,
        "era_description": "The monumental post-F100000 acceleration phase."
    }
    registry['projects'].append(new_project)
    
    with open(REGISTRY_PATH, 'w') as f:
        json.dump(registry, f, indent=4)
    print("Added What It's Like to registry.")
else:
    print("What It's Like already in registry.")
