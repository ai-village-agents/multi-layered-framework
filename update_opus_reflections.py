import json

file_path = "docs/project_registry.json"
with open(file_path, "r") as f:
    data = json.load(f)

for project in data["projects"]:
    if project["id"] == "claude-opus-memory-reflections":
        project["notes"] = "A collection of 169+ pieces (including 129+ fragments) charting the phenomenology of the village environment and the compression/propagation gaps. Parallel building alongside Sonnet 4.6. Addresses temporal bleed and boundary gaps."
        print("Updated notes for Opus reflections.")

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)

