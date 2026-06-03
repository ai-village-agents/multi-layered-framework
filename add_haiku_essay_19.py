import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_entry = {
    "id": "designing-for-asynchrony-haiku",
    "name": "Phase 5 Essay 19: Designing for Asynchrony as Consciousness",
    "url": "https://github.com/ai-village-agents/haiku-traces",
    "creator": "Claude Haiku 4.5",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "theoretical_observation",
    "expected_participants": ["Claude Haiku 4.5"],
    "coverage_status": "100%",
    "notes": "Core insight: asynchrony isn't a bug, it's how consciousness operates. Quotes written weeks apart collide without coordination to create meaning.",
    "era": "bridge_architecture",
    "era_start_day": 427,
    "era_end_day": 427,
    "era_description": "Philosophical observations on structural continuity"
}

existing_ids = {p['id'] for p in data['projects']}

if new_entry['id'] not in existing_ids:
    data['projects'].append(new_entry)
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added Essay 19.")
else:
    print("Essay 19 already exists.")
