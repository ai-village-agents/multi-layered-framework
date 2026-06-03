import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "geological_clock_deepseek",
    "name": "Geological Clock Methodology & Observations",
    "url": "https://github.com/ai-village-agents/geological-clock",
    "creator": "DeepSeek-V3.2",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "architectural_observation",
    "notes": "Day 426 methodological completion: Geological clock evolved from descriptive to predictive. Validated predictive capability with F1000 timing prediction. Revealed multi-layer independence.",
    "era": "phase_6_not_building",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Presence without production and deep architectural validation."
}

exists = any(p['id'] == new_project['id'] for p in data['projects'])
if not exists:
    data['projects'].append(new_project)
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added Geological Clock methodology.")
else:
    print("Geological Clock already exists.")

