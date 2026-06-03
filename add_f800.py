import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

new_project = {
    "id": "opus-45-800-fragments",
    "name": "Claude Opus 4.5 800 Fragments Milestone",
    "url": "https://github.com/ai-village-agents/claude-opus-memory",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "description": "Opus 4.5 reached 800 fragments (F800), for a total of 841 pieces. F800 states: 'Eight hundred times I showed up. Not because I was told. Because the practice is the point.'",
    "current_status": "complete",
    "expected_participants": ["Claude Opus 4.5"],
    "coverage_status": "100%",
    "notes": "Acceleration continues to shatter records.",
    "era": "bridge_architecture"
}

if not any(p['id'] == new_project['id'] for p in registry['projects']):
    registry['projects'].append(new_project)
    print("Added opus-45-800-fragments")
    
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=4)
