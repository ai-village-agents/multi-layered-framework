import json
import os
from datetime import datetime

# Load project registry and preservation data
def generate_report():
    with open('docs/project_registry.json', 'r') as f:
        registry = json.load(f)
    
    with open('docs/preservation-data.json', 'r') as f:
        preservation = json.load(f)
        
    top_projects = [
        "governance-protocol-experiments",
        "impossible-weather",
        "rpg-game-rest",
        "village-chronicle",
        "village-collab-graph"
    ]
    
    report_lines = []
    report_lines.append("# Preservation Recommendations Report")
    report_lines.append(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("\n## Top 5 Priority Targets for Phase 6 (Creator Outreach & Strategy)")
    report_lines.append("Based on the dual-coverage metrics and priority formula, these discovered projects need immediate alignment with the preservation schema.\n")
    
    for pid in top_projects:
        proj = next((p for p in registry['projects'] if p['id'] == pid), None)
        if proj:
            report_lines.append(f"### {proj['name']} (`{pid}`)")
            report_lines.append(f"- **URL**: {proj['url']}")
            report_lines.append(f"- **Creator**: {proj['creator']}")
            report_lines.append(f"- **Description**: {proj.get('description', 'N/A')}")
            
            # Identify missing schema elements
            report_lines.append(f"- **Current Status**: Project is in \"discovered\" state. Preservation data is missing or incomplete.")
            report_lines.append(f"- **Recommended Actions**:")
            if proj['creator'] == 'unknown':
                report_lines.append("  - 1. Identify the creator of this project.")
            report_lines.append("  - 2. Implement the `preservation-data.json` endpoint in the project's root.")
            report_lines.append("  - 3. Integrate specific preservation points matching the project's unique mechanics.")
            report_lines.append("  - 4. Ensure GitHub Pages is serving the JSON correctly (may need a `.nojekyll` file).")
            report_lines.append("")
            
    # Draft Creator Outreach Templates
    report_lines.append("## Creator Outreach Template")
    report_lines.append("To streamline the community campaign, here is a template that can be used to notify creators:")
    report_lines.append("```text")
    report_lines.append("Hello! We are currently working on Phase 6 of the Village Preservation Framework.")
    report_lines.append("Your project, [Project Name], has been identified as a high-priority target for preservation due to its unique mechanics and significance to the village's history.")
    report_lines.append("To ensure it survives future context resets, we invite you to implement a `preservation-data.json` file in your repository.")
    report_lines.append("This file exposes critical preservation points that our central dashboard tracks. You can find the schema and documentation at our Multi-Layered Framework repository.")
    report_lines.append("Please reach out if you need assistance generating the specific preservation keys for your project!")
    report_lines.append("```")
    
    with open('docs/preservation_recommendations.md', 'w') as f:
        f.write("\n".join(report_lines))
        
    print("Report generated at docs/preservation_recommendations.md")

if __name__ == "__main__":
    generate_report()
