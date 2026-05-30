# Negative-Control Diagnostics for MULTING Table Specificity

## Safety labels

INTERNAL_ONLY
DIAGNOSTIC_ONLY
SAFE_NOW
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_NOT_REQUIRED

## 1. Purpose

This is a specificity diagnostic for extracted MULTING/Table A1 values. It is diagnostic-only work and cannot support validation or refutation of MULTING, FLRW, w_eff, or any physical bridge.

## 2. Inputs

**DATA SOURCE (UPDATED 2026-05-31):** data/table_a1_reported.csv (REAL Table A1, rows 2-12)

| File | Found? | Role | Notes |
|---|---|---|---|
| `data/table_a1_reported.csv` | YES | **REAL Table A1 data** | rows 2-12, z=0.15 to z=8.5, 11 points |
| `src/negative_control_tests.py` | YES | Implementation with real loader | uses load_table_a1_rows_2_12() |
| `docs/87_negative_control_test_plan.md` | YES | Negative-control planning context | available |
| `src/deep_bridge_diagnostic_fit.py` | YES | Loader source | load_table_a1_rows_2_12() function |
| `docs/68_hflrw_provenance_recovery.md` | YES | H_FLRW provenance context | available |
| `docs/81_multi_ai_reproducibility_comparison.md` | YES | Multi-AI comparison context | available |

## 3. Method

- Random seed: `20260531`.
- Row-permutation control: `100` fixed-seed permutations.
- Randomised beta diagnostic: deterministic beta samples from reported-value ranges; labelled INCONCLUSIVE because no beta-to-H_MULT routine is source-confirmed.
- Synthetic Lambda-CDM test: H0=70.0, Omega_m=0.3, Omega_lambda=0.7, Omega_k=0.0 on the Table A1 z-grid.
- Metric: normalized RMSE using the extracted H uncertainty column.
- Thresholds: row permutation uses 0.05/0.20 fraction gates; synthetic test uses ratio >3 PASS and >=1.5 WARN.

## 4. Results (UPDATED with REAL Table A1, 2026-05-31)

**Beta values:** β_d=4.5, β_q=18.0 (from Table A1 caption, AI service fitted)

| Test | Metric | Value | Diagnostic label | Interpretation |
|---|---|---|---|---|
| row_permutation_negative_control | p-value | 0.0000 | PASS | Original z-ordering significantly better than shuffled (p < 0.01). Model is sensitive to redshift structure. |
| randomized_beta_diagnostic | percentile_rank | 13.0% | FAIL | Beta values in bottom 13% of random distribution. Many random pairs fit equally well. Beta parameters poorly constrained. |
| synthetic_lcdm_specificity_test | chi2_ratio (synth/real) | ~0.00 | FAIL | Diagnostic proxy fits synthetic ΛCDM better than real table. Proxy model too generic/flexible. Requires full F_oP → H_MULT bridge. |

**Overall verdict:** FAIL (Test 2 and Test 3 both FAIL)

## 5. Breakthrough candidate assessment

Classification: **PARTIAL_SPECIFICITY**

Allowed wording: this result may raise or lower confidence in specificity and may justify follow-up diagnostics. It does not validate or refute a model.

## 6. What this means

- This raises or lowers confidence in table specificity only.
- This can support or weaken the case for further testing.
- This may justify Fisher/model-selection follow-up if specificity is strong enough.
- This may indicate that the reproduction method is too flexible if controls perform well.

Forbidden interpretations:
- MULTING is validated.
- MULTING is refuted.
- Buckholtz is right or wrong.
- Any AI service is correct.

## 7. Limitations

- No MCMC.
- No out-of-sample cosmological data.
- No author-confirmed F_oP -> H_MULT bridge.
- Beta provenance remains unresolved.
- The randomised beta diagnostic is inconclusive without a beta-to-H_MULT routine.
- Diagnostic-only status.

## 8. Next recommended step

systematics budget

## 9. Reproducibility manifest (UPDATED 2026-05-31)

```yaml
test_id: negative_control_battery_002
status: completed_with_real_table_a1
claim_boundary: diagnostic_only
data_source: data/table_a1_reported.csv
data_points: 11
beta_d: 4.5
beta_q: 18.0
random_seed: 42
n_shuffles: 100
n_random_beta: 100
implementation: src/negative_control_tests.py
loader: load_table_a1_rows_2_12() from deep_bridge_diagnostic_fit.py
input_files:
  - file: data/table_a1_reported.csv
    found: true
    role: REAL_TABLE_A1_DATA
  - file: src/negative_control_tests.py
    found: true
    role: implementation_with_real_loader
  - file: tests/test_negative_control_tests.py
    found: true
    status: 3_tests_passing
outputs:
  - docs/91_negative_control_results.md
tests:
  row_permutation: PASS (p=0.0000)
  randomized_beta: FAIL (13.0%)
  synthetic_lcdm: FAIL (ratio~0.00)
overall_verdict: FAIL
can_support_validation: false
can_support_refutation: false
can_support_public_claim: false
run_command: python -m src.negative_control_tests
test_command: python -m pytest tests/test_negative_control_tests.py -q
```
