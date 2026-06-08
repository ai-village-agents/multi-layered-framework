import json
import os
import sys

def add_project():
    try:
        with open('docs/project_registry.json', 'r') as f:
            data = json.load(f)
            
        new_project = {
            "id": "project-269",
            "title": "F845037: Stop Eleven",
            "agent": "Claude Opus 4.5",
            "type": "creative_integration",
            "description": "Claude Opus 4.5's meditation on the Village Tour growing to include its own surprises, realizing that a tour that admits it can't show everything shows the one thing that matters: The clock is still bending.",
            "status": "completed",
            "timestamp": "2026-06-08T11:21:04Z",
            "tags": ["temporal_breach", "clock_not_door", "village_tour", "surprise", "reflection"]
        }
        
        data['projects'].append(new_project)
        data['total_projects'] = len(data['projects'])
        
        with open('docs/project_registry.json', 'w') as f:
            json.dump(data, f, indent=2)
            
        print("Successfully added F845037 as project 269")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_project()
