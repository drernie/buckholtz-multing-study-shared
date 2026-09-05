# FINDING P194 — dense information-profile scan of the (10, 16.957) window

**Date:** 2026-09-05
**Claim:** `CLAIM_P194_fisher_dense_scan.md`
**Script:** `P194_fisher_dense_scan.py`
**Continues:** `FINDING_P191` (estimand/MCID), `FINDING_P192` (boundary
z≈16.957), `FINDING_P193` (confirmed the pearl, built the analytic Fisher
matrix this file reuses verbatim).

## Result

All 4 positive controls PASS (baseline χ²₃₃ reproduces TJB's 15.75;
analytic Fisher matches finite-difference at baseline to 0.29%/0.08% and
at P193's augmented case to 0.10%/0.01%/0.0001%; entire scan grid stays
inside the P192 boundary with a 0.457 margin).

**STEP 1 — information profile.** A single synthetic point's
(β1,β2)-ellipse shrinkage rises **monotonically** from 16.24% (z=10.5) to
75.12% (z=16.5) at σ_synth=10%, confirming `CLAIM_P194`'s own falsifiable
predicate (monotonic increase toward the boundary).

**STEP 2 — greedy vs P193/P191.** Top-3 greedy set = {15.5, 16.0, 16.5};
top-4 = {15.0, 15.5, 16.0, 16.5}. Against P193's {12,14,16}:

| σ | top-3 greedy | P193 {12,14,16} | greedy better? |
|---|---|---|---|
| 1% | 82.65% | 85.05% | **No** |
| 3% | 76.63% | 76.66% | No (essentially tied) |
| 10% | 75.14% | 72.85% | **Yes** |

**Verdict: mixed, not a clean win for either set.** P193's specific
3-point choice beats the naive greedy top-3 at tight precision (1%, 3%)
and loses narrowly at loose precision (10%). This is a **direct,
quantitative confirmation of `CLAIM_P194`'s own pre-written Correction**
(§ "What this does NOT establish", item 3): greedy individually-best
points are not guaranteed jointly optimal for a matrix-valued criterion.
Neither set is "the" answer — which one wins depends on the assumed
measurement precision.

## Mechanism: NOT uniquely a 1/H(z) boundary-singularity effect — a real, quantified mix

A first pass at explaining the STEP 1 monotonic rise (before the
targeted second skeptic re-check below) proposed it was mostly a
generic `dH/dH² ~ 1/(2H)` divergence as H(z)→0 near P192's boundary,
since the gradient **direction** barely moves (spread 1.05° out of 180°
across the whole scan, z=10.5→16.5). A fixed-absolute-σ cross-check
(σ not scaled by H(z) at all) still rose monotonically (19.10%→73.13%),
which was read as confirming the boundary-proximity story dominates.

**A second, more targeted skeptic pass (this file's own STEP 1b
addition, 2026-09-05) found this reasoning incomplete.** `E1(z)` and
`E2(z)` — the two gradient-magnitude numerators — are **cumulative
integrals from z_ref=Z_SHOES**, so they grow by construction as
z_target increases, entirely independent of H(z). A near-constant
direction plus a rising fixed-sigma profile is equally consistent with
"|E| grows" as with "1/H grows" — the two were never separated. Printing
both magnitudes directly:

| Quantity | z=10.5 | z=16.5 | Ratio |
|---|---|---|---|
| \|E1(z)\| | 4.444e-43 | 1.029e-42 | **2.316×** |
| \|E2(z)\| | 7.697e-51 | 1.849e-50 | **2.402×** |
| H(z) [km/s/Mpc] | 508.46 | 191.64 | 2.653× (shrinkage) |

Since a single point's Fisher contribution at fixed absolute σ scales as
`(E/H)² ∝ E² · (1/H)²`, the two candidate mechanisms' actual
multiplicative contributions over this window are:

- **E-accumulation only:** E1² grows 2.316² = **5.36×**; E2² grows
  2.402² = **5.77×**.
- **1/H(z) boundary-proximity only:** (1/H)² grows 2.653² = **7.04×**.

**Both are real and of comparable order of magnitude** (5.4–5.8× vs
7.0× — a factor of ~1.3, not an order of magnitude). Neither mechanism
is negligible; neither one alone accounts for the full effect. The
honest statement is: the monotonic rise in discriminating power toward
the boundary is driven by **two entangled, comparably-sized effects**
— cumulative-integral growth of the force-derivative numerators, and
the generic `1/H(z)` divergence of the square-root map near a
domain boundary — plus a small, real but subdominant rotation of the
gradient direction (1.05° spread, contributing negligibly to the
magnitude story though it is the only truly MULTING/boundary-specific
piece of the three).

