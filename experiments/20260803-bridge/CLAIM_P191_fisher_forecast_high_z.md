# CLAIM P191 — Fisher-information forecast: would synthetic high-z H(z)
# points measurably shrink/rotate v82's own (β1,β2) degeneracy ellipse?

**Date:** 2026-09-05
**Continues:** `FINDING_P190`'s own named next step (item 5 of "What this
file does NOT establish") — "quantify how much different z-coverage
would be needed to meaningfully narrow the degeneracy — that would
require a real Fisher-information/forecast calculation, not attempted
here." Directly operationalizes the Pearl Registry entry logged
2026-09-02 (`next_check` 2026-11-15, row starting "FINDING_P190
(exact-vs-approximate degeneracy check...)").
**Bottleneck:** #3 (Absolute scale / observable mapping, `docs/147`).
Forward-looking (what-if a future/planned dataset existed) — distinct
from `P182`-`P187`'s real-data/real-literature confound-breaking
attempts and from `P190`'s purely retrospective structural check.
**Authorization:** explicit user go-ahead given 2026-09-05 (session
transcript) — this is the one item `CURRENT_EVIDENCE_STATE.md` §5 marks
RECOMMENDED, NOT AUTHORIZED until a separate go-ahead; that go-ahead has
now been given for this specific test only.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 **descriptive** (a structural/statistical property
of TJB's own real χ² surface plus a well-defined synthetic-data
extension — not a claim about what future data will actually show, not
a causal claim about physics; same L0 tag as `P176`/`P190`, the direct
precedents this continues).

---

## EstimandOps L0 gate

**Classified DESCRIPTIVE, not predictive, not causal.**

- **Not causal**: no intervention on the real universe is modeled;
  "adding synthetic points" is a property of an estimator's information
  content, not a treatment applied to a population.
- **Not predictive** in the EstimandOps sense ("what will X be for a new
  case") either — a Fisher forecast evaluates the information content a
  *hypothetical* dataset would contribute to an *existing* estimator, at
  the estimator's own current best-fit point. It does not forecast the
  value of a specific new observation.
- **Descriptive**: "what is the shape/size of the (β1,β2)
  uncertainty ellipse implied by TJB's own real χ² surface, under
  [baseline] vs [baseline + synthetic high-z points]?" — the same class
  of question as `P176` (real Hessian at 7 fit points) and `P190` (real
  coefficient functions E1(z)/E2(z)), extended to a synthetic-data
  scenario.

## Estimand

| Field | Value |
|---|---|
| Population | TJB's own real 33-point H(z) compilation (31-pt cosmic chronometer + SH0ES z=0.0233 + DESI DR2 z=2.33), reused **verbatim** from `P176` — this IS the dataset, not a sample. |
| Intervention | Adding a set of synthetic H(z) "points" at z > 2.33 (beyond the real dataset's current maximum), each fixed **exactly** at the fiducial model's own prediction (TJB's own reported Table II best-fit, `unconstrained_spotlighted` row), with an assumed measurement uncertainty σ_synth — swept across {1%, 3%, 10%} relative, not fixed to one arbitrary number. |
| Comparator | Baseline = real 33-point dataset alone — `P176`'s own already-established Hessian / condition number / near-null slope at the spotlighted row. |
| Endpoint | Three linked descriptors of the (β1,β2) covariance ellipse at fixed `H0,anchor`, in `P176`'s own rescaled coordinates: (1) Hessian condition number, (2) the Δχ²=1 semi-axis length along the near-null eigenvector, (3) the near-null eigenvector's slope/rotation angle. |
| Summary measure | Relative change (baseline → augmented) in each of the three endpoints, reported as ratios/percentages — **not p-values**: a forecast is deterministic given the assumed σ_synth, there is no sampling uncertainty to test. |
| MCID | "Measurably shrink/rotate" = **≥10% reduction in the Δχ²=1 semi-axis length**, OR **≥5° rotation of the near-null eigenvector**. The 10% bar is anchored to `P190`'s own found 12.7% z-dependence of the *local* level-set slope — the closest existing scale of "real, non-trivial variation" in this exact system — not a round-number default. |
| ICE | N/A — a static forecast has no missing-data/dropout mechanism. |

**Natural language statement** (written before any result is known):
*"We estimate the relative change in the (β1,β2) parameter-uncertainty
ellipse's size and orientation (condition number, Δχ²=1 semi-axis,
near-null eigenvector angle) for TJB's own real 33-point H(z)
chi-squared surface, comparing baseline (real data only) against
baseline-plus-synthetic-high-z-points (z ∈ {3, 5, 7, 10}, each fixed at
the fiducial model's own prediction, σ_synth swept across {1%, 3%,
10%} relative), with no intercurrent events."*

## What this does NOT mean (required, ≥3)

1. Does **not** predict what a real future high-z H(z) measurement would
   actually find — synthetic points sit exactly at the fiducial model's
   own prediction by Fisher-forecast convention; real data would differ.
2. Does **not** establish that z>2 H(z) measurements at the assumed
   precision are technically achievable — σ_synth values are
   assumption-swept for sensitivity, not sourced from any specific
   proposed survey's real forecasted sensitivity.
3. Does **not** resolve bottleneck 3 even in the best case — an improved
   condition number narrows the mathematical degeneracy of *this
   specific* `(H0,anchor, β1, β2)` parametrization; it says nothing about
   the separate, still fully open "absolute scale / observable mapping"
   question of connecting β1,β2 (or any internal MULTING quantity) to an
   independently-measurable physical observable (`docs/134`, untouched).
4. Does **not** evaluate whether v82's own theory is correct
   (`NO_AUTHOR_ERROR`).

## Floor–Ceiling Interval (FL Step 4a, resolved BEFORE the main run)

| | Construction | Question it answers |
|---|---|---|
| **FLOOR** | Synthetic points with σ_synth → ∞ (zero weight) | Does the augmentation correctly reduce to baseline when the new points carry no information? (Also serves as the negative control.) |
| **CEILING** | Synthetic points with σ_synth → 0 (perfect precision) at the *same* z-values | What is the maximum possible condition-number improvement achievable by measuring exactly at these z's, at any precision? Bounds what any real future survey could achieve here. |

**Decision rule, checked before trusting any realistic-σ result:**
- If ceiling itself shows negligible improvement (condition number barely
  moves even at σ→0) → **TASK_INFEASIBLE** for these z-values: the added
  points carry little independent information regardless of precision,
  and the honest conclusion is that this specific z-range does not
  practically help bottleneck 3 — not evidence against the claim, a
  finding about the world.
- If realistic-σ improvement ≈ ceiling → informative about the world:
  the limiting factor is genuinely how many/how-precise such points
  would be, and current assumptions are already near the best case.
- If realistic-σ improvement ≪ ceiling → informative about the method:
  the assumed σ is too loose to extract the available information; a
  tighter (but still plausible) σ assumption would be needed to see the
  real effect.

## Positive controls

1. **Reuse `P176`'s own `chi2_fixed_h0anchor` verbatim** (already
   positive-controlled against TJB's real reported `χ²₃₃` for two Table
   II rows to <0.1%) — no re-derivation, straight copy into this
   script, same convention `P190` already used.
2. **Floor check doubles as positive control**: augmented χ² at
   σ_synth → very large (e.g. 1e6× the real DESI point's uncertainty)
   must reduce to baseline χ² to < 1e-6 relative error — confirms the
   augmentation term correctly vanishes at zero weight before trusting
   any nonzero-weight result.

## Cheapest differentiating test, ordered by cost

1. **(cheapest, diagnostic only)** Extend `P190`'s own `-E1(z)/E2(z)`
   level-set-slope computation to z ∈ {3, 5, 7, 10, 20} (same verbatim
   machinery, just wider z-range) — does the already-observed monotonic
   rise (5.39×10⁷ at z=0.07 → 6.12×10⁷ at z=2.33, with shrinking
   increments near the top of that range) continue, or does it visibly
   saturate? This is a cheap analytic pre-check of whether extending
   past z=2.33 is even a promising direction, before running the full
   Fisher-matrix comparison.
2. **Main test**: Hessian condition number / Δχ²=1 semi-axis / near-null
   angle, baseline vs. augmented, across the {3,5,7,10}×{1%,3%,10%}
   grid, floor and ceiling included.

## What this does NOT establish (repeated for the artifact itself, not
just the estimand)

1. Does not identify a *specific, currently-existing or funded* survey
   that could deliver H(z) at z>2.33 at the assumed precision — that is
   an observational-astronomy question outside this project's scope.
2. Does not repeat or supersede `P182`-`P187`'s real-data confound-
   breaking attempts.
3. Does not connect to `FINDING_P165`'s ε-absorption mechanism (out of
   scope, already retracted twice in that lineage).
