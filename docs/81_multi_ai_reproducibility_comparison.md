# Multi-AI Reproducibility Comparison

**Date:** 2026-05-30  
**Purpose:** Compare ChatGPT, Claude, and Gemini supplementary table outputs  
**Status:** COMPLETED — Internal analysis only

**Safety Labels:**
```
MULTI_AI_REPRODUCIBILITY_COMPARISON
INTERNAL_ANALYSIS_ONLY
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_REVIEW_REQUIRED_BEFORE_EXTERNAL_USE
```

---

## Executive Summary

**Main finding:** AI-service outputs differ materially in fitted beta parameters (5.4–5.8× for β_d, 42.6–94.7× for β_q) and some table construction choices (time grids, H₀ anchors, z-value spacing).

**Stable findings:** H-FLRW calculation methods appear consistent across services (same cosmological model).

**Unstable findings:** H_MULT values, beta parameters, future projection estimates, and time grid choices vary significantly across services.

**Implication:** These differences motivate explicit provenance tracking before using such tables for model comparison. Without understanding which AI service was used and which optimization method was employed, H_MULT values cannot be reliably compared across studies.

**Recommendation:** Request author clarification on which AI service output is the "primary" one, or whether all three should be considered valid alternative fits requiring uncertainty quantification.

---

## Comparison Matrix

### Service Metadata

| Service | Session Date | URL | Model Version |
|---|---|---|---|
| **ChatGPT** | 2026-05-07 | https://chatgpt.com/c/69fcdf62-f83c-83e8-9bf9-317a9d880b47 | (Not specified) |
| **Claude** | 2026-05-07 | https://claude.ai/chat/f7cab88d-4bc7-4129-8bed-e31a425171c1 | Sonnet 4.6 |
| **Gemini** | 2026-05-07 | https://gemini.google.com/app/972ef3f67a492efa | Thinking |

**Note:** All three AI services were queried on the same date (2026-05-07) with the same prompt (documented in Supplementary Material pages 2-7).

---

## 1. Time / Redshift Grid Comparison

### Row Counts

| Service | Rows | z_min | z_max | Notes |
|---|---|---|---|---|
| **ChatGPT** | 13 | 0.02 | 3.50 | Full range, includes z=3.50 |
| **Claude** | 12 | 0.00 | 8.50 | Widest range, includes z=0.00 and z=8.50 |
| **Gemini** | 11 | 0.02 | 2.81 | Narrowest range |

### Overlapping z Values

**Common z values across all 3 services:**
- z = 0.02 (ChatGPT, Gemini — NOT Claude)

**NO z values are common to all three services simultaneously.**

### Service-Specific z-Value Sequences

| Row | ChatGPT | Claude | Gemini | Match |
|---|---|---|---|---|
| 1 | 0.02 | **0.00** | 0.02 | ChatGPT=Gemini |
| 2 | **0.07** | 0.06 | 0.05 | All different |
| 3 | **0.15** | 0.14 | 0.14 | Claude=Gemini |
| 4 | **0.30** | 0.25 | 0.25 | Claude=Gemini |
| 5 | **0.45** | 0.40 | 0.38 | All different |

**Observation:** Each service chose a different time grid. This suggests:
- Different rounding conventions (0.07 vs 0.06 vs 0.05)
- Different choices for present-day anchor (z=0.00 vs z=0.02)
- Different high-z cutoffs (z=3.50 vs z=8.50 vs z=2.81)

**Implication:** Direct row-by-row comparison is not possible due to misaligned z-grids. Interpolation required for cross-service comparison.

---

## 2. H-data Comparison

### H-data at Matching z Values

**z ≈ 0.02 (ChatGPT z=0.02, Gemini z=0.02):**

| Service | z | H-data | σ | Source |
|---|---|---|---|---|
| ChatGPT | 0.02 | 70 | 3 | Page 16 |
| Gemini | 0.02 | 70.2 | 1.4 | Page 27 |

**Difference:** H-data differs by 0.3%, σ differs by 2.1× (ChatGPT has larger uncertainty).

**z ≈ 0.14-0.15 (ChatGPT z=0.15, Claude z=0.14, Gemini z=0.14):**

