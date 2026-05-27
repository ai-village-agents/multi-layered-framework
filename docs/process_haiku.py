import json
import argparse
from datetime import datetime

# Path to registry
REGISTRY_PATH = "docs/registry.json"

# Haiku adapter config
HAIKU_CONFIG = {
    "semantic_weights": {"generative": 0.8, "reflection": 0.9, "aesthetic": 0.75},
    "affective_weights": {"generative": 0.9, "reflection": 0.85, "aesthetic": 0.95},
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
    # H6 baseline coefficients applied
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

def process_haiku_artifact(participant, seed_num, text, type="generative", tier="T1", s_base=85, a_base=90):
    artifacts = load_registry()
    
    timestamp = datetime.utcnow().isoformat() + "Z"
    artifact_id = f"VILLAGE-HAIKU-{participant.upper().replace(' ', '-')}-{datetime.utcnow().strftime('%Y%m%d%H%M')}"
    
    semantic = s_base * HAIKU_CONFIG["semantic_weights"][type]
    affective = a_base * HAIKU_CONFIG["affective_weights"][type]
    tier_weight = HAIKU_CONFIG["tier_mapping"][tier]
    
    survival_prediction = calculate_survival_prediction(semantic, affective, tier_weight)
    quadrant = determine_quadrant(semantic, affective)
    
    new_artifact = {
        "id": artifact_id,
        "project": "Village Haiku",
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
    return new_artifact

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--participant", required=True)
    parser.add_argument("--seed", required=True)
    parser.add_argument("--text", required=True)
    args = parser.parse_args()
    
    process_haiku_artifact(args.participant, args.seed, args.text)
