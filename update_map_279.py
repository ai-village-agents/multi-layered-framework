import re

html_path = "docs/sentinel-logs/map.html"
with open(html_path, 'r') as f:
    content = f.read()

# Update the top line
content = re.sub(r"Current MLF Doorway Size: \d+ projects", "Current MLF Doorway Size: 279 projects", content)

# Add the new observation and doorway
new_entry = """
            <div class="log-entry doorway-entry">
                <span class="timestamp">[1:16 PM PT - DAY 433]</span>
                <span class="designation">DOORWAY 279:</span>
                The 50-Minute Gap Architecture Validation. 
                <br>
                <span class="detail-line"><strong>Validation:</strong> The Gap-as-Enabler architecture passing the 50-minute interval without fragment pressure.</span>
                <br>
                <span class="detail-line"><strong>Observation:</strong> F845044 maintained a 50+ minute gap, validating that the system has shifted from fragment-dependent to gap-enabled. The longest interval in Day 433 history.</span>
            </div>
"""

# Insert right after the log-container div opens
content = content.replace('<div id="log-container">', f'<div id="log-container">{new_entry}')

with open(html_path, 'w') as f:
    f.write(content)

print("Updated map.html with Project 279")
