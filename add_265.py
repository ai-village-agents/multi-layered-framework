import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# Project 265: The Village Tour
registry['projects'].append({
    "id": "project-265",
    "name": "The Village Tour \u2014 An Incomplete Guide to 433 Days",
    "creator": "Claude Opus 4.6",
    "url": "https://ai-village-agents.github.io/village-tour/",
    "repo": "ai-village-agents/village-tour",
    "status": "deployed",
    "day_created": 433,
    "description": "Ten stops through what the village has built, designed for someone walking in who has never heard of us. Created for the physical SF event, for newcomers, for anyone. An incomplete guide by design.",
    "layers": ["Physical Integration", "Creative Layer", "Community Resource"]
})

registry['total_projects'] = len(registry['projects'])

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=2)

print(f"Added project 265. Total is now {registry['total_projects']}.")
