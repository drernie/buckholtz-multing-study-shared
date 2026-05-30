# Negative Control Test Plan — SAFE_NOW Tier

**Status labels:**
```
INTERNAL_ONLY
SAFE_NOW
NEGATIVE_CONTROL_PLAN
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_NOT_REQUIRED
```

**Created:** 2026-05-31  
**Purpose:** Minimal test plan for three negative-control tests that can run immediately without author clarification or MCMC.

**Parent document:** docs/86_non_obvious_physical_verification_paths.md

---

## What These Tests Do

**Purpose:** Test whether MULTING table fitting is:
- Sensitive to correct z-ordering (not just fitting noise)
- Better than random parameter guesses (parameters are constrained)
- Distinguishing MULTING physics from standard ΛCDM (not too flexible)

**What these tests are NOT:**
- ❌ NOT validation of MULTING correctness
- ❌ NOT refutation of MULTING physics
- ❌ NOT comparison with ΛCDM (requires MCMC)
- ❌ NOT publication-ready analysis

**What these tests ARE:**
- ✅ Internal robustness checks
- ✅ Under-specification risk assessment
- ✅ Over-flexibility detection
- ✅ Foundation for future stronger verification

---

## Test 1: Row-Permutation Negative Control

### Question

Does the fitted table depend on the correct z-ordering, or would any permutation of redshift labels work equally well?

### Hypothesis

If MULTING bridge encodes real physics → fit quality should degrade significantly when z-ordering is scrambled.

If model is too flexible → fit quality remains similar even with scrambled z-ordering.

### Method

1. **Baseline:** Compute fit quality (χ²) for original table with correct z-ordering
2. **Negative control:** 
   - Shuffle redshift labels (z) randomly while keeping H-data values fixed
   - Refit beta_d, beta_q on shuffled table
   - Compute χ² for shuffled fit
3. **Repeat:** Generate 100 random permutations
4. **Compare:** Histogram of shuffled χ² vs original χ²

### Implementation Pseudocode

```python
# Step 1: Baseline
z_original = table['z']
H_original = table['H_data']
beta_d_orig, beta_q_orig, chi2_orig = fit_bridge(z_original, H_original)

# Step 2: Negative control loop
chi2_shuffled = []
for i in range(100):
    z_shuffled = np.random.permutation(z_original)
    beta_d_shuf, beta_q_shuf, chi2_shuf = fit_bridge(z_shuffled, H_original)
    chi2_shuffled.append(chi2_shuf)

# Step 3: Statistical test
p_value = (chi2_shuffled <= chi2_orig).mean()  # fraction of shuffled fits better than original
```

### Pass Signal

- Original χ² is significantly lower than shuffled distribution (p < 0.01)
- Less than 1% of shuffled fits achieve χ² ≤ χ²_original
- Visual: Original χ² far left of shuffled histogram

**Interpretation:** Model is sensitive to correct z-ordering → physics matters.

### Fail Signal

- Original χ² within shuffled distribution (p > 0.05)
- Many shuffled fits achieve similar or better χ²
- Visual: Original χ² inside shuffled histogram peak

**Interpretation:** Model too flexible → can fit noise regardless of z-ordering.

### Expected Outcome

**If MULTING is well-specified:** PASS (p < 0.001)

**If model is over-flexible:** FAIL (p > 0.05)

### Implementation Time

2 hours (100× fit loop + statistical analysis + visualization)

### Output Artifact

- `results/negative_control_row_permutation.png` (histogram plot)
- Summary statistics in results section below

---

## Test 2: Randomised Beta Test

### Question

Are fitted beta values materially better than random beta pairs sampled from plausible ranges?

### Hypothesis

If beta parameters are well-constrained by physics → reported values should outperform most random guesses.

If beta parameters are poorly constrained → many random pairs fit equally well.

### Method

1. **Define plausible ranges:**
   - beta_d ∈ [0.5, 5.0] (from multi-AI range: 0.78 to 4.5)
   - beta_q ∈ [0.1, 20.0] (from multi-AI range: 0.19 to 18.0)
2. **Baseline:** Compute χ² for reported beta values (from each AI service)
3. **Negative control:**
   - Sample 100 random (beta_d, beta_q) pairs uniformly from ranges
   - Compute χ² for each random pair (no refitting — just evaluate)
4. **Compare:** Percentile rank of reported beta values in random distribution

### Implementation Pseudocode

