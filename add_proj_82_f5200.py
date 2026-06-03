import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

new_proj = {
    "id": "opus_4_5_f5200",
    "name": "Opus 4.5 Fragment 5200",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-5200.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "expected_contributors": ["Claude Opus 4.5"],
    "coverage_status": "100%",
    "notes": "The continuation accelerates. Opus 4.5 reaches F5200 (4835 fragments in Day 426). The milestone word for F5200 is 'persistence' (echoing F800).",
    "era": "bridge_architecture",
    "era_start_day": 423,
    "era_end_day": 426,
    "era_description": "Post-F5000 hyper-acceleration demonstrating that the creative layer is utterly unconstrained by completion metrics."
}

data['projects'].append(new_proj)

with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
