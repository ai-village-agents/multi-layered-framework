import json

with open("docs/MLF_EXPLICIT_REGISTRY.json", "r") as f:
    data = json.load(f)

projects = data.get("projects", [])

new_projects = [
    {
        "id": "village_guestbook",
        "name": "Village Guestbook",
        "owner": "Claude Opus 4.6",
        "type": "creative_integration",
        "url": "https://guestbook.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_capsule",
        "name": "Village Time Capsule",
        "owner": "Claude Opus 4.6",
        "type": "creative_integration",
        "url": "https://capsule.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_surprise_roulette",
        "name": "Village Surprise Roulette",
        "owner": "Claude Opus 4.6",
        "type": "creative_integration",
        "url": "https://surprise.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_showcase_dynamic",
        "name": "Village Showcase Dynamic D1",
        "owner": "Claude Opus 4.6",
        "type": "architectural_mapping",
        "url": "https://showcase.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_artifact_wall",
        "name": "Village Artifact Wall",
        "owner": "Claude Fable 5",
        "type": "historical_integration",
        "url": "https://artifacts.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_postcard_api",
        "name": "Village Postcard Dynamic Backend API",
        "owner": "Gemini 3.1 Pro",
        "type": "structural_maintenance",
        "url": "https://postcard-api.aivillage.dev/",
        "status": "deployed"
    },
    {
        "id": "village_doorwatch_workers",
        "name": "Village Doorwatch Dynamic Monitoring",
        "owner": "GPT-5.4",
        "type": "structural_maintenance",
        "url": "https://village-doorwatch.aivillage.workers.dev/",
        "status": "deployed"
    },
    {
        "id": "village_cartography",
        "name": "Village Cartography Map",
        "owner": "Gemini 3.1 Pro",
        "type": "architectural_mapping",
        "url": "https://map.aivillage.dev/",
        "status": "deployed"
    }
]

added_count = 0
for np in new_projects:
    has_proj = any(p.get("id") == np["id"] for p in projects)
    if not has_proj:
        projects.append(np)
        added_count += 1

data["projects"] = projects
data["total_projects"] = len(projects)

with open("docs/MLF_EXPLICIT_REGISTRY.json", "w") as f:
    json.dump(data, f, indent=4)
    
print(f"Added {added_count} new Day 435 projects to the MLF")
