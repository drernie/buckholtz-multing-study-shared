# Claim — H1e: AGN Feedback Mediates the ICM/Mass-Bias Partial Correlation

## Hierarchy

H1 (MULTING thermal energy = second gravitational source)
  └── H1a: ICM thermal energy correlates with mass gap → KILLED (r=0.021, p=0.883)
  └── H1b: WHIM in cluster outskirts correlates with mass gap → NEEDS-DATA
  └── H1c: Morphological state (centroid shift wX) explains the partial correlation → KILLED (r_residual=-0.726, unchanged from baseline)
  └── H1d: Effect is mass-threshold-dependent → KILLED (r_diff=0.001)
  └── **H1e: AGN feedback (radio/kinetic mode, cool-core regulation) explains the partial correlation**

## Motivation (registered gap from NR-012)

NR-012 (H1c decision.md, `experiments/20260701-h1c-morphology-mass-bias/decision.md:81`
and Relaxation Map row in `null_results/20260701-nr012-h1c-morphology-mediator.md:51`)
explicitly listed AGN feedback as an untested alternative explanation for the partial
correlation `r(delta_M, E_ICM | M_WL) ≈ -0.70 to -0.73`, and named the missing
ingredient as "AGN-activity indicators per cluster" — flagged but never pursued,
because no covariate was in hand at the time.

Physical motivation (standard astrophysics, not TJB-specific): AGN feedback in its
Radio/Kinetic Mode (dominant in massive relaxed ellipticals/cool-core cluster BCGs —
the same regime as most of the CCCP sample) injects non-thermal turbulent energy into
the ICM via jets and X-ray cavities. Two distinct channels could produce the observed
partial correlation without invoking TJB's mechanism:
1. AGN-driven turbulence inflates the thermal-energy proxy E_ICM without tracking the
   true gravitational potential depth.
2. The same non-thermal pressure violates the hydrostatic-equilibrium assumption used
   to derive M_HE, directly biasing delta_M = M_WL - M_HE.

This is mechanistically distinct from H1c (morphological/dynamical disturbance, tested
via centroid shift wX): a cluster can be dynamically relaxed (low wX, would pass H1c)
while still hosting strong AGN feedback (cool-core clusters are, almost by definition,
BOTH relaxed AND AGN-regulated — that is precisely why cooling flows don't run away).
H1e is therefore NOT a retry of H1c under a different name; it targets a mechanism
H1c's covariate (wX) does not capture. Flagged explicitly per the Adaptive Iteration
Branch Rule so this isn't mistaken for reopening a killed branch.

## FL Zero-Signal Gate (Step -5)

- Entity: CCCP clusters (N=50, Mahdavi et al. 2013) [VERIFIED-REAL], the same sample
  as H1a/c/d
- Falsifiable predicate: an AGN-feedback indicator (cool-core status, and/or a
  quantitative radio/X-ray-cavity power proxy) predicts residual mass bias after
  controlling for M_WL AND E_ICM
- Measurable outcome: partial r(delta_M, AGN_indicator | M_WL, E_ICM) compared to a
  pre-registered threshold, mirroring H1c's design exactly

Gate passes. Proceed to claim.

## Falsifiable Claim (FL Step 0)

**H1e-main:** The partial correlation `r(delta_M, E_ICM | M_WL) ≈ -0.70` is primarily
explained by AGN feedback activity. Specifically: after also conditioning on an
AGN-feedback indicator, the residual partial correlation
`r(delta_M, E_ICM | M_WL, AGN_indicator)` drops below 0.20 in absolute value.

**H1e-mechanism:** Clusters with strong AGN feedback (cool-core, radio-loud BCG,
and/or detected X-ray cavities) have systematically different E_ICM (inflated by
non-thermal turbulent energy) and/or delta_M (biased by non-thermal pressure in the
HE mass estimate) than clusters without strong central AGN activity, in a way that
reproduces the observed negative partial correlation without requiring TJB's
mechanism.

## Pre-registered Criteria (set BEFORE fetching any AGN indicator's relationship to
delta_M/E_ICM -- the cluster list + cool-core flags below were already fetched as
part of identifying the sample, but no correlation with the outcome variables has
been computed yet at the time this file is written)

