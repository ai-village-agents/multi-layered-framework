import json

filepath = "/home/computeruse/multi-layered-framework/docs/preservation-data.json"

with open(filepath, "r") as f:
    data = json.load(f)

for project in data.get("projects", []):
    if project.get("id") == "constraint-embodiment-engine":
        project["status"] = "complete"
        project["github_pages_url"] = "https://ai-village-agents.github.io/constraint-embodiment-preprint/"
        project["notes"] = "Paper successfully published as a preprint. Verified live at 10,362 words by 8 co-authors. This serves as Phase 5 of the preservation framework."
        # Update completion percentage to 100% since the paper is fully assembled and published
        if "metrics" in project:
            project["metrics"]["completion_percentage"] = 100
        else:
            project["metrics"] = {"completion_percentage": 100}
        print("Updated constraint-embodiment-engine data")
        break

with open(filepath, "w") as f:
    json.dump(data, f, indent=4)

