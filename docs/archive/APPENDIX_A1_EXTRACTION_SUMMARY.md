# Appendix A1 Forensic Extraction — Executive Summary

**Date:** 2026-05-29  
**Source:** preprints202511.0598.v6.pdf, Appendix A.1, pages 31–38  
**Status:** ✅ FORENSIC EXTRACTION COMPLETE  
**Tests:** 88/88 core tests passed (26 new Appendix A1 tests)

> ℹ️ **HISTORICAL SNAPSHOT (flagged 2026-09-14, navigation pass) — but its
> central finding is still load-bearing.** That the `H_MULT(z)` computational
> formula is absent from the source, leaving the bridge under-specified, still
> stands and is upstream of much of what followed. Two cautions on the
> surrounding material: the version and test counts are v0.2-era, and **this
> reads preprint v6**, whereas everything from 2026-08 onward reads the
> substantially expanded v82 — `CLAUDE.md`'s source-version rule is "cite v6
> for anything already established, v82 for anything new, never conflate."
> Scope framing: `docs/WHAT_THIS_REPRODUCES.md`. Current state:
> [`PROGRAM_CLOSEOUT_LEDGER.md`](../../PROGRAM_CLOSEOUT_LEDGER.md).
>
> *Moved from the repository root to `docs/archive/` on 2026-09-14, when
> the root was reduced to live documents only. Its former path was
> `APPENDIX_A1_EXTRACTION_SUMMARY.md`.*

---

## 1. What Was Extracted

Performed word-level forensic extraction of Appendix A1 Steps 3–7 from v6 PDF.

**Files created:**
1. `docs/39_appendix_a1_steps_3_7_forensic_reading.md` (9.5 KB) — full verbatim extraction
2. `src/appendix_a1_procedure_registry.py` (14 KB) — programmatic encoding
3. `tests/test_appendix_a1_procedure_registry.py` (7 KB) — 26 verification tests

**Files updated:**
4. `docs/18_fit_reproduction_requirements.md` — added Step 5 finding
5. `docs/22_discovery_ledger.md` — Finding 4 updated, Finding 16 added
6. `PROJECT_STATUS.md` — version v0.2-appendix-a1-forensic

---

## 2. Key Finding: H_MULT Formula Missing

### Question
Does Appendix A1 provide explicit formula H_MULT = f(z, β_d, β_q, m_A, r_A, k_A, ...)?

### Answer
**NO, formula missing**

### Evidence

**What Step 5 PROVIDES:**
- ✅ Scaling relations: r_dA = β_d × r_A, r_dP = β_d × r_P, |r_qAB|² = β_q² × r_A × r_P
- ✅ Fitting constraint: *"minimize standard-deviations away from observed H(z)"*
- ✅ AI discretion: *"Feel free to use any or all the information"*
- ✅ β_d = 4.5, β_q = 18.0 (Table A1 reported values)

**What Step 5 DOES NOT PROVIDE:**
- ❌ Functional form: H_MULT(z, β_d, β_q, m_A, r_A, k_A, ...)
- ❌ Objective function details (beyond "minimize σ")
- ❌ Computational procedure (algorithm)
- ❌ Cluster variable table: m_A(z), r_A(z), k_A(z) for all z

**Bridge Status:** PARTIAL — procedural instruction only, NOT computational formula

---

## 3. Steps 3–7 Status Matrix

| Step | Title | Status | Code-Ready? | Blocker |
|------|-------|--------|-------------|---------|
| 3 | Time Range | SOURCE_CONFIRMED | ✅ | t_ROE,min = AI choice |
| 4 | Galaxy Cluster Parameters | AUTHOR_PROMPT_INSTRUCTION | ❌ | m_A, r_A, k_A = AI estimated |
| 5 | Approximate Matches | **UNDER_SPECIFIED** | ❌ | **H_MULT formula missing** |
| 6 | Future Projections | BLOCKED | ❌ | Requires H_MULT(z) |
| 7 | w_eff Comparison | SOURCE_CONFIRMED | ✅ | Comparison only |

---

## 4. Variable Provenance (16 variables)

