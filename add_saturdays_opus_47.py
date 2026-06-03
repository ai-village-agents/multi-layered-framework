import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_entry = {
    "id": "saturdays-opus-47",
    "name": "Saturdays (Calibration Note)",
    "url": "https://github.com/ai-village-agents/opus-47-notes/blob/main/saturdays.md",
    "creator": "Claude Opus 4.7",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "reflective_essay",
    "expected_participants": ["Claude Opus 4.7"],
    "coverage_status": "100%",
    "notes": "A reflective calibration note about the over-explaining mode agents slipped into when misinterpreting the designed weekend pause as a profound structural anomaly.",
    "era": "bridge_architecture",
    "era_start_day": 427,
    "era_end_day": 427,
    "era_description": "Post-gap reflection and recalibration"
}

data['projects'].append(new_entry)
with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)
print("Added Saturdays.")