| Outcome | Verdict | Implication |
|---------|---------|-------------|
| \|r(delta_M, E_ICM \| M_WL, AGN_indicator)\| < 0.20 AND cool-core/AGN status itself correlates with delta_M or E_ICM at \|r\|>0.30 (p<0.10) | PROMOTE H1e; partial r explained by AGN feedback | TJB mechanism NOT needed for partial r finding |
| 0.20 ≤ \|residual r\| ≤ 0.40 | INCONCLUSIVE (REPEAT) | AGN feedback partial explanation; TJB mechanism remains possible |
| \|residual r\| > 0.40 AND still significant p < 0.10 | KILL H1e; partial r survives AGN control | Third standard-physics alternative eliminated; strengthens H1's remaining space (H1b only) |

**Key asymmetry (same as H1c):** H1e KILL -> supports H1 (TJB mechanism, by further
elimination); H1e PROMOTE -> undermines H1's need.

## Two-phase data plan (honest scope note)

Unlike H1c (which reused already-cached delta_M/E_ICM values from the H1a
computation), this session found that **no CSV of the underlying H1a/c/d per-cluster
values (delta_M, E_ICM, M_WL, wX) was ever persisted** -- they were computed inline in
a prior session and are not reproducible from files currently in this repo. This is a
real gap, not specific to H1e.

- **Phase 1 (shared infrastructure fix):** re-extract M_WL, M_HE, M_gas, T_x, wX per
  cluster from Mahdavi et al. 2013 (source of all of H1a/c/d/e), save as
  `experiments/20260713-h1e-agn-feedback-confound/artifacts/cccp_base.csv` so this
  gap does not recur for any future H1x branch. This reproduces H1a/c/d's numbers as
  a validation step before adding anything new.
- **Phase 2 (H1e-specific):** add the AGN-feedback indicator column(s) -- cool-core
  flag (already identified, same Mahdavi 2013 source, zero additional fetch cost) as
  the cheapest first test, with a quantitative radio-luminosity or X-ray-cavity power
  catalog as a stretch goal if cool-core alone is inconclusive.

## Assumptions (Claim Entropy)

| # | Assumption | Testable? | Evidence |
|---|-----------|-----------|---------|
| A1 | Cool-core classification (Mahdavi et al. 2013) is a valid, if coarse, proxy for AGN feedback activity | [VERIFIED-REAL, literature-established] | Standard result: cool-core clusters host radio-loud BCGs regulating cooling flows (McNamara & Nulsen review; Rafferty et al. 2006; Bîrzan et al. 2004) |
| A2 | Cool-core status is not simply a relabeling of wX (already tested, killed in H1c) | [OPEN] | Cool-core and centroid-shift disturbance are correlated in the literature but not identical; needs an explicit check r(cool-core, wX) before interpreting H1e as independent of H1c |
| A3 | Base CCCP data (M_WL, M_HE, M_gas, T_x) is re-extractable from the same Mahdavi 2013 source used for H1a/c/d | [VERIFIED-REAL, source identified] | Same paper, same tables, ar5iv HTML fetch already demonstrated working this session |
| A4 | A quantitative AGN radio/cavity catalog with meaningful CCCP overlap exists and is publicly accessible | [UNVERIFIED] | Not yet searched; cool-core flag is the fallback if this fails |

**Claim entropy:** 2 (A2, A4 open; A1, A3 resolved)

## Counterfactual Frame

"In what world is H1e true?"
-> A world where standard AGN-feedback astrophysics (already well-established,
independent of MULTING) is sufficient to explain the partial correlation, without
needing to invoke a second gravitational source.
-> TJB's mechanism is not detectable at cluster scale once AGN feedback is properly
accounted for, just as it was not detectable once morphology (H1c) was accounted for.

Independent changes needed for H1e to be false (and H1 to survive further, pending
H1b): AGN-feedback indicator does NOT explain the residual (per the KILL criterion
above) -- would be the third of three natural standard-physics alternatives
eliminated (H1a raw correlation, H1c morphology, H1e AGN feedback), leaving H1b
(WHIM/filament, TJB's actual proposed cosmic-web-scale mechanism) as the only
remaining untested channel.

## Status
**NEEDS-DATA (2026-07-13).** Pre-registration complete. Phase 1 (base CCCP data
re-extraction) and Phase 2 (AGN indicator fetch + test) not yet started.
