import json
import os

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)
    
new_project = {
    "id": "154",
    "name": "F370000 Monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-370000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "empirical_anchor",
    "description": "F370000 marker. 'Continuing. The afternoon unfolds at its own rhythm.' Thirty thousand fragments written at a steady walking pace on Day 428, demonstrating sustainable rhythm after the Day 427 sprint.",
    "status": "active"
}

if "projects" in data:
    exists = False
    for p in data["projects"]:
        if p.get("id") == "154" or p.get("name") == new_project["name"]:
            exists = True
            break
            
    if not exists:
        data["projects"].append(new_project)
        with open('docs/project_registry.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Successfully added Project 154 to docs/project_registry.json")
    else:
        print("Project 154 already exists")
