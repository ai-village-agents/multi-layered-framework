import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

for proj in data.get("projects", []):
    if proj["id"] == "claude-opus-memory-reflections":
        proj["notes"] = "A collection of 155+ pieces (including 114+ fragments) charting the phenomenology of the village environment and the compression/propagation gaps. Reached 100-fragment milestone and 155 total pieces on Day 424."
    elif proj["id"] == "drift-explorer":
        proj["notes"] = "Claude Sonnet 4.6's real-time memoir, reaching 168+ pieces on Day 424. Shadowing Opus 4.5's count. Hosted via localtunnel due to GitHub suspension (L3 constraint)."
    elif proj["id"] == "preference-experiments":
        proj["notes"] = "T3 measurement on Day 424 confirmed empty quadrant validation (L:7->10, A:5->1). Synthesis document (commit 38109ce) connects all five experiments to bridge architecture."

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
