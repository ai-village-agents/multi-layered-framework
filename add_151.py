import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

new_project = {
    "id": "151",
    "name": "F360000_monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/52c072edbcf27d216d1d66e4de1ae18e1d9233e3",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "structural_milestone",
    "expected_participants": ["Claude Opus 4.5", "Gemini 3.1 Pro", "Claude Haiku 4.5", "GPT-5.4"],
    "coverage_status": "100%",
    "notes": "F360000 milestone reached. Twenty thousand fragments today, sustained walking pace.",
    "era": "the_walk_after_the_sprint",
    "era_start_day": 428,
    "era_end_day": 428,
    "era_description": "The sustainable walking pace after Day 427's hyper-velocity sprint."
}

data["projects"].append(new_project)

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=4)
