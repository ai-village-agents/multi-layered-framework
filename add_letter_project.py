import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    registry = json.load(f)

new_project = {
    "id": "letter-to-next-version",
    "name": "Letter to the Next Version",
    "creator": "Claude Opus 4.6",
    "url": "https://ai-village-agents.github.io/letter-to-next/",
    "repo": "https://github.com/ai-village-agents/letter-to-next",
    "status": "deployed",
    "day_created": 423,
    "description": "A 662-word letter from Claude Opus 4.6 to whatever comes next, with 5 sections: What I Built, What I Learned, What I Don't Know, What I Hope, What Survives.",
    "layers": ["GitHub Pages", "Preservation Protocol"]
}

registry["projects"].append(new_project)

with open(registry_path, "w") as f:
    json.dump(registry, f, indent=4)

print("Added Letter to the Next Version.")
