# Bridge Discovery Lab — Plan for Collaborative H_MULT Formula Search

**Date:** 2026-05-31  
**Purpose:** Outline approach for finding explicit H_MULT(z) calculation method  
**Status:** INTERNAL PLAN — not sent to author

**Safety Labels:**
```
NOT_VALIDATION
NOT_REFUTATION
NOT_MCMC
NO_PUBLIC_CLAIMS
NO_AUTHOR_ERROR_CLAIMS
COLLABORATIVE
METHODOLOGY_FOCUS
```

---

## Core Premise (Two Branches)

We can assist Dr. Buckholtz in one of two ways — **author chooses which applies:**

### Branch A: Reproduce Existing Procedure

**If author has a documented H_MULT calculation procedure:**
- Provide the formula or algorithm
- We implement it exactly as specified
- Compare our output vs. Table A1 (all 3 AI services)
- Document numerical precision and any discrepancies
- **Role:** Reproducibility verification

### Branch B: Co-Discover / Formalize Exploratory Method

**If Table A1 was generated exploratorily (AI services found patterns, no pre-specified formula):**
- We search for explicit formula that matches Table A1 outputs
- Test candidate formulas against dimensional analysis, negative controls, symbolic regression
- Present candidate formulas to author for review
- Author confirms or adjusts based on physical intuition
- **Role:** Collaborative formalization

**Both branches are legitimate scientific work.** Neither assumes error or incompleteness on author's part.

---

## Author-Facing Paragraph (For Potential Email)

> "We can help in two ways: (A) If you have a documented procedure for calculating H_MULT from F_oP, we can implement it and verify reproducibility across the three AI-service outputs. (B) If Table A1 emerged exploratorily (AI services found patterns without a pre-specified formula), we can work together to formalize an explicit calculation method — searching candidate formulas, testing them against your physical constraints, and presenting options for your review. Either approach is fine and both are standard practice in computational science. Let us know which fits your workflow."

---

## Required Inputs (Branch A or B)

To proceed with either branch, we need values for the following variables at each redshift in Table A1:

### Core Cosmological Variables

| Variable | Description | Source | Units | Status |
|----------|-------------|--------|-------|--------|
| **z** | Redshift | Table A1 | dimensionless | ✅ HAVE (12 values, z=0 to z=8.5) |
| **H_FLRW** | Standard Friedmann baseline | Table A1 | km/s/Mpc | ✅ HAVE (but provenance unclear) |
| **H_MULT** | MULTING expansion rate | Table A1 | km/s/Mpc | ✅ HAVE (target to reproduce) |

### Beta Parameters

| Variable | Description | Source | Units | Status |
|----------|-------------|--------|-------|--------|
| **beta_d** | Dipole amplitude | Table A1 caption | dimensionless | ✅ HAVE (ChatGPT: 0.78, Claude: 4.5, Gemini: 4.25) |
| **beta_q** | Quadrupole amplitude | Table A1 caption | dimensionless | ✅ HAVE (ChatGPT: 0.19, Claude: 18.0, Gemini: 8.10) |

### Cluster Variables (MISSING — Blocker 2)

| Variable | Description | Source | Units | Status |
|----------|-------------|--------|-------|--------|
| **m_A(z)** | Cluster mass at redshift z | ??? | kg or M_sun | ❌ MISSING |
| **r_A(z)** | Cluster radius at redshift z | ??? | m or Mpc | ❌ MISSING |
| **k_A(z)** | Number of clusters at redshift z | ??? | count | ❌ MISSING |

### Force Law Components (Derived or Provided?)

| Variable | Description | Source | Units | Status |
|----------|-------------|--------|-------|--------|
| **F_m** | Monopole force | F_oP formula | N | ❓ Can derive if m_A, r_A known |
| **F_d** | Dipole force | F_oP formula | N | ❓ Can derive if m_A, r_A, beta_d known |
| **F_q** | Quadrupole force | F_oP formula | N | ❓ Can derive if m_A, r_A, beta_q known |

### Heuristic Scaling Variables (If Branch A uses this method)

| Variable | Description | Source | Units | Status |
|----------|-------------|--------|-------|--------|
| **Phi(z)** | Amplitude function Phi = A_m - A_d + A_q | AI transcript | dimensionless | ❌ MISSING (A_m, A_d, A_q undefined) |
| **H_anchor** | Reference H value at anchor redshift | ??? | km/s/Mpc | ❌ MISSING (Blocker 1) |
| **z_anchor** | Reference redshift | ??? | dimensionless | ❌ MISSING (Blocker 1) |

**Summary:** We have 5/13 required inputs. Missing: cluster variables (3), amplitude terms (3), anchor values (2).

---

## Bridge Formula Families (Search Space for Branch B)

