# CLAIM E12 — do Moresco's 15 cosmic-chronometer points and the other
# 16 (different groups) actually disagree, or is `E8c`'s effect noise?

**Date:** 2026-09-06 (pre-registered before any code)
**Continues:** `FINDING_E8`/`E8c`, which found MULTING's sign vs free ΛCDM
flips only when 16 non-Moresco CC points are included, and that those 16
points on their own pull `Δχ²` from `+2.64` to `+0.56` relative to
Moresco's 15. Named there as a side-finding worth checking on its own.
Explicit go-ahead: "запускай" (general, per the user's own stated order).

## L0 (EstimandOps)

**Question type: descriptive.** Do Moresco's 15 CC points and the other
16 (Simon+2005, Stern+2010, Zhang+2014, Ratsimbazafy+2017, and others,
as compiled in TJB's own 31-point set) imply different flat-ΛCDM
parameters, or is any apparent difference consistent with their quoted
statistical errors alone?

## Falsifiable predicate

If the two subsamples are statistically consistent, independently fit
`(H₀, Ωₘ)` should agree within their own combined uncertainties. If they
disagree beyond that, the `E8c` effect reflects a real, if modest,
inter-group inconsistency in the CC compilation itself — not an
artifact of how `E8` built the covariance.

## Method (cheap, diagonal errors only — no new covariance machinery)

1. Split TJB's 31-point `CC_POINTS` (`P176`) into Moresco's 15
   (identified in `E8c` by `(z,H)` match) and the other 16.
2. Fit flat ΛCDM `(H₀,Ωₘ)` to each subsample alone (diagonal χ², Nelder-
   Mead, as `E8b`), and to the union (regression check: must match
   `P176`'s own 31-point CC-only fit, not previously computed but
   derivable).
3. Compare `H₀` and `Ωₘ` between the two subsample fits with a proper
   joint 2-parameter test (χ² of the parameter difference using the sum
   of each fit's own inverse-Fisher covariance, not eyeballing 1D error
   bars — a discipline this project's own `P176`/`P193` already uses
   for 2-parameter surfaces).

## Pre-registered MCID

**MATERIAL** if the joint 2-parameter difference exceeds `Δχ²=6.18`
(2 dof, `95%`). **Not material** below that — reported as consistent
with statistical fluctuation, not as "no difference."

## Controls

- **Regression:** union of both subsamples' fit must reproduce a direct
  31-point CC-only ΛCDM fit (computed once, independently, as the
  control) to `<0.5%` in both parameters.
- **Sample-size sanity:** report each subsample's own χ² at its best fit
  and at the OTHER subsample's best fit — if a subsample's own best fit
  is not meaningfully better than the other's on its own points, the
  "disagreement" is not real regardless of the joint test.

## What this claim does NOT say

- Nothing about MULTING vs ΛCDM (E8's own topic) — this is entirely
  about internal CC-compilation consistency.
- Does not question any individual group's own published measurement or
  its errors — only asks whether the ENSEMBLE is mutually consistent.
- `NO_AUTHOR_ERROR`.