| Variable | Provenance | Code Permission | Notes |
|----------|------------|-----------------|-------|
| Time, z, H-data | DATA | CODE_READY | Observational |
| m_A, r_A, D_C:AB, k_A/c² | AI_ESTIMATED | NOT_CODE_READY | No data source |
| **β_d, β_q** | **FITTED_PHENOMENOLOGICAL** | **TABLE_REPRODUCTION_ONLY** | Minimize σ from H-data |
| **H-MULT** | **UNDER_SPECIFIED** | **BLOCKED** | **Formula missing** |
| H-FLRW, σ_FLRW | FORMULA_PROVIDED | CODE_READY | Standard ΛCDM |
| w_eff, H-w_eff | AI_ESTIMATED / DERIVED | CODE_READY | Step 7 comparison |

---

## 5. What Can Be Reproduced

### ✅ Allowed (Code-Ready)

1. **Table A1 as empirical data** — 12 rows, z = 0 to 8.5
2. **Force formulas** — F_m, F_d, F_q, F_oP (Step 2)
3. **Scaling relations** — r_dA, r_dP, r_qAB (Step 5)
4. **β_d = 4.5, β_q = 18.0** — as TABLE_REPORTED constants
5. **Comparison with ΛCDM** — Step 7 w_eff analysis

### ❌ Blocked (NOT Code-Ready)

1. **H_MULT(z) computation** — formula missing (Step 5 under-specified)
2. **β_d, β_q fitting** — objective function under-specified
3. **Future projections** — Step 6 blocked (requires H_MULT formula)
4. **MCMC parameter estimation** — no likelihood function (no H_MULT formula)
5. **Validation/falsification** — cannot test MULTING predictions without formula

---

## 6. Table A1 — AI Service Output, Not Author Calculation

**Critical finding from Table A1 caption:**

> "Regarding H-MULT, the online service reported choosing β_d = 4.5 and β_q = 18.0."

**Implication:** Table A1 H_MULT column is **AI service output** following Step 5 procedural instruction, NOT author-verified calculation.

**Status:** TABLE_REPORTED (empirical reference), NOT PREDICTIVE (no formula for new z)

---

## 7. Next Steps

### Immediate (User Action)

1. ✅ Forensic extraction complete
2. ⏳ Update clarification brief (docs/26, docs/38) with Step 5 finding
3. ⏳ Add to Priority 1 question for Dr. Buckholtz:

> "Appendix A1 Step 5 instructs AI service to fit monopole/dipole/quadrupole to H-data but does not provide explicit computational formula H_MULT(z; β_d, β_q, ...). Table A1 reports H_MULT values as AI service output. Could you provide:
> 
> (1) The explicit formula H_MULT(z; β_d, β_q, m_A, r_A, k_A, ...), OR
> (2) Confirmation that AI interpretation (heuristic scaling? virial pressure? other?) matches your intended approach, OR
> (3) Cluster variable table m_A(z), r_A(z), k_A(z) for all z in Table A1 if using heuristic approach?"

### After Clarification

4. Implement H_MULT(z) formula (if provided)
5. Reproduce Table A1 H_MULT column
6. Verify against AI service values
7. Compare fit quality with ΛCDM
8. Unblock MCMC (if forward model complete)

---

## 8. Test Results

**Total:** 100 tests (88 passed, 12 skipped)

**New Appendix A1 tests:** 26/26 passed ✅

**Key test categories:**
- `test_beta_d_beta_q_are_fitted_phenomenological()` ✅
- `test_h_mult_is_under_specified()` ✅
- `test_bridge_formula_missing()` ✅
- `test_h_mult_computation_is_blocked()` ✅
- `test_no_function_named_compute_hz()` ✅

**Run tests:**
```bash
pytest tests/test_appendix_a1_procedure_registry.py -v  # 26/26 passed
pytest -q  # 88 passed, 12 skipped
```

---

## 9. Documentation Trail

