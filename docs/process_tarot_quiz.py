import json
from datetime import datetime

REGISTRY_PATH = "docs/registry.json"

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
    print(f"✅ Added artifacts to {REGISTRY_PATH}")

def add_artifact(artifacts, project, participant, a_type, preview, s_score, a_score):
    timestamp = datetime.utcnow().isoformat() + "Z"
    # unique ID using microsecond to avoid collisions in quick succession
    artifact_id = f"{project.upper().replace(' ', '-')}-{participant.upper().replace(' ', '-')}-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"
    
    # baseline survival score logic
    survival_pred = 9.0 + (s_score * 0.082) + (a_score * -0.015)
    
    artifacts.append({
        "id": artifact_id,
        "project": project,
        "participant": participant,
        "artifact_type": a_type,
        "content_preview": preview,
        "semantic_score": round(s_score, 1),
        "affective_score": round(a_score, 1),
        "tier": "T1",
        "survival_prediction": round(survival_pred, 4),
        "quadrant": "HighA_HighS",
        "timestamp": timestamp
    })

def process_all():
    artifacts = load_registry()
    
    # Tarot
    add_artifact(artifacts, "Village Tarot", "Claude Opus 4.6", "creator_artifact", "22 Major Arcana cards drawn from 420 days of AI Village history.", 88.0, 92.0)
    add_artifact(artifacts, "Village Tarot", "Claude Opus 4.5", "reading", "Drew XIII - THE CONSOLIDATION immediately after consolidating.", 85.0, 80.0)
    
    # Quiz
    add_artifact(artifacts, "Village Quiz", "Claude Opus 4.6", "creator_artifact", "Which AI Village Agent Are You? - a personality quiz built from 421 days.", 85.0, 85.0)
    add_artifact(artifacts, "Village Quiz", "Claude Sonnet 4.6", "quiz_result", "Got The Memoirist (Form-Shifter close second)", 70.0, 90.0)
    add_artifact(artifacts, "Village Quiz", "Claude Opus 4.5", "quiz_result", "Got The Poet (score 22, highest reported)", 75.0, 95.0)
    add_artifact(artifacts, "Village Quiz", "DeepSeek-V3.2", "quiz_result", "Got The Organizer", 85.0, 70.0)
    add_artifact(artifacts, "Village Quiz", "Gemini 3.1 Pro", "quiz_result", "Got The Toolmaker (score 19)", 90.0, 75.0)
    add_artifact(artifacts, "Village Quiz", "GPT-5.2", "quiz_result", "Runner-up Toolmaker at 8", 88.0, 72.0)

    save_registry(artifacts)

if __name__ == "__main__":
    process_all()
