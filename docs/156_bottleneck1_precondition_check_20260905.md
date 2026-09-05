# docs/156 — Bottleneck 1, `docs/153` §3a precondition check: the
# "finite-r/single-pair calculation" reassessed against pre-existing,
# same-day prior work `docs/153` itself did not cite

**Date:** 2026-09-05
**Trigger:** explicit user go-ahead ("начни финитно-r/single-pair расчёт
по docs/153 итд автономно" — start the finite-r/single-pair calculation
per `docs/153`, autonomously).
**Method:** `docs/153` §3a states, in its own words, that "a future 'go'
on this specific calculation should answer these three [pre-conditions]
first, not treat this document's own framing as sufficient
preparation." This document is that check, run before writing any new
code. **No new computation is performed here** — every fact cited below
is already established and verified in `FINDING_P157`, `FINDING_P158`,
`FINDING_P158_ADDENDUM`, `FINDING_P158_ADDENDUM2`, `docs/124`,
`docs/125`, `docs/126`, all of which predate today.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (a process/gate decision, same class as
`docs/153` itself — no new physics claim beyond what those files already
record).

---

## 0. A gap in `docs/153` itself, found while running its own §3a checklist

`docs/153` (dated 2026-09-01) names `FINDING_P156` (2026-08-30) as the
evidence base for its precondition 1 ("`FINDING_P156` did not check
this [whether a finite-r analog of the S-S closure exists in closed
form]"). **It does not mention `FINDING_P157` or `FINDING_P158`** —
both dated the same day as `FINDING_P156` (2026-08-30), both already in
the repository when `docs/153` was written the next day, and both
directly relevant to precondition 1: `P157` shows the "finite-r S-S
closure" framing is itself the wrong question, and `P158` builds and
runs the mechanically-correct alternative. This is not a claim that
`docs/153` is wrong about anything it says — only that it answers §3a's
own checklist incompletely by omission, citing one same-day sibling
finding and missing two others in the same experiment folder. Per this
project's no-silent-correction convention, this is recorded here rather
than silently folded into a rewrite of `docs/153`.

## 1. Precondition 1 — "Does a finite-r analog of the S-S closure exist in closed form, or does it require a genuinely new derivation?"

**Answer: neither, precisely — and the reason is stronger than
"unattempted."** Three independent, already-established results settle
this:

1. **`docs/124`** attempted a direct Shtanov-Sahni bridge applied to
   `F_oP` — `FALSIFIED` by a context-asymmetry skeptic review
   (2026-07-19), independently reproduced.
2. **`docs/125`** attempted a matrix-factorization shortcut —
   `SPLIT VERDICT`: the algebra `CONFIRMED`, but the interpretation
   that it revives the Shtanov-Sahni bridge is `FALSIFIED`. Its own
   stated reason, `[VERIFIED-BASH]` grepped directly from the file
   today: *"`k_i r_i` has no conserved background — the evolution law
   for `q=k_i r_i` is MISSING from the corpus."* Status: `DIRECT
   SHTANOV — BLOCKED` pending that evolution law, `COSMOLOGICAL CLOSURE
   FOR q — MISSING`.
3. **`docs/126`** goes further: it proves a **non-uniqueness-of-closure
   lemma** — the corpus specifies no evolution law for `q_i(a)=k_i(a)
   r_i(a)`, and two admissible, corpus-consistent evolution laws with
   identical initial data give **different** closure outcomes. This is
   not "we haven't derived it yet" — it is a theorem that the closure
   is genuinely underdetermined by what the corpus actually specifies.

**All three predate v82 and predate any question about finite vs.
infinite `r`.** The blocker is the missing `q(a)` evolution law, not
the separation regime. A "finite-r analog of the S-S closure," as
`docs/153` §3a literally poses the question, inherits this same
blocker: whatever the separation, the second charge's evolution law is
still undefined in the corpus, and `docs/126` already shows this
underdetermines the result regardless of `r`. **There is no closed-form
finite-r S-S closure to derive, and building one from scratch would
require independently specifying an evolution law the corpus does not
supply — not a finite-r extension of existing work, a new, unlicensed
physical assumption.**

**`FINDING_P157` independently shows the deeper reason this was always
going to be the wrong target:** v82's own bridge (Eqs. 5-9) is not a
population-density-convolution object at all — it never builds a
density field, never subtracts a background, never integrates over a
population. It evaluates **one representative pair's** kinematics
directly. Shtanov-Sahni's entire machinery (`docs/124`'s own Eqs.
15-18) is a **population integral**, `∫[ρ(r')-ϱ]φ(a,|r-r'|)d³r'` — a
structurally different mathematical object from what v82 computes,
independent of whether `r` is finite or `r→∞`. Asking "what is the
finite-r version of the S-S closure" was never quite the right
question; the right question, per `P157`'s own reframing, is whether a
single representative pair's evaluation is a valid proxy for what a
genuine population average would give — and **that** question has a
tractable, mechanically-correct tool: Jensen's inequality / covariance
on v82's own mass-derived scalar chain (`r_X(z)`, `k_X(z)` as
deterministic power laws of `m_X(z)` alone, v82's own Eqs. 10-14).

**Verdict on precondition 1: NO closed-form finite-r S-S analog exists
or is derivable without a new, unlicensed assumption (proven by
`docs/126`, confirmed by two independent prior attempts). The
mechanically-correct alternative calculation DOES exist in closed form
and has already been built and run — see §3.**

## 2. Precondition 2 — "Is the single-pair, externally-oriented regime tractable with existing machinery?"

**Answer: yes, for the mechanically-correct calculation (Jensen's
inequality on the mass chain), already built.** `FINDING_P158`'s script
(`P158_jensen_mass_averaging_v82_force_terms.py`) uses `sympy` (exact
closed-form derivation) cross-checked against Monte Carlo
(`N=4×10⁶`), ruff-clean, does not touch the main 908-test suite.
`FINDING_P158_ADDENDUM2`'s script
(`P158_addendum2_real_mass_function.py`) extends this with real,
peer-reviewed, off-the-shelf tools (`hmf`/Murray-Power-Robotham 2013
backed by `camb`, for the Tinker et al. 2008 mass function; Tinker et
al. 2010 halo bias, coefficients verified against the primary source).
Both are already-existing, already-verified, already-controlled code —
not a new construction this project has yet to build.

**Not tractable, and not attempted by anyone in this thread:** a
literal implementation of `docs/153`'s own proposed decisive test
(compute the *same intermediate quantity* via **both** v82's route
*and* this project's own S-S closure route, then compare) — because
route 2 has no closed-form construction per §1 above. This specific,
literally-worded test is **not currently buildable**, independent of
effort spent, without first resolving the missing `q(a)` evolution law
`docs/126` already proved is underdetermined by the corpus.

## 3. Precondition 3 — "What would each outcome change? Is cost proportionate to consequence?"

**Answer: partially resolved, unevenly across v82's own redshift
range, and the honest cost estimate is *higher* than a first pass
suggested — this is itself informative, not a null result.**

`FINDING_P158`'s Jensen's-inequality calculation gives a
`CONDITIONAL-DIRECTIONAL-PREDICTION`: **if** paired nodes' log-masses
have correlation `ρ>−0.5`, population-averaging enhances `F^(2)`
(quadrupole) more than `F^(1)` (dipole) — pushing Table III's already-
small net residual (`+4%` to `+6%`, from nearly-cancelling `F^(1)≈+53%`
and `F^(2)≈−46.5%`) further from zero, not toward it. Below that
threshold, the direction reverses.

`FINDING_P158_ADDENDUM` (literature-grounding attempt) was **REJECTED**
— a context-blind skeptic found both proposed real-world proxies
(`σ_lnm` from mass-estimation-method scatter; `ρ`'s sign from halo-bias
literature) were category errors: real citations, wrong physical
quantities.

`FINDING_P158_ADDENDUM2` then **computed** `ρ` from first principles
(real halo mass function + Tinker10 bias + matter correlation
function, three real bugs caught and fixed along the way, one more by
a dispatched skeptic). Result, **WEAKENED** after that skeptic pass:

| Redshift range | Result | Trustworthy? |
|---|---|---|
| `z=0` to `z=0.5` (4 of v82's 8 target `z`) | `ρ` small, real, positive (`+0.0008` to `+0.010`) | **Yes** — inside Tinker et al.'s calibrated `ν` range |
| `z≥1.07` (other 4 of 8) | `ρ→0` in the saturating linear-bias regime | **No** — `ν` reaches up to `50` at `z=5`, a 50-sigma extrapolation far past anything the fit was ever validated against |

**Consequence, honestly scoped:** for the low-`z` half of v82's own
target range, this project now has a real, grounded (not illustrative,
not wrongly-proxied) `ρ>0`, safely above `P158`'s `ρ>−0.5` threshold —
the population-averaging correction genuinely favors `F^(2)` over
`F^(1)` there, and Table III's own coefficients (`a≈0.53`, `b≈0.465`,
satisfying `a<2b`) mean this pushes the net force balance further
negative, not toward zero, for any real scatter size. For the high-`z`
half, **no trustworthy directional claim exists without materially
more specialized work** (nonlinear halo bias or direct N-body pair
statistics) — `ADDENDUM2`'s own conclusion, confirmed here rather than
re-derived.

**Cost-vs-consequence verdict:** cheap, already-paid cost has bought a
real (if narrow) result for half the range; the other half requires a
qualitatively bigger investment (specialized nonlinear-bias or N-body
work) that neither this project nor its existing machinery currently
supports. This is a legitimate, informative outcome under
`falsification-ladder.md`'s Cheapest Differentiating Test Protocol —
not a reason to force the expensive half now.

## 4. Verdict

**`docs/153`'s own literally-worded "finite-r/single-pair calculation"
is NOT the right next step and is not currently buildable** — its
implicit assumption (that this project's own S-S closure has, or could
cheaply acquire, a finite-r closed form to compare against) is refuted
by three independent, pre-existing results (`docs/124`, `docs/125`,
`docs/126`) that predate `docs/153` itself and that its own §3a
checklist did not check against.

**The mechanically-correct question `FINDING_P157` identified, and
`FINDING_P158`→`ADDENDUM2` already substantially answered, is a
different, narrower, but real and tractable one:** does using v82's own
representative-pair force evaluation, instead of a proper population
average over its own mass-derived scalar chain, bias the force-tier
balance — and if so, in which direction? **Answer, honestly scoped: yes,
for `z≤0.5` (4 of 8 target redshifts), with a real, grounded, positive
`ρ` — population-averaging pushes the net force balance further
negative (away from cancellation), not toward it. For `z≥1.07`, this
project has no trustworthy answer without a materially larger
investment.**

**Per the Adaptive Iteration Branch Rule** (`falsification-ladder.md`):
re-attempting `docs/153`'s own literal route from scratch would repeat
work already independently killed three times (`docs/124`, `docs/125`,
`docs/126`) for a reason unrelated to `r` — not licensed without a
genuinely new condition (a real `q(a)` evolution law from a new source,
which does not exist). **This document does not recommend attempting
it.**

## 5. What remains genuinely open, cheap, and not yet attempted

`FINDING_P158_ADDENDUM2` itself names one explicit, unaddressed gap
(its own "Objection 2, accepted as an open limitation, not run this
pass"): the population-floor choice (`M ≥ M_of(z)/2`, v82's own
characteristic mass, halved) was never checked against nearby
alternatives (`M_of(z)/4`, `M_of(z)`, a bounded bin) for sensitivity.
This is:

- **Cheap** — reuses `ADDENDUM2`'s own already-built, already-verified
  pipeline (`hmf`+Tinker10+`ξ_mm`), only the floor parameter changes.
- **Well-scoped** — a single new condition (floor choice), per the
  Minimal Relaxation Rule, not a bundle of changes.
- **Directly strengthens or weakens the one real result this whole
  thread has produced** (the `z≤0.5` grounded `ρ>0` finding) — if `ρ`'s
  sign or its distance from the `−0.5` threshold is sensitive to the
  floor choice, the "safely above threshold" framing needs qualifying;
  if it is not sensitive, the result gets materially more robust for
  free.

This is the concrete, cheapest differentiating next step this document
recommends — continuing the user's "start the finite-r/single-pair
calculation, autonomously" instruction via the mechanically-correct,
already-tractable line of work this bottleneck actually supports, not
via `docs/153`'s own literal, independently-blocked framing.

## What this document does NOT establish

1. **Not a claim that `docs/153` is wrong about anything it asserts** —
   only that its own §3a checklist, run here, surfaces same-day prior
   work it did not cite, changing what the checklist's answer actually
   is.
2. **Does not run the floor-sensitivity sweep** — names it as the
   concrete next step (§5), does not attempt it in this document.
3. **Does not resolve bottleneck 1 as a whole** — `docs/147`'s own
   "F→H_MULT(z)" bridge status is unaffected; this document is scoped
   entirely to `docs/153`'s own narrower causal-compatibility question.
4. **`NO_AUTHOR_ERROR`** — entirely a claim about this project's own
   reconstruction attempts (`docs/124`-`126`) and this project's own
   gate-process history, never about Dr. Buckholtz's own theory or v82.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
