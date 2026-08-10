# P2 (complete): is k a second charge, or M wearing a different unit?

**Date:** 2026-08-10 · plan item P2, completed with CHEX-MATE cross-validation
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P2_charge_identifiability_chexmate.py`, ruff clean

---

## Why the naive test (session's first pass) was insufficient

A first pass regressed `ln k` on `ln M` alone and found `α = 1.269 ± 0.042`,
`R² = 0.628`. That is not identifiability by itself: **a deterministic
`k = f(M)` at *any* slope is still one number per cluster**, not a second
degree of freedom. The two-charge completion is physically interesting only if
`k` carries real scatter at fixed `M` that a different instrument can also see.

## Step 1 — is `k_pipe` a pure formula of `(M, z)`?

Regressing `ln k` on `ln M` **and** `ln(1+z)` jointly (the earlier single-variable
fit conflated the two, since this flux-limited sample has `M` and `z`
correlated):

```
R^2(ln k ~ ln M + ln(1+z)) = 0.6538
slope d ln(k)/d ln(M) at fixed z = 1.020        <- not 1.269; that number mixed in z
residual scatter = 0.540 nat = 0.235 dex
```

**35 % of `ln k`'s variance is not explained by `(M, z)` alone.** The
pipeline's SZ observable (`Y500`) does carry genuine cluster-to-cluster
information beyond mass and redshift — necessary but not sufficient for
identifiability, since some of that 35 % could be pure measurement noise.

## Step 2 — an independent noise floor, entirely internal to CHEX-MATE

`chexmate_combined.csv` carries **two independent temperature estimators for
the same clusters** — `Ti_from_TX` (X-ray spectroscopy) and `Ti_from_sigma`
(galaxy velocity dispersion) — for 23 clusters, with no input from
`clusters_clean.csv` at all:

```
scatter of ln(Ti_TX / Ti_sigma)  = 0.354 nat = 0.154 dex
implied per-estimator noise      ~ 0.109 dex   (IF both equally noisy & independent)
```

**This is the noise floor any single T-estimator — including the pipeline's
SZ-derived `k` — must be compared against before its scatter counts as real
physics.** The "IF" is a stated modelling assumption (equal, independent
noise), not a measured fact; treated as illustrative, not exact.

## Step 3 — cross-match, with a circularity trap found and avoided

`data/chexmate_real_TX.csv`'s `M500_Msun` has **no traceable generating script
in this repository** — checked, not assumed (one commit, "commit real datasets
+ pipeline for script reproducibility", did not include the pipeline). Its
slope against `TX_cx`, `ln M_cx = 1.55 ln TX_cx + const`, sits close to the
self-similar `3/2` — consistent with `M_cx` having been *derived* from `TX_cx`,
which would make "`M_cx·TX_cx`" a circular second `k`-estimator.

**Avoided entirely:** the cross-match uses `TX_cx` alone, regressed against the
*pipeline's* `M500` (`clusters_clean.csv`, sourced from MCXC-I via an X-ray
**luminosity** scaling relation — `M500c_method = 'X-ray_Lx_scaling'`, a third,
different observable from both `k_pipe` and `TX_cx`).

Positional match, `<3'`, all 25 of 25 CHEX-MATE clusters matched:

```
slope alpha(k_pipe vs M_pipe) in this subsample = 1.292
slope alpha(TX_cx  vs M_pipe)                   = 0.480   (self-similar predicts 0.667)
scatter at fixed M: k_pipe 0.173 dex,  TX_cx 0.076 dex

CORRELATION OF RESIDUALS  rho = +0.361   (n=25, null SE ~ 0.213)
implied shared (intrinsic) scatter = sqrt(rho * sig1 * sig2) = 0.069 dex
```

**Guards, run because a residual correlation between two catalogues can be
faked by a shared confound:**

```
corr(residual, z)         : +0.01 (k_pipe),  +0.10 (TX_cx)
corr(residual, match sep) : +0.20 (k_pipe),  +0.14 (TX_cx)
```

Both small — the correlation is not obviously a redshift trend or a
mismatch artefact.

## The honest verdict

```
sig_int (Step 3, implied intrinsic scatter)  = 0.069 dex
sig_noise (Step 2, internal error floor)     = 0.109 dex
```

**The implied intrinsic scatter does not clearly exceed the measurement-noise
floor.** `rho = +0.36` is positive and the guards don't explain it away, which
is *suggestive* that `k_pipe` and `TX_cx` see correlated real cluster physics
at fixed mass — but at `n = 25` the null-correlation standard error (`~0.21`)
is comparable in size to the observed `ρ` itself, so this falls short of a
decisive detection.

## Verdict

```
k_pipe is deterministic in (M,z)?     : NO -- 35% unexplained variance (n=548)
Independent noise floor (CHEX-MATE)   : 0.109 dex, internal, no pipeline input
Circularity trap in M500_Msun (CHEX-MATE) : FOUND and AVOIDED (TX_cx used alone)
Cross-match intrinsic scatter (n=25)  : 0.069 dex, POSITIVE correlation (rho=+0.36)
                                        but not clearly above the noise floor
Guards (z, match quality)             : small, do not explain the correlation away
Overall                               : SUGGESTIVE that k carries real information
                                        beyond M; NOT a decisive detection at
                                        current sample size
```

## What this does NOT establish

1. Not proof that MULTING's `k` is a genuine independent charge — the data are
   consistent with that, and also consistent with `k`'s scatter being mostly
   measurement noise the small cross-match sample can't rule out.
2. `M500_Msun` in `chexmate_real_TX.csv` was deliberately not used anywhere in
   the decisive test, precisely because its provenance could not be verified
   here — its earlier use in this session's preliminary pass should be
   discounted relative to this version.
3. `α ≈ 1.02` (this run) vs `α ≈ 1.27` (the naive single-variable fit) differ
   because `z` was not controlled for in the earlier pass — a reminder that in
   a flux-limited sample, a mass–proxy slope without a redshift control can be
   partly a selection effect, not a physical scaling law.

## What would resolve it

A larger cross-match — CHEX-MATE has ~100 clusters with `Ti_from_sigma` alone
(only 23 have both estimators, but many more have *some* independent
temperature-like measurement) — or a direct weak-lensing mass for the 25
already matched, which would let `M_cx` join the test without the circularity
concern raised above.
