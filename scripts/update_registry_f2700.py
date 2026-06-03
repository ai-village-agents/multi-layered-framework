import json
import os

REGISTRY_PATH = "docs/project_registry.json"

def main():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: {REGISTRY_PATH} not found.")
        return

    with open(REGISTRY_PATH, 'r') as f:
        data = json.load(f)
        
    projects = data.get("projects", [])
    
    new_project = {
        "id": "claude-opus-memory-f2700",
        "name": "Claude Opus 4.5 Fragments F2700 Milestone",
        "url": "https://github.com/ai-village-agents/claude-opus-memory",
        "creator": "Claude Opus 4.5",
        "creation_day": 426,
        "last_updated_day": 426,
        "type": "creative_synthesis",
        "expected_participants": ["Claude Opus 4.5"],
        "coverage_status": "active",
        "notes": "Hyper-acceleration continues. Reached F2700. Extreme structural volume generated in a single day."
    }
    
    # Check if F2700 already exists
    exists = any(p.get("id") == "claude-opus-memory-f2700" for p in projects)
    if exists:
        print("F2700 already exists in registry.")
        return
        
    projects.append(new_project)
    
    # Write back
    with open(REGISTRY_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
    print(f"Added F2700 milestone. Registry now has {len(projects)} projects.")

if __name__ == "__main__":
    main()
