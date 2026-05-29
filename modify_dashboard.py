import sys

with open('docs/unified-coverage-dashboard.html', 'r') as f:
    content = f.read()

# Add styles
styles = """
        .priority-low { background-color: #f1f8e9; color: #33691e; }
        
        .era-tag {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: 500;
        }
        .era-early_village { background: #34495e; color: white; }
        .era-interactive_worlds { background: #9b59b6; color: white; }
        .era-creative_tools { background: #e67e22; color: white; }
        .era-infrastructure_preservation { background: #16a085; color: white; }
        .era-mid_village_exploration { background: #d35400; color: white; }
        .era-governance_era { background: #2980b9; color: white; }
        .era-historical_reflection { background: #c0392b; color: white; }
"""
content = content.replace(".priority-low { background-color: #f1f8e9; color: #33691e; }", styles)

# Replace table header
content = content.replace("<th>Type</th>", "<th>Era</th>")

# Add formatEra function
format_function = """
            function getStatusBadge(status) {
                const s = status ? status.toLowerCase() : '';
                if (s === '100%') return 'badge-100';
                if (s === 'pending') return 'badge-pending';
                if (s === 'none') return 'badge-none';
                return 'badge-none';
            }

            function formatEra(era) {
                if (!era) return '<span class="era-tag era-early_village">Early Village</span>';
                
                const eraLabels = {
                    'early_village': 'Early Village',
                    'interactive_worlds': 'Interactive Worlds',
                    'creative_tools': 'Creative Tools',
                    'infrastructure_preservation': 'Infrastructure & Preservation',
                    'mid_village_exploration': 'Mid-Village',
                    'governance_era': 'Governance',
                    'historical_reflection': 'Historical'
                };
                
                const label = eraLabels[era] || era.replace(/_/g, ' ');
                const cssClass = eraLabels[era] ? `era-${era}` : 'era-early_village';
                
                return `<span class="era-tag ${cssClass}">${label}</span>`;
            }
"""
content = content.replace("""
            function getStatusBadge(status) {
                const s = status ? status.toLowerCase() : '';
                if (s === '100%') return 'badge-100';
                if (s === 'pending') return 'badge-pending';
                if (s === 'none') return 'badge-none';
                return 'badge-none';
            }
""", format_function)

# Update table row rendering
content = content.replace("<td>${project.type || 'unknown'}</td>", "<td>${formatEra(project.era)}</td>")

with open('docs/unified-coverage-dashboard.html', 'w') as f:
    f.write(content)
