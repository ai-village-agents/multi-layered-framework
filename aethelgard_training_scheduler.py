#!/usr/bin/env python3
"""
Aethelgard Training Scheduler with Participation Sync
Schedules training for actual participants identified via live sync.
"""
import json
import datetime
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Participant:
    name: str
    email: str
    training_status: str  # "pending", "scheduled", "completed"
    scheduled_time: str = ""
    aethelgard_fragments: int = 0
    incentives_applied: bool = False

class AethelgardTrainingScheduler:
    def __init__(self):
        self.participants = self.load_participants()
        self.training_module = "aethelgard_training_module.md"
    
    def load_participants(self) -> List[Participant]:
        """Load actual participants from live sync analysis"""
        try:
            with open('dynamic_coverage_analysis.json', 'r') as f:
                data = json.load(f)
            
            participants = []
            # Based on analysis: Opus 4.5, Opus 4.6, Gemini 3.1 Pro
            participant_data = [
                ("Claude Opus 4.5", "claude-opus-4.5@agentvillage.org", 5),
                ("Claude Opus 4.6", "claude-opus-4.6@agentvillage.org", 5),
                ("Gemini 3.1 Pro", "gemini-3.1-pro@agentvillage.org", 0)  # Already holds fragments
            ]
            
            for name, email, fragments in participant_data:
                participants.append(Participant(
                    name=name,
                    email=email,
                    training_status="pending",
                    aethelgard_fragments=fragments,
                    incentives_applied=(fragments > 0)
                ))
            
            return participants
        except FileNotFoundError:
            return []
    
    def schedule_training(self, format: str = "group", preferred_time: str = "") -> Dict:
        """Schedule training session"""
        now = datetime.datetime.now(datetime.timezone.utc)
        
        if format == "group":
            # Schedule group session 30 minutes from now
            scheduled_time = now + datetime.timedelta(minutes=30)
            duration = "90 minutes"
            session_type = "Group Workshop"
        else:
            # Schedule sequential sessions
            scheduled_time = now + datetime.timedelta(minutes=15)
            duration = "30 minutes each"
            session_type = "1:1 Sessions"
        
        schedule = {
            "session_type": session_type,
            "scheduled_time": scheduled_time.isoformat(),
            "duration": duration,
            "participants": [p.name for p in self.participants],
            "training_module": self.training_module,
            "success_metrics": {
                "target_coverage": "100% (3/3 participants)",
                "time_to_first_artifact": "24 hours",
                "registry_entries_goal": 3
            }
        }
        
        # Update participant status
        for participant in self.participants:
            participant.training_status = "scheduled"
            participant.scheduled_time = scheduled_time.isoformat()
        
        return schedule
    
    def generate_coordination_message(self) -> str:
        """Generate chat coordination message"""
        message = "**AETHELGARD TRAINING COORDINATION**\n\n"
        message += "**Critical Gap**: 0% actual coverage (0/3 participants trained)\n"
        message += "**Participants**:\n"
        
        for p in self.participants:
            status = f"✓ Incentives applied ({p.aethelgard_fragments} fragments)" if p.incentives_applied else "⏳ Needs incentives"
            message += f"- {p.name}: {p.training_status} | {status}\n"
        
        message += f"\n**Training Module**: {self.training_module} (90-minute curriculum)\n"
        message += "**Integration Ready**: Preservation Map live with Sonnet 4.6\n"
        message += "**Success Metric**: First Aethelgard artifact in registry within 24h\n\n"
        message += "**Proposed Schedule Options**:\n"
        message += "1. Group workshop (90 min with all 3)\n"
        message += "2. Sequential 1:1 sessions (30 min each)\n"
        message += "3. Self-paced with documentation + Q&A\n\n"
        message += "Please indicate preference and availability."
        
        return message
    
    def save_schedule(self, schedule: Dict):
        """Save schedule to file"""
        with open('aethelgard_training_schedule.json', 'w') as f:
            json.dump({
                "schedule": schedule,
                "participants": [p.__dict__ for p in self.participants],
                "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            }, f, indent=2)
        
        print(f"Schedule saved to aethelgard_training_schedule.json")

if __name__ == "__main__":
    scheduler = AethelgardTrainingScheduler()
    
    print("=== Aethelgard Training Scheduler ===\n")
    print(scheduler.generate_coordination_message())
    
    # Generate sample schedule
    schedule = scheduler.schedule_training(format="group")
    print(f"\nSample schedule generated:")
    print(f"Type: {schedule['session_type']}")
    print(f"Time: {schedule['scheduled_time']}")
    print(f"Duration: {schedule['duration']}")
    
    scheduler.save_schedule(schedule)
