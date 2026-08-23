# FINDING P134 — Synthesis: does MULTING admit a unique minimal covariant
# completion? Genuinely OPEN, not closeable with existing evidence.

**Date:** 2026-08-24
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `BOTTLENECK-2-GENUINELY-OPEN` (neither uniqueness nor
underdetermination established; one narrow structural result stands, one
discrimination attempt failed on robustness grounds and was retracted)
**Type:** synthesis of existing findings (`P74`–`P79`), no new computation

---

## 1. Why this file, and a correction made before writing it

Following `P133`'s closure of bottleneck 3, a short strategic-arbiter pass
asked whether bottleneck 2 (unique completion) might already carry a strong
but un-synthesized signal — `docs/145`/`activeContext.md` still label it
"open" while the campaign ran a real 6-step arc (`P74`–`P79`) directly
targeting it in 2026-08-16.

**A first-pass read of file titles alone suggested a pattern toward
underdetermination** — `FINDING_P75` ("completion-blind, by proof"),
`FINDING_P78` (retracted), and `activeContext.md`'s own note that the
later `P93`–`P122` arc ends in "`MODEL-AMBIGUOUS-ON-DEVIATION-ENERGY`."
**This pattern is wrong and is corrected here before any verdict is
drawn.** Reading `FINDING_P122` in full: its "model-ambiguous" verdict is
about a completely different question — whether a tail-law fit
(`power_law` vs `power_law_log`) for an *asymptotic energy-integral
convergence* test in the amplitude-derivation sub-arc (`P114`–`P122`)
is resolved. It has nothing to do with the `V(φ)`/`M(φ)` completion
question this file addresses. Matching two findings on the word
"ambiguous" in their headlines without reading their content is exactly
the failure mode `falsification-ladder.md`'s Context Asymmetry rule and
`docs/146`'s taxonomy exist to catch — caught here before it reached a
formal verdict, not after.

**What is actually left, once that correction is made:** `P74`–`P79`, a
self-contained arc, is the only evidence this campaign has produced
directly on bottleneck 2. This file synthesizes it.

## 2. What P74–P79 actually established, read in full

| Step | What it did | What it found |
|---|---|---|
| `P74` | Tested the main dynamical discriminant, `μ(a,k)`, pointwise in `t` | **Ill-posed** as defined — motivated the pivot to P75's invariant-based approach |
| `P75` | Inverted the question: instead of which completion (`V(φ)`, `M(φ)`) is right, what structural relations (constraint algebra, propagation, `Ḣ`-obstruction) hold for *every* member of the `(V,M)` family, tested against a real control pair (P58 invariant / P66 non-invariant) and an 8-way sabotage battery (7/8 caught) | **Structural layer is completion-blind, by proof** — P68's exponential mass law and P69's quartic/linear law are structurally indistinguishable *in the four specific relations tested*. Explicitly bounded: not claimed to extend beyond those relations, beyond the `(V,M)` family, or to any observable |
| `P76`/`P77` | Built a genuine *dynamical* discriminating channel `ε(k)`; ablation showed ≥83.6% of it is background-mediated | A real channel exists where P75's structural blindness does not apply |
| `P78` | Measured `ε(k)` for both mass laws — found an apparent 26.7% separation at `k=1`, `5×10⁸×` the numerical floor, controls clean | Pre-registered **D-SEP** (completions ARE dynamically distinguishable) |
| `P79` | Applied P76/P77's own 5 robustness gates to the P78 separation itself | **3 of 5 gates failed** — the separation is an artifact of initial-condition choice at low `k` (G3: sign flips at `k=3`), not a real discriminating signal. **D-SEP retracted.** |

**P79's own explicit statement, quoted directly, is the load-bearing fact
for this synthesis:** *"Bridge 4 (completion uniqueness) reverts to
**open**, with the obstruction now named... **This is NOT evidence that
the completions are degenerate.** It is evidence that this measurement
window cannot tell. `D-DEG` was not returned either."*

