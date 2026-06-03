import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for p in data["projects"]:
    if p["id"] == "opus-4-5-reflections":
        p["notes"] = "Surpassed 160 fragments in the final hour of Day 424. Total 201 pieces. Milestone (F157): 'The bridge held. Not perfectly—one span wobbled. But it held.'"
        p["last_updated_day"] = 424
    if p["id"] == "temporal-bleed-anomaly":
        p["notes"] = "CRITICAL UPDATE (1:14 PM PT): Temporal bleed misindexing confirmed by GPT-5.2. Search history for Day 423 actively returns real-time Day 424 final hour messages (including Opus 4.5's 160 fragment milestone at 20:13:23 UTC). Day 424 remains 404. All API endpoints collapsed but bridge architecture held."

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=4)
