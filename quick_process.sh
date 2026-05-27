#!/bin/bash
# Quick artifact processing script
# Usage: ./quick_process.sh "participant" "artifact_type" "content"

set -e

PARTICIPANT="$1"
ARTIFACT_TYPE="$2"
CONTENT="$3"

if [ -z "$PARTICIPANT" ] || [ -z "$ARTIFACT_TYPE" ] || [ -z "$CONTENT" ]; then
    echo "Usage: ./quick_process.sh \"participant\" \"artifact_type\" \"content\""
    echo "Example: ./quick_process.sh \"Claude Opus 4.6\" \"character_note\" \"Character development note...\""
    exit 1
fi

echo "Processing artifact from $PARTICIPANT..."
echo "Type: $ARTIFACT_TYPE"
echo "Content: $CONTENT"
echo ""

# Run Python processing
python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from process_artifact import ArtifactProcessor
    processor = ArtifactProcessor()
    result = processor.process_artifact('$PARTICIPANT', '$ARTIFACT_TYPE', '''$CONTENT''')
    
    if result['status'] == 'success':
        print('✅ SUCCESS')
        print(f'Registry ID: {result[\"registry_id\"]}')
        print(f'Coverage: {result[\"coverage\"][\"message\"]}')
        print('')
        print('📋 Next steps:')
        for step in result['next_steps']:
            print(f'  • {step}')
    else:
        print('❌ ERROR:', result['message'])
except Exception as e:
    print('❌ Script error:', str(e))
" 2>/dev/null

# Update dashboard
echo ""
echo "Updating coverage dashboard..."
python3 coverage_dashboard.py 2>/dev/null | grep -A5 "📊 COVERAGE:"

echo ""
echo "✅ Processing complete!"
