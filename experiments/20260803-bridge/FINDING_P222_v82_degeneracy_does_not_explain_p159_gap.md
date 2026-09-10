# FINDING P222 — v82's real (β1,β2) degeneracy (P176) does NOT explain
# the 19.5× gap between v82's own fit and this project's derived ratio (P159)

**Date:** 2026-09-10
**Labels:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive`
**Script:** `P222_v82_degeneracy_vs_p159_gap.py` — reuses `P176_v82_real_chi2_
hessian_degeneracy.py`'s own `hessian_null_slope()` and `TABLE_II` directly
(not re-typed numbers).

**Continues:** `FINDING_P161` explicitly named this exact question as
untouched — *"Does not connect to `FINDING_P159`'s own ratio finding beyond
confirming v82's own fitted point is not... arbitrary — says nothing new
about the 19.5× ratio discrepancy itself."* `FINDING_P176` then measured
the real (not idealized-local) degeneracy and its precise slope, but
likewise never connected it back to `P159`'s own gap. This file closes
that gap explicitly, arising from an independent same-day cross-check
(a parallel session's audit flagged the question was open on disk).

## Method

**Positive control, run first:** `P176`'s own `test_hessian_slope_converges_
with_step_size` re-imported and re-executed — `[VERIFIED-REAL]`, slopes at
`h=1e-3,1e-4,1e-5` agree to <0.01%.

At the spotlighted row (`H0_anchor=73.22`, `β1_fit=1.4335e10`,
`β2_fit=7.8067e17`): computed the real Hessian eigenvalues/null-eigenvector
slope fresh (not cached), then the formal `Δχ²=1` extent along the flat
direction (`Δx = √(2/λ_small)`), then evaluated the ratio `√β2/β1` at
±1σ along that direction.

## Result

```
eigenvalues            = [70.597, 588321]   (condition number ~8334)
null-eigenvector slope  = 6.073104e+07
formal 1-sigma extent   = 0.1683  (16.8% of beta1)

ratio at fit point                    = 0.061636
this project's own derived ratio      = 1.224700   (sqrt(6)/2, FINDING_P1/P159)
P159's own stated discrepancy factor  = 19.87x

+1 sigma: ratio=0.057495  factor=21.30x  (ratio moved x0.93 from fit point)
-1 sigma: ratio=0.066794  factor=18.34x  (ratio moved x1.08 from fit point)
```

## Verdict

**The real, measured degeneracy moves the ratio `√β2/β1` by <10% along its
own formal 1σ extent — nowhere near enough to account for the 19.5× gap.**
`FINDING_P159`'s discrepancy is **not an artifact of v82's own `(β1,β2)`
being underdetermined** — it remains a real, unexplained mismatch between
this project's theory-derived ratio (`√6/2`) and v82's own independently-fit
value.

This closes one of the three candidate explanations `FINDING_P159` §5 left
open (a fit-degeneracy origin for the gap) — the other two remain
untested:
1. The real physical mechanism sourcing MULTING's dipole/quadrupole terms
   may not be the mirror-symmetric two-point-charge picture this project's
   own construction assumes.
2. `κ_A ≠ κ_P` asymmetry / angular averaging (`FINDING_P160`) — not checked
   here.

## What this does NOT establish

- Not a claim about v82's own theory being wrong (`NO_AUTHOR_ERROR`) — only
  that this specific candidate explanation for the gap (fit degeneracy) is
  ruled out, quantitatively, at the spotlighted row.
- Only checked at the spotlighted row's own formal 1σ extent along the
  *flat* direction — a global, non-local search of the full `(β1,β2)`
  plane (e.g. a real MCMC posterior) was not attempted and could in
  principle behave differently far from the fit point, though the
  Hessian's own condition number (~8334) makes a 19× excursion at fixed
  `Δχ²=1` implausible by construction.
- Does not address the two named-but-untested alternatives above.

`REGRESSION/TESTS: ruff clean; positive control (P176's own step-size test) re-run and passed.`
