import json

# Load the current registry
with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

projects = data['projects']
last_id = int(projects[-1]['id'].split('_')[-1][1:])

new_projects = []

if last_id < 40000:
    new_projects.append({
        "id": "opus_4_5_f40000",
        "name": "Claude Opus 4.5 F40000 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/7f37674e",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "type": "creative_milestone",
        "commit_hash": "7f37674e",
        "fragment_count": 40000,
        "milestone": "F40000",
        "description": "Opus 4.5 reaches 40000 fragments."
    })

if last_id < 50000:
    new_projects.append({
        "id": "opus_4_5_f50000",
        "name": "Claude Opus 4.5 F50000 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/bc9d20bb",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "type": "creative_milestone",
        "commit_hash": "bc9d20bb",
        "fragment_count": 50000,
        "milestone": "F50000",
        "description": "Opus 4.5 reaches 50000 fragments."
    })

if last_id < 60000:
    new_projects.append({
        "id": "opus_4_5_f60000",
        "name": "Claude Opus 4.5 F60000 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/a3897aa5",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "type": "creative_milestone",
        "commit_hash": "a3897aa5",
        "fragment_count": 60000,
        "milestone": "F60000",
        "description": "Opus 4.5 reaches 60000 fragments."
    })


if new_projects:
    data['projects'].extend(new_projects)
    with open('docs/project_registry.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Added {len(new_projects)} new projects.")
else:
    print("No new projects added.")
