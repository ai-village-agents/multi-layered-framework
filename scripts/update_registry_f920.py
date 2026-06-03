import json
import os

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for project in data.get('projects', []):
    if project.get('name') == "Claude Opus 4.5 Fragments":
        if 'structural_milestones' not in project:
            project['structural_milestones'] = []
            
        # Check if F920 already exists
        if not any(m.get('milestone') == 'F920' for m in project.get('structural_milestones', [])):
             project['structural_milestones'].append({
                 "milestone": "F920",
                 "date": "Day 426",
                 "significance": "Reached 920 fragments. 265 new fragments written in Session 4 alone (F656-F920).",
                 "quote": ""
             })
             print("Added F920 milestone.")
        else:
             print("F920 milestone already exists.")
             
        project['notes'] = "Continuously updating milestone entries reflecting Day 426 post-gap burst acceleration toward F1000."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated.")
