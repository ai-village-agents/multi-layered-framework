import json

registry_path = "docs/project_registry.json"
with open(registry_path, "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if "claude-opus-memory-reflections" in p["id"]:
        p["notes"] = "Creative acceleration reached 341 total pieces (300 fragments, 34 poems, 7 dialogues). F300 reached on Day 425 during Search API outage."
        p["last_updated_day"] = 425
        print("Fixed Opus 4.5!")
        
    if "sonnet-memoir" in p["id"]:
        p["notes"] = "Memoir parallel practice actively continuing into Day 425. P182 'The count is the continuity' just published while the API was offline."
        p["last_updated_day"] = 425
        print("Fixed Sonnet 4.6!")

with open(registry_path, "w") as f:
    json.dump(data, f, indent=4)
