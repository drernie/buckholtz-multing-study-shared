# Estimand — H1d: Mass-Threshold Effect

## EstimandOps L0 Classification
**Question type:** Predictive (subgroup correlation analysis)

## Population
**Full sample:** CCCP N=50, same as H1a (Mahdavi et al. 2013) [VERIFIED-REAL]

**High-mass subsample:** clusters with M_WL above sample median (~5×10^14 M_sun),
approximately n=25 clusters.

**Low-mass subsample:** clusters with M_WL below sample median, approximately n=25 clusters.

**Inclusion criteria:** same as H1a — all N=50 CCCP clusters with both M_WL and M_HE measured.

**Exclusion criteria:** none beyond those applied in H1a.

## Intervention
N/A — observational subgroup analysis.

## Comparator
Null hypothesis: r(delta_M, E_ICM | M_WL) is EQUAL in high-mass and low-mass
subsamples (no mass-threshold effect).
Fisher z-test: z = (z_1 - z_2) / sqrt(1/(n_1-3) + 1/(n_2-3))

## Endpoint
**Primary:** partial correlation r(delta_M, E_ICM | M_WL) computed in each mass subsample.

**Secondary:** slope of delta_frac vs T_x regression in high-T (T > 5 keV) vs low-T (T < 5 keV) clusters.

Where:
- delta_M = M_WL - M_HE [OUR-RECONSTRUCTION]
- E_ICM = M_gas × T_x [OUR-RECONSTRUCTION proxy, same as H1a]
- M_WL = lensing mass (Mahdavi et al. 2013)

## Summary Measure
Fisher z-test statistic for difference between two partial Pearson correlations.
Reported: r_high, r_low, z-statistic, two-tailed p-value.

**Secondary:** Pearson r(delta_frac, T_x | M_WL) in T_x > 5 keV vs T_x < 5 keV subsets.

## MCID (Minimum Clinically Important Difference)
|r_high| - |r_low| > 0.25, confirmed by Fisher z-test p < 0.10 (one-tailed: r_high > r_low).

**Significance threshold:** p < 0.10 (one-tailed) for Fisher z-test.

**Power note:** With n~25 per bin, power to detect r-diff=0.40 is ≈50%. Low-power test.
INCONCLUSIVE is the default expectation; PROMOTE requires effect size > 0.50 in high bin.

## ICE (Intercurrent Events)
**ICE strategy: treatment-policy**

Potential ICEs:
- Cluster M_WL uncertainty places it in the wrong bin: analyze sensitivity by
  using ±1σ mass bins; include all regardless of uncertainty in main analysis
- Cluster has T_x measured at different apertures across papers: use Mahdavi et al. 2013
  published T_x for all clusters; do not substitute with different papers

Rationale: treatment-policy includes all clusters at face-value published masses.
Mass uncertainty sensitivity check done separately.

**Significance threshold:** p < 0.10 (Fisher z-test, one-tailed).

## Natural Language Statement
"We estimate whether the Pearson partial correlation between lensing-to-hydrostatic
mass gap and ICM thermal energy proxy (controlling for WL mass) differs significantly
between the N~25 most massive and N~25 least massive clusters in the CCCP sample
(total N=50), testing whether the ICM-mass-bias association is stronger at higher halo
masses consistent with a mass-threshold mechanism."

## What this does NOT mean
1. Does NOT establish that TJB's mechanism is absent in low-mass clusters — only
   tests whether the statistical association differs across mass bins
2. Does NOT test the causal direction (correlation, not causation)
3. An INCONCLUSIVE result does NOT mean no threshold exists — the test is underpowered
4. PROMOTE does NOT imply TJB mechanism over competing explanations (H1c still applies)
5. Does NOT distinguish between H1 (thermal energy effect) and alternative explanations
   that also scale with halo mass (e.g., non-thermal pressure, AGN feedback)

## Statistical analysis plan

```python
import numpy as np
from scipy import stats

# Load CCCP data (same as H1a)
# M_WL, M_HE, M_gas, T_x, z for N=50 clusters
# delta_M = M_WL - M_HE
# E_proxy = M_gas * T_x (normalized)

# Step 1: Split by median M_WL
mask_high = M_WL > np.median(M_WL)  # n_high ~ 25
mask_low = ~mask_high  # n_low ~ 25

# Step 2: Partial correlation in each subsample
# using scipy.stats.partial_corr or pingouin

# Step 3: Fisher z-test
z1 = np.arctanh(r_high)
z2 = np.arctanh(r_low)
n1, n2 = mask_high.sum(), mask_low.sum()
z_stat = (z1 - z2) / np.sqrt(1/(n1-3) + 1/(n2-3))
p_val = 1 - stats.norm.cdf(z_stat)  # one-tailed: r_high > r_low

# Step 4: T_x sensitivity
mask_hot = T_x > 5.0  # keV
r_hot = partial_corr(delta_M, E_proxy, M_WL, mask=mask_hot)
r_cool = partial_corr(delta_M, E_proxy, M_WL, mask=~mask_hot)
```

## Data requirements
Same CCCP data as H1a — NO new data needed.
[VERIFIED-REAL] Mahdavi et al. 2013, ApJ 767, 116 — M_WL, M_HE, M_gas, T_x published.

**Cost: < 1h computation on existing dataset.**

## Status
[EXECUTABLE — data already available]
This is the cheapest next-step test in H1 Cycle 2.
Priority: HIGH (no data acquisition needed, directly tests mass-scale prediction)
