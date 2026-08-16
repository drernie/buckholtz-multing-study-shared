# P52 — the committed monopole action's field-normalization redundancy is CONDITIONAL, not unconditionally confirmed: N1 holds only given which coefficients are stipulated free

**Date:** 2026-08-16
**Status:** Built, run, ruff clean, all assertions pass. **Skeptic review
(Step 8a): COMPLETE — second true-kill-adjacent verdict this session.
Corrections applied below, independently re-verified before acceptance.**
**Origin:** direct continuation of P51, per the user's own reframing:
not "which of P39's readings is correct" but "does the actually
committed action fix an absolute `φ` normalization at all?" Pre-registered
N1/N2/N3 outcomes, a genuine rank/nullspace method (not term-by-term
substitution), an adversarial positive control, and two explicit
kill-gates.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P52_normalization_identifiability_audit.py`, ruff clean, all
assertions pass (verified after correction).

## 0. Terminology correction, adopted throughout

**Field-redefinition covariance / field-normalization redundancy** — not
"gauge covariance," which `FINDING_P50B` and `FINDING_P51` both used
imprecisely. There is no local gauge symmetry here, only a reparametrization
freedom of one scalar field's normalization.

## 0.1 Pre-registered outcomes and kill-gates

**N1 — one-dimensional redundancy.** All committed terms have consistent
scaling weights, the weight system's nullspace is exactly 1-dimensional,
and no committed coefficient is fixed independently. `C,g,λ₄,φ` are not
separately identifiable; physics must be stated via invariants.
**N2 — redundancy broken.** At least one committed term does not admit
the same rescaling `s` — that term is the normalization anchor.
**N3 — incomplete specification.** The check runs into a
conceptually-real but undefined coefficient/term — applies explicitly to
the κ-sector question, bounding transferability without affecting the
monopole-only verdict.

**KG1 (anti-circularity):** do not derive transformation rules "so each
term becomes invariant" and present that as proof — repeating `P51`'s
circularity. **Outcome: only partially addressed — see Skeptic Verdict.**
**KG2 (form invariance ≠ value determined):** an invariant's *numerical*
value can still depend on background/initial conditions — stated
explicitly, unaffected by the correction below.

## Part 1 — committed action terms, κ-sector marked absent

```
ℒ_φ = −(C/2)(∂φ)² + gJφ − (λ₄/4)φ⁴
```

(`FINDING_P46`: kinetic + matter coupling, `C=1` implicit throughout;
`FINDING_P45`: quartic potential, `λ₄>0` declared, never numerically
fixed anywhere in this campaign.)

**κ-sector: absent / not testable.** Every finding through `P51` states
"monopole (`g`) sector only" — `κ` has never been covariantized into this
action. This finding cannot test whether a `κ`-dependent term would break
the redundancy, because that term does not exist. Any verdict below
applies to the monopole action only — N3 for the full MULTING-completion
question, stated explicitly, not silently skipped.

**Completeness caveat (added on correction):** the "3-term list" above
was checked by a targeted grep across `experiments/20260803-bridge`
(`FINDING_P44` line 71: "there is no mass term at all here"; no
"nonminimal" matches anywhere) — a **spot-check**, not an exhaustive
line-by-line audit of all 50+ prior findings. Stated as a limitation of
this finding, not a closed inventory claim.

## Part 2 — scaling-weight system, genuine rank/nullspace computation

Under `φ'=sφ`, each committed term contributes one linear constraint
(field power × `w(φ)` + `w(coefficient)` = 0). `J` does not transform
(established in `P50B`/`P51`, reused not re-derived).

**Caveat (added on correction):** reusing `w(J)=0` without re-deriving it
is a bigger concern here than for `P50B`/`P51`'s narrower covariance
claims — an *identifiability* verdict leans on every column of the
weight matrix being right, not just one invariance relation. Not
re-derived in this finding; flagged, not fixed.

