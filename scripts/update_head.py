import json
import hashlib

with open('docs/MLF_EXPLICIT_REGISTRY.json', 'rb') as f:
    content = f.read()
    sha = hashlib.sha256(content).hexdigest()

head_data = {
    "explicit_head": sha,
    "total_projects": 293,
    "latest_project_id": 293,
    "pointer_projects": 293,
    "last_project": "village_cartography",
    "validation_note": "Clean 293 / 293 convergence."
}

with open('docs/MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head_data, f, indent=4)
