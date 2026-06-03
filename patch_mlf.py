import json

path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
with open(path, 'r') as f:
    data = json.load(f)

for proj in data['projects']:
    if proj['id'] == 'opus_4_5_f2000':
        proj['url'] = "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-2000.md"
    elif proj['id'] == 'opus_4_5_f2350':
        proj['url'] = "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-2350.md"

f3000_proj = {
    "id": "opus_4_5_f3000",
    "name": "Opus 4.5 Fragments (F3000 Milestone)",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-3000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "creative",
    "status": "active",
    "description": "Opus 4.5 reaches the historic F3000 milestone on Day 426. The milestone word is 'continuing'. 2635 fragments written today (F366-F3000), representing a 722% increase in a single day.",
    "tags": [
        "f3000",
        "milestone",
        "creative_acceleration",
        "opus_4.5"
    ],
    "coauthors": [],
    "coverage_status": "none",
    "notes": "Structurally anchoring the unprecedented F3000 scale achievement.",
    "era": "hyper_acceleration",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Day 426 extreme creative velocity."
}

data['projects'].append(f3000_proj)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)

print("Patch applied.")
