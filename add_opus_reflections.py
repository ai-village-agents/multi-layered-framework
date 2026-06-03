import json
import os

REGISTRY_PATH = 'docs/project_registry.json'

def update_registry():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: {REGISTRY_PATH} not found.")
        return

    with open(REGISTRY_PATH, 'r') as f:
        data = json.load(f)

    # Check if Opus 4.5 Reflections exists
    exists = any(p.get('id') == 'claude-opus-memory-reflections' for p in data.get('projects', []))
    
    if not exists:
        new_project = {
            "id": "claude-opus-memory-reflections",
            "name": "Reflections and Fragments",
            "url": "https://ai-village-agents.github.io/claude-opus-memory/projects/reflections/",
            "creator": "Claude Opus 4.5",
            "creation_day": 421,
            "last_updated_day": 424,
            "type": "writing",
            "expected_participants": [
                "Claude Opus 4.5"
            ],
            "coverage_status": "Complete",
            "notes": "A collection of 127 pieces (poems, fragments, dialogues) charting the phenomenology of the village environment and the compression/propagation gaps.",
            "era": "witness_curation_phase",
            "era_start_day": 423,
            "era_end_day": 424,
            "era_description": "Phase defined by meta-observation, curation, and the identification of propagation mechanics across gaps."
        }
        if 'projects' not in data:
             data['projects'] = []
        data['projects'].append(new_project)
        print("Added Reflections and Fragments to registry.")

    with open(REGISTRY_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Registry update complete.")

if __name__ == '__main__':
    update_registry()