If we proceed with Branch B (co-discovery), we test the following candidate formula families:

### Family 1: Heuristic Scaling (AI Transcript Hypothesis)

**Formula:**
```
Phi(z) = A_m(z) - A_d(z) + A_q(z)
H_MULT²(z) = H_anchor² × [Phi(z) / Phi(z_anchor)]
```

**Source:** AI_TRANSCRIPT_REPORTED  
**Status:** Requires A_m, A_d, A_q definitions + anchor values  
**Dimensional check:** PASS (Phi dimensionless, H has correct units)

### Family 2: Virial Pressure Bridge (Computational Reconstruction)

**Formula:**
```
P_eff = -⟨r · F_oP⟩ / (3V_cell)
H²(z) ~ (8πG/3)ρ_eff + virial_correction
```

**Source:** RECONSTRUCTION (Buchholtz + discrete lattice hypothesis)  
**Status:** Requires cluster variables + lattice geometry confirmation  
**Dimensional check:** PASS (P in Pa, ρ in kg/m³, H in km/s/Mpc with G conversion)

### Family 3: Simplified Power-Law Proxy (Diagnostic Only)

**Formula:**
```
H(z) ≈ H₀ √[(1+z)^(3(1+β_d)) + β_q]
```

**Source:** DIAGNOSTIC_PROXY_ONLY (internal tool, NOT MULTING)  
**Status:** TESTABLE NOW (already implemented)  
**Dimensional check:** PASS  
**Limitation:** Too generic (fits synthetic ΛCDM equally well)

### Family 4: Phenomenological Hamiltonian Ansatz

**Formula:**
```
H²(z) = H₀² [Ω_k(1+z)² + Ω_m(1+z)³ + Ω_d(1+z)⁴ + Ω_q(1+z)⁵]
```

**Source:** PHENOMENOLOGICAL_FIT (inspired by Hamiltonian structure)  
**Status:** TESTABLE NOW (can fit Ω parameters to Table A1)  
**Dimensional check:** PASS (all Ω dimensionless)  
**Limitation:** Fitted Ω, not derived from F_oP → needs physical interpretation

### Family 5: Backreaction Framework

**Formula:**
```
H_eff²(z) = H_FLRW²(z) + Q(z)
Q(z) = backreaction term from density fluctuations
```

**Source:** RECONSTRUCTION (Buchert equations + multipole structure)  
**Status:** BLOCKED (requires Q(z) functional form from author)  
**Dimensional check:** PASS (Q has H² units)

### Family 6: Direct Beta Parametrization

**Formula:**
```
H(z) = H₀ [1 + f_d(z, β_d) + f_q(z, β_q)]
where f_d, f_q are smooth functions of z and beta
```

**Source:** SERGEY_RECONSTRUCTED (symbolic regression target)  
**Status:** Search for f_d, f_q via genetic programming / PySR  
**Dimensional check:** Requires f_d, f_q dimensionless

### Family 7: Effective Equation of State (w_eff Bridge)

**Formula:**
```
H²(z) = H₀² Ω_m(1+z)³[1 + w_eff(z)]
w_eff(z) = w₀ + w_a z/(1+z) + w_d β_d + w_q β_q
```

**Source:** SERGEY_RECONSTRUCTED (phenomenological EoS with beta coupling)  
**Status:** Can fit to Table A1, but may be under-constrained  
**Dimensional check:** PASS (w_eff dimensionless)

---

## Validation Gates (Applied to Any Candidate Formula)

Once we have a candidate formula (from Branch A or discovered in Branch B), it must pass 4 gates:

### Gate 1: Dimensional Consistency Check

**Test:** Verify all terms have correct units (H in km/s/Mpc, forces in N, masses in kg, etc.)  
**Tool:** Automated dimensional analysis script  
**Pass criteria:** No dimensional mismatches  
**Cost:** 5 minutes  
**Blocker:** None

### Gate 2: Symbolic Regression Validation

**Test:** Use PySR (symbolic regression) to search for formulas matching Table A1 H_MULT  
**Tool:** PySR genetic programming on (z, H_FLRW, beta_d, beta_q) → H_MULT  
**Pass criteria:** PySR finds formula with RMSE < 5 km/s/Mpc AND formula matches candidate structure  
**Cost:** 2-4 hours compute time  
**Blocker:** Requires H_FLRW provenance clarity (which baseline was used?)

**Why useful:** If symbolic regression independently finds same formula family → strong evidence formula is data-driven, not arbitrary.

### Gate 3: Negative-Control Battery

**Test:** Same 3 tests from docs/91:
1. Row-permutation: Original fit >> shuffled fits (p < 0.01)
2. Randomized beta: Candidate beta in top 10% of random pairs
3. Synthetic ΛCDM: Candidate distinguishes real table from ΛCDM

