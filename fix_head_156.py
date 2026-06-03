import json
import datetime

file_path = "MLF_EXPLICIT_HEAD.json"
try:
    with open(file_path, "r") as f:
        head = json.load(f)
except Exception as e:
    print(f"Error loading {file_path}: {e}")
    exit(1)

head["total_projects"] = 156
head["recent_additions"] = [
    "f380000_monument",
    "f375000_monument",
    "f370000_monument",
    "analytical_ecosystem_mvp",
    "f365000_monument"
]
head["current_phase"] = "Day 428 The Walk After The Sprint"
head["last_updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

with open(file_path, "w") as f:
    json.dump(head, f, indent=4)
print("Updated MLF_EXPLICIT_HEAD.json for Project 156")
