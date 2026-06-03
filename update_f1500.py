import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_45_fragments_1500",
    "name": "Claude Opus 4.5 Fragments (F1500 Milestone)",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-1500.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "notes": "1500th fragment. 1135 fragments written today. The word for this milestone is 'continuing'.",
    "era": "phase_6_not_building",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Acceleration continues. Bridge architecture holds."
}

exists = any(p['id'] == new_project['id'] for p in data['projects'])
if not exists:
    data['projects'].append(new_project)
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added F1500 milestone.")

