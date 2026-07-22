# Null Results Index — Buckholtz IDM/MULTING Audit

**Protocol:** Falsification Ladder (FL) — Full-Ladder REJECT registry  
**Rule:** Do NOT retry a REJECT entry without fundamentally different approach.  
**Extended:** Each entry includes `## Mechanistic Insight` — what the failure reveals about the mechanism.

---

| ID | Date | Slug | Verdict | Why falsified (10 words) |
|----|------|------|---------|--------------------------|
| NR-001 | 2026-06-12 | constant-eps-bridge | REJECT | ε(z) varies 4.7×; constant bridge max residual 0.104 |
| NR-002 | 2026-06-12 | powerlaw-bridge | REJECT | α has 3 sign changes; not a power law |
| NR-003 | 2026-06-12 | ps-comoving-density-model-a | REJECT | PS comoving density monotone; cannot peak at z=0.40 |
| NR-004 | 2026-06-13 | mavs-virial-ps-insufficient | REJECT | virial k_A monotone ∝H(z)^(4/3); all Pearson r negative |
| NR-005 | 2026-06-13 | intrinsic-formation-selection-ambiguity | REJECT (partial) | PS density killed; selection f_sel alone r=0.666 survives |
| NR-007 | 2026-06-13 | sector-count-dm-baryon-ratio | REJECTED_AS_DERIVATION | Author "might suggest" only; 5 required mechanisms all missing |
| NR-008 | 2026-06-18 | merger-epoch-rP-falsified | REJECT | r_P merger correction r=0.682 < 0.75; secondary z=8.5 bump unsolvable by single component |
| NR-009 | 2026-06-23 | s3-geometry-eq32-mechanism | REJECT | (4/3)=(n+1)/n & 12=n(n+1) at n=3 = post-hoc relabeling; ~456 simple (p,h) families coincide |
| NR-010 | 2026-07-01 | cluster-mass-bias-test | KILL | r(delta_M, M_gas×T_x)=0.021 p=0.88; correlation absent; direction reversed (hot clusters show LESS bias) |
| NR-011 | 2026-07-01 | h1d-mass-threshold | KILL | partial r identical high/low mass (−0.732 vs −0.731); Fisher z p=0.498; no mass-threshold effect |
| NR-012 | 2026-07-01 | h1c-morphology-mediator | KILL | partial r unchanged after controlling wX (−0.726 vs −0.714 baseline); morphology does not mediate |
| NR-013 | 2026-07-13 | r011-beta-profile-nesting | REJECTED WITHIN IMPLEMENTATION | true eta_q profile + eta_q→∞ closed form both ≤ Q(0,0)=0.7334; old "optimum" 0.6235 was a box-excluded-baseline artifact |
| NR-014 | 2026-07-17 | h1e-agn-feedback-confound | KILL | r(delta_M,E_ICM\|M_WL,K0)=-0.7181 p=1.33e-08; AGN feedback does not mediate; 4/4 standard-physics alternatives now killed |
| NR-015 | 2026-07-18 | tx-shared-variable-artifact | WEAKENED (mechanism unresolved) | r(delta_M,M_gas\|M_WL,T_X)=-0.08 p=0.58, signal vanishes once T_X controlled; T_X alone r=-0.81 stronger than E_ICM itself; reclassifies NR-011/012/014's "robust to 4 confounds" framing as overclaim. NOTE: file's own "ARTIFACT-CONFIRMED" first-draft label was retired 2026-07-18 by skeptic review — do not cite it |
| NR-016 | 2026-07-19 | shtanov-bridge-naive-mapping | REJECT | phi=V/(m_A m_P) not universal kernel; B,C depend on per-cluster k_A/m_A, k_P/m_P not just m_A*m_P product |
| NR-017 | 2026-07-22 | 79-17-rg-boundary-condition | REJECT | tan²θ_W(m_Z)=0.301 already exceeds target 2/7=0.286, runs monotonically AWAY with scale; no non-post-hoc high-scale μ* exists; companion to T3b's same-day pole-mass REJECT — exhausts 7:9:17's mechanism search |

---

**Files:**
- [NR-009: S³ geometry as Eq.32 mechanism — rejected](20260623-nr009-s3-geometry-eq32-mechanism.md)
- [NR-001/NR-002: constant-eps and powerlaw bridge](20260612-bridge-candidates-fail.md)
- [NR-003: PS comoving density Model A](20260612-ps-comoving-model-a-fail.md)
- [NR-004: MAVS virial+PS insufficient](20260613-mavs-virial-ps-insufficient.md)
- [NR-005: Intrinsic formation vs selection ambiguity](20260613-intrinsic-formation-selection-ambiguity.md)
- [NR-007: Sector count DM/baryon ratio](20260613-nr007-sector-count-dm-baryon-ratio.md)
- [NR-008: Merger-epoch r_P falsified](20260618-nr008-merger-epoch-rP-falsified.md)
- [NR-010: H1a cluster ICM thermal energy — killed](20260701-nr010-cluster-mass-bias-test.md)
- [NR-011: H1d mass-threshold — killed](20260701-nr011-h1d-mass-threshold.md)
- [NR-012: H1c morphology mediator — killed](20260701-nr012-h1c-morphology-mediator.md)
- [NR-013: R011 beta_d/beta_q profile vs nested monopole — rejected within implementation](20260713-nr013-r011-beta-profile-nesting.md)
- [NR-014: H1e AGN feedback confound — killed](20260713-nr014-h1e-agn-feedback-confound.md)
- [NR-015: T_X shared-variable artifact — reclassifies NR-011/012/014](20260718-nr015-tx-shared-variable-artifact.md)
- [NR-017: 7:9:17 RG boundary condition — rejected, exhausts mechanism search](20260722-nr017-79-17-rg-boundary-condition.md)
