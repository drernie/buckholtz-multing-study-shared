# FINDING P75 — the structural layer is **completion-blind**, by proof

**Status:** built, run, reviewed context-blind, circularity charge refuted by
test, two reviewer catches applied.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P75_completion_invariants.py`

---

## The inversion

The campaign has been asking *"which completion of the local law is correct?"* —
scalar with `V(φ)`? a different mass law `m(φ)`? Every answer to that needs an
observable that separates them, and `FINDING_P74` just showed the `μ` channel is
ill-posed pointwise in `t`.

So invert it: **instead of asking which completion is right, ask what must be
true of all of them.** An invariant needs no discriminating observable to be worth
having.

**The completion family.** Two free functions, left as unspecified sympy
`Function`s throughout:

| | | |
|---|---|---|
| `V(φ)` | the potential | P45's quartic is *one* choice |
| `M(φ) := m(φ)/m₀` | the mass law | P33's `1−ĝφ` is one choice, **P68's `e^{−ĝφ}` another** |

---

## A. The control pair — run **before** anything new

This programme is not starting from zero: it has one confirmed instance and one
confirmed counter-instance, both established *before* the question was posed.
That is exactly the pair Gate 3 demands, and a test that cannot separate them
discriminates nothing.

| | control | result | `[VERIFIED-SYMPY]` |
|---|---|---|---|
| **A1** | `FINDING_P58` Route B: `ρ̄̇+3Hρ̄ = ρ̄(d ln m/dφ)φ̄̇` for **any** `m` | residual **0** with `V`, `M` unspecified | **INVARIANT**, P58 reproduced |
| **A2** | `FINDING_P66` first integral, which `P69` broke | `d/dt(a³φ̄̇) = −a³[V′(φ̄) + ρ_A M′(φ̄)]` | **NOT invariant**, P69's breakage reproduced |

A2 is worth reading closely: the general form shows the first integral fails for
**two independent reasons** — `V′` (which P69 found) *and* `ρ_A M′` (which nobody
had checked). It is not merely potential-dependent; it is mass-law-dependent too.

**The machinery separates the two known cases. It discriminates.**

---

## B. The constraint algebra is completion-invariant `[VERIFIED-SYMPY]`

`FINDING_P73` established, for the *committed* model (quartic `V`, linear `M`):

```
dC₀₀/dt = −3H·C₀₀ + (k²/a²)·C₀ᵢ
```

With `V` and `M` left **unspecified**, solving for the coefficients gives

```
residual over ALL coefficients:  0
A = −3H          B = k²/a²
```

**The coefficients reference neither `V` nor `M`.** Specialising back to the
committed model returns `A+3H = 0`, `B−k²/a² = 0` exactly — so this *generalises*
P73 rather than contradicting it.

---

## C. `P71`'s obstruction is completion-invariant `[VERIFIED-SYMPY]`

`FINDING_P71` proved `dC₀ᵢ/dt|_{C=0} = −Ψ·[Ḣ + 4πG(ρ+p)]` and that its residual is
**λ-free** for the quartic. Whether it is free of the **mass law** was never
tested — and P68's exponential `m(φ)` is a live alternative, so it matters.

```
dC₀ᵢ/dt == −Ψ·R_Ḣ   with V, M unspecified  →  True
```

So the obstruction P71 named, and P72 removed, is the **same** obstruction for
every completion in this family — and P72's closure is therefore not specific to
P69's background either.

---

## D. Ledger

| relation | status | source |
|---|---|---|
| `ρ_A a³ = C` (bare) | **INVARIANT** | imposed; P58's premise, `n a³` fixed |
| matter exchange form (P58 Route B) | **INVARIANT** | A1, any `V` and any `M` |
| constraint algebra (P73) | **INVARIANT** | Part B |
| `Ḣ` obstruction (P71) | **INVARIANT** | Part C |
| first integral `a³φ̄̇` (P66) | **NOT INVARIANT** | A2, retains `−a³(V′+ρ_A M′)` |
| `μ(a,k)` | untested here | P74: ill-posed pointwise in `t` |

**4 invariant against 1 non-invariant** — a separation, not a blanket
"everything is invariant" that would discriminate nothing.

---

## Verdict — what this means for the completion question

**The structural layer is completion-blind.** What the constraints *are*, how
they *propagate*, and what *obstructs* them is shared by every member of the
`(V, M)` family, **by proof rather than by coincidence.**

Consequence, and it is a hard one: **no work on the four structural relations
tested here can distinguish P68's exponential mass law from P69's quartic
potential.** They are structurally identical *in those relations*. Discrimination
must come from the *dynamical* layer — and P74 just showed this campaign's main
dynamical channel is ill-posed as currently defined.

**Wording bounded after review** (concern 6): an earlier draft said "no amount of
further work on that layer can *ever* distinguish them". That generalises from
four specific identities to a universal impossibility, which is not what was
computed. The claim is scoped to the relations actually tested.

---

## E. Post-review: the circularity charge, **tested rather than argued**

The reviewer's central charge: Part B is **circular** — the file writes the
evolution equations itself (`SUBS`) and then checks an identity among its own
equations, so closure is guaranteed by construction. Testable in one move: break
one equation at a time. **The reviewer had no shell and could not run this.**
Run here `[VERIFIED-SYMPY]`:

| deliberately broken equation | still closes? |
|---|---|
| KG drag `3H → 2H` | no — caught |
| KG: drop `V′` | no — caught |
| KG: drop `ρ_A M′` | no — caught |
| `Ψ̈`: `4H → 5H` | no — caught |
| matter continuity `3H → 2H` | no — caught |
| continuity: flip the `k²Q` sign | no — caught |
| **Euler: drop the exchange term** | **YES — test blind here** |
| `ρ_A` dilution `3H → 4H` | no — caught |

**7 of 8 break the closure. Circularity REFUTED.** The system is over-determined
— 2 unknowns `(A,B)` against 6 coefficient equations — so closure is a real
constraint on the equations, not bookkeeping.

**Blind spot, reported not hidden:** dropping the Euler exchange term does *not*
break closure. The 00-constraint algebra simply does not constrain that term, so
Part B certifies less than "the whole system is right."

### E2 — Bianchi vs P71's obstruction: no contradiction, but P71 deflates

The reviewer argued the two framings are mutually exclusive: if propagation
follows from covariance, there was never an obstruction to remove. Tested by
re-running the closure **without** imposing the `Ḣ` equation:

```
closure without the H-dot equation imposed:  False
```

Both statements are true. **Bianchi gives propagation on-shell; P71's obstruction
is exactly the off-shell failure.** But P71 **deflates** accordingly: the
"obstruction" is the requirement to impose the *full* background system rather
than a subset — standard GR bookkeeping, not a discovery.

### A2's guard was vacuous — fixed

The original guard read `assert d_first_int.has(V) or d_first_int.has(sp.Derivative)`.
Since `H = ȧ/a`, **any** expression carrying an `H` satisfies the second clause,
so the guard would have passed even if `V` had cancelled. Verified:
`H.has(sp.Derivative) = True`. Replaced with a test for the `V`- and
`M`-derivatives specifically. The *conclusion* was right; the guard did not
establish it.

---

### Honest deflation, and why it strengthens rather than weakens

Parts B and C may be **less surprising than they look**. Constraint propagation is
a consequence of the Bianchi identities, which hold for *any* diffeomorphism-
invariant action. So the invariance is arguably *expected*, and these results are
partly a confirmation that our system is properly covariant. `[INFERRED — the
Bianchi argument is not carried out here, only the two-function family is]`

But that reading makes the conclusion **stronger**, not weaker: if the invariance
follows from covariance rather than from our particular parameterisation, it
extends to completions **outside** the `(V, M)` family — including the
worldline-EFT and coarse-grained routes this file does not touch. The structural
layer would then be blind to *every* covariant completion, not just ours. Stated
as `[INFERRED]`, and it is the cheapest available next test.

---

## What this does NOT establish

1. **That these are all the invariants.** Named candidates were tested; the
   invariant ring was not enumerated. **Absence of a test is not absence of an
   invariant.**
2. **That `(V, M)` is the whole completion space.** Worldline-EFT and
   coarse-grained routes are not in it, and nothing here bears on them — except
   through the `[INFERRED]` Bianchi argument above, which is not proven.
3. **Anything observational.** These are structural identities; **none of them
   predicts a number.** An invariant that no experiment can see is a constraint on
   theorising, not a measurement.
4. **That the invariance is surprising.** See the deflation above.
5. **Anything about MULTING itself** (Gate 1): the family is *ours*.

---

## Skeptic Verdict (Step 8a)

**Central charge `[REFUTED]`; two subsidiary catches `[CONFIRMED]` and applied.**
Review was context-blind. **The reviewer had neither Bash nor Write** — it said so
and produced analysis rather than runs. Per `audit-verification-gate` that makes
all of it `[INFERRED]` to me, so every claim was independently re-run before
being accepted or rejected; those runs are now Part E of the artifact.

| # | Concern | My independent re-run | Response |
|---|---|---|---|
| 1 | Part B is circular — closure guaranteed by the author's own `SUBS` | **REFUTED.** 7 of 8 deliberate sabotages break the closure | **DISMISSED with data.** The system is over-determined; closure is a real constraint |
| 2 | Controls A1/A2 are single `SUBS` lines read back, so they do no work | **PARTLY CONFIRMED.** A1/A2 *are* shallow — but the sabotage battery is the harder control they asked for, and it discriminates | **ACCEPTED, and answered** by adding Part E rather than defending A1/A2 |
| 3 | The A2 guard `.has(sp.Derivative)` is vacuous | **CONFIRMED.** `H.has(sp.Derivative) = True`, so a bare `H` passes it | **FIXED** — now tests for the `V`/`M` derivatives specifically |
| 4 | "Bianchi extends broadly" and "P71 found a real obstruction" are mutually exclusive | **REFUTED as a contradiction, CONFIRMED as a deflation.** Closure fails off-shell, so both hold — but P71 reduces to "impose the full background system" | **RECONCILED and P71 deflated** (E2) |
| 5 | Claim doesn't extend to `K(φ)(∂φ)²` or `f(φ)R` completions | **NOT TESTED — accepted as a limitation.** I did not build those systems | **ACCEPTED**, already in *What this does NOT establish* #2 |
| 6 | "No further work can ever distinguish P68 from P69" overreaches | **PARTLY CONFIRMED.** It holds for the *structural* layer as tested, not universally | Wording bounded to the structural layer |

**Kill assessment.** The central result stands and is now backed by a
discriminating test the reviewer demanded and could not run. The two real catches
(vacuous guard, P71 deflation) improved the artifact without touching the
conclusion.

**Perelman condition 5 (external reconstruction):** still **not met**.
