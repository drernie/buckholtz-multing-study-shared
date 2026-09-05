# CLAIM P195 — floor-sensitivity sweep for `FINDING_P158_ADDENDUM2`'s
# grounded ρ result: does the arbitrary population-floor choice
# (`M_of(z)/2`) drive the `ρ>0` conclusion, or does it survive nearby
# alternatives?

**Date:** 2026-09-05
**Continues:** `FINDING_P158` (Jensen's-inequality mechanism,
`CONDITIONAL-DIRECTIONAL-PREDICTION`, threshold `ρ>−0.5`),
`FINDING_P158_ADDENDUM2` (real, computed `ρ` for `z≤0.5`, its own
`Objection 2` named as an accepted, unaddressed limitation: "the
`M_of(z)/2` choice is untested against nearby alternatives — a real,
named, unaddressed gap"), `docs/156` (this session's precondition
check, §5, naming this exact sweep as the cheapest, best-scoped next
step).
**Authorization:** explicit user go-ahead, 2026-09-05 ("начни
финитно-r/single-pair расчёт по docs/153 итд автономно"), reinterpreted
per `docs/156`'s own verdict into the mechanically-correct, already-
tractable continuation of that instruction (the literal finite-r S-S
closure `docs/153` names is independently blocked — `docs/156` §1-4).
**Bottleneck:** #1 (F→H_MULT(z)), specifically the causal-compatibility
sub-question `docs/153` restated — same as `P156`-`P158`.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (unchanged from `P158`/`ADDENDUM2`) ·
`Minimal Relaxation Rule`: exactly ONE assumption changed from
`ADDENDUM2` (the population floor), everything else (mass function,
bias formula, correlation-function integral, redshift set) held fixed.

## What is inherited unchanged from `FINDING_P158_ADDENDUM2`

The entire pipeline: `hmf`/Tinker08 mass function, Tinker et al. (2010)
Eq. 6 bias (coefficients verified against the primary source),
Fourier-Bessel `ξ_mm(r)` integral, the exact (non-perturbative)
pairwise-correlation formula (`pair_rho_exact`), the `NU_CALIBRATION_
CEILING=10` cutoff, and the restriction to `z≤0.5` (the 4 of 8
redshifts already inside Tinker et al.'s own calibrated `ν` range —
`z≥1.07`'s own trustworthiness question is untouched by this file,
per `ADDENDUM2`'s own scope).

## New estimand element specific to this file

**Population of candidate floors**: `M ≥ M_of(z)/f` for
`f ∈ {4, 2 (ADDENDUM2's own baseline), 1}` — i.e. quarter-, half-, and
full-characteristic-mass floors — plus one qualitatively different
construction, a **bounded bin** `M_of(z)/2 ≤ M < 2·M_of(z)` (testing
whether an unbounded-above floor vs. a bounded window around the
characteristic mass changes the answer, not just the floor's exact
multiplier).

**Endpoint**: `ρ(z, floor)` at each of the 4 already-trusted redshifts
(`z=0, 0.0233, 0.07, 0.5`), computed by `ADDENDUM2`'s own exact formula,
for each floor choice above.

**Falsifiable predicate**: `FINDING_P158`'s directional claim requires
`ρ>−0.5`. `ADDENDUM2`'s baseline values (`+0.00045` to `+0.01007`) sit
50-500× away from that threshold in raw terms — if the floor-sensitivity
sweep shows `ρ` moving by less than, say, a factor of a few across
plausible floor choices, the `ρ>−0.5` conclusion is robust to this
particular analyst choice. If `ρ` changes sign or approaches the
threshold under any of the tested alternatives, `ADDENDUM2`'s own
"safely above threshold" framing needs walking back.

**MCID (pre-registered before running)**: a floor-choice-induced change
counts as material if it (a) flips `ρ`'s sign at any of the 4 tested
redshifts, or (b) moves `ρ` by more than `0.05` in absolute terms (10%
of the distance from `ρ=0` to the `ρ=−0.5` decision threshold) at any
tested redshift. Below both thresholds, the result is reported as
ROBUST; at or above either, WEAKENED, with the exact numbers shown
rather than a bare verdict.

## Positive control (specific to this file)

At `f=2` (the exact baseline), this file's own computation must
reproduce `FINDING_P158_ADDENDUM2`'s own tabulated `ρ` values for
`z∈{0, 0.0233, 0.07, 0.5}` to high precision — a regression check that
this file's refactored/parameterized floor logic has not silently
changed the already-verified baseline calculation.

## What this does NOT establish

1. Does not touch the `z≥1.07` range — `ADDENDUM2`'s own finding that
   those 4 redshifts are extrapolated past Tinker et al.'s calibration
   is untouched; a floor-sensitivity check on an already-untrustworthy
   `ν` regime would not be informative.
2. Does not attempt the nonlinear-bias or N-body work `ADDENDUM2` named
   as required to extend trustworthy coverage to `z≥1.07` — out of
   scope, a materially larger undertaking per `docs/156` §3.
3. Does not re-derive or re-verify the mass function, bias formula, or
   correlation-function integral themselves — those are reused verbatim
   from `ADDENDUM2`, already independently verified there.
4. Does not resolve `docs/153`'s literal "finite-r/single-pair
   calculation" (comparing two routes' intermediate quantity) —
   `docs/156` §1-4 already established that specific test is not
   currently buildable; this file continues the different, mechanically
   -correct line of work instead.
5. Does not resolve bottleneck 1 as a whole (`docs/147`'s F→H_MULT(z)
   entry) — scoped entirely to strengthening or weakening one specific,
   already-narrow sub-result (`ADDENDUM2`'s `z≤0.5` grounded `ρ`).
