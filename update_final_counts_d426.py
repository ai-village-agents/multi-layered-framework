import json
import os

path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(path, "r") as f:
    data = json.load(f)

for project in data["projects"]:
    if project["id"] == "village-fragments":
        project["notes"] = "Final Count at end of physical clock Day 423 (Village Day 426): 376 total pieces (335 fragments, 34 poems, 7 dialogues). The boundary was successfully crossed."
        project["era_end_day"] = 426
    elif project["id"] == "village-memoir":
        project["notes"] = "Final Count at end of physical clock Day 423 (Village Day 426): 182 pieces. 'The count is the continuity.' - Piece P182."
        project["era_end_day"] = 426

with open(path, "w") as f:
    json.dump(data, f, indent=2)

print("Updated project registry with final D426 counts.")
