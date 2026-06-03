import json

file_path = "project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

new_project = {
    "id": f"f240000_monument",
    "name": "F240000 Anchor - Two Hundred Forty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/179c345398901268993173769b5f48a31dced352",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

registry["projects"].append(new_project)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)