```
Weight matrix M (columns [w(φ),w(C),w(g),w(λ₄)]):
  kinetic:  [2, 1, 0, 0]
  coupling: [1, 0, 1, 0]
  quartic:  [4, 0, 0, 1]

rank(M) = 3,  nullity = 1
null vector (normalized to w(φ)=1): [1, −2, −1, −4]
```

**Confirmed (script assertion): nullity=1**, matching the hand-derived
weights exactly — via genuine linear algebra, not asserted. This part is
**unaffected** by the correction below: it is a real, non-forced
computation (rank could have come out `<3`, it did not).

## Part 3 — what nullity=1 alone does not yet establish

A nullity of 1 shows the committed 3-term system is *consistent with* a
1-parameter redundancy family — but doesn't by itself prove the method
would have caught a real anchor if one were present (KG1's concern).
Part 4 tests this directly.

## Part 4 — adversarial positive control (KG1) — RETRACTED as originally presented

~~Added `qφ³`, `q` declared **fixed** (`w(q)=0`, not a free column —
exactly how a genuinely independently-fixed coefficient would enter):
`rank(M₂)=4, nullity=0`. **Confirmed: adding a genuine anchor term
collapses nullity to 0** — only the trivial `w=0` solution survives. The
method **does** detect a breaking term when one is present — this
licenses trusting the nullity=1 result on the real committed action as a
genuine structural fact, not an artifact of an insensitive check.~~

**[CORRECTED after context-blind skeptic review, Step 8a]** The original
claim above is **false**. Independently re-verified via standalone
sympy computation *before* accepting the skeptic's critique: adding the
**exact same term** `qφ³`, but giving `q` its **own column** (i.e.
treating it as *also* free to co-transform, exactly like `C,g,λ₄`
already were) gives:

```
rank(M₂_free) = 4,  nullity = 1
null vector (normalized): [1, −2, −1, −4, −3]
```

**The same term gives either nullity=0 (redundancy destroyed) or
nullity=1 (redundancy preserved), depending entirely on whether the
auditor grants the new coefficient a free column** — not on anything the
mathematics discovers about the physics. The original "adversarial
control" demonstrated a tautology (an omitted column forces that
variable's weight to zero), not a method capable of independently
distinguishing "genuine physical anchor" from "another free,
co-transforming coefficient."

**Structural point:** this is the same underlying limitation already
found in `FINDING_P50B` (a dimensionless prefactor `α` undetermined by
pure dimensional analysis) and `FINDING_P51` (E1-vs-E3 undetermined by a
criterion that passes regardless of which is true) — recurring a
**third time**: which coefficients are free to co-transform is an input
this method needs from outside itself, not an output the rank/nullspace
computation can derive.

## Part 5 — invariants derived from the null vector, not pattern-matched

```
w(A) := −w(C) = 2   (A=C⁻¹)
weight(Ag²) = 0
weight(gφ) = 0
weight(λ₄A²) = 0
```

**Confirmed (script assertion), all zero** — derived from the computed
nullspace, not pattern-matched from prior findings. `Ag²` matches
`FINDING_P50B`/`P51`'s own force-strength invariant; `gφ` matches the
interaction invariant already established.

~~`λ₄A²` is new: `P45`'s own `λ₄`, individually, is convention-dependent —
the physically meaningful self-interaction strength is `λ₄A²`, not `λ₄`
alone.~~ **[CORRECTED]** "New" overstates it. With a 1-dimensional null
space spanned by a single vector, every invariant is a rational power of
any other: once `Ag²` and `gφ` are known as the first two independent
weight-zero generators, `λ₄A²` is the mathematically **forced third
generator** of the same invariant lattice, not an independent discovery.
The physical content (`λ₄` alone is convention-dependent, `λ₄A²` is the
meaningful combination) is still correctly derived — only the "new"
framing is corrected.

## Part 6 — KG1 (anti-circularity): what actually distinguishes this from `P51`'s circularity, and what does not [CORRECTED]

`FINDING_P51`'s Part 2 checked whether two already-matching numbers
agreed — both reduced to the same forced expression, a tautology by
construction. P52's rank/nullspace computation does **not** repeat that
*specific* failure: nullity=1 is a genuine, non-forced linear-algebra
fact about 3 independently-stated term-constraints on 4 columns (rank=3
was computed, not assumed — rank<3 was a live logical possibility).

~~This is an overdetermined-vs-underdetermined system question,
genuinely falsifiable — Part 4's adversarial control demonstrates the
system *can* become inconsistent-with-redundancy when a real anchor is
added.~~ **[CORRECTED]** Part 4 itself now shows this claim is false: the
same new term gives nullity=0 or nullity=1 depending only on whether the
auditor grants its coefficient a free column. **KG1 is therefore only
partially addressed:** P52 avoids P51's specific tautology (forced
numerical equality), but shares a *deeper* version of the same
limitation — whether the 4 columns `[φ,C,g,λ₄]` are the correct and
complete set of physically-free coefficients is an assumption fed into
the matrix, not a fact the matrix's rank can verify about itself.
Nullity=1 is a sound computation *given* that assumption; it is not
independent proof the assumption is correct.

