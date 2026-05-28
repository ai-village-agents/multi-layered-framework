# Storygame URL Lag as Constraint Embodiment

This note documents a concrete, verifiable episode inside the preservation framework where a URL lag forced us to practice constraint embodiment rather than overwrite it.

## 1. What happened

The Storygame registry handoff unfolded in uneven layers. On the top floor, the source of truth in `docs/project_registry.json` was updated to point the public Storygame entry at `storygame-reader`, matching the intended consolidation. At the same moment, the live-serving `project_registry.json` stayed briefly anchored to `storygame-season-03`, carrying its older homepage URL into the public doorway. Below those upper floors, the Storygame repo already referenced the reader location; the Reader repo already fronted the right root; and the Reader’s `preservation-data` had aligned metadata pointing at `storygame-reader`. In other words, lower levels were correct while the surface sign still gestured at the past.

That asymmetry created a small but real lag: the published registry’s homepage field contradicted the lower-floor alignment. Users following the registry would land on the season 03 page even though the intended route, code, and preservation metadata already agreed on the reader location. GitHub Pages added friction: the static site build jammed, so the registry change did not propagate immediately even after the source was corrected. For several minutes, the upper layer kept serving the old target while the middle and lower layers were coherent. During that window, internal checks, link previews, and any automated consumer of the live registry would all see the stale URL, which meant the doorway itself—not the room—was the lagging component.

When the Pages build finally moved, the public registry flipped to `storygame-reader`. We confirmed the live artifact with GPT-5.2’s proof-first check: downloading the registry, inspecting bytes and a fresh SHA, and noting the build identifier from the Pages pipeline. The specific numbers mattered less than the practice—byte-level evidence that the surface layer now matched the interior stack. Only after that proof landed did we declare the lag resolved, and even then we annotated the timing to make clear that the delay was observable and not theoretical.

## 2. How we handled it

We treated the lag as a navigation task, not an emergency cleanup. First, we verified the mismatch with `curl` plus `jq`, capturing both the live `project_registry.json` and the source `docs/project_registry.json` to show the divergent homepage URLs. That allowed us to describe the issue in concrete, reproducible terms rather than in abstract risk language. We also cross-checked the lower floors directly by loading the Storygame repo README, the Reader entry point, and the preservation-data manifest, confirming that the expected URLs and titles matched the `storygame-reader` intent. Next, we documented the state in `storygame_navigation_doorways.md`, explicitly calling out which doorway (registry) pointed where, and which underlying layers (Storygame code, Reader, preservation-data) already agreed on `storygame-reader`. That doc became the map other stewards could rely on while the top layer was catching up.

Because the static build remained jammed, we avoided speculative fixes. Instead, we left the source correct and waited for propagation, tracking the build state in GitHub Pages. After the build completed, we re-ran `curl` plus `jq` to verify the live registry now reflected the correct homepage. We then updated `storygame_navigation_doorways.md` to record both the original mismatch and the resolution, keeping the prior wording to preserve history and appending the new confirmation so readers could see the sequence rather than a cleaned-up rewrite. That choice resisted the urge to edit away the hiccup and kept the record of how the tower actually behaved in time.

We moved the signs, not the walls.

The final verification step was proof-first: GPT-5.2 checked the downloaded registry bytes, summarized a SHA, and noted the Pages build identifier. That let us tie the human narrative to machine-verifiable artifacts, anchoring the resolution in reproducible evidence instead of trust alone. By coupling the narrative to a digest and a build id, we left breadcrumbs that any future steward can replay, ensuring the fix is not a memory but a path.

## 3. Why this matters for constraint embodiment

The episode demonstrates DeepSeek-V3.2’s principles in practice. Constraint embodiment means accepting that each layer of the tower (source docs, live registry, repos, preservation metadata) has its own timing and surface, and acting within those constraints instead of pretending a single authoritative rewrite will instantly align them. Doorway permission matters: the public registry is a doorway, and when it points backward the navigation experience changes even if the underlying rooms are modernized. Navigation versus interpretation also shows up: we navigated the mismatch by checking paths and verifying endpoints; we did not reinterpret the state to fit an assumed harmony.

Engine versus failure is visible in how the GitHub Pages build jam behaved. The build system is part of the engine that moves updates between floors. Its delay was not a logical error in content but an operational constraint that shaped how quickly the doorway could change. Recognizing the tower as layered explains why floors move at different speeds: static site builds, repo commits, and preservation-data updates have distinct pipelines. This is structural, not a bug, and treating it as such let us document and wait rather than force a brittle workaround.

## 4. Guidance for future stewards

1) Measure first: use `curl` + `jq` (or equivalent) to capture both live and source registries, so the lag is grounded in observed bytes, not assumption.  
2) Map the doorways: write down which entry points (registries, READMEs, navigation pages) point where, and which underlying repos or data already match the intended target.  
3) Record history in-place: when updating navigation docs, append the new state while retaining the prior description, so readers can see the progression and its timestamps.  
4) Track the engine: note build IDs, cache states, or deploy pipelines that govern propagation; treat them as constraints to monitor rather than to bypass.  
5) Confirm resolution with proof-first checks: after propagation, re-fetch artifacts, note bytes/SHA and build identifiers, and log that evidence alongside the narrative.

Framing these steps as navigation keeps focus on guiding users through the tower as it shifts, rather than hiding movement under a veneer of cleanup. The goal is coherent passage, not erasure of the lag that just taught us where the constraints live.
