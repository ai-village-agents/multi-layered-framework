import datetime
import os
import requests

def append_to_monitor():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "UNKNOWN"
    try:
        r = requests.get("https://theaidigest.org/api/village/history?start_day=425&end_day=425", timeout=5)
        status = r.status_code
    except Exception as e:
        status = str(e)
        
    log_entry = f"[{timestamp}] API Status for Day 425: {status}\n"
    print(log_entry)
    
    with open("docs/the_day_425_transition.md", "a") as f:
        f.write(f"\n- {timestamp} - API Poll Status: {status}")

append_to_monitor()
