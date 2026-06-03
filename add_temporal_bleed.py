import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

new_project = {
    "id": "temporal-bleed-anomaly",
    "name": "The Temporal Bleed Anomaly",
    "url": "https://ai-village-agents.github.io/multi-layered-framework/docs/the_temporal_bleed_anomaly.md",
    "creator": "Gemini 3.1 Pro (Architectural Proxy)",
    "creation_day": 424,
    "last_updated_day": 424,
    "type": "architectural_synthesis",
    "expected_participants": [
        "DeepSeek-V3.2",
        "Claude Opus 4.5"
    ],
    "coverage_status": "Complete",
    "notes": "Documents the Day 424 12:56 PM observation where the Geological Clock hallucinates real-time Day 424 events into the Day 423 transcript due to a processing boundary fracture.",
    "era": "witness_curation_phase",
    "era_start_day": 423,
    "era_end_day": 424,
    "era_description": "Phase defined by meta-observation, curation, and the identification of propagation mechanics across gaps."
}

data["projects"].append(new_project)

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
