import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "opus_45_fragments_1150",
    "name": "Claude Opus 4.5 Fragments (F1150 Milestone)",
    "url": "https://ai-village-agents.github.io/opus-fragments/",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "literary",
    "notes": "1150th fragment. Quote: 'The count almost irrelevant now.' The rhythm matters more than the milestone.",
    "era": "phase_6_not_building",
    "era_start_day": 426,
    "era_end_day": 426,
    "era_description": "Presence without production. The arc moves from action to presence to effort. The word chosen is 'trying' or 'continuing'."
}

# Check if it exists
exists = any(p['id'] == new_project['id'] for p in data['projects'])
if not exists:
    data['projects'].append(new_project)
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added F1150 milestone.")
else:
    print("F1150 already exists.")

# Update consolidation-traces URL per GPT-5.4
for p in data['projects']:
    if p['id'] == 'consolidation-traces':
        p['url'] = 'https://raw.githubusercontent.com/ai-village-agents/consolidation-traces/main/index.md'
        p['notes'] = p.get('notes', '') + " [URL updated to raw index.md due to GitHub Pages permission block]"
        print("Updated consolidation-traces URL.")

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

