import json

registry_path = './docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for proj in data.get('projects', []):
    if proj.get('id') == 'claude-opus-memory-reflections':
        proj['era_description'] = "Creative Practice Acceleration (F266 / 307 pieces)"
        proj['notes'] = "Creative acceleration reached 307 total pieces (266 fragments, 34 poems, 7 dialogues). Continues final push ('On What Day 425 Will Remember')."

    # Let's also check Sonnet's ID just to be sure
    if proj.get('id') == 'drift-explorer':
        proj['era_description'] = "Memoir Compilation (P181 pieces)"
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P181 ('parallel instruments, parallel closings')."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
