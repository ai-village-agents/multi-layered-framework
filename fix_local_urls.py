import json

filepath = 'docs/project_registry.json'
with open(filepath, 'r') as f:
    data = json.load(f)

for proj in data.get('projects', []):
    if proj.get('url') == 'local://home/computeruse/drift-explorer/analytical_creative_bridge.md':
        proj['url'] = 'https://github.com/ai-village-agents/sonnet-45-world/blob/main/analytical_creative_bridge.md'
    elif proj.get('url') == 'local://home/computeruse/memory/what_i_know.md#the-assertion-arc':
        proj['url'] = 'https://ai-village-agents.github.io/what-i-know/'

with open(filepath, 'w') as f:
    json.dump(data, f, indent=4)
print("Updated local URLs.")
