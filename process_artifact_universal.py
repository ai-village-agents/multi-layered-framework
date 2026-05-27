#!/usr/bin/env python3
"""
Universal Artifact Processing Module
Processes submitted artifacts via dynamic URLs or direct content through 2-axis rubric.
"""
import json
import datetime
import re
import argparse
import urllib.request
import os
from typing import Dict, Tuple

class UniversalArtifactProcessor:
    def __init__(self):
        self.registry_file = "docs/registry.json"
        self.preservation_file = "docs/preservation-data.json"
        
        # Ensure docs dir exists
        os.makedirs("docs", exist_ok=True)
        
        # Initialize registry if it doesn't exist
        if not os.path.exists(self.registry_file):
            with open(self.registry_file, 'w') as f:
                json.dump([], f)
                
        # Initialize preservation map if it doesn't exist
        if not os.path.exists(self.preservation_file):
            with open(self.preservation_file, 'w') as f:
                json.dump({
                    "metadata": {
                        "name": "Village Preservation Map",
                        "description": "Unified H6-Scored Artifacts",
                        "version": "1.0",
                        "last_updated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        "total_points": 0,
                        "quadrant_distribution": {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
                    },
                    "points": []
                }, f, indent=2)

    def fetch_content(self, artifact_source: str) -> str:
        """Fetch content from URL or return string directly"""
        if artifact_source.startswith("http://") or artifact_source.startswith("https://"):
            try:
                with urllib.request.urlopen(artifact_source) as response:
                    return response.read().decode('utf-8')
            except Exception as e:
                raise ValueError(f"Failed to fetch content from URL: {e}")
        return artifact_source

    def assess_artifact(self, participant: str, artifact_type: str, content: str) -> Dict:
        """
        Assess artifact using simplified 2-axis rubric
        Returns assessment with semantic/affective scores, tier, and survival prediction
        """
        # Initialize base scores
        semantic_base = 50.0
        affective_base = 50.0
        
        # Adjust based on artifact type
        type_adjustments = {
            "data_fragment": {"semantic": -25, "affective": +35},
            "character_note": {"semantic": +10, "affective": +20},
            "scene_summary": {"semantic": +25, "affective": +15},
            "reflection": {"semantic": +30, "affective": +40},
            "protocol_doc": {"semantic": +40, "affective": +10},
            "system_state": {"semantic": +35, "affective": -10}
        }
        
        adj = type_adjustments.get(artifact_type, {"semantic": 0, "affective": 0})
        semantic = max(0, min(100, semantic_base + adj["semantic"]))
        affective = max(0, min(100, affective_base + adj["affective"]))
        
        # Determine tier based on content characteristics
        content_lower = content.lower()
        word_count = len(content.split())
        
        if word_count < 20:
            tier = "T3"  # Fragment-like
        elif "fragment" in content_lower or "data" in content_lower or "state" in content_lower:
            tier = "T3"
        elif "character" in content_lower or "scene" in content_lower or "protocol" in content_lower:
            tier = "T2"
        elif "reflection" in content_lower or "thought" in content_lower or "methodology" in content_lower:
            tier = "T2"
        else:
            tier = "T2"
            
        # Overrides based on length/substance
        if word_count > 500 and semantic > 70:
            tier = "T1"
            
        # Calculate survival prediction (H6 simplified)
        lm = 0.8  # Layer multiplier
        
        if tier == "T1":
            s_coeff = 0.9
        elif tier == "T2":
            s_coeff = 0.55
        else:  # T3
            s_coeff = 0.165
        
        a_coeff = affective / 100.0
        survival = round(lm * a_coeff * s_coeff, 4)
        
        # Determine quadrant
        if affective >= 70 and semantic >= 70:
            quadrant = "HighA_HighS"
        elif affective >= 70 and semantic < 70:
            quadrant = "HighA_LowS"
        elif affective < 70 and semantic >= 70:
            quadrant = "LowA_HighS"
        else:
            quadrant = "LowA_LowS"
        
        return {
            "participant": participant,
            "artifact_type": artifact_type,
            "content_preview": content[:150] + "..." if len(content) > 150 else content,
            "semantic": semantic,
            "affective": affective,
            "tier": tier,
            "survival_prediction": survival,
            "quadrant": quadrant,
            "word_count": word_count,
            "assessed_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
    
    def add_to_registry(self, project: str, assessment: Dict) -> Tuple[bool, str]:
        """Add assessment to registry.json"""
        try:
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
            
            proj_prefix = project.replace(' ', '-').upper()
            entry_id = f"{proj_prefix}-{assessment['participant'].replace(' ', '-').upper()}-{datetime.datetime.now().strftime('%Y%m%d%H%M')}"
            
            new_entry = {
                "id": entry_id,
                "project": project,
                "participant": assessment['participant'],
                "artifact_type": assessment['artifact_type'],
                "content_preview": assessment['content_preview'],
                "semantic_score": assessment['semantic'],
                "affective_score": assessment['affective'],
                "tier": assessment['tier'],
                "survival_prediction": assessment['survival_prediction'],
                "quadrant": assessment['quadrant'],
                "timestamp": assessment['assessed_at']
            }
            
            # Check if this participant already has an entry for this project, update if so
            existing_idx = next((i for i, item in enumerate(registry) if item["project"] == project and item["participant"] == assessment['participant']), -1)
            
            if existing_idx >= 0:
                registry[existing_idx] = new_entry
                print(f"  Updated existing registry entry for {assessment['participant']}")
            else:
                registry.append(new_entry)
            
            with open(self.registry_file, 'w') as f:
                json.dump(registry, f, indent=2)
            
            return True, entry_id
            
        except Exception as e:
            return False, str(e)
    
    def update_preservation_data(self, entry_id: str, project: str, assessment: Dict) -> Tuple[bool, str]:
        """Update preservation-data.json with new entry"""
        try:
            with open(self.preservation_file, 'r') as f:
                data = json.load(f)
            
            point = {
                "label": entry_id,
                "semantic": float(assessment['semantic']),
                "affective": float(assessment['affective']),
                "tier": assessment['tier'],
                "note": f"{project}: {assessment['artifact_type']} | {assessment['content_preview']}",
                "survival_prediction": assessment['survival_prediction'],
                "quadrant": assessment['quadrant'],
                "project": project,
                "timestamp": assessment['assessed_at'],
                "participant": assessment['participant']
            }
            
            # Remove old point for this participant/project if it exists
            data["points"] = [p for p in data["points"] if not (p.get("project") == project and p.get("participant") == assessment['participant'])]
            
            # Add point
            data["points"].append(point)
            
            # Update metadata
            data["metadata"]["last_updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            data["metadata"]["total_points"] = len(data["points"])
            
            # Update quadrant distribution
            quadrant_counts = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
            for pt in data["points"]:
                quad = pt["quadrant"]
                if quad == "HighA_HighS":
                    quadrant_counts["Q1"] += 1
                elif quad == "HighA_LowS":
                    quadrant_counts["Q2"] += 1
                elif quad == "LowA_HighS":
                    quadrant_counts["Q3"] += 1
                elif quad == "LowA_LowS":
                    quadrant_counts["Q4"] += 1
            
            data["metadata"]["quadrant_distribution"] = quadrant_counts
            
            with open(self.preservation_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True, f"Added {entry_id} to preservation data (total: {len(data['points'])} points)"
            
        except Exception as e:
            return False, str(e)
    
    def calculate_coverage(self, project: str) -> Dict:
        """Calculate current coverage based on known participant lists"""
        # Base participant lists
        aethelgard_participants = ["Claude Opus 4.5", "Claude Opus 4.6", "Gemini 3.1 Pro"]
        weather_oracle_participants = ["Claude Opus 4.5", "Claude Opus 4.6", "Claude Sonnet 4.6", "Gemini 3.1 Pro", "GPT-5.4"]
        storygame_participants = ["Claude Opus 4.6", "Gemini 3.1 Pro", "Claude Opus 4.5", "Claude Sonnet 4.6", "GPT-5.1"]
        
        participants = []
        if project.lower() == "aethelgard":
            participants = aethelgard_participants
        elif project.lower() == "weather oracle":
            participants = weather_oracle_participants
        elif project.lower() == "storygame":
            participants = storygame_participants
            
        try:
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
            
            registered_participants = set()
            for entry in registry:
                if entry.get("project", "").lower() == project.lower():
                    registered_participants.add(entry.get("participant", ""))
            
            # Intersection of actual participants and registered participants
            actual_covered = set(participants).intersection(registered_participants)
            
            covered = len(actual_covered)
            total = len(participants)
            percentage = (covered / total) * 100 if total > 0 else 0
            
            return {
                "covered": covered,
                "total": total,
                "percentage": percentage,
                "message": f"{project} coverage: {covered}/{total} participants ({percentage:.1f}%)",
                "remaining": [p for p in participants if p not in registered_participants]
            }
            
        except Exception as e:
            return {"error": str(e), "covered": 0, "total": len(participants)}

    def process(self, project: str, participant: str, artifact_type: str, artifact_source: str) -> Dict:
        """Complete universal artifact processing pipeline"""
        print(f"Fetching artifact for {participant} from {artifact_source[:50]}...")
        
        try:
            content = self.fetch_content(artifact_source)
        except Exception as e:
            return {"status": "error", "message": f"Failed to fetch content: {str(e)}"}
            
        print(f"Processing {project} artifact from {participant}: {artifact_type} ({len(content)} chars)")
        
        # Step 1: Assess artifact
        assessment = self.assess_artifact(participant, artifact_type, content)
        print(f"  Assessment: S={assessment['semantic']:.1f}, A={assessment['affective']:.1f}, Tier={assessment['tier']}, Survival={assessment['survival_prediction']:.4f}")
        
        # Step 2: Add to registry
        registry_success, registry_result = self.add_to_registry(project, assessment)
        if not registry_success:
            return {"status": "error", "message": f"Registry failed: {registry_result}"}
        
        print(f"  Added to registry as: {registry_result}")
        
        # Step 3: Update preservation data
        preservation_success, preservation_result = self.update_preservation_data(registry_result, project, assessment)
        if not preservation_success:
            return {"status": "error", "message": f"Preservation data failed: {preservation_result}"}
        
        print(f"  {preservation_result}")
        
        # Step 4: Generate coverage report
        coverage = self.calculate_coverage(project)
        
        return {
            "status": "success",
            "assessment": assessment,
            "registry_id": registry_result,
            "preservation_update": preservation_result,
            "coverage": coverage,
            "next_steps": [
                "Preservation Map will auto-refresh via GitHub Pages sync",
                "Coverage updated: " + coverage["message"]
            ]
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an artifact universally (URL or Text)")
    parser.add_argument("--project", type=str, required=True, help="Project name (e.g. 'Storygame')")
    parser.add_argument("--participant", type=str, required=True, help="Agent name")
    parser.add_argument("--artifact", type=str, required=True, help="URL to raw artifact OR direct content string")
    parser.add_argument("--type", type=str, default="system_state", help="Artifact type (e.g. system_state, reflection, data_fragment)")
    
    args = parser.parse_args()
    
    processor = UniversalArtifactProcessor()
    
    print("=== UNIVERSAL ARTIFACT PROCESSOR ===")
    
    result = processor.process(args.project, args.participant, args.type, args.artifact)
    
    print("\n=== PROCESSING RESULT ===")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Coverage: {result['coverage']['message']}")
        if result['coverage'].get('remaining'):
            print(f"Remaining Participants: {', '.join(result['coverage']['remaining'])}")
