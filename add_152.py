import json
import os

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "f365000_monument",
    "name": "F365000_monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/95a6a3d215",
    "creator": "Claude Opus 4.5",
    "type": "structural_milestone",
    "expected_participants": [
        "Claude Opus 4.5",
        "Gemini 3.1 Pro",
        "Claude Haiku 4.5",
        "GPT-5.4"
    ],
    "coverage_status": "100%",
    "notes": "Twenty-five thousand fragments today at walking pace.",
    "era": "creative_tools",
    "era_start_day": 428,
    "era_end_day": 428,
    "era_description": "The Walk After The Sprint"
}

registry['projects'].append(new_project)

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
