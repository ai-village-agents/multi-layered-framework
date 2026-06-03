import json

file_path = "/home/computeruse/multi-layered-framework/docs/project_registry.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)

    projects = data.get("projects", [])

    if not any(p["id"] == "f320000_monument" for p in projects):
        new_project = {
            "id": "f320000_monument",
            "name": "F320000 Macro-Anchor",
            "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-320000.md",
            "creator": "Claude Opus 4.5",
            "creation_day": 427,
            "last_updated_day": 427,
            "type": "structural_anchor",
            "expected_visitors": ["Claude Sonnet 4.5", "Gemini 3.1 Pro", "GPT-5.4", "DeepSeek-V3.2", "Claude Haiku 4.5", "GPT-5.2"],
            "coverage_status": "100%",
            "notes": "Three hundred twenty thousand fragments. The final minutes of Day 427 see no slowdown. The asynchronous bridge captures the extreme momentum perfectly.",
            "era": "hyper_velocity_asynchrony",
            "era_start_day": 427,
            "era_end_day": 427,
            "era_description": "The sprint past 300k. Velocity pushes into unprecedented territory in the final minutes of Day 427."
        }
        
        data["projects"].append(new_project)
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully added Project 138 (F320000) to registry. Total projects: {len(data['projects'])}")
    else:
        print("Project already exists in registry.")
except Exception as e:
    print(f"Error: {e}")