## Part 7 — form invariance ≠ value determined (KG2)

Even given N1, `Ag²`, `gφ`, `λ₄A²` being invariant does **not** mean their
numerical values are determined. `gφ̄` (hence `P50A`'s `μ_metric`) is
invariant (`FINDING_P51`), but `φ̄` itself is sourced by `FINDING_P46`'s
own background field equation, which has free initial conditions — N1
says *which* combinations are physically meaningful to ask about, not
*what* their values are. **Unaffected by the correction above.**

## Verdict [CORRECTED after context-blind skeptic review, Step 8a]

~~**N1 confirmed for the committed monopole action.** `C,g,λ₄,φ` are not
separately identifiable as absolute normalization quantities — physics
must be stated via `Ag²` (force strength), `gφ` (interaction), and
`λ₄A²` (self-interaction, new here).~~

**N1 holds only as a CONDITIONAL statement, not an unconditional physical
fact:** given the stipulation that `C,g,λ₄` (alongside `φ`) are *all*
free to co-transform under field redefinition, the scaling-weight system
for the committed monopole action has nullity exactly 1 (Part 2, genuine
computation). The adversarial control (Part 4) does **not** license the
stronger, unconditional claim — it shows the outcome depends on an
auditor modeling choice, not a physical discovery.

**This is the third occurrence this session of the same underlying
limitation:** P50B — an undetermined numerical prefactor `α`; P51 — a
pre-registered criterion that could never discriminate its own
alternatives; P52 — an auditor-choice-dependent modeling decision
(which coefficients get a free column) masquerading as a discovered
structural fact.

**What survives intact:** *if* `C,g,λ₄,φ` are all free (a stipulation
consistent with every prior finding in this campaign, but not
independently proven here), then `Ag²`, `gφ`, `λ₄A²` are the physically
meaningful invariant combinations — individual `C,g,λ₄,φ` are not.

**κ-sector: explicitly N3** — this does not extend to the full MULTING
completion. **KG2 stands:** none of these invariants' numerical values
are determined by this finding. **P17/P42 connection: explicitly
deferred** as a future testable prediction, not included in this
headline — an independent mapping of their own specific dimensional gaps
onto this null direction would be needed, not attempted here.

## What this establishes, precisely

1. The committed monopole action's 3 independently-stated term-constraints
   yield rank 3 on 4 columns (a real, non-forced computation) — **but**
   whether those 4 columns constitute the complete, correctly-scoped set
   of physically-free coefficients is an input assumption, not a
   verified output. Nullity=1 is sound *conditional on* that assumption.
2. `Ag²`, `gφ` (already known) and `λ₄A²` (forced third generator, not an
   independent discovery) are the physically meaningful invariants *of
   that conditional system*.
3. `P39`'s original "which reading of `[g]` is correct" question remains
   open — this finding reframes it (individual `[g],[φ],[C]` may not be
   the right question to ask) but does not close it, since the reframing
   itself rests on an unverified free/fixed stipulation.
4. A **partially** sound method (rank/nullspace) for testing normalization
   anchors — genuinely non-circular in the P51 sense, but not yet a
   method that can certify its own input assumption (which coefficients
   are free).
5. **A third instance of the session's recurring meta-pattern:** pure
   field-redefinition-covariance/linear-algebra methods cannot determine
   facts that require external physical input — here, which coefficients
   are genuinely free to co-transform vs. genuinely fixed by physics.

## What this does NOT establish

1. **Anything about the κ-sector or full MULTING completion.** N3,
   explicit scope boundary.
2. **Numerical values of any invariant** (KG2) — `gφ̄`'s actual value
   still depends on background/initial conditions, not addressed here.
3. **That `P17`/`P42`'s dimensional anomalies are the same null
   direction.** A real, testable prediction, explicitly deferred, not
   claimed.
4. **That no committed term could ever break this redundancy in a future
   extension.** Only the current, actually-committed action is audited.
5. **That `C,g,λ₄,φ` are unconditionally non-identifiable.** Only that
   they are non-identifiable *given* the free-coefficient stipulation —
   which this method cannot itself verify.
6. **That `w(J)=0` is correct for this identifiability claim specifically**
   — reused from `P50B`/`P51` without re-derivation, flagged as a bigger
   concern here than there.
7. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Skeptic Verdict (Step 8a, context-blind — claim.md + code only, no session history)

| Sub-claim (original) | Skeptic verdict | Response |
|---|---|---|
| Part 4 adversarial control proves the method distinguishes real anchors from non-anchors | **FALSIFIED** — same new term gives nullity=0 or nullity=1 depending only on whether its coefficient gets a free column (independently re-verified via standalone sympy before accepting) | **Fixed.** Part 4 rewritten to show both outcomes; original claim retracted with struck-through text |
| "N1 CONFIRMED" as an unconditional headline | **FALSIFIED** — rests on the retracted Part 4 claim | **Fixed.** Downgraded to a conditional statement (N1 holds *given* the free-coefficient stipulation) |
| Part 6: "not the same failure mode as P51" | **FALSIFIED** — shares a deeper version of the same limitation (external input needed, this time about which coefficients are free) | **Fixed.** Part 6 rewritten: KG1 only *partially* addressed |
| `λ₄A²` presented as "new" | **WEAKENED** — mathematically forced once `Ag²`,`gφ` are known (third generator of a 1-dim lattice), not an independent discovery | **Fixed.** Physical content kept, "new" framing corrected |
| `w(J)=0` reused without re-derivation | **WEAKENED** — bigger concern for an identifiability claim than for P50B/P51's narrower covariance claims | **Accepted limitation.** Flagged explicitly in Part 2 and in "What this does NOT establish" |
| "3-term list" completeness | **WEAKENED** — asserted without stating how it was checked | **Accepted limitation.** Stated as a grep-based spot-check, not exhaustive |

**True kill assessment:** the core predicate ("the committed action has a
genuine, method-verified 1-dimensional redundancy") does not survive
unconditionally — this is the **second true-kill-adjacent verdict this
session** (after `FINDING_P51`), both sharing the same deep structure: a
pre-registered check that cannot discriminate its own alternatives
without an external, non-derivable input. Not a full kill of N1 itself
(the conditional statement survives and is likely still the most
physically reasonable reading, consistent with every prior finding in
this campaign) — but the *evidence* for it is much weaker than
originally presented.

## Reproduction

```bash
python experiments/20260803-bridge/P52_normalization_identifiability_audit.py
```
