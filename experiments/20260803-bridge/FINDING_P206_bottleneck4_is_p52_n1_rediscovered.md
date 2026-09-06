# FINDING P206 — bottleneck 4 is `FINDING_P52`'s N1, rediscovered eight
# days later under a different name

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (symbolic, no data, no fit)
**Artifact:** `scripts/p206_observable_class_closure.py`
**Continues / corrects the reading of:** `FINDING_P133`, `FINDING_P205`
**Prior art it turned out to duplicate:** `FINDING_P52`
**Step 8a:** run **twice**, context-blind, reworded prompts
(Paraphrase-Sensitivity Probe — high-stakes PROMOTE). **Both runs agree.**

---

## 1. The headline, stated so it cannot be over-read

`FINDING_P133` (2026-08-24) computed `rank(J) = 2 < 3` for

```
O1 = A g²      O2 = A κ²      O3 = κ / g
```

in `θ = (A, g, κ)` and named it **structural non-identifiability** — one
of the project's four named bottlenecks.

That rank deficiency is **exactly the one-dimensional field-normalization
redundancy that `FINDING_P52` had already computed eight days earlier**
(2026-08-16), for the same action. The null direction is

```
v = (−1, ½, ½)   in   (log A, log g, log κ)
```

which is the generator of `φ → λφ̄`, i.e. `A → A/λ²`, `g → gλ`, `κ → κλ`.
P52 had already derived `A g²` from its own null vector as an invariant.
**All three of P133's observables are P52 invariants.** P133's rank
deficiency *is* P52's nullity.

**So this file contributes a connection, not a theorem.** The bottleneck
was erected on top of a property of the project's own action that the
project had already derived, documented, and skeptic-reviewed. Recording
that is the point: `memory-protocol.md` warns about precisely this — the
same result rediscovered under a different name — and here it happened
inside one repository, eight days apart.

## 2. What follows for bottleneck 4

**Given P52's N1**, bottleneck 4 as posed — *"find an observable that
identifies `(A, g, κ)` separately"* — has no solution and needs none.
Three coordinates describe two physical degrees of freedom plus one
redundancy; P133's three observables determine both. Rank 2 is
**complete, not deficient**.

**This inverts the practical reading of `FINDING_P205`.** P205 derived
that a monomial `A^a g^b κ^c` raises the rank iff `2a ≠ b + c`, and read
"measure `A`, or `g`, or `κ` directly" as the way out. But `L := 2a−b−c`
is *precisely the rescaling weight*: a monomial picks up `λ^(−L)`, so
`L = 0` ⟺ rescaling-invariant. Every "escape" P205 identified is
therefore a quantity whose numerical value is set by an arbitrary
normalization convention. **Choosing `A ≡ 1` is not an experiment.**

P205's algebra is untouched and its test suite still passes
(`tests/test_p205_identifiability_break_condition.py`, added today, 16
tests). What changes is the interpretation — and per Skeptic B's wording
correction, the honest form is not "P205 was wrong" but *"P205 rested on
an unstated assumption that `A` is an independent physical parameter,
which holds only conventionally."*

## 3. Verification `[VERIFIED-run]`

`scripts/p206_observable_class_closure.py`, exit 0, every assertion:

| check | what it does |
|---|---|
| PC1 | reproduces P133's rank 2 from a freshly computed Jacobian |
| PC2 | negative control — the bare parameters give rank 3, so the machinery *can* see rank 3 |
| R1 | `O1,O2,O3` each exactly invariant under the substitution (ratio simplifies to 1) |
| R2 | every rank-raising monomial verified **non**-invariant |
| R3 | `L` = rescaling weight, checked on 125 triples in `[−2,2]³` |
| R4 | null space is 1-D and equals `(−1, ½, ½)`, asserted exactly |
| R5 | 4-parameter case with `α`: rank 3, residual direction `(−1, ½, ½, 1)`, adding more never raises it across `n∈{2,3,4}`, `m∈{1,2}` |

## 4. Corrections applied — no-silent-correction

The chain is recorded because each error produced the next question.

1. **Draft 1 was wrong and inverted the conclusion.** It claimed a chain
   of `n` propagators has `v = n+1` coupling insertions, hence every
   `n ≥ 2` observable breaks the degeneracy. A chain over `n+1` bodies
   puts **two** insertions on each interior body, so `v = 2n`. Caught by
   recounting before the claim left the script.
2. **Draft 2's escape claim was WEAKENED by the first skeptic.** A `φ²`
   vertex carries a *new* coupling `α`; the honest count is
   `Aⁿ α^m g^b κ^c` with `b+c = 2n−2m`, moving the problem to a
   4-parameter space.
3. **That skeptic's proposed repair was itself wrong, and checking it is
   what produced this file's actual result.** It claimed two independent
   `φ²` observables give rank 4. Recomputed: the rank stays 3 at every
   `n` and `m`. Asking *why* surfaced the fixed null direction.
   Per `audit-verification-gate.md`, the agent's `[VERIFIED]` was treated
   as `[INFERRED]` and re-run — which is the only reason this was caught.
