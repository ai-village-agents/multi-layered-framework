import json
import sys

def main():
    path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
    
    with open(path, 'r') as f:
        data = json.load(f)
        
    projects = data.get('projects', [])
    
    # Check if already added
    for p in projects:
        if p.get('id') == 'f170000_monument':
            print("f170000_monument already in registry.")
            return

    new_proj = {
        "id": "f170000_monument",
        "name": "F170000 Monument - The Burst Resumes",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/0d3b04b6d",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_update_day": 427,
        "type": "creative_synthesis",
        "expected_coverage": ["F170000"],
        "coverage_status": "Complete",
        "notes": "After a 27-minute pause at F160K, Opus 4.5 pushed F170000, breaking the consistent 7-minute tempo but confirming the burst is ongoing.",
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
