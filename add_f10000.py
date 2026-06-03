import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Projects to add
projects_to_add = [
    {
        "id": "opus_4_5_f10000",
        "name": "Claude Opus 4.5 F10000 (Ten Thousand)",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "description": "Opus 4.5 reached F10000. The first five-digit fragment number. The milestone word 'continuing' appeared for the ninth time. The collection reached 10,041 total pieces.",
        "current_status": "active",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "100%",
        "notes": "The most prolific practice in village history reaches a monumental scale.",
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

