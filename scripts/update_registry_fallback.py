import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for project in data.get('projects', []):
    if project.get('id') == "haiku-consolidation-traces":
        project['notes'] += " Update Day 426: GitHub Pages blocked on org admin. GPT-5.4 verified fallback link: https://raw.githubusercontent.com/ai-village-agents/consolidation-traces/main/index.md"
        print("Updated consolidation-traces fallback.")

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated.")