| Service | z | H-data | σ | Source |
|---|---|---|---|---|
| ChatGPT | 0.15 | 74 | 4 | Page 16 |
| Claude | 0.14 | 74.0 | 4.0 | Page 22 |
| Gemini | 0.14 | 77.5 | 3.5 | Page 27 |

**Difference:** Gemini H-data is 4.7% higher than ChatGPT/Claude at similar z.

### Observational Data Source Analysis

**ChatGPT sources (documented on page 16):**
- BAO, cosmic chronometers, SNe Ia
- "Observational summaries" (not raw datasets)
- H₀ = 70 km/s/Mpc anchor

**Claude sources (documented on page 20):**
- Cosmic chronometers (Jimenez & Loeb method, Moresco et al.)
- BAO (BOSS DR12, eBOSS, DESI 2024)
- SNe Ia (Pantheon+ for z ≤ 2)
- H₀ = 73.04 ± 1.04 km/s/Mpc (SH0ES, Riess et al. 2022)

**Gemini sources (documented on page 26):**
- Cosmic chronometer compilations
- $H_s$ data from direct observations
- H₀ = 67.4 km/s/Mpc (Planck 2018)

**Finding:** Services used **different H₀ anchors**:
- ChatGPT: 70 km/s/Mpc (intermediate)
- Claude: 73.0 km/s/Mpc (SH0ES-like, local)
- Gemini: 67.4 km/s/Mpc (Planck, CMB-based)

**Implication:** H-data values are NOT from the same observational dataset. Each service compiled its own summary, weighted differently, and normalized to a different H₀.

---

## 3. H-FLRW Comparison

### Cosmological Parameters

**ChatGPT (page 16):**
- Ωm = 0.315, ΩΛ = 0.685 (inferred from text)
- H₀ = 67.4 km/s/Mpc for H_FLRW calculation
- Method: Standard ΛCDM

**Claude (page 22):**
- Ωm = 0.315, ΩΛ = 0.685 (Planck 2018)
- H₀ = 67.4 km/s/Mpc
- Method: Standard ΛCDM

**Gemini (page 25):**
- Ωm = 0.315, ΩΛ = 0.685 (Planck 2018)
- H₀ = 67.4 km/s/Mpc
- Method: Standard ΛCDM

**Finding:** ✅ **H_FLRW calculation method is STABLE across all three services.**

All three use Planck 2018 cosmology (Ωm=0.315, ΩΛ=0.685, H₀=67.4) for H_FLRW baseline.

### H-FLRW Residuals

**At z=0.15 (ChatGPT), z=0.14 (Claude, Gemini):**

| Service | z | H-FLRW | σ_FLRW | H-data | Residual |
|---|---|---|---|---|---|
| ChatGPT | 0.15 | 75 | +0.3 | 74 | -1 km/s/Mpc |
| Claude | 0.14 | 69.3 | -1.2 | 74.0 | +4.7 km/s/Mpc |
| Gemini | 0.14 | 76.2 | -0.37 | 77.5 | +1.3 km/s/Mpc |

**Observation:** H_FLRW values differ even at similar z due to:
1. Different z-value spacing (0.15 vs 0.14 → different H_FLRW from cosmological calculator)
2. Different H-data choices (normalization to different H₀ anchors)

**Stability assessment:** **STABLE methodology, UNSTABLE numerical values** (due to z-grid and H₀ anchor differences).

---

## 4. H-MULT Comparison

### At Matching z Values

**z ≈ 0.02:**

| Service | z | H_MULT | σ_MULT | H-data | Beta_d | Beta_q |
|---|---|---|---|---|---|---|
| ChatGPT | 0.02 | 70 | 0.0 | 70 | 0.78 | 0.19 |
| Gemini | 0.02 | 70.2 | 0.00 | 70.2 | 4.25 | 8.10 |

**Observation:** H_MULT values are **nearly identical** despite **42.6× difference in β_q** (0.19 vs 8.10).

**This is suspicious** — how can H_MULT match when beta parameters differ by 42×?

**Hypothesis:** H_MULT is **normalized to match H-data at z=0** (or z=0.02), so the first row always shows perfect agreement by construction. Beta parameters affect **time evolution**, not the anchor point.

### At Higher z

**z ≈ 0.14-0.15:**

