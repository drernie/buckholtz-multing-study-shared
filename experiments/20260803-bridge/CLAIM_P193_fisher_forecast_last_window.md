# CLAIM P193 — does a Fisher-forecast at synthetic z∈{12,14,16} (the
# last well-defined window before P192's found boundary) outperform
# P191's own z∈{3,5,7,10}?

**Result (2026-09-05, added after the test ran):** CONFIRMED —
z∈{12,14,16} gives up to 5.4× more shrinkage than P191's z∈{3,5,7,10}
at matched precision. The test as pre-registered below could be
answered as intended; unlike `CLAIM_P192`, no domain-of-validity
correction was needed here (that is precisely why this z-set was
chosen). A real, separate methodological finding surfaced along the
way: the standard finite-difference Hessian method does not converge
at σ_synth∈{1%,3%} this close to `P192`'s found boundary, resolved with
an independent analytic Fisher matrix. Full result, two rounds of
Step 8a skeptic review, and the numerical-method finding:
`FINDING_P193_fisher_forecast_last_window.md`.

**Date:** 2026-09-05
**Continues:** `FINDING_P191` (estimand, MCID, Floor-Ceiling framework,
machinery) and `FINDING_P192` directly (the found domain-of-validity
boundary: TJB's own real fitted `(β1,β2)` make `H²(z)` go negative at
z≈16.957). **Minimal Relaxation Rule**: the ONLY change from
`CLAIM_P191`/`CLAIM_P192` is the synthetic-z set,
`{3,5,7,10} → {20,30,50} → {12,14,16}`, this time chosen to sit inside
the domain of validity `P192` established, in the last remaining window
between `P191`'s own z≤10 and the found boundary.
**Authorization:** explicit user go-ahead, 2026-09-05 ("запусти третий
Fisher-forecast на z∈{12,14,16}").
**Bottleneck:** #3, same as `P191`/`P192`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (unchanged from `P191`/`P192`).

## What is inherited unchanged from `CLAIM_P191` (not restated in full)

EstimandOps L0 gate (descriptive), population/comparator/endpoint/
summary-measure definitions, MCID (≥10% Δχ²=1 semi-axis shrinkage OR
≥5° near-null-eigenvector rotation), ICE (N/A), "what this does NOT
mean" items 1-4, Floor-Ceiling decision rule.

## New pre-check specific to this z-choice (per `P192`'s own finding)

Before trusting any Hessian computed at z∈{12,14,16}, verify the
domain-of-validity margin holds not just at the fiducial `(β1,β2)` but
at every finite-difference perturbation the Hessian's own numerical
scheme actually evaluates — `P192` showed the boundary itself
(z≈16.957) is close enough to z=16 (≈5.7% margin) that this needs
checking, not assuming. **Already checked in a pre-flight probe before
writing this file's script** (not deferred to a positive control found
by a failing test, learning from `P192`'s own two caught bugs): at
h∈{1e-4,1e-5,1e-6}, all 8 finite-difference corners
`(x1,x2)∈{1±h}×{1±h}` keep `H²(z=16)>0`, and the perturbed boundary
itself stays at z≈16.956-16.957 — stable, not shifting meaningfully
under these perturbations. This check is formalized as a positive
control in the script itself, not left as an informal pre-flight-only
fact.

## Falsifiable predicate (same shape as P192's, now testable)

At matched σ_synth (1%, 3%, 10%), does z∈{12,14,16} give **larger**
semi-axis shrinkage than `P191`'s own z∈{3,5,7,10} (73.0%, 45.6%,
13.6%)? Per `P191`'s own diagnostic table, the level-set slope at
z=10-16 continues declining (5.79×10⁷ at z=10, falling toward and past
the z=20 value of 5.47×10⁷) — further from the real dataset's
χ²-weighted slope (6.073×10⁷) than any of `P191`'s own z-choices — so
the pearl's own mechanism (slope-distance drives discriminating power)
predicts yes, if it is correct.

## What this does NOT establish (in addition to `CLAIM_P191`'s own list)

1. Does not establish z∈{12,14,16} as realistically observable H(z)
   redshifts by any current technique — same caveat as `P191`/`P192`,
   this remains a mathematical forecast exercise.
2. Does not, even if the MCID is met here, mean the *entire* window
   (10,17) is uniformly informative — only that these 3 specific points
   are.