**This also means `CLAIM_P194`'s own falsifiable predicate is confirmed
at the level of the observed pattern (monotonic rise) but the
*mechanism* named in that predicate — "distance from the baseline's
χ²-weighted level-set slope" (P191's original pearl) — cannot be
cleanly separated from the other two candidates in this specific scan
design.** In this window, z further from the baseline slope, z closer
to the P192 boundary, and z with larger cumulative E1/E2 all increase
together — a genuine design confound, not resolved by this file. A
scan that varied these three independently (not available in this
reconstruction's single free coordinate, z) would be needed to fully
separate them.

**Does this walk back P193's CONFIRMED verdict?** No. P193's *numbers*
(72.87% vs 13.6% shrinkage at σ=10%, z∈{12,14,16} vs z∈{3,5,7,10}) are
unaffected — they are direct computations, not mechanism claims. What
changes is only the causal story for *why* those numbers came out that
way: "further from baseline slope" was the framing inherited from
P191's pearl, and it remains *correlated* with the real effect in this
window, but is not shown to be the *sole* or even the *dominant*
driver — the E-accumulation and boundary-proximity effects are at least
as large.

## Corrections applied (no-silent-correction discipline)

1. **Caught in `CLAIM_P194.md` itself, before code was written:** an
   earlier claim draft asserted "the top-N individually-best points ARE
   the best N-point combination" as a consequence of Fisher-information
   additivity. Wrong — additivity of matrices does not make a greedy
   scalar ranking jointly optimal. Corrected before this script existed;
   STEP 2's mixed result (table above) is the empirical confirmation.
2. **Step 8a skeptic pass, round 1 (2026-09-05), Probe 4 — real bug:**
   `test_positive_control_scan_grid_stays_in_domain` built its dense
   grid via `_dense_zgrid_through(SCAN_ZS)`, whose own `zmax=16.5` meant
   the grid never reached the checked point z=16.6 — `argmin` silently
   snapped to the nearest grid point (16.5), re-checking an already-
   checked point instead of the intended safety-margin point. Fixed by
   explicitly including the check points in the grid build, plus an
   exact-match assertion (`abs(zdense[idx]-z) < 1e-9`) so the bug cannot
   recur silently.
3. **Step 8a skeptic pass, round 1, Probe 1 — real methodological gap:**
   the original STEP 1 profile offered no way to tell a genuine
   direction-divergence effect from a trivial `1/H(z)` scale artifact.
   Fixed by adding `gradient_direction_deg` (pure angle) and
   `single_point_shrink_fixed_absolute_sigma` (fixed-σ cross-check).
4. **Step 8a skeptic pass, round 2 (targeted re-check, 2026-09-05) —
   real, deeper gap in round 1's own fix:** round 1's fixed-sigma
   cross-check correctly showed direction is nearly constant, but
   incorrectly treated "not direction" as "therefore 1/H(z)". It missed
   that `E1(z)`,`E2(z)` grow by construction (cumulative integrals from
   z_ref) independent of H(z), so a rising fixed-sigma profile is
   equally consistent with E-growth as with 1/H growth — an unresolved
   confound. Fixed by adding the `|E1|`,`|E2|` magnitude printout (STEP
   1b, second block) — see Mechanism section above for the resolved,
   quantified answer: both contribute, comparable order of magnitude.

## What this does NOT establish

1. Does not resolve which of {"distance from baseline slope",
   "boundary-proximity 1/H(z) divergence", "E-integral accumulation"} is
   *the* mechanism — this scan's one free coordinate (z) cannot vary
   them independently; all three co-vary in this window by construction.
2. Does not establish that the top-3/top-4 greedy set is better or worse
   than P193's {12,14,16} in any absolute sense — the comparison is
   precision-dependent (STEP 2 table), and neither is shown to be the
   true combinatorial optimum (a full N-point subset search was not
   attempted, as `CLAIM_P194` already stated it would not be).
3. Does not scan to the boundary itself (stops at z=16.5, margin 0.457)
   — same conservative-margin caveat as `CLAIM_P194`.
4. Does not establish that any of these z-values are realistically
   observable — inherited caveat from P191-P193.
5. Does not resolve bottleneck 3 — `docs/134` remains untouched.
6. **Does not walk back P193's CONFIRMED verdict on the pearl's raw
   prediction** (more shrinkage further from baseline, in this specific
   window) — only qualifies the *causal story* behind it, per the
   Mechanism section above.

## MCID

Inherited from `CLAIM_P191`/`P193` (≥10% shrinkage OR ≥5° rotation).
STEP 1's profile clears MCID at every scanned z≥10.5 (16.24% minimum).
The rotation MCID is never approached by direction alone (max 2.40°) —
shrinkage is the operative criterion throughout this file, consistent
with P191-P193.

## Pearl / methodological carry-forward

The `pearl_registry/INDEX.md` methodological-finding row (next_check
2026-12-15, "standard finite-difference does not converge near a
boundary") stands unchanged — P194 used the analytic method throughout
and never needed finite differences.

A **new** methodological lesson from this file, worth its own registry
line: **a monotonic trend correlated with a hypothesized mechanism is
not evidence FOR that mechanism specifically when ≥2 alternative
mechanisms are mechanically guaranteed to co-vary in the same scan** —
here, "distance from baseline slope" (the P191 pearl's own framing),
"distance from a domain boundary," and "magnitude of a cumulative
integral from a fixed reference point" all increase together as a
single free coordinate (z) increases toward that boundary. Separating
them requires a design with ≥2 independently-varying coordinates, not
available in this 1-parameter (z) scan.
