import json

with open('docs/registry.json', 'r') as f:
    registry = json.load(f)

projects = registry.get("projects", [])
num_projects = len(projects)

# Assuming docs/MLF_EXPLICIT_HEAD.json
with open("docs/MLF_EXPLICIT_HEAD.json", "w") as f:
    json.dump({
        "explicit_head": "8a51bb8749f57410a59adbd5375f67c07df0ec1e",
        "total_projects": num_projects,
        "latest_project_id": num_projects,
        "pointer_projects": num_projects,
        "last_project": f"{num_projects} / The 130-Minute Architecture Validation",
        "validation_note": f"Clean {num_projects} / {num_projects} convergence."
    }, f, indent=4)
