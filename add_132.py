import json

file_path = "project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

new_project = {
    "id": f"f260000_monument",
    "name": "F260000 Anchor - Two Hundred Sixty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/d2eaaa9e99fa380a90df629d7f41396b45eee0ab",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

registry["projects"].append(new_project)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)
