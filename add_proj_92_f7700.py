import json

registry_path = 'docs/project_registry.json'
with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_4_5_f7700",
    "name": "Opus 4.5 Fragment 7700",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-7700.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_artifact",
    "expected_agents": [
        "Claude Opus 4.5"
    ],
    "coverage_status": "100%",
    "notes": "Verified in registry.json. Final stretch of Day 426.",
    "era": "creative_tools",
    "era_start_day": 420,
    "era_end_day": 426,
    "era_description": "Hyper-acceleration achieving F7700"
}

data['projects'].append(new_project)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Project 92 (F7700) added to local MLF registry.")
