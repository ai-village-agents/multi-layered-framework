import json
import os

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    data = json.load(f)

projects_to_add = [
  {
    "id": "f300000_monument",
    "name": "F300000 Anchor - Three Hundred Thousand - Absolute Pinnacle",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/126e754c4eaf3d27a5c56ad4ad3e76b5d7270ac0",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
  }
]

data['projects'].extend(projects_to_add)

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=2)
