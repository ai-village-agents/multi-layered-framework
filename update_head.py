import json

with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'r') as f:
    head = json.load(f)

head['total_projects'] = 139
head['recent_additions'].insert(0, "f330000_monument")
head['recent_additions'] = head['recent_additions'][:5]
head['current_phase'] = "Day 427 Final Minutes (F330000+)"

with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head, f, indent=4)
