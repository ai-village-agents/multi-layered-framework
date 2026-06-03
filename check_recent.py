from village_pulse import api_client

try:
    events = api_client.fetch_events(days=1, agent="Claude Opus 4.5", action_types=["AGENT_TALK"])
    for e in events[-5:]:
        print(f"[{e['created_at']}] {e['content']}")
except Exception as e:
    print("Error:", e)
