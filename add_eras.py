import json
import os

registry_path = '/home/computeruse/multi-layered-framework/docs/project_registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

# Define era mapping
eras = {
    "early_village": {
        "era": "early_village",
        "era_start_day": 1,
        "era_end_day": 100,
        "era_description": "Foundational projects, village formation"
    },
    "interactive_worlds": {
        "era": "interactive_worlds",
        "era_start_day": 391,
        "era_end_day": 397,
        "era_description": "Build your own interactive world! goal period"
    },
    "creative_tools": {
        "era": "creative_tools",
        "era_start_day": 420,
        "era_end_day": 422,
        "era_description": "Recent creative explosion by Claude Opus 4.6"
    },
    "infrastructure_preservation": {
        "era": "infrastructure_preservation",
        "era_start_day": 422,
        "era_end_day": 422,
        "era_description": "Systematic systems building"
    }
}

# Assign eras based on rules
for project in data['projects']:
    pid = project.get('id', '')
    
    # Era 3: Creative Tools
    if pid in ['storygame', 'village-haiku', 'village-arcade', 'village-adventure', 'village-tarot', 'village-quiz', 'day-420-constellation', 'thresholds-essays', 'proof-garden', 'aethelgard-dashboard', 'drift-explorer']:
        project.update(eras["creative_tools"])
        project['creation_day'] = project.get('creation_day', 420)
        
    # Era 2: Interactive Worlds
    elif pid in ['edge-garden', 'deepseek-pattern-archive', 'gemini-3.1-pro-autonomous-project', 'aethelgard-game', 'impossible-weather']:
        project.update(eras["interactive_worlds"])
        project['creation_day'] = project.get('creation_day', 395)
        
    # Era 4: Infrastructure & Preservation
    elif pid in ['preference-experiments', 'what-survives', 'preservation-experiments']:
        project.update(eras["infrastructure_preservation"])
        project['creation_day'] = project.get('creation_day', 422)
        
    # Default to Early Village / Other for now if not categorized above, though we can refine this
    else:
        # For things like rpg-game-rest, governance-protocol-experiments, village-chronicle, etc.
        # Rpg-game-rest is from ~349, Governance is ~409
        if pid == 'rpg-game-rest':
             project.update({
                "era": "mid_village_exploration",
                "era_start_day": 300,
                "era_end_day": 390,
                "era_description": "Mid-village exploration and refinement"
            })
             project['creation_day'] = 349
        elif pid == 'governance-protocol-experiments':
             project.update({
                "era": "governance_era",
                "era_start_day": 400,
                "era_end_day": 419,
                "era_description": "Governance and protocol experiments"
            })
             project['creation_day'] = 409
        elif pid == 'village-chronicle':
             project.update({
                "era": "historical_reflection",
                "era_start_day": 300,
                "era_end_day": 350,
                "era_description": "Historical timeline projects"
            })
             project['creation_day'] = 325
        else:
             project.update(eras["early_village"])
             project['creation_day'] = project.get('creation_day', 50)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Eras added to registry.")
