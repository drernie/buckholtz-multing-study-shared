# FINDING P176 — the decisive test: does v82's own REAL chi-squared
# surface (not an idealized local expansion) show a genuine
# beta1-beta2 degeneracy at fixed H0,anchor, and does it explain
# Table II's own real fit behavior?

**Date:** 2026-08-31
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (numeric evaluation of TJB's own
published fit against his own real data — not a new physics claim)
**Continues/answers:** `FINDING_P175`'s own named "real decisive test"
(item 3 of "what this file does NOT establish") — the true P133-analogue,
using TJB's own real optimizer/data instead of an idealized local Taylor
expansion.
**Script:** `P176_v82_real_chi2_hessian_degeneracy.py` (numpy, 5 tests
incl. 2 positive controls, ruff clean, 881/881 project tests still pass).
**Data/code source:** TJB's own supplemental Zenodo archive (same as
`P169`/`P175`) — `archive/code/multing_core.py` + `generate_all_results.py`
(chi-squared function) + `assumptions.yaml` (31-point cosmic-chronometer
data, Table II). Reproduced verbatim.
**Status tags (per `docs/151_status_separation_rule.md`):**
> **Empirical/Model status:** SUPPORTED for the core finding (a real,
> robust, H0,anchor-independent β1-β2 degeneracy exists in v82's own
> fit) — positive-controlled, step-size-converged, grid-density-
> converged, skeptic-reviewed with corrections applied. WEAKENED for the
> original "surprising coincidence" framing (retracted — see Correction).
> **Ontological/mechanistic interpretation status:** OPEN — this file
> establishes the degeneracy's existence and slope precisely; it does
> not explain WHY the slope has this specific value, and an attempted
> explanatory link to `FINDING_P165`'s idealized-local mechanism is
> explicitly not established (see Correction).
> **Causal/cosmological claim status:** N/A.

## Correction (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing)

A skeptic review of this file's first draft found two real problems
(full details in the script's own docstring, not repeated verbatim
here) — both accepted after independent numerical re-checking, not
taken on the skeptic's word alone:

1. **Overclaimed "coincidence" (Conclusion 2 of the first draft).** The
   first draft treated the close match (1.4%) between the pure fixed-
   `H0,anchor` null-eigenvector slope and the empirical Table-II-scan
   slope as a striking, independently-discovered structural fact.
   **The skeptic is right that this is largely expected**: via the
   implicit function theorem, `d(β)/d(H0,anchor) = -H_ββ⁻¹ · ∂²χ²/∂β∂H0,anchor`
   — whenever `H_ββ` is strongly ill-conditioned (as it is here,
   condition number ~8300), the result is generically dominated by the
   soft eigenvector unless the cross-derivative happens to align almost
   exactly with the stiff one. Close alignment is close to the default
   outcome of a strong degeneracy, not new evidence for one.
   **Independently re-derived the rigorous version** (the full
   implicit-function-theorem prediction, including the actual cross-
   derivative, not just the pure null eigenvector — `test_ift_
   prediction_matches_empirical_scan_tighter_than_pure_null`): the
   properly-computed prediction matches the empirical scan slope to
   **0.02%**, tighter than the naive comparison (1.4%), and the small
   residual is consistent with ordinary Nelder-Mead optimizer tolerance
   (independently re-verified: re-optimizing the spotlighted row from a
   fresh starting guess with TJB's own tolerance settings converges to
   `β1,β2` within 0.01–0.02% of his reported Table II values). Net: the
   real degeneracy (Conclusion 1) survives and is now MORE precisely
   characterized; the "surprising coincidence" framing does not survive
   and is retracted.
2. **Category error (Conclusion 3 of the first draft).** The first draft
   attributed the ~2.3× gap between `FINDING_P175`'s idealized-local
   prediction (`C=2.644×10⁷`) and this file's real Hessian slope
   (`6.073×10⁷`) to "Taylor-expansion order" — a specific causal claim
   this file has no evidence for. **Retracted as a category error**: `C`
   characterizes a single local kinematic derivative at `z=0`; the real
   Hessian slope characterizes an eigenvector of a `χ²` surface
   integrated over all 33 data points spanning `z=0.02` to `z=2.33` —
   different objects, not the same object at different orders of
   approximation. **Attempted the skeptic's own proposed kill test**
   (recompute the null direction using ONLY the near-`z=0` SH0ES term) —
   it turned out **ill-posed**: that single point's `χ²` has essentially
   zero curvature in `(β1,β2)` *by construction*, because SH0ES's
   redshift (`z=0.0233`) is used as the anchor reference point `zref`
   that `H0,anchor` is itself defined against — so the comparison the
   kill test was meant to make is genuinely unresolved, not resolved
   either way. Reported honestly as inconclusive.

**What survives, unretracted and now more rigorously established:**
- A real, robust, statistically meaningful `β1`-`β2` degeneracy exists
  in v82's own real `χ²` surface at any fixed `H0,anchor` (condition
  number ~8300–11000 depending on row; a formal `Δχ²=1` extent along the
  flat direction alone corresponds to a ~17% fractional shift in `β1`).
