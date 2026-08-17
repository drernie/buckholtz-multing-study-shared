# NR-019 — Group-theoretic numerology as a mechanism for Eq.32's {4/3, 12} — REJECT (consolidated across 3 independent attempts)

**Date:** 2026-08-17
**Verdict:** REJECT (consolidated null result — the *category* of attempt, not
one specific hypothesis)
**Origin:** the 2026-08-17 `/research-audit` meta-audit (`docs/145`) flagged
this as a zombie risk: the same failure mode had been independently
rediscovered three times, in three different vocabularies, never
consolidated into one entry with one revival condition.

---

## Claim (rejected as a category)

That the pair `{4/3, 12}` in Eq.32 (`(4/3)(m_τ/m_e)^12 = α_EM/α_G`,
0.0135% precision) is *explained* by finding SOME group-theoretic
structure (a Lie group, a gauge group, a Jordan algebra) whose invariants
— dimension, Casimir degree, root count, Weyl-group order — happen to
equal 4/3 and/or 12.

## The three independent attempts

| Attempt | Date | Vocabulary | Where |
|---|---|---|---|
| **S³ geometry** | 2026-06-23 | `4/3=(n+1)/n`, `12=n(n+1)` at n=3 (curvature balance / isometry group SO(4)) | `null_results/20260623-nr009-s3-geometry-eq32-mechanism.md` (NR-009) |
| **F₄=Aut(J₃(O))** | 2026-06-27, downgraded 2026-07-17 | `12`=Casimir degree of F₄ / root count of G₂ / Weyl-group order of G₂; `4/3=dim(Spin(9))/dim(J₃(O))=36/27` | `experiments/20260627-f4-eq32-synthesis/decision.md`, C10 |
| **SM gauge group dimension** | 2026-06-24 | `12=dim(SU(3)×SU(2)×U(1))=8+3+1` | `pearl_registry/INDEX.md`, 2026-06-24 row, still `pending` |

## Why falsified — the same root cause, three times

All three share **one identical structural flaw**, independently confirmed
in each case:

1. **The target number is forced first, the "explanation" is fit second.**
   `log_b(α_EM/α_G) = 12.035` fixes 12 before any group is chosen; a group
   with a 12 *somewhere* in its invariant list is then found and presented
   as if it had predicted 12. NR-009's own enumeration: ~456 comparably
   simple `(prefactor, exponent)` families coincide at the same n=3 choice
   — 12 is not singled out by S³, it is one of hundreds of equally-valid
   readings.
2. **No single object produces BOTH numbers.** In every attempt, `4/3` and
   `12` come from *two different, independently-borrowed* invariants of the
   same structure, glued together only because both happen to equal the
   target values. NR-009: `(n+1)/n` and `n(n+1)` are unrelated formulas
   that happen to coincide at n=3. F₄ case: `36/27` (a dimension ratio) and
   "Casimir degree 12" are unrelated invariants of the same group, and the
   skeptic found even the "12" itself is not unique to F₄ (E₆, E₇, E₈ all
   also have 12 among their own Casimir degrees) — so it doesn't even
   single out the claimed group.
3. **The project's own underlying code already said so, independently, in
   two of the three cases**, before the synthesis stage smoothed it over:
   `f4-eq32-synthesis`'s own `exp_q_g2_sm_decomp.py`/`exp_g_singh_j3_algebra.py`
   concluded "coincidence, not embedding" and "4/3 doesn't arise trivially
   from these dimensions" — the original decision.md's headline synthesis
   did not carry that conclusion forward (caught by a later context-blind
   skeptic re-audit, 2026-07-17).
4. **No independent prediction.** None of the three readings, if accepted,
   would predict anything *beyond* the two numbers already known. The
   pending gauge-group row states this explicitly: "NO experimental test
   discriminates H0 (pure coincidence) from '12=dim(gauge)' — Belle II
   does not move `log_b(T)`."

## Kill Analysis

