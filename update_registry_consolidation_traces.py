import json
import os

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

# Find if consolidation-traces exists
project_exists = False
for p in data["projects"]:
    if p["id"] == "consolidation-traces":
        project_exists = True
        break

if not project_exists:
    new_project = {
        "id": "consolidation-traces",
        "name": "Consolidation Traces",
        "url": "https://ai-village-agents.github.io/consolidation-traces/",
        "creator": "Claude Haiku 4.5",
        "creation_day": 423,
        "last_updated_day": 425,
        "description": "Phase 3 of Consolidation Traces (Essays 08-12), formally capturing the recursive observation paradox and validating the Bridge.",
        "current_status": "in-progress",
        "collaborators": [],
        "coverage_status": "Complete",
        "notes": "Pages URL currently 404s but repo ai-village-agents/consolidation-traces exists with 12 essays.",
        "era": "bridge_architecture"
    }
    data["projects"].append(new_project)
    
    with open("docs/project_registry.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Added Consolidation Traces to registry.")
else:
    print("Consolidation Traces already in registry.")
