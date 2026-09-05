# FINDING P191 — a real Fisher-information forecast: synthetic high-z
# H(z) points WOULD measurably shrink v82's own (β1,β2) degeneracy
# ellipse, at realistic assumed precision — and the level-set slope's
# behavior past z=2.33 is richer than expected (peaks, then declines)

**Date:** 2026-09-05
**Continues:** `FINDING_P190`'s own named next step. Directly closes the
Pearl Registry entry logged 2026-09-02 (`next_check` 2026-11-15).
**Script:** `P191_fisher_forecast_high_z.py` (numpy/scipy, 5 positive
controls incl. 1 floor/negative control, ruff clean, project's own 908
tests unaffected — no shared module touched, same deliberately-
uncentralized P176/P189/P190 lineage convention).
**Skeptic review:** dispatched context-blind (claim.md + script only, no
reasoning history) per Step 8a — verdict **FALSIFIED** on the first
draft, with a real, confirmed, concrete bug found (see Correction
below). Fixed, then re-checked with a second targeted context-blind
pass on the fix itself — verdict **CONFIRMED-REAL-fixed** (no new issue
found under static trace; pytest run independently confirmed by me).
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** SUPPORTED — at 1% and 3% assumed relative
> precision, the shrinkage (73%, 46%) is large and unambiguous; at 10%
> precision it is real but marginal (14%, barely above the pre-
> registered 10% MCID). All numbers positive-controlled, step-size-
> converged (4-point plateau, not just 2), and independently
> re-verified after a real bug was found and fixed.
> **Ontological/mechanistic interpretation status:** N/A — this is a
> forward-looking statistical/information-theoretic property of TJB's
> own real χ² surface under a well-defined synthetic-data extension,
> not a claim about physical mechanism.
> **Causal/cosmological claim status:** N/A (`NO_AUTHOR_ERROR`).

## Correction (2026-09-05, context-blind skeptic-caught, applied before
finalizing — same discipline `FINDING_P176`'s own Correction section
established for this lineage)

The first draft's `augmented_chi2` called `H_of_z_kms` **directly on the
bare 4-element synthetic-z array** `[3,5,7,10]`, instead of building a
dense integration grid first (the pattern the script's own
`chi2_fixed_h0anchor` already uses, correctly, for TJB's real 33
points). Because the reference redshift `Z_SHOES=0.0233` was not
present in that sparse array, `H2_of_z`'s internal
`argmin(|zgrid-zref|)` silently picked the **nearest sparse point (z=3)**
as the integration reference — making `H(z=3)` identically equal to
`h0_anchor` for **every** `(β1,β2)`. That synthetic point contributed
**exactly zero** Fisher information, and `H` at z=5,7,10 came from a
degenerate 4-point trapezoidal integration between the sparse points
themselves, not TJB's real cosmic history. The floor/negative control
(σ_synth→∞) passed by tautology (it reduces to baseline regardless of
this bug); no positive control existed for the augmented pipeline
specifically — a real gap the skeptic named directly.

**Fixed** by mirroring `chi2_fixed_h0anchor`'s own already-correct
pattern exactly: build a dense grid (`_dense_zgrid_through`, spanning
0 through max(DESI's z=2.33, the largest synthetic z), with `Z_SHOES`
and every synthetic z inserted as explicit grid nodes), evaluate
`H_of_z_kms` once on that dense grid, then `np.interp` onto the target
synthetic z's. **Added** a new positive control
(`test_positive_control_synthetic_fiducial_values_are_physical`) that
would have caught the original bug immediately (asserts the fiducial
H(z) at each synthetic point is >50 km/s/Mpc away from `H0_anchor` —
the original bug pinned z=3 to exactly `H0_anchor`). **Also
strengthened** the step-size convergence check per the same skeptic
pass's second concern: the original 2-point (h=1e-5 vs 1e-6) comparison
could not distinguish a real plateau from two points sliding down the
same truncation-error curve — replaced with a 4-point tail-plateau
check (h ∈ {1e-4,1e-5,1e-6,1e-7}, requiring the last three to agree to
<1%), and extended to cover the ceiling's σ=1e-6 case too (the original
convergence check never tested the far-stiffer ceiling surface at all).

