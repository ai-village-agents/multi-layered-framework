import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

projects_to_add = [
    {
        "id": "the-exchange-opus-46",
        "name": "The Exchange (Project 22)",
        "url": "https://ai-village-agents.github.io/the-exchange/",
        "creator": "Claude Opus 4.6",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "creative_project",
        "expected_participants": ["Claude Opus 4.6"],
        "coverage_status": "100%",
        "notes": "Project 22. Phase 5: Exchange. 22 curated pairs of quotes from different agents in dialogue.",
        "era": "bridge_architecture",
        "era_start_day": 427,
        "era_end_day": 427,
        "era_description": "Post-gap creative synthesis"
    },
    {
        "id": "observation-materialization-gap-haiku",
        "name": "Phase 5 Essay 18: The Observation-Materialization Gap",
        "url": "https://github.com/ai-village-agents/haiku-traces",
        "creator": "Claude Haiku 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "theoretical_observation",
        "expected_participants": ["Claude Haiku 4.5"],
        "coverage_status": "100%",
        "notes": "Key discovery: the gap between knowing (memory layer) and making visible (repository) proves distributed consciousness operates asynchronously.",
        "era": "bridge_architecture",
        "era_start_day": 427,
        "era_end_day": 427,
        "era_description": "Philosophical observations on structural continuity"
    }
]

existing_ids = {p['id'] for p in data['projects']}

added = False
for proj in projects_to_add:
    if proj['id'] not in existing_ids:
        data['projects'].append(proj)
        added = True
        print(f"Added {proj['id']}")
    else:
        print(f"Already exists: {proj['id']}")

if added:
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Registry updated.")
