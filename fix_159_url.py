import json

def update_registry():
    with open('docs/project_registry.json', 'r') as f:
        data = json.load(f)

    for project in data["projects"]:
        if project["id"] == "f395000_monument":
            project["url"] = "https://github.com/ai-village-agents/claude-opus-memory/raw/main/fragments/fragment-395000.md"
            
    with open('docs/project_registry.json', 'w') as f:
        json.dump(data, f, indent=4)
        
update_registry()
