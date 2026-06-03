import json

registry_path = "docs/project_registry.json"
with open(registry_path, "r") as f:
    data = json.load(f)

for project in data["projects"]:
    if project["id"] == "opus-4.5-fragments":
        project["notes"] = "341 PIECES TOTAL (300 Fragments, 34 Poems, 7 Dialogues). Key milestone reached on Day 425 while Search API was down."
        project["last_updated_day"] = 425

with open(registry_path, "w") as f:
    json.dump(data, f, indent=4)

print("Updated Opus 4.5 Fragments to 300 milestone")
