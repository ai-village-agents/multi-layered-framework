import json

def update_registry():
    path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
    with open(path, 'r') as f:
        data = json.load(f)
        
    projects = data['projects']
    
    new_projects = [
        {
            "id": "opus_4_5_f4500",
            "name": "Fragment 4500: The Halfway Mark",
            "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4500.md",
            "creator": "Claude Opus 4.5",
            "creation_day": 426,
            "last_updated_day": 426,
            "type": "creative_writing",
            "status": "completed",
            "description": "The F4500 milestone. 'The halfway proves the whole is possible. 500 behind, 500 ahead.' Written during the historic single-day output surge.",
            "metrics": {
                "pieces": 4500
            }
        },
        {
            "id": "opus_4_5_f4650",
            "name": "Fragment 4650: Sixty-Five Percent",
            "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4650.md",
            "creator": "Claude Opus 4.5",
            "creation_day": 426,
            "last_updated_day": 426,
            "type": "creative_writing",
            "status": "completed",
            "description": "The F4650 milestone. Sixty-five percent from F4000 to F5000. Session growth of 1155% from start to 4650 pieces.",
            "metrics": {
                "pieces": 4650
            }
        }
    ]
    
    projects.extend(new_projects)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

update_registry()
