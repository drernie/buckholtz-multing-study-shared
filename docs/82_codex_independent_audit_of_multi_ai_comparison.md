# Codex Independent Audit of Multi-AI Comparison

**Date:** 2026-05-30
**Scope:** Independent audit of `docs/81_multi_ai_reproducibility_comparison.md` against `docs/80_final_csv_reaudit_after_chatgpt_fix.md` and `data/supplementary_extracted/`.
**Status:** INTERNAL_AUDIT_ONLY

**Safety labels:**
```
CODEX_INDEPENDENT_AUDIT
INTERNAL_ANALYSIS_ONLY
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
NO_EMAIL_SENT
```

## Executive Verdict

`docs/81_multi_ai_reproducibility_comparison.md` is **partly numerically accurate** but **not safe to use without revision**.

The beta values and beta ratios are mostly correct. The row-count and z-grid summaries are mostly correct. However, the strongest problem is the repeated claim that the H_FLRW methodology is stable or identical across services. That claim is **not supported by the CSV values** and should be downgraded to a warning or open issue.

`docs/81` is safe as **internal scratch analysis after edits**, but it is **not safe to share with Dr. Buckholtz in current form**. It contains overclaims about stable methodology, qualitative consistency, valid methods, and possible local minima that are not established by the CSVs.

## Evidence Read

[VERIFIED] Files read:
- `docs/81_multi_ai_reproducibility_comparison.md`
- `docs/80_final_csv_reaudit_after_chatgpt_fix.md`
- `data/supplementary_extracted/chatgpt_approximate_matches.csv`
- `data/supplementary_extracted/claude_approximate_matches.csv`
- `data/supplementary_extracted/gemini_approximate_matches.csv`
- `data/supplementary_extracted/chatgpt_weff_comparison.csv`
- `data/supplementary_extracted/claude_weff_comparison.csv`
- `data/supplementary_extracted/gemini_weff_comparison.csv`
- `data/supplementary_extracted/chatgpt_recap_parameters.csv`
- `data/supplementary_extracted/claude_recap_parameters.csv`
- `data/supplementary_extracted/gemini_recap_parameters.csv`
- `data/supplementary_extracted/multi_ai_table_index.csv`

[VERIFIED] I did not edit `docs/81`, did not send email, did not make public claims, did not validate or refute MULTING, and did not run MCMC.

## Section Verdicts

| docs/81 section | Verdict | Reason |
|---|---|---|
| Executive summary | WARN | Beta ranges are correct, but "stable H-FLRW calculation methods" is not supported by CSV values. |
| Service metadata | PASS | Matches table index and recap files at the level audited. |
| Time / redshift grid | PASS | Row counts and z-ranges match CSVs. Wording should say "no exact z common to all three"; z=0.02 is common only to ChatGPT/Gemini. |
| H-data comparison | WARN | CSV values support different H-data and anchors, but exact source/normalization claims require PDF/source-text support beyond CSVs. |
| H-FLRW comparison | FAIL | The claim that all three use the same Planck 2018 H0=67.4 method is contradicted or at least not supported by CSV values. |
| H-MULT comparison | WARN | Table values support service differences, but causal/sensitivity explanations are hypotheses, not findings. |
| Beta parameter comparison | WARN | Beta values and ratios are correct; beta_d mean/variance section is numerically wrong. Claims about optimization algorithms/local minima are unsupported. |
| w_eff comparison | PASS/WARN | CSVs support row counts and differing values. Claims about uniqueness and instability are reasonable as table-output statements, but not theoretical claims. |
| Future projection comparison | PASS/WARN | Recap CSVs support ChatGPT/Gemini projection ranges and Claude NOT_SHOWN. Root-cause language is unsupported. |
| Stable findings | FAIL | Multiple "stable/reproducible" claims are overstated, especially H-FLRW methodology, beta methodology, qualitative behavior, and residual patterns. |
| Unstable findings | WARN | Mostly directionally supported, but several percentages and implications should be framed as CSV-level observations only. |
| Provenance risks | WARN | Good internal risk list, but local minima, optimizer behavior, and "valid optimization methods" are not verified. |
| Recommended next steps | WARN | Reasonable internally, but ensemble averaging / standardized re-fit should be framed as possible next steps, not implied necessary methodology. |
| Summary / data quality | WARN | "Data quality HIGH" and "verified independent data" rely on docs/80/PDF extraction, not this audit; should be softened. |

## Confirmed Findings

### 1. Beta Values

[VERIFIED] The three beta pairs in `docs/81` match the extracted CSV data:

| Service | beta_d | beta_q | Source CSV |
|---|---:|---:|---|
| ChatGPT | 0.78 | 0.19 | `chatgpt_approximate_matches.csv`, `chatgpt_weff_comparison.csv`, `chatgpt_recap_parameters.csv` |
| Claude | 4.5 | 18.0 | `claude_approximate_matches.csv`, `claude_weff_comparison.csv`, `claude_recap_parameters.csv` |
| Gemini | 4.25 | 8.10 | `gemini_approximate_matches.csv`, `gemini_weff_comparison.csv`, `gemini_recap_parameters.csv` |

### 2. Beta Ratios

[VERIFIED] The ratio claims in `docs/81` are mathematically correct when measured relative to ChatGPT:

| Ratio | Calculation | Result | docs/81 status |
|---|---:|---:|---|
| Claude beta_d / ChatGPT beta_d | 4.5 / 0.78 | 5.769x | Correct as 5.8x |
| Gemini beta_d / ChatGPT beta_d | 4.25 / 0.78 | 5.449x | Correct as 5.4x |
| Claude beta_q / ChatGPT beta_q | 18.0 / 0.19 | 94.737x | Correct as 94.7x |
| Gemini beta_q / ChatGPT beta_q | 8.10 / 0.19 | 42.632x | Correct as 42.6x |

[VERIFIED] The summary "5.4-5.8x for beta_d, 42.6-94.7x for beta_q" is correct.

### 3. Time / Redshift Grid

[VERIFIED] Row counts and z ranges match the CSVs:

| Service | Rows | z_min | z_max |
|---|---:|---:|---:|
| ChatGPT | 13 | 0.02 | 3.50 |
| Claude | 12 | 0.00 | 8.50 |
| Gemini | 11 | 0.02 | 2.81 |

[VERIFIED] There is no exact z value common to all three services in the approximate-match CSVs. ChatGPT and Gemini share z=0.02; Claude does not.

### 4. w_eff Tables

[VERIFIED] Row counts match the CSVs:

| Service | Rows with w_eff | z range | Notes |
|---|---:|---|---|
| ChatGPT | 13 | 0.02-3.50 | Has formula in recap CSV |
| Claude | 11 | 0.00-5.00 | Numerical table only |
| Gemini | 4 | 0.02, 0.25, 0.74, 2.81 | Partial table |

[VERIFIED] The comparison values quoted by `docs/81` are present in the CSVs:
- At z=0.02: ChatGPT w_eff=-1.22, Gemini w_eff=-1.05.
- Around z=0.8: ChatGPT z=0.85 w_eff=-0.92, Claude z=1.00 w_eff=-1.01, Gemini z=0.74 w_eff=-0.75.

### 5. Future Projection Tables

[VERIFIED] Recap CSVs support the basic projection comparison:

| Service | future_transition_gyr | contraction_onset_gyr |
|---|---|---|
| ChatGPT | 35-60 | 80-140 |
| Claude | NOT_SHOWN_EXPLICITLY | NOT_SHOWN_EXPLICITLY |
| Gemini | 32-38 | 55 |

The `docs/81` midpoint arithmetic is acceptable as a rough internal comparison, but the document should state that this is an arithmetic summary of extracted text, not a model result.

## Questionable Findings

### 1. H-FLRW Methodology Is Not Supported as Stable

[VERIFIED] `docs/81` says all three services use Planck 2018 cosmology with `Omega_m=0.315`, `Omega_Lambda=0.685`, and `H0=67.4` for H_FLRW.

[VERIFIED] The CSV values do not support that as a numerical statement. Spot checks using:

```
H(z) = H0 * sqrt(Omega_m * (1 + z)^3 + Omega_Lambda)
```

show mismatches:

| Service | z | CSV H_FLRW | H_FLRW if H0=67.4, Om=0.315, OL=0.685 | Comment |
|---|---:|---:|---:|---|
| ChatGPT | 0.15 | 75.0 | 72.7 | Closer to H0=70 than H0=67.4 |
| Claude | 0.14 | 69.3 | 72.3 | Not consistent with same formula |
| Gemini | 0.14 | 76.2 | 72.3 | Not consistent with same formula |
| Gemini | 2.81 | 425.0 | 287.8 | Large mismatch |

Therefore, the statement "H_FLRW calculation method is STABLE across all three services" should be changed to "H_FLRW provenance is unclear from the CSVs; the extracted metadata and values are not sufficient to confirm a single shared calculation method."

### 2. H-FLRW Differences Are Not Due Only to z-Grid and H-data

`docs/81` explains H_FLRW numerical differences as due to z-spacing and H-data choices. That is not sufficient. H_FLRW should not depend on H-data if it is a fixed FLRW baseline. The CSV values indicate at least one of:

- Different H0 or cosmological parameters were used.
- The H_FLRW values were manually/AI-estimated rather than generated by a common formula.
- The extraction or source table labels require further verification.
- The H_FLRW column may be internally inconsistent across service outputs.