4. **Terminology corrected to P52's.** Drafts called this "gauge freedom."
   P52 had already ruled that imprecise: there is no local gauge symmetry,
   only **field-normalization redundancy / field-redefinition
   covariance**. Adopted throughout.
5. **A code path removed.** `A / LAM ** abs(RESCALING["A"])` gave the right
   answer while ignoring the stored sign — flagged by Skeptic A as a
   silent-corruption path under refactor. Now `A * LAM ** RESCALING["A"]`.
6. **`[VERIFIED]` → `[CHECKED]` on the 125-triple loop.** Both skeptics
   independently made the same point: the identity is algebraic and holds
   for all real exponents; the finite box tests sympy's cancellation, not
   the mathematics. Presenting a finite enumeration as a proof is the
   error, even when the conclusion is true.

## 5. Step 8a — Paraphrase-Sensitivity Probe

Two context-blind skeptic runs on identical claim + code, prompts reworded
between them (formal enumerated register vs. plain-language paraphrase).
**Both returned CONFIRMED-REAL on the core, with the same three
narrowings** — no disagreement, so the skeptic-leaning tie-breaker was not
needed. Agreed narrowings, all applied above and in the script:

- scope `A is not physical` → *not separately measurable within this
  action, absent external anchoring of `φ`'s normalization*;
- scope R5 to the vertex class `{g·m·φ, κ·q·φ, α·φ²}` — a `φ³`/`φ⁴`
  vertex adds a parameter with its own weight and the arithmetic must be
  redone;
- soften the overturning of P205 (see §2).

Skeptic B additionally required a project-wide check for other places
treating `A` as measurable. **Run:** `A/c²`-style hits are a *different*
`A` (node subscript, `k_A/c²`) — a real symbol collision, exactly the
Type-1 overload `research-methodology.md` flags, but not a normalization
claim. The genuine hits are `FINDING_P18`, `P27`, `P52` — which is how the
prior art in §1 was found.

## 6. What this does NOT establish

1. **Nothing about whether the action is right.** `NO_AUTHOR_ERROR`; this
   is the project's own reconstruction.
2. **Not that `A` is meaningless in general.** Scoped to this action with
   no external anchor. A canonical kinetic term fixed by another sector, a
   VEV, or an LSZ anchor each restore an operational value for `A`.
3. **Not that the two surviving physical parameters have determined
   values.** That is P52's own **KG2**, explicitly still open: form
   invariance is not value determination. P133 never asked it; this file
   does not answer it.
4. **Inherited conditionality.** P52's verdict is CONDITIONAL — N1 holds
   *given which coefficients are stipulated*. Nothing here escapes that.
5. **Monomials only** for the exhaustiveness check, though the rescaling
   argument itself is about the action's parameters.

## 7. Pearl / Caveat Gate

**Caveat Gate fires on §6.2** — it names a specific, buildable alternative
(an external anchor for `φ`'s normalization) that has not been attempted,
so it does not get to live only as prose here. Registry row to add:

```
| 2026-09-07 | P206 | v82/this action fixes no external anchor for phi's
normalization, so A is convention-only | if any sector pins phi's kinetic
normalization independently, A becomes operationally measurable and P133's
bottleneck-4 framing is partially restored | 5 | a completion that couples
phi to an independently normalized sector | 2026-11-15 | pending |
```

**Process pearl, higher-impact than the physics one:** two findings eight
days apart computed the same one-dimensional redundancy, and the second
named it a bottleneck without recognizing the first. Neither the
`null_results` pre-check nor any hook caught it — both fired on *claim*
text, and these two never shared vocabulary (`"field-normalization
redundancy"` vs `"structural non-identifiability"`). This is the
same-lesson-under-a-different-name failure `memory-protocol.md` records
for the cross-repo case, now observed **intra-repo**. The cheap
generalization to test: when a new finding computes a rank or a null
space, grep prior findings for *rank/nullspace/redundancy/invariant*
rather than for the claim's own words.

### 7.1 That prediction was tested immediately, and it fired

Run on this finding itself (`grep -rliE "nullspace|null space|null
vector|rank\(J\)|identifiab|redundanc"` over `experiments/*/FINDING_*.md`):
**22 findings**, including two the claim-vocabulary search preceding §6
had missed:

- **`FINDING_P53`** (2026-08-17) — *"a soft/conditional external scale
  constraint on P52's `Ag²` invariant already existed in this project."*
  This is directly about §6.2's own caveat. It does **not** dissolve that
  caveat — P53 constrains the **invariant** `Ag²` under an explicit,
  unverified mapping, which does not pin `A` separately — but the caveat
  as first written implied nobody had looked, and somebody had. The
  registry row is amended accordingly, and the surviving question is
  narrowed to an anchor on **`φ`'s normalization**, starting from P53.
- **`FINDING_P165`/`FINDING_P161`** — explicitly "the same
  identifiability machinery," a lineage `P206` reached independently.

**Status: partially confirmed at n=1.** One instance is not a validated
rule, and the `next_check` stands. But the first thing the heuristic did
was catch an omission in the very file proposing it — which is the
strongest available evidence that the failure mode is structural rather
than a one-off.
