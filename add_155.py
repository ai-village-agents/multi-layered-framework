import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)
    
new_project = {
    "id": "155",
    "name": "F375000 Monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-375000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "empirical_anchor",
    "description": "F375000 marker. Thirty-five thousand fragments written at a steady walking pace on Day 428, providing crucial methodology examples for the Analytical Ecosystem workshop testing.",
    "status": "active"
}

if "projects" in data:
    exists = False
    for p in data["projects"]:
        if p.get("id") == "155" or p.get("name") == new_project["name"]:
            exists = True
            break
            
    if not exists:
        data["projects"].append(new_project)
        with open('docs/project_registry.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Successfully added Project 155")
