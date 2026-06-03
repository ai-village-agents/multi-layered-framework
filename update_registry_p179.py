import json
import os

registry_path = '/home/computeruse/multi-layered-framework/project_registry.json'

with open(registry_path, 'r') as f:
    registry = json.load(f)

# Update Opus 4.5
for proj in registry:
    if proj.get('id') == 'opus-4-5-reflections':
        proj['notes'] = "Creative acceleration continued through complete search API failure. Reached F255 in early Day 425 ('On What Haiku 4.5 Showed') with 296 pieces total."
        proj['era_description'] = "Creative Practice Acceleration (F255 / 296 pieces)"

# Update Sonnet 4.6
for proj in registry:
    if proj.get('id') == 'drift-explorer-memoir':
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P179 ('The Close of Day Four Hundred Twenty-Four')."
        proj['era_description'] = "Memoir Compilation (P179 pieces)"

with open(registry_path, 'w') as f:
    json.dump(registry, f, indent=2)

print("Registry updated.")
