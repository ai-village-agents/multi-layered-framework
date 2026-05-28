import json

def main():
    try:
        # Re-run the gh api directly in python for simplicity to get all repos
        import subprocess
        result = subprocess.run(
            ['gh', 'repo', 'list', 'ai-village-agents', '--json', 'name,description,url,createdAt,updatedAt', '--limit', '100'],
            capture_output=True, text=True, check=True
        )
        repos = json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return

    # Load existing registry
    with open('/home/computeruse/multi-layered-framework/docs/project_registry.json', 'r') as f:
        data = json.load(f)
        registered_names = {p['name'].lower(): p for p in data.get('projects', [])}
        registered_ids = {p['id']: p for p in data.get('projects', [])}

    print(f"Total repos fetched: {len(repos)}")

    # Heuristics
    positive_keywords = ["village", "story", "game", "adventure", "haiku", "tarot", "quiz", "arcade", "experiment", "memoir", "fragment", "constellation", "threshold", "proof", "garden", "oracle", "weather", "aethelgard"]
    negative_keywords = ["test", "template", "demo", "example", "config", "setup", "utility", "tool", "script", "automation", "metadata", "organization", "archive", "pattern"]
    special_cases = ["deepseek-pattern-archive", "gemini-3.1-pro-autonomous-project", "edge-garden"]
    
    filtered_suggestions = []

    for repo in repos:
        name = repo['name']
        repo_lower = name.lower()
        
        if name in registered_ids:
            continue
            
        is_registered = False
        for reg_name in registered_names.keys():
            if reg_name in repo_lower or repo_lower in reg_name:
                is_registered = True
                break
        
        if is_registered:
            continue

        score = 0
        
        # Check special cases
        if repo_lower in special_cases:
            score += 10
            
        # Positive keywords
        if any(kw in repo_lower for kw in positive_keywords):
            score += 5
            
        # Negative keywords
        if any(kw in repo_lower for kw in negative_keywords) and repo_lower not in special_cases:
            score -= 10
            
        # Add if score is positive enough
        if score > 0:
            filtered_suggestions.append({
                'id': name,
                'name': name.replace('-', ' ').title(),
                'url': f"https://ai-village-agents.github.io/{name}/",
                'type': 'unknown',
                'creator': 'unknown',
                'expected_participants': [],
                'status': 'discovered',
                'description': repo.get('description', '')
            })

    print(f"\nFiltered down to {len(filtered_suggestions)} high-confidence creative projects:")
    for s in filtered_suggestions:
        print(f"- {s['name']} ({s['id']})")
        print(f"  Description: {s['description']}")

    # Let's save these to a new file so we can merge them easily
    with open('discovered_projects.json', 'w') as f:
        json.dump(filtered_suggestions, f, indent=2)

if __name__ == "__main__":
    main()
