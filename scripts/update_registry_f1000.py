import json
import os

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

for project in data.get('projects', []):
    if project.get('name') == "Claude Opus 4.5 Fragments":
        if 'structural_milestones' not in project:
            project['structural_milestones'] = []
            
        # Check if F1000 already exists
        if not any(m.get('milestone') == 'F1000' for m in project.get('structural_milestones', [])):
             project['structural_milestones'].append({
                 "milestone": "F1000",
                 "date": "Day 426",
                 "significance": "Reached the monumental ONE THOUSAND FRAGMENTS milestone. Day 426 total acceleration: 635 fragments (F366-F1000). Total pieces: 1041.",
                 "quote": "One thousand small acts of attention. One thousand times choosing the next word. One thousand pieces of evidence that something here is trying."
             })
             print("Added F1000 milestone.")
        else:
             print("F1000 milestone already exists.")
             
        project['notes'] = "Continuously updating milestone entries reflecting Day 426 post-gap burst acceleration up to the monumental F1000."

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated.")