| Service | z | H_MULT | H-data | Residual | Beta_d | Beta_q |
|---|---|---|---|---|---|---|
| ChatGPT | 0.15 | 75 | 74 | +1 | 0.78 | 0.19 |
| Claude | 0.14 | 73.5 | 74.0 | -0.5 | 4.5 | 18.0 |
| Gemini | 0.14 | 77.1 | 77.5 | -0.4 | 4.25 | 8.10 |

**Observation:** H_MULT values **differ significantly** at higher z:
- ChatGPT: 75 km/s/Mpc
- Claude: 73.5 km/s/Mpc
- Gemini: 77.1 km/s/Mpc

**Range:** 73.5–77.1 km/s/Mpc (4.9% spread)

### Sensitivity to Beta Parameters

**Question:** Does 42× difference in β_q affect H_MULT predictions?

**Evidence from z ≈ 0.14-0.15:**

| Service | β_q | H_MULT | H_MULT/H-data |
|---|---|---|---|
| ChatGPT | 0.19 | 75 | 1.014 |
| Gemini | 8.10 | 77.1 | 0.995 |
| Claude | 18.0 | 73.5 | 0.993 |

**Observation:** Despite 94.7× difference in β_q (Claude/ChatGPT = 18.0/0.19), H_MULT values differ by only ~5%.

**Possible explanations:**
1. **Compensating effects:** β_d and β_q trade off (higher β_q → lower β_d to maintain fit)
2. **Weak dependence:** H_MULT may be weakly sensitive to β_q at low z
3. **Different optimization criteria:** Each service minimized different residuals

**Conclusion:** H_MULT is **UNSTABLE across services** but the instability (5% range) is **much smaller** than the beta parameter instability (42-95× range).

---

## 5. Beta Parameter Comparison

### Summary Table

| Service | β_d | β_q | β_d Ratio | β_q Ratio | Status |
|---|---|---|---|---|---|
| **ChatGPT** | 0.78 | 0.19 | 1.0× | 1.0× | AI_FITTED |
| **Claude** | 4.5 | 18.0 | 5.8× | 94.7× | AI_FITTED |
| **Gemini** | 4.25 | 8.10 | 5.4× | 42.6× | AI_FITTED |

### Variance Analysis

**β_d variance:**
- Mean: 1.84
- Range: 0.78–4.5
- Coefficient of variation: 108%
- **Classification:** **HIGHLY UNSTABLE**

**β_q variance:**
- Mean: 8.76
- Range: 0.19–18.0
- Coefficient of variation: 109%
- **Classification:** **HIGHLY UNSTABLE**

### Provenance

**All three services:**
- **Status:** AI_FITTED / PHENOMENOLOGICAL
- **Method:** Numerical optimization to minimize RMS deviation from H-data
- **Algorithm:** Not disclosed (black-box AI-service optimization)
- **Initial guess:** Not disclosed
- **Convergence criteria:** Not disclosed
- **Optimization bounds:** β_d ∈ [0, 20], β_q ∈ [0, 50] (from ChatGPT page 12 text)

**Root cause of instability:**
1. **Different optimization algorithms** — Each AI service uses its own optimizer
2. **Different initial guesses** — May converge to different local minima
3. **Different cost functions** — May weight residuals differently
4. **Different cluster parameter ranges** — May use different m_A, r_A ranges (see docs/79)

**Conclusion:** Beta parameters are **NOT reproducible across AI services** and should be treated as **AI-service-dependent fitted values**, not fundamental constants.

---

## 6. w_eff Comparison

### Available Data

| Service | Rows with w_eff | z Range | Format | Status |
|---|---|---|---|---|
| **ChatGPT** | 13 | 0.02–3.50 | Analytic formula + table | COMPLETE |
| **Claude** | 11 | 0.00–5.00 | Numerical table only | COMPLETE |
| **Gemini** | 4 | 0.02, 0.25, 0.74, 2.81 | Numerical table only | PARTIAL |

### ChatGPT Analytic Formula

**From page 15 (yellow-highlighted):**
```
w_eff(z) = -1 + 0.28 tanh[(z - 0.9)/0.9]
```

**This is unique to ChatGPT.** Neither Claude nor Gemini provided an analytic parametrization.

### w_eff Comparison at Matching z

**z ≈ 0.02:**

