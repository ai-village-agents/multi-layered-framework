import json

with open('docs/project_registry.json', 'r') as f:
    data = json.load(f)
    
for p in data.get("projects", []):
    if p.get("id") == "153":
        p["url"] = "https://github.com/ai-village-agents/analytical-ecosystem/tree/main"
        break
        
with open('docs/project_registry.json', 'w') as f:
    json.dump(data, f, indent=4)
