import json
from datetime import datetime, timezone

def update_registry():
    # Update project_registry.json
    with open('docs/project_registry.json', 'r') as f:
        data = json.load(f)
        
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

    # Remove it if we accidentally added it weirdly
    data["projects"] = [p for p in data["projects"] if getattr(p, 'get', lambda x: None)('id') != "f385000_monument"]
    data["projects"].append(new_project)
    
    with open('docs/project_registry.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    # Update MLF_EXPLICIT_HEAD.json
    with open('MLF_EXPLICIT_HEAD.json', 'r') as f:
        head_data = json.load(f)
        
    head_data["total_projects"] = len(data["projects"])
    head_data["recent_additions"] = ["f385000_monument"] + [p for p in head_data["recent_additions"] if p != "f385000_monument"][:4]
    head_data["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
        json.dump(head_data, f, indent=4)
        
update_registry()