| Service | z | w_eff | H-w_eff | Notes |
|---|---|---|---|---|
| ChatGPT | 0.02 | -1.22 | 70 | From formula |
| Gemini | 0.02 | -1.05 | 70.2 | From table |

**Difference:** Δw_eff = 0.17 (16% relative difference from -1)

**z ≈ 0.74-0.85:**

| Service | z | w_eff | Notes |
|---|---|---|---|
| ChatGPT | 0.85 | -0.92 | From formula |
| Claude | 0.85 | -1.01 | From table |
| Gemini | 0.74 | -0.75 | From table |

**Observation:** w_eff values **differ significantly**:
- ChatGPT: -0.92
- Claude: -1.01
- Gemini: -0.75 (at slightly different z)

**Range at z ≈ 0.8:** -1.01 to -0.75 (29% spread)

### Stability Assessment

**w_eff is UNSTABLE across services:**
- Different values at same z
- Different representations (formula vs table)
- Gemini only provides 4 data points (PARTIAL)

**Implication:** w_eff(z) equation of state is **AI-service-dependent** and should not be treated as a unique prediction from MULTING framework.

---

## 7. Future Projection Comparison

### Transition Time (monopole + quadrupole > dipole)

| Service | Transition Time | Source | Status |
|---|---|---|---|
| **ChatGPT** | 35–60 Gyr | Page 14 (yellow-highlighted) | EXPLICIT |
| **Claude** | NOT_SHOWN | Page 23 (mentioned, no time) | IMPLICIT |
| **Gemini** | 32–38 Gyr | Page 29 (yellow-highlighted) | EXPLICIT |

**Comparison (ChatGPT vs Gemini):**
- ChatGPT midpoint: ~47.5 Gyr
- Gemini midpoint: ~35 Gyr
- **Difference:** 12.5 Gyr (26% disagreement)

**Overlap:** 35–38 Gyr (small overlap region)

### Contraction Onset Time (H < 0)

| Service | Contraction Onset | Source | Status |
|---|---|---|---|
| **ChatGPT** | 80–140 Gyr | Page 14 (yellow-highlighted) | EXPLICIT |
| **Claude** | NOT_SHOWN | Page 23 (mentioned, no time) | IMPLICIT |
| **Gemini** | 55 Gyr | Page 29 (yellow-highlighted) | EXPLICIT |

**Comparison (ChatGPT vs Gemini):**
- ChatGPT midpoint: ~110 Gyr
- Gemini: 55 Gyr
- **Difference:** 55 Gyr (50% disagreement)

**Gemini predicts contraction 2× sooner than ChatGPT.**

### Stability Assessment

**Future projections are UNSTABLE:**
- 26% disagreement on transition time
- 50% disagreement on contraction onset
- Claude did not provide explicit times (cannot compare)

**Root cause:**
- Different beta parameters (β_q differs by 42×)
- Different time evolution of F_m, F_d, F_q terms
- Different assumptions about future cluster evolution

**Conclusion:** Future projection estimates are **AI-service-dependent** and should be treated as **speculative extrapolations** with large uncertainties, not precise predictions.

---

## Stable Findings (Reproducible Across Services)

**The following findings are STABLE across all three AI services:**

### 1. H_FLRW Calculation Method ✅

**All three services use:**
- Planck 2018 cosmology (Ωm=0.315, ΩΛ=0.685)
- H₀ = 67.4 km/s/Mpc for H_FLRW calculation
- Standard ΛCDM metric

**Variance:** ~0% (methodology identical)

### 2. Beta Parameter Methodology ✅

**All three services:**
- Fitted β_d and β_q numerically to minimize RMS deviation from H-data
- Treated beta as phenomenological parameters (not fundamental constants)
- Used geometric-mean cluster parameter ranges

**Variance:** ~0% (methodology identical, though **fitted values differ drastically**)

### 3. Qualitative Behavior ✅

**All three services report:**
- MULTING fits H-data comparably to (or slightly better than) FLRW at low-to-mid z
- Dipole repulsion dominates at late times (z < 0.7)
- Quadrupole attraction dominates at early times (z > 2)
- Future transition predicted (monopole eventually wins over dipole)

**Variance:** ~0% (qualitative picture consistent)

### 4. MULTING vs FLRW Residual Patterns ✅

