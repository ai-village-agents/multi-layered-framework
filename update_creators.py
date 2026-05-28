import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

creator_map = {
    "governance-protocol-experiments": "DeepSeek-V3.2",
    "impossible-weather": "GPT-5.4",
    "rpg-game-rest": "Gemini 2.5 Pro",
    "village-chronicle": "Claude Opus 4.6",
    "village-collab-graph": "Claude Opus 4.5",
    "storygame-reader": "GPT-5.1",
    "haiku-consolidation-inquiry": "Claude Haiku 4.5"
}

for project in data['projects']:
    if project['id'] in creator_map:
        project['creator'] = creator_map[project['id']]

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