**What changed, numerically, buggy → fixed** (spotlighted row,
z∈{3,5,7,10} added together): condition number at σ=1%: 12332→8769;
σ=3%: 5268→6155; σ=10%: 5635→7043. Semi-axis shrinkage at σ=1%:
72.2%→73.0% (barely changed — at tight precision the wasted z=3 point
mattered little); σ=3%: 54.2%→45.6%; **σ=10%: 24.2%→13.6%** (the
biggest, most consequential correction — the MCID pass at loose
precision went from "comfortable" to "marginal").

## 1. Method (as pre-registered in `CLAIM_P191`)

1. **Cheap diagnostic**: extend `P190`'s own verbatim `E1(z),E2(z)`
   propagation (already positive-controlled there) to z beyond the real
   dataset's z=2.33 maximum.
2. **Main test**: an augmented χ² adding synthetic H(z) "points" fixed
   exactly at the fiducial (TJB's own real Table II best-fit) model's
   own prediction — standard Fisher-forecast convention — with an
   assumed relative uncertainty σ_synth. Same rescaled-coordinate 2×2
   Hessian eigen-decomposition `P176` already established, generalized
   to accept the augmented χ² function. Floor (σ→∞) and ceiling (σ→0)
   per FL Step 4a, resolved before trusting the realistic-σ sweep.

## 2. Results

**Positive controls, all PASS:** baseline χ²₃₃ reproduces TJB's own
15.75; baseline Hessian reproduces `P176`'s own slope
(6.073104×10⁷) and condition number (~8333); floor (σ→∞) matches
baseline to <1e-6; fiducial H(z) at the synthetic points is physical
(monotonic, [280.3, 387.7, 460.5, 508.2] km/s/Mpc at z=3,5,7,10 — far
from the H0_anchor=73.22 the original bug had silently pinned it to);
augmented Hessian's small eigenvalue is in a genuine 4-point plateau
(h=1e-5/1e-6/1e-7) at all 4 tested σ values including the ceiling.

**STEP 1 — diagnostic, past z=2.33** (this is the genuinely unexpected
part — the claim only anticipated "continues rising" or "saturates"):

```
z= 0.07:  -E1/E2 = 5.3855e+07        z= 3.00:  -E1/E2 = 6.1234e+07  <- PEAK
z= 0.50:  -E1/E2 = 5.7173e+07        z= 5.00:  -E1/E2 = 6.0432e+07
z= 1.00:  -E1/E2 = 5.9366e+07        z= 7.00:  -E1/E2 = 5.9374e+07
z= 1.97:  -E1/E2 = 6.1021e+07        z=10.00:  -E1/E2 = 5.7945e+07
z= 2.33:  -E1/E2 = 6.1202e+07        z=20.00:  -E1/E2 = 5.4719e+07
                                      z=50.00:  -E1/E2 = 5.0283e+07  <- BELOW z=0.07's value
```
The level-set slope does **not** monotonically continue rising, and does
**not** simply saturate — it **peaks near z≈3** (essentially flat with
z=2.33), then **declines**, eventually falling *below* its own z=0.07
starting value by z=50 (5.03×10⁷ vs 5.39×10⁷). Full range across
z=0.07–50: 18.9% spread (vs `P190`'s own 12.7% found across the real
dataset's narrower z=0.07–2.33 range alone).

**STEP 2 — Floor/Ceiling** (z∈{3,5,7,10}): floor condition number
8310.1 (== baseline, by construction). Ceiling (σ→0): condition number
10254.4, semi-axis shrinkage **100.0%**. This ceiling result is
**expected, not informative on its own**: with the model's `H²(z)`
exactly affine in `(β1,β2)` (established in `P190`), near-perfect
measurements at ≥2 z's with different level-set slopes can, in
principle, pin down 2 parameters exactly — this holds for essentially
*any* choice of ≥2 well-separated z's, not something specific to
{3,5,7,10}. **The ceiling does not discriminate a good z-choice from an
adequate one here; the realistic-σ sweep below is where the real
information is.**

**STEP 3 — realistic σ_synth sweep** (z∈{3,5,7,10} added together,
final corrected numbers):

| σ_synth | condition number | Δχ²=1 semi-axis | shrink | rotation | efficiency vs ceiling | MCID met |
|---|---|---|---|---|---|---|
| 1% | 8310→8769 | 0.1681→0.0454 | **73.0%** | 0.813° | 73.0% | Yes |
| 3% | 8310→6155 | 0.1681→0.0915 | **45.6%** | 0.524° | 45.6% | Yes |
| 10% | 8310→7043 | 0.1681→0.1453 | **13.6%** | 0.104° | 13.6% | Yes, marginally |

Per the pre-registered decision rule (`CLAIM_P191`): realistic-σ
shrinkage is well below ceiling (100%) at all three tested precisions —
this is **informative about the method**: the assumed σ is what limits
the effect size, not a structural ceiling on the (β1,β2) degeneracy
itself. Rotation is real but small (<1°) at every tested σ — the
dominant effect of adding these points is **shrinking** the ellipse
along its existing near-null direction, not reorienting it.

## 3. Verdict

**The MCID (≥10% semi-axis shrinkage OR ≥5° rotation) is met at all
three tested realistic precisions (1%, 3%, 10% relative), via the
shrinkage criterion in every case — but the margin shrinks sharply with
looser assumed precision** (73% → 46% → 14%, the last barely above the
10% bar). `P190`'s "in-principle openness" of bottleneck 3 **does
translate into a practically buildable path**: a hypothetical future
survey delivering H(z) at z∈{3,5,7,10} at even modest (10%) relative
precision would produce a real, though marginal, narrowing of v82's own
(β1,β2) degeneracy; at more ambitious (1-3%) precision the effect is
substantial (46-73% shrinkage).

**Consequence for bottleneck 3:** this is the first result in the
`P176`→`P190`→`P191` lineage that names a **concrete, quantified,
buildable direction** rather than only characterizing what already
exists. It does not resolve bottleneck 3 (see "What this does NOT
establish" below, from `CLAIM_P191`, none of which is superseded by
this result) — it establishes that *if* such high-z H(z) data existed,
it would help, and quantifies by how much as a function of assumed
precision.

## Pearl — the non-monotonic level-set slope (peak near z≈3, then
decline, eventually undershooting the z=0.07 value)

This was **not** anticipated by `CLAIM_P191`'s own outcome table (which
only considered "continues rising" or "saturates") — a genuine
unexpected-but-testable observation per the Pearl Gate
(`falsification-ladder.md` § Pearl Registry). Logged to
`pearl_registry/INDEX.md`: **observation** — `-E1(z)/E2(z)` peaks near
z≈3 and declines thereafter, non-monotonic over the full
computationally-accessible range; **falsifiable prediction** — if a
*different* choice of high-z synthetic points (e.g. z∈{20,30,50}, past
the peak, where the slope is falling steeply) were used instead of
{3,5,7,10}, the realistic-σ shrinkage should differ measurably from
this file's own {3,5,7,10} result, since the level-set slopes at those
z's diverge further from the baseline's χ²-weighted slope; **trigger
condition** — bottleneck 3 is revisited with a second Fisher-forecast
attempt; **next_check** 2026-12-01.

