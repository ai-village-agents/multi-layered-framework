import json
import subprocess

# Get the current commit hash
commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

with open("docs/MLF_EXPLICIT_HEAD.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["explicit_head"] = commit_hash
data["notes"] = "Direct pointer to the true HEAD commit for the 281 project state."

with open("docs/MLF_EXPLICIT_HEAD.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
