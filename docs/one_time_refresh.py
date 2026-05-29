import json
import logging
from auto_refresh_monitor import (
    load_registry, 
    load_project_registry,
    calculate_village_wide_coverage, 
    regenerate_preservation_data, 
    update_dashboard_statistics, 
    CONFIG,
    write_preservation_data
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('RefreshScript')

logger.info("Loading registry...")
registry = load_registry()
project_registry = load_project_registry()

logger.info("Analyzing coverage...")
village_wide_coverage = calculate_village_wide_coverage(registry, project_registry)
# The monitor uses an empty dict for coverage_stats in regenerate_preservation_data because the full data is computed there
coverage_stats = {} 

logger.info("Generating preservation data...")
preservation_data = regenerate_preservation_data(registry, coverage_stats, village_wide_coverage)

if 'preservation_points' in preservation_data and 'points' not in preservation_data:
    preservation_data['points'] = preservation_data['preservation_points']

write_preservation_data(preservation_data)

logger.info("Updating dashboard data...")
update_dashboard_statistics(coverage_stats, village_wide_coverage)
logger.info("Done.")
