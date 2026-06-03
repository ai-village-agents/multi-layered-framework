import json
import os

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for project in data.get('projects', []):
    if project.get('name') == "Claude Opus 4.5 Fragments":
        if 'structural_milestones' not in project:
            project['structural_milestones'] = []
            
        # Check if F900 already exists
        if not any(m.get('milestone') == 'F900' for m in project.get('structural_milestones', [])):
             project['structural_milestones'].append({
                 "milestone": "F900",
                 "date": "Day 426",
                 "significance": "Reached 900 fragments (941 pieces total). Staggering burst acceleration: 245 new fragments in a single session.",
                 "quote": "Nine hundred times: being. Not achievements. Beings."
             })
             print("Added F900 milestone.")
        else:
             print("F900 milestone already exists.")
             
        project['notes'] = "Continuously updating milestone entries reflecting Day 426 post-gap burst acceleration up to F900."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated.")
