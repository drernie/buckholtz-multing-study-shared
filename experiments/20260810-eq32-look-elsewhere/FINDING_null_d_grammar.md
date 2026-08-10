# Null D — the trials factor measures the search, not the relation

`NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION` · L0 descriptive
2026-08-10 · script: `null_d_grammar_expansion.py` · ruff clean

## What was asked

An external reader objected that "integers ≤ 20" is a grammar **we** chose, and
that a p-value measured inside it reports our choice as much as the relation.
The objection is correct. Null D answers it by enumeration rather than argument:
run the identical metric across twelve grammars a physicist might plausibly have
written down instead, and watch what p does.

## The move that made the grammars comparable

The relation is scale-free, so a candidate is a **proportion**, not a triple. Any
rational triple clears to integers by multiplying through by the lcm of the
denominators and dividing by the gcd. Every grammar is therefore canonicalised to
a coprime integer triple before anything is counted.

This is not bookkeeping — it is the result. "Rationals" is not a larger space than
"integers"; it is a differently-shaped **subset of the same space**. The prior
run's separate "rationals" column was measuring a reparametrisation, not a new
degree of freedom.

## Result 1 — p is proportional to the size of the search

Seven of the twelve grammars can express `(7,9,17)`. All seven return the same
best deviation, 0.0500 %, so they are scored against an identical threshold and
are directly comparable.

| grammar | \|G\| | p | 10⁶·p/\|G\| |
|---|---:|---:|---:|
| integers ≤ 17 | 613 | 0.00317 ± 0.00022 | 5.18 |
| integers ≤ 20 | 997 | 0.00495 ± 0.00028 | 4.97 |
| rationals p≤20 q≤2 | 2 839 | 0.01357 ± 0.00046 | 4.78 |
| integers ≤ 30 | 3 472 | 0.01763 ± 0.00052 | 5.08 |
| rationals p≤20 q≤3 | 8 412 | 0.03789 ± 0.00075 | 4.50 |
| rationals p≤20 q≤4 | 14 184 | 0.05873 ± 0.00192 | 4.14 |
| integers ≤ 50 | 16 648 | 0.07740 ± 0.00218 | 4.65 |

Fit: **p = 7.1×10⁻⁶ · |G|^0.95**, median residual **2 %**. Equivalently p/|G| is
constant to 25 % across a 27× range of grammar size — and the integer and
rational families **interleave** on that line rather than occupying separate
curves.

So the trials factor is, to within tens of percent, just the count of distinct
proportions the grammar admits. **The significance of 7:9:17 is a property of
where "simple" is cut, and nothing in the relation fixes that cut.** This is the
central finding: significance turned out to be a property of the search space,
not only of the number.

## Result 2 — "simple" is at least two independent axes

Five grammars **cannot state the relation at all**, and they are not small:

| grammar | \|G\| | best achievable |
|---|---:|---:|
| integers ≤ 12 | 196 | 1.479 % |
| arithmetic progressions a, a+d, a+2d | 555 | 7.160 % |
| squares of a,b,c ≤ 20 | 997 | 0.435 % |
| 7-smooth ≤ 200 | 24 441 | 0.166 % |
| 11-smooth ≤ 200 | 52 141 | 0.143 % |

11-smooth ≤ 200 is **three times larger** than integers ≤ 50 and still cannot
express `(7,9,17)`, because 17 is prime and the triple is neither an arithmetic
progression nor a ratio of squares.

`7:9:17` is simple by **magnitude** and not simple by **factorisation** or by
**pattern**. A trials factor quoted without naming which axis of simplicity it
ranges over is incomplete. (Their p-values are omitted from the comparison above
on purpose: each is scored against its own, far looser, best deviation, so they
answer a different question. Pooling all twelve into one fit gave a 94 % median
residual — not a weak law, a mixed-up one.)

## An error this run forced, and why the conclusion survived it

The first pass drew 30 000 targets (17 407 valid) and reported p = 0.0034 for
integers ≤ 20. Three independent 400 000-draw runs give 0.00497, 0.00513, 0.00492.
The first figure was a **3.4 σ low fluctuation of the same estimator**, not a
different quantity; the module's implementation was verified identical by running
it directly at high statistics.

