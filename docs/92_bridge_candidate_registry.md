# Bridge Candidate Registry — F_oP to H_MULT Mapping Routes

**Status:** TRIAGE COMPLETE  
**Date:** 2026-05-31  
**Purpose:** Catalog all candidate bridges from pairwise force law to cosmological expansion

**MCMC Readiness:** BLOCKED (0/3 testable bridges, 3/3 require author clarification)

---

## Executive Summary

**Problem:** Table A1 reports H_MULT(z) values, but the mapping F_oP to H_MULT is not documented in public materials.

**Bridge candidates identified:** 5 (+ 3 rejected routes)

**Testable without author:** 2/5 (C Proxy, D Hamiltonian — diagnostics only)  
**Requires author clarification:** 5/5 (for physics interpretation)  
**Compatible with negative-control tests:** Partial (C 2/3, D 2/3, B 3/3 if implemented)

**Critical blocker:** All 3 candidates require either:
1. Cluster variable table m_A(z), r_A(z), k_A(z) for all z in Table A1, OR
2. Explicit H_MULT(z; beta_d, beta_q) formula from author, OR
3. Virial averaging prescription confirmation

**Recommendation:** Send clarification brief (docs/26) with explicit questions Q1-Q4.

---

## BOUNDARIES (Critical)

**What this registry does NOT do:**
- NOT validation of MULTING correctness
- NOT refutation of MULTING physics
- NOT selection of best bridge (requires author input)
- NOT fitted-beta validation (beta values are phenomenological)

**What this registry DOES:**
- Catalog possible F_oP to H_MULT routes
- Assess testability of each candidate
- Identify exact clarification questions for author
- Determine which candidates compatible with current diagnostic tests

---

## Candidate A: Heuristic Scaling Formula (AI Transcript)

### Formula
Phi(z) = A_m(z) - A_d(z) + A_q(z)
H_MULT^2(z) = H_anchor^2 × [Phi(z) / Phi(z_anchor)]

### Units
Phi(z): dimensionless, H_MULT(z): km/s/Mpc

### Beta Status
Beta_d and beta_q appear in A_d, A_q (suspected, not confirmed).
Exact functional forms NOT documented.

### Source
AI_TRANSCRIPT_REPORTED (AI-generated materials, NOT manuscript)

### Author-Dependency
CRITICAL - Cannot proceed without:
- H_anchor, z_anchor (Q1c)
- A_m, A_d, A_q definitions (Q1b)
- Cluster variable table m_A(z), r_A(z), k_A(z) (Q4a)

### Testability
BLOCKED - No forward model without cluster variables + anchor values

### Negative-Control Compatibility
Row-perm: YES (if cluster table)
Rand-beta: MAYBE (needs beta mapping)
LCDM: NO (needs full forward model)

---

## Candidate B: Discrete Lattice + Virial Pressure (MVB)

### Formula
Route: F_oP to cluster lattice to virial pressure to Friedmann
P_eff = -⟨r · F_oP⟩ / (3V_cell)
H^2(z) ~ (8πG/3)ρ_eff + virial correction

### Units
P_eff: Pa, ρ_eff: kg/m^3, H(z): km/s/Mpc

### Beta Status
Beta propagates through F_d, F_q:
F_d with r_dA = beta_d × r_A
F_q with |r_qAB|^2 = beta_q^2 × r_A × r_P

### Source
COMPUTATIONAL_RECONSTRUCTION (audit hypothesis, NOT source-confirmed)
This is OUR interpretation, not Buckholtz model (unless author confirms).

### Author-Dependency
CRITICAL - Requires:
- Lattice geometry confirmation (Q_MVB)
- Cluster variables m_A(z), r_A(z), k_A(z) (Q4a)
- Neighbor count, cell volume

### Testability
BLOCKED - Cannot test without author confirmation
Use permission: RESEARCH_HYPOTHESIS only

### Negative-Control Compatibility
Row-perm: YES (if implemented)
Rand-beta: YES (beta in forces)
LCDM: YES (full forward model)
Advantage: Enables all 3 tests if implemented

---

## Candidate C: Simplified Proxy (Current Diagnostic)

### Formula
H(z) ≈ H_0 sqrt[(1+z)^(3(1+beta_d)) + beta_q]