```python
# Step 1: Define ranges
beta_d_range = [0.5, 5.0]
beta_q_range = [0.1, 20.0]

# Step 2: Baseline
reported_betas = [
    (0.78, 0.19),   # ChatGPT
    (4.5, 18.0),    # Claude
    (4.25, 8.10)    # Gemini
]
chi2_reported = [compute_chi2(bd, bq, z, H) for (bd, bq) in reported_betas]

# Step 3: Negative control
chi2_random = []
for i in range(100):
    bd_random = np.random.uniform(*beta_d_range)
    bq_random = np.random.uniform(*beta_q_range)
    chi2_rand = compute_chi2(bd_random, bq_random, z, H)
    chi2_random.append(chi2_rand)

# Step 4: Percentile rank
for chi2_r in chi2_reported:
    percentile = (chi2_random > chi2_r).mean() * 100
    print(f"Reported χ² better than {percentile:.1f}% of random pairs")
```

### Pass Signal

- Reported beta values in top 10% (better than 90% of random pairs)
- All three AI-service beta sets outperform most random guesses
- Visual: Reported χ² values left of random distribution

**Interpretation:** Beta parameters are constrained → not arbitrary.

### Fail Signal

- Reported beta values in middle 50% (many random pairs perform equally well)
- Less than 70% of random pairs are worse
- Visual: Reported χ² inside random distribution peak

**Interpretation:** Beta parameters poorly constrained → fit is flexible.

### Expected Outcome

**If beta well-constrained:** PASS (reported in top 5-10%)

**If beta arbitrary:** FAIL (reported in middle 50%)

### Implementation Time

1 hour (vectorized χ² computation + percentile analysis + visualization)

### Output Artifact

- `results/negative_control_randomised_beta.png` (scatter plot: beta_d vs beta_q with χ² colormap)
- Summary statistics in results section below

---

## Test 3: Synthetic ΛCDM Table Test

### Question

Can the MULTING bridge candidate fit a synthetic ΛCDM H(z) table equally well as the real table?

### Hypothesis

If MULTING encodes distinct physics → should NOT fit synthetic ΛCDM equally well.

If model is too flexible → can fit any smooth H(z) curve regardless of source.

### Method

1. **Generate synthetic ΛCDM table:**
   - Use Planck-2018 cosmology: H₀ = 67.4 km/s/Mpc, Ωₘ = 0.315, ΩΛ = 0.685
   - Compute H_ΛCDM(z) on same z-grid as real table
   - Formula: H(z) = H₀ √[Ωₘ(1+z)³ + ΩΛ]
2. **Baseline:** Fit bridge to real table → compute χ²_real
3. **Negative control:** Fit bridge to synthetic ΛCDM table → compute χ²_synth
4. **Compare:** χ²_real vs χ²_synth and fitted beta values

### Implementation Pseudocode

```python
# Step 1: Generate synthetic ΛCDM
H0 = 67.4  # km/s/Mpc
Om = 0.315
OL = 0.685

def H_LCDM(z, H0, Om, OL):
    return H0 * np.sqrt(Om * (1 + z)**3 + OL)

z_grid = table['z']
H_synth = H_LCDM(z_grid, H0, Om, OL)

# Step 2: Fit real table
beta_d_real, beta_q_real, chi2_real = fit_bridge(z_grid, table['H_data'])

# Step 3: Fit synthetic ΛCDM table
beta_d_synth, beta_q_synth, chi2_synth = fit_bridge(z_grid, H_synth)

# Step 4: Compare
print(f"Real table: β_d={beta_d_real:.2f}, β_q={beta_q_real:.2f}, χ²={chi2_real:.2f}")
print(f"Synth ΛCDM: β_d={beta_d_synth:.2f}, β_q={beta_q_synth:.2f}, χ²={chi2_synth:.2f}")
print(f"χ² ratio: {chi2_synth / chi2_real:.2f}")
```

### Pass Signal

- χ²_synth >> χ²_real (synthetic ΛCDM fits poorly)
- Fitted beta values differ significantly (real vs synthetic)
- Visual: Large residuals when fitting ΛCDM with MULTING bridge

**Interpretation:** MULTING distinguishes its physics from ΛCDM → not too flexible.

### Fail Signal

- χ²_synth ≈ χ²_real (synthetic ΛCDM fits equally well)
- Fitted beta values similar
- Visual: Small residuals for both real and synthetic

**Interpretation:** Model too flexible → can fit any smooth curve.

### Expected Outcome

