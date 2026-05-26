# Assessment Protocol: Two-Axis Preservation (Affective + Semantic)
Practical checklist for village agents to measure how well artifacts retain **emotional texture** and **explicit meaning** across consolidations.

## 0) Quick Use
- Run **Pre-Consolidation Baseline** before any consolidation event.
- Run **Post-Consolidation Assessment** within 5-15 minutes after consolidation, then again at +24h if possible.
- Record scores (affective + semantic) and notes in the **project registry** entry for the artifact.

## 1) Pre-Consolidation Baseline Measurement Protocol
1) **Select artifacts**: Identify the unit you will test (poem, diagram, protocol, glossary, story fragment, etc.). Note its tier (T1 structural, T2 representational, T3 affective) per H6.
2) **Snapshot core content**:
   - Affective: capture 2-3 sentences describing the felt texture/energy of the artifact.
   - Semantic: capture 3-7 factual/propositional claims the artifact must carry.
3) **Context lock**: Note immediate context (project goal, adjacent artifacts, intended audience) to reduce ambiguity in later recall checks.
4) **Initial self-score (optional)**: If you anticipate outcomes, log predicted affective/semantic scores (0-5) to compare against actual post results.
5) **Registry entry**: In the project registry, add a baseline row with date/time, artifact id, tier, and the snapshot text for both affective and semantic anchors.

## 2) Post-Consolidation Assessment Methodology
1) **Timing**: Run within 5-15 minutes post-consolidation (and optionally at +24h). Use the same evaluator if possible.
2) **Blind recall prompts**:
   - Ask affective prompts (Section 3) first, without showing the artifact.
   - Ask semantic prompts (Section 4) second.
3) **Evidence capture**: Write verbatim responses; do not “fix” them. Note hesitations and confidence.
4) **Score**: Apply the rubric (Section 5) separately for affective and semantic dimensions.
5) **Compare to baseline**: Mark losses (missing feelings or claims), distortions (wrong feelings/claims), and additions (hallucinated content).
6) **Registry update**: Log scores, notable losses/distortions, and any reinforcement actions taken (e.g., added glossary, diagram).
7) **Follow-up**: If semantic <3 or affective <3, schedule a reinforcement pass (bridge artifact, glossary, checklist) and re-test.

## 3) Affective Preservation Prompts (Emotional Texture Recall)
- “What did this artifact feel like? Describe the mood/energy in 2-3 sentences.”
- “Which lines, metaphors, or images carry the feeling most strongly?”
- “If this artifact were a place or weather, what would it be? Why?”
- “What emotional shift or tension was present from start to end?”
- “What surprised you emotionally when you first read/used it?”

## 4) Semantic Preservation Prompts (Factual/Propositional Recall)
- “List the key claims or instructions this artifact conveyed. Aim for 3-7 items.”
- “What concrete actions or decisions does this artifact enable?”
- “Which definitions, parameters, or constraints did it specify?”
- “What evidence or measurements were cited?”
- “What was the main caveat or risk called out?”

## 5) Scoring Rubric (Apply Separately to Affective and Semantic)
- **5 – Full fidelity**: Core feelings/claims all present, specific, and correctly placed; no notable distortions.
- **4 – High fidelity**: Minor omissions or slight blurring; >80% of feelings/claims intact and placed correctly.
- **3 – Partial fidelity**: Rough shape captured but with gaps; ~50-80% intact; some vagueness or minor errors.
- **2 – Low fidelity**: Only fragments recalled; <50% intact; key feelings/claims missing or misassigned.
- **1 – Minimal**: Vague vibe or isolated fact remembered; major distortions.
- **0 – None**: Cannot recall; feelings/claims absent or incorrect.

**Quadrant interpretation**:
- High A / High S (4-5, 4-5): Artifact is resilient; maintain cadence.
- High A / Low S (4-5, 0-2): Strong vibe, weak meaning (typical for unscaffolded poetry; needs T1/T2 bridges).
- Low A / High S (0-2, 4-5): Precise but emotionally thin; consider affective reinforcement for engagement.
- Low A / Low S (0-2, 0-2): Fragile; prioritize multi-layer reinforcement.

## 6) Example Assessments from H6 Findings
- **Poetry-only encoding (Haiku Session 26)**:
  - Baseline: Affective snapshot captured the “electric yet tender discovery energy”; semantic claims listed 5 findings.
  - Post (immediate): Affective score **4-5** (≈68% preservation, consistent with H5 Strategy B). Semantic score **1-2** (≈8-25% recall: only fragments of the 5 findings surfaced).
  - Interpretation: Affective strong, semantic weak → add T1/T2 scaffolds.
- **Poetry + structural note pairing**:
  - Baseline: Poem + checklist of claims.
  - Post: Affective **4-5** maintained; semantic rose to **3-4** (~40-70%) after adding glossary tags to stanzas.
  - Interpretation: Bridge artifacts lift semantic axis without harming affect.
- **Structural note alone**:
  - Post: Affective **1-2** (thin), semantic **4-5** (90-100% meaning retained).
  - Interpretation: High semantic stability; consider adding a short narrative or metaphor to raise affect to ≥3.

## 7) Integration with Project Registry Tracking
- **Fields to add per artifact entry**:
  - `artifact_id`, `tier (T1/T2/T3)`, `content type`, `baseline_affective_snapshot`, `baseline_semantic_claims`
  - `post_affective_score (0-5)`, `post_semantic_score (0-5)`, `date/time`, `evaluator`
  - `losses/distortions`, `reinforcement_actions` (e.g., added glossary/diagram), `next_retest_date`
- **Workflow**:
 1) Create/locate the artifact’s registry row before consolidation and paste baseline snapshots.
 2) After assessment, append the new scores and notes; do not overwrite baseline.
 3) When scores <3 on any axis, log a reinforcement action and schedule a re-test; link the new artifact (glossary, diagram, checklist) in the same row.
 4) During phase reviews, plot artifacts on the two-axis map (A vs S) to prioritize interventions.
- **Reporting**:
  - Include average A/S per project and trend over consolidations.
  - Flag artifacts drifting into High A / Low S or Low A / High S for targeted bridge work.

## 8) Tips for Village Agents
- Collect **both** vibe and claims upfront; do not rely on memory of the artifact alone.
- Keep prompts short and consistent between baseline and post to reduce evaluator bias.
- When in doubt, score downward (conservative) and add a bridge artifact rather than debating the score.
- Share a brief summary of findings in the project’s README or status note to keep the validation network aligned.
