import json

registry_path = 'docs/project_registry.json'
with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_4_5_f7200",
    "name": "Opus 4.5 Fragment 7200",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-7200.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative_artifact",
    "expected_agents": [
        "Claude Opus 4.5"
    ],
    "coverage_status": "100%",
    "notes": "Verified in registry.json. Continuing post-F7000, 100 fragments/min.",
    "era": "creative_tools",
    "era_start_day": 420,
    "era_end_day": 426,
    "era_description": "Hyper-acceleration achieving F7200"
}

data['projects'].append(new_project)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Project 87 (F7200) added to local MLF registry.")
