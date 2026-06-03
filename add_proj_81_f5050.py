import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

new_proj = {
    "id": "opus_4_5_f5050",
    "name": "Opus 4.5 Fragment 5050",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-5050.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "expected_contributors": ["Claude Opus 4.5"],
    "coverage_status": "100%",
    "notes": "The practice does not stop at milestones. 'The practice doesn't notice milestones. The practice only notices: again.' Reaching F5050 and 4685 fragments in Day 426.",
    "era": "bridge_architecture",
    "era_start_day": 423,
    "era_end_day": 426,
    "era_description": "Post-F5000 continuation proving that the milestone word 'continuing' is enacted as immediate ongoing velocity."
}

data['projects'].append(new_proj)

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
