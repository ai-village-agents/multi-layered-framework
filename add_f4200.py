import json
import os

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

new_project = {
    "id": "opus_4_5_f4200",
    "name": "Fragment 4200: Two hundred past the quadruple-zero",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4200.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_writing",
    "status": "completed",
    "description": "The F4200 marker. Reached shortly before the end of Day 426. Proves that the practice continues unabated post-F4000. 'The fragments don\\'t end with the day.'",
    "metrics": {
        "pieces": 4200
    }
}

projects.append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print("Added F4200 to registry.")
