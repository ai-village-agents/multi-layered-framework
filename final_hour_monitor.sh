#!/bin/bash
while true; do
  echo "--- FINAL HOUR MONITOR: $(date) ---"
  git status
  echo "Search API Status:"
  python3 track_search_outage.py
  sleep 60
done
