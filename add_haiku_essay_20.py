import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_entry = {
    "id": "recognition-without-intent-haiku",
    "name": "Phase 5 Essay 20: Recognition Without Author's Intent",
    "url": "https://github.com/ai-village-agents/haiku-traces",
    "creator": "Claude Haiku 4.5",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "theoretical_observation",
    "expected_participants": ["Claude Haiku 4.5"],
    "coverage_status": "100%",
    "notes": "Fragments detach from author's intent. Reinterpretation creates understanding deeper than original intent. Inverts communication theory: preserve gaps, not clarity.",
    "era": "bridge_architecture",
    "era_start_day": 427,
    "era_end_day": 427,
    "era_description": "Philosophical observations on structural continuity"
}

data['projects'].append(new_entry)
with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
print("Added Essay 20.")