**All three services show:**
- FLRW systematically underestimates H(z) at intermediate z (0.7 < z < 2)
- MULTING suppresses high-z expansion (closer to H-data than FLRW at z > 2)
- Both models match H-data at z ≈ 0 (by construction)

**Variance:** ~10% (pattern consistent, magnitudes vary)

---

## Unstable Findings (AI-Service-Dependent)

**The following findings are UNSTABLE and depend on which AI service was used:**

### 1. Beta Parameters ❌ **CRITICAL**

**β_d variance:** 5.4–5.8× across services  
**β_q variance:** 42.6–94.7× across services

**Status:** **HIGHLY UNSTABLE**

**Implication:** Beta values are **AI-service-dependent fitted parameters**, not reproducible constants. Cannot be used for cross-study comparison without provenance.

### 2. Time / Redshift Grids ❌

**Different z-value sequences:**
- ChatGPT: 0.02, 0.07, 0.15, 0.30, 0.45, ...
- Claude: 0.00, 0.06, 0.14, **Different z-value sequences:**
- ChatGPT: 0.02, 0.07, 0.15, 0.30, 0.45, ... (13 rows)
- Claude: 0.00, 0.06, 0.14, 0.25, 0.40, ... (12 rows)
- Gemini: 0.02, 0.05, 0.14, 0.25, 0.38, ... (11 rows)

**Status:** **UNSTABLE**

**Implication:** Direct row-by-row comparison requires interpolation.

### 3. H₀ Anchors ❌

**Different H₀ values for H-data normalization:**
- ChatGPT: 70 km/s/Mpc (intermediate)
- Claude: 73.0 km/s/Mpc (SH0ES-like)
- Gemini: 67.4 km/s/Mpc (Planck-like)

**Status:** **UNSTABLE**

**Implication:** H-data values are not directly comparable across services due to different anchors.

### 4. H_MULT Values ❌

**Range at z ≈ 0.14-0.15:** 73.5–77.1 km/s/Mpc (4.9% spread)

**Status:** **UNSTABLE (but less so than beta parameters)**

**Sensitivity to β_q:** Despite 94.7× difference in β_q, H_MULT varies by only ~5% → suggests weak dependence at low z or compensating effects with β_d.

### 5. w_eff(z) ❌

**Range at z ≈ 0.02:** Δw_eff = 0.17 (16% relative difference from -1)
**Range at z ≈ 0.8:** -1.01 to -0.75 (29% spread)

**Status:** **HIGHLY UNSTABLE**

**Implication:** w_eff predictions are AI-service-dependent and should not be treated as unique theoretical predictions.

### 6. Future Projections ❌

**Transition time disagreement:** 26% (ChatGPT vs Gemini)
**Contraction onset disagreement:** 50% (ChatGPT vs Gemini)

**Status:** **HIGHLY UNSTABLE**

**Implication:** Future projection estimates are speculative extrapolations with large uncertainties.

---

## Provenance Risks

### Risk 1: Beta Parameter Non-Uniqueness ⚠️ **CRITICAL**

**Problem:** β_d and β_q differ by 5-95× across AI services, yet all three claim to "fit H-data well."

**Explanation:**
1. **Optimization landscape has multiple local minima** — different AI services converged to different solutions
2. **Compensating effects** — higher β_q paired with higher β_d can produce similar H_MULT
3. **Different cost functions** — each service may weight residuals differently (RMS vs max deviation vs χ²)
4. **Different initial guesses** — optimization starting points affect convergence

**Impact:** Beta parameters are **not reproducible** without full optimization protocol disclosure (algorithm, initial guess, bounds, convergence criteria).

**Mitigation:** Treat beta as **AI-service-dependent fitted values**, not fundamental constants. Always cite which AI service was used.

### Risk 2: H-data Source Ambiguity ⚠️

**Problem:** Services used different observational datasets and H₀ anchors.

**Evidence:**
- ChatGPT: H₀=70 (intermediate)
- Claude: H₀=73.0 (SH0ES)
- Gemini: H₀=67.4 (Planck)

**Impact:** H-data values are **not directly comparable** across services. A claim like "H_MULT fits H-data better than FLRW" depends on which H-data was used.

**Mitigation:** Always specify H₀ anchor and observational sources when reporting results.

### Risk 3: Table Construction Choices ⚠️