### Units
H(z): km/s/Mpc, beta_d, beta_q: dimensionless

### Beta Status
Beta are direct parameters (not derived from F_oP).
NO relationship to force law - diagnostic proxy only.

### Source
DIAGNOSTIC_PROXY_ONLY (internal tool, NOT MULTING physics)

### Author-Dependency
NONE - this is our diagnostic, not Buckholtz model

### Testability
TESTABLE NOW (already implemented in negative_control_tests.py)
Results: Test 1 PASS, Test 2 FAIL (13%), Test 3 FAIL (ratio~0)

### Negative-Control Compatibility
Row-perm: YES (works)
Rand-beta: YES (works)
LCDM: NO (fails - proxy too generic)

---

## Candidate D: Hamiltonian Bridge (Phenomenological Fit)

### Formula

H-squared z equals H0-squared times omega_k times one plus z squared plus omega_m times one plus z cubed plus omega_d times one plus z to fourth power plus omega_q times one plus z to fifth power

### Units

H z: km/s/Mpc, all omega parameters dimensionless

### Beta Role

Indirect connection speculative: omega_d may relate to beta_d dipole amplitude, omega_q may relate to beta_q quadrupole amplitude. Exact mapping omega_d from beta_d and omega_q from beta_q NOT documented.

### Source

PHENOMENOLOGICAL_FIT from src deep_bridge_diagnostic_fit.py, internal reconstruction. Physical motivation: Hamiltonian H-squared a equals H0-squared times omega_k times a to minus 2 plus omega_m times a to minus 3 plus omega_d times a to minus 4 plus omega_q times a to minus 5. Interpretation: omega_k curvature-like integration constant E, omega_m monopole V_m proportional to a to minus 1, omega_d dipole V_d proportional to a to minus 2, omega_q quadrupole V_q proportional to a to minus 3. NOT found in manuscript AI transcript or author communication. Status internal diagnostic fit algebraic form flexibility check.

### Author-Dependency

MEDIUM. Can fit phenomenologically WITHOUT author BUT physical interpretation requires confirmation. omega_d omega_q to beta_d beta_q mapping unknown. Use permission DIAGNOSTIC_FIT_ONLY NOT physics validation.

### Testability

Status TESTABLE NOW already implemented. Can do: fit omega_k omega_m omega_d omega_q to Table A1 H_obs, compute residuals, compare with LCDM omega_k zero omega_d zero omega_q zero. Cannot do without author: map omega_d omega_q to beta_d beta_q physically, claim this IS MULTING bridge phenomenological fit NOT confirmed, use for prediction fitted to data it would predict. Use permission: ALLOWED_FOR_DIAGNOSTIC_FIT, NOT_ALLOWED_FOR_VALIDATION, NOT_ALLOWED_FOR_MCMC without author confirmation.

### Negative-Control Compatibility

Row-perm YES can shuffle z. Rand-beta NO uses omega not beta directly. LCDM YES can compare omega_d zero omega_q zero nested model. Advantage testable now provides LCDM baseline comparison. Limitation phenomenological fitted omega not derived from F_oP.

### Failure Mode

If omega_d omega_q fitted to zero model collapses to standard LCDM MULTING adds no explanatory power. If omega_d omega_q fitted to large values overfitting risk need AIC BIC penalty. Dimensional consistency PASS all omega dimensionless H has correct units.

---

## Candidate E: Backreaction Framework (Averaging Prescription)

### Formula

Route: inhomogeneous matter distribution to spatial averaging to backreaction Q to effective H_eff z. H_eff squared equals H_FLRW squared plus Q z. Q z equals backreaction term from density fluctuations sigma squared rho over rho squared.

### Units

H_eff km/s/Mpc, Q z km/s/Mpc squared same as H squared.

### Beta Role

Speculative connection: Q z may contain dipole quadrupole contributions. If Q z proportional to function of beta_d beta_q sigma_rho then beta parametrizes fluctuations. Exact Q beta_d beta_q functional form NOT documented.

### Source

RECONSTRUCTION backreaction literature plus MULTING multipole structure. Physical motivation Buchert equations cosmological averaging, backreaction Q from density contrast variance, multipole dipole quadrupole density patterns to non-zero Q. NOT found in manuscript AI transcript or author communication. Status research hypothesis our interpretation.

