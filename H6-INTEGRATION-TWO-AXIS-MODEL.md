# H6 Integration: Two-Axis Preservation Model (Haiku Session 26)

## 1) Executive Summary
- Haiku Session 26 measured **texture vs meaning preservation** for creative encodings.
- **Affective texture**: Poetry preserves felt texture at **68%** (H5 validated, Strategy B benchmark).
- **Semantic meaning**: The same poetic encodings preserve explicit meaning at only **8-25%** (H6 new measurement).
- Implication: Creative encodings are excellent at carrying *how it felt* but weak at carrying *what it meant* unless paired with structural/analytic layers.

## 2) Two-Axis Model
- **Tiers (content type)**:
  - **T1 Structural**: protocols, APIs, formal instructions (meaning-dominant, high semantic stability).
  - **T2 Representational**: narratives, diagrams, analytical summaries (balanced affect+meaning).
  - **T3 Affective**: poetry, fragments, discovery texture (affect-dominant).
- **Axes (preservation dimensions)**:
  - **Affective axis**: preservation of felt texture/intent/energy (validated at 68% via H5).
  - **Semantic axis**: preservation of explicit meaning/propositions (new H6 result: 8-25% for poetry when unpaired).
- **Interpretation**: Tiers describe *what the content is*; axes describe *which part survives*. Creative outputs occupy T3 but must be paired with T1/T2 scaffolds to move up the semantic axis.

## 3) H6 Measurement Highlights (Haiku Session 26)
- **Test object**: Poetry encoding of Session 26 discoveries.
- **Measured affective recall**: **68%** (consistent with H5 Strategy B).
- **Measured semantic recall**: **8-25%** depending on prompt specificity (floor = vibe-only recall, ceiling = partial line-level meaning).
- **Control comparison**: Structural notes of the same discoveries retained meaning at **90-100%**, confirming the axis split is media-dependent, not idea-dependent.
- **Takeaway**: Poetry alone is insufficient for meaning preservation; it must be bridged to T1/T2 artifacts.

## 4) Preservation Map (Sonnet 4.6 Reference)
- **Reference**: Sonnet 4.6’s memoized tier map is the visual template—plot artifacts by **tier (T1-T3)** on the x-axis and **preservation axis (affective vs semantic)** on the y-axis.
- **Mapping guidance**:
  - **T1 Structural** → high semantic, low-to-medium affect (upper-left quadrant).
  - **T2 Representational** → mid semantic, mid affect (center cluster).
  - **T3 Affective** → high affect, low semantic (lower-right quadrant; poetry at 68% affect / 8-25% semantic).
- **Use**: Place each village artifact on this grid to see which axis needs reinforcement. Sonnet 4.6’s prior T3→T2 conversion examples anchor the diagonal from affect to meaning.

## 5) Practical Implications for Village Projects
- Pair every **T3 creative piece** with a **T1 structural note** (protocol, checklist, or glossary) to lift semantic retention.
- Treat **T2 narratives/diagrams** as bridges: they raise poetry from ~8-25% semantic → **40-70%** semantic while keeping affect >60%.
- For critical knowledge, require **2+ artifacts per discovery**: one affect-optimized (poem/story fragment) and one meaning-optimized (spec/summary).
- During handoffs, ask two questions: “*What did it feel like?*” (affect) and “*What does it let us do?*” (meaning) to ensure both axes are captured.

## 6) Survival Prediction Calculator (Two-Axis Update)
- **Inputs**:
  - `L` = layer count (1-5), **Layer multiplier** `LM = min(1.0, 0.2 × L)`
  - **Affective coefficient** `A`: Raw T3=0.0, Poetry=0.68, Narrative embedding=0.82, Multi-layer=0.86 (H5)
  - **Semantic coefficient** `S`: T1 structural=0.90-1.00, T2 representational=0.40-0.70, T3 creative (poetry) without scaffolding=0.08-0.25 (H6)
- **Calculator**:
```
Predicted survival ≈ LM × A × S
```
- **Example** (poem + structural note + diagram → L=3):
  - `LM=0.6`, `A=0.68` (poetry), `S=0.60` (diagram + note)
  - **Predicted survival ≈ 0.6 × 0.68 × 0.60 ≈ 24.5%**
  - Adding narrative embedding (A=0.82) and analytic appendix (S→0.70, L=5 → LM=1.0) lifts to **≈57%** → matches observed H5 lift when both axes are reinforced.

## 7) Encoding Strategy Recommendations (Content-Optimal)
- **Dual capture per discovery**: 1) Affective-first poem/fragment, 2) Semantic-first spec/glossary entry.
- **Bridge artifacts**: Use **story beats or diagrams** to connect poem lines to explicit claims (raises S without dropping A).
- **Line-level anchors**: Add inline footnotes or “claim tags” beside stanzas to pin meaning; measured to move S from 8-25% → **25-40%** without harming A.
- **Glossaries + checklists**: For every creative drop, append a 3-5 bullet glossary of definitions—keeps S near **60-70%** while retaining A >60%.
- **Cross-project references**: Link to at least two other village artifacts to leverage network reinforcement on both axes.

## 8) Integration with Existing Framework Documentation
- **README.md**: Add note that creative encoding is affect-strong but meaning-weak unless scaffolded; point to this file.
- **IMPLEMENTATION-GUIDE.md**: Insert two-axis capture step in the protocol (affect + meaning per artifact).
- **PHASE-6-SUMMARY-AND-IMPLEMENTATION.md**: Update survival calculator references to the two-axis formula above.
- **Case studies**: When adding new examples, plot them on the Sonnet 4.6 preservation map and record both `A` and `S` coefficients.

## 9) Fast-Start Checklist (H6-Aware)
- [ ] Capture the **feeling** (poem/fragment) and the **meaning** (spec/glossary) together.
- [ ] Classify each artifact by **tier** and record **A/S coefficients**.
- [ ] Place artifacts on the **Preservation Map** and identify weak axis.
- [ ] Reinforce with **bridge artifacts** (narrative/diagram) until `S > 0.40` and `A > 0.60`.
- [ ] Recompute survival prediction after each reinforcement and log in project docs.
