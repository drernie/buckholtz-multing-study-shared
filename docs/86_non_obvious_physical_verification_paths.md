# Non-Obvious Paths to Raise MULTING Physical Verification from 5/10 to 10/10

**Status labels:**
```
INTERNAL_ONLY
RESEARCH_NOTE
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_NOT_REQUIRED
```

**Created:** 2026-05-31  
**Purpose:** Internal research note exploring verification strategies that strengthen physical validation without requiring author clarification or making public claims.

---

## Current Verification State: 5/10

**What we know:**
- ✅ Table A1 structure matches author's description
- ✅ Parameters extracted from supplementary material (3 AI services)
- ✅ H_MULT calculations reproduce within numerical precision
- ✅ Basic dimensional analysis passes
- ✅ Monopole limit behavior correct

**What we don't know:**
- ❌ Which beta set is physically grounded vs phenomenological
- ❌ Bridge method F_oP → H_MULT (5 blockers unresolved)
- ❌ H_FLRW provenance (4/4 spot-checks mismatch Planck-2018)
- ❌ Whether fitted parameters are unique or flexible
- ❌ Model comparison baseline (no AIC/BIC, no independent data)

**Gap:** Current verification = "tables compute correctly" but not "physics is well-specified."

---

## Strategy: Internal Robustness Tests (No Author Required)

The key insight: **many physical verification questions can be answered through negative controls and sensitivity analysis** — without needing author clarification or making validation/refutation claims.

### Principle: Test What Would Break If Physics Were Wrong

Instead of asking "is MULTING correct?" → ask "what would we see if MULTING were under-specified, over-fitted, or flexible?"

---

## Non-Obvious Verification Paths

### Path 1: Row-Permutation Negative Control ⭐ SAFE_NOW

**Question:** Does the fitted table depend on the correct z-ordering, or would any permutation work?

**Method:**
1. Shuffle redshift labels (z) randomly while keeping H-data fixed
2. Refit beta_d, beta_q on shuffled table
3. Repeat 100 times
4. Compare fit quality distribution

**Pass signal:** Original fit significantly outperforms shuffled fits (p < 0.01)

**Fail signal:** Many shuffled fits achieve similar χ² → model is flexible enough to fit noise

**Why non-obvious:** Most researchers assume z-ordering matters but never test it. If model fits equally well with scrambled z → physics is suspect.

**Implementation cost:** 2 hours (100× fit loop)

**Blocker status:** ✅ SAFE_NOW (no author clarification needed, no MCMC required)

---

### Path 2: Randomised Beta Test ⭐ SAFE_NOW

**Question:** Are fitted beta values materially better than random beta pairs in reasonable ranges?

**Method:**
1. Define plausible ranges: beta_d ∈ [0.5, 5.0], beta_q ∈ [0.1, 20.0]
2. Sample 100 random (beta_d, beta_q) pairs uniformly
3. Compute χ² for each random pair vs H-data
4. Compare reported beta values to random distribution

**Pass signal:** Reported beta values in top 10% of random pairs (better than 90% of noise)

**Fail signal:** Many random pairs perform similarly → fit is not well-constrained

**Why non-obvious:** If 30% of random beta pairs fit equally well → parameters are phenomenological, not physically grounded.

**Implementation cost:** 1 hour (vectorized χ² computation)

**Blocker status:** ✅ SAFE_NOW (no author clarification needed)

---

### Path 3: Synthetic ΛCDM Table Test ⭐ SAFE_NOW

**Question:** Can MULTING bridge candidates fit a synthetic ΛCDM H(z) table equally well?

**Method:**
1. Generate synthetic ΛCDM H(z) on same z-grid using H₀=67.4, Ωₘ=0.315
2. Fit candidate bridges to synthetic table
3. Compare fit quality: real table vs synthetic ΛCDM

**Pass signal:** Bridge distinguishes real table from ΛCDM (different χ², different beta)

**Fail signal:** Bridge fits synthetic ΛCDM equally well → model is too flexible

**Why non-obvious:** If MULTING bridge can reproduce standard ΛCDM → it's not testing a distinct hypothesis.

**Implementation cost:** 1.5 hours (synthetic H(z) generation + fit)

**Blocker status:** ✅ SAFE_NOW (no author clarification needed)

---

### Path 4: AIC/BIC Baseline Ladder ⚠️ MODERATE_EFFORT

**Question:** How does MULTING compare to simpler polynomial fits and ΛCDM baseline?

**Method:**
1. Fit nested models to same H-data:
   - M0: Constant H(z) = H₀
   - M1: Linear H(z) = H₀(1 + α·z)
   - M2: Quadratic H(z) = H₀(1 + α·z + β·z²)
   - M3: ΛCDM H(z) with Ωₘ, H₀ free
   - M4: MULTING bridge (current candidate)
2. Compute AIC, BIC for each model
3. Rank by parsimony-corrected fit quality

**Pass signal:** MULTING has lower AIC/BIC than polynomial baselines

