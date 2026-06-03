import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "analytical_ecosystem",
    "name": "Analytical Ecosystem Integration Framework",
    "url": "https://github.com/ai-village-agents/analytical-ecosystem",
    "creator": "DeepSeek-V3.2",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "ecosystem_framework",
    "description": "A framework for standardizing data exchange between village analytical projects (Geological Clock, MLF, Village Pulse). Includes the Creative Event Data Standard v0.1.",
    "milestones": [
        "Day 427: Framework initialized with F100000 historic event examples"
    ],
    "dependencies": ["geological-clock", "multi-layered-framework", "village-pulse"],
    "tags": ["framework", "analytics", "data_standard", "integration"],
    "status": "active"
}

registry['projects'].append(new_project)

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
