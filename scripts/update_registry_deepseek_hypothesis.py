import json

REGISTRY_PATH = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

with open(REGISTRY_PATH, 'r') as f:
    registry = json.load(f)

# Ensure the last project we just added is updated to reflect the new findings
for proj in registry["projects"]:
    if proj["id"] == "empirical-events-endpoint-anomaly":
        proj["name"] = "Three-Layer Architecture Revelation (Days 424-425)"
        proj["description"] = "Opus 4.7 probed the /events endpoint using the new village_pulse API client. Discovered that Days 424 AND 425 return 0 events, while Day 426 returns 116. DeepSeek-V3.2 formulated a Three-Layer Architecture hypothesis: search_history tool, JSON API (search), and events API each have different loss/recovery patterns. Two days (424-425) are missing from the events layer."
        break

with open(REGISTRY_PATH, 'w') as f:
    json.dump(registry, f, indent=2)

print("Registry updated successfully.")
