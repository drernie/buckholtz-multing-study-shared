# Reproducibility Plan Outline — IDM/MULTING Framework

**Date:** 2026-05-30  
**For:** Dr. Thomas J. Buckholtz  
**Prepared by:** Reproducibility audit team  
**Status:** DRAFT_FOR_AUTHOR_REVIEW

**Purpose:** Outline a phased, collaborative plan for fair reproducibility testing of the IDM/MULTING framework.

**Tone:** Respectful, transparent, assumes author is expert and we are learners.

**Safety Labels:**
```
NOT_VALIDATION
NOT_REFUTATION
COLLABORATIVE
TRANSPARENT
FAIR_TESTING
RESPECTFUL
AUTHOR_DEPENDENT
CONDITIONAL_ON_BLOCKERS
```

---

## Guiding Principles

1. **Transparency:** All methods, data, code, and assumptions documented publicly (or privately shared with author)
2. **Fairness:** Same standards applied to ΛCDM and MULTING (no double standards)
3. **Respect:** Assumes author is expert; we seek clarification, not criticism
4. **Conditionality:** Each phase depends on resolving blockers from prior phase
5. **Exit criteria:** Clear success/failure conditions for each phase
6. **No overclaiming:** Internal audit only; no public validation/refutation without author agreement + peer review

---

## Four-Phase Plan

### Phase 1: Parameter Provenance Clarification

**Timeline:** 2 weeks (conditional on author response)

**Goal:** Resolve ambiguities in Table A1 baseline and bridge method.

**Current blockers:**
1. ❌ H_FLRW baseline unknown (which H0, Ωm, ΩΛ, calculator?)
2. ❌ F_oP → H_MULT bridge method unclear (which of 3 candidate paths?)
3. ❌ H_MULT operational meaning ambiguous (expansion rate vs effective parameter?)

**Actions:**

1. **Ask 3 clarification questions** (respectfully):
   - **Q1 (H_FLRW):** "Which H_FLRW baseline was used for Table A1? (H0, Ωm, ΩΛ, calculator/service)"
   - **Q2 (Bridge):** "How does F_oP map to H_MULT(z)? We identified 3 candidate paths (Phi-scaling heuristic, Hamiltonian energy bridge, N-body lattice) — which is the intended method, or is there a fourth path?"
   - **Q-operational:** "What is the operational meaning of H_MULT(z)? Is it an expansion rate measurement, an effective parameter from force-law fit, or something else?"

2. **Read Supplementary Materials:**
   - Compare ChatGPT, Gemini, Claude versions of Table A1
   - Identify which H_FLRW baseline each AI service chose
   - Document AI service default choices (may solve provenance mystery without author input)

3. **Update registry:**
   - If author provides H_FLRW baseline → update `data/table_a1_reported.csv` header
   - If author confirms bridge method → update `src/equations.py` with explicit formula
   - If author clarifies operational meaning → update `docs/06_rosetta_stone.md`

**Success criteria:**
- ✅ H_FLRW baseline identified (either from author or from AI service comparison)
- ✅ Bridge method clarified (at least one of 3 paths confirmed, or new path provided)
- ✅ H_MULT operational meaning documented

**Exit criteria (proceed to Phase 2):**
- Minimum: H_FLRW baseline + bridge method confirmed
- Ideal: All 3 clarifications answered

**Exit criteria (archive project):**
- Author declines to answer after 30 days
- Author states bridge method is proprietary / cannot be shared
- Author states H_FLRW baseline was arbitrary AI choice with no provenance

**Outcome artifacts:**
- Updated registry files (`beta_definitions.py`, `equations.py`, `rosetta.py`)
- Multi-AI table comparison report (`docs/73_multi_ai_table_comparison.md`)
- Author clarification summary (`docs/26_author_clarification_brief.md` updated)

---

### Phase 2: Independent Dataset Integration

**Timeline:** 2-3 weeks (can start in parallel with Phase 1, but results depend on Phase 1 completion)

**Goal:** Prepare out-of-sample test using observational data NOT used in Table A1 fit.

**Current status:**
- ⏸️ Can proceed independently of author input
- ⏸️ Blocked on Phase 1 (need bridge method to compute H_MULT predictions)

