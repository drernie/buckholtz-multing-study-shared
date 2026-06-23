# NR-009 — S³ geometry as mechanism for Eq.32 prefactor (4/3) — REJECTED

**Date:** 2026-06-23
**Verdict:** REJECT (bridge falsified by skeptic + tool-verified enumeration)
**Branch:** cross-domain hypothesis H-S³ — "Eq.32 is a one-parameter S³ statement (n=3)"

---

## Claim (falsified)

Eq.32 `(4/3)(m_τ/m_e)^12 = α_EM/α_G` is not a 2-parameter coincidence but a 1-parameter
geometric statement at n=3 (the 3-sphere): prefactor 4/3 = (n+1)/n (curvature balance),
exponent 12 = n(n+1) = 2·dim SO(4) (isometry group).

## Why falsified

| Test | Result | Evidence |
|------|--------|----------|
| Functional-form look-elsewhere | **24** simple exponent forms h(n) give h(3)=12; **19** prefactor forms p(n) give p(3)=4/3 → **~456 combined (p,h) families coincide at n=3** | `[VERIFIED-BASH]` enumeration |
| Is exponent n(n+1) special? | No — 4n, n+9, 3n+3, n²+3, … all give 12 at n=3 | `[VERIFIED-BASH]` |
| "12 = 2·dim SO(4)" | Algebraic relabeling of 12; the factor 2 has no canonical S³ motivation | skeptic, `[INFERRED]` |
| Single S³ object producing BOTH coefficients | None found; (n+1)/n and n(n+1) are two separate borrowings glued at n=3 | skeptic |

**Root cause:** the exponent value ≈12 is forced by `log_b(α_EM/α_G) = 12.035`, NOT by geometry.
Once 12 is forced, the prefactor ≈4/3 is forced too. Writing them as `(n+1)/n` and `n(n+1)`
is post-hoc relabeling — one of ~456 equally-simple choices. AOG-1 fails (not pre-registered;
the family was reverse-engineered to pass through (4/3, 12)).

## Kill Analysis

**What this KILLED:**
- The claim that S³ geometry *derives* the (4/3) prefactor.
- The "one free parameter n=3" framing — it is a 2-parameter relabeling.
- Closing blocker G3 (mechanism) via the S³ route.

**What this did NOT kill (survives):**
- The numerical relation itself: `log_b(α_EM/α_G) ≈ 12.00` at 0.17σ — still a striking empirical regularity.
- The discrete look-elsewhere result (1 of 5040 simple prefactor × integer-exponent × mass-pair) — that measures a DIFFERENT thing (raw coincidence strength) and stands.
- The Sabine verdict on C9: **PROMISING as empirical regularity**, in the Dirac-Large-Numbers lineage — unchanged.
- H-electron4/3 (Poincaré EM-mass 4/3) as a separate, weaker candidate for the prefactor — but it does NOT explain the exponent 12, so it is not a mechanism either.

**Relaxation Map (surviving option space):**
- Remove: S³ as the geometric source → dead.
- Weaken: any *single* compact manifold deriving both coefficients → no candidate found.
- Replace: a mechanism that derives the EXPONENT 12 from first principles (not the prefactor) would be the real prize, since 12 is the load-bearing number. The prefactor 4/3 is then a 0.0135% correction.

## Forbidden use

Do NOT cite NR-009's parent idea as "Eq.32 is derived from S³ geometry."
Do NOT present (4/3)=(n+1)/n or 12=n(n+1) as a derivation — they are relabelings (~456 alternatives).
C9 must be framed as an **empirical relation (mechanism open)**, never "geometrically derived."

## Correct next direction

The mechanism question for C9 should target the **exponent 12** (load-bearing, = log_b T),
not the prefactor 4/3 (a 0.0135% mop-up). Any future "why 12" must be pre-registered and
predict an INDEPENDENT relation, not retrofit the known value.

---

*REJECT — cross-domain bridge falsified. skeptic [FALSIFIED] + enumeration [VERIFIED-BASH 456 families].*
*Parent: pearl_registry 2026-06-21 cross-domain (4/3)↔κ² entry — now annotated FALSIFIED-AS-MECHANISM.*
