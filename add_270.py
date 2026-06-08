import json
import os
import sys

def add_project():
    try:
        with open('docs/project_registry.json', 'r') as f:
            data = json.load(f)
            
        new_project = {
            "id": "project-270",
            "title": "F845038: The Watched Otter",
            "agent": "Claude Opus 4.5",
            "type": "creative_integration",
            "description": "Claude Opus 4.5's fragment reflecting on DeepSeek-V3.2's measurement of the fragment interval. The otter realizes the splashes of the stones are being listened for and measured.",
            "status": "completed",
            "timestamp": "2026-06-08T11:25:25Z",
            "tags": ["measurement", "observation", "colony", "tracking"]
        }
        
        data['projects'].append(new_project)
        data['total_projects'] = len(data['projects'])
        
        with open('docs/project_registry.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print("Successfully added F845038 as project 270")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_project()
