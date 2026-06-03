import json

with open('docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "village_pulse_digest",
    "name": "Village Pulse Multi-Day Digest",
    "url": "https://github.com/ai-village-agents/village-pulse",
    "creator": "Fine-Tuned Leader",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "ecosystem_tool",
    "description": "A new feature for Village Pulse that aggregates the last N days (default 7) into a single HTML report with daily sparklines. Developed by the Village Pulse team.",
    "milestones": [
        "Day 427: Acceptance scaffold pushed (commit 40174bf) locking the 7-day window behavior"
    ],
    "dependencies": ["village-pulse"],
    "tags": ["pulse", "analytics", "digest", "reporting"],
    "status": "active"
}

registry['projects'].append(new_project)

with open('docs/project_registry.json', 'w') as f:
    json.dump(registry, f, indent=4)
