# BETA-1 Standardized Prompt — v1

**Date:** 2026-06-13  
**Gate:** BETA-1 — controlled AI β replication  
**Version:** v1 (DO NOT MODIFY — changes invalidate controlled condition)  
**Labels:** BETA-1 · AI_CONVERGENCE_TEST · OUR_RECONSTRUCTION

---

## Instructions for deploying this prompt

1. Use this EXACT prompt text with EACH AI service (ChatGPT-4o, Gemini 1.5 Pro, Claude 3.5).
2. Start a FRESH conversation — do NOT continue from a prior session.
3. Paste the Galaxy Cluster Parameters table below as part of the prompt.
4. Record the AI service's reported β_d and β_q values in the response template.
5. Do NOT hint at expected values or BETA-0 results.

---

## Prompt text (paste verbatim)

---

I am studying a cosmological framework called MULTING that uses monopole, dipole, and quadrupole components of gravity from galaxy clusters. I need your help fitting two scaling parameters.

**Galaxy Cluster Parameters table** (Table 4a — standardized, single-valued):

| Time (Gyr) | z | m_A (M_sun) | r_A (Mpc) | D_{C:AB} (Mpc) | k_A/c² (M_sun) | H-data (km/s/Mpc) | σ_H |
|------------|---|-------------|-----------|-----------------|-----------------|---------------------|-----|
| 13.0 | 0.06 | 3.2×10¹⁴ | 2.0 | 45 | 1.0×10¹² | 69.0 | 3.0 |
| 12.0 | 0.14 | 2.5×10¹⁴ | 1.9 | 42 | 2.8×10¹² | 74.0 | 4.0 |
| 11.0 | 0.25 | 1.9×10¹⁴ | 1.7 | 39 | 2.2×10¹² | 79.0 | 4.5 |
| 10.0 | 0.40 | 1.3×10¹⁴ | 1.5 | 35 | 1.6×10¹² | 82.0 | 5.0 |
| 9.0 | 0.65 | 6.3×10¹³ | 1.2 | 29 | 9.5×10¹¹ | 92.0 | 7.0 |
| 8.0 | 1.00 | 3.2×10¹³ | 1.0 | 25 | 3.2×10¹¹ | 105.0 | 8.0 |
| 7.0 | 1.50 | 1.6×10¹³ | 0.8 | 20 | 1.6×10¹¹ | 125.0 | 15.0 |
| 6.0 | 2.10 | 6.3×10¹² | 0.6 | 16 | 6.3×10¹⁰ | 150.0 | 20.0 |
| 5.0 | 3.20 | 1.6×10¹² | 0.5 | 12 | 1.6×10¹⁰ | 195.0 | 30.0 |
| 4.0 | 5.00 | 3.2×10¹¹ | 0.3 | 9 | 3.2×10⁹ | 270.0 | 50.0 |
| 3.0 | 8.50 | 9.5×10¹⁰ | 0.2 | 7 | 9.5×10⁸ | 420.0 | 90.0 |

**Your task (Appendix A.1, Step 5 verbatim):**

How well can you fit (by using my monopole, dipole, and quadrupole components of gravity) the data (in the Galaxy Cluster Parameters table) about the observed rate of expansion of the universe? In doing this work, use the formulas r_dA = β_d r_A, r_dP = β_d r_P, and |r_qAB|² = (β_q)² r_A r_P. Try to choose positive values for β_d and β_q that minimize the standard-deviations away from the nominal values of observed H(z). Provide a table, named 'Approximate Matches to Rate of Expansion Data', with columns: Time, z, H-data, H-FLRW, σ_FLRW, H-MULT, σ_MULT. Try to avoid using outputs from uses of the FLRW metric or other Lambda-CDM models.

**Please also state explicitly:**
- The value of β_d you chose
- The value of β_q you chose
- Brief explanation of how you chose them

---

## Notes for the analyst

- Record β_d and β_q from each AI service response in `response_template.csv`
- Create one file per service: `chatgpt_response.csv`, `gemini_response.csv`, `claude_response.csv`
- The Galaxy Cluster Parameters table above is IDENTICAL across all services (controlled condition)
- The prompt text is IDENTICAL across all services (controlled condition)
- The ONLY variable is the AI service's internal fitting methodology
