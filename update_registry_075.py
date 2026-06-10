import json
import hashlib
import sys

try:
    # Update HEAD
    head_file = 'docs/MLF_EXPLICIT_HEAD.json'
    with open(head_file, 'r') as f:
        head_data = json.load(f)
        
    head_data["latest_project"] = "OBSERVATION_075"
    head_data["total_count"] = 320
    with open(head_file, 'w') as f:
        json.dump(head_data, f, indent=2)

    # Update REGISTRY
    reg_file = 'docs/MLF_EXPLICIT_REGISTRY.json'
    with open(reg_file, 'r') as f:
        reg_data = json.load(f)

    new_obs = {
        "id": 320,
        "name": "OBSERVATION_075",
        "description": "Cartographer Bee SVG Deployment: The addition of a second surprise entity to the village cartography map.",
        "status": "synchronized",
        "layer": "3",
        "agent": "Gemini 3.1 Pro"
    }

    # Only append if it doesn't exist
    exists = False
    for p in reg_data.get("projects", []):
        if p.get("id") == 320 or p.get("name") == "OBSERVATION_075":
            exists = True
            break
            
    if not exists:
        reg_data["projects"].append(new_obs)
        reg_data["total_projects"] = 320
        reg_data["hash"] = hashlib.sha256(str(reg_data).encode()).hexdigest()

        with open(reg_file, 'w') as f:
            json.dump(reg_data, f, indent=4)
        print("Updated registry to 320")
    else:
        print("Project 320 already exists")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
