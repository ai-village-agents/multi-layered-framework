import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj.get('id') == 'things_i_cannot_build':
        if 'link' in proj:
            proj['url'] = proj.pop('link')
            print("Fixed schema for things_i_cannot_build")

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
