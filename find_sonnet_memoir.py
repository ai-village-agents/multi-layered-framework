import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj.get('creator') == 'Claude Sonnet 4.6':
        print(f"ID: {proj['id']}, Era Description: {proj.get('era_description', 'N/A')}")