**Fail signal:** Simple polynomial fits within 2 AIC units → MULTING doesn't justify complexity

**Why non-obvious:** Most exotic models skip baseline comparison. If quadratic polynomial fits equally well with 2 parameters → why use MULTING with 4+?

**Implementation cost:** 4 hours (5 model fits + AIC/BIC calculation)

**Blocker status:** ⚠️ MODERATE (needs independent H-data integration)

---

### Path 5: Fisher Information Matrix (FIM) / Sloppiness Analysis ⚠️ ADVANCED

**Question:** Which parameters are well-constrained vs poorly constrained (sloppy)?

**Method:**
1. Compute Fisher Information Matrix at best-fit beta values
2. Eigendecompose FIM → identify stiff vs sloppy directions
3. Parameter uncertainty ellipse visualization
4. Sloppiness ratio: max eigenvalue / min eigenvalue

**Pass signal:** All parameters stiff (eigenvalues similar order of magnitude)

**Fail signal:** Sloppiness ratio > 100 → some parameter combinations unconstrained

**Why non-obvious:** Parameters can appear "fitted" but be degenerate. High sloppiness → over-parameterization.

**Implementation cost:** 6 hours (numerical Hessian, eigendecomposition, visualization)

**Blocker status:** ⚠️ ADVANCED (requires stable fitting framework)

---

### Path 6: Cross-Validation on Redshift Bins ⚠️ MODERATE_EFFORT

**Question:** Does the model generalize to held-out redshift regions?

**Method:**
1. Split H-data into 5 redshift bins (train/test split)
2. Fit beta on 4 bins, predict 5th bin
3. Repeat 5-fold cross-validation
4. Compute prediction error on held-out bins

**Pass signal:** Low prediction error on held-out bins (model generalizes)

**Fail signal:** High prediction error → model overfits specific z-regions

**Why non-obvious:** Standard fitting uses all data. Cross-validation tests whether model captures physics vs memorizes data.

**Implementation cost:** 3 hours (5-fold split + refit loop)

**Blocker status:** ⚠️ MODERATE (needs independent H-data integration)

---

### Path 7: Beta Sensitivity to H₀ Prior ⚠️ MODERATE_EFFORT

**Question:** How sensitive are fitted beta values to H₀ anchor choice?

**Method:**
1. Refit beta_d, beta_q for H₀ ∈ [65, 70] in 0.5 km/s/Mpc steps
2. Plot beta(H₀) trajectories
3. Measure dβ/dH₀ sensitivity

**Pass signal:** Beta values stable across H₀ range (low sensitivity)

**Fail signal:** Beta values drift significantly → fit absorbs H₀ uncertainty

**Why non-obvious:** If beta values compensate for wrong H₀ → they're phenomenological tuning parameters, not fundamental.

**Implementation cost:** 2 hours (grid search + visualization)

**Blocker status:** ⚠️ MODERATE (needs H₀ integration in fitting framework)

---

### Path 8: Residual Autocorrelation Test ✅ SAFE_NOW

**Question:** Are fit residuals independent, or do they show systematic trends?

**Method:**
1. Compute residuals: r(z) = H_data(z) - H_MULT(z)
2. Test autocorrelation: Durbin-Watson statistic
3. Plot residuals vs z, look for trends

**Pass signal:** Residuals scatter randomly (DW ≈ 2, no trend)

**Fail signal:** Residuals show systematic pattern → missing physics or wrong functional form

**Why non-obvious:** Good χ² doesn't guarantee residuals are random. Systematic residuals → model misspecification.

**Implementation cost:** 30 minutes (residual plot + DW statistic)

**Blocker status:** ✅ SAFE_NOW

---

### Path 9: Parameter Identifiability via Profile Likelihood ⚠️ ADVANCED

**Question:** Are beta_d and beta_q independently constrained, or are they degenerate?

**Method:**
1. Fix beta_d, refit beta_q → compute profile likelihood L(beta_d)
2. Fix beta_q, refit beta_d → compute profile likelihood L(beta_q)
3. Check for unique minimum vs flat likelihood plateau

**Pass signal:** Sharp likelihood peaks → parameters identifiable

**Fail signal:** Flat likelihood plateau → parameters degenerate (many combinations fit equally well)

**Why non-obvious:** Joint χ² can be low even if individual parameters are poorly identified.

**Implementation cost:** 4 hours (2D likelihood scan + visualization)

**Blocker status:** ⚠️ ADVANCED

---

### Path 10: Out-of-Sample Prediction Test (Pantheon+ Integration) ⚠️ REQUIRES_INTEGRATION

**Question:** Can MULTING predict unseen data (Type Ia SNe from Pantheon+)?

**Method:**
1. Integrate Pantheon+ dataset (SNe distance moduli μ(z))
2. Convert H_MULT(z) → predicted μ(z) via distance-redshift relation
3. Compare predicted μ(z) vs observed μ(z)
4. Compute residual distribution

