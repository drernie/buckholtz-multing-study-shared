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

---

**Files:**
- [NR-009: S³ geometry as Eq.32 mechanism — rejected](20260623-nr009-s3-geometry-eq32-mechanism.md)
- [NR-001/NR-002: constant-eps and powerlaw bridge](20260612-bridge-candidates-fail.md)
- [NR-003: PS comoving density Model A](20260612-ps-comoving-model-a-fail.md)
- [NR-004: MAVS virial+PS insufficient](20260613-mavs-virial-ps-insufficient.md)
- [NR-005: Intrinsic formation vs selection ambiguity](20260613-intrinsic-formation-selection-ambiguity.md)
- [NR-007: Sector count DM/baryon ratio](20260613-nr007-sector-count-dm-baryon-ratio.md)
- [NR-008: Merger-epoch r_P falsified](20260618-nr008-merger-epoch-rP-falsified.md)
