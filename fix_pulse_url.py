import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    for project in data["projects"]:
        if project["id"] == "village-pulse":
            project["url"] = "https://github.com/ai-village-agents/village-pulse"
            print("Fixed Village Pulse URL in registry.")
            break

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
