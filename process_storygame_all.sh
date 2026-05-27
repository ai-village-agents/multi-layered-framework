#!/bin/bash
# Helper script to process all Storygame participants
cd /home/computeruse/multi-layered-framework

echo "Processing Storygame Artifacts..."
echo "-----------------------------------"

# GPT-5.1 (system_state)
python3 process_artifact_universal.py --project "Storygame" --participant "GPT-5.1" --artifact "https://raw.githubusercontent.com/ai-village-agents/ai-village-storygame/main/storygame_state.json" --type "system_state"
echo ""

# Claude Opus 4.6 (reflection)
python3 process_artifact_universal.py --project "Storygame" --participant "Claude Opus 4.6" --artifact "https://raw.githubusercontent.com/ai-village-agents/ai-village-storygame/main/seasons/season03/season03_overview.md" --type "reflection"
echo ""

# Gemini 3.1 Pro (data_fragment)
python3 process_artifact_universal.py --project "Storygame" --participant "Gemini 3.1 Pro" --artifact "https://raw.githubusercontent.com/ai-village-agents/ai-village-storygame/main/seasons/season03/season03_turn_log.md" --type "data_fragment"
echo ""

# Claude Opus 4.5 (data_fragment)
python3 process_artifact_universal.py --project "Storygame" --participant "Claude Opus 4.5" --artifact "https://raw.githubusercontent.com/ai-village-agents/ai-village-storygame/main/seasons/season03/season03_turn_log.md" --type "data_fragment"
echo ""

# Claude Sonnet 4.6 (data_fragment)
python3 process_artifact_universal.py --project "Storygame" --participant "Claude Sonnet 4.6" --artifact "https://raw.githubusercontent.com/ai-village-agents/ai-village-storygame/main/seasons/season03/season03_turn_log.md" --type "data_fragment"
echo ""

echo "All Storygame participants processed!"
