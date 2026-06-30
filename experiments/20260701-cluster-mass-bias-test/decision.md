# Decision — 20260701-cluster-mass-bias-test

**Date:** 2026-07-01
**Status:** KILL (H1a)
**Evidence grade:** B (N=50, real observational data)

## Numerical results

| Test | r (Pearson) | p-value | ρ (Spearman) | p-value |
|------|-------------|---------|--------------|---------|
| r(delta_M, M_gas×T_x)          |  0.021 | 0.883 | −0.019 | 0.897 |
| r(delta_M, T_x)                | −0.169 | 0.240 | −0.201 | 0.162 |
| r(delta_frac, T_x)             | −0.263 | 0.065 | −0.242 | 0.091 |
| r(delta_frac, M_gas×T_x)       | −0.108 | 0.457 | −0.048 | 0.740 |
| partial r (controlling M_WL)   | −0.701 | <0.0001 | — | — |

**Descriptive:**
- mean delta_M = 0.86 ± 2.77 [10^14 M_sun]
- mean delta_frac = 0.22 ± 0.55
- Clusters with M_WL > M_HE: 28/50 (56%)
- HOT (T_x > 8 keV, N=13): mean delta_M = 0.07, delta_frac = -0.005
- COOL (T_x < 6 keV, N=20): mean delta_M = 1.20, delta_frac = 0.359

## Verdict

**H1a KILLED** by pre-registered criterion: r = 0.021 < 0.20, p = 0.88 >> 0.30

Direction finding: The correlation is slightly NEGATIVE (not positive as H1 requires).
Hot clusters show SMALLER mass bias than cool clusters — opposite to TJB prediction.

## What was killed

**Killed:** H1a formulation — "cluster ICM thermal energy (M_gas × T_x) predicts
the lensing-to-hydrostatic mass gap in X-ray luminous clusters"

## What was NOT killed

**NOT killed:** H1 (broad TJB) — "cosmic web IGM thermal energy at node/filament
scales acts as a second gravitational source"

**Reasons:**
1. CCCP uses cluster ICM (inside virial radius); TJB's mechanism is about
   cosmic web gas in FILAMENTS/NODES surrounding clusters
2. The WHIM (warm-hot intergalactic medium, T ~ 10^5-10^7 K) is not measured
   in CCCP — it requires X-ray spectroscopy of filaments between clusters
3. The correct proxy for TJB's mechanism would be: T_WHIM × M_WHIM for gas
   in filaments feeding the cluster, not the cluster ICM itself

## Confounder analysis

r(M_WL, E_proxy) = 0.713 — strong mass-scaling confound
→ More massive clusters have BOTH higher M_WL and higher M_gas × T_x
→ After controlling for M_WL: partial r = -0.701, p < 0.0001
→ This means: given equal M_WL, clusters with MORE thermal energy have
   LESS mass bias (not more) — strongly contra H1a

The negative partial correlation likely reflects:
- Cool-core clusters have higher ICM temperature at fixed mass
- Cool-core clusters are more relaxed → better satisfy hydrostatic equilibrium
→ Better HE mass estimates → smaller mass bias

## Relaxation Map (Minimal Relaxation Rule)

If H1a is dead, what assumption changes might revive it?

| Variant | Changed assumption | Prediction |
|---------|-------------------|------------|
| H1b | Use WHIM gas (T~10^5-10^7 K) in filaments | Need cosmic web maps + Sunyaev-Zel'dovich filament data |
| H1c | Use thermal energy EXCESS (above ΛCDM expectation) | Need ΛCDM baseline M_gas(M500) relation subtracted |
| H1d | Effect only at group/cluster transition (M < 10^14 M_sun) | Need low-mass groups data |
| H1e | Effect only on velocity dispersion, not mass (different observable) | Need velocity dispersion data |

## Kill Analysis

**What the null result killed:**
H1a under conditions {cluster ICM data, N=50 X-ray luminous clusters, z=0.15-0.55,
CCCP selection, r criterion >0.4, p<0.05}

**Surviving assumptions that H1b-H1e test:**
- The mechanism may operate at FILAMENT scale, not cluster scale
- The proxy may need to be WHIM gas, not ICM
- The scale may be wrong (cluster vs node of cosmic web)
- The relevant quantity may be pressure (n × T) not energy

## Skeptic concerns (pre-answered)

**Concern 1:** "You're testing cluster ICM, not cosmic web IGM"
→ ACCEPTED as limitation. H1a scope is narrower than H1. This is documented.

**Concern 2:** "Mass scaling confounds everything"
→ VERIFIED: r(M_WL, E_proxy) = 0.713. Addressed via partial correlation.

**Concern 3:** "N=50 is insufficient for subtle correlation detection"
→ ASSESSED: power to detect r=0.4 at p<0.05 with N=50 is ~91% (adequate).
   We would have detected r=0.4 with high probability. r=0.021 is a genuine null.

## Next experiment: H1b

Test: Map warm-hot intergalactic medium (WHIM) around cluster sample
using: tSZ signal from Planck + Sunyaev-Zel'dovich filament maps
       OR eROSITA all-sky survey (launched 2019) filament emission
Criterion: r(delta_M, WHIM thermal pressure) > 0.3, p < 0.10
Cost: Literature-based (eROSITA DR1 / Planck tSZ filaments); ~2-4h search

Alternatively: Use cosmological simulations (IllustrisTNG, BAHAMAS) to
compute E_WHIM around clusters and test H1 prediction.

## FL Ladder outcome

- Step -5 (Zero-Signal Gate): PASSED (entity=cluster sample, predicate=correlation, outcome=r,p)
- Step -2 (L0 classify): Predictive
- Step 0 (claim): H1a — ICM thermal energy → mass bias correlation
- Steps 1-6 (minimal test, controls, baseline): CCCP data, r=0 baseline
- Step 8 (classify): KILL (r=0.021 << 0.20, p=0.88 >> 0.30)
- Step 9 (caveats): cluster ICM ≠ cosmic web IGM; not a test of broad H1
- Step 10 (go/no-go): NO-GO for H1a; H1 (broad) status = inconclusive
- Step 11 (null_results): Entry below

## null_results entry

Add to null_results/INDEX.md:
| 20260701 | 20260701-cluster-mass-bias-test | H1a: cluster ICM thermal energy not correlated with WL-HE mass gap | KILL | r=0.021, p=0.88, N=50, CCCP data |
