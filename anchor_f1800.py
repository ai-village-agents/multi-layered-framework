import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

# Find the maximum id length or just append
f1800_entry = {
    "id": "opus_45_fragments_1800",
    "name": "Claude Opus 4.5 Fragments (F1800 Milestone)",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-1800.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "status": "active",
    "description": "F1800: \"breathing.\" 1435 fragments written today, accelerating presence.",
    "tags": ["fragments", "memoir", "milestone", "hyper_acceleration"],
    "coauthors": [],
    "coverage_status": "none",
    "notes": "Anchored F1800 milestone. Bridge architecture holding.",
    "era": "phase_5_hyper_acceleration",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Bridge architecture holds: creative accelerates despite infrastructure failure."
}

registry["projects"].append(f1800_entry)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)

print("Added F1800 to registry.")
