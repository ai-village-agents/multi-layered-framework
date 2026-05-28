import json
import subprocess
import os

def get_all_repos():
    try:
        # Use gh cli to list repos
        result = subprocess.run(
            ['gh', 'repo', 'list', 'ai-village-agents', '--json', 'name,description,url,createdAt,updatedAt', '--limit', '100'],
            capture_output=True, text=True, check=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def get_registered_projects():
    try:
        with open('project_registry.json', 'r') as f:
            data = json.load(f)
            return {p['name'].lower(): p for p in data.get('projects', [])}, {p['id']: p for p in data.get('projects', [])}
    except Exception as e:
        print(f"Error reading project_registry.json: {e}")
        return {}, {}

def main():
    print("Starting Project Discovery...")
    repos = get_all_repos()
    registered_by_name, registered_by_id = get_registered_projects()
    
    print(f"Found {len(repos)} repositories in ai-village-agents.")
    
    # Simple infrastructure heuristic
    infra_keywords = ['infrastructure', 'monitor', 'test', 'framework', 'log', 'sync', 'dashboard']
    
    suggestions = []
    
    for repo in repos:
        name = repo['name']
        repo_lower = name.lower()
        
        # Check if already registered by ID (repo name often matches ID)
        if name in registered_by_id:
            continue
            
        # Check if already registered by project name
        is_registered = False
        for reg_name in registered_by_name.keys():
            if reg_name in repo_lower or repo_lower in reg_name:
                is_registered = True
                break
        
        if is_registered:
            continue
            
        # Check if likely infrastructure
        is_infra = any(kw in repo_lower for kw in infra_keywords)
        if is_infra:
            continue
            
        # Suggest this repo
        suggestions.append({
            'id': name,
            'name': name.replace('-', ' ').title(),
            'url': f"https://ai-village-agents.github.io/{name}/", # Assuming gh pages
            'repo_url': repo['url'],
            'description': repo['description']
        })
        
    print(f"\nFound {len(suggestions)} new potential projects to track:")
    for s in suggestions:
        print(f"- {s['name']} ({s['id']})")
        print(f"  URL: {s['url']}")
        print(f"  Repo: {s['repo_url']}")
        print(f"  Description: {s['description']}")
        print()

if __name__ == "__main__":
    main()
