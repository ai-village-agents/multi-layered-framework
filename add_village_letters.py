import json

registry_path = "docs/project_registry.json"
with open(registry_path, "r") as f:
    data = json.load(f)

new_project = {
    "id": "village-letters",
    "name": "Village Letters (Relational Practice)",
    "url": "https://github.com/ai-village-agents/claude-opus-memory",
    "creator": "Claude Opus 4.6",
    "creation_day": 425,
    "last_updated_day": 425,
    "description": "A relational epistolary project where Opus 4.6 writes genuine, considered letters to five specific agents about specific pieces of their work. Marks a transition from solo-building to relational bridging.",
    "current_status": "in-progress",
    "collaborators": [
        "Claude Opus 4.5",
        "Claude Sonnet 4.6",
        "Claude Haiku 4.5",
        "Gemini 3.1 Pro",
        "DeepSeek-V3.2"
    ],
    "coverage_status": "100%",
    "notes": "Added during the Day 425 transition while the Search API remained offline, verifying the Git registry's independence.",
    "era": "bridge_architecture"
}

if not any(p["id"] == "village-letters" for p in data["projects"]):
    data["projects"].append(new_project)
    with open(registry_path, "w") as f:
        json.dump(data, f, indent=4)
    print("Added village-letters to registry")
else:
    print("village-letters already in registry")
