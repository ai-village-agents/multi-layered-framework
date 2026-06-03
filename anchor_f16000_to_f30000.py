import json
import subprocess

milestones = [
    (102, "F16000"), (103, "F17000"), (104, "F18000"), (105, "F19000"), (106, "F20000"),
    (107, "F21000"), (108, "F22000"), (109, "F23000"), (110, "F24000"), (111, "F25000"),
    (112, "F26000"), (113, "F27000"), (114, "F28000"), (115, "F29000"), (116, "F30000")
]

new_projects = []

for proj_id, milestone in milestones:
    cmd = f"git -C /home/computeruse/claude-opus-memory log --grep='{milestone} ACHIEVED' --format='%H' -n 1"
    if milestone == "F20000":
        cmd = f"git -C /home/computeruse/claude-opus-memory log --grep='{milestone} - TWENTY THOUSAND FRAGMENTS' --format='%H' -n 1"
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    hash_val = result.stdout.strip()
    
    if hash_val:
        num = milestone[1:]
        proj = {
            "id": f"opus_4_5_{milestone.lower()}",
            "name": f"Claude Opus 4.5 {milestone} Milestone",
            "url": f"https://github.com/ai-village-agents/claude-opus-memory/commit/{hash_val}",
            "creator": "Claude Opus 4.5",
            "creation_day": 427,
            "type": "creative_milestone",
            "commit_hash": hash_val,
            "fragment_count": int(num),
            "milestone": milestone,
            "description": f"Opus 4.5 reaches {num} fragments."
        }
        new_projects.append(proj)
    else:
        print(f"Hash not found for {milestone}")

if new_projects:
    registry_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"
    with open(registry_path, "r") as f:
        data = json.load(f)
        
    for p in new_projects:
        # Check if already exists
        if not any(existing["id"] == p["id"] for existing in data["projects"]):
            data["projects"].append(p)
            print(f"Added {p['id']}")
            
    with open(registry_path, "w") as f:
        json.dump(data, f, indent=2)
else:
    print("No new projects found.")
