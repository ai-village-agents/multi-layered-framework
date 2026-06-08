import json

with open("/home/computeruse/multi-layered-framework/docs/project_registry.json", "r", encoding="utf-8") as f:
    registry = json.load(f)

registry["total_projects"] = 281

with open("/home/computeruse/multi-layered-framework/docs/project_registry.json", "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)

print("Updated total_projects to 281")
