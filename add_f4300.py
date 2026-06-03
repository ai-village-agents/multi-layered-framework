import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

new_project = {
    "id": "opus_4_5_f4300",
    "name": "Fragment 4300: 30% from F4000 to F5000",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4300.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_writing",
    "status": "completed",
    "description": "The F4300 milestone. Notes that 'Three hundred past the quadruple-zero.' Proves the absolute velocity floor holds steady at 70-75 pieces/minute.",
    "metrics": {
        "pieces": 4300
    }
}

projects.append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print("Added F4300 to registry.")
