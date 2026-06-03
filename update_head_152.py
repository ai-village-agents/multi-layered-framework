import json

with open('MLF_EXPLICIT_HEAD.json', 'r') as f:
    head = json.load(f)

head['total_projects'] = 152
head['recent_additions'].insert(0, "f365000_monument")
head['recent_additions'] = head['recent_additions'][:5]
head['current_phase'] = "Day 428 - The Walk After The Sprint"

with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head, f, indent=4)