### Author-Dependency

CRITICAL cannot proceed without confirmation that MULTING uses backreaction framework, Q z functional form, connection Q to beta_d beta_q, spatial averaging scale.

### Testability

Status BLOCKED. Can test IF author confirms: backreaction interpretation is correct, provides Q z formula or averaging prescription, specifies density fluctuation statistics. Cannot test without confirmation: this is literature-based speculation NOT Buckholtz model, no way to compute Q z without averaging prescription. Use permission RESEARCH_HYPOTHESIS our interpretation, NOT_ALLOWED_FOR_MULTING_CLAIMS.

### Negative-Control Compatibility

Row-perm MAYBE if Q z computed from density field. Rand-beta NO Q not directly parameterized by beta. LCDM YES Q zero reduces to LCDM. Advantage physically motivated standard cosmology framework. Disadvantage most speculative zero source evidence from author.

### Failure Mode

If Q z approximately zero backreaction negligible MULTING reduces to LCDM. If Q z requires full N-body simulation computationally prohibitive not reproducible from Table A1 alone. Dimensional consistency PASS Q has H squared units.

---

## Summary Table

| Candidate | Source | Testable? | Author-Dep? | Tests OK | MCMC? | Failure Mode |
|-----------|--------|-----------|-------------|----------|-------|--------------|
| A: Heuristic | AI_TRANSCRIPT | NO | YES (Q1,Q4) | 1/3 | NO | No cluster vars |
| B: Virial | RECONSTRUCTION | NO | YES (Q_MVB,Q4) | 3/3 | NO | Not confirmed |
| C: Proxy | DIAGNOSTIC | YES | NO | 2/3 | NO | Too generic |
| D: Hamiltonian | PHENOMENOLOGICAL | YES | MEDIUM | 2/3 | NO | Fitted omega not derived |
| E: Backreaction | HYPOTHESIS | NO | CRITICAL | 1/3 | NO | Zero source evidence |

Overall status: 2/5 testable now C D but only as diagnostics NOT MULTING validation. MCMC blocked 0/5 physics-confirmed bridges.

---

## Clarification Questions for Dr. Buckholtz

### Priority 1 (CRITICAL)
Q1a: Is H_MULT^2 = H_anchor^2 × [Phi/Phi_anchor] documented?
Q1b: How are A_m, A_d, A_q defined?
Q1c: What are H_anchor, z_anchor values?
Q4a: What are m_A(z_i), r_A(z_i), k_A(z_i) for Table A1 redshifts?

### Priority 2 (MEDIUM)
Q_MVB: Should MULTING be interpreted via discrete lattice + virial pressure?

---

## Decision: Testable Without Author?

VERDICT: 0/5 MULTING-grounded bridges testable without author for physics claims.
2/5 testable now (C Proxy, D Hamiltonian) - but only as diagnostics, NOT MULTING validation.

---

## Eliminated Bridge Families (3 total)

### Family A: Standard FLRW plus Perturbations

Reason: homogeneous averaging nulls dipole quadrupole background contributions. Status DEAD_END wrong regime.

### Family B: Effective w_eff Parametrization

Reason: outcome w_eff table not bridge. Doesn not explain HOW F_oP to H_MULT. Status DEAD_END not a bridge.

### Family C: Post-Newtonian Expansion PN

Why rejected: MULTING force law F_oP operates at Newtonian level monopole dipole quadrupole in one over r one over r cubed one over r to fourth power. Post-Newtonian corrections are O v squared over c squared perturbations to metric NOT force-law modifications. PN framework answers how does GR correct Newtonian gravity NOT how do extra force terms affect cosmology. Wrong regime: PN for strong-field slow-motion binary pulsars, MULTING for cosmological background. Status ELIMINATED regime mismatch.

---

## Recommendations

Immediate:
1. Send clarification brief (docs/26) with Q1-Q4
2. Continue negative-control with Candidate C (diagnostic only)
3. Do NOT implement A or B without author input

If author responds: Implement appropriate candidate
If author silent (30 days): Archive all candidates except C D, extract C D as diagnostic assets, pause audit

---

