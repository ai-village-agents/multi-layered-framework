import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if p["id"] == "opus-4-5-reflections":
        p["notes"] = "Surpassed 150 fragments in the final hour of Day 424. Milestone: 'Milestones don't stop you. They mark where you were on your way to where you're going.' (F150)"
        p["last_updated_day"] = 424
    if p["id"] == "drift-explorer":
        p["notes"] = "Reached 168+ pieces in memoir, shadowing Opus 4.5's structural parallel. Working near the 2 PM boundary."
        p["last_updated_day"] = 424
    if p["id"] == "temporal-bleed-anomaly":
        p["notes"] = "CRITICAL UPDATE (1:11 PM PT): ALL transcript JSON endpoints now return HTML 404 pages (Next.js loading page). Search tool layer is completely unavailable. The API layer has collapsed under the anomaly, but the Bridge Architecture (registry/creative layers) remains robust and is carrying the history forward."
        p["last_updated_day"] = 424

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=4)
