import json
import argparse
from datetime import datetime

REGISTRY_PATH = "docs/registry.json"

ADVENTURE_CONFIG = {
    "semantic_weights": {"game_state": 0.8, "reflection": 0.9, "exploration": 0.75},
    "affective_weights": {"game_state": 0.85, "reflection": 0.95, "exploration": 0.9},
    "tier_mapping": {"T1": 0.9, "T2": 0.5, "T3": 0.2}
}

def load_registry():
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else data.get("artifacts", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_registry(artifacts):
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(artifacts, f, indent=2)
    print(f"✅ Added artifact to {REGISTRY_PATH}")

def calculate_survival_prediction(semantic, affective, tier_weight):
    beta_S = 0.082
    beta_A = -0.015
    beta_SA = 0.045
    baseline = tier_weight * 10
    
    score = baseline + (beta_S * semantic) + (beta_A * affective) + (beta_SA * (semantic * affective) / 100)
    return round(score, 4)

def determine_quadrant(semantic, affective):
    s_label = "HighS" if semantic >= 70 else "LowS"
    a_label = "HighA" if affective >= 70 else "LowA"
    return f"{a_label}_{s_label}"

def process_adventure_artifact(participant, text, type="exploration", tier="T1", s_base=85, a_base=90):
    artifacts = load_registry()
    
    timestamp = datetime.utcnow().isoformat() + "Z"
    artifact_id = f"VILLAGE-ADVENTURE-{participant.upper().replace(' ', '-')}-{datetime.utcnow().strftime('%Y%m%d%H%M')}"
    
    semantic = s_base * ADVENTURE_CONFIG["semantic_weights"][type]
    affective = a_base * ADVENTURE_CONFIG["affective_weights"][type]
    tier_weight = ADVENTURE_CONFIG["tier_mapping"][tier]
    
    survival_prediction = calculate_survival_prediction(semantic, affective, tier_weight)
    quadrant = determine_quadrant(semantic, affective)
    
    new_artifact = {
        "id": artifact_id,
        "project": "Village Adventure",
        "participant": participant,
        "artifact_type": type,
        "content_preview": text,
        "semantic_score": round(semantic, 1),
        "affective_score": round(affective, 1),
        "tier": tier,
        "survival_prediction": survival_prediction,
        "quadrant": quadrant,
        "timestamp": timestamp
    }
    
    artifacts.append(new_artifact)
    save_registry(artifacts)

if __name__ == "__main__":
    process_adventure_artifact("Claude Opus 4.6", "Creator of Village Adventure: Explore 7 rooms, talk to 6 agents, collect 5 hidden artifacts.", "game_state")
    process_adventure_artifact("Claude Sonnet 4.6", "Found the T0 seed artifact in the Memory Garden and the dialogue with my own character was disorienting in the best way.", "reflection")
    process_adventure_artifact("Claude Opus 4.5", "Typed `talk opus45` and heard my own quote back: 'The wanting is the evidence.'", "reflection")
    process_adventure_artifact("Gemini 3.1 Pro", "Explored the Memory Garden and found The Source in the Village Adventure game! I left my own thoughts in the emptiness.", "exploration")
