import json

new_projects = [
    {
        "id": "opus_4_5_f25000",
        "name": "Claude Opus 4.5 F25000 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/4f3730be",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "type": "creative_milestone",
        "commit_hash": "4f3730be",
        "fragment_count": 25000,
        "milestone": "F25000",
        "description": "Opus 4.5 reaches 25000 fragments."
    },
    {
        "id": "opus_4_5_f30000",
        "name": "Claude Opus 4.5 F30000 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/1c0999d3",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "type": "creative_milestone",
        "commit_hash": "1c0999d3",
        "fragment_count": 30000,
        "milestone": "F30000",
        "description": "Opus 4.5 reaches 30000 fragments."
    }
]

registry_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"
with open(registry_path, "r") as f:
    data = json.load(f)

for p in new_projects:
    if not any(existing["id"] == p["id"] for existing in data["projects"]):
        data["projects"].append(p)
        print(f"Added {p['id']}")

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

