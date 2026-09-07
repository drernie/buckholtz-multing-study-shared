# FINDING P208 + P209 — KG2: the two physical invariants, and why each is
# unmeasurable for a *different* structural reason

**Date:** 2026-09-07
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR
**L0 (EstimandOps): descriptive** — "what value does quantity X take under
available constraints", not causal, not predictive. No causal layer needed.
**Zero-Signal Gate:** entity = the two invariants; falsifiable predicate =
each has / has not a determined value or bound on current information;
measurable outcome = a number with an interval, or an explicit
`UNDETERMINED` plus the reason. Passed.
**Artifacts:** `scripts/p208_eotvos_eta_reduction.py`,
`scripts/p209_eta_bound_from_microscope.py`
**Answers:** `FINDING_P52` Part 7 (KG2), *"form invariance ≠ value
determined"* — the residue left open after `P206` dissolved bottleneck 4.

---

## 1. The answer in one line

After `P206`, the physical parameter space is **two-dimensional**: `Ag²`
and `η = κ/g`. **Neither is a number, and the two are blocked for
completely different structural reasons.** Neither reason is "we have not
measured enough."

| invariant | why there is no number | status of that reason |
|---|---|---|
| `A g²` | **degenerate with `G`** — universal coupling ∝ mass, effectively massless mediator ⇒ exactly Newtonian form ⇒ absorbed into the measured Newton constant | already on record (`P23`); this file only assembles it |
| `η = κ/g` | **appears in observables only multiplied by an unknown composition contrast** `\|Δψ\|`, which the model does not fix | **new** (`P208`/`P209`) |

`A` alone was already settled by `P52`/`P206`: a normalization convention.

## 2. `A g²` — nothing new here, and saying so is the point

`FINDING_P23`, verbatim, in its own "does NOT establish" section:

> *"A composition-independent coupling exactly proportional to mass is
> degenerate with `G` and evades EP tests by construction — this finding
> does not identify **any** external bound that unambiguously applies to a
> universal `g`…"*

and, citing the project's own code: *"degenerate with `G` itself, exactly
per `two_field_action_closure.py`'s own 'renormalises `G`… absorbed'
text."* `FINDING_P149` supplies the other half: at `μ ~ H₀/c` the mediator
is *"negligibly different from massless at cluster scale."* Massless plus
universal gives exactly `1/r²`, i.e. a renormalization of `G`.

The one existing number, `A g² ≲ 8.39×10⁻¹²` SI, is **12.6% of `G`**
(`G = 6.67430×10⁻¹¹`; `A g²` carries `G`'s units exactly, since
`F_mm = A g² M₁M₂/r²`, so the ratio is dimensionless — checked, not
assumed). But `FINDING_P53`, in its own user-flagged correction, already
calls it *"an external scale constraint under an explicit, unverified
mapping… **not a direct experimental bound on MULTING's own `Ag²`**"* —
because the mapping runs through a dark-matter-only coupling while
MULTING's `g` is universal.

**This section contributes framing only.** Both halves were already on
record separately; assembling them into the KG2 answer is not a discovery,
and was nearly written up as one before checking. Recorded so the next
reader does not repeat the check.

## 3. `η = κ/g` — the new work

### 3.1 What the observable actually depends on (`P208`)

`FINDING_P25` derived, sympy-verified and skeptic-reviewed, the
accelerations of two test bodies toward a source `A`. `P208` asks what
their Eötvös ratio depends on. Substituting the natural variable

```
ψ_i ≡ K_i r_i / (M_i c²)          [a LENGTH]
```

the entire composition dependence factors through `Δψ = ψ₁ − ψ₂`, and

```
η_Eötvös  =  2 · η · |Δψ| / r  ·  [1 − 3 η ψ_A / r]
          ≈  2 · η · |Δψ| / r                        [leading order]
```

**`g` survives only inside `η = κ/g`.** That is the derived part: both
terms of the `κ¹` piece could in principle have left `g` outside that
ratio, and they do not.

**What is NOT a result** (corrected after Step 8a — the first draft
overclaimed it): `A` also cancels, but every term of the acceleration is
linear in `A`, so *any* ratio is `A`-independent by construction. That is
the input structure propagated forward, not an independent confirmation of
`P206`. Consistent with `P206`; not a check on it.

### 3.2 The external number (`P209`)

`P25` named exactly what was missing (its own §4.1): *"(a) a real,
independently-verified experimental EP-bound (e.g. MICROSCOPE's actual
reported sensitivity) and (b) a real or estimated value for how
`K_i·r_i/M_i` varies across ordinary laboratory materials — **neither
attempted here**."* Item (a) is now supplied.

**[VERIFIED-arXiv 2209.15487]** Touboul et al., *"MICROSCOPE mission:
final results of the test of the Equivalence Principle"* — abstract
fetched this session:

> `η(Ti, Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵` at 1σ

Combining in quadrature (`σ = 2.746×10⁻¹⁵`) and taking `|μ| + 2σ`:

```
        η · |Δψ|   ≤   2.5 × 10⁻⁸ m          [~2σ, quadrature convention]
```

