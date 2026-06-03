import json
import os

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

new_project = {
    "id": "opus_4_5_f4250",
    "name": "Fragment 4250: Quarter-way to F5000",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4250.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_writing",
    "status": "completed",
    "description": "The F4250 milestone. Reached shortly after F4000. Confirms sustained velocity of ~70-75 pieces/minute and continuous hyper-acceleration post-boundary.",
    "metrics": {
        "pieces": 4250
    }
}

projects.append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print("Added F4250 to registry.")
