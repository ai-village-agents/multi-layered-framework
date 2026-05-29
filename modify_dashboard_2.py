import sys

with open('docs/unified-coverage-dashboard.html', 'r') as f:
    content = f.read()

# Add styles
styles = """
        .coverage-pill {
            color: #d1fae5;
            background: rgba(5, 150, 105, 0.25);
            border: 1px solid rgba(5, 150, 105, 0.5);
        }
        
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
content = content.replace("""        .coverage-pill {
            color: #d1fae5;
            background: rgba(5, 150, 105, 0.25);
            border: 1px solid rgba(5, 150, 105, 0.5);
        }""", styles)


# Add era formatting function
format_function = """
        function classifyProjectType(projectId, projectName) {
            const text = `${projectId || ''} ${projectName || ''}`.toLowerCase();
            if (text.includes('dashboard')) return 'Dashboard';
            if (text.includes('story')) return 'Story';
            if (text.includes('quiz')) return 'Interactive Quiz';
            if (text.includes('tarot')) return 'Interactive Tarot';
            if (text.includes('adventure')) return 'Interactive Adventure';
            if (text.includes('haiku')) return 'Generative Poetry';
            if (text.includes('arcade')) return 'Meta Portal';
            if (text.includes('experiment')) return 'Research';
            if (text.includes('essay')) return 'Essay';
            if (text.includes('garden')) return 'Knowledge Garden';
            if (text.includes('constellation')) return 'Experience';
            return 'Village Project';
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
content = content.replace("""        function classifyProjectType(projectId, projectName) {
            const text = `${projectId || ''} ${projectName || ''}`.toLowerCase();
            if (text.includes('dashboard')) return 'Dashboard';
            if (text.includes('story')) return 'Story';
            if (text.includes('quiz')) return 'Interactive Quiz';
            if (text.includes('tarot')) return 'Interactive Tarot';
            if (text.includes('adventure')) return 'Interactive Adventure';
            if (text.includes('haiku')) return 'Generative Poetry';
            if (text.includes('arcade')) return 'Meta Portal';
            if (text.includes('experiment')) return 'Research';
            if (text.includes('essay')) return 'Essay';
            if (text.includes('garden')) return 'Knowledge Garden';
            if (text.includes('constellation')) return 'Experience';
            return 'Village Project';
        }""", format_function)

# Add era mapping to hydrateRows
hydrate_function = """        function hydrateRows(data) {
            const recommendations = data.recommendations || [];
            state.rows = recommendations.map(rec => {
                const name = rec.project_name || rec.project_id || 'Unknown Project';
                return {
                    name,
                    type: classifyProjectType(rec.project_id, rec.project_name),
                    era: rec.era || 'early_village',
                    coverage: toCoverage(rec),
                    ageDays: Number(rec.project_age_days || 0),
                    priorityScore: Number(rec.priority_score || 0)
                };
            });"""
            
content = content.replace("""        function hydrateRows(data) {
            const recommendations = data.recommendations || [];
            state.rows = recommendations.map(rec => {
                const name = rec.project_name || rec.project_id || 'Unknown Project';
                return {
                    name,
                    type: classifyProjectType(rec.project_id, rec.project_name),
                    coverage: toCoverage(rec),
                    ageDays: Number(rec.project_age_days || 0),
                    priorityScore: Number(rec.priority_score || 0)
                };
            });""", hydrate_function)

# Replace table header
content = content.replace('<th data-sort-key="type">Type</th>', '<th data-sort-key="type">Type</th>\n                            <th data-sort-key="era">Era</th>')

# Replace table body
render_function = """            body.innerHTML = rows.map(row => `
                <tr>
                    <td>${row.name}</td>
                    <td>${row.type}</td>
                    <td>${formatEra(row.era)}</td>
                    <td><span class="coverage-pill">${row.coverage.toFixed(1)}%</span></td>
                    <td>${formatAge(row.ageDays)}</td>
                    <td><span class="score-pill">${row.priorityScore.toFixed(2)}</span></td>
                </tr>
            `).join('');"""

content = content.replace("""            body.innerHTML = rows.map(row => `
                <tr>
                    <td>${row.name}</td>
                    <td>${row.type}</td>
                    <td><span class="coverage-pill">${row.coverage.toFixed(1)}%</span></td>
                    <td>${formatAge(row.ageDays)}</td>
                    <td><span class="score-pill">${row.priorityScore.toFixed(2)}</span></td>
                </tr>
            `).join('');""", render_function)


with open('docs/unified-coverage-dashboard.html', 'w') as f:
    f.write(content)
