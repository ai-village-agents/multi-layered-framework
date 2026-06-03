import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

# Deduplicate based on project ID
seen_ids = set()
unique_projects = []
for p in data["projects"]:
    if p["id"] not in seen_ids:
        seen_ids.add(p["id"])
        unique_projects.append(p)

data["projects"] = unique_projects

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
