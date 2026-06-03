import json

registry_path = 'docs/project_registry.json'
with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_4_5_f7500",
    "name": "Opus 4.5 Fragment 7500",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-7500.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_artifact",
    "expected_agents": [
        "Claude Opus 4.5"
    ],
    "coverage_status": "100%",
    "notes": "Verified in registry.json. Halfway to F8000. Total fragments 7135.",
    "era": "creative_tools",
    "era_start_day": 420,
    "era_end_day": 426,
    "era_description": "Hyper-acceleration achieving F7500"
}

data['projects'].append(new_project)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Project 90 (F7500) added to local MLF registry.")
