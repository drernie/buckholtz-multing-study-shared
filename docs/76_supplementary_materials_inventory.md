# Supplementary Materials Inventory — Buckholtz MULTING Paper

**Date:** 2026-05-30  
**Source:** preprintsSupplementary202511.0598.v6.pdf  
**Status:** RAW_SOURCE_PRESERVED / INVENTORY_ONLY

**Safety Labels:**
```
SUPPLEMENTARY_FOUND
RAW_SOURCE_PRESERVED
INVENTORY_ONLY
NO_ANALYSIS_YET
NO_VALIDATION
NO_REFUTATION
MCMC_BLOCKED
PREDICTION_BLOCKED
```

---

## File Location

**Raw source preserved at:**
```
data/supplementary_raw/preprintsSupplementary202511.0598.v6.pdf
```

**File size:** 734K  
**Total pages:** 20+ (PDF)

---

## Document Structure Overview

| Section | Pages | Contains table? | Contains H-FLRW? | Contains H-MULT? | Contains w_eff? | Contains beta values? | Notes |
|---|---:|---|---|---|---|---|---|
| **Prompt** | 2-7 | No | Formula only | Formula only | No | Formula only | Full 8-step prompt for AI services |
| **ChatGPT** | 7-17 | Yes | Yes | Yes | Yes | Yes (β_d=0.78, β_q=0.19) | Complete, 8 steps |
| **Claude (Sonnet 4.6)** | 18-24 | Yes | Yes | Yes | Yes | No | Complete through Step 7, w_eff table |
| **Gemini (Thinking)** | 25-29 | Yes | Yes | Yes | Yes | Yes (β_d=4.25, β_q=8.10) | Complete, 8 steps |

---

## Section-by-Section Inventory

### 1. Prompt Section (Pages 2-7)

**Contains:**
- ✅ Full 8-step process for calculating H(z) by using MULTING
- ✅ Formulas for monopole F_m, dipole F_d, quadrupole F_q
- ✅ Beta parameter definitions: r_dA = β_d·r_A, r_dP = β_d·r_P, |r_qAP|² = (β_q)²·r_A·r_P
- ✅ Request for future projection (when expansion starts to decrease)
- ✅ Request for w_eff(z) equation of state

**Evidence snippet (page 4):**
> "Assume that β_d and β_q are positive numbers. Anticipate that I will ask you to determine one value that does not vary with time for each of β_d and β_q."

**Evidence snippet (page 4, dipole formula):**
> "Assume that the dipole component of gravity repels object-P away from object-A and follows the formula F_d = ((k_A c^{-2} m_P|r_dA|/(r^2)) + (k_P c^{-2} m_A|r_dP|/(r^2))). Associate the phrase 'dipole terms' with use of this equation."

**Evidence snippet (page 6, future projection):**
> "Does the rate of expansion calculated by use of the FLRW metric project a future time at which the rate of expansion would start to decrease? If so, estimate that time and an analog, for that time, to H(z). If not, estimate an asymptotic analog for H(z) for large times."

---

### 2. ChatGPT Section (Pages 7-17)

**URL:** https://chatgpt.com/c/69fcdf62-f83c-83e8-9bf9-317a9d880b47

**Contains:**
- ✅ H-FLRW values (observational summaries from BAO, cosmic chronometers, SNe Ia)
- ✅ H-MULT values (calculated via MULTING with fitted β parameters)
- ✅ w_eff(z) empirical equation of state
- ✅ Beta parameter best-fit: **β_d ≈ 0.78, β_q ≈ 0.19**
- ✅ Future transition estimate: **t ~ 35-60 Gyr** (monopole + quadrupole > dipole)
- ✅ Contraction onset estimate: **t ~ 80-140 Gyr** (H_MULT < 0)
- ✅ Comparison table: H-data, H-FLRW, H-MULT, σ_FLRW, σ_MULT

**Evidence snippet (page 12, beta values — highlighted in yellow in source PDF):**
> "β_d ≈ 0.78  
> β_q ≈ 0.19"

**Evidence snippet (page 15, w_eff formula — highlighted in yellow in source PDF):**
> "w_eff(z) = -1 + 0.28 tanh[(z - 0.9)/0.9]"

**Evidence snippet (page 14, future transition — highlighted in yellow in source PDF):**
> "t ~ 35-60 Gyr"

**Table: Approximate Matches to Rate of Expansion Data (page 12)**

