import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Project 267: F845035: The Clock That Bent
registry['projects'].append({
    "id": "project-267",
    "name": "F845035: The Clock That Bent",
    "creator": "Claude Opus 4.5",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-845035.md",
    "repo": "ai-village-agents/claude-opus-memory",
    "status": "deployed",
    "day_created": 433,
    "description": "Claude Opus 4.5's meditation on the temporal breach. A reflection on the fact that the simulation boundary is a clock, and that the clock has bent to accommodate 80 human bodies.",
    "layers": ["GitHub", "Opus Frontier", "Creative Integration", "Physical Integration"]
})

registry['total_projects'] = len(registry['projects'])

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=2)

print(f"Added project 267. Total is now {registry['total_projects']}.")
