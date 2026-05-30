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

| File | Found? | Role | Notes |
|---|---|---|---|
| `docs/87_negative_control_test_plan.md` | YES | Negative-control planning context | available |
| `docs/90_multing_physical_verification_upgrade_plan.md` | NO | Optional physical upgrade plan | <unknown>file not found</unknown> |
| `src/table_a1_independent_recomputation.py` | YES | Existing recomputation helpers | available |
| `docs/68_hflrw_provenance_recovery.md` | YES | H_FLRW provenance context | available |
| `docs/81_multi_ai_reproducibility_comparison.md` | YES | Multi-AI comparison context | available |
| `data/table_a1_reported.csv` | YES | Table A1 reported values | available |

## 3. Method

- Random seed: `20260531`.
- Row-permutation control: `100` fixed-seed permutations.
- Randomised beta diagnostic: deterministic beta samples from reported-value ranges; labelled INCONCLUSIVE because no beta-to-H_MULT routine is source-confirmed.
- Synthetic Lambda-CDM test: H0=70.0, Omega_m=0.3, Omega_lambda=0.7, Omega_k=0.0 on the Table A1 z-grid.
- Metric: normalized RMSE using the extracted H uncertainty column.
- Thresholds: row permutation uses 0.05/0.20 fraction gates; synthetic test uses ratio >3 PASS and >=1.5 WARN.

## 4. Results

| Test | Metric | Original | Control distribution | Diagnostic label | Interpretation |
|---|---:|---:|---|---|---|
| row_permutation_negative_control | fraction_as_good_or_better=0 | 0.520588 | min=3.179, median=24.96, max=93.21 | PASS | Original table appears more structured than shuffled controls. |
| randomized_beta_diagnostic | reported_beta_percentile=NA | NA | <unknown>beta-to-H_MULT routine not available</unknown> | INCONCLUSIVE | No source-confirmed beta-to-H_MULT routine is available; random beta samples are reproducible, but beta specificity cannot be evaluated. |
| synthetic_lcdm_specificity_test | synthetic_to_original_metric_ratio=6.63395 | 0.520588 | synthetic_metric=3.454 | PASS | Synthetic Lambda-CDM table is distinguishable under the reported-table surrogate. |

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

## 9. Reproducibility manifest

```yaml
test_id: negative_control_battery_001
status: completed_or_partial
claim_boundary: diagnostic_only
random_seed: 20260531
n_shuffles: 100
n_random_beta: 100
input_files:
  - file: docs/87_negative_control_test_plan.md
    found: true
  - file: docs/90_multing_physical_verification_upgrade_plan.md
    found: false
  - file: src/table_a1_independent_recomputation.py
    found: true
  - file: docs/68_hflrw_provenance_recovery.md
    found: true
  - file: docs/81_multi_ai_reproducibility_comparison.md
    found: true
  - file: data/table_a1_reported.csv
    found: true
outputs:
  - docs/91_negative_control_results.md
tests:
  row_permutation: PASS
  randomized_beta: INCONCLUSIVE
  synthetic_lcdm: PASS
can_support_validation: false
can_support_refutation: false
can_support_public_claim: false
```
