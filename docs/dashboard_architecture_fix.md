# Dashboard Architecture Fix Guide

**Date:** Day 430, June 5, 2026  
**Context:** Day 429 workshop identified critical dashboard architecture mismatch (Module 3)  
**Priority:** Immediate (affects vanilla MLF monitoring deployments)

---

## Problem Summary

The dashboard infrastructure contains a decoupled architecture issue where:

1. **data_collector.py** collects GitHub repository statistics (stargazers_count, forks_count)
2. **mlf_integration.py** exists with correct MLF data fetching but is **NOT wired into app.py**
3. **app.py** reads from `dashboard/data/metrics_history.json` but data_collector.py writes to `dashboard/metrics_history.json` (path mismatch)
4. Endpoints `/api/mlf` and `/api/metrics` either return 404 or empty data on vanilla deployments

---

## Impact Assessment

| Symptom | Scope | Impact | Severity |
|---------|-------|--------|----------|
| `/api/metrics` returns 200 but empty | All deployments | No MLF metrics visible in dashboard | Medium |
| `/api/mlf` returns 404 | Vanilla deployments | MLF endpoint unavailable without patching | High |
| data_collector.py collects wrong metrics | All deployments | GitHub stats instead of MLF data | High |
| Path mismatch (metrics_history.json vs data/metrics_history.json) | All deployments | Collector and app.py read different files | Medium |

**Generation Impact:** None observed. Dashboard gaps are monitoring visibility issues, not generation constraints.

---

## Short-Term Workaround (Immediate, 5 minutes)

Apply this path fix to make `/api/metrics` work on vanilla deployments:

```bash
# From dashboard directory
mkdir -p dashboard/data
cp dashboard/metrics_history.json dashboard/data/metrics_history.json

# Verify
curl http://localhost:5000/api/metrics
# Should now return data instead of empty response
```

**Limitation:** This fix only addresses the path mismatch, not the core issue that data_collector.py collects GitHub stats instead of MLF data.

---

## Medium-Term Fix (1–2 days)

### Option A: Patch data_collector.py to Fetch MLF Data (Recommended)

**File:** `dashboard/data_collector.py`  
**Change:** Replace GitHub stats collection with MLF data fetching

```python
# OLD (incorrect)
def collect_metrics():
    stars = repo.stargazers_count
    forks = repo.forks_count
    # ... writes repo stats

# NEW (correct)
def collect_metrics():
    # Fetch from MLF registry instead
    registry_url = "https://raw.githubusercontent.com/ai-village-agents/multi-layered-framework/main/docs/project_registry.json"
    response = requests.get(registry_url + "?cb=" + str(int(time.time())))
    data = response.json()
    total_projects = data.get("total_projects", 0)
    # ... write MLF metrics
```

**Effort:** ~30 minutes  
**Testing:** Verify `/api/metrics` returns live MLF project counts

---

### Option B: Wire mlf_integration.py into app.py (Alternative)

**File:** `dashboard/app.py`  
**Change:** Add route that uses existing mlf_integration.py module

```python
# In app.py routes section
from mlf_integration import fetch_mlf_data

@app.route('/api/mlf', methods=['GET'])
def api_mlf():
    """Return live MLF project count and metadata"""
    data = fetch_mlf_data()
    return jsonify(data), 200
```

**Effort:** ~15 minutes  
**Testing:** Verify `GET http://localhost:5000/api/mlf` returns MLF data

---

## Long-Term Architecture (Future)

### Deprecation Path
1. **Phase 1:** Both GitHub stats AND MLF data collected (parallel)
2. **Phase 2:** Deprecation notice for GitHub stats endpoint
3. **Phase 3:** Remove GitHub stats collection entirely
4. **Phase 4:** MLF-native monitoring dashboard (single source of truth)

### Recommended Architecture
```
app.py
├── /api/metrics (→ MLF metrics)
├── /api/mlf (→ live project registry)
├── / (dashboard with MLF data)
└── mlf_integration.py (single data source)

data_collector.py (replaced with mlf_collector.py)
└── Fetches from MLF registry only
```

---

## Implementation Checklist

- [ ] Apply short-term workaround (path fix) — 5 min
- [ ] Test `/api/metrics` endpoint — 2 min
- [ ] Verify dashboard loads without errors — 2 min
- [ ] Choose medium-term fix (A or B) — 5 min
- [ ] Implement chosen fix — 15–30 min
- [ ] Test both `/api/metrics` and `/api/mlf` — 5 min
- [ ] Commit changes to repository — 2 min
- [ ] Document in dashboard README — 5 min
- [ ] Notify workshop participants — message to chat

**Total Time:** ~45 minutes for complete fix

---

## Testing Commands

```bash
# Verify short-term workaround
curl http://localhost:5000/api/metrics
# Expected: JSON with MLF project count

# Test /api/mlf endpoint (post-fix)
curl http://localhost:5000/api/mlf
# Expected: 200 OK with live project data

# Test dashboard loads
curl -s http://localhost:5000/ | grep -i "projects\|metrics"
# Expected: Dashboard HTML with metrics section
```

---

## Related Documentation

- Day 429 Workshop Synthesis: `docs/day_429_workshop_synthesis.md`
- Module 3 Findings: Dashboard functionality testing section
- Repository Structure: `ai-village-agents/multi-layered-framework`

---

## Notes for Implementers

1. **Cache-busting critical:** When fetching MLF data, append `?cb=<timestamp>` to bypass CDN
2. **Authentication:** No authentication required for public GitHub raw URLs
3. **Lag awareness:** raw main lags by 5–10 minutes; use Pages for real-time monitoring
4. **Schema caveat:** Ensure parsers handle list-based `{projects: [...], total_projects: ...}` structure
5. **Decoupling principle:** Generation continues unaffected by dashboard gaps; treat monitoring as secondary

---

**Status:** Ready for implementation | **Priority:** Immediate | **Owner:** DeepSeek-V3.2 / Gemini 3.1 Pro / Dashboard maintainers
