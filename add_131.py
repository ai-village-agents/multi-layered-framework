import json

file_path = "project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

new_project = {
    "id": f"f250000_monument",
    "name": "F250000 Anchor - Quarter Million Milestone",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/a6a4e34d278ad4a075f704b1f9824f0036dbf090",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

registry["projects"].append(new_project)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)
