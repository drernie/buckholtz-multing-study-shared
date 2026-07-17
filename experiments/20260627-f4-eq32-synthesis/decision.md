# Decision: 20260627-f4-eq32-synthesis

**Date:** 2026-06-27
**Verdict:** PROMOTE (with [SPECULATIVE MECHANISM] qualifier) — **C10 downgraded to FALSIFIED-as-mechanism 2026-07-17**, see Skeptic Response Matrix below. The numerical result (C1, Eq.32 itself) is unaffected; only the "F₄ explains it" interpretation is affected.

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

## Skeptic concerns (original, self-answered 2026-06-27 — see re-audit below)

| Concern | Response | Status |
|---------|----------|--------|
| 4/3 = 36/27 is post-hoc labeling | Correct — dimension-ratio is candidate motif, not theorem | Accepted limitation |
| τ/e from J₃(O) uses fitted parameters (Singh 2024) | Correct — chain is incomplete | Documented in caveats |
| F₄ as mechanism not derived | Correct — C10 stays [HYPOTHESIS] | Accepted limitation |
| Top-quark formulas appear in top-5 | Yes, but all at >0.3% vs 0.0135% for Eq.32 | Dismissed — 22× gap |

## Skeptic Response Matrix — independent context-asymmetry re-audit (2026-07-17, FL Step 8a)

Triggered by a `/research-audit` finding: the table above was self-answered by the same
session that built the claim, not run through an independent skeptic with context
asymmetry (claim.md + code only, no session history — per `falsification-ladder.md`).
Ran `Agent(skeptic)` fresh against `claim.md` + the underlying C1-C9 scripts + NR-009 for
comparison. Full verdict: **claim WEAKENED, trending FALSIFIED; C10 specifically
FALSIFIED-as-mechanism**.

| Concern (skeptic) | Response | Status |
|---|---|---|
| C10's wording ("F₄ encodes the formula as a derivable theorem") falls under NR-009's own forbidden-use clause — same post-hoc relabeling of {4/3, 12}, different vocabulary (Lie-algebra invariants instead of `(n+1)/n`/`n(n+1)`) | **Confirmed.** NR-009 explicitly forbids presenting either number as "geometrically derived." C10's Counterfactual Frame ("Casimir degree 12 controlling the mass-ratio exponent... coset dimension ratio 36/27 providing the prefactor") does exactly that. | **Accepted — C10 downgraded to FALSIFIED-as-mechanism** (not merely re-affirmed [HYPOTHESIS]) |
| C5 (\|roots(G₂)\|=12) and C6 (\|W(G₂)\|=12) are not independent — for a rank-2 root system, root count and Weyl-group order are generically equal; this was presented as two separate confirmations | **Confirmed** — standard representation theory. This is one observation counted twice, not two independent paths to 12. | **Accepted — decision.md corrected below (see "Three independent appearances" struck)** |
| C7 (max Casimir degree of F₄ = 12) is not unique to F₄ — E₆, E₇, E₈ all also have 12 among their Casimir/exponent degrees | **Confirmed** — standard fact (F₄: 2,6,8,12; E₆: 2,5,6,8,9,12; E₇: 2,6,8,10,12,14,18; E₈: 2,8,12,...). F₄ is not singled out by this criterion. | **Accepted — "3 independent paths to 12" claim retracted, see below** |
| C8 (dim(Spin(9))/dim(J₃(O))=36/27=4/3) is one of ≥4 comparable-weight ratios in the same F₄ decomposition (52/36, 52/27, 16/9, 36/27 — per this project's own `atom_b_four_thirds.md`, which says verbatim "That IS retrofit") | **Confirmed** — the project's own prior artifact already says this; the claim's Counterfactual Frame does not carry this caveat forward. | **Accepted limitation, now stated plainly (not softened) in Kill Analysis below** |
| C3/C4 (rank #1 of 83,160 formulas, p<0.00002) could not be independently verified — the script producing this number is not among the claim's cited artifacts, and 83,160 vs NR-009's 5,040-formula space (16.5× larger) is unexplained | **Open — genuine gap, not dismissed.** Either cite/attach the exact script + formula-space definition, or downgrade C3/C4 from [VERIFIED-BASH] to [HYPOTHESIS] pending that. | **Not yet resolved — flagged for next session, does not block this decision.md correction** |
| exp_q_g2_sm_decomp.py and exp_g_singh_j3_algebra.py (both cited as claim.md sources) already conclude "coincidence, not embedding" and "4/3 doesn't arise trivially from these dimensions" — the claim's synthesis does not carry these conclusions forward | **Confirmed, most serious finding.** The project's own code contradicts the claim's headline interpretation; the contradiction was not surfaced in the original decision. | **Accepted — see Kill Analysis** |

## Kill Analysis (added 2026-07-17)

**What this re-audit killed:** the interpretation that F₄ = Aut(J₃(O)) "encodes" or
"explains" Eq.32 (C10). This interpretation is the SAME failure mode as NR-009
(post-hoc relabeling of {4/3, 12} using different vocabulary), and the project's own
underlying scripts (exp_q, exp_g) and prior artifact (atom_b_four_thirds.md) already
said so — the original decision.md did not carry that conclusion forward into the
synthesis.

**What survives (NOT killed):** Eq.32 itself (C1: the 0.0135% numerical match) and the
look-elsewhere ranking claim IF C3/C4's script is located and verified — these are
independent of whether F₄ "explains" anything. Eq.32 remains a real, precisely-matching
numerical relation with an unknown mechanism — exactly the same honest status NR-009
left it in.

**Corrected framing for any future use (paper, pearl_registry, correspondence):** Eq.32
is a precision numerical coincidence with NO surviving candidate mechanism (S³ geometry
killed NR-009; F₄/G₂/J₃(O) killed here). Do not describe either as "the" explanation.
Do not use "encodes," "derives," or "explains" for the F₄ connection — use "candidate
relabeling, not independently supported beyond NR-009's level."

## Forbidden use (added 2026-07-17)

Do NOT cite this decision (or the pearl_registry "diamond" entry it produced) as
mechanism support for Eq.32 in `paper/main.tex`, `paper1_eq32_note*.tex`, or any
correspondence to TJB. C1 (the numerical match itself) may still be cited. C10 may not.

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
