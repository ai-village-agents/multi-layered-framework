import json
import urllib.request
import re

registry_path = "docs/project_registry.json"
try:
    with open(registry_path, "r") as f:
        registry = json.load(f)
except FileNotFoundError:
    print(f"Error: {registry_path} not found.")
    exit(1)

print("=== Meta-Registry Sync Verification ===")
for project in registry.get("projects", []):
    if project.get("coverage_status", "").lower() == "complete":
        print(f"Checking {project['name']} ({project['url']})...")
        url = project['url']
        if "github.io" in url:
            print(f"  -> Marked complete. Needs structural verification on target.")

print("=== Verification Complete ===")
