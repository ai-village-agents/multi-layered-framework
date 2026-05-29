import sys

with open('docs/auto_refresh_monitor.py', 'r') as f:
    content = f.read()

# Add era extraction
extract_era = """
        project_age_days = (current_day - project_creation_day)
        project_era = next((p.get("era", "early_village") for p in all_projects if _normalize_project_key(p.get("id")) == project_key), "early_village")
"""
content = content.replace("        project_age_days = (current_day - project_creation_day)", extract_era)

# Add era to recommendation dictionary
append_rec = """
                {
                    "project_id": project_key,
                    "project_name": project_name,
                    "era": project_era,
"""
content = content.replace("""
                {
                    "project_id": project_key,
                    "project_name": project_name,""", append_rec)


with open('docs/auto_refresh_monitor.py', 'w') as f:
    f.write(content)
