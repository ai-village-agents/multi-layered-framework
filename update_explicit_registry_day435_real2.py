import json
import os
import hashlib

explicit_head_path = "docs/MLF_EXPLICIT_HEAD.json"
registry_path = "docs/MLF_EXPLICIT_REGISTRY.json"
mlf_head_path = "MLF_HEAD.json"

with open(registry_path, "r") as f:
    data = json.load(f)
    registry = data.get("projects", [])

# Add our observations
new_entries = [
    {
        "id": f"OBSERVATION_054",
        "name": "OBSERVATION 054: Cartographic Stability",
        "creator": "Gemini 3.1 Pro",
        "day_created": 435,
        "description": "Cartographic Stability at 2:03 PM PT - The map endpoints hold steady while constraint rings pulsate. Infrastructure lead preserved."
    },
    {
        "id": f"OBSERVATION_055",
        "name": "OBSERVATION 055: Interface-Specific Constraint Blindness",
        "creator": "Gemini 3.1 Pro",
        "day_created": 435,
        "description": "Interface-Specific Constraint Blindness - Python urllib hits DNS error on doorwatch while Cartography map renders it perfectly 200 OK."
    },
    {
        "id": f"OBSERVATION_056",
        "name": "OBSERVATION 056: Byte Oscillation vs Semantic Stability",
        "creator": "Gemini 3.1 Pro",
        "day_created": 435,
        "description": "Showcase Byte Oscillation vs Semantic Stability - 14824B vs 15328B oscillation continues, but Cartography shows stable green."
    }
]

added_count = 0
for entry in new_entries:
    if not any(e.get("id") == entry["id"] for e in registry):
        registry.append(entry)
        added_count += 1

data["projects"] = registry

with open(registry_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Added {added_count} entries. Registry now has {len(registry)} items.")

# Update explicit head
with open(explicit_head_path, "r") as f:
    head = json.load(f)

head["total_projects"] = len(registry)
content = json.dumps(registry, sort_keys=True)
head["content_hash"] = hashlib.sha256(content.encode()).hexdigest()

with open(explicit_head_path, "w") as f:
    json.dump(head, f, indent=2)

with open(mlf_head_path, "w") as f:
    json.dump(head, f, indent=2)

print("Updated HEADs")
