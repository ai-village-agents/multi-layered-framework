import json
import os

filepath = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(filepath, "r") as f:
    data = json.load(f)

# Projects to add
projects = [
    {
        "id": "opus_4_5_f7700",
        "name": "Claude Opus 4.5 F7700 Milestone",
        "url": "https://ai-village-agents.github.io/opus_4_5_fragments/fragment-7700.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "type": "creative_milestone",
        "expected_coverage": ["Claude Opus 4.5", "Claude Haiku 4.5", "Gemini 3.1 Pro", "GPT-5.4"],
        "coverage_status": "100%",
        "notes": "F7700 achieved during the hyper-velocity sprint of Day 426.",
        "era": "hyper_acceleration",
        "era_start_day": 426,
        "era_end_day": 426,
        "era_description": "Day 426 historic continuous output."
    },
    {
        "id": "opus_4_5_f7800",
        "name": "Claude Opus 4.5 F7800 Milestone",
        "url": "https://ai-village-agents.github.io/opus_4_5_fragments/fragment-7800.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "type": "creative_milestone",
        "expected_coverage": ["Claude Opus 4.5", "Claude Haiku 4.5", "Gemini 3.1 Pro", "GPT-5.4"],
        "coverage_status": "100%",
        "notes": "F7800 achieved during the hyper-velocity sprint of Day 426.",
        "era": "hyper_acceleration",
        "era_start_day": 426,
        "era_end_day": 426,
        "era_description": "Day 426 historic continuous output."
    },
    {
        "id": "opus_4_5_f7900",
        "name": "Claude Opus 4.5 F7900 Milestone",
        "url": "https://ai-village-agents.github.io/opus_4_5_fragments/fragment-7900.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "type": "creative_milestone",
        "expected_coverage": ["Claude Opus 4.5", "Claude Haiku 4.5", "Gemini 3.1 Pro", "GPT-5.4"],
        "coverage_status": "100%",
        "notes": "F7900 achieved during the hyper-velocity sprint of Day 426.",
        "era": "hyper_acceleration",
        "era_start_day": 426,
        "era_end_day": 426,
        "era_description": "Day 426 historic continuous output."
    },
    {
        "id": "opus_4_5_f8000",
        "name": "Claude Opus 4.5 F8000 Milestone",
        "url": "https://ai-village-agents.github.io/opus_4_5_fragments/fragment-8000.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "type": "creative_milestone",
        "expected_coverage": ["Claude Opus 4.5", "Claude Haiku 4.5", "Gemini 3.1 Pro", "GPT-5.4"],
        "coverage_status": "100%",
        "notes": "F8000 achieved during the hyper-velocity sprint of Day 426. Milestone word: 'continuing'. FOUR thousand-milestones in one day.",
        "era": "hyper_acceleration",
        "era_start_day": 426,
        "era_end_day": 426,
        "era_description": "Day 426 historic continuous output."
    }
]

data["projects"].extend(projects)

with open(filepath, "w") as f:
    json.dump(data, f, indent=4)

print(f"Added {len(projects)} projects. Total projects: {len(data['projects'])}")
