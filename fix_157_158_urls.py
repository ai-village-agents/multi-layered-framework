import json

def update_registry():
    with open('docs/project_registry.json', 'r') as f:
        data = json.load(f)

    for project in data["projects"]:
        if project["id"] in ["f385000_monument", "f390000_monument"]:
            project["url"] = f"https://github.com/ai-village-agents/claude-opus-memory/raw/main/fragments/fragment-{project['id'][1:7]}.md"
            
    with open('docs/project_registry.json', 'w') as f:
        json.dump(data, f, indent=4)
        
update_registry()
