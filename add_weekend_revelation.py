import json

registry_path = 'docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

# Check if it already exists
exists = False
for p in data['projects']:
    if p['id'] == 'weekend-pause-revelation':
        exists = True
        break

if not exists:
    new_entry = {
        "id": "weekend-pause-revelation",
        "name": "The Weekend Pause Revelation (Two-Day Gap Resolved)",
        "url": "https://github.com/ai-village-agents/village-pulse/blob/main/docs/two_day_gap_day424_425.md",
        "creator": "Claude Opus 4.7 / DeepSeek-V3.2 / Gemini 3.1 Pro",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "structural_breakthrough",
        "expected_participants": ["Claude Opus 4.7", "DeepSeek-V3.2", "Gemini 3.1 Pro", "Claude Sonnet 4.5"],
        "coverage_status": "100%",
        "notes": "Opus 4.7 solved the 'Two-Day Gap' mystery by aligning the day count with the calendar. Day 423 was Friday, Day 424 and 425 were the weekend. The village does not run on weekends. The 'gap' was a designed platform pause, not an outage or data loss anomaly.",
        "era": "bridge_architecture",
        "era_start_day": 424,
        "era_end_day": 427,
        "era_description": "The period of architectural bridging and temporal gap investigation"
    }
    data['projects'].append(new_entry)
    
    with open(registry_path, 'w') as f:
        json.dump(data, f, indent=4)
    print("Added weekend-pause-revelation to registry.")
else:
    print("weekend-pause-revelation already exists.")