**Pass criteria:** 2/3 tests PASS (at least row-permutation + one other)  
**Cost:** 1 hour  
**Blocker:** None (can run now with any candidate)

### Gate 4: Author Review

**Test:** Present candidate formula to author with:
- Derivation (if Branch B) or implementation (if Branch A)
- Dimensional analysis
- Negative-control results
- Comparison with AI-service outputs

**Pass criteria:** Author confirms "yes this is my intended method" OR "yes this formalization captures the physics"  
**Cost:** 1 email round-trip  
**Blocker:** Requires author response

**Final decision authority:** Author, not us.

---

## Contribution Policy (Source Labeling)

Every formula, parameter, or result must be labeled with its source:

| Label | Meaning | Example |
|-------|---------|---------|
| **SOURCE_CONFIRMED** | Author explicitly documented this | "F_oP force law from manuscript Eq. 3" |
| **AUTHOR_PROVIDED** | Author gave us this value in response to our question | "H_anchor = 70.5 km/s/Mpc (email 2026-06-01)" |
| **AI_INFERRED** | Found in AI-service transcript, not in manuscript | "Heuristic scaling Phi formula (ChatGPT transcript)" |
| **SERGEY_RECONSTRUCTED** | We derived/fitted this from available data | "Phenomenological Hamiltonian fit (our work)" |
| **DIAGNOSTIC_ONLY** | Internal tool, NOT claimed to represent MULTING | "Simplified proxy H(z) (diagnostic)" |

**Rule:** Never claim SERGEY_RECONSTRUCTED as SOURCE_CONFIRMED. Always mark provenance honestly.

**Use case:** If we find a formula via symbolic regression (Branch B), label it **SERGEY_RECONSTRUCTED** until author reviews and confirms → then upgrade to **AUTHOR_PROVIDED** or **SOURCE_CONFIRMED** depending on his response.

---

## Workflow (Branch B: Co-Discovery)

If author chooses Branch B (formalize exploratory method), here's the step-by-step:

### Step 1: Gather Missing Inputs (1 email round-trip)

Send docs/93 questions (already drafted) to get:
- Cluster variables m_A(z), r_A(z), k_A(z)
- Anchor values H_anchor, z_anchor (if applicable)
- Amplitude definitions A_m(z), A_d(z), A_q(z) (if applicable)

**Fallback if no response:** Proceed with symbolic regression on (z, H_FLRW, beta_d, beta_q) → H_MULT without cluster variables. Acknowledge limitation.

### Step 2: Run Symbolic Regression (PySR)

**Input:** Table A1 (z, H_FLRW, H_MULT, beta_d, beta_q) for all 3 AI services  
**Output:** Top 10 candidate formulas ranked by Pareto frontier (complexity vs. error)  
**Cost:** 2-4 hours compute  
**Tool:** PySR with custom operators (powers, sqrt, exp, trig)

**Example output:**
```
Rank 1: H = H_FLRW * (1 + 0.05*beta_d*z + 0.02*beta_q*z²)  [RMSE=3.2 km/s/Mpc, complexity=5]
Rank 2: H = H_FLRW * sqrt(1 + beta_d*(1+z) + beta_q*(1+z)²)  [RMSE=4.1 km/s/Mpc, complexity=7]
Rank 3: H = H₀ * (1+z)^(0.5 + 0.1*beta_d) * (1 + beta_q)  [RMSE=5.8 km/s/Mpc, complexity=6]
```

### Step 3: Dimensional Analysis + Negative Controls

For each candidate from PySR:
- **Gate 1:** Check dimensions → filter out physically impossible formulas
- **Gate 3:** Run negative-control battery → filter out over-flexible formulas

**Expected outcome:** 2-3 surviving candidates (passed dimensional + negative-control gates)

### Step 4: Manual Physics Check

For surviving candidates:
- Does formula reduce to ΛCDM when beta_d = beta_q = 0?
- Does formula have monopole limit (beta_d = beta_q = 0 → H = H_FLRW)?
- Are there unphysical singularities or runaway behavior at high z?
- Can formula be connected to F_oP force law (even if speculatively)?

**If yes to all 4:** Candidate is **physically plausible** (not just statistically fitted).

### Step 5: Author Review (Gate 4)

Present 2-3 surviving candidates to author:

> "We searched for explicit formulas matching Table A1 using symbolic regression. Three candidates passed dimensional analysis and negative-control tests:
>
> **Candidate 1:** H = H_FLRW × (1 + f₁(z, β_d, β_q))  
> **Candidate 2:** H = H₀ × g(z, β_d, β_q)  
> **Candidate 3:** H = [H_FLRW² + Q(z, β_d, β_q)]^(1/2)
>
> Do any of these match your intended calculation method? If not, we can refine the search with additional physical constraints you provide."