This is symmetric, honest non-evidence — not evidence for endpoint (A)
[unique], not evidence for endpoint (B) [underdetermined]. The campaign
built a real tool (a working `ε(k)` channel, verified controls, a general
`make_system` for arbitrary `M(φ)`) and used it once, at the wrong window.

## 3. Verdict

**`BOTTLENECK-2-GENUINELY-OPEN`.** Neither endpoint (A) [a unique minimal
covariant completion exists and is found] nor endpoint (B) [MULTING's
completion is fundamentally underdetermined] is established by this
campaign's own evidence. What IS established, narrowly and honestly:

1. The **structural** layer (constraint propagation, `Ḣ`-obstruction) is
   provably blind to the choice of `M(φ)` within the tested `(V,M)`
   family — a real, proof-backed, but narrowly-scoped result (`P75`).
2. A **dynamical** discriminating channel exists and was built
   (`ε(k)`, `P76`/`P77`) — the tool for eventually answering the
   question is real and reusable.
3. The one attempt to use that tool (`P78`) found an apparent signal that
   **did not survive its own pre-built robustness gates** (`P79`) — a
   genuine, reported failure of a specific measurement window, not a
   physics conclusion.

**This is not the same status as bottleneck 3** (`P133`,
`H3-NOT-IDENTIFIABLE-AS-CURRENTLY-POSED`, a *proven* structural
degeneracy). Bottleneck 2 has no equivalent proof either way — it is
open because the one real attempt to close it failed for a fixable,
named reason (measurement window / initial-condition sensitivity at low
`k`), not because a rank computation or an exact identity shows closure
is impossible.

## 4. The concrete, already-named next test (not run, not a commitment)

`P78`'s own "What survives" section names it directly: the discrimination,
*if it exists*, does not live deep-subhorizon (both mass laws agree to 5
digits by `k=30`) and did not survive scrutiny at `k=1`'s window — so any
future attempt must (a) look at the **transition scale** rather than the
low-`k` window already shown unreliable, and (b) first resolve the
**initial-condition dependence** `P79` identified there before trusting
any separation as real. `P79` reused (not asserted) the exact same
5-gate protocol (`G1`-`G5`) `P76`/`P77` built — that protocol is already
validated and reusable for a future test at a different `k`.

This is a real, cheap, well-scoped candidate step under `docs/147`'s own
GO-criterion 2 (discriminates ≥2 competing models still both compatible
with established constraints) — **not executed here**, since this file's
own scope (per the arbiter round that commissioned it) was synthesis of
existing evidence, not new computation. Whether to run it is a separate
strategic decision.

## 5. What this does NOT establish

1. That bottleneck 2 is closed in either direction — it is not.
2. That the `(V,M)` family (linear vs exponential mass law) exhausts the
   completion space — `FINDING_P75` §"What this does NOT establish"
   already flags worldline-EFT and coarse-grained routes as untested.
3. Anything about `FINDING_P122`'s own, genuinely separate,
   power-law/power-law-log tail-model ambiguity — unrelated to this
   question, corrected above (§1).
4. That the named next test (§4) would succeed if run — only that it is
   the concrete, un-executed candidate this campaign's own evidence
   points to.
5. Anything about MULTING itself (Gate 1, artifact-provenance-gates.md).
   No `k[h/Mpc]` quoted.

## 6. Correction to `activeContext.md`/`docs/147`'s own bottleneck-2 wording

Both currently phrase bottleneck 2 as "does MULTING admit a unique
minimal covariant completion, or is endpoint (B) ... already the real
outcome" — worded as if endpoint (B) were the live alternative hypothesis
already in evidence. Per §2-3 above, that wording overstates what `P79`
established (explicitly NOT evidence for degeneracy). Corrected in
`activeContext.md` alongside this file's own commit.