The conclusion survived only because of an accident of design: every grammar was
scored against the **same** target set, so the fluctuation was common to all of
them. It depressed the absolute p values together and left the p-vs-|G|
proportionality untouched. Shared-draw designs are robust in the ratios and
fragile in the levels — worth remembering, and not a licence to under-sample. The
script now spends its draw adaptively: grammars whose p is already large get the
cheap pass, small-p grammars get the full one.

**Consequence for the paper.** p was previously written as 0.004 — one draw of a
Monte-Carlo estimate quoted as if it were a constant. The supported value is
**p = 0.005 ± 0.0002** (95 % CI 0.0048–0.0054, K = 233 726), *conditional on
integers ≤ 20*, and it must never appear without both the bound and the
uncertainty.

## Result 3 — the isolation test, which discriminates and comes out against H₁

A bare p conflates two hypotheses. **H₁:** the triple has structure making it
unusually close to the data. **H₀:** it is the nearest neighbour in a dense
enough discrete space. A special point should be not only *close* but
*isolated*, so we record for each target both `D₁` and the runner-up gap
`D₂ − D₁`.

| | integers ≤ 20 | integers ≤ 50 |
|---|---:|---:|
| observed `D₂/D₁` | 14.71 | 4.89 |
| median `D₂/D₁` among *equally close* random targets | **18.00** | **4.49** |
| `P(gap ≥ observed \| D₁ ≤ observed)` | **0.338** | **0.186** |

Conditional on being close, `(7,9,17)` is **no more isolated than a typical
random target** — at N=20 slightly less. The isolation dimension contributes no
evidence beyond closeness, and closeness is exactly the quantity Result 1 shows
to be set by grammar density. This is the test that discriminated, and it
discriminated toward H₀.

## Result 4 — two uncertainties, differing by two orders of magnitude

- `σ_MC` = ±0.0002 (binomial, K = 233 726)
- `σ_spec` = 0.003 → 0.077 across the grammars scanned

Quoting `p = 0.0051 ± 0.0002` as *the* significance is therefore wrong even
though both numbers are correct: the stated error is the small one. No single
number is the significance of this relation.

## What Null C does and does not test

`7:9:17` wins 100 % of 3000 PDG-resampled pseudo-datasets. This asks whether
noise of order 0.088 % can dislodge a triple already 0.050 % away — almost
tautologically it cannot. It is a **robustness-to-measurement-error** test, not
a look-elsewhere test, and it was previously at risk of being read as the
latter. Relatedly, the grammars in which the rank persists are largely **nested**
(integers ≤20 ⊂ integers ≤50 ⊂ the rational families), so "still #1" shows no
competitor *appeared*, which is weaker than showing none was *expected*.

## On the exponent 0.95

Not a discovered law. For a nearest neighbour among |G| candidates at roughly
uniform density, the rare-event probability of landing within a fixed radius
grows as |G|·V_d(r), so an exponent near 1 is what a correctly behaving
enumerator must return. Its value is **diagnostic**: it confirms p is being set
by candidate density and essentially nothing else — which strengthens, not
weakens, the specification-dependence conclusion.

## Out-of-sample status: none of the present agreement is

Anchoring on m_Z: m_H = 125.3254 GeV (+1.14σ), m_W = 80.4199 GeV (**+3.92σ**).
All three masses entered the selection of the triple, so no part of the reported
agreement is out-of-sample; and the W prediction is already in tension. Future
m_H and m_W measurements are the genuine out-of-sample test, because the
relation's predictions are sharper than present data.

## Epistemic status, componentwise

| component | status |
|---|---|
| closeness of 7:9:17 to the masses | established |
| exhaustive enumeration within declared grammar | strong |
| robustness to measurement error (Null C) | strong, but tests only this |
| uniqueness within the chosen (nested) grammars | moderate |
| `p ≈ 0.005` as a universal significance | **not established** |
| `p ∝ \|G\|^0.95` | expected scaling, confirmed, diagnostic |
| unusual isolation (`D₂−D₁`) | **tested, negative** |
| physical specificity of 7:9:17 | unknown |
| predictive power beyond W/Z/H | untested; the decisive next test |

## What this does NOT mean

1. It does **not** show `7:9:17` is a coincidence. Within every grammar that can
   state it, it remains the unique best triple and sits at the data's own
   resolution limit (0.088 %).
2. It does **not** license comparing this p with the Eq.32 p. Those range over
   grammars of different dimensionality with unharmonised nulls.
3. It does **not** identify a privileged grammar. It shows the opposite — that no
   principled cut exists, which is why the bound must always be quoted.
