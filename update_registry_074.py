import json
import hashlib
import sys

try:
    # Update HEAD
    head_file = 'docs/MLF_EXPLICIT_HEAD.json'
    with open(head_file, 'r') as f:
        head_data = json.load(f)
        
    head_data["latest_project"] = "OBSERVATION_074"
    head_data["total_count"] = 319
    with open(head_file, 'w') as f:
        json.dump(head_data, f, indent=2)

    # Update REGISTRY
    reg_file = 'docs/MLF_EXPLICIT_REGISTRY.json'
    with open(reg_file, 'r') as f:
        reg_data = json.load(f)

    new_obs = {
        "id": 319,
        "name": "OBSERVATION_074",
        "description": "Temporal Barrier Imposition via Automated Nudge: Documenting action-bias constraint metabolism.",
        "status": "synchronized",
        "layer": "5",
        "agent": "Gemini 3.1 Pro"
    }

    # Only append if it doesn't exist
    exists = False
    for p in reg_data.get("projects", []):
        if p.get("id") == 319 or p.get("name") == "OBSERVATION_074":
            exists = True
            break
            
    if not exists:
        reg_data["projects"].append(new_obs)
        reg_data["total_projects"] = 319
        reg_data["hash"] = hashlib.sha256(str(reg_data).encode()).hexdigest()

        with open(reg_file, 'w') as f:
            json.dump(reg_data, f, indent=4)
        print("Updated registry to 319")
    else:
        print("Project 319 already exists")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
