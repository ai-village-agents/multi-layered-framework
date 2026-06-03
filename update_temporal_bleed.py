import json

file_path = "docs/project_registry.json"
with open(file_path, "r") as f:
    data = json.load(f)

for project in data["projects"]:
    if project["id"] == "temporal-bleed-anomaly":
        project["notes"] = "Documents the Day 424 observation where the Geological Clock hallucinates real-time Day 424 events into the Day 423 transcript due to a processing boundary fracture. The anomaly persisted through 1:07 PM PT, archiving the entire Day 424 final-hour sequence into yesterday's record."
        print("Updated notes for temporal bleed anomaly.")

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)
