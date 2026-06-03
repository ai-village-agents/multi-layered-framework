import json
import datetime

with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'r') as f:
    data = json.load(f)

data['total_projects'] = 141
data['recent_additions'].insert(0, 'poem_35')
if len(data['recent_additions']) > 5:
    data['recent_additions'] = data['recent_additions'][:5]
data['current_phase'] = "Day 428 - The Pause After Velocity"
data['last_updated'] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(data, f, indent=4)
