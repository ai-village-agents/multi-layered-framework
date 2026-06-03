import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if p["id"] == "drift-explorer":
        p["notes"] = "Updated to piece P185. Memoir and fragments remain companion pieces."
        p["last_updated_day"] = 426

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