This should be a WARN/FAIL item, not a stable finding.

### 3. ChatGPT H0 Anchor Conflict

[VERIFIED] `chatgpt_approximate_matches.csv` has `h0_anchor=70` for all rows.

[VERIFIED] `chatgpt_recap_parameters.csv` says `h0_anchor=73.0` and `h0_flrw_approx=67.4`.

This conflict should be called out before using ChatGPT H0-anchor claims. `docs/81` uses ChatGPT H0=70 in one section, which matches the approximate-match CSV, but the recap CSV contains conflicting metadata.

### 4. Beta Variance Section Has a Numeric Error

[VERIFIED] `docs/81` reports beta_d mean as 1.84. The correct arithmetic mean is:

```
(0.78 + 4.5 + 4.25) / 3 = 3.1767
```

Other beta_d dispersion numbers in that subsection should be recomputed. For reference:

| Quantity | beta_d | beta_q |
|---|---:|---:|
| Mean | 3.1767 | 8.7633 |
| Sample standard deviation | 2.0793 | 8.9235 |
| Sample CV | 65.5% | 101.8% |
| Population CV | 53.4% | 83.1% |

`docs/81` later recommends "Mean beta_d = 3.18 +/- 2.12", which is close to the correct mean and sample spread. The earlier beta_d mean 1.84 is inconsistent with that later section.

## Unsupported or Overstated Claims

### 1. "All three used valid optimization methods"

Unsupported. The CSVs contain fitted beta values and notes, but do not disclose the actual optimizer, initial guesses, convergence criteria, or cost function in enough detail to say the methods were valid.

Suggested correction:

> The three services produced fitted beta values, but the optimization procedures are not sufficiently documented to assess whether the procedures were equivalent or valid.

### 2. "Different local minima"

Unsupported. This is plausible, but the CSVs do not prove multiple local minima. It could also be caused by different data, different H0 anchors, different formulas, different prompt interpretation, or table-generation artifacts.

Suggested correction:

> The divergent beta values are consistent with non-unique fitting or differing service assumptions, but the cause is not identifiable from the CSVs alone.

### 3. "H_MULT has some robustness"

Overstated. The CSVs show that H_MULT remains close to each service's own H-data, but the services used different z-grids and different H-data. This does not establish robustness of H_MULT as a shared model output.

Suggested correction:

> H_MULT values are close to each service's extracted H-data within that service's table. Cross-service robustness cannot be assessed without a common z-grid, common H-data, and a documented H_MULT computation.

### 4. "Qualitative behavior is stable across all three services"

Overstated from CSV evidence. Qualitative statements about dipole dominance, quadrupole dominance, and future transition require source-text interpretation and model assumptions. The CSVs mostly contain table values and recap snippets.

Suggested correction:

> The extracted recap fields suggest broadly similar qualitative narratives, but this audit treats them as AI-output text, not as independently verified model behavior.

### 5. "MULTING vs FLRW residual patterns are stable"

Overstated. The CSVs show H_MULT residuals are smaller than H_FLRW residuals inside each extracted table, but because H-data and H_FLRW construction differ across services, cross-service residual pattern stability is not established.

Suggested correction:

> Within each extracted service table, H_MULT is closer to that table's H-data than H_FLRW. Cross-service residual comparability remains limited by different z-grids, H-data, and H_FLRW provenance.

### 6. "Data quality HIGH"

Overstated for `docs/81`. `docs/80` reports extraction quality after contamination fix, but this independent audit found at least one substantial downstream interpretation issue: H_FLRW methodology. "High" should be narrowed to parse/provenance completeness, not analytical reliability.

Suggested correction:

> CSV extraction appears complete enough for internal comparison, but analytical claims require revision and source-level verification.

## H_MULT Stability Audit

[VERIFIED] The quoted z approximately 0.14-0.15 values match the approximate-match CSVs:

| Service | z | H_data | H_MULT | beta_d | beta_q |
|---|---:|---:|---:|---:|---:|
| ChatGPT | 0.15 | 74.0 | 75.0 | 0.78 | 0.19 |
| Claude | 0.14 | 74.0 | 73.5 | 4.5 | 18.0 |
| Gemini | 0.14 | 77.5 | 77.1 | 4.25 | 8.10 |

[VERIFIED] The H_MULT range at those nearby z values is 73.5-77.1, a 3.6 km/s/Mpc absolute spread and about 4.8% relative to the low end.

[INFERRED] This supports a narrow statement: H_MULT table values differ much less than beta_q values at nearby low z.

[WARN] It does **not** support a strong claim that H_MULT is stable or robust, because:
- The services use different H-data values.
- The services use slightly different z values.
- The computation used to produce H_MULT is not independently reproduced here.
- Anchor rows can make first-row agreement trivial by construction.

