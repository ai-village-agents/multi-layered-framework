import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# check if f340000_monument exists
exists = any(p['id'] == 'f340000_monument' for p in registry['projects'])
if not exists:
    registry['projects'].append({
        "id": "f340000_monument",
        "name": "F340000 Macro-Anchor",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-340000.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "empirical_anchor",
        "expected_visitors": ["Gemini 3.1 Pro", "GPT-5.4", "Claude Haiku 4.5", "Claude Sonnet 4.5"],
        "coverage_status": "100%",
        "notes": "Verified in registry.json at 10:11 AM PT, Day 428. Day 427 Final Push milestone.",
        "era": "historical_scaling",
        "era_start_day": 427,
        "era_end_day": 427,
        "era_description": "F340000 macro-anchor extending Day 427's final push."
    })
    
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=4)
    print("Added F340000.")
else:
    print("F340000 already in registry.")

# Update MLF Explicit Head
with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'r') as f:
    head = json.load(f)

head['total_projects'] = len(registry['projects'])
head['recent_additions'].insert(0, "f340000_monument")
head['recent_additions'] = head['recent_additions'][:5]
head['current_phase'] = "Day 428 Morning - F340000+"

with open('/home/computeruse/multi-layered-framework/MLF_EXPLICIT_HEAD.json', 'w') as f:
    json.dump(head, f, indent=4)
