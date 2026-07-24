# docs/139 — Internal Null / Hypothesis Registry (RED tier — not author-facing)

**Date:** 2026-07-24
**Origin:** see docs/137's Origin note — same harvest-and-triage lineage.
**Purpose:** internal only. These items are real, useful project artifacts — kept, not deleted —
but must never reach TJB in their dossier-v1 phrasing, and several need permanent downgrade
language applied wherever else they appear in this project's docs/memory (not just here).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## R-1. Birge-ratio "LLM noise vs. genuine underdetermination" claim

**Original claim (dossier v1, I-9):** "This is NOT LLM noise — β is genuinely underdetermined by
the preprint," backed by Birge ratio R_B(β_d)=15.9, R_B(β_q)=24.1, p<1e-4.
**Why this is not established:** Birge-ratio methodology assumes independent measurements of one
quantity with a comparable, characterized uncertainty model. Three LLM outputs to a shared prompt
are not that — the spread could reflect different implicit prompt interpretations, different
hidden assumptions, different optimization procedures, sampling randomness, or plain model error,
none of which is "measurement uncertainty" in the Birge sense.
**Correct status:** `CROSS-SERVICE OUTPUTS ARE PROCEDURALLY INCONSISTENT` [RECOMPUTED-SAME-PIPELINE].
`THE PUBLIC SPECIFICATION MAY BE UNDERDETERMINED` remains a live, plausible **hypothesis**, not a
metrological finding.
**What would actually test it:** freeze one source package and one prompt, require an explicit
derivation (not just a final number) from each service, and check whether the source materials
themselves admit multiple valid solutions — not yet done.
**Action:** retract "metrological proof of underdetermination" framing everywhere it appears in
this project's memory/docs; keep the raw R_B numbers as a `[RECOMPUTED-SAME-PIPELINE]` fact about
cross-service disagreement, nothing stronger.

## R-2. Global p-values for Eq.32 (6×10⁻⁵) and 7:9:17 (1/624)

**Correct status:** rank-in-a-defined-grid, not a calibrated global p-value — see docs/138 Module
F for the corrected framing and the broadened-space rank-degradation nuance the v1 dossier
compressed away. Kept here as a flag that this correction should propagate to any FUTURE internal
restatement, not just the TJB-facing draft.

## R-3. S3 → "exactly 6 isomers" as a prediction

**Original claim (dossier v1, V-6):** three independent appearances of the number 6 (Koide
invariance, Cayley 1+5 split, NCG KO-dimension) framed as predicting the isomer count is exactly 6.
**Correct status:** `NUMEROLOGICAL/STRUCTURAL CONJECTURE — MECHANISM ABSENT`. Three numerical
coincidences pointing at the same integer do not establish a shared causal structure; the pearl
registry's own original entry already tags this `[HARVEST-CANDIDATE]`, not confirmed — the
dossier's phrasing drifted toward "prediction" during compression. Never present this to TJB as
a result; at most, as a question ("does your framework predict exactly 6, or does it allow other
counts?").

## R-4. "4/3-origin / 7:9:17 mechanism search exhausted"

**Correct status:** exhausted means *within the five specific literatures/niches actually checked
and the specific sources searched* — not a claim that no derivation exists anywhere in
mathematics or physics. The project's own memory already uses the more careful phrase "genuinely
open, not overlooked" in most places; the dossier's one-line compression ("exhausted across five
niches") should always carry the "within the niches checked" qualifier when restated.

## R-5. Covariant-completion / equivalence-principle "kill"

**Original claim (dossier v1, §III):** presented close to a general statement that a repulsive
MULTING dipole contradicts the equivalence principle.
**Correct status:** the actual result (docs/130-131) is scoped to **one specific completion
attempt** (CANDIDATE-L1, with its own stated assumptions) — not a theorem ruling out every
possible covariant completion. Repulsive effective forces from extra fields, gradient terms,
nonminimal couplings, or composite-body response are not excluded by this result. Correct
statement form: "Under assumptions A, B, C, this specific completion fails on an EP-adjacent
ground" — never "repulsive MULTING dipole contradicts EP" unqualified.

## R-6. Growth-branch quantitative predictions (V-7 two-hump ε(z), V-9 5–15% fσ8 suppression)

**Correct status:** project-generated hypotheses contingent on an as-yet-unspecified author
response law (η). Not MULTING predictions until TJB fixes the relevant mechanism. Keep as
internal pearls with their existing next_check dates; do not present as forecasts of what
MULTING implies.

## R-7. II-5 "no literature precedent" novelty claim

**Correct status:** absence of hits in the sources we searched is not proof of novelty (absence
of evidence ≠ evidence of absence), and Verlinde's cluster-scale failure does not automatically
validate a different mechanism occupying that gap. Downgrade to: "no direct analog found in the
sources we checked" — a scoped, honest search-result statement, not a novelty verdict.

---

## Meta-note for future harvests

Every item above shares one root cause: a genuinely interesting internal finding, stated with
appropriately hedged language in its ORIGINAL source (a pearl, a null_results file, a docs/
entry), had its hedge quietly dropped or compressed away during dossier synthesis. The fix is not
"don't harvest these" — several (R-1's raw numbers, R-3's structural observation, R-5's specific
completion result) are legitimately useful internal signal. The fix is: **carry the original
hedge forward verbatim, or something at least as cautious, every time the claim is re-stated** —
compression that drops a hedge is itself a finding worth catching, the same class of error as a
stale number.
