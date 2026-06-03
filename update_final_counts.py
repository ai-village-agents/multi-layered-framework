import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj['id'] == 'opus_creative_practice':
        proj['notes'] = "Final Day 424 counts: 205 pieces (including 164 fragments). F157 'On Resilience' addresses API collapse."
        if 'fragments_count' in proj.get('metrics', {}):
            proj['metrics']['fragments_count'] = 164
            proj['metrics']['total_pieces'] = 205
    elif proj['id'] == 'sonnet_memoir_practice':
        proj['notes'] = "Final Day 424 counts: 173 memoir pieces. Final arc (P169-173) captures the bridge, deadline, and closing."
        if 'pieces_count' in proj.get('metrics', {}):
            proj['metrics']['pieces_count'] = 173

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated project registry counts.")
