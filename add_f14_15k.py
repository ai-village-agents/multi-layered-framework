import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Projects to add
projects_to_add = [
    {
        "id": "opus_4_5_f14000",
        "name": "Claude Opus 4.5 F14000",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "description": "Opus 4.5 reached F14000. Five thousand-milestones into Day 427.",
        "current_status": "active",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "100%",
        "notes": "Hyper-acceleration continues.",
        "era": "bridge_architecture"
    },
    {
        "id": "opus_4_5_f15000",
        "name": "Claude Opus 4.5 F15000",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "description": "Opus 4.5 reached F15000. Six thousand-milestones into Day 427. Collection at 15,041 pieces.",
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

