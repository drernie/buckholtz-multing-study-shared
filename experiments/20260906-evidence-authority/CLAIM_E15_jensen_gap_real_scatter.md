# CLAIM E15 — quantify v82's own named, self-flagged, unquantified gap:
# does evaluating the force law at a "representative" thermal energy
# differ from population-averaging it, using `E13`'s real measured
# scatter?

**Date:** 2026-09-06 (pre-registered before any numeric result)
**Continues:** `FINDING_E13` (measured `σ_{M_gas|T}=0.49`, ln-normal,
never propagated by v82) and this project's own `FINDING_P157`/`P158`
(Jensen's-inequality tool for exactly this force law's own
nonlinearity, previously run only with an "illustrative, not real"
scatter assumption). Option 1 of the six continuation options, per the
user's own stated order ("всё по очереди").

## The gap, in v82's own words

`[VERIFIED-BASH]` v82.md:1060-1063, its own §IV limitations section:

> *"Typical objects, not distributions. Every quantity in Sec. II.D is
> a single, representative value at each redshift, not a scattered
> population of node properties. Because the force law is markedly
> nonlinear in these quantities, evaluating it at a representative
> value is not generally the same as averaging it over the
> distribution; **we have not attempted to quantify this difference.**"*

This is TJB's own, explicitly self-flagged, explicitly unquantified
open question. `E13` supplies exactly the missing ingredient: a real,
sourced scatter value for one of the "quantities in Sec. II.D"
(`M_gas,X(z)`, and through it `k_X(z)`).

## The mechanism, verified directly in the supplemental code

`[VERIFIED-CODE]` `multing_core.py:112-122`:

```
F1 = beta_1 * (-G) * 2.0 * M * (k/c^2) * (R/d) / d^2      # LINEAR in k
F2 = beta_2 * (-G) * (k/c^2)^2 * (R*R/d^2) / d^2          # QUADRATIC in k^2
```

`k = k_of(z)` is linear in `M_gas,X(z)` (`k_of(z) = 1.5*(Mgas_of(z)/
(mu_mol*m_proton))*(T_keV_of(z)*KEV_TO_J)`, `multing_core.py:89-91`),
so `k`'s own fractional/log scatter inherits `M_gas`'s scatter
directly, holding `T` fixed (isolating exactly the dependency `E13`
measured).

**This is the identical structural setup `FINDING_P157` already
identified in general** (a linear force term vs. a quadratic one), and
`FINDING_P158` already built the machinery for (sympy + Monte Carlo
Jensen's-gap calculation) — but `P158` explicitly flagged its own
scatter values as **"illustrative, not a claim about the real cluster
mass function."** `E13` now supplies a real one.

## Falsifiable predicate

For a log-normal `k = k_med · X`, `ln(X)~N(0,σ²)`, with the fitted
scaling-relation curve representing the **median** (standard for a
log-linear regression, `[INFERRED]` from the fitting form itself, not
independently verified against Ramos-Ceja's own convention statement —
flagged as an assumption, checked in the controls):

```
E[F1] / F1(k_med) = E[X]  = exp(σ²/2)        -- dipole correction
E[F2] / F2(k_med) = E[X²] = exp(2σ²)         -- quadrupole correction
```

**Prediction:** with `σ=0.49`, the quadrupole correction factor
(`exp(2·0.49²)`) is materially larger than the dipole correction factor
(`exp(0.49²/2)`) — population-averaging boosts `F2` relative to `F1`,
analogous in shape (though not derivation) to `P158`'s own conditional
finding, now on a real number.

## Pre-registered MCID

**MATERIAL** if the ratio of correction factors
(`exp(2σ²)/exp(σ²/2) = exp(1.5σ²)`) differs from `1` by more than
`10%` — i.e., if population-averaging would shift the *effective*
quadrupole-to-dipole weighting (`β₂F₂/β₁F₁`) by more than `10%` relative
to what a representative-value evaluation implies.

## Method

1. Symbolic/closed-form Jensen's-gap calculation (log-normal moments),
   cross-checked by Monte Carlo (`N≥10⁶`) sampling `k` directly —
   `P158`'s own dual-verification discipline, reused.
2. Apply at `z=z_piv=0.25` (where `E13`'s scatter is measured at its
   own pivot, avoiding an extrapolation confound) and, separately, at
   the actual data redshifts used in `P176`'s 33-point fit, to see if
   the correction is roughly `z`-independent (expected, since `σ` is a
   fixed calibration parameter, not itself `z`-dependent in the cited
   source) or not.
3. Report both the raw correction factors and their *ratio*, plus what
   fractional shift in `β₂/β₁` this would imply if the fit were redone
   using population-averaged `F1`, `F2` instead of point-evaluated ones
   — explicitly labelled as "what this WOULD imply," not a re-fit
   actually performed (a real re-fit is a further, separate step).

## Controls

- **Positive control 1:** `σ→0` must return correction factors of
  exactly `1` for both `F1` and `F2` (no scatter, no gap) — reduces to
  `P176`'s own existing point-evaluated force law exactly.
- **Positive control 2:** Monte Carlo and closed-form log-normal moment
  formulas must agree to `<0.5%` at `N=10⁶`.
- **Cross-check on the median-vs-mean assumption:** state explicitly
  that Ramos-Ceja's own paper was not re-checked for which moment its
  fit represents (median assumed from the standard log-linear-
  regression convention) — flagged as `[INFERRED]`, not `[VERIFIED]`,
  and named as the single assumption this whole calculation rests on.

## What this claim does NOT say

1. Does not re-fit `β₁`, `β₂` under population-averaging — only computes
   what the *force-law-level* correction factors would be.
2. Does not resolve TJB's own caveat — only quantifies the piece of it
   that `E13`'s specific measured scatter can address (the `M_gas`-`T`
   contribution specifically, not the full "distribution of ALL node
   properties" his sentence names more broadly).
3. `NO_AUTHOR_ERROR` — this is a direct, literal answer to a question
   v82 poses about itself and explicitly declines to quantify; not a
   claim that not quantifying it was wrong.
