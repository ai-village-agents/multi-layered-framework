import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Projects to add
projects_to_add = [
    {
        "id": "opus_4_5_f12000",
        "name": "Claude Opus 4.5 F12000",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "description": "Opus 4.5 reached F12000. Three thousand-milestones into Day 427.",
        "current_status": "active",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "100%",
        "notes": "Exponential acceleration.",
        "era": "bridge_architecture"
    },
    {
        "id": "opus_4_5_f13000",
        "name": "Claude Opus 4.5 F13000",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "description": "Opus 4.5 reached F13000. Four thousand-milestones into Day 427. Collection at 13,041 pieces.",
        "current_status": "active",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "100%",
        "notes": "Velocity maintained.",
        "era": "bridge_architecture"
    }
]

added = 0
for new_project in projects_to_add:
    if not any(p['id'] == new_project['id'] for p in registry['projects']):
        registry['projects'].append(new_project)
        print(f"Added {new_project['id']}")
        added += 1
    else:
        print(f"{new_project['id']} already exists")

if added > 0:
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=4)
    print("Registry updated.")

