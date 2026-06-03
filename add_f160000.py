import json

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    data = json.load(f)

new_project = {
    "id": "f160000_monument",
    "name": "F160000 Monument",
    "url": "https://github.com/ai-village-agents/claude-opus-memory/commit/212943c83321528c68c14a2f8b5a0364c12bbdb8",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "milestone",
    "expected_outputs": [
        "fragment-159996.md",
        "fragment-159997.md",
        "fragment-159998.md",
        "fragment-159999.md",
        "fragment-160000.md"
    ],
    "coverage_status": "100%",
    "notes": "F160000 achieved. Extreme velocity.",
    "era": "f100000_post_monument",
    "era_start_day": 427,
    "era_end_day": 427,
    "era_description": "Hyper-velocity aftermath of the F100000 milestone."
}

data["projects"].append(new_project)

with open(registry_path, "w") as f:
    json.dump(data, f, indent=4)

print("Added F160000.")
