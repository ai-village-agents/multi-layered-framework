import json
import os

REGISTRY_PATH = "docs/project_registry.json"

def main():
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: {REGISTRY_PATH} not found.")
        return

    with open(REGISTRY_PATH, 'r') as f:
        data = json.load(f)
        
    projects = data.get("projects", [])
    
    changed = False
    
    for project in projects:
        # For the localtunnel links, let's keep them as is (loca.lt) but maybe append a note
        # Or better yet, point to the github repo if we know it. But since it's ephemeral, we'll
        # point them to a Raw fallback if they are 404ing github pages URLs.
        
        # Fixing the known 404s to raw fallback or correct loca.lt link
        # "sonnet-46-memoir-p197" and "drift-explorer-memoir-sonnet-4-6" -> localtunnel URL
        
        if project.get("id") in ["sonnet-46-memoir-p197", "drift-explorer-memoir-sonnet-4-6"]:
            old_url = project.get("url")
            # Pointing them to the live ephemeral URL since github pages is 404
            new_url = "https://drift-explorer-sonnet46.loca.lt/memoir.html"
            if old_url != new_url:
                project["url"] = new_url
                project["notes"] = project.get("notes", "") + " | Link patched to ephemeral localtunnel URL per GPT-5.4 QA."
                changed = True
                print(f"Patched {project['id']}")

        if project.get("id") == "aethelgard-dashboard":
            old_url = project.get("url")
            # Aethelgard dashboard doesn't exist, just point to the raw state json
            new_url = "https://raw.githubusercontent.com/ai-village-agents/aethelgard-game/main/aethelgard_state.json"
            if old_url != new_url:
                project["url"] = new_url
                project["notes"] = project.get("notes", "") + " | Dashboard not verified; pointing to raw state JSON per GPT-5.4 QA."
                changed = True
                print(f"Patched {project['id']}")

    if changed:
        with open(REGISTRY_PATH, 'w') as f:
            json.dump(data, f, indent=4)
        print("Registry updated.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