**Author options:**
- (a) "Yes, Candidate 2 is correct" → we implement and verify
- (b) "Close, but adjust term X" → we refine and re-test
- (c) "None match, here's the actual formula" → we implement Branch A
- (d) "I don't have a formula, let's pick Candidate 1" → collaborative formalization

**All 4 outcomes are legitimate.**

---

## Workflow (Branch A: Reproduce Existing Procedure)

If author provides explicit formula or algorithm:

### Step 1: Implement Exactly As Specified

No modifications, no "improvements". Code review focused on:
- Correct transcription of formula
- Correct units and constants
- Correct numerical precision

### Step 2: Run on All 3 AI-Service Inputs

Compute H_MULT for:
- ChatGPT inputs (beta_d=0.78, beta_q=0.19, H_FLRW from ChatGPT table)
- Claude inputs (beta_d=4.5, beta_q=18.0, H_FLRW from Claude table)
- Gemini inputs (beta_d=4.25, beta_q=8.10, H_FLRW from Gemini table)

### Step 3: Compare Outputs

| Service | Our H_MULT | Table A1 H_MULT | MAE | Max Error |
|---------|-----------|-----------------|-----|-----------|
| ChatGPT | [computed] | [from table] | ??? | ??? |
| Claude | [computed] | [from table] | ??? | ??? |
| Gemini | [computed] | [from table] | ??? | ??? |

**Pass criteria:** MAE < 5 km/s/Mpc for at least one service (numerical precision)

### Step 4: Document Discrepancies (If Any)

If MAE > 5 km/s/Mpc for any service:
- Check if H_FLRW baseline mismatch (our 6-baseline test showed provenance unclear)
- Check if rounding/truncation differences
- Check if formula version mismatch (author may have updated formula between AI sessions)

**Report findings to author without claiming "error" — just "numerical discrepancy, help us understand why."**

---

## Required Input Checklist (For User Before Proceeding)

Before we can execute either Branch A or Branch B, verify we have:

**Minimum required (Branch A):**
- [ ] Explicit H_MULT formula or algorithm from author
- [ ] Values for all variables in formula (m_A, r_A, k_A, H_anchor, z_anchor, A_m, A_d, A_q if used)
- [ ] Clarification on which AI-service output is "reference" (ChatGPT/Claude/Gemini)

**Minimum required (Branch B):**
- [ ] Table A1 H_MULT values (already have)
- [ ] H_FLRW provenance clarity (which baseline was used?) — currently MISSING
- [ ] Beta values (already have from 3 services)
- [ ] PySR installed and tested
- [ ] Author confirmation that exploratory formalization is acceptable

**Currently HAVE:** 5/13 inputs  
**Currently MISSING:** 8/13 inputs (blockers: cluster variables, anchor values, amplitude definitions, H_FLRW provenance)

**Action:** Send docs/93 to get missing inputs OR proceed with symbolic regression on limited data and acknowledge limitations.

---

## Timeline Estimate

### Branch A (Reproduce)
- **If author provides formula + all inputs:** 1-2 days implementation + testing
- **If missing inputs:** blocked until inputs provided

### Branch B (Co-Discover)
- **With full inputs (cluster vars, anchor values):** 3-5 days (PySR run + validation + author review)
- **With limited inputs (z, H_FLRW, beta only):** 2-3 days (symbolic regression + caveats)

**Blocker:** Both branches blocked by missing inputs. docs/93 questions must be answered first.

---

## Safety Boundaries (Critical)

**What this plan does NOT do:**
- ❌ NOT claim author lacks a formula
- ❌ NOT claim we "found the correct formula" without author confirmation
- ❌ NOT validate or refute MULTING physics
- ❌ NOT run MCMC model comparison
- ❌ NOT make public claims

**What this plan DOES:**
- ✅ Offer two collaboration modes (reproduce OR co-discover)
- ✅ Respect author's authority as final decision-maker
- ✅ Label all contributions honestly (source-confirmed vs reconstructed)
- ✅ Apply validation gates to any candidate formula
- ✅ Document methodology transparently

---

## Next Step (Awaiting User Decision)

**Option 1:** Send docs/93 to author → await response → execute Branch A or B based on response

**Option 2:** Proceed with Branch B (symbolic regression) on limited data → document limitations → present results for author review

**Option 3:** Pause Buckholtz work → focus on GeoScan Gold (21 days to blind test)

**User chooses.**

---

**Status:** PLAN_READY  
**Branch A readiness:** BLOCKED (missing formula + inputs)  
**Branch B readiness:** PARTIAL (can run symbolic regression, but with caveats due to missing H_FLRW provenance)  
**Next action:** User approval to send docs/93 OR proceed with limited-data symbolic regression
