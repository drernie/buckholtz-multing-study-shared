# Decision: 20260627-f4-eq32-synthesis

**Date:** 2026-06-27  
**Verdict:** PROMOTE (with [SPECULATIVE MECHANISM] qualifier)

## Evidence summary

### Look-Elsewhere Audit [VERIFIED-BASH]
- 83,160 formulas scanned: (p/q)(m_i/m_j)^n, p,q≤10, n≤24, 11 particles
- **Eq.32 rank: #1** at 0.0135% error
- Next best: `(7/5)(m_t/m_s)^13` at 0.2985% — **22× worse**
- Within 0.1%: **only Eq.32** (1 of 83,160 = p < 0.00002)
- Within 1%: 5 formulas (p = 0.0001)
- Interpretation: Eq.32 is NOT a look-elsewhere artifact at any reasonable threshold

### Exceptional algebraic coincidences [VERIFIED-MATH]
Three independent appearances of n=12 in F₄/G₂ structure:
1. `|roots(G₂)| = 12`
2. `|W(G₂)| = 12`
3. Max Casimir degree of F₄ = 12

Factor 4/3: `dim(Spin(9))/dim(J₃(O)) = 36/27 = 4/3` [SPECULATIVE as mechanism]

### Null results as cross-checks [VERIFIED-BASH]
- **EXP-H:** No quark-sector analog → consistent with J₃(O) being lepton-sector specific
- **EXP-Q reinterpreted:** G₂→8+3+3̄ under SU(3) = correct QCD content, wrong expectation killed
- **Koide bridge:** falsified (nearest miss 12.5%)

## Skeptic concerns

| Concern | Response | Status |
|---------|----------|--------|
| 4/3 = 36/27 is post-hoc labeling | Correct — dimension-ratio is candidate motif, not theorem | Accepted limitation |
| τ/e from J₃(O) uses fitted parameters (Singh 2024) | Correct — chain is incomplete | Documented in caveats |
| F₄ as mechanism not derived | Correct — C10 stays [HYPOTHESIS] | Accepted limitation |
| Top-quark formulas appear in top-5 | Yes, but all at >0.3% vs 0.0135% for Eq.32 | Dismissed — 22× gap |

## What to add to paper

**Discussion section** — new paragraph (marked [SPECULATIVE]):

The Look-Elsewhere Audit upgrades the claim from "possible coincidence" to
"structural anomaly": Eq.32 is unique at 0.1% precision over 83,160 candidate
formulas, with empirical p < 0.00002 at that threshold.

The three components {4/3, 12, τ/e} each map to F₄ = Aut(J₃(O)) structures —
but as correlation, not derivation. Paper should present this as a direction for
future theoretical work, not a proven mechanism.

## Claim entropy at close

| Source of entropy | Start | End |
|-------------------|-------|-----|
| Look-elsewhere risk | HIGH | ZERO (rank #1, p<0.00002) |
| Koide ambiguity | HIGH | ZERO (falsified) |
| Mechanism claim | LOW (was hypothesis) | LOW (still hypothesis) |
| 4/3 origin | SPECULATIVE | SPECULATIVE |
| τ/e derivation | SPECULATIVE | SPECULATIVE |

## Pearl gate

**Diamond:** F₄ = Aut(J₃(O)) as unified source of {4/3, 12, τ/e} — registered in pearl_registry/INDEX.md 2026-06-27.

## Next action

1. Add F₄ Discussion paragraph to paper/main.tex [SPECULATIVE]
2. Push to GitHub
3. arXiv submission