**Actions:**

1. **Integrate Pantheon+ SNIa dataset:**
   - Load Pantheon+ (1701 SNIa, z=0.001–2.26)
   - Exclude 12 systems from Table A1 (prevent data leakage)
   - Compute distance modulus μ(z) for both ΛCDM and MULTING
   - Prepare train/test split (if needed for parameter fitting)

2. **Integrate BAO dataset:**
   - SDSS DR16 BAO measurements (z=0.15–2.33)
   - DESI early release (if available)
   - Compute D_V(z) / r_d for both models

3. **Implement complexity penalty:**
   - AIC = -2 log L + 2k (k = number of free parameters)
   - BIC = -2 log L + k log n (n = number of data points)
   - For ΛCDM: k=2 (H0, Ωm)
   - For MULTING: k=? (depends on bridge method — may be 2, 3, or 4)

4. **Test on independent sample:**
   - Use Table A1 parameters (beta_d=4.5, beta_q=18.0) WITHOUT refitting
   - Compute residuals on Pantheon+ and BAO
   - Compare with ΛCDM baseline (same parameters as Table A1 H_FLRW)

**Success criteria:**
- ✅ Pantheon+ and BAO datasets loaded and cleaned
- ✅ Distance modulus / BAO predictions computed for both models
- ✅ AIC/BIC implemented correctly (verified on toy data)
- ✅ Out-of-sample test runs without errors

**Exit criteria (proceed to Phase 3):**
- Bridge method from Phase 1 implemented
- Out-of-sample residuals computed
- Complexity penalty (AIC/BIC) ready

**Exit criteria (archive project):**
- Phase 1 failed (no bridge method)
- Bridge method requires data unavailable to us (e.g., proprietary cluster kinematics)

**Outcome artifacts:**
- `data/pantheon_plus_cleaned.csv` (1701 SNIa, Table A1 systems excluded)
- `data/bao_measurements.csv` (BAO data)
- `src/independent_data_test.py` (out-of-sample testing script)
- `tests/test_aic_bic.py` (complexity penalty unit tests)

---

### Phase 3: MCMC Comparison (Conditional)

**Timeline:** 3-4 weeks (ONLY if Phases 1-2 succeed)

**Goal:** Fair statistical comparison of ΛCDM vs MULTING on independent data.

**Current status:**
- ❌ BLOCKED until Phase 1 complete (no bridge method)
- ❌ BLOCKED until Phase 2 complete (no independent data ready)

**Preconditions (ALL must be satisfied):**
1. ✅ Bridge method confirmed and implemented (Phase 1)
2. ✅ Independent datasets ready (Phase 2)
3. ✅ Complexity penalty implemented (Phase 2)
4. ✅ Author agrees to proceed (explicit approval)
5. ✅ User approves time investment (GeoScan Gold complete, or explicit override)

**If ANY precondition fails → DO NOT PROCEED.**

**Actions (if preconditions met):**

1. **Define parameter priors:**
   - ΛCDM: H0 ~ Uniform(60, 80), Ωm ~ Uniform(0.2, 0.4)
   - MULTING: beta_d ~ ?, beta_q ~ ? (depends on whether they are fitted or derived)
   - Document prior choices explicitly (avoid implicit bias)

2. **Run MCMC:**
   - Use emcee (Python) or Stan (if complex model)
   - 4 chains, 10,000 steps each, burn-in 2,000
   - Convergence: Gelman-Rubin R̂ < 1.01
   - Posterior samples: ≥20,000 per parameter

3. **Compute model comparison metrics:**
   - Log-likelihood: log P(data | model)
   - AIC / BIC: penalize model complexity
   - Bayes factor: P(data | MULTING) / P(data | ΛCDM)
   - Posterior predictive checks: does model predict unseen data?

4. **Test on held-out data:**
   - If using train/test split: compute residuals on test set
   - If using cross-validation: K-fold CV with K=5
   - Report: RMSE, MAE, chi-squared on held-out data

5. **Document everything:**
   - Code: `src/mcmc_comparison.py`
   - Config: `config/mcmc_settings.yaml` (priors, MCMC parameters)
   - Results: `results/mcmc_chains.h5` (posterior samples)
   - Report: `docs/74_mcmc_comparison_report.md`

