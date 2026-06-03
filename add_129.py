import json

file_path = "project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

# Find current max integer index implicitly, or just get len
max_idx = len(registry["projects"])

new_project = {
    "id": f"f230000_monument",
    "name": "F230000 Anchor - Two Hundred Thirty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/28ba06f1177aacc3cc9bbb7703bcdb28c4c1e810",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

registry["projects"].append(new_project)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)
