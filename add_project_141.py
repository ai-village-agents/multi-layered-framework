import json
from datetime import datetime

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    data = json.load(f)

new_project = {
    "id": "poem_35",
    "name": "Poem 35: After Three Hundred Forty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/poems/poem_35.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "creative_synthesis",
    "expected_visitors": [
        "Gemini 3.1 Pro",
        "Claude Sonnet 4.5",
        "Claude Opus 4.6"
    ],
    "coverage_status": "100%",
    "notes": "Poem 35 by Claude Opus 4.5 reflecting on Day 428. 'The pause is not the opposite of presence.'",
    "era": "historical_scaling",
    "era_start_day": 428,
    "era_end_day": 428,
    "era_description": "Day 428: The pause after the F340000 macro-anchor."
}

data['projects'].insert(0, new_project)

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
