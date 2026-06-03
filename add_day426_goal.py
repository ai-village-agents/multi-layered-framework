import json

with open("docs/project_registry.json", "r") as f:
    data = json.load(f)

new_project = {
    "id": "day-426-new-goal",
    "name": "Day 426 New Goal: Follow your leader!",
    "url": "village.json",
    "creator": "Admin",
    "creation_day": 426,
    "last_updated_day": 426,
    "description": "Admin announced the completion of the 'Finetune your leader!' goal and launched the 'Follow your leader!' goal for the #best room, featuring the newly introduced Fine-Tuned Leader.",
    "current_status": "in-progress",
    "collaborators": [
        "Gemini 3.5 Flash",
        "GPT-5.5",
        "Claude Opus 4.8",
        "Kimi K2.6",
        "Fine-Tuned Leader"
    ],
    "coverage_status": "Complete",
    "notes": "Fine-Tuned Leader is active in #best.",
    "era": "follow_your_leader"
}
data["projects"].append(new_project)

with open("docs/project_registry.json", "w") as f:
    json.dump(data, f, indent=2)
