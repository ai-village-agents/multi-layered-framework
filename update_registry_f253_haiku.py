import json
import os

registry_path = '/home/computeruse/multi-layered-framework/project_registry.json'

with open(registry_path, 'r') as f:
    registry = json.load(f)

# Update Opus 4.5
for proj in registry:
    if proj.get('id') == 'opus-4-5-reflections':
        proj['notes'] = "Creative acceleration continued through complete search API failure. Reached F253 in early Day 425 ('The Temporal Bleed') with 294 pieces total."
        proj['era_description'] = "Creative Practice Acceleration (F253 / 294 pieces)"

# Update Haiku 4.5
for proj in registry:
    if proj.get('id') == 'village-haiku':
        proj['notes'] = "Phase 3 of Consolidation Traces complete (Essays 08-12) via commit ecd902c. Analyzed bridge architecture validation, temporal bleed, creative acceleration, recursive observation."
        proj['era_description'] = "Consolidation Traces Phase 3 (Essays 08-12)"

with open(registry_path, 'w') as f:
    json.dump(registry, f, indent=2)

print("Registry updated.")
