# Claim — 20260701-cluster-mass-bias-test

## Question type (EstimandOps L0)
[x] Predictive — does E_ICM/c² predict the WL-to-HE mass difference?

## Natural language statement
We estimate the Pearson correlation between (M_WL − M_HE) and M_gas × T_x
for 50 X-ray luminous galaxy clusters, comparing clusters with different
thermal energy proxies to test whether higher ICM thermal energy predicts
a larger lensing-to-hydrostatic mass excess.

## Falsifiable claim
H1a (sub-hypothesis of H1 TJB): Within the CCCP sample, (M_WL − M_HE)
correlates POSITIVELY with M_gas × T_x (thermal energy proxy), meaning
clusters with more ICM thermal energy show a larger WL-to-hydrostatic
mass gap.

**Estimand:**
- Population: X-ray luminous galaxy clusters, 0.15 < z < 0.55 (CCCP, N=50)
- Intervention: N/A (observational)
- Comparator: null correlation (r = 0)
- Endpoint: r( delta_M, E_proxy ) where delta_M = M_WL − M_HE, E_proxy = M_gas × T_x
- Summary measure: Pearson r with p-value
- MCID: r > 0.4 required for practical significance

## Pre-registered criteria (set BEFORE seeing data)
- H1 PASSES → PROMOTE: r > 0.4 AND p < 0.05
- H1 INCONCLUSIVE → REPEAT: 0.2 ≤ r ≤ 0.4 or p near 0.05
- H1 FAILS → KILL: r < 0.2 OR p > 0.3

## Source
[VERIFIED-REAL] Mahdavi et al. 2013, ApJ 767, 116, arXiv:1210.3689
- Table 1: T_x (keV) for 50 clusters
- Table 2: M_WL, M_gas, M_hydro (10^14 M_sun) for 50 clusters

## What this does NOT mean
1. Does NOT test the broader H1 (cosmic web IGM thermal energy as 2nd gravity source)
2. Does NOT test TJB's mechanism at cosmic web filament / node scales
3. Does NOT include WHIM (warm-hot intergalactic medium) outside cluster virial radius
4. Does NOT apply to groups or low-mass clusters (CCCP is X-ray luminous subsample)

## Relationship to H1 hierarchy
H1 (full TJB claim): IGM thermal energy at cosmic web NODES = 2nd grav. source
H1a (this test):     CLUSTER ICM thermal energy → lensing-hydrostatic mass gap

H1a is a necessary but not sufficient condition for H1:
- H1a PASSES → H1 plausible (but not proven — different gas component)
- H1a KILLS → H1 in specific sub-form killed; broader H1 still untested