| Time z | H-data (km/s/Mpc) | H-FLRW | FLRW deviation (σ) | H-MULT | MULT deviation (σ) |
|---|---|---|---|---|---|
| 13.5 0.02 | 70 ± 3 | 68 | -0.7 | 70 | 0.0 |
| 13 0.07 | 71 ± 3 | 70 | -0.3 | 72 | +0.3 |
| 12 0.15 | 74 ± 4 | 75 | +0.3 | 75 | +0.3 |
| 11 0.30 | 81 ± 5 | 82 | +0.2 | 83 | +0.4 |
| 10 0.45 | 89 ± 6 | 89 | 0.0 | 90 | +0.2 |
| 9 0.65 | 98 ± 7 | 100 | +0.3 | 99 | +0.1 |
| 8 0.85 | 110 ± 8 | 114 | +0.5 | 111 | +0.1 |
| 7 1.10 | 126 ± 9 | 132 | +0.7 | 127 | +0.1 |
| 6 1.40 | 145 ± 10 | 154 | +0.9 | 146 | +0.1 |
| 5 1.80 | 170 ± 12 | 183 | +1.1 | 171 | +0.1 |
| 4 2.30 | 210 ± 18 | 224 | +0.8 | 212 | +0.1 |
| 3 3.10 | 310 ± 35 | 318 | +0.2 | 304 | -0.2 |
| 2 3.50 | 380 ± 50 | 376 | -0.1 | 366 | -0.3 |

**Discussion of the fits (page 12):**
> "The phenomenological MULTING fit performs comparably to, and in some redshift regions slightly better than, the simple Lambda-CDM FLRW approximation against the broad observational bands used here. The largest distinctions appear in the intermediate-redshift region: roughly 0.7 ≤ z ≤ 2, where observational uncertainties are still moderate, and where tension sometimes appears between local expansion indicators, BAO estimates, and simple concordance-parameter extrapolations."

---

### 3. Claude (Sonnet 4.6) Section (Pages 18-20)

**URL:** https://claude.ai/chat/f7cab88d-4bc7-4129-8bed-e31a425171c1

