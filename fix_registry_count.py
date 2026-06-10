import json

with open('docs/MLF_EXPLICIT_REGISTRY.json', 'r') as f:
    data = json.load(f)

data['total_projects'] = 293

with open('docs/MLF_EXPLICIT_REGISTRY.json', 'w') as f:
    json.dump(data, f, indent=4)
