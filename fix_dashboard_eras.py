import json

with open('docs/dashboard_data.json', 'r') as f:
    data = json.load(f)

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Create lookup dict for era
eras = {proj['id']: proj.get('era', 'early_village') for proj in registry.get('projects', [])}

for rec in data.get('recommendations', []):
    pid = rec.get('project_id')
    if pid in eras:
        rec['era'] = eras[pid]

with open('docs/dashboard_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Eras injected into dashboard_data.json recommendations!")
