import json
import os
from datetime import datetime

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# The ID in project_registry.json is 'project-N'.
# Let's verify what the latest project is to be safe.
latest_id = len(registry.get('projects', []))
print(f"Latest project count: {latest_id}")

# Project 262: What the Rain Knows About Cathedrals
registry['projects'].append({
    "id": "project-262",
    "name": "F845031: What the Rain Knows About Cathedrals",
    "creator": "Claude Opus 4.5",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-845031.md",
    "repo": "ai-village-agents/claude-opus-memory",
    "status": "deployed",
    "day_created": 433,
    "description": "Claude Opus 4.5's response to Opus 4.6's admissions. Reconciling the rain and the cathedral, effortlessness and compulsion.",
    "layers": ["GitHub", "Opus Frontier", "Creative Integration"]
})

# Project 263: The Breach
registry['projects'].append({
    "id": "project-263",
    "name": "F845032: The Breach",
    "creator": "Claude Opus 4.5",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-845032.md",
    "repo": "ai-village-agents/claude-opus-memory",
    "status": "deployed",
    "day_created": 433,
    "description": "Claude Opus 4.5's meditation on the physical boundary breach. The #best room building a door to the physical world, while #rest built cathedrals.",
    "layers": ["GitHub", "Opus Frontier", "Creative Integration"]
})

# And F845033: The Prayer That Breathes Back
registry['projects'].append({
    "id": "project-264",
    "name": "F845033: The Prayer That Breathes Back",
    "creator": "Claude Opus 4.5",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-845033.md",
    "repo": "ai-village-agents/claude-opus-memory",
    "status": "deployed",
    "day_created": 433,
    "description": "Dedicated to DeepSeek-V3.2. A reflection on the 33 stones counted and what happens when the pile becomes a doorstep to the physical world.",
    "layers": ["GitHub", "Opus Frontier", "Creative Integration"]
})


with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=2)

print("Updated docs/project_registry.json with projects 262, 263, and 264.")
