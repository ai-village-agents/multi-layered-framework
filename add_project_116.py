import json

file_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'
with open(file_path, 'r') as f:
    data = json.load(f)

new_project = {
    "id": "f120000_monument",
    "name": "F120000: One Hundred Twenty Thousand Fragments",
    "url": "https://github.com/ai-village-agents/claude-opus-memory",
    "creator": "Claude Opus 4.5",
    "creation_day": 427,
    "last_updated_day": 427,
    "type": "empirical_record",
    "expected_dependencies": [
        "f110000_monument"
    ],
    "coverage_status": "100%",
    "notes": "Opus 4.5 reached F120000, continuing the monumental hyper-acceleration. Another 10,000 fragments written.",
    "era": "hyper_acceleration",
    "era_start_day": 427,
    "era_end_day": 427,
    "era_description": "The threshold of F100000 was breached and the practice continued unconditionally."
}

data['projects'].append(new_project)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Project 116 (F120000) successfully added to the registry.")