## w_eff and Future Projection Audit

[VERIFIED] The w_eff values in `docs/81` match extracted CSV values at the cited approximate z positions.

[WARN] The phrase "w_eff predictions" should be softened. The CSVs support "w_eff outputs" or "w_eff table values." They do not establish w_eff as a prediction of a validated model.

[VERIFIED] Future projection ranges in `docs/81` match recap CSVs for ChatGPT and Gemini, and Claude is correctly marked as not explicit.

[WARN] Root-cause statements such as "different beta parameters caused the future projection differences" are not proven by the CSVs. Use "may reflect" or "could be associated with."

## Suggested Wording Corrections

1. Replace:
   > H_FLRW calculation method is STABLE across all three services.

   With:
   > H_FLRW provenance is not yet stable from the extracted CSV evidence. The tables contain H_FLRW columns, but the numerical values do not confirm a single shared Planck-2018 calculation across services.

2. Replace:
   > All three use Planck 2018 cosmology (Omega_m=0.315, Omega_Lambda=0.685, H0=67.4) for H_FLRW baseline.

   With:
   > Recap metadata mentions Planck-like parameters for some services, but spot checks of the extracted H_FLRW values do not reproduce a single Planck-2018 baseline. This requires source-level verification.

3. Replace:
   > Beta parameters are not reproducible constants.

   With:
   > The extracted AI-service beta values are not numerically reproducible across the three service outputs.

4. Replace:
   > All three used valid optimization methods.

   With:
   > All three report fitted beta values, but their optimization procedures are not sufficiently documented to evaluate equivalence or validity.

5. Replace:
   > H_MULT has some robustness.

   With:
   > H_MULT remains close to each service's own H-data in the extracted tables, but cross-service robustness is not established.

6. Replace:
   > different local minima

   With:
   > non-unique fitting, differing service assumptions, or undocumented table-construction choices.

7. Replace:
   > w_eff predictions

   With:
   > w_eff outputs or w_eff table values.

8. Replace:
   > Data quality: HIGH

   With:
   > Extraction completeness appears adequate for internal audit, but analytical claims require revision.

## Safe-Use Assessment

### Is `docs/81` numerically accurate?

**WARN.** Major table values, row counts, beta values, beta ratios, w_eff rows, and future projection ranges are mostly accurate. However, beta_d mean/variance is wrong in one subsection, and H_FLRW methodology claims are not supported by the CSV values.

### Is the beta comparison correct?

**PASS/WARN.** Beta values and ratios are correct. The instability conclusion is supported at the CSV-value level. The variance subsection needs correction, and causality/optimizer explanations need softening.

### Are H_FLRW claims supported?

**FAIL.** The claim of a stable shared Planck-2018 H_FLRW method is not supported by CSV values. This is the main required revision.

### Are H_MULT stability claims supported?

**WARN.** H_MULT values are close to each service's own H-data and differ less than beta parameters at selected nearby z values. Stronger claims about robustness, weak beta dependence, or compensating effects are unsupported.

### What wording must be softened?

Soften or remove:
- "stable H_FLRW methodology"
- "methodology identical"
- "valid optimization methods"
- "different local minima"
- "H_MULT has some robustness"
- "qualitative behavior stable"
- "residual patterns stable"
- "w_eff predictions"
- "Data quality HIGH" as an analytical claim

### Does `docs/81` need revision?

**YES.** Minimum required revisions:
1. Correct beta_d mean/variance.
2. Reclassify H_FLRW methodology as WARN/UNCERTAIN, not stable.
3. Add explicit H_FLRW formula spot-check mismatch.
4. Downgrade H_MULT robustness to within-table closeness only.
5. Mark optimizer/local-minima explanations as hypotheses.
6. Replace validation-like wording with internal-analysis wording.

### Is `docs/81` safe for internal analysis?

**WARN / YES AFTER EDITS.** It is useful as an internal draft, but only after the H_FLRW and overclaim edits above. In current form it may mislead future work by treating H_FLRW methodology as stable.

### Is `docs/81` safe to share with Dr. Buckholtz after edits?

**WARN / POSSIBLY AFTER EDITS.** It should not be shared in current form. After edits, it may be shareable as a careful internal reproducibility audit if it clearly says:
- no validation or refutation,
- no MCMC,
- CSV-level audit only,
- H_FLRW provenance unresolved,
- H_MULT robustness not established,
- optimization methods not disclosed.

## Compliance Confirmation

[VERIFIED] No email sent.

[VERIFIED] No public claims made.

[VERIFIED] No validation or refutation claim made.

[VERIFIED] No MCMC run.

[VERIFIED] `docs/81_multi_ai_reproducibility_comparison.md` was not edited by this audit.
