# PRE-REGISTRATION — v82's own quantities, frozen as prospective tests

**Frozen:** 2026-09-07. **Git commit at freeze:** see `git log` for the
commit that added this file — that hash is the timestamp of record.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR
**L0 (EstimandOps):** **predictive** — what future, currently
non-existent measurements will show. Not causal: nothing here claims
MULTING's mechanism is the cause of any agreement or disagreement.

## Why this file exists

`FINDING_E21` established that v82's archive contains 2-3 quantities
that are **checkable against future data but were computed after the
fit**. Their epistemic weight is therefore low: anything found after
the data cannot be a prediction about it.

That status is fixable, and only one way: **freeze them now, before the
data exists.** From this file's commit forward, these are prospective
out-of-sample tests. This does not retroactively make them predictions
— it makes them predictions *from today*.

**Honest statement of what this is and is not:**
- It **is** a dated, public commitment to numbers and pass/fail
  thresholds, made before the relevant measurements exist.
- It is **not** a claim that these were predicted in advance of the
  33-point fit. They were not. Every number below is a consequence of a
  fit already performed against data already in hand.
- It is **not** a claim that agreement would validate MULTING's
  mechanism. See "What a pass would and would not mean".

## Frozen model state

All numbers below follow from v82's **spotlighted** Table II row, whose
fit this project independently re-optimized and reproduced to better
than 0.1% (`FINDING_E18`): `β₁=1.433479e+10`, `β₂=7.806760e+17`,
`H0,anchor=73.2160`, `χ²₃₃=15.7515`. Any change to these parameters
voids the predictions below and requires a new pre-registration.

**Empirical-support boundary, stated up front:** the fit's own
highest-redshift point is `z=2.33` (DESI Ly-α). Some load-bearing
cluster inputs are supported only to `z≈1.07`; the CC fit to `z≈1.965`.
Everything below at `z>2.33` is therefore an **extrapolation test**,
not a clean mechanism test — flagged per prediction, not buried here.

## The predictions

### P-1 — deceleration parameter today

| | |
|---|---|
| **Quantity** | `q(0)`, the present-day deceleration parameter |
| **v82's value** | `q(0) = −1.416` |
| **Test against** | any future *independent* reconstruction of the low-redshift expansion history (SNe, BAO) not using the 33 points of this fit |
| **PASS** | independent `q(0)` within `±0.10` of `−1.416` |
| **FAIL** | independent `q(0)` outside `±0.25`, with quoted uncertainty smaller than that gap |
| **INCONCLUSIVE** | the independent measurement's own `1σ` exceeds `0.25` |
| **Extrapolation?** | **No** — `z→0` is inside the data's coverage. This is the cleanest of the three. |
| **Discriminating?** | **Weak.** `q(0)≈−1.4` is not unique to MULTING; ΛCDM-like models with fitted `H₀,Ωm` land nearby. A pass is consistency, not confirmation. |

### P-2 — divergence from ΛCDM at moderate redshift

| | |
|---|---|
| **Quantity** | fractional `H(z)` divergence from fixed-ΛCDM |
| **v82's values** | `10%` at `z=3.09`; `20%` at `z=3.95` |
| **Test against** | DESI / Euclid `H(z)` at those redshifts |
| **PASS** | measured divergence within `±5` percentage points of the stated value at the stated redshift |
| **FAIL** | measured divergence differs by `>10` percentage points with quoted uncertainty smaller than that |
| **Extrapolation?** | **Yes, both** — beyond the fit's own highest point (`z=2.33`). A FAIL here is evidence against the extrapolation, and only weakly against the mechanism. |
| **Discriminating?** | **Moderate** — a 10-20% deviation at `z≈3-4` is a real, non-generic signature. |

### P-3 — the low-z minimum of H(z)

| | |
|---|---|
| **Quantity** | position and depth of the `H(z)` minimum |
| **This project's reconstruction** | `z_min = 0.0988`, dip `= 1.4895` km/s/Mpc below `H(today)` |
| **Test against** | any future low-z `H(z)` compilation with per-point `σ < 0.5` km/s/Mpc near `z≈0.1` |
| **PASS** | a minimum resolved at `z = 0.099 ± 0.03` |
| **FAIL** | `H(z)` monotonic over `0 < z < 0.3` at `>3σ` |
| **INCONCLUSIVE (expected)** | current data: the dip is **8-13× smaller** than the quoted `1σ` at the two nearest real CC points. Today this is untestable. |
| **Known open discrepancy** | this project gets `z_min≈0.099`; TJB's own separately-commissioned session got `≈0.086`. **Unresolved, recorded before the fact** — a future measurement landing between them will not discriminate. |
| **Discriminating?** | **Weak** — not a unique MULTING fingerprint. |

## What a pass would and would not mean

**Would mean:** the frozen parameter set survived contact with data it
was not fitted to. That is a real, non-trivial thing, and it is the
thing this file exists to make possible.

**Would NOT mean:**
1. that MULTING's *mechanism* is right — `FINDING_P167` showed a
   physics-free quadratic-in-z model fits the same 33 points slightly
   better at equal parameter count (`Δχ²≈−1.7`). Good fit has low
   discriminating value; so does good extrapolation from a good fit.
2. that MULTING beats ΛCDM — on the two comparisons v82 itself calls
   fairest, `ΔAIC≈+1.2` to `+1.4` and `ΔBIC≈+2.7` to `+2.9` favour the
   benchmark (`FINDING_P166`).
3. that the parameters are identified — `FINDING_P133` proves
   `rank(J)=2<3` for `(A,g,κ)`: the current observable set cannot
   determine them independently. A pass constrains the *curve*, not the
   *parameters*.

**A FAIL on P-1 is the most informative single outcome available**,
because P-1 alone is not an extrapolation.

## Amendment rule

This file may be **added to** but not silently edited. Any change to a
frozen number, threshold, or the parameter set voids that prediction
and must be recorded as a new dated section stating what changed and
why — never by rewriting the original. Same discipline as
`null_results/`.
