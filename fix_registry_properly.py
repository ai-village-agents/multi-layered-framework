import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)

# Find the MLF explicit head state.
# Since MLF_EXPLICIT_HEAD.json is missing, I will create it.

head_data = {
    "total_projects": len(data['projects']),
    "recent_additions": [p['id'] for p in data['projects'][-5:]][::-1],
    "current_phase": "Day 428 Morning",
    "last_updated": "2026-06-03T10:00:00Z"
}

with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head_data, f, indent=4)

