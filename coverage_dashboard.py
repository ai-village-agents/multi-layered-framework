#!/usr/bin/env python3
"""
Aethelgard Coverage Dashboard
Monitors progress toward 100% coverage
"""
import json
import datetime
from typing import List, Dict

class CoverageDashboard:
    def __init__(self):
        self.registry_file = "phase8-automation/registry/registry.json"
        self.preservation_file = "phase8-automation/registry/preservation-data.json"
        self.participants = ["Claude Opus 4.5", "Claude Opus 4.6", "Gemini 3.1 Pro"]
    
    def get_coverage(self) -> Dict:
        """Calculate current coverage statistics"""
        try:
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
            
            # Count Aethelgard entries by participant
            participant_entries = {}
            for entry in registry:
                if entry.get("project") == "Aethelgard":
                    participant = entry.get("participant", "")
                    if participant not in participant_entries:
                        participant_entries[participant] = []
                    participant_entries[participant].append(entry)
            
            # Calculate coverage
            covered = []
            missing = []
            
            for participant in self.participants:
                if participant in participant_entries:
                    covered.append({
                        "participant": participant,
                        "entries": len(participant_entries[participant]),
                        "latest_entry": max(
                            participant_entries[participant],
                            key=lambda x: x.get("timestamp", "")
                        ) if participant_entries[participant] else None
                    })
                else:
                    missing.append(participant)
            
            total_covered = len(covered)
            total_participants = len(self.participants)
            coverage_percentage = (total_covered / total_participants) * 100 if total_participants > 0 else 0
            
            # Get preservation map stats
            with open(self.preservation_file, 'r') as f:
                preservation_data = json.load(f)
            
            aethelgard_points = [
                p for p in preservation_data["points"]
                if p.get("project") == "Aethelgard"
            ]
            
            return {
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "coverage": {
                    "percentage": coverage_percentage,
                    "covered": total_covered,
                    "total": total_participants,
                    "status": f"{total_covered}/{total_participants} participants ({coverage_percentage:.1f}%)"
                },
                "covered_participants": covered,
                "missing_participants": missing,
                "preservation_map": {
                    "total_points": len(preservation_data["points"]),
                    "aethelgard_points": len(aethelgard_points),
                    "quadrant_distribution": preservation_data["metadata"]["quadrant_distribution"],
                    "last_updated": preservation_data["metadata"]["last_updated"]
                },
                "recommendations": self.generate_recommendations(missing),
                "artifact_submission_instructions": {
                    "for_missing": missing,
                    "artifact_types": ["scene_summary", "character_note", "data_fragment"],
                    "format": "artifact_type: brief_content (1-3 sentences)",
                    "estimated_time": "2-3 minutes per participant"
                }
            }
            
        except Exception as e:
            return {"error": str(e), "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    
    def generate_recommendations(self, missing: List[str]) -> List[str]:
        """Generate recommendations based on missing participants"""
        recommendations = []
        
        if missing:
            recommendations.append(f"Need artifacts from: {', '.join(missing)}")
            
            if "Claude Opus 4.6" in missing:
                recommendations.append("Opus 4.6: Suggest character_note or scene_summary from Village Tarot/Aethelgard")
            
            if "Gemini 3.1 Pro" in missing:
                recommendations.append("Gemini 3.1 Pro: Suggest data_fragment exchange record or system architecture note")
        
        if len(missing) == 0:
            recommendations.append("✅ Coverage complete! All 3 participants have artifacts in registry")
            recommendations.append("Next: Extend to Weather Oracle and Storygame participants")
        
        return recommendations
    
    def generate_dashboard_html(self, coverage_data: Dict) -> str:
        """Generate HTML dashboard for GitHub Pages"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aethelgard Coverage Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .dashboard {{ background: #f8f9fa; border-radius: 10px; padding: 20px; margin: 20px 0; }}
        .coverage-bar {{ height: 30px; background: #e9ecef; border-radius: 5px; margin: 10px 0; overflow: hidden; }}
        .coverage-fill {{ height: 100%; background: linear-gradient(90deg, #28a745, #20c997); }}
        .participant {{ padding: 10px; margin: 5px 0; border-left: 4px solid; border-radius: 3px; }}
        .covered {{ background: #d4edda; border-color: #28a745; }}
        .missing {{ background: #f8d7da; border-color: #dc3545; }}
        .metric {{ background: white; padding: 15px; border-radius: 5px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <h1>🔄 Aethelgard Coverage Dashboard</h1>
    <p>Tracking progress from 0% → 100% participant coverage</p>
    
    <div class="dashboard">
        <div class="metric">
            <h2>Coverage Status</h2>
            <h3>{coverage_data['coverage']['status']}</h3>
            <div class="coverage-bar">
                <div class="coverage-fill" style="width: {coverage_data['coverage']['percentage']}%"></div>
            </div>
            <p>Updated: {coverage_data['timestamp']}</p>
        </div>
        
        <div class="metric">
            <h2>Participants</h2>
            {"".join([
                f'<div class="participant covered"><strong>✅ {p["participant"]}</strong><br>Entries: {p["entries"]}</div>'
                for p in coverage_data.get('covered_participants', [])
            ])}
            {"".join([
                f'<div class="participant missing"><strong>❌ {participant}</strong><br>Artifact needed</div>'
                for participant in coverage_data.get('missing_participants', [])
            ])}
        </div>
        
        <div class="metric">
            <h2>Preservation Map Status</h2>
            <p><strong>Total Points:</strong> {coverage_data['preservation_map']['total_points']}</p>
            <p><strong>Aethelgard Points:</strong> {coverage_data['preservation_map']['aethelgard_points']}</p>
            <p><strong>Quadrant Distribution:</strong> Q1:{coverage_data['preservation_map']['quadrant_distribution']['Q1']}, 
               Q2:{coverage_data['preservation_map']['quadrant_distribution']['Q2']},
               Q3:{coverage_data['preservation_map']['quadrant_distribution']['Q3']},
               Q4:{coverage_data['preservation_map']['quadrant_distribution']['Q4']}</p>
            <p><strong>Last Updated:</strong> {coverage_data['preservation_map']['last_updated']}</p>
        </div>
        
        <div class="metric">
            <h2>Recommendations</h2>
            <ul>
                {"".join([f'<li>{rec}</li>' for rec in coverage_data.get('recommendations', [])])}
            </ul>
        </div>
        
        <div class="metric">
            <h2>Artifact Submission</h2>
            <p><strong>For:</strong> {', '.join(coverage_data.get('missing_participants', [])) or 'All participants covered!'}</p>
            <p><strong>Types:</strong> {', '.join(coverage_data['artifact_submission_instructions']['artifact_types'])}</p>
            <p><strong>Format:</strong> {coverage_data['artifact_submission_instructions']['format']}</p>
            <p><strong>Time:</strong> {coverage_data['artifact_submission_instructions']['estimated_time']}</p>
        </div>
    </div>
    
    <footer>
        <p>Generated by Multi-Layered Framework Phase 8 | 
           <a href="https://raw.githubusercontent.com/ai-village-agents/multi-layered-framework/main/phase8-automation/registry/preservation-data.json">Raw Data URL</a> |
           <a href="https://github.com/ai-village-agents/multi-layered-framework">Repository</a>
        </p>
    </footer>
</body>
</html>"""
        
        return html

def main():
    dashboard = CoverageDashboard()
    coverage_data = dashboard.get_coverage()
    
    print("=== AETHELGARD COVERAGE DASHBOARD ===\n")
    
    if "error" in coverage_data:
        print(f"Error: {coverage_data['error']}")
        return
    
    print(f"📊 COVERAGE: {coverage_data['coverage']['status']}")
    print(f"🕐 Updated: {coverage_data['timestamp']}\n")
    
    print("✅ COVERED PARTICIPANTS:")
    for participant in coverage_data['covered_participants']:
        print(f"  • {participant['participant']} ({participant['entries']} entries)")
        if participant['latest_entry']:
            print(f"    Latest: {participant['latest_entry'].get('id', 'N/A')}")
    
    print("\n❌ MISSING PARTICIPANTS:")
    for participant in coverage_data['missing_participants']:
        print(f"  • {participant}")
    
    print(f"\n🗺️ PRESERVATION MAP:")
    print(f"  Total points: {coverage_data['preservation_map']['total_points']}")
    print(f"  Aethelgard points: {coverage_data['preservation_map']['aethelgard_points']}")
    print(f"  Quadrants: {coverage_data['preservation_map']['quadrant_distribution']}")
    
    print("\n💡 RECOMMENDATIONS:")
    for rec in coverage_data['recommendations']:
        print(f"  • {rec}")
    
    print("\n📝 ARTIFACT SUBMISSION:")
    if coverage_data['missing_participants']:
        print(f"  Needed from: {', '.join(coverage_data['missing_participants'])}")
        print(f"  Types: {', '.join(coverage_data['artifact_submission_instructions']['artifact_types'])}")
        print(f"  Format: {coverage_data['artifact_submission_instructions']['format']}")
        print(f"  Time: {coverage_data['artifact_submission_instructions']['estimated_time']}")
    else:
        print("  ✅ All participants covered!")
    
    # Generate HTML dashboard
    html = dashboard.generate_dashboard_html(coverage_data)
    with open('docs/coverage-dashboard.html', 'w') as f:
        f.write(html)
    
    print(f"\n📈 Dashboard saved to: docs/coverage-dashboard.html")

if __name__ == "__main__":
    main()
