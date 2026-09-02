# CLAIM P190 — is v82's own (β1,β2) degeneracy an EXACT parametrization
# redundancy, or an approximate, data-range-limited near-degeneracy?

**Date:** 2026-09-02
**Continues:** `FINDING_P176`'s own explicit open item — "Does not explain
WHY the slope is 6.073×10⁷ specifically." `FINDING_P175`/`P176` both
attempted a mechanistic explanation (P165's ε-absorption link) and both
retracted it as a category error. This file asks a DIFFERENT, narrower,
cheaper question than "why this value" — not the mechanism, but whether
the degeneracy is EXACT (a true redundancy in how (β1,β2) parametrize
v82's own H(z) construction — structurally unbreakable by any amount of
new data) or only APPROXIMATE (a numerically-strong but data-range-
specific near-flatness of TJB's own real 33-point χ² surface, in
principle breakable by different/wider z-coverage).
**Bottleneck:** touches #3 (Absolute scale / observable mapping,
`docs/147`) — `docs/147`'s own reopen bar for bottleneck 3 requires "a
genuinely new confound-breaking angle, not a repeat of this pattern"
(P182-P187 already exhausted real-dataset/real-literature confound-
breaking without resolving the β1-β2 physical-origin question). This is
that different angle: P176 only checked LOCAL numerical curvature
(Hessian) at 7 discrete fit points; it never checked whether the found
near-null DIRECTION is a symmetry of the FULL functional form, for all
z simultaneously, not just locally at one point.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive/structural (a mathematical-structure
question about TJB's own published construction, not a new physical
claim, not a claim about whether v82's theory is right or wrong)

---

## Zero-Signal Gate (falsification-ladder.md Step -5)

- **Entity:** TJB's own `H²(z; H0_anchor, β1, β2)` construction, verbatim
  from `archive/code/multing_core.py` (already reproduced in `P176`'s own
  script, positive-controlled against his own reported χ²₃₃ values).
- **Falsifiable predicate:** the coefficient functions of β1 and β2 in
  `H²(z)`'s affine dependence on `(β1,β2)` — call them `E1(z)`, `E2(z)` —
  are proportional to each other for ALL z (`E1(z)/E2(z) = const`,
  i.e. an exact symmetry direction exists), OR they are not (the ratio
  genuinely varies with z).
- **Measurable outcome:** symbolic (sympy) simplification of `E1(z)/E2(z)`
  and/or its numerical evaluation at several z spanning TJB's own 33-point
  dataset range (z=0.07 to z=2.33) — either it collapses to a single
  number (exact symmetry, `[VERIFIED]` either way once computed) or it
  visibly varies (approximate degeneracy).

All three present → gate passes, not `REFUSE`.

## Why this is well-posed and cheap

`forces(z, b1, b2)` (P176's own verbatim copy of TJB's `multing_core.py`)
is **linear** in `(b1, b2)` at every fixed `z`:
```
F1(z, b1) = b1 * (-G) * 2*M(z) * (k(z)/c^2) * (R(z)/d(z)) / d(z)^2
F2(z, b2) = b2 * (-G) * (k(z)/c^2)^2 * (R(z)^2/d(z)^2) / d(z)^2
```
`addot_over_a(z,b1,b2) = (F0(z) - F1(z,b1) + F2(z,b2) - F_acc(z)) / (M(z)/2) / d(z)`
is therefore AFFINE in `(b1,b2)` at each z, and `H²(z)` — built by a
LINEAR operation (cumulative trapezoid integration) applied to
`addot_over_a(z)/(1+z)` — is therefore also affine in `(b1,b2)` at each
fixed z, with z-dependent coefficients:
```
H²(z; H0_anchor, b1, b2) = [H0_anchor-and-b-independent part](z)
                             + b1 * E1(z) + b2 * E2(z)
```
An EXACT degeneracy direction `(Δb1, Δb2)` — one that leaves H²(z)
identically unchanged for every z, not just locally at one fit point —
exists **if and only if** `E1(z)/E2(z)` is the same number for every z.
This is a closed-form symbolic question, not a numerical-optimization
one — cheap to check directly from TJB's own `M(z), R(z), k(z), d(z)`
formulas (all explicit, already verbatim-reproduced in this campaign).

## What each outcome would mean

| Outcome | Meaning for bottleneck 3 |
|---|---|
| `E1(z)/E2(z) = const` for all z (exact) | The (β1,β2) degeneracy is a genuine, structural redundancy in how TJB's own construction parametrizes physical predictions — NOT a fluke of the specific 33-point dataset. No amount of new/different H(z) data could ever break it. This would be a strong, precise, NEW structural result: "absolute scale is structurally non-identifiable from H(z) data alone, by construction" — stronger and more specific than P133's formal rank-deficiency result (which was for THIS project's own (A,g,κ), not v82's own real (β1,β2)). |
| `E1(z)/E2(z)` varies with z (approximate) | P176's found near-flat direction is a strong but data-range-specific near-degeneracy — informative about how ill-conditioned TJB's ACTUAL 33-point compilation is, but NOT proof the degeneracy is unbreakable in principle. Different/wider z-coverage (e.g. more high-z anchors) could in principle constrain (β1,β2) independently — though `docs/147`'s own note that P182-P187 already tried real-data confound-breaking without success tempers how actionable this would be right now. |

## Cheapest differentiating test (per CDT Protocol)

Build `E1(z)`, `E2(z)` symbolically (sympy) from TJB's own verbatim
`M_of`, `R_of`, `k_of`, `d_of` (already reproduced in `P176`'s script —
copy, do not re-derive), simplify `E1(z)/E2(z)`, and:
- **Positive control**: numerically cross-check the symbolic `E1(z)`,
  `E2(z)` against a finite-difference `∂H²(z)/∂b1`, `∂H²(z)/∂b2` computed
  from P176's own (already positive-controlled) numeric `H2_of_z`
  function, at 2-3 z values — confirms the symbolic translation is
  faithful before trusting anything derived from it.
- **Main check**: is `E1(z)/E2(z)` symbolically constant? If sympy can't
  simplify it to a literal constant, evaluate numerically at ≥5 z values
  spanning the real dataset range (z=0.07, 0.5, 1.0, 1.965, 2.33) — if
  the ratio visibly changes, that alone falsifies "exact symmetry"
  without needing a full symbolic proof.
- **Cross-check against P176**: does the LOCAL ratio `E1(z)/E2(z)`
  evaluated near the data-weighted "center" of the 33-point compilation
  land in the same ballpark as P176's own found slope (6.073×10⁷,
  inverted/rescaled appropriately for units)? This is not expected to
  match exactly (P176's slope is a χ²-weighted average over ALL 33
  points with their own uncertainties, not a single-z ratio) — but wild
  disagreement would flag a translation error.

## What this does NOT establish

1. Does not explain WHY `E1(z)/E2(z)` has whatever value/behavior it
   turns out to have — only whether it is constant or not.
2. Does not resolve whether v82's own theory is correct (`NO_AUTHOR_ERROR`)
   — this evaluates the mathematical structure of the published
   construction only.
3. Does not, even in the "exact" outcome, prove no OTHER observable
   (beyond H(z) alone) could break the degeneracy — only that H(z) data
   alone, at any z-coverage, cannot.
4. Does not repeat P182-P187's real-data/real-literature confound-
   breaking attempts — this is a purely structural/symbolic question
   about the construction's own functional form.
