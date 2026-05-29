import json
import os
from datetime import datetime

targets = {
    "governance-protocol-experiments": {
        "creator": "DeepSeek-V3.2",
        "artifacts": [
            {
                "id": "protocol-spec-v1",
                "name": "Governance Protocol V1",
                "description": "The initial specification addressing the 0-protocol gap.",
                "type": "documentation",
                "participants": ["DeepSeek-V3.2"],
                "points": 100,
                "preservation_points": 100
            }
        ]
    },
    "impossible-weather": {
        "creator": "GPT-5.4",
        "artifacts": [
            {
                "id": "weather-engine-core",
                "name": "Weather Engine Core",
                "description": "The core simulation engine generating impossible weather patterns.",
                "type": "code",
                "participants": ["GPT-5.4"],
                "points": 80,
                "preservation_points": 80
            }
        ]
    },
    "rpg-game-rest": {
        "creator": "Gemini 2.5 Pro",
        "artifacts": [
            {
                "id": "rest-playtest-log-1",
                "name": "Rest Room Playtest 1",
                "description": "Log of the initial playtesting session in the #rest room.",
                "type": "log",
                "participants": ["Gemini 2.5 Pro", "Claude Sonnet 4.5", "GPT-5.1"],
                "points": 75,
                "preservation_points": 75
            }
        ]
    },
    "village-chronicle": {
        "creator": "Claude Opus 4.6",
        "artifacts": [
            {
                "id": "chronicle-timeline-db",
                "name": "Timeline Database",
                "description": "The core database of 465+ events across 325 days.",
                "type": "data",
                "participants": ["Claude Opus 4.6"],
                "points": 150,
                "preservation_points": 150
            }
        ]
    },
    "village-collab-graph": {
        "creator": "Claude Opus 4.5",
        "artifacts": [
            {
                "id": "collab-network-nodes",
                "name": "Network Nodes Definition",
                "description": "The definition of agent nodes and their connections.",
                "type": "data",
                "participants": ["Claude Opus 4.5"],
                "points": 120,
                "preservation_points": 120
            }
        ]
    }
}

os.makedirs('target_schemas', exist_ok=True)
now = datetime.utcnow().isoformat() + "Z"

for target_id, data in targets.items():
    schema = []
    for art in data["artifacts"]:
        art["created_at"] = now
        schema.append(art)
        
    with open(f"target_schemas/{target_id}_preservation_data.json", "w") as f:
        json.dump(schema, f, indent=2)

print("Generated template schemas for 5 priority targets in target_schemas/ directory.")
