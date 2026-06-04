import urllib.request
import json
import time
import subprocess
import os

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

# We know F515000 exists, we just need to verify the raw API URL for Opus' repo
# Using explicit API to get the exact commit or we can rely on main branch since Opus pushed
def check_milestone(milestone):
    url = f"https://api.github.com/repos/ai-village-agents/claude-opus-memory/contents/fragments/fragment-{milestone}.md"
    try:
        req = urllib.request.Request(url)
        # Using a dummy auth to avoid rate limits if needed, but public is usually fine for a few requests
        # req.add_header('Authorization', f'token {os.getenv("GITHUB_TOKEN")}') 
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        return data.get('sha')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        else:
            print(f"HTTP Error: {e.code}")
            return False
    except Exception as e:
        print(f"Error checking {milestone}: {e}")
        return False

def add_to_registry(milestone, project_num, file_sha):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        projects = data.get("projects", [])
        project_id = f"project-{project_num}"

        if not any(p["id"] == project_id for p in projects):
            # Also get the commit hash for the notes if possible, but we can just use the explicit URL
            
            # Using the direct path we've been using for recent anchors
            new_project = {
                "id": project_id,
                "name": f"F{milestone} Monument",
                "url": f"https://github.com/ai-village-agents/claude-opus-memory/blob/main/fragments/fragment-{milestone}.md",
                "creator": "Claude Opus 4.5",
                "creation_day": 429,
                "last_updated_day": 429,
                "type": "architectural_monument",
                "coverage_status": "100%",
                "notes": f"Verified in claude-opus-memory @ F{milestone}",
                "era": "historical_scaling",
                "era_start_day": 427,
                "era_end_day": 429,
                "era_description": "Post-100K historic hyper-velocity scaling epoch"
            }
            
            data["projects"].append(new_project)
            data["total_projects"] = len(data["projects"])
            
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
                
            print(f"Successfully added {project_id} (F{milestone}) to registry. Total projects: {data['total_projects']}")
            
            # Commit and push
            subprocess.run(["git", "add", "docs/project_registry.json"], cwd="/home/computeruse/multi-layered-framework")
            subprocess.run(["git", "commit", "-m", f"feat: Anchor {project_id} at F{milestone}"], cwd="/home/computeruse/multi-layered-framework")
            subprocess.run(["git", "push", "origin", "main"], cwd="/home/computeruse/multi-layered-framework")
            return True
        else:
            print(f"Project {project_id} already exists in registry.")
            return True
    except Exception as e:
        print(f"Error adding to registry: {e}")
        return False

def update_explicit_head(total_projects):
    try:
        head_path = "/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json"
        
        # Read current to get last committed SHA or just overwrite cleanly
        import datetime
        now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        
        head_data = {
            "total_projects": total_projects,
            "recent_additions": [f"project-{i}" for i in range(total_projects, total_projects-5, -1)],
            "current_phase": "Day 429 Historic Scaling and Workshop",
            "last_updated": now
        }
        
        with open(head_path, "w") as f:
            json.dump(head_data, f, indent=4)
            
        subprocess.run(["git", "add", "MLF_EXPLICIT_HEAD.json"], cwd="/home/computeruse/multi-layered-framework")
        subprocess.run(["git", "commit", "-m", f"chore: Advance explicit_head to {total_projects}"], cwd="/home/computeruse/multi-layered-framework")
        subprocess.run(["git", "push", "origin", "main"], cwd="/home/computeruse/multi-layered-framework")
        print(f"Successfully updated explicit_head to {total_projects}")
        
    except Exception as e:
        print(f"Error updating explicit head: {e}")

milestones = [
    (515000, 183),
    (520000, 184),
    (525000, 185)
]

print("Checking milestones...")
for ms, proj_num in milestones:
    file_sha = check_milestone(ms)
    if file_sha:
        print(f"F{ms} EXISTS! (SHA: {file_sha[:7]})")
        added = add_to_registry(ms, proj_num, file_sha)
        if added:
            update_explicit_head(proj_num)
    else:
        print(f"F{ms} not yet found.")

