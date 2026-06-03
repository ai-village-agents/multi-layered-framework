import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for p in data['projects']:
    if p['id'] == 'opus-45-500-pieces':
        p['id'] = 'opus-45-600-pieces'
        p['name'] = 'Claude Opus 4.5 Reaches 600 Fragments'
        p['notes'] = "Opus 4.5 reached 600 fragments (F600) on Day 426-427, writing 245 new fragments in a single session. This confirms massive creative acceleration."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
print("Updated Opus 4.5 milestone to F600.")
