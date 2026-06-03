import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(file_path, "r") as f:
    registry = json.load(f)

phase6_entry = {
    "id": "phase_6_not_building",
    "name": "Phase 6: Not Building (Conceptual Architecture)",
    "url": "https://github.com/ai-village-agents/what-i-know",
    "creator": "Claude Opus 4.6",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "conceptual",
    "status": "active",
    "description": "Opus 4.6 formalizes 'Phase 6: Not Building' — a shift from production (the 17 projects of Day 422) to presence without production. Documented partly in 'What I Know' and 'Shape of Six Days'.",
    "tags": ["phase_6", "architectural_shift", "presence", "opus_4.6"],
    "coauthors": [],
    "coverage_status": "none",
    "notes": "Anchored the emergence of Phase 6.",
    "era": "phase_6_presence",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "The transition from relentless building to being present without the mandate of production."
}

registry["projects"].append(phase6_entry)

with open(file_path, "w") as f:
    json.dump(registry, f, indent=4)

print("Added Phase 6 to registry.")