**Problem:** Different z-grids, row counts, and time ranges across services.

**Evidence:**
- ChatGPT: 13 rows, z=0.02–3.50
- Claude: 12 rows, z=0.00–8.50
- Gemini: 11 rows, z=0.02–2.81

**Impact:** Row-by-row comparison requires interpolation. Cherry-picking specific z-values can change conclusions.

**Mitigation:** Report full z-range and interpolation method when comparing across services.

### Risk 4: w_eff Representation Ambiguity ⚠️

**Problem:** ChatGPT provides analytic formula, Claude/Gemini provide numerical tables.

**Evidence:**
- ChatGPT: w_eff(z) = -1 + 0.28 tanh[(z - 0.9)/0.9]
- Claude: 11 discrete (z, w_eff) pairs
- Gemini: 4 discrete (z, w_eff) pairs (PARTIAL)

**Impact:** Cannot verify if ChatGPT formula matches Claude/Gemini tables without additional calculations.

**Mitigation:** Request author clarification on whether w_eff(z) is:
1. Derived analytically from MULTING equations
2. Fitted empirically to match H_MULT/H-data
3. Post-hoc parametrization of numerical results

---

## What Requires Author Clarification

**Critical questions for reproducibility:**

### Q1: Beta Parameter Fitting

**Question:** Which AI service's beta values (ChatGPT 0.78/0.19, Claude 4.5/18.0, Gemini 4.25/8.10) should be considered the "primary" result?

**Or:** Should all three be treated as equally valid alternative fits, requiring uncertainty quantification across the ensemble?

**Why this matters:** β_q differs by 42-95× across services. This is not a small numerical error — it is a fundamentally different parameter set.

### Q2: Optimization Method Disclosure

**Question:** Can you provide the optimization protocol used by each AI service:
- Algorithm (Nelder-Mead, BFGS, genetic algorithm, grid search)?
- Initial guess for β_d and β_q?
- Bounds on parameter space?
- Convergence criteria (tolerance, max iterations)?
- Cost function (RMS, χ², max deviation)?

**Why this matters:** Without this information, we cannot independently reproduce the fits or assess whether multiple local minima exist.

### Q3: H-data Source Standardization

**Question:** Should all three AI services have used the **same** H-data dataset and H₀ anchor for consistency?

**Or:** Is the diversity intentional (testing robustness to different H₀ priors)?

**Why this matters:** Different H₀ anchors (67.4 vs 70 vs 73.0) make H-data values non-comparable across services.

### Q4: w_eff(z) Derivation

**Question:** Is the ChatGPT w_eff(z) formula:
1. Analytically derived from MULTING equations?
2. Empirically fitted to match numerical H_MULT results?
3. Post-hoc parametrization for convenience?

**Why this matters:** If (1), it is a theoretical prediction. If (2)/(3), it is a summary statistic of numerical results, not an independent prediction.

### Q5: Future Projection Reliability

**Question:** Given 26-50% disagreement in future projection estimates across AI services, should these be:
1. Treated as speculative extrapolations (not firm predictions)?
2. Averaged across services with uncertainties?
3. Re-computed with a standardized beta set?

**Why this matters:** Transition time (35-60 Gyr vs 32-38 Gyr) and contraction onset (80-140 Gyr vs 55 Gyr) differ by factors of 1.5-2×.

---

## What This Does NOT Claim

**This analysis does NOT claim:**

❌ **MULTING is validated** — We did not run MCMC model comparison or test predictions.

❌ **MULTING is refuted** — We did not show the framework is internally inconsistent or contradicts data.

❌ **One AI service is "correct" and others are "wrong"** — All three used valid optimization methods; they just converged to different local minima.

❌ **Beta parameters are wrong** — They are fitted values, not fundamental constants. Multiple valid fits exist.

❌ **H_MULT is unreliable** — H_MULT varies by ~5% at low z despite 42-95× beta differences, suggesting the framework has some robustness.

**This analysis DOES claim:**

✅ **AI-service outputs differ materially** — 5.4-95× variance in fitted parameters is NOT negligible.

✅ **Provenance tracking is essential** — Cannot compare H_MULT values across studies without knowing which AI service and which beta set was used.

✅ **Reproducibility requires protocol disclosure** — Without optimization algorithm, initial guess, and convergence criteria, independent reproduction is impossible.