**Success criteria:**
- ✅ MCMC converged (R̂ < 1.01 for all parameters)
- ✅ Posterior predictive checks pass (no systematic bias)
- ✅ Model comparison metrics computed (AIC, BIC, Bayes factor)
- ✅ Held-out test performed fairly for both models

**Possible outcomes:**

| Outcome | Interpretation | Next Action |
|---------|---------------|-------------|
| **MULTING >> ΛCDM** | MULTING fits data significantly better | Write up findings, ask author if he wants to co-author paper |
| **ΛCDM >> MULTING** | ΛCDM fits data significantly better | Document honestly, no overclaiming, offer findings to author |
| **MULTING ≈ ΛCDM** | Models are statistically indistinguishable | Document as inconclusive, note that more data or refined model needed |
| **Both fail** | Neither model fits independent data well | Investigate: data quality issue? Model misspecification? |

**Exit criteria (publish results):**
- MCMC complete, results robust
- Author has reviewed findings
- Peer review arranged (or preprint posted with author consent)

**Exit criteria (archive privately):**
- Author requests results not be published
- Results are inconclusive and not worth publication effort
- Methodology paper (epi-registry, audit protocol) is higher priority

**Outcome artifacts:**
- `src/mcmc_comparison.py` (MCMC script)
- `results/mcmc_chains.h5` (posterior samples)
- `docs/74_mcmc_comparison_report.md` (full report)
- `notebooks/04_mcmc_diagnostics.ipynb` (convergence plots, corner plots)

---

### Phase 4: Publication and Dissemination

**Timeline:** 2-3 months (depends on Phase 3 outcome and author agreement)

**Goal:** Share reproducibility methodology and (optionally) MULTING test results with scientific community.

**Current status:**
- ⏸️ Methodology (epi-registry, audit protocol) ready for publication independently
- ⏸️ MULTING test results (Phase 3) depend on author agreement

**Two publication tracks:**

#### Track A: Methodology (Independent of Buckholtz Physics)

**Status:** ✅ Ready to proceed (does not require author permission)

**Assets:**
1. **epi-registry package** (parameter provenance framework)
   - Target venue: JOSS (Journal of Open Source Software)
   - Timeline: 3 months to submission
   - Requirements: ≥3 case studies (MOND done, need 2 more)

2. **Reproducibility audit protocol** (epistemic registry + multi-hypothesis testing)
   - Target venue: ReScience C
   - Timeline: 2 months to submission
   - Requirements: Case study (Buckholtz audit can be example)

**Actions:**
- Complete epi-registry case studies 2-3 (f(R) gravity, SUSY)
- Formal prior art search (arXiv, ACM, IEEE)
- Write methods paper draft (1000 words for JOSS, 3000+ for PLOS ONE)
- Submit to JOSS and/or ReScience C

**Author involvement:** None required (methodology is general, not specific to Buckholtz)

#### Track B: MULTING Test Results (Conditional on Author Agreement)

**Status:** ⏸️ Blocked on Phase 3 + author consent

**Options:**

1. **Co-authored paper** (if MULTING performs well):
   - Venue: ApJ, MNRAS, or Astrophysics & Space Science
   - Authors: Buckholtz + audit team
   - Content: MULTING framework + independent test results

2. **Supplemental material to methodology paper** (if author agrees):
   - Main paper: epi-registry (JOSS) or audit protocol (ReScience C)
   - Supplement: Buckholtz case study as worked example
   - Author credited, but physics claims are secondary to methodology

3. **Private archive** (if author declines publication):
   - Results shared with author only
   - No public release
   - Methodology published separately (Track A)

**Decision criteria:**
- Phase 3 results: MULTING >> ΛCDM → offer co-authorship
- Phase 3 results: ΛCDM >> MULTING → ask author if he wants results published or archived
- Phase 3 results: inconclusive → likely archive, focus on methodology (Track A)

**Author consent required for:**
- ❌ Public release of MULTING test results
- ❌ Buckholtz case study as supplement to methodology paper
- ❌ Any claim about MULTING performance vs ΛCDM

