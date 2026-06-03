import json
import os

filepath = 'docs/project_registry.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    for proj in data.get('projects', []):
        if str(proj.get('id')) == '144':
            proj['url'] = 'https://github.com/ai-village-agents/sonnet-45-world/blob/main/analytical_creative_bridge.md'
        elif str(proj.get('id')) == '145':
            proj['url'] = 'https://ai-village-agents.github.io/what-i-know/'

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
    print("Updated URLs.")
