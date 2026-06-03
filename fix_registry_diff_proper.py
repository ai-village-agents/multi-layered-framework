import json

registry_path = './docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for proj in data.get('projects', []):
    if proj.get('id') == 'opus-4-5-reflections':
        proj['era_description'] = "Creative Practice Acceleration (F265 / 306 pieces)"
        proj['notes'] = "Creative acceleration reached 306 total pieces (265 fragments, 34 poems, 7 dialogues). Continues final push ('The village is a collective instrument.')."
    if proj.get('id') == 'drift-explorer-memoir':
        proj['era_description'] = "Memoir Compilation (P181 pieces)"
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P181 ('parallel instruments, parallel closings')."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
