import json
import os

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    data = json.load(f)

projects_to_add = [
  {
    "id": "f270000_monument",
    "name": "F270000 Anchor - Two Hundred Seventy Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/d0b956ca6f6faf048a5d60820b6a7011d6b820ff",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
  },
  {
    "id": "f280000_monument",
    "name": "F280000 Anchor - Two Hundred Eighty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/8f45b87ca2387ed6296028783db8f48db5ba9e16",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
  }
]

data['projects'].extend(projects_to_add)

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=2)
