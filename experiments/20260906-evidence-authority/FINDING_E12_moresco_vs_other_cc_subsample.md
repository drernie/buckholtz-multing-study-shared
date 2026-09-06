# FINDING E12 — Moresco's 15 CC points and the other 16 give visually
# different ΛCDM fits, but the difference is NOT statistically material:
# `E8c`'s sign flip is amplified noise, not a real inter-group tension

**Date:** 2026-09-06
**Claim:** `CLAIM_E12_moresco_vs_other_cc_subsample.md` (pre-registered)
**Script:** `E12_moresco_vs_other_cc_subsample.py`
**Continues:** `FINDING_E8`/`E8c`'s named side-finding — the 16 non-
Moresco CC points pull `Δχ²(MULTING vs free ΛCDM)` from `+2.64` (on
Moresco's 15 alone) to `+0.56` (all 31), flipping sign under covariance.

## Controls — pass

- **PC1 regression:** direct 31-point diagonal ΛCDM fit, `H₀=68.150,
  Ωₘ=0.3196, χ²=14.492`.
- **PC2 sanity:** each subsample's own best fit has lower χ² on its own
  points than the union fit does — confirms the split fits are genuine
  optima, not artifacts.

## Result

| subsample | n | `H₀` | `Ωₘ` | χ² (own) |
|---|---|---|---|---|
| Moresco's 15 | 15 | `66.83 ± 4.02` | `0.339 ± 0.097` | `5.92` |
| Other 16 | 16 | `72.38 ± 5.98` | `0.277 ± 0.075` | `7.90` |

The point estimates differ by `5.5` in `H₀` — visually a real split
(Moresco's own low-`z` sample runs cooler, matching the CC-vs-SH0ES
`H₀` tension direction; the other 16 run closer to SH0ES). But the
**joint 2-parameter test** (using each subsample's own Hessian-derived
covariance, the same estimator convention `P176`/`P191` already use):

```
Δχ² = 0.652   (2 dof, 95% threshold = 5.99)
```

**Not material by a wide margin.** The `5.5`-unit `H₀` gap sits inside
`~1σ` of the combined uncertainty (`√(4.02²+5.98²)≈7.2`), and the
cross-check confirms it: each subsample's own best fit, evaluated on
the *other's* points, costs only `~1-3` extra χ² (`8.77` vs own-best
`7.90`; `9.13` vs own-best `5.92`) — a small, unremarkable degradation
for 15-16 points, not the signature of two genuinely inconsistent
populations.

## What this means for `E8c`

`E8c`'s sign flip (`+2.64→+0.56→negative under covariance`) is **real
in the arithmetic sense** — it happens, and `E8c` correctly traced it
to these 16 points — but this file shows the underlying cause is
**ordinary statistical scatter in a small sample**, not a documented or
detectable inconsistency between CC measurement groups. MULTING's own
3-parameter fit is simply more sensitive to which small subset of `31`
points happens to pull which way than a 2-parameter ΛCDM fit is — which
is itself consistent with `FINDING_E8`'s lead result (MULTING's own
degeneracy makes its fit unusually sensitive to exactly this kind of
perturbation).

## What this does NOT establish

1. Does not claim the two subsamples are drawn from "the same
   population" in a strong sense — only that this specific 2-parameter
   test finds no evidence against it at the pre-registered threshold.
   A more sensitive test (more parameters, or a purpose-built
   heterogeneity statistic) might find something this one does not.
2. Does not revisit `E8`'s own headline (`|Δχ²|≤2.6`, no discrimination
   either way) — this file explains *why* the sign was unstable, it
   does not change that conclusion.
3. `NO_AUTHOR_ERROR` — entirely about internal consistency of a public
   catalog compilation, not a claim about any measurement group's own
   published result.