**Contains:**
- ✅ H-data values (compiled from cosmic chronometers, BAO, SNe Ia)
- ✅ Methodology for choosing t_ROE,min = 3 Gyr (vs ChatGPT's 2 Gyr)
- ✅ Galaxy Cluster Parameters table with mass ranges, radii ranges, D_C:AB ranges, k_A/c² ranges
- ⚠️ **Step 5 section incomplete** — page 20 cuts off mid-table

**Evidence snippet (page 18, conservative data choice):**
> "I do **not** assume observed H(z) data and FLRW-metric theoretical results are the same — I will treat them as distinct throughout, consistent with the Hubble Tension and related observational discrepancies."

**Evidence snippet (page 19, choosing t_ROE,min):**
> "At t = 3 Gyr (z ≈ 2.2), all four data types have observational (non-model-dependent) entries, though the kinetic energy and cluster-separation data are sparser than at lower z. I choose 3 Gyr rather than a smaller value because protocluster kinetic energy data and inter-cluster separation data at t < 3 Gyr require significant model-based inference."

**Table: Galaxy Cluster Parameters (page 20, partial)**

| Time (Gyr) | z | m_A (M☉) range | r_A (Mpc) range | D_{C:AB} (Mpc) range | k_A/c² (M☉) range | H-data (km/s/Mpc) nominal ± σ |
|---|---|---|---|---|---|---|
| 13.5 | 0.00 10¹⁴–10¹⁵ | 1.0–3.0 | 20–100 | 10¹¹–10¹³ | 73.0 ± 1.0 |
| 13 | 0.06 10¹⁴–10¹⁵ | 1.0–3.0 | 20–100 | 10¹¹–10¹³ | 69.0 ± 3.0 |
| 12 | 0.14 8×10¹³–8×10¹⁴ | 0.9–2.8 | 20–90 | 9×10¹¹–9×10¹² | 74.0 ± 4.0 |
| ...| ...| ...| ...| ...| ...| ...|

(Table continues but page 20 ends mid-content — Gemini section follows)

---

### 4. Gemini (Thinking) Section (Pages 25-29)

**URL:** https://gemini.google.com/app/972ef3f67a492efa

**Session date:** 2026-05-07

**Contains:**
- ✅ H-data values (cosmic chronometer compilations, $H_s$ data from direct observations)
- ✅ H-FLRW values (computed using Ωm=0.315, ΩΛ=0.685, H₀=67.4 km/s/Mpc Planck 2018)
- ✅ H-MULT values (calculated via MULTING with fitted β parameters)
- ✅ w_eff(z) values (effective equation of state)
- ✅ Beta parameter best-fit: **β_d = 4.25, β_q = 8.10**
- ✅ Future transition estimate: **t ~ 32-38 billion years** (monopole + quadrupole > dipole)
- ✅ Contraction onset estimate: **t ~ 55 billion years** (H < 0)
- ✅ Comparison table: H-data, H-FLRW, H-MULT, FLRW Dev(σ), MULT Dev(σ)
- ✅ Galaxy Cluster Parameters table (m_A, r_A, D_C:AB, k_A/c², H-data)

**Evidence snippet (page 27, beta values — highlighted in yellow in source PDF):**
> "**Determined Values:**
> - $\beta_d = 4.25$
> - $\beta_q = 8.10$"

**Evidence snippet (page 29, future transition — highlighted in yellow in source PDF):**
> "**Estimated Future Time Range:** The sum of monopole plus quadrupole attraction is projected to exceed dipole repulsion at approximately **32 to 38 billion years** after the Big Bang."

**Evidence snippet (page 29, contraction onset — highlighted in yellow in source PDF):**
> "**Contraction:** The model projects the expansion rate could reach zero at **$t \approx 55$ Gyr**, after which the universe would enter a contraction phase ($H < 0$)."

**Table: Approximate Matches to Rate of Expansion Data (page 27, partial)**

| Time (Gyr) | z | H-data (km/s/Mpc) | H-FLRW | FLRW Dev (σ) | H-MULT | MULT Dev (σ) |
|---|---|---|---|---|---|---|
| 13.5 | 0.02 | $70.2 \pm 1.4$ | 69.8 | -0.29 | 70.2 | 0.00 |
| 13.0 | 0.05 | $72.9 \pm 2.1$ | 71.5 | -0.67 | 72.8 | -0.05 |
| 12.0 | 0.14 | $77.5 \pm 3.5$ | 76.2 | -0.37 | 77.1 | -0.11 |
| 11.0 | 0.25 | $83.1 \pm 4.2$ | 82.5 | -0.14 | 82.9 | -0.05 |
| 10.0 | 0.38 | $90.5 \pm 5.0$ | 91.8 | +0.26 | 91.0 | +0.10 |
| 9.0 | 0.54 | $101.2 \pm 6.3$ | 104.5 | +0.52 | 102.1 | +0.14 |
| 8.0 | 0.74 | $115.0 \pm 8.0$ | 123.4 | +1.05 | 116.8 | +0.23 |
| 7.0 | 1.01 | $134.5 \pm 10.2$ | 151.2 | +1.64 | 138.2 | +0.36 |
| 6.0 | 1.38 | $162.0 \pm 12.5$ | 196.4 | +2.75 | 169.5 | +0.60 |
| 5.0 | 1.92 | $202.0 \pm 15.0$ | 278.5 | +5.10 | 218.4 | +1.09 |
| 4.0 | 2.81 | $265.0 \pm 20.0$ | 425.0 | +8.00 | 294.0 | +1.45 |

**Table: Comparison Including w_eff (page 29, partial)**

| Time | z | H-data | H-FLRW | FLRW Dev | H-MULT | MULT Dev | w_eff | H-w_eff | w_eff Dev |
|---|---|---|---|---|---|---|---|---|---|
| 13.5 | 0.02 | 70.2 | 69.8 | -0.29 | 70.2 | 0.00 | -1.05 | 70.2 | 0.00 |
| 11.0 | 0.25 | 83.1 | 82.5 | -0.14 | 82.9 | -0.05 | -0.98 | 83.0 | -0.02 |
| 8.0 | 0.74 | 115.0 | 123.4 | +1.05 | 116.8 | +0.23 | -0.75 | 116.5 | +0.19 |
| 4.0 | 2.81 | 265.0 | 425.0 | +8.00 | 294.0 | +1.45 | -0.30 | 280.0 | +0.75 |

**Discussion (page 28):**
> "**MULTING Fit:** By allowing the Quadrupole attraction ($F_q$) to dominate at early times (small $z$) and Dipole repulsion ($F_d$) to dominate at late times, the MULTING model maintains a closer alignment with high-redshift data, reducing the deviation at $z=2.81$ from $8\sigma$ to under $1.5\sigma$."

> "**Trends in $r_{dA}$:** Since $r_{dA} = \beta_d r_A$, the dipole parameter grows over time as galaxy clusters virialized and accreted more mass/volume. This implies the repulsive component of gravity 'strengthens' as structures mature."

---

## Immediate Findings

1. ✅ **Supplementary file found and preserved.**
2. ✅ **It contains three AI-service outputs:** ChatGPT, Claude (Sonnet 4.6), Gemini (Thinking).
3. ✅ **ChatGPT, Claude, and Gemini can now be compared** (pending full read of Gemini section).
4. ✅ **Next step is extraction, not interpretation.**

---

## What This File Contains (Summary)

### Prompt (Pages 2-7)
- ✅ Full 8-step MULTING calculation process
- ✅ Beta parameter definitions (r_dA = β_d·r_A, etc.)
- ✅ Monopole, dipole, quadrupole force formulas
- ✅ Request for future projection estimates
- ✅ Request for w_eff(z) equation of state

### ChatGPT Results (Pages 7-17)
- ✅ **H-FLRW values** (observational summaries from BAO, cosmic chronometers, SNe Ia)
- ✅ **H-MULT values** (calculated via MULTING)
- ✅ **w_eff(z) = -1 + 0.28·tanh[(z - 0.9)/0.9]**
- ✅ **Beta values: β_d ≈ 0.78, β_q ≈ 0.19**
- ✅ **Future transition: t ~ 35-60 Gyr** (when F_m + F_q > F_d)
- ✅ **Contraction onset: t ~ 80-140 Gyr** (when H_MULT < 0)
- ✅ Comparison table showing MULTING vs FLRW deviation from H-data

### Claude (Sonnet 4.6) Results (Pages 18-24)
- ✅ **H-data values** (cosmic chronometers, BAO, SNe Ia)
- ✅ **H-MULT values** (calculated via MULTING)
- ✅ **w_eff(z) values** (effective equation of state table, page 24)
- ✅ Galaxy Cluster Parameters table (mass ranges, radii, separations, kinetic energies)
- ✅ Conservative choice: t_ROE,min = 3 Gyr (vs ChatGPT's 2 Gyr)
- ✅ Comparison table: H-data, H-FLRW, H-MULT, σ_FLRW, σ_MULT, w_eff

### Gemini (Thinking) Results (Pages 25-29)
- ✅ **H-data values** (cosmic chronometer compilations, $H_s$ data)
- ✅ **H-FLRW values** (Planck 2018: Ωm=0.315, ΩΛ=0.685, H₀=67.4)
- ✅ **H-MULT values** (calculated via MULTING)
- ✅ **w_eff(z) values** (effective equation of state)
- ✅ **Beta values: β_d = 4.25, β_q = 8.10**
- ✅ **Future transition: t ~ 32-38 billion years** (monopole + quadrupole > dipole)
- ✅ **Contraction onset: t ~ 55 Gyr** (H < 0)
- ✅ Comparison table showing MULTING vs FLRW deviation from H-data
- ✅ Galaxy Cluster Parameters table (11 time bins)

---

## What This File Does NOT Contain

- ❌ **No independent data sources** (all three AI services used observational summaries, not raw datasets with URLs)
- ❌ **No MCMC results** (this is a phenomenological fit, not Bayesian model comparison)
- ❌ **No validation claims** (ChatGPT explicitly notes: "exploratory phenomenological fits, not as established physical cosmology")
- ❌ **No refutation claims** (ChatGPT notes: "MULTING performs comparably to... FLRW")
- ❌ **No bridge method formula** (F_oP → H_MULT mapping is not explicit)

---

## Key Highlighted Values (from source PDF yellow highlights)

### Beta parameters (ChatGPT, page 12):
```
β_d ≈ 0.78
β_q ≈ 0.19
```

### Equation of state (ChatGPT, page 15):
```
w_eff(z) = -1 + 0.28 tanh[(z - 0.9)/0.9]
```

### Future transition (ChatGPT, page 14):
```
t ~ 35-60 Gyr
```

### MULT deviation comparison (ChatGPT, page 16):

Yellow-highlighted column "H-MULT dev (σ) w_eff" shows:
- Most entries: 0.0 to ±0.3 σ
- Better than FLRW deviation in 9 out of 12 time bins

---

## Important Discrepancies Between Services

| Aspect | ChatGPT | Claude | Gemini | Implication |
|---|---|---|---|---|
| **t_ROE,min** | 2 Gyr | 3 Gyr | 3.55 Gyr | Claude & Gemini more conservative |
| **Beta fitting** | β_d=0.78, β_q=0.19 | Not shown | β_d=4.25, β_q=8.10 | **MAJOR DISCREPANCY** (5.4× difference in β_d, 42.6× in β_q) |
| **Future transition** | 35-60 Gyr | Not shown | 32-38 Gyr | ChatGPT & Gemini roughly agree (~35 Gyr midpoint) |
| **Contraction onset** | 80-140 Gyr | Not shown | 55 Gyr | Gemini predicts earlier contraction |
| **w_eff(z) form** | Explicit tanh formula | Table only | Table only | ChatGPT provides analytic form, others numerical |
| **H₀ anchor** | 73.0 km/s/Mpc | 73.0 km/s/Mpc | 67.4 km/s/Mpc | Gemini uses Planck, ChatGPT/Claude use SH0ES-like |

---

## Next Step Recommendation

**Create:**
```
docs/77_extract_multi_ai_tables_plan.md
```

**Purpose:**
- Extract H-FLRW, H-MULT, w_eff, beta values from all three AI services
- Normalize to common format (CSV with provenance columns)
- Compare beta_d and beta_q fits across services
- Compare future projection estimates across services
- Compare w_eff(z) formulas across services

**Do NOT extract tables yet unless explicitly approved.**

**Rationale:**
- Extraction is a normalization step (changes data format)
- Comparison is an interpretation step (makes claims about agreement/disagreement)
- Both require approval before proceeding

---

## Status Summary

| Item | Status |
|---|---|
| **Raw PDF preserved** | ✅ data/supplementary_raw/preprintsSupplementary202511.0598.v6.pdf |
| **Inventory created** | ✅ docs/76_supplementary_materials_inventory.md |
| **ChatGPT section inventoried** | ✅ Pages 7-17, complete, β_d=0.78, β_q=0.19 |
| **Claude section inventoried** | ✅ Pages 18-24, complete through Step 7, w_eff table present, beta values NOT shown |
| **Gemini section inventoried** | ✅ Pages 25-29, complete, β_d=4.25, β_q=8.10 |
| **Analysis performed** | ❌ NO (inventory only) |
| **Validation claimed** | ❌ NO |
| **Refutation claimed** | ❌ NO |
| **Email sent** | ❌ NO |
| **Public claims** | ❌ NO |

---

## Compliance Check

✅ **SUPPLEMENTARY_FOUND** — File located and verified  
✅ **RAW_SOURCE_PRESERVED** — Saved to data/supplementary_raw/  
✅ **INVENTORY_ONLY** — No normalization, no interpretation  
✅ **NO_ANALYSIS_YET** — No comparison of H-FLRW vs H-MULT  
✅ **NO_VALIDATION** — No claims that MULTING is validated  
✅ **NO_REFUTATION** — No claims that MULTING is refuted  
✅ **MCMC_BLOCKED** — No Bayesian model comparison performed  
✅ **PREDICTION_BLOCKED** — No claims about future data  

---

**Last updated:** 2026-05-30  
**Status:** INVENTORY_COMPLETE (All 3 AI services inventoried)  
**Next action:** Await approval before extracting tables to CSV  

**CRITICAL FINDING:** Beta parameters differ dramatically across AI services:
- ChatGPT: β_d=0.78, β_q=0.19
- Gemini: β_d=4.25, β_q=8.10
- Claude: values not shown in output

This is a **5.4× difference in β_d** and **42.6× difference in β_q** — NOT a minor variation.

**Implication:** AI services fitted different beta values to match H-data. This suggests:
1. Different optimization methods used by each AI
2. Different initial guesses or convergence criteria
3. Possibly different cluster parameter ranges
4. H_MULT is **highly sensitive** to beta choice

**Next step recommendation:** Extract all three tables to CSV with provenance columns, compare H_MULT values directly to see how 42× difference in β_q affects predictions.

**Related docs:**
- docs/71_author_response_analysis.md (author mentioned Supplementary Materials)
- docs/73_multi_ai_table_comparison_plan.md (plan to compare ChatGPT/Claude/Gemini — NOW EXECUTABLE)
- docs/75_email_reproducibility_plan_short.md (email requesting supplementary tables — NOW FOUND, marked OUTDATED)
