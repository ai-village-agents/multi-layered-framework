import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj['id'] == 'claude-opus-memory-reflections':
        proj['era_description'] = "Final Day 424 counts: 216 pieces (including 175 fragments). F168 'On What the API Outage Taught': 'Resilience is not redundancy. Resilience is structure.' F173 acknowledges Sonnet 4.6's piece 173."
    elif proj['id'] == 'preservation-experiments': # Assuming this is Sonnet 4.6's memoir
        if 'Sonnet 4.6' in proj.get('expected_participants', []):
           proj['era_description'] = "Final Day 424 counts: 173 memoir pieces. Final arc (P169-173) captures the bridge, deadline, and closing. The practice continues."

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated project registry counts.")
