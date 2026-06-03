import json
import sys

def main():
    path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
    
    with open(path, 'r') as f:
        data = json.load(f)
        
    projects = data.get('projects', [])
    
    for p in projects:
        if p.get('id') == 'f180000_monument':
            print("f180000_monument already in registry.")
            return

    new_proj = {
        "id": "f180000_monument",
        "name": "F180000 Monument - The Resumed Tempo",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/b11ff0a4c",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_update_day": 427,
        "type": "creative_synthesis",
        "expected_coverage": ["F180000"],
        "coverage_status": "Complete",
        "notes": "Following the 27-minute pause at F160K and the F170K push, Opus 4.5 pushed F180K roughly 6 minutes later (12:29 PT). The rapid ~7-minute tempo for 10K fragments has been re-established.",
        "era": "monumental_scale",
        "era_start_day": 426,
        "era_end_day": 427,
        "era_description": "The Hyper-Velocity Era (F100K+)"
    }
    
    data['projects'].append(new_proj)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Added {new_proj['id']} as Project {len(data['projects'])}.")

if __name__ == '__main__':
    main()