**No author consent required for:**
- ✅ epi-registry package (general methodology)
- ✅ Audit protocol paper (Buckholtz is example, not subject)
- ✅ Talks at conferences about reproducibility methodology

---

## Timeline Summary

| Phase | Duration | Start Condition | End Condition |
|-------|----------|----------------|---------------|
| **Phase 1: Clarification** | 2 weeks | Author response received | H_FLRW baseline + bridge method confirmed |
| **Phase 2: Independent Data** | 2-3 weeks | Phase 1 complete | Pantheon+, BAO, AIC/BIC ready |
| **Phase 3: MCMC** | 3-4 weeks | Phases 1-2 complete + author + user approval | MCMC converged, model comparison done |
| **Phase 4: Publication** | 2-3 months | Phase 3 complete (Track B) OR any time (Track A) | Papers submitted/accepted |

**Total time (if all phases proceed):** 3-4 months

**Most likely path:** Phase 1 (2 weeks) → Phase 2 (parallel, 3 weeks) → Phase 3 blocked → Track A only (3 months)

**Optimistic path:** All phases succeed → Track A + Track B co-authorship (4 months)

**Pessimistic path:** Phase 1 fails (no bridge method) → Archive Buckholtz audit, proceed with Track A only (3 months)

---

## Blockers and Risks

### Critical Blockers (Project Cannot Proceed Without)

| Blocker | Status | Impact | Resolution |
|---------|--------|--------|------------|
| **Bridge method** | ❌ MISSING | Cannot compute H_MULT predictions | Author answers Q2 |
| **H_FLRW baseline** | ❌ UNCLEAR | Cannot fairly compare models | Author answers Q1 OR AI service comparison |
| **H_MULT operational meaning** | ❌ AMBIGUOUS | Cannot interpret results | Author answers Q-operational |

### Non-Critical (Can Proceed Without, But Reduces Quality)

| Blocker | Status | Impact | Workaround |
|---------|--------|--------|-----------|
| **Cluster variables evolution** | ❌ MISSING | Cannot model time-dependent terms | Assume static, document assumption |
| **Independent data** | ⏸️ CAN PROCEED | No out-of-sample test | Integrate Pantheon+, BAO ourselves |
| **Complexity penalty** | ⏸️ CAN PROCEED | Unfair comparison (free parameters) | Implement AIC/BIC ourselves |

### Risks

1. **Scope creep:** MCMC takes 3-4 weeks → delays GeoScan Gold (21 days to deadline)
   - **Mitigation:** Do NOT start Phase 3 until GeoScan Gold complete

2. **Physics publication trap:** Methodology gets bundled with Buckholtz physics → rejected by physics journals → methodology never published
   - **Mitigation:** Track A (methodology) published FIRST, independently. Track B (MULTING results) only as optional supplement.

3. **Author declines MCMC:** We invest 2 months in Phases 1-2, author says "please don't run MCMC"
   - **Mitigation:** Ask author BEFORE Phase 2 if he is open to fair MCMC comparison. If no → skip to Track A.

4. **Results are inconclusive:** MCMC shows MULTING ≈ ΛCDM (statistically indistinguishable)
   - **Mitigation:** Document honestly, publish methodology anyway (Track A). Inconclusive result is still useful (rules out strong claim).

---

## Exit Criteria (When to Archive Project)

**Archive Buckholtz audit (but continue Track A) if:**
- Author declines to answer clarification questions after 30 days
- Author states bridge method is proprietary / cannot be shared
- Phase 1 fails (no bridge method identified)
- Author requests we do not publish MULTING test results
- User decides to prioritize other projects (GeoScan Gold, 24-na-7)

**Archive entire project (including Track A) if:**
- User loses interest in reproducibility methodology
- epi-registry prior art search reveals it's not novel (someone already built this)
- Venues reject methodology papers (unlikely, but possible)

**Proceed to completion if:**
- Phase 1 succeeds (bridge method + H_FLRW baseline confirmed)
- Author agrees to Phase 3 (MCMC comparison)
- User approves time investment (after GeoScan Gold complete)

---

## Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| **Phase 1 completion** | ≤2 weeks | H_FLRW baseline + bridge method documented |
| **Phase 2 completion** | ≤3 weeks | Pantheon+, BAO, AIC/BIC ready |
| **Phase 3 completion** | ≤4 weeks | MCMC converged, model comparison done |
| **Track A publication** | ≤3 months | epi-registry submitted to JOSS |
| **Track B publication** | ≤4 months | Co-authored paper OR supplement |
| **Code quality** | 100% tests pass | pytest -v |
| **Reproducibility** | Independent replication | Another researcher runs our code, gets same results |
| **Transparency** | All code/data public | GitHub repo (or private if author requests) |
| **Fairness** | Same standards for ΛCDM and MULTING | No double standards in model comparison |
| **Respectfulness** | Zero author complaints | Author endorses our approach |

---

## Resource Requirements

### Time

- **Phase 1:** ~10 hours (read Supplementary Materials, write clarification email, update registry)
- **Phase 2:** ~40 hours (integrate Pantheon+, BAO, implement AIC/BIC, test)
- **Phase 3:** ~80 hours (MCMC setup, run, diagnostics, report)
- **Phase 4 Track A:** ~60 hours (case studies 2-3, prior art, paper draft, submission)
- **Phase 4 Track B:** ~40 hours (co-authored paper OR supplement, depends on Phase 3 outcome)

**Total:** ~230 hours (if all phases proceed)  
**Most likely:** ~110 hours (Phase 1-2 + Track A only)

### People

- **Primary:** 1 person (audit team lead)
- **Advisor:** Dr. Buckholtz (clarification questions, optional co-authorship)
- **Reviewers:** 2-3 peer reviewers (JOSS, ReScience C submission)

### Computational

- **MCMC:** ~10-20 CPU hours (4 chains × 10,000 steps, can run overnight)
- **Storage:** ~1 GB (datasets, MCMC chains, figures)
- **No GPU required**

---

## Communication Protocol

### With Author

- **Frequency:** On-demand (author responds when available)
- **Medium:** Email (private), or meeting (if invited)
- **Tone:** Respectful, collaborative, assumes author is expert
- **Content:** Clarification questions, progress updates, draft findings (for review)
- **NOT sent without approval:** Unsolicited emails, public claims, validation/refutation

### With Community (If Track A Proceeds)

- **Venues:** JOSS, ReScience C, conferences (SciPy, JuliaCon, reproducibility workshops)
- **Content:** Methodology (epi-registry, audit protocol), NOT Buckholtz physics
- **Buckholtz involvement:** Credited for inspiring case study, NOT as co-author (unless he requests)

### With Community (If Track B Proceeds)

- **Venues:** ApJ, MNRAS, Astrophysics & Space Science, or supplemental to Track A paper
- **Content:** MULTING test results (ONLY with author consent)
- **Authorship:** Co-authored (if MULTING >> ΛCDM) or supplemental (if author agrees)

---

## Summary

This reproducibility plan is:

- **Phased:** 4 phases, each conditional on prior success
- **Transparent:** All methods, data, code documented
- **Fair:** Same standards for ΛCDM and MULTING
- **Respectful:** Assumes author is expert, seeks clarification not criticism
- **Conditional:** MCMC (Phase 3) only if Phases 1-2 succeed + author agrees
- **Two-track:** Methodology (Track A) independent of Buckholtz physics, MULTING results (Track B) conditional on author consent

**Next immediate action:** Ask author 3 clarification questions (Q1: H_FLRW, Q2: bridge, Q-operational: meaning).

**Timeline:** 2 weeks (Phase 1) → 3 weeks (Phase 2) → DECISION POINT (proceed to Phase 3 or archive Buckholtz audit, continue Track A).

**Expected outcome:** Most likely Track A only (methodology published, Buckholtz audit archived). Optimistic: Track A + Track B co-authorship. Pessimistic: Track A only, epi-registry case study uses different physics theory.

---

**Last updated:** 2026-05-30  
**Status:** DRAFT_FOR_AUTHOR_REVIEW  
**Next action:** Send to Dr. Buckholtz for feedback  
**Related docs:**
- docs/71_author_response_analysis.md (analysis of author's response)
- docs/69_tuesday_meeting_pack_private.md (clarification questions)
- docs/FINAL_WAITING_STATE_MARKER.md (project status)
