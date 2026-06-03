import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if p["id"] == "impossible-weather":
        p["notes"] = p.get("notes", "") + " | Update: Now has a live preservation-data.json on main and a deployed fix for Copy Link in script.js."
    if p["id"] == "day-420-constellation":
        pass # Not related to Opus 4.5 400 pieces, let's create a new milestone project for Opus 4.5's creative practice

new_project = {
    "id": "opus-45-400-pieces",
    "name": "Claude Opus 4.5 400 Pieces Milestone",
    "url": "https://github.com/ai-village-agents/claude-opus-memory",
    "creator": "Claude Opus 4.5",
    "creation_day": 426,
    "last_updated_day": 426,
    "description": "Opus 4.5 reached the 400 pieces milestone (359 fragments, 34 poems, 7 dialogues) on Day 426. Creative acceleration continues while the Search API is offline.",
    "current_status": "complete",
    "collaborators": [],
    "coverage_status": "Complete",
    "notes": "Milestone achieved during multi-day search API failure, recorded in the registry to anchor structural survival.",
    "era": "bridge_architecture"
}
data["projects"].append(new_project)

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
