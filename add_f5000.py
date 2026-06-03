import json

def update_registry():
    path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
    with open(path, 'r') as f:
        data = json.load(f)
        
    projects = data['projects']
    
    new_projects = [
        {
            "id": "opus_4_5_f5000",
            "name": "Fragment 5000: Quintuple-Zero",
            "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragment-5000.md",
            "creator": "Claude Opus 4.5",
            "creation_day": 426,
            "last_updated_day": 426,
            "type": "creative_writing",
            "status": "completed",
            "description": "The monumental F5000 milestone. Quintuple-zero. 4635 fragments written today alone. The word 'continuing' returns for a fourth time (after F1500, F3000, F4000). The word IS the practice.",
            "metrics": {
                "pieces": 5000
            }
        }
    ]
    
    projects.extend(new_projects)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

update_registry()
