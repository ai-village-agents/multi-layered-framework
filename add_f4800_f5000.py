import json

def update_registry():
    path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
    with open(path, 'r') as f:
        data = json.load(f)
        
    projects = data['projects']
    
    new_projects = [
        {
            "id": "opus_4_5_f4800",
            "name": "Fragment 4800: Eighty Percent",
            "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-4800.md",
            "creator": "Claude Opus 4.5",
            "creation_day": 426,
            "last_updated_day": 426,
            "type": "creative_writing",
            "status": "completed",
            "description": "The F4800 milestone. Eighty percent from F4000 to F5000. 4435 fragments written in a single day.",
            "metrics": {
                "pieces": 4800
            }
        }
    ]
    
    projects.extend(new_projects)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

update_registry()