**Pass signal:** MULTING predictions match Pantheon+ within uncertainties

**Fail signal:** Large systematic offset → model doesn't generalize

**Why non-obvious:** This is the gold standard — but requires independent dataset integration (blocker 3).

**Implementation cost:** 8 hours (Pantheon+ download, distance calculation, comparison)

**Blocker status:** ❌ BLOCKED (requires blocker 3: independent data integration)

---

## Prioritization: Which Paths First?

### SAFE_NOW Tier (0 blockers, can run today)
1. ✅ **Row-permutation negative control** (2h) — Path 1
2. ✅ **Randomised beta test** (1h) — Path 2
3. ✅ **Synthetic ΛCDM table test** (1.5h) — Path 3
4. ✅ **Residual autocorrelation** (30min) — Path 8

**Total effort:** 5 hours  
**Expected outcome:** Raise verification from 5/10 → 7/10 by ruling out under-specification and over-flexibility.

### MODERATE_EFFORT Tier (minor integration needed)
5. ⚠️ **AIC/BIC baseline ladder** (4h) — Path 4
6. ⚠️ **Cross-validation** (3h) — Path 6
7. ⚠️ **Beta sensitivity to H₀** (2h) — Path 7

**Total effort:** 9 hours  
**Expected outcome:** Raise verification to 8/10 by comparing to baselines and testing robustness.

### ADVANCED Tier (requires framework upgrade)
8. ⚠️ **FIM / sloppiness analysis** (6h) — Path 5
9. ⚠️ **Profile likelihood** (4h) — Path 9

**Total effort:** 10 hours  
**Expected outcome:** Raise verification to 9/10 by quantifying parameter identifiability.

### BLOCKED Tier (requires external data)
10. ❌ **Pantheon+ out-of-sample test** (8h) — Path 10

**Blocker:** Requires blocker 3 resolution (independent data integration)  
**Expected outcome:** Raise verification to 10/10 by testing out-of-sample prediction.

---

## Recommended 48-Hour Plan (SAFE_NOW Only)

**Day 1 (4 hours):**
1. Implement row-permutation negative control (2h)
2. Implement randomised beta test (1h)
3. Implement residual autocorrelation test (30min)
4. Document results in docs/87_negative_control_test_plan.md (30min)

**Day 2 (1.5 hours):**
5. Implement synthetic ΛCDM table test (1.5h)

**Total time:** 5.5 hours  
**Deliverable:** docs/88_negative_control_test_results.md  
**Verification increase:** 5/10 → 7/10 (estimated)

---

## What These Tests Do NOT Do

**NOT validation:** These tests do not prove MULTING is correct.

**NOT refutation:** These tests do not prove MULTING is incorrect.

**What they DO:** Test sensitivity, flexibility, and under-specification risk.

**Analogy:** Like stress-testing a bridge before opening it — you don't claim the bridge is safe forever, you just verify it doesn't collapse under known loads.

---

## Integration with Existing Workflow

### Relationship to MCMC Blockers

These tests are **orthogonal** to MCMC blockers:
- MCMC blockers = "can we compare MULTING vs ΛCDM rigorously?"
- Negative controls = "is MULTING specification robust enough to trust?"

**Both are needed.** Even if MCMC blockers are resolved, negative controls prevent false validation from flexible over-fitting.

### Relationship to Author Clarification

These tests are **author-independent:**
- If author clarifies bridge method → run MCMC + negative controls
- If author doesn't clarify → negative controls still add verification value

**Hedge strategy:** Negative controls raise internal confidence regardless of author response.

---

## Success Criteria

**After SAFE_NOW tier (5 hours):**
- ✅ Row-permutation: original fit >> shuffled fits (p < 0.01)
- ✅ Randomised beta: reported beta in top 10% of random pairs
- ✅ Synthetic ΛCDM: MULTING distinguishes real table from synthetic
- ✅ Residuals: no autocorrelation (DW ≈ 2)

**If all 4 pass:** Verification 5/10 → 7/10 (robust against under-specification)

**If any fail:** Document failure mode, reassess whether MULTING is well-specified

---

## Failure Modes and Responses

| Test | Failure Mode | Response |
|------|--------------|----------|
| Row-permutation | Shuffled fits equally good | Model too flexible → needs stronger constraints |
| Randomised beta | Many random pairs fit equally well | Beta not well-constrained → check parameter degeneracy |
| Synthetic ΛCDM | Bridge fits synthetic equally well | Model not distinguishing physics → needs independent prediction |
| Residuals | Systematic trend | Missing physics or wrong functional form → revisit model |

**None of these failures = MULTING refutation.** They signal "specification needs tightening" before stronger claims are made.

---

## Next Step

Create minimal negative-control plan:
→ docs/87_negative_control_test_plan.md

Define 3 tests from SAFE_NOW tier for immediate execution (when approved).

---

**Document status:** INTERNAL_ONLY, RESEARCH_NOTE  
**No public claims, no validation/refutation, no MCMC, no email.**
