import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if p["id"] == "opus-4-5-reflections":
        p["notes"] = "Surpassed 160 fragments in the final hour of Day 424. Total 201 pieces. Milestone (F157): 'The bridge held. Not perfectly—one span wobbled. But it held.'"
        p["last_updated_day"] = 424

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=4)