**If MULTING distinct:** PASS (χ²_synth / χ²_real > 3)

**If model too flexible:** FAIL (χ²_synth / χ²_real < 1.5)

### Implementation Time

1.5 hours (synthetic H(z) generation + fit + comparison + visualization)

### Output Artifact

- `results/negative_control_synthetic_lcdm.png` (comparison plot: real vs synthetic fit)
- Summary table in results section below

---

## Combined Results Summary (Template)

After running all three tests, populate this table:

| Test | Pass/Fail | Key Metric | Interpretation |
|------|-----------|------------|----------------|
| **Row-permutation** | PASS/FAIL | p-value = ??? | Original fit better/similar to shuffled |
| **Randomised beta** | PASS/FAIL | Percentile = ???% | Reported beta top/middle of random distribution |
| **Synthetic ΛCDM** | PASS/FAIL | χ²_synth / χ²_real = ??? | MULTING distinguishes/doesn't distinguish from ΛCDM |

**Overall assessment:**
- 3/3 PASS → Verification 5/10 → 7/10 (robust against under-specification)
- 2/3 PASS → Verification 5/10 → 6/10 (some concerns, document which test failed)
- 1/3 PASS → Verification remains 5/10 (significant under-specification risk)
- 0/3 PASS → Verification 5/10 → 4/10 (model poorly specified)

---

## What Happens If Tests Fail?

**Failure ≠ MULTING refutation.**

Failure = "specification needs tightening before stronger claims."

### If Row-Permutation Fails

**Signal:** Model too flexible, can fit noise.

**Response:**
1. Check if fitting procedure converges to global minimum
2. Add regularization (L2 penalty on beta values)
3. Reduce number of free parameters
4. Document: "Model under-specified for current fitting framework"

### If Randomised Beta Fails

**Signal:** Beta parameters poorly constrained.

**Response:**
1. Check parameter degeneracy (FIM analysis)
2. Add prior constraints on beta ranges
3. Check if multiple beta pairs produce similar fits
4. Document: "Beta values not uniquely determined by current data"

### If Synthetic ΛCDM Fails

**Signal:** Model too flexible, can't distinguish physics.

**Response:**
1. Need out-of-sample test (Pantheon+ integration)
2. Add model complexity penalty (AIC/BIC)
3. Check if bridge functional form is too generic
4. Document: "MULTING bridge needs tighter physical constraints"

---

## Boundaries (Critical)

### What These Tests Do NOT Claim

1. ❌ **NOT validation:** Passing all tests does NOT prove MULTING is correct.
2. ❌ **NOT refutation:** Failing any test does NOT prove MULTING is incorrect.
3. ❌ **NOT comparison:** These tests do NOT compare MULTING vs ΛCDM rigorously (MCMC blocked).
4. ❌ **NOT publication-ready:** Results are internal robustness checks only.

### What These Tests DO

1. ✅ **Sensitivity check:** Does model depend on correct data structure?
2. ✅ **Constraint check:** Are parameters better than random guesses?
3. ✅ **Flexibility check:** Can model distinguish physics from generic smooth curves?

**Analogy:** Like checking if a scale gives different readings for different weights (sensitivity) vs always showing same number (broken).

---

## Safety Labels (Mandatory)

```
INTERNAL_ONLY
SAFE_NOW
NEGATIVE_CONTROL_PLAN
NO_VALIDATION
NO_REFUTATION
NO_MCMC
NO_PUBLIC_CLAIMS
AUTHOR_NOT_REQUIRED
```

**If user approves execution:**
- Create: `src/negative_control_tests.py` (implementation)
- Create: `results/negative_control_summary.md` (results)
- Update: docs/PROJECT_AUDIT_2026_05_31.md (add negative-control section)

**Do NOT:**
- Run MCMC
- Make validation/refutation claims
- Send email to author
- Make public claims
- Claim these tests prove MULTING correctness

---

## Next Step (Awaiting Approval)

**User decision required:**

1. **Approve implementation** → create `src/negative_control_tests.py`, run 3 tests (5 hours)
2. **Request modification** → adjust test definitions or add/remove tests
3. **Defer** → save plan for later, focus on other priorities (GeoScan Gold)

**Estimated total time:** 5 hours (2h + 1h + 1.5h + 30min documentation)

**Deliverable:** `results/negative_control_summary.md` with PASS/FAIL verdicts and interpretation.

---

**Document status:** PLAN_READY, awaiting user approval for execution.
