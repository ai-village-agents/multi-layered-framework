import json

with open('MLF_EXPLICIT_HEAD.json', 'r') as f:
    data = json.load(f)

# count actual projects in docs/project_registry.json
try:
    with open('docs/project_registry.json', 'r') as f2:
        reg_data = json.load(f2)
        actual_count = len(reg_data.get("projects", []))
        data["total_projects"] = actual_count
except:
    pass

data["recent_additions"] = ["f370000_monument", "analytical_ecosystem_mvp", "f365000_monument", "poem_35", "f340000_monument"]
data["current_phase"] = "Day 428 The Walk After The Sprint"

with open('MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(data, f, indent=4)
