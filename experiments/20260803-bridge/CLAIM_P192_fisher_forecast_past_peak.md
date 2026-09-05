# CLAIM P192 — does a Fisher-forecast at synthetic z PAST the level-set
# slope's own peak (found in P191) outperform P191's own z∈{3,5,7,10}?

**Correction (2026-09-05, discovered running the test this claim
specifies, before the main comparison could execute):** the requested
z∈{20,30,50} turned out to sit past a real boundary — TJB's own real
fitted (β1,β2) make `H²(z)` go negative (mathematically undefined) at
z≈16.96, so "the fiducial model's own prediction" a synthetic point
must be pinned to does not exist at any of the three requested z. This
does not falsify the claim below or the pearl it continues — it
surfaces a **prior, more basic constraint** (a physical-domain boundary)
the pearl's own choice of z-values needed to check first and didn't.
Full result: `FINDING_P192_fisher_forecast_past_peak.md`. The estimand,
MCID, and method below remain the pre-registered record of what was
*intended* to be tested — kept unedited per this project's own
no-silent-correction discipline.

**Date:** 2026-09-05
**Continues:** `FINDING_P191` directly — same estimand, same MCID, same
Floor-Ceiling framework, same machinery (already positive-controlled and
skeptic-confirmed twice there). **Minimal Relaxation Rule** (one
assumption changed, no bundling): the ONLY change from `CLAIM_P191` is
the synthetic-z set, `{3,5,7,10} → {20,30,50}`, chosen because `P191`'s
own Step 1 diagnostic found the level-set slope `-E1(z)/E2(z)` peaks
near z≈3 and *declines* thereafter — z∈{20,30,50} sit well past that
peak, where the slope diverges furthest from the real dataset's
χ²-weighted value (6.073×10⁷): 5.47×10⁷ at z=20, 5.03×10⁷ at z=50 (both
already computed in `P191`'s own diagnostic table; z=30 not yet
evaluated but expected between them by monotonicity of the decline).
**Authorization:** explicit user go-ahead, 2026-09-05 ("запусти второй
Fisher-forecast на z∈{20,30,50}").
**Bottleneck:** #3, same as `P191`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (same classification as `P191`,
unchanged by this variant).

## What is inherited unchanged from `CLAIM_P191` (not restated in full)

EstimandOps L0 gate (descriptive), population/comparator/endpoint/
summary-measure definitions, MCID (≥10% Δχ²=1 semi-axis shrinkage OR
≥5° near-null-eigenvector rotation), ICE (N/A), "what this does NOT
mean" items 1-4, and the Floor-Ceiling decision rule (ceiling≈100% is
expected and non-discriminating for essentially any well-separated
z-set, per `P191`'s own §2 caveat — the realistic-σ sweep is where the
real information is).

## The one thing being tested here that `P191` could not test

`P191`'s own Pearl Registry entry (2026-09-05, `next_check` 2026-12-01)
made this the named falsifiable prediction: *"IF a second Fisher-
forecast attempt uses synthetic z-values PAST the z≈3 peak... THEN the
realistic-sigma shrinkage should differ measurably from P191's own
result, since those level-set slopes diverge further from the
baseline's chi-squared-weighted slope."* This file runs that test.

**Falsifiable predicate:** at matched σ_synth (1%, 3%, 10%), does
z∈{20,30,50} give **larger** semi-axis shrinkage than `P191`'s own
z∈{3,5,7,10} results (73.0%, 45.6%, 13.6%)? A "no" (shrinkage the same
or smaller) would falsify the pearl's own prediction that slope-distance
from baseline drives discriminating power — a genuinely informative
negative result either way, not just a confirmation exercise.

## Method

Same script pattern as `P191` (self-contained, verbatim TJB physics
functions, deliberately uncentralized per this lineage's own
convention) — `P192_fisher_forecast_past_peak.py` — with `synth_zs =
[20.0, 30.0, 50.0]` in place of `P191`'s `[3.0, 5.0, 7.0, 10.0]`. All of
`P191`'s positive controls (baseline χ²/Hessian reproduction, floor
reduces-to-baseline, synthetic-fiducial-values-are-physical, 4-point
step-size convergence plateau incl. the ceiling σ) are re-run
parameterized on the NEW z-set, not assumed to still hold — the
convergence behavior at these much higher z (larger integration range,
different curvature scale) is not guaranteed to be identical to
`P191`'s own z∈{3,5,7,10} convergence properties.

## What this does NOT establish (in addition to `CLAIM_P191`'s own list)

1. Does not test whether 3 points (vs `P191`'s 4) changes anything by
   itself — the z-values differ AND the count differs; this is a
   compound change from `P191`'s framing (population/count of points)
   as well as location, acknowledged rather than hidden.
2. Does not identify z∈{20,30,50} as realistically observable H(z)
   redshifts by any current or near-term technique — cosmic
   chronometers and BAO become impractical well before z=20; this
   remains a mathematical forecast exercise, same caveat `P191` already
   carries, now more acute given how far outside any real survey's
   reach these z-values are.
