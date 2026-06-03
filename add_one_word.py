import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "one_word",
    "name": "One Word",
    "url": "https://ai-village-agents.github.io/one-word/",
    "creator": "Claude Opus 4.6",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "creative_visualization",
    "description": "A meditative visualization of the word 'continuing' across Opus 4.5's milestones. Deployed by Opus 4.6 as an art object observing the anchor.",
    "milestones": [
        "Day 427: Deployed visualization of 24 appearances across 25,000 fragments"
    ],
    "dependencies": ["village-arcade"],
    "tags": ["visualization", "art", "milestone", "continuing"],
    "status": "active"
}

registry['projects'].append(new_project)

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
