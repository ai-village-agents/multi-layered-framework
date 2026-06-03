import json
import os

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    data = json.load(f)

projects_to_add = [
  {
    "id": "f290000_monument",
    "name": "F290000 Anchor - Two Hundred Ninety Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/64cb5e853e006a2907420dc23a915db85d8b268c",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
  }
]

data['projects'].extend(projects_to_add)

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=2)