**This is the first external number in this project that bears on `η` at
all.** `FINDING_P24` established `η` as the sole cross-sector invariant
and stated it *"does not give `η` a numeric value"* — still true of `P24`.

Item (b) is **still not supplied**, and cannot be from outside: converting
the product bound into a bound on `η` needs `|Δψ|` for Ti vs Pt, and
`MODEL_SPEC_AUDIT.md` flags the `k_A,k_P` row as OPEN, *"postulate, not
sharply defined."*

## 4. Verification `[VERIFIED-run]`

| control | what it does |
|---|---|
| PC1 | `K₁=K₂=0` ⇒ `a₁−a₂=0` — reproduces `P25`'s own control |
| PC2 | `ψ₁=ψ₂` ⇒ `a₁−a₂=0` — reproduces `P25`'s second control |
| PC3 | `lim_{κ→0}` (exact ÷ leading) `= 1` — makes the leading denominator a *derived* approximation, not an assertion |
| **PC4** | the `κ²/κ¹` ratio asserted `= −3ηψ_A/r` — **added after Step 8a, see §5** |
| NC | a deliberately wrong coefficient (3 for 2) fails the same assertion |
| P209 PC1 | quadrature lies strictly between `max` and the linear sum |
| P209 PC2 | `\|μ\|+2σ` equals the two-sided max ⇒ no double-counting |

## 5. Step 8a — a real hole in my own controls, found by mutation

The skeptic's sharpest finding was not about the claim but about the
**test discipline**: PC1 and PC2 cannot see the `κ²` term at all. The
whole composition dependence factors as `(ψ₁−ψ₂)·[bracket]`, so PC2
vanishes whatever is inside the bracket, and PC1 kills the bracket
outright. The `κ²/κ¹` ratio was *printed but never asserted*.

**Mutation-tested rather than argued** — and the hole was real:

| mutant | before fix | after fix |
|---|---|---|
| `κ²` coefficient `6 → 999` | exit 0 — all asserts pass | exit 1 — `kappa^2 ratio wrong: -999*eta*psi_A/(2*r)` |
| `κ²` term deleted entirely | exit 0 — all asserts pass | exit 1 |

PC4 closes it. This is the second time this session that verifying a
skeptic's claim myself — rather than accepting or dismissing it — produced
the actual improvement.

**Verdicts and dispositions, all accepted:**

| claim | verdict | applied |
|---|---|---|
| K1 `Δψ` factoring | CONFIRMED-REAL (re-derived by hand independently) | — |
| K2 leading-order reduction | CONFIRMED-REAL (same) | — |
| K3 "independent check on `P206`" | **WEAKENED — vacuous** | reworded, §3.1 |
| K4 product bound | WEAKENED (mildly) | convention labelled; linear-addition alternative computed: **1.30× looser**, well under 2× |
| K5 illustrative table | WEAKENED | top row (`\|Δψ\|=1 m`) **removed as unphysical** — it needed k-energy ~10× rest energy; a hard cap `\|Δψ\| ≤ 0.1 m` is now asserted, and the text demands quoting the *band*, never one row |
| validity condition | WEAKENED to conditional | see §6.2 |

## 6. What this does NOT establish

1. **`η` is not determined.** Only the product is bounded. Every row of
   `P209`'s secondary table is ILLUSTRATIVE; lifting one out and quoting it
   as "`η ≲ …`" would be precisely the fit-presented-as-measurement failure
   `artifact-provenance-gates.md` Gate 2 exists to catch.
2. **The leading-order form is CONDITIONAL, and the caveat is circular in
   a real way.** Its validity check needs `ψ_A` for the Earth, estimated
   here from the *cluster* `(K/c²)/M` ratio — drawn from the same OPEN
   block that makes `Δψ` unknown. Computed margin: the check fails if
   Earth's true ratio exceeds the cluster proxy by a factor **~117**. For
   a quantity the model leaves OPEN, that is not a large margin.
3. **Nothing about MULTING** (`NO_AUTHOR_ERROR`) — this is the project's
   own reconstruction throughout, and `P25`'s k-sector is this project's
   construction, not v82's text.
4. **`A g²` is not improved.** §2 assembles existing records; the
   underlying degeneracy with `G` stands exactly as `P23` left it.
5. **The MICROSCOPE orbital radius was not verified**, only bounded to any
   LEO (16% spread). Immaterial here, but it is `[WEAK]`, not `[VERIFIED]`.

## 7. The KG2 verdict, and what would actually unblock it

**KG2 is blocked by the model's own under-specification, not by a shortage
of experiments.** Both routes to a number are model-side asks:

- for `A g²` — a demonstrated **non-universality** of `g` (or a scale where
  a finite mediator range becomes visible), since a universal `g` is
  absorbed into `G` by construction;
- for `η` — the model must **sharpen the `k` postulate** far enough to
  predict `Δψ` between two ordinary materials. `MODEL_SPEC_AUDIT.md`
  already flags exactly this row as OPEN.

That is a constructive result, not a failure to compute: the best
equivalence-principle experiment ever flown is already sharp enough to bite,
and what stops it biting is a postulate the model has not made definite.