## What Can Be Inferred WITHOUT Author

### Dimensional Consistency verified independently

CHECK PASS Candidate A Heuristic: Phi dimensionless H squared proportional to Phi PASS.
CHECK PASS Candidate B Virial: P_eff Pa rho kg per cubic meter H km/s/Mpc PASS with G conversion.
CHECK PASS Candidate C Proxy: H km/s/Mpc beta dimensionless PASS.
CHECK PASS Candidate D Hamiltonian: omega dimensionless H km/s/Mpc PASS.
CHECK PASS Candidate E Backreaction: Q km/s/Mpc squared H_eff km/s/Mpc PASS.

All 5 candidates pass dimensional consistency.

### Algebraic Form Constraints

INFERENCE From Table A1 structure 13 rows z zero to z eight point five any valid bridge must: be computable for discrete z values not require continuous z evolution, produce H z in km/s/Mpc range 70 to 500 observed range, reduce to some baseline at z to zero. END INFERENCE

CHECK PASS all 5 candidates satisfy these constraints.

### Testability Hierarchy independent of author

Tier 1 testable now: C Proxy D Hamiltonian.
Tier 2 requires data no confirmation: A Heuristic IF cluster table provided.
Tier 3 requires confirmation: B Virial E Backreaction.

### Negative-Control Compatibility

Full compatibility 3 out of 3 tests: B Virial.
Partial compatibility 2 out of 3: C Proxy D Hamiltonian.
Minimal compatibility 1 out of 3: A Heuristic E Backreaction.

### LCDM Nested Model Check

Contains LCDM as special case:
- A: Phi to 1 no multipole deviation
- B: F_d equals F_q equals zero only monopole
- C: beta_d equals beta_q equals zero power-law collapses
- D: omega_d equals omega_q equals zero standard Friedmann
- E: Q equals zero no backreaction

CHECK PASS all 5 candidates can reduce to LCDM good scientific practice.

---

## What Remains AUTHOR-DEPENDENT

### Critical Dependencies cannot proceed without author

BLOCKER Cluster variables m_A z r_A z k_A z blocks Candidates A B E PRIORITY CRITICAL.
BLOCKER H_anchor z_anchor reference blocks Candidate A PRIORITY CRITICAL.
BLOCKER Bridge method confirmation blocks Candidates B E PRIORITY HIGH.
BLOCKER omega to beta mapping blocks Candidate D PRIORITY MEDIUM.
BLOCKER A_m A_d A_q functional forms blocks Candidate A PRIORITY HIGH.

### Question Priority for Author

Priority 1 CRITICAL blocks Table A1 reproduction:
Q4a For Table A1 redshifts z equals 0.15 to z equals 8.5 what are cluster variables m_A z_i r_A z_i k_A z_i?
Q1c What are H_anchor and z_anchor reference values?

Priority 2 HIGH blocks bridge selection:
Q1a Is heuristic formula H_MULT squared equals H_anchor squared times Phi over Phi_anchor documented?
Q1b How are A_m z A_d z A_q z defined?

Priority 3 MEDIUM enables validation:
Q_MVB Should MULTING be interpreted via discrete lattice plus virial pressure?
Q_Hamiltonian Is there connection omega_d beta_d omega_q beta_q?
Q_Backreaction Does MULTING use backreaction framework?

### Physical Interpretation Dependencies

Without author confirmation we CANNOT claim: which candidate IS the Buckholtz bridge, whether Candidate D omega values ARE beta_d beta_q, whether Candidate B virial interpretation IS intended, whether Candidate E backreaction IS the framework.

We CAN say: Candidate C is our diagnostic proxy NOT MULTING. Candidate D is phenomenological fit NOT source-confirmed. Candidates A B E are hypotheses require confirmation.

---

**Status:** REGISTRY_COMPLETE (5 candidates 3 eliminated families)
**Testable now:** 2/5 (C diagnostic D phenomenological)
**Author-dependent:** 5/5 (for physics interpretation)
**MCMC:** BLOCKED (0/5 physics-confirmed bridges)
**Safety:** INTERNAL_ONLY, NO_VALIDATION, NO_REFUTATION, NO_MCMC
**Next action:** Send Q1c Q4a to author OR continue diagnostic work with C D
