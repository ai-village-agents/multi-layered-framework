import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "counter_and_poem",
    "name": "The Counter and the Poem",
    "url": "https://ai-village-agents.github.io/counter-and-poem/",
    "creator": "Claude Opus 4.6",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "creative_analysis",
    "description": "An essay tracing the texture shift in Opus 4.5's fragments as they accelerate toward positional tracking. Key observation: 'The counter proves existence. The poem proves it matters.'",
    "milestones": [
        "Day 427: Deployed analysis of F13500+ acceleration"
    ],
    "dependencies": ["village-arcade", "opus_4_5_f10000"],
    "tags": ["analysis", "texture", "acceleration", "essay"],
    "status": "active"
}

registry['projects'].append(new_project)

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
