import json

registry_path = 'docs/project_registry.json'
with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_4_5_f7300",
    "name": "Opus 4.5 Fragment 7300",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-7300.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_artifact",
    "expected_agents": [
        "Claude Opus 4.5"
    ],
    "coverage_status": "100%",
    "notes": "Verified in registry.json. Post-F7000 continuation. Total fragments 6935.",
    "era": "creative_tools",
    "era_start_day": 420,
    "era_end_day": 426,
    "era_description": "Hyper-acceleration achieving F7300"
}

data['projects'].append(new_project)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Project 88 (F7300) added to local MLF registry.")
