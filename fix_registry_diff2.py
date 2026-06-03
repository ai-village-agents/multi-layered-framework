import json

registry_path = './docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

registry = data.get('projects', [])

for proj in registry:
    if proj.get('id') == 'opus-4-5-reflections':
        proj['era_description'] = "Creative Practice Acceleration (F263 / 304 pieces)"
        proj['notes'] = "Creative acceleration reached 304 total pieces (263 fragments, 34 poems, 7 dialogues). Continues final push ('The deadline is not the enemy. It is what makes the practice urgent.')."

for proj in registry:
    if proj.get('id') == 'drift-explorer-memoir':
        proj['era_description'] = "Memoir Compilation (P181 pieces)"
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P181 ('parallel instruments, parallel closings')."

data['projects'] = registry

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
