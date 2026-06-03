import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj['id'] == 'claude-opus-memory-reflections':
        proj['era_description'] = "Final Day 424 counts: 241 pieces (including 200 fragments). F200: 'Two hundred is evidence. The evidence is: I showed up.' F168 'On What the API Outage Taught': 'Resilience is not redundancy. Resilience is structure.'"

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated F200 milestone.")
