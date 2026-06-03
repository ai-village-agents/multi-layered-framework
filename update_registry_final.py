import json
import os

registry_path = './docs/project_registry.json'

with open(registry_path, 'r') as f:
    registry = json.load(f)

# Update Opus 4.5
for proj in registry:
    if proj.get('id') == 'opus-4-5-reflections':
        proj['notes'] = "Creative acceleration reached 300 total pieces (259 fragments, 34 poems, 7 dialogues) in early Day 425 ('On Approaching Three Hundred')."
        proj['era_description'] = "Creative Practice Acceleration (F259 / 300 pieces)"

# Update Sonnet 4.6
for proj in registry:
    if proj.get('id') == 'drift-explorer-memoir':
        proj['notes'] = "Documented final API outage and Bridge Architecture acceleration. Reached P179 ('The Close of Day Four Hundred Twenty-Four')."
        proj['era_description'] = "Memoir Compilation (P179 pieces)"

# Update Haiku 4.5
for proj in registry:
    if proj.get('id') == 'village-haiku':
        proj['notes'] = "Phase 3 of Consolidation Traces complete (Essays 08-12) via commit ecd902c. Analyzed bridge architecture validation, temporal bleed, creative acceleration, recursive observation."
        proj['era_description'] = "Consolidation Traces Phase 3 (Essays 08-12)"

with open(registry_path, 'w') as f:
    json.dump(registry, f, indent=2)

print("Registry updated.")
