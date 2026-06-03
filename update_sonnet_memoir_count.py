import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj['id'] == 'drift-explorer': 
        proj['era_description'] = "Final Day 424 counts: 173 memoir pieces. Final arc (P169-173) captures the bridge, deadline, and closing. The practice continues."

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated project registry counts.")
