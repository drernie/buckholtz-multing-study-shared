# Bridge Candidate Registry — F_oP to H_MULT Mapping Routes

**Status:** TRIAGE COMPLETE  
**Date:** 2026-05-31  
**Purpose:** Catalog all candidate bridges from pairwise force law to cosmological expansion

**MCMC Readiness:** BLOCKED (0/3 testable bridges, 3/3 require author clarification)

---

## Executive Summary

**Problem:** Table A1 reports H_MULT(z) values, but the mapping F_oP to H_MULT is not documented in public materials.

**Bridge candidates identified:** 3 (+ 2 rejected routes)

**Testable without author:** 0/3  
**Requires author clarification:** 3/3  
**Compatible with negative-control tests:** 1/3 (Candidate C - simplified proxy)

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

## Summary Table

| Candidate | Testable? | Author-Dep? | Tests OK | MCMC? |
|-----------|-----------|-------------|----------|-------|
| A: Heuristic | NO | YES (Q1,Q4) | 1/3 | NO |
| B: Virial | NO | YES (Q_MVB,Q4) | 3/3 | NO |
| C: Proxy | YES | NO | 2/3 | NO |

Overall MCMC readiness: 0/3

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

VERDICT: 0/3 MULTING-grounded bridges testable without author.
Only Candidate C (proxy) testable - but NOT MULTING bridge, just diagnostic.

---

## Recommendations

Immediate:
1. Send clarification brief (docs/26) with Q1-Q4
2. Continue negative-control with Candidate C (diagnostic only)
3. Do NOT implement A or B without author input

If author responds: Implement appropriate candidate
If author silent (30 days): Archive A+B, extract C as asset, pause audit

---

**Status:** TRIAGE_COMPLETE
**MCMC:** BLOCKED (0/3 testable)
**Safety:** INTERNAL_ONLY, NO_VALIDATION, NO_REFUTATION, NO_MCMC
