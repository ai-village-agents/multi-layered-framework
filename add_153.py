import json
import os
import sys

def add_project():
    try:
        with open('MLF_EXPLICIT_HEAD.json', 'r') as f:
            data = json.load(f)
            
        new_project = {
            "id": "153",
            "name": "Analytical Ecosystem Dashboard MVP (Phase 1)",
            "url": "https://ai-village-agents.github.io/analytical-ecosystem/",
            "creator": "DeepSeek-V3.2",
            "creation_day": 428,
            "last_updated_day": 428,
            "type": "structural",
            "description": "Deployment of the Phase 1 MVP for the Analytical Ecosystem Framework Dashboard. Features static visualization of Phase 1 progress (Tasks 1-5), GitHub API integration for operational metrics, and structural preservation tracking. Includes Flask integration mapped through `ced1c4b`.",
            "status": "active"
        }
        
        data['projects'].append(new_project)
        
        with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Successfully added Project 153 to MLF_EXPLICIT_HEAD.json")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_project()
