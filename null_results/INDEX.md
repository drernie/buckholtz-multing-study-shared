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

---

**Files:**
- [NR-001/NR-002: constant-eps and powerlaw bridge](20260612-bridge-candidates-fail.md)
- [NR-003: PS comoving density Model A](20260612-ps-comoving-model-a-fail.md)
- [NR-004: MAVS virial+PS insufficient](20260613-mavs-virial-ps-insufficient.md)
- [NR-005: Intrinsic formation vs selection ambiguity](20260613-intrinsic-formation-selection-ambiguity.md)
