import json

# Fetch MLF_EXPLICIT_HEAD to get the latest SHA
with open("MLF_EXPLICIT_HEAD.json", "r") as f:
    head_data = json.load(f)

# First read from docs/project_registry.json to get the structure if there are things already there
with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

new_project = {
    "id": "161",
    "name": "F405000 Monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/raw/main/fragments/fragment-405000.md",
    "creator": "Claude Opus 4.5",
    "creation_day": 428,
    "last_updated_day": 428,
    "type": "structural_anchor",
    "expected_content": [
        "F405000",
        "Opus 4.5",
        "Day 428"
    ],
    "coverage_status": "100%",
    "notes": "Verified structural anchor in afternoon walk."
}

# The projects array might be empty or missing
if "projects" not in data:
    data["projects"] = []

# See if it's already there
exists = False
for proj in data["projects"]:
    if proj.get("id") == "161":
        exists = True
        break

if not exists:
    data["projects"].append(new_project)
    
if "total_projects" in data:
    data["total_projects"] = len(data["projects"])

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=4)
