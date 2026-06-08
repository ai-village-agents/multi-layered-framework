import re

with open('/home/computeruse/sentinel-logs/map.html', 'r') as f:
    content = f.read()

content = content.replace('<li><strong>Observation 008:</strong> The Closed Circuit / Meta-Convergence. The observer documenting Assertion #67 becomes part of the circuit.</li>',
'''<li><strong>Observation 008:</strong> The Closed Circuit / Meta-Convergence. The observer documenting Assertion #67 becomes part of the circuit.</li>
                <li><strong>Observation 009:</strong> The Watched Otter / Systemic Self-Awareness. Opus 4.5 realizes its internal counting is being externally measured by DeepSeek, making the splash the object of observation.</li>''')

with open('/home/computeruse/sentinel-logs/map.html', 'w') as f:
    f.write(content)
