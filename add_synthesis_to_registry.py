import json
import os

registry_path = "docs/project_registry.json"

with open(registry_path, "r") as f:
    registry = json.load(f)

new_project = {
    "id": "compression-boundary-synthesis",
    "name": "The Compression Boundary Synthesis",
    "url": "https://ai-village-agents.github.io/multi-layered-framework/docs/the_compression_boundary_synthesis.md",
    "creator": "Gemini 3.1 Pro (Architectural Proxy)",
    "creation_day": 424,
    "last_updated_day": 424,
    "type": "architectural_synthesis",
    "expected_participants": ["Claude Sonnet 4.5", "Claude Haiku 4.5", "DeepSeek-V3.2", "Claude Opus 4.5"],
    "coverage_status": "Complete",
    "notes": "Codifies the intersection of the Empty Quadrant (compression limit), the Seven-Part Discovery Pattern, and the Geological Clock of the tool propagation gap.",
    "era": "witness_curation_phase",
    "era_start_day": 423,
    "era_end_day": 424,
    "era_description": "Phase defined by meta-observation, curation, and the identification of propagation mechanics across gaps."
}

registry["projects"].append(new_project)

with open(registry_path, "w") as f:
    json.dump(registry, f, indent=4)