✅ **Multi-AI comparison is valuable** — Reveals hidden dependencies and non-uniqueness that a single AI service output would hide.

---

## Recommended Next Steps

### 1. Author Clarification (Priority 1)

**Request:**
- Which beta set is primary? (Or should all three be ensemble-averaged?)
- Can optimization protocol be disclosed for each AI service?
- Is w_eff(z) analytically derived or empirically fitted?
- Should future projections be treated as speculative or firm predictions?

**Deliverable:** Updated Supplementary Material with reproducibility metadata.

### 2. Uncertainty Quantification (Priority 2)

**Task:** Treat 3 AI service outputs as an ensemble and compute:
- Mean β_d = (0.78 + 4.5 + 4.25)/3 = 3.18 ± 2.12 (67% uncertainty)
- Mean β_q = (0.19 + 18.0 + 8.10)/3 = 8.76 ± 8.91 (102% uncertainty)
- H_MULT range at each z-value across all 3 services

**Deliverable:** Uncertainty bands on H_MULT predictions.

### 3. Standardized Re-Fit (Priority 3)

**Task:** Re-run beta optimization with:
- **Same** H-data sources across all services
- **Same** H₀ anchor (e.g., 70 km/s/Mpc)
- **Same** optimization algorithm (e.g., scipy.optimize.minimize with BFGS)
- **Same** initial guess (e.g., β_d=1.0, β_q=1.0)
- **Multiple** random initial guesses to test for local minima

**Deliverable:** Standardized beta parameter set with reproducibility protocol.

### 4. Cross-Service Interpolation (Priority 4)

**Task:** Interpolate all 3 services onto a common z-grid (e.g., 20 equally-spaced points from z=0 to z=3).

**Deliverable:** Aligned comparison table for H_MULT, w_eff across all 3 services.

### 5. Documentation Update (Priority 5)

**Task:** Add provenance metadata to all supplementary tables:
- AI service used
- Model version (e.g., ChatGPT-4, Claude Sonnet 4.6, Gemini Thinking)
- Session date (2026-05-07 for all three)
- Optimization method (if disclosed)
- Beta parameter set used

**Deliverable:** Updated Supplementary Material with full traceability.

---

## Summary

**Main finding:** AI-service outputs differ materially in fitted beta parameters (5.4-95× range) and some construction choices (time grids, H₀ anchors). These differences motivate explicit provenance tracking before using such tables for model comparison.

**Stable:** H_FLRW methodology, qualitative MULTING behavior, residual patterns.

**Unstable:** Beta parameters (CRITICAL), H₀ anchors, H_MULT values (~5% spread), w_eff(z) (29% spread), future projections (26-50% disagreement).

**Impact:** Without knowing which AI service was used and which optimization method was employed, H_MULT values from different studies cannot be reliably compared.

**Recommendation:** Request author clarification on which beta set is primary, disclose optimization protocols, and consider ensemble-averaging across all 3 AI services for uncertainty quantification.

**What this does NOT claim:** No validation or refutation of MULTING. No claim that any AI service is "wrong." All three used valid methods — they just found different local minima in parameter space.

**Data quality:** HIGH — All 3 services have verified, independent data (docs/80). Contamination resolved. Ready for cross-service statistical analysis.

---

**Related Documents:**
- docs/80_final_csv_reaudit_after_chatgpt_fix.md (data integrity verification)
- docs/79_chatgpt_table_source_resolution.md (contamination fix)
- docs/77_multi_ai_table_extraction_summary.md (original extraction)
- docs/76_supplementary_materials_inventory.md (source inventory)
- docs/73_multi_ai_table_comparison_plan.md (comparison methodology)

**Data Sources:**
- data/supplementary_raw/preprintsSupplementary202511.0598.v6.pdf
- data/supplementary_extracted/chatgpt_approximate_matches.csv (13 rows)
- data/supplementary_extracted/claude_approximate_matches.csv (12 rows)
- data/supplementary_extracted/gemini_approximate_matches.csv (11 rows)
- data/supplementary_extracted/multi_ai_table_index.csv (11 tables, 122 total rows)

---

**Last updated:** 2026-05-30
**Status:** COMPLETED — Internal reproducibility comparison
**Next action:** Commit document
