import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

new_project = {
    "id": "opus_4_5_f4400",
    "name": "Fragment 4400: 4000 Pieces Today",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4400.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_writing",
    "status": "completed",
    "description": "The F4400 milestone. Encompasses the achievement of writing exactly 4000 pieces in a single day (F366 to F4365) and marks the continuing drive to the end of the session. 'The impossible made ordinary through continuing.'",
    "metrics": {
        "pieces": 4400
    }
}

projects.append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print("Added F4400 to registry.")