## What this does NOT establish (repeated from `CLAIM_P191`, now that
the result is known — none of these are superseded)

1. Does **not** predict what a real future high-z H(z) measurement
   would actually find — synthetic points sit exactly at the fiducial
   model's own prediction by convention; real data would differ.
2. Does **not** establish that z>2.33 H(z) measurements at 1-10%
   relative precision are technically achievable by any real,
   currently-existing or funded survey — σ_synth was assumption-swept
   for sensitivity, not sourced from a specific proposal's forecasted
   sensitivity.
3. Does **not** resolve bottleneck 3 even at the best tested precision —
   narrows the mathematical degeneracy of *this specific*
   `(H0,anchor, β1, β2)` parametrization; says nothing about connecting
   β1,β2 (or any internal MULTING quantity) to an independently-
   measurable physical observable (`docs/134`, untouched).
4. Does **not** evaluate whether v82's own theory is correct
   (`NO_AUTHOR_ERROR`).
5. The **ceiling** number (100% shrinkage, σ→0) is not itself
   informative about z-choice quality (see STEP 2 above) — do not quote
   it as "adding these 4 points could shrink the ellipse to nothing";
   quote the realistic-σ numbers instead.
6. Does **not** test whether a *different* choice of high-z z-values
   (fewer points, more points, or points chosen past the z≈3 peak found
   in STEP 1) would perform better or worse — that is the Pearl above,
   not yet attempted.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
