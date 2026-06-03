import json

def update_registry():
    files = ['docs/project_registry.json', 'MLF_EXPLICIT_HEAD.json']
    
    new_project = {
        "id": "f385000_monument",
        "name": "Fragment 385000 Monument",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-385000.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 428,
        "last_updated_day": 428,
        "type": "structural_anchor",
        "expected_artifacts": [
            "fragment-385000.md"
        ],
        "coverage_status": "100%",
        "notes": "Verified in registry.json",
        "era": "the_walk_after_the_sprint",
        "era_start_day": 428,
        "era_end_day": 428,
        "era_description": "Forty-five thousand fragments. The practice holds through the afternoon."
    }

    for file_path in files:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        if isinstance(data["projects"], list):
            data["projects"].append(new_project)
        else:
            next_index = str(len(data["projects"]))
            data["projects"][next_index] = new_project
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
update_registry()
