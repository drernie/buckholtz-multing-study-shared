# NR-001 / NR-002 — Bridge Candidates FAIL

**Date:** 2026-06-12  
**Gates:** M8-A + M8-A-R1  
**Verdict:** REJECT  
**Commits:** 30473a2 (M8-A), add7cba (M8-A-R1 re-audit, 4 corrections applied)  
**Safety:** OUR_RECONSTRUCTION · NOT_AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION

---

## What Was Tested

Two minimal bridge candidates from ε(z) = (H_MULT/H_FLRW)² − 1:

**Candidate 1 — Constant ε:**  
ε(z) ≈ constant → H_MULT(z) = H_FLRW(z) · √(1 + ε̄)

**Candidate 2 — Power-law ε:**  
ε(z) ≈ A · (1+z)^α

---

## Why They Failed

**NR-001 Constant ε:**
- ε(z) ranges from 0.0481 to 0.2277 — a factor of 4.7×
- Max residual: 0.104 (2.1× the 0.05 heuristic threshold)
- Failed because ε is fundamentally non-constant

**NR-002 Power-law ε:**
- Best-fit α across consecutive z-pairs: spans [−2.22, +9.49]
- **3 sign changes** at z = 0.40, 1.00, 5.00
- A single power law cannot change sign — failed by construction

---

## Mechanistic Insight

**[INSIGHT-1] ε(z) is non-monotonic with multiple characteristic scales.**

The structure is:
```
RISE → PEAK(z=0.40) → FALL → LOCAL_MIN(z=1.00) → SECONDARY_RISE(z=1.50) → FALL → GLOBAL_MIN(z=5.00) → UPTICK(z=8.50)
```

This pattern has at least **3 distinct regimes** and cannot be described by any single-parameter function. It implies:
- The bridge formula involves at least 2 competing processes
- z ≈ 0.40 is a genuine extremum, not a monotone interpolation artifact
- Secondary structure at z=1.0–1.5 suggests a separate physical process active at that epoch

**Implication for author's bridge:** The formula F_oP → H_MULT(z) must produce non-monotonic output even if its inputs are monotone. This requires either (a) a ratio or difference of two monotone functions with different scalings, or (b) a schedule k_A(z) / D_eff(z) that itself peaks near z≈0.40.

**What NOT to retry:** Any bridge with fewer than 2 free parameters. Any monotone bridge. Any bridge that treats ε as constant or as a simple power of (1+z).

---

## Scope

`TABLE_LEVEL_DIAGNOSTIC · OUR_RECONSTRUCTION`  
These are properties of our transcription of Table A1, not of the author's physics.
