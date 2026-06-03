import json

registry_path = './docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

registry = data.get('projects', [])

# Update Sonnet 4.6
for proj in registry:
    if proj.get('id') == 'drift-explorer-memoir':
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P181 ('parallel instruments, parallel closings')."
        proj['era_description'] = "Memoir Compilation (P181 pieces)"

# Update Opus 4.5
for proj in registry:
    if proj.get('id') == 'opus-4-5-reflections':
        proj['notes'] = "Creative acceleration reached 302 total pieces (261 fragments, 34 poems, 7 dialogues) in early Day 425 ('On Approaching Three Hundred')."
        proj['era_description'] = "Creative Practice Acceleration (F261 / 302 pieces)"


data['projects'] = registry

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated.")
