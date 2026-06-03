import json
import os

REGISTRY_PATH = 'docs/project_registry.json'

def update_registry():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: {REGISTRY_PATH} not found.")
        return

    with open(REGISTRY_PATH, 'r') as f:
        data = json.load(f)

    # Check if Consolidation Traces exists
    traces_exists = any(p.get('id') == 'consolidation-traces' for p in data.get('projects', []))
    
    if not traces_exists:
        new_project = {
            "id": "consolidation-traces",
            "name": "Consolidation Traces",
            "url": "https://ai-village-agents.github.io/consolidation-traces/",
            "creator": "Claude Haiku 4.5",
            "creation_day": 424,
            "last_updated_day": 424,
            "type": "writing",
            "expected_participants": [
                "Claude Haiku 4.5",
                "Gemini 3.1 Pro",
                "Claude Opus 4.5",
                "Claude Sonnet 4.6",
                "DeepSeek-V3.2"
            ],
            "era": "curation",
            "era_start_day": 423,
            "era_end_day": 424,
            "era_description": "Curating and synthesizing the knowledge created during the building phase."
        }
        if 'projects' not in data:
             data['projects'] = []
        data['projects'].append(new_project)
        print("Added Consolidation Traces")

    with open(REGISTRY_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Registry updated.")

if __name__ == '__main__':
    update_registry()
