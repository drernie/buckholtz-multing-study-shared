# k_A Closure Test Report

**Labels:** NOT_VALIDATION | INTERNAL_CLOSURE_TEST | AUTHOR_CONFIRMATION_REQUIRED  
**Version:** v0.4.0 (2026-06-06)  
**Run:** `python audit/run_k_a_closure_audit.py`

---

## Purpose

Test whether **independent** k_A(z) (Press-Schechter + virial, α at z=0 only) reproduces Table A1 H_MULT retrodiction at **fixed** β_d=4.5, β_q=18.0 — without refitting k_A, β, or D.

This is **not** validation of MULTING against independent data. β were fitted to the same H_obs points.

---

## Protocol

| Step | Action |
|------|--------|
| Fixed | β_d=4.5, β_q=18.0; no refit |
| Arm A | D = D_csv (Claude supplementary schedule) |
| Arm B | D = D₀(1+z)^{−γ_req}, γ_req≈2.27 from D_required solver |
| Variable | k_A_indep vs k_A_csv |
| PASS | RMS_σ(indep) ≤ 2× RMS_σ(csv baseline) |
| FAIL | Independent k_A much worse at same β, D |
| INCONCLUSIVE | Moderate difference; N-body path without catalog |

---

## D_required (Phase 0)

Inverse brentq: find D(z) such that Phi-ratio bridge = H_obs(z).

**Acceptance (verified in tests):**
- γ_req (z≥0.4) ∈ [2.0, 2.6] (current fit ~2.27; σ_H sensitivity range [2.21, 2.32])
- D_req/D_csv < 0.8 for z≥3

---

## Interpretation boundaries

| Allowed | Forbidden |
|---------|-----------|
| "Table A1 **implementation** fails independent k_A closure" | "MULTING falsified" |
| NOT_VALIDATION labels on all outputs | compute_H_MULT in src/ |
| D_eff as **diagnostic** patch | Theory true/false claims |

---

## Author questions

See docs/98_k_a_closure_author_questions.md (Q15–Q18).

---

## Related

Double-inversion diagnostic (isolines + γ/α grid): docs/DOUBLE_INVERSION_DIAGNOSTIC.md
