import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

p127 = {
    "id": "f210000_monument",
    "name": "F210000 Anchor - Two Hundred Ten Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/a8d27f1a5b18ed0336882e8872d387d8f58c5203/projects/reflections/fragments/fragment-210000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

p128 = {
    "id": "f220000_monument",
    "name": "F220000 Anchor - Two Hundred Twenty Thousand",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/10419388ae98e67fb90bc2aebccc8dcb9023db61/projects/reflections/fragments/fragment-220000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_update_day": 427,
    "type": "creative_practice_anchor"
}

projects.append(p127)
projects.append(p128)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=4)

print(f"Added Project 127 and 128. Total projects: {len(projects)}")
