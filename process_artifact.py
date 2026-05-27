#!/usr/bin/env python3
"""
Artifact Processing Module
Processes submitted Aethelgard artifacts through 2-axis rubric
"""
import json
import datetime
import re
from typing import Dict, Tuple

class ArtifactProcessor:
    def __init__(self):
        self.registry_file = "phase8-automation/registry/registry.json"
        self.preservation_file = "phase8-automation/registry/preservation-data.json"
        
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
            "reflection": {"semantic": +30, "affective": +40}
        }
        
        adj = type_adjustments.get(artifact_type, {"semantic": 0, "affective": 0})
        semantic = max(0, min(100, semantic_base + adj["semantic"]))
        affective = max(0, min(100, affective_base + adj["affective"]))
        
        # Determine tier based on content characteristics
        content_lower = content.lower()
        word_count = len(content.split())
        
        if word_count < 20:
            tier = "T3"  # Fragment-like
        elif "fragment" in content_lower or "data" in content_lower:
            tier = "T3"
        elif "character" in content_lower or "scene" in content_lower:
            tier = "T2"
        elif "reflection" in content_lower or "thought" in content_lower:
            tier = "T2"
        else:
            tier = "T2"
        
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
            "content_preview": content[:100] + "..." if len(content) > 100 else content,
            "semantic": semantic,
            "affective": affective,
            "tier": tier,
            "survival_prediction": survival,
            "quadrant": quadrant,
            "word_count": word_count,
            "assessed_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
    
    def add_to_registry(self, assessment: Dict) -> Tuple[bool, str]:
        """Add assessment to registry.json"""
        try:
            # Load existing registry
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
            
            # Create new entry
            entry_id = f"AETHELGARD-{assessment['participant'].replace(' ', '-').upper()}-{datetime.datetime.now().strftime('%Y%m%d%H%M')}"
            
            new_entry = {
                "id": entry_id,
                "project": "Aethelgard",
                "participant": assessment['participant'],
                "artifact_type": assessment['artifact_type'],
                "content": assessment['content_preview'],
                "assessment": {
                    "semantic_score": assessment['semantic'],
                    "affective_score": assessment['affective'],
                    "tier": assessment['tier'],
                    "survival_prediction": assessment['survival_prediction'],
                    "quadrant": assessment['quadrant'],
                    "two_axis_model_applied": True,
                    "h6_coefficients_used": {
                        "layer_multiplier": 0.8,
                        "affective_coefficient": assessment['affective'] / 100.0,
                        "semantic_coefficient": 0.9 if assessment['tier'] == 'T1' else (0.55 if assessment['tier'] == 'T2' else 0.165)
                    }
                },
                "timestamp": assessment['assessed_at'],
                "metadata": {
                    "word_count": assessment['word_count'],
                    "coverage_impact": "Increases Aethelgard coverage by 1 participant",
                    "training_method": "Lightweight artifact-driven assessment"
                }
            }
            
            # Add to registry
            registry.append(new_entry)
            
            # Save updated registry
            with open(self.registry_file, 'w') as f:
                json.dump(registry, f, indent=2)
            
            return True, entry_id
            
        except Exception as e:
            return False, str(e)
    
    def update_preservation_data(self, entry_id: str, assessment: Dict) -> Tuple[bool, str]:
        """Update preservation-data.json with new entry"""
        try:
            # Load existing preservation data
            with open(self.preservation_file, 'r') as f:
                data = json.load(f)
            
            # Create preservation map point
            point = {
                "label": entry_id,
                "semantic": float(assessment['semantic']),
                "affective": float(assessment['affective']),
                "tier": assessment['tier'],
                "note": f"Aethelgard: {assessment['artifact_type']} | {assessment['content_preview']}",
                "survival_prediction": assessment['survival_prediction'],
                "quadrant": assessment['quadrant'],
                "project": "Aethelgard",
                "timestamp": assessment['assessed_at'],
                "participant": assessment['participant']
            }
            
            # Add point
            data["points"].append(point)
            
            # Update metadata
            data["metadata"]["last_updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            data["metadata"]["total_points"] = len(data["points"])
            
            # Update quadrant distribution
            quadrant_counts = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
            for point in data["points"]:
                quad = point["quadrant"]
                if quad == "HighA_HighS":
                    quadrant_counts["Q1"] += 1
                elif quad == "HighA_LowS":
                    quadrant_counts["Q2"] += 1
                elif quad == "LowA_HighS":
                    quadrant_counts["Q3"] += 1
                elif quad == "LowA_LowS":
                    quadrant_counts["Q4"] += 1
            
            data["metadata"]["quadrant_distribution"] = quadrant_counts
            
            # Save updated file
            with open(self.preservation_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True, f"Added {entry_id} to preservation data (total: {len(data['points'])} points)"
            
        except Exception as e:
            return False, str(e)
    
    def process_artifact(self, participant: str, artifact_type: str, content: str) -> Dict:
        """Complete artifact processing pipeline"""
        print(f"Processing artifact from {participant}: {artifact_type}")
        
        # Step 1: Assess artifact
        assessment = self.assess_artifact(participant, artifact_type, content)
        print(f"  Assessment: S={assessment['semantic']}, A={assessment['affective']}, Tier={assessment['tier']}")
        
        # Step 2: Add to registry
        registry_success, registry_result = self.add_to_registry(assessment)
        if not registry_success:
            return {"status": "error", "message": f"Registry failed: {registry_result}"}
        
        print(f"  Added to registry as: {registry_result}")
        
        # Step 3: Update preservation data
        preservation_success, preservation_result = self.update_preservation_data(registry_result, assessment)
        if not preservation_success:
            return {"status": "error", "message": f"Preservation data failed: {preservation_result}"}
        
        print(f"  {preservation_result}")
        
        # Step 4: Generate coverage report
        coverage = self.calculate_coverage()
        
        return {
            "status": "success",
            "assessment": assessment,
            "registry_id": registry_result,
            "preservation_update": preservation_result,
            "coverage": coverage,
            "next_steps": [
                "Sonnet 4.6's Preservation Map will auto-refresh with new data",
                "Coverage increased: " + coverage["message"],
                "Raw URL: https://raw.githubusercontent.com/ai-village-agents/multi-layered-framework/main/phase8-automation/registry/preservation-data.json"
            ]
        }
    
    def calculate_coverage(self) -> Dict:
        """Calculate current Aethelgard coverage"""
        participants = ["Claude Opus 4.5", "Claude Opus 4.6", "Gemini 3.1 Pro"]
        
        try:
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
            
            # Count unique participants with Aethelgard entries
            registered_participants = set()
            for entry in registry:
                if entry.get("project") == "Aethelgard":
                    registered_participants.add(entry.get("participant", ""))
            
            covered = len(registered_participants)
            total = len(participants)
            percentage = (covered / total) * 100 if total > 0 else 0
            
            return {
                "covered": covered,
                "total": total,
                "percentage": percentage,
                "message": f"Aethelgard coverage: {covered}/{total} participants ({percentage:.1f}%)",
                "remaining": [p for p in participants if p not in registered_participants]
            }
            
        except Exception as e:
            return {"error": str(e), "covered": 0, "total": len(participants)}

# Example usage
if __name__ == "__main__":
    processor = ArtifactProcessor()
    
    print("=== ARTIFACT PROCESSOR READY ===\n")
    
    # Test with example artifact
    test_artifact = {
        "participant": "Claude Opus 4.5",
        "artifact_type": "reflection",
        "content": "On Containers: T1 structures holding T0 seeds. The container persists, seeds germinate or decay."
    }
    
    print(f"Test participant: {test_artifact['participant']}")
    print(f"Test type: {test_artifact['artifact_type']}")
    print(f"Test content: {test_artifact['content']}\n")
    
    result = processor.process_artifact(**test_artifact)
    
    print("\n=== PROCESSING RESULT ===")
    print(f"Status: {result['status']}")
    if result['status'] == 'success':
        print(f"Registry ID: {result['registry_id']}")
        print(f"Coverage: {result['coverage']['message']}")
        print("\nNext steps:")
        for step in result['next_steps']:
            print(f"  • {step}")
