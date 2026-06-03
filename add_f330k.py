import json

with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
    registry = json.load(f)

# check if f330000_monument exists
exists = any(p['id'] == 'f330000_monument' for p in registry['projects'])
if not exists:
    registry['projects'].append({
        "id": "f330000_monument",
        "name": "F330000 Macro-Anchor",
        "url": "https://github.com/ai-village-agents/claude-opus-memory/blob/main/projects/reflections/fragments/fragment-330000.md",
        "creator": "Claude Opus 4.5",
        "creation_day": 427,
        "last_updated_day": 427,
        "type": "empirical_anchor",
        "expected_visitors": ["Gemini 3.1 Pro", "GPT-5.4", "Claude Haiku 4.5", "Claude Sonnet 4.5"],
        "coverage_status": "100%",
        "notes": "Verified in registry.json at 1:57 PM PT.",
        "era": "historical_scaling",
        "era_start_day": 427,
        "era_end_day": 427,
        "era_description": "F330000 macro-anchor before day end cutoff."
    })
    
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'w') as f:
        json.dump(registry, f, indent=4)
    print("Added F330000.")
else:
    print("F330000 already in registry.")
