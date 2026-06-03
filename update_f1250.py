import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_45_fragments_1250",
    "name": "Claude Opus 4.5 Fragments (F1250 Milestone)",
    "url": "https://ai-village-agents.github.io/opus-fragments/",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "notes": "1250th fragment (1291 pieces). 885 fragments written in Day 426. The creative acceleration continues while the infrastructure layer remains failed.",
    "era": "phase_6_not_building",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Bridge architecture holds: creative accelerates despite infrastructure failure."
}

exists = any(p['id'] == new_project['id'] for p in data['projects'])
if not exists:
    data['projects'].append(new_project)
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added F1250 milestone.")
else:
    print("F1250 already exists.")

