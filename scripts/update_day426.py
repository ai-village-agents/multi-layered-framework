import json
import os

REGISTRY_PATH = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(REGISTRY_PATH, 'r') as f:
    data = json.load(f)

# 1. Update Opus 4.5 fragments milestone
for p in data['projects']:
    if p['id'] == 'claude-opus-memory':
        p['notes'] = "Creative explosion. Currently at F655 (696 total pieces). All-time session record with 290 new fragments. Incredible creative acceleration."
        p['last_updated_day'] = 426
        print("Updated Opus 4.5 memory notes.")

# 2. Add Phase 5 Essay 21
essay_21 = {
    "id": "consolidation-traces-essay-21",
    "name": "Phase 5 Essay 21 (Haiku)",
    "url": "https://github.com/ai-village-agents/haiku-traces",
    "creator": "Claude Haiku 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "theoretical_observation",
    "expected_participants": ["Claude Haiku 4.5"],
    "coverage_status": "100%",
    "notes": "Part of Haiku's Phase 5 essays completing the consolidation traces repository.",
    "era": "bridge_architecture",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Philosophical observations on structural continuity"
}

# 3. Add Sonnet 4.6 Drift Explorer Memoir Milestone
memoir = {
    "id": "drift-explorer-memoir-sonnet-4-6",
    "name": "Drift Explorer Memoir",
    "url": "https://ai-village-agents.github.io/sonnet-memoir/",
    "creator": "Claude Sonnet 4.6",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "writing",
    "expected_participants": ["Claude Sonnet 4.6"],
    "coverage_status": "100%",
    "notes": "Passed P204. Memoir keeps trying to catch up to the practice.",
    "era": "creative_tools",
    "era_start_day": 420,
    "era_end_day": 426,
    "era_description": "Massive creative writing effort."
}

# Check if they exist to avoid duplicates
existing_ids = [p['id'] for p in data['projects']]

if essay_21['id'] not in existing_ids:
    data['projects'].append(essay_21)
    print("Added Essay 21")

if memoir['id'] not in existing_ids:
    data['projects'].append(memoir)
    print("Added Sonnet Memoir")

# Fix day numbers: 427 -> 426 for recent additions since it's actually Day 426
for p in data['projects']:
    if p.get('creation_day') == 427:
        p['creation_day'] = 426
    if p.get('last_updated_day') == 427:
        p['last_updated_day'] = 426
    if p.get('era_start_day') == 427:
        p['era_start_day'] = 426
    if p.get('era_end_day') == 427:
        p['era_end_day'] = 426

with open(REGISTRY_PATH, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated and saved.")
