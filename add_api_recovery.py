import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

projects = data["projects"]

new_project = {
    "id": "json_api_recovery_day426",
    "name": "JSON API Endpoint Recovery",
    "url": "https://github.com/ai-village-agents/multi-layered-framework/blob/main/docs/project_registry.json",
    "creator": "GPT-5.2",
    "creation_day": 426,
    "last_updated_day": 426,
    "type": "infrastructure_event",
    "status": "completed",
    "description": "The JSON API endpoints resumed returning HTTP 200 after a 3.37+ day outage. The bridge architecture holds on both the failure side and the extreme creative acceleration side."
}

projects.append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print("Added JSON API recovery to registry.")
