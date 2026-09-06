# CLAIM E8 — propagating the cosmic-chronometer covariance through this
# project's own χ² and degeneracy analysis

**Date:** 2026-09-06 (pre-registered BEFORE the script is run)
**Continues:** `FINDING_E5`, which named this as "the separate, unrun
computation." Executes option 2 of the second option set ("actually run
the full covariance through our own calculations"), explicit go-ahead.

## L0 (EstimandOps)

**Question type: descriptive.** How do (a) the χ² values and (b) the
`(β₁,β₂)` degeneracy structure this project already computed on the
33-point dataset (`P176`) change when the 31 cosmic-chronometer points
carry Moresco's own published covariance instead of diagonal errors?

## Falsifiable predicate

`FINDING_E5` established that the CC modelling systematic (mean
`~4.5-8.9%` of `H(z)`, fully correlated across bins) is absent from the
quoted `errHz`. **Prediction:** replacing the diagonal χ² with the
covariance-weighted `rᵀC⁻¹r` will (i) reduce every model's χ² (larger
total error), and (ii) reduce the **difference** in χ² between MULTING's
Table II rows and flat ΛCDM — i.e., shrink the dataset's discriminating
power between any two smooth `H(z)` models — because a fully-correlated
systematic mostly penalizes an overall normalization offset, which any
smooth model can absorb.

## Pre-registered MCID

- **Endpoint 1 — discriminating power.** `Δχ² ≡ χ²(ΛCDM) − χ²(MULTING
  spotlighted row)`. MATERIAL if `|Δχ²_cov − Δχ²_diag| > 2.0` (roughly
  the width of a 1σ two-parameter confidence step) OR if the SIGN of
  `Δχ²` flips.
- **Endpoint 2 — degeneracy.** `P176`'s small Hessian eigenvalue at the
  spotlighted row. MATERIAL if it changes by more than a factor of 2
  (the near-null direction's stiffness halves or doubles), OR the null
  slope `dβ₂/dβ₁` changes by > 20%.
- Anything below both thresholds → the E5 finding is real but does not
  change this project's own prior conclusions at the level they were
  stated.

## Method

1. Import `P176`'s own `chi2_fixed_h0anchor`, `H_of_z_kms`, data arrays,
   and `TABLE_II` (precedent: `P198` imports from `P196`).
2. Build the covariance **exactly per Moresco's own notebook**
   (`examples/CC_covariance.ipynb`, fetched this session):
   `C_CC = diag(σ²) + Σ_k outer(H·x_k, H·x_k)`, `x_k` = `data_MM20.dat`
   percentages interpolated to the data redshifts. **His default:**
   `k ∈ {spsooo, imf}`. **Stress variant:** `k ∈ {sps, imf}` (the larger
   estimate). Embed into 33×33 with SH0ES and DESI diagonal.
3. **Correlation-structure assumption, stated:** Moresco's recipe treats
   the modelling part as fully correlated across HIS points. 15 of TJB's
   31 CC points are Moresco's; 16 come from other groups using other SPS
   choices. Applying full correlation across all 31 is the
   **conservative** case (Moresco's own stance). Run both: (a) all 31
   correlated; (b) only Moresco's 15 correlated, others diagonal.
4. χ²_cov for every Table II row and for flat ΛCDM
   (`H₀=67.4, Ωₘ=0.315`, v82 §II.G).
5. `P176`'s Hessian eigen-decomposition with χ²_cov.

## Controls

- **Positive control 1:** with all modelling components zeroed, χ²_cov
  must equal `P176`'s diagonal χ² to `<1e-9` relative (regression: the
  covariance path reduces exactly to the diagonal path).
- **Positive control 2:** diagonal χ² must reproduce TJB's own Table II
  χ²₃₃ for ≥2 rows to `<0.1%` (inherited from `P176`, re-asserted).
- **Positive control 3:** `C` must be symmetric positive-definite
  (Cholesky succeeds) — Moresco's own README asserts invertibility.
- **Negative control:** a covariance with an absurdly large modelling
  fraction (100%) must drive all χ² toward the same small value —
  discriminating power → 0 — confirming the mechanism direction.

## Post-registration record (added AFTER the run; the sections above are
## unchanged)

- **Negative control premise was wrong** — see `FINDING_E8` "Corrections".
  A rank-1 fully-correlated term frees one direction only; the gap vs
  fixed ΛCDM lives in SH0ES, outside the CC block. Control tested the
  wrong lever. Not a code bug (PC3 held to `<1e-9`).
- **Two post-hoc scripts were added**, both labelled as such: `E8b`
  (re-optimise both models under the covariance, after a sign flip
  appeared) and `E8c` (the skeptic's kill test: restrict to Moresco's
  own 15 points). Neither was foreseen here.
- **Endpoint 1's sign-flip criterion fired but was then demoted** by
  `E8c`: on Moresco's own points the sign does not flip. Recorded as
  WEAKENED, not deleted.

## What this claim does NOT say

- Nothing about whether any v82 conclusion is right or wrong. It is a
  statement about what the *data's own published error structure* does
  to model discrimination on this dataset — for every model equally.
- Does not derive the covariance; it applies Moresco's, verbatim.
- `NO_AUTHOR_ERROR`.
