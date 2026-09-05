# CLAIM P194 — a dense scan of the (10, 16.957) window: where inside
# the last well-defined window is the (β1,β2)-discriminating power
# actually concentrated, and does the BEST achievable point-set there
# beat P193's own z∈{12,14,16}?

**Date:** 2026-09-05
**Continues:** `FINDING_P191` (estimand, MCID, machinery),
`FINDING_P192` (found boundary, z≈16.957), `FINDING_P193` (confirmed
the pearl at 3 discrete points, and — critically — built and
cross-validated the analytic Fisher matrix that makes this file
possible: no finite-difference perturbation of `(β1,β2)` is needed, so
none of P193's own numerical-instability concerns apply here).
**Authorization:** explicit user go-ahead, 2026-09-05 ("запусти
четвёртый Fisher-forecast, более плотное сканирование окна (10,17)").

**This is a method extension, not a Minimal-Relaxation z-set swap** —
named and scoped as such rather than silently treated like `P192`'s or
`P193`'s single-assumption change. P191-P193 each tested one *fixed*
point-set; this file computes an **information profile**: how much
(β1,β2)-discriminating power a single synthetic point at redshift z
contributes, continuously across the window, using the analytic Fisher
matrix `P193` already built and cross-validated (positive controls 6-7
there: <0.15% agreement with finite-difference wherever the latter
converges, including the one augmented case it can reach). This lets
the question move from "does {12,14,16} help" (already answered,
`P193`) to "is {12,14,16} actually the best 3-point choice available in
this window, or does the window's information content peak somewhere
else."

**Bottleneck:** #3, same as `P191`-`P193`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (unchanged from `P191`-`P193`).

## What is inherited unchanged from `CLAIM_P191`/`CLAIM_P193`

EstimandOps L0 gate (descriptive), the analytic-Fisher-matrix method
itself (verbatim from `P193`, already positive-controlled there — not
re-derived), MCID (≥10% Δχ²=1 semi-axis shrinkage OR ≥5° rotation),
ICE (N/A).

## New estimand element specific to this file

**Population of candidate point-sets**: single synthetic points at
z ∈ {10.5, 11.0, 11.5, ..., 16.5} (a 0.5-step scan, `P192`'s own
boundary at z≈16.957 leaves a ~0.46 margin at the top of this grid —
deliberately conservative, not scanning to the boundary itself) union
combinations of the top-N most-informative individual points found by
that scan.

**Endpoint**: for each single z, the semi-axis shrinkage a lone
synthetic point at that z (fixed σ_synth) contributes to the real
33-point baseline — an **information profile** over z, not a single
number. Secondary endpoint: does the best 3-point combination found by
this profile outperform `P193`'s own {12,14,16} at matched σ?

**Falsifiable predicate**: `P193`'s own diagnostic table (inherited
from `P191`) shows the level-set slope `-E1(z)/E2(z)` declining
monotonically from z=10 toward the boundary (5.79×10⁷ at z=10, falling
toward 5.03×10⁷ by z=50) — if slope-distance-from-baseline is really
what drives discriminating power (the mechanism `P193` confirmed), the
information profile should be **monotonically increasing** toward the
boundary (z≈16.957), with the single most-informative point being the
one closest to it (within the safety margin) — not, e.g., peaking in
the middle of the window or near z=10.

## What this does NOT establish

1. Does not scan all the way to the P192-found boundary itself
   (z≈16.957) — stops at z=16.5, a margin chosen for safety (this file
   uses the analytic method, immune to P193's specific finite-
   difference perturbation instability, but H(z) itself still becomes
   numerically delicate very close to zero — see Positive control
   design below).
2. Does not establish that any of these z-values are realistically
   observable — same caveat carried from `P191`-`P193`.
3. **Correction, caught before this file's own script was written**:
   an earlier draft of this claim asserted "the top-N individually-best
   points ARE the best N-point combination" as a consequence of Fisher
   information's additivity. That is wrong. Additivity
   (`F_total = F_baseline + Σ F_i`, each `F_i` a rank-1 matrix from one
   point) is exact — but a GREEDY choice of individually-best points is
   not guaranteed optimal for a matrix-valued criterion: if several
   candidate points have similar `(dH/dx1, dH/dx2)` gradient directions
   (plausible for nearby z in a narrow, smoothly-varying window), their
   rank-1 contributions overlap and add LESS combined shrinkage than a
   set with more diverse directions would. This file reports the
   greedy top-N set's **actual, honestly-computed** combined shrinkage
   (via the same `analytic_fisher_matrix` summed over the real point
   list, not summed shrinkage numbers) as one reasonable, cheap
   candidate — not as a proven-optimal combination. A true
   combinatorial search over N-point subsets is not attempted here.
4. Does not resolve bottleneck 3 — `docs/134` remains untouched.