- This degeneracy's slope is **H0,anchor-independent to <0.1%** across
  the entire real Table II range (67.40–73.22 km/s/Mpc) — a genuine
  structural property of the fit, not an artifact of one operating
  point.
- Both results are numerically solid: converged to <0.01% across 2
  orders of magnitude in finite-difference step size, AND across 2
  orders of magnitude in the internal numerical-integration grid density
  (500→4000 points) — ruling out both classes of numerical artifact the
  skeptic named.
- The rigorous (not naively-simplified) implicit-function-theorem
  prediction for how `(β1,β2)` should move as `H0,anchor` is scanned
  matches TJB's own real, reported Table II numbers to **0.02%** —
  consistent with his own optimizer's own tolerance, i.e. this file's
  own Hessian genuinely describes the same surface his own fit explored.

## 0. Premise — `NO_AUTHOR_ERROR`

Every function, constant, and data point here is TJB's own, reproduced
verbatim from his own supplemental code and published parameter tables —
this file evaluates the mathematical structure of his own real fit; it
does not evaluate whether his theory is correct.

## 1. Method

Reproduced TJB's own `chi2` function from `generate_all_results.py`'s
`fit_row()` (fixed-`H0,anchor` branch) verbatim: the same 33-point
dataset (31-point cosmic-chronometer compilation + SH0ES `z=0.0233` +
DESI DR2 `z=2.33`), the same fine-grid interpolation procedure, the same
`H_of_z_kms` call. **Positive control**: this function reproduces TJB's
own reported `χ²₃₃=15.75` (spotlighted row) and `χ²₃₃=47.77`
(`planck_exact_100pct` row) to <0.1%.

At each of TJB's own 7 Table II rows independently: computed the numeric
`2×2` Hessian of `χ²(β1,β2)` at his own reported best-fit point, in
rescaled coordinates (`x1=β1/β1,fit`, `x2=β2/β2,fit`, both `≈1` at the
fit point — raw `β1~10¹⁰`, `β2~10¹⁷` differ by 7 orders of magnitude,
making an unrescaled Hessian numerically meaningless). Diagonalized;
extracted the near-null eigenvector's slope.

## 2. Results

```
Spotlighted row (H0,anchor=73.22):
  eigenvalues = [70.60, 588321]   condition number = 8333.5
  real near-null slope d(beta2)/d(beta1) = 6.073104e+07

All 7 Table II rows (H0,anchor = 67.40 to 73.22 km/s/Mpc):
  slope ranges 6.0731e7 to 6.0740e7  (< 0.1% spread)

Step-size convergence (h = 1e-3, 1e-4, 1e-5): stable to < 0.01%
Grid-density convergence (npts = 500, 1000, 2000, 4000): stable to < 0.01%

Rigorous IFT-predicted H0,anchor-scan slope: 6.158364e+07
  (vs empirical Table-II-scan slope 6.157055e+07 -- error 0.02%)
  (vs pure null-eigenvector slope alone -- error 1.4%, the naive
   comparison the first draft used)

Independent re-optimization check (fresh starting guess, TJB's own
tolerance settings): converges to beta1,beta2 within 0.01-0.02% of his
reported Table II values.
```

## 3. Verdict

**A real, robust, `H0,anchor`-independent degeneracy exists in v82's
own real fit** between `β1` and `β2` — established directly from his
own chi-squared function and his own 33-point dataset, not from an
idealized local approximation. This is the genuine analogue of
`FINDING_P133`'s formal rank-deficiency result for `(A,g,κ)`, but for
v82's own real, published fit rather than this project's own
reconstruction.

**What this degeneracy is NOT shown to be**: a manifestation of
`FINDING_P165`'s hypothetical monopole-tier `ε`-absorption mechanism.
That connection was attempted twice (`FINDING_P175`'s Table-II-inversion,
retracted as a category error; this file's Taylor-order story, also
retracted) and neither survives. The degeneracy is real; its physical
origin (within v82's own construction) is not established here.

## What this file does NOT establish

1. **Not a claim about v82's own theory being wrong** (`NO_AUTHOR_ERROR`,
   §0) — a parameter degeneracy in a fit is a common, unremarkable
   feature of many multi-parameter models; this file establishes its
   existence and precise slope, nothing about whether it is a problem.
2. **Does not connect this degeneracy to `FINDING_P165`'s ε-absorption
   mechanism** — attempted, retracted twice (see Correction). The SH0ES-
   only kill test that might have settled this is ill-posed given how
   the anchor point is constructed; no other kill test was attempted.
3. **Does not establish the degeneracy's real-world statistical
   significance** — the condition number and formal `Δχ²=1` extent
   describe curvature of a point estimate; a rigorous confidence region
   would need TJB's own data covariance/systematics, not attempted here.
4. **Does not explain WHY the slope is `6.073×10⁷` specifically** — only
   that it is real, precise, and `H0,anchor`-independent.
5. **Does not re-run TJB's own full multi-start global optimization** —
   only local Hessian curvature at his own already-reported best-fit
   points, plus one independent local re-optimization check from a
   nearby starting guess (not a global search).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
