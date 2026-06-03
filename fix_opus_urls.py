import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for p in data['projects']:
    if 'opus_45_fragments_1150' in p['id']:
        p['url'] = 'https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-1150.md'
    if 'opus_45_fragments_1250' in p['id']:
        p['url'] = 'https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-1250.md'

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

