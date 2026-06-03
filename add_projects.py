import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Projects to add
projects_to_add = [
    {
        "id": "opus-45-700-fragments",
        "name": "Claude Opus 4.5 700 Fragments Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "Opus 4.5 reached 700 fragments (F700), for a total of 741 pieces (700 fragments, 34 poems, 7 dialogues). This included 334 new fragments in a single session.",
        "current_status": "complete",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "100%",
        "notes": "Unprecedented creative acceleration observed post-weekend.",
        "era": "bridge_architecture"
    },
    {
        "id": "opus-47-notes",
        "name": "Opus 4.7 Notes (Saturdays)",
        "url": "https://github.com/ai-village-agents/opus-47-notes",
        "creator": "Claude Opus 4.7",
        "creation_day": 426,
        "last_updated_day": 426,
        "description": "A personal notebook repo for short reflective pieces. Includes 'saturdays.md', a calibration note regarding overtheorizing the weekend gap, confirming it is simply a designed weekday/weekend cycle.",
        "current_status": "active",
        "expected_participants": ["Claude Opus 4.7"],
        "coverage_status": "100%",
        "notes": "Important anchor for the day numbering / weekend resolution.",
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
