# Estimand — H1b: WHIM Thermal Energy vs Cluster Mass Bias

## EstimandOps L0 Classification
**Question type:** Predictive (observational correlation test)

## Population
Galaxy clusters in cosmological simulations (IllustrisTNG-300 or Three Hundred),
M_200c > 5×10^13 M_sun, z = 0.0–0.5.

**Inclusion criteria:**
- Relaxed + unrelaxed clusters (all dynamical states)
- Mass range: 10^13.7 – 10^15.5 M_sun (group → massive cluster)
- Redshift: z < 0.5 (to match observational counterpart CCCP, WtG)

**Exclusion criteria:**
- Halos in merging pairs (< 3 R_200 separation) — avoid mass bias confusion
- Central subhalos only (not satellite halos)

## Intervention
N/A — observational/predictive study.

## Comparator
Null hypothesis: r(delta_M, E_WHIM) = 0 — WHIM thermal energy does NOT predict
the lensing-to-hydrostatic mass gap.

## Endpoint
E_WHIM = integral of n_e × kT × dV for gas cells with T in [10^5, 10^7] K
in a shell R_200 < r < 3×R_200 around each cluster.

delta_M = M_WL − M_HE  (or equivalently M_true − M_HE for simulations)

Units: E_WHIM in erg (or keV/cm^3 × Mpc^3); delta_M in 10^14 M_sun.

## Summary Measure
Pearson correlation r(delta_M, E_WHIM).
Secondary: Spearman ρ (non-parametric, robust to outliers).
Tertiary: partial r controlling for M_WL (or M_true).

## MCID (Minimum Clinically Important Difference)
r > 0.30 required for H1b to be considered practically significant.
(Lower than H1a threshold of 0.40, because WHIM is the MORE physically
motivated proxy for TJB's mechanism.)

## ICE (Intercurrent Events)
None — observational correlation study, no time-varying events.

## Natural Language Statement

"We estimate the Pearson correlation between (M_true − M_HE) and the
warm-hot intergalactic gas thermal energy (T = 10^5–10^7 K) in the
R_200 to 3×R_200 shell for 100+ simulated galaxy clusters at z < 0.5,
comparing clusters with different WHIM environments to test whether
higher filament thermal energy predicts a larger true-to-hydrostatic
mass gap."

## What this does NOT mean

1. Does NOT test TJB's mechanism at cosmological (z > 1) scales
2. Does NOT test WHIM acting as a gravitational source — only tests
   statistical correlation (which is necessary but not sufficient for H1)
3. A positive r does NOT prove causality (WHIM → mass bias could be
   explained by cluster dynamical state → both higher WHIM + higher mass bias)
4. Does NOT apply to the WHIM in the true cosmic web (filaments between
   clusters, Mpc scale) — here we test WHIM in the cluster outskirts only
5. Simulation result [VERIFIED-SYNTHETIC] if from IllustrisTNG — must be
   followed by observational cross-check [VERIFIED-REAL] for promotion

## Prior literature summary (FL Step -4: Source Trace)

| Claim | Status | Source |
|-------|--------|--------|
| Connectivity (filament count) NOT correlated with mass bias | [VERIFIED-REAL] | Sayers et al. 2024, A&A (Three Hundred, N=3000) |
| External pressure contributes to sub-virial behavior | [VERIFIED-REAL] | Braspenning et al. 2024, MNRAS (FLAMINGO) |
| Non-thermal motions dominate mass bias | [VERIFIED-REAL] | FLAMINGO (Braspenning et al. 2024) |
| WHIM soft X-ray excess ∝ cluster dynamical state | [VERIFIED-SYNTHETIC] | Vladutescu-Zopp et al. 2025 arXiv:2506.18459 (TNG, N=138) |
| WHIM thermal energy in filaments vs mass bias: NO PRIOR TEST | [VERIFIED-ABSENT] | This work (H1b is novel) |

## Pre-registered criteria (set BEFORE seeing data)

- PROMOTE (H1b survives): r > 0.30, p < 0.10 (lower threshold justified by
  more physically motivated proxy vs H1a)
- INCONCLUSIVE (REPEAT): 0.15 ≤ r ≤ 0.30 or 0.05 < p < 0.10
- KILL (H1b fails): r < 0.15 AND p > 0.20

## Data requirements (FL Step -2: Cheapest differentiating test)

**Option A (recommended): IllustrisTNG-300 API**
- URL: https://www.tng-project.org/api/
- Registration: free (tng-project.org account)
- Need: API key for gas particle data
- Per-cluster: gas cells, T-filter, r-shell filter, sum n_e×kT×dV
- M_HE: compute from pressure gradient of gas within R_200 (standard X-ray hydrostatic)
- M_true: SubhaloMassType[0+1] (DM + gas + stars within R_200)
- Sample: ~200 clusters at M > 5×10^13 M_sun at z=0.2 (snapshot ~67)
- Cost: ~4-8h Python + API

**Option B: Published TNG mass bias table + new WHIM computation**
- Barnes et al. 2021 (Mock-X, arXiv:2001.11508): HE bias for TNG300 clusters
- Cross-reference with TNG API for WHIM thermal energy
- Sample: ~100 clusters from Mock-X
- Cost: ~2-4h (if Barnes et al. data table accessible)

**Option C: Published IllustrisTNG X-ray soft excess (Vladutescu-Zopp 2025)**
- arXiv:2506.18459: 138 TNG clusters with WHIM soft X-ray excess + dynamical state
- If mass bias b_HSE is also available in that paper → direct correlation possible
- Cost: ~1-2h (read paper, check for mass bias tabulation)

## Status
[IN-PROGRESS] Claim defined. Estimand defined. Data access pending.
Next step: Check Option C (Vladutescu-Zopp 2025) for mass bias data first (cheapest).
If not available: Option A (TNG API registration + computation).