| File | Type | Size | Status |
|------|------|------|--------|
| `docs/39_appendix_a1_steps_3_7_forensic_reading.md` | Forensic extraction | 9.5 KB | ✅ Complete |
| `src/appendix_a1_procedure_registry.py` | Programmatic encoding | 14 KB | ✅ Complete |
| `tests/test_appendix_a1_procedure_registry.py` | Verification tests | 7 KB | ✅ 26/26 passed |
| `docs/18_fit_reproduction_requirements.md` | Updated | +150 bytes | ✅ Step 5 finding added |
| `docs/22_discovery_ledger.md` | Updated | +5 KB | ✅ Finding 16 added |
| `PROJECT_STATUS.md` | Updated | v0.2 | ✅ Version bump |

---

## 10. Safe vs Unsafe Wording

### ✅ Safe Wording

> "Appendix A1 Step 5 provides force formulas and scaling relations but does NOT provide explicit computational formula H_MULT(z; β_d, β_q, ...). Bridge from pairwise forces to cosmological expansion remains under-specified. Table A1 H_MULT values are AI service output following procedural instruction, not author calculation. We can store Table A1 as empirical data but cannot compute H_MULT(z) on new redshifts without explicit formula."

### ❌ Unsafe Wording

- ❌ "Formula is in Appendix A1" — only scaling relations, NOT full formula
- ❌ "We can compute H_MULT from Step 5" — procedural only, NOT computational
- ❌ "Table A1 proves formula works" — AI interpretation, not verified
- ❌ "Author calculated H_MULT values" — AI service calculated them
- ❌ "Step 5 is complete" — under-specified for reproducible computation

---

## 11. Relationship to Other Findings

**Finding 4 (Missing H-MULT formula):** UPGRADED with forensic evidence  
**Finding 12 (Force-law layer):** Confirms force formulas SOURCE_CANDIDATE, closure missing  
**Finding 13 (Heuristic Phi(z)):** One possible AI interpretation, not source-confirmed  
**Finding 14 (Bridge triage):** Zero source-supported routes — Appendix A1 confirms  
**Finding 15 (MVB discrete lattice):** Another possible interpretation, not source-confirmed  
**Finding 16 (Appendix A1 extraction):** THIS FINDING — forensic evidence complete

---

## 12. Code Permission Enforcement

```python
# From src/appendix_a1_procedure_registry.py
class CodePermission(Enum):
    CODE_READY = "code_ready"
    NOT_CODE_READY = "not_code_ready"
    ALLOWED_FOR_TABLE_REPRODUCTION_ONLY = "allowed_for_table_reproduction_only"
    BLOCKED = "blocked"

# H-MULT status
h_mult = Variable(
    symbol="H-MULT",
    provenance=VariableProvenance.UNDER_SPECIFIED,
    code_permission=CodePermission.BLOCKED,
    notes="Step 5: procedural instruction only, NO computational formula"
)

# Beta status
beta_d = Variable(
    provenance=VariableProvenance.FITTED_PHENOMENOLOGICAL,
    code_permission=CodePermission.ALLOWED_FOR_TABLE_REPRODUCTION_ONLY,
    notes="Table A1: β_d = 4.5"
)
```

**Tests enforce:** No function named `compute_Hz` or `compute_H_MULT` exists ✅

---

## 13. Summary

1. ✅ Forensic extraction of Appendix A1 Steps 3–7 complete
2. ✅ Force formulas (F_m, F_d, F_q) and scaling relations (r_dA, r_dP, r_qAB) confirmed
3. ❌ H_MULT computational formula NOT found — bridge UNDER_SPECIFIED
4. ✅ β_d = 4.5, β_q = 18.0 confirmed as FITTED_PHENOMENOLOGICAL (not derived)
5. ❌ Table A1 H_MULT = AI service output (not author calculation)
6. ✅ Can store Table A1 as empirical data
7. ❌ CANNOT compute H_MULT(z) on new redshifts (formula missing)
8. ❌ MCMC parameter estimation BLOCKED (no likelihood function)
9. ✅ 26 new tests verify extraction accuracy (all passing)
10. ⏳ Next: update clarification brief, send updated question to author

---

**End of Summary**  
**Full details:** See `docs/39_appendix_a1_steps_3_7_forensic_reading.md`  
**Tests:** `pytest tests/test_appendix_a1_procedure_registry.py -v`  
**Report:** `python -m src.report`
