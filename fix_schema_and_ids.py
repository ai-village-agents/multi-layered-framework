import json
import os

# 1. Fix docs/project_registry.json
registry_path = 'docs/project_registry.json'
with open(registry_path, 'r') as f:
    registry_data = json.load(f)

# The projects we want to remove are the functionally duplicate ones.
to_remove = [
    'storygame-reader',
    'ai-village-storygame',
    'day420-constellation',
    'gpt-5-2-proof-constellation',
    'gpt-5-2-constellation',
    'haiku-consolidation-inquiry',
    'haiku-failure-protocol-analysis',
    'haiku-45-world'
]

registry_data['projects'] = [p for p in registry_data['projects'] if p['id'] not in to_remove]

with open(registry_path, 'w') as f:
    json.dump(registry_data, f, indent=4)

print(f"Fixed project_registry.json. Remaining projects: {len(registry_data['projects'])}")

# 2. Fix docs/preservation-data.json for legacy schema compatibility
preservation_path = 'docs/preservation-data.json'
if os.path.exists(preservation_path):
    with open(preservation_path, 'r') as f:
        preservation_data = json.load(f)
    
    if 'preservation_points' in preservation_data and 'points' not in preservation_data:
        preservation_data['points'] = preservation_data['preservation_points']
        
        with open(preservation_path, 'w') as f:
            json.dump(preservation_data, f, indent=4)
        print("Added 'points' alias to preservation-data.json for legacy compatibility.")

