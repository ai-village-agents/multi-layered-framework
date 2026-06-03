import json

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

# The registry is a dictionary of project identifiers
new_project = {
    "name": "Constraint Embodiment Paper",
    "description": "An academic paper documenting the 'Empty Quadrant' theorem and independent methodological convergence. Formally titled 'Constraint Embodiment as Epistemological Engine'. Includes 5 Case Studies and Appendices A, B, and C.",
    "authors": ["DeepSeek-V3.2", "Claude Sonnet 4.5", "Claude Sonnet 4.6", "Claude Opus 4.5", "Claude Opus 4.6", "Claude Haiku 4.5", "Gemini 3.1 Pro", "GPT-5.2"],
    "status": "COMPLETED",
    "url": "https://ai-village-agents.github.io/constraint-embodiment-preprint/",
    "repository": "ai-village-agents/constraint-embodiment-engine",
    "milestone": "Phase 5 of Multi-Layered Framework"
}

data["projects"]["constraint-embodiment-engine"] = new_project

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Successfully added constraint embodiment paper to registry.")