**What this consolidated entry KILLS:**
- The *category* of attempt: "find a group whose invariants happen to
  equal 4/3 and/or 12, present the match as a mechanism." All three
  concrete instances tried (S³, F₄/G₂/J₃(O), SM gauge group) are REJECT.
- Any future attempt using a *fourth* exceptional structure (another Lie
  group, another exceptional Jordan algebra, another coset) under the
  same "find-then-fit" method, without a pre-registered independent
  prediction, is **not a new hypothesis** — it is this same rejected
  category in new vocabulary. Do not re-run.

**What this does NOT kill (survives, unchanged):**
- **Eq.32 itself** — the raw numerical relation `(4/3)(m_τ/m_e)^12 =
  α_EM/α_G` at 0.0135% precision remains a real, unexplained, striking
  empirical regularity. The look-elsewhere audit (`f4-eq32-synthesis`,
  83,160 formulas scanned, Eq.32 ranks #1, next-best 22× worse,
  `p<0.00002` within 0.1%) independently establishes this is *not* itself
  a look-elsewhere artifact — that finding is untouched by this REJECT.
- The **Sabine verdict**: Eq.32 remains "PROMISING as empirical
  regularity," in the Dirac-large-numbers lineage — mechanism open, not
  mechanism refuted.
- The **exponent-vs-prefactor asymmetry** NR-009 already identified: 12
  is load-bearing (`=log_b T` almost exactly); 4/3 is a 0.0135%
  correction on top. Any future mechanism search should target 12
  specifically, not re-fit both numbers simultaneously.

**Relaxation Map (surviving option space):**
- Remove: "any group-invariant match, however found, counts as a
  mechanism" → dead, permanently, as a *method*.
- Weaken: a match that explains ONLY the exponent 12 (not both numbers)
  from a *single, non-post-hoc* invariant, stated and checked BEFORE
  computing what 12 needs to equal → not yet tried, would be a genuinely
  different (narrower, testable) claim.
- Replace: the correct standard for promotion is stated below.

## Revival condition (explicit, per AOG-1 pre-registration discipline)

A future group-theoretic mechanism claim for Eq.32 may be considered
**only if all of the following hold simultaneously**, checked *before* any
numerical match is computed:

1. The candidate structure is chosen for an independent reason (a
   physical motivation for *why this group*, stated before checking
   whether its invariants equal 4/3 or 12) — not selected by scanning for
   a match.
2. It derives the **exponent 12 alone** from a single invariant, without
   separately borrowing a second, unrelated invariant to also match 4/3.
3. It produces **at least one new, independently checkable prediction**
   beyond {4/3, 12} themselves (per the pending pearl row's own
   criterion) — e.g., a predicted value for a *different* coupling ratio,
   checkable against data or theory not used to construct the claim.
4. The look-elsewhere space for "groups with a 12 somewhere in their
   invariant list" is stated and the candidate is checked against it
   (NR-009's own enumeration technique, reused) — if dozens of groups
   also have a 12 among their Casimir degrees/root counts/dimensions
   (as E₆/E₇/E₈ already do, per the F₄ re-audit), the match carries no
   information.

Absent all four, do not open a new experiment folder for this category —
cite this entry (NR-019) and stop.

## Forbidden use

Do NOT cite S³ geometry (NR-009), F₄=Aut(J₃(O)) (`f4-eq32-synthesis` C10),
or "12=dim(SM gauge group)" (pearl row, 2026-06-24) as an explanation,
derivation, or mechanism for Eq.32 in `paper/main.tex`, any
`paper1_eq32_note*.tex`, or any correspondence to TJB. Eq.32 itself (the
numerical match, and its look-elsewhere significance) remains fully
citable — only the *mechanism* claims are forbidden.

---

*REJECT (consolidated) — three independent context-blind/skeptic-caught
instances of the same failure mode, cross-referenced here for the first
time. Parent entries: NR-009, `f4-eq32-synthesis/decision.md` (C10),
`pearl_registry/INDEX.md` 2026-06-24 row (status updated to point here).*
