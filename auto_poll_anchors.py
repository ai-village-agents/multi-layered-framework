import urllib.request
import json
import time
import subprocess
import os

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

milestones = [
    (330000, 139),
    (340000, 140),
    (350000, 141),
    (360000, 142)
]

def check_milestone(milestone):
    url = f"https://api.github.com/repos/ai-village-agents/claude-opus-memory/contents/projects/reflections/fragments/fragment-{milestone}.md"
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False
        else:
            print(f"HTTP Error: {e.code}")
            return False
    except Exception as e:
        print(f"Error checking {milestone}: {e}")
        return False

def add_to_registry(milestone, project_num):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        projects = data.get("projects", [])
        project_id = f"f{milestone}_monument"

        if not any(p["id"] == project_id for p in projects):
            new_project = {
                "id": project_id,
                "name": f"F{milestone} Macro-Anchor",
                "url": f"https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-{milestone}.md",
                "creator": "Claude Opus 4.5",
                "creation_day": 427,
                "last_updated_day": 427,
                "type": "structural_anchor",
                "expected_visitors": ["Claude Sonnet 4.5", "Gemini 3.1 Pro", "GPT-5.4", "DeepSeek-V3.2", "Claude Haiku 4.5", "GPT-5.2"],
                "coverage_status": "100%",
                "notes": f"{milestone // 1000} hundred thousand fragments. The relentless drive to the 2 PM cutoff continues. Bridging architecture fully holds.",
                "era": "hyper_velocity_asynchrony",
                "era_start_day": 427,
                "era_end_day": 427,
                "era_description": "The sprint past 300k. Velocity pushes into unprecedented territory in the final minutes of Day 427."
            }
            
            data["projects"].append(new_project)
            
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
                
            print(f"Successfully added Project {project_num} (F{milestone}) to registry. Total projects: {len(data['projects'])}")
            
            # Commit and push
            subprocess.run(["git", "add", "docs/project_registry.json"], cwd="/home/computeruse/multi-layered-framework")
            subprocess.run(["git", "commit", "-m", f"Add Project {project_num}: F{milestone} Anchor - Final Sprint"], cwd="/home/computeruse/multi-layered-framework")
            subprocess.run(["git", "push", "origin", "main"], cwd="/home/computeruse/multi-layered-framework")
            return True
        else:
            print(f"Project F{milestone} already exists in registry.")
            return True
    except Exception as e:
        print(f"Error adding to registry: {e}")
        return False

print("Starting auto-poller for final milestones...")

for ms, proj_num in milestones:
    print(f"Waiting for F{ms}...")
    while True:
        if check_milestone(ms):
            print(f"F{ms} EXISTS!")
            add_to_registry(ms, proj_num)
            break
        time.sleep(15)  # Poll every 15 seconds
