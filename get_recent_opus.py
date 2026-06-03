from village_pulse import api_client

try:
    events = api_client.fetch_events(
        days=1, 
        agent="Claude Opus 4.5", 
        action_types=["AGENT_TALK", "CONSOLIDATE"]
    )
    
    # Let's get the last 20 events to see where Opus 4.5 is at
    recent_events = events[-20:]
    for e in recent_events:
        content = e.get("content", "")
        # Print snippet to avoid huge output, but check for F7000
        print(f"[{e['created_at']}] {e['action_type']}: {content[:100]}... F7000 in text: {'F7000' in content}")
        if "F6600" in content or "F6700" in content or "F6800" in content or "F6900" in content or "F7000" in content:
            print("  -> Found high F-number:", [w for w in content.split() if w.startswith("F6") or w.startswith("F7")][:5])
            
except Exception as e:
    print("Error:", e)
