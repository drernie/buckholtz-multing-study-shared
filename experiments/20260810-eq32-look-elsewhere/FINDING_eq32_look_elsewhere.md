# Eq.32 survives its own falsifier, at p ≈ 0.16

**Date:** 2026-08-10 · **L0:** Descriptive
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

---

## Why this was overdue

NR-009 (2026-06-23) killed the S³-geometry explanation of Eq.32's `(4/3)`
prefactor by enumerating ~456 equally-simple `(prefactor, exponent)` families that
coincide at n = 3. The enumeration was built for that purpose and then left
unapplied to the claim it was defending — Eq.32 itself.

The gap is a category confusion this project has flagged in other contexts and
then reproduced here. **"Eq.32 holds at 0.17σ" is a statement about the PDG
uncertainty on m_τ given the formula.** It says nothing about the probability of
finding such a formula somewhere in an admissible expression space. Only the first
had ever been computed.

---

## Search space — declared before scanning

| element | choice | count |
|---|---|---|
| prefactor | simple rationals `p/q`, `p, q ≤ 12`, lowest terms | 91 |
| mass ratio | every ordered pair from {e, μ, τ, u, d, s, c, b, t, W, Z, H, p} with ratio > 1 | 78 |
| exponent | integers 1 … 24 | 24 |
| **expressions** | | **170 352** |

Target: `α_EM/α_G` with `α_G = (m_e/m_Planck)²`, PDG 2024.

**Anchor verified first:** `(4/3)(m_τ/m_e)¹² / (α_EM/α_G) − 1 = 0.01354 %`,
matching the published 0.0135 %. `[VERIFIED-BASH]`

---

## Step 1 — hits at Eq.32's own precision

| tolerance | hits | per 1000 expressions |
|---|---|---|
| 0.0010 % | 0 | 0.00 |
| **0.0135 %** (Eq.32) | **1** | 0.01 |
| 0.1000 % | 2 | 0.01 |
| 1.0000 % | 12 | 0.07 |
| 5.0000 % | 64 | 0.38 |

At its own precision Eq.32 is the **unique** hit in 170 352 expressions.

**This is the misleading number, and quoting it alone would be the same error the
finding is about.** Uniqueness at a given precision says nothing until one knows
how precise the best available hit would have been for an *arbitrary* target.

## Step 2 — the null, which is the actual measurement

4000 random targets drawn log-uniformly within ±1 decade of `α_EM/α_G`; for each,
the best hit available in the *same* space.

| | best hit |
|---|---|
| median random target | 0.05632 % |
| 10th percentile | 0.00823 % |
| 1st percentile | 0.00075 % |
| **real target (Eq.32)** | **0.01354 %** |

```
look-elsewhere p = 0.157
```

**About one arbitrary target in six does at least as well.** Eq.32 sits between
the median and the 10th percentile of what this expression space achieves for a
number picked at random.

---

## What this changes, and what it does not

**Does not change.** The numerical relation stands. `n = 12` is still the unique
integer *at fixed form* — adjacent integers miss by ~10⁵ %. The relation remains a
striking arithmetic fact and the Belle II prediction it generates (m_τ = 1776.840
MeV if exact) is unaffected: that prediction is falsifiable regardless of how the
formula was found.

**Does change.** The claim "Eq.32 holds at 0.17σ" is formally correct and
rhetorically misleading without this p. 0.17σ measures experimental precision
given the formula; the search that produced the formula is not free, and its cost
is now measured at p ≈ 0.16 — modest, not extraordinary.

`paper/main.tex` states the 0.17σ figure in four places (abstract, §2 `ssec:eq32`,
the assessment table, conclusions) without the trials factor. Corrected in the
same session; leaving it would apply a softer standard to our own surviving claim
than the one applied to the author's.

---

## Symmetry of application

The same enumeration, on the same project:

| target | verdict |
|---|---|
| S³ geometry explains `(4/3)` (NR-009) | **killed** — ~456 equally simple families |
| F₄/G₂ explains `{4/3, 12}` (2026-07-17) | **killed** — same failure mode, different vocabulary |
| **Eq.32 itself** | **survives, p ≈ 0.16** |

The tool was consistent: it spared neither the external hypothesis nor ours.

---

## Three caveats

1. **The space boundaries are mine.** Prefactors to 12, exponents to 24, thirteen
   particles. A wider grammar raises the trials factor and lowers p; a narrower one
   raises it. The bounds were declared before scanning but are not derived from a
   principle, so p ≈ 0.16 carries that arbitrariness.
2. **The null randomises the target.** An alternative null — random masses at fixed
   target — probes a different question and could give a different p.
3. **7:9:17 is not covered.** It has a different structure (a triple of small
   integers, not prefactor × power) and needs its own enumerator. Its `0.4σ` claim
   therefore still stands uncorrected for trials.

---

## Epistemic summary

| statement | status |
|---|---|
| Anchor reproduces the published 0.0135 % | **[VERIFIED-BASH]** |
| Eq.32 is the unique hit at its own precision in this space | **[VERIFIED-BASH]** |
| Look-elsewhere p ≈ 0.157 within the declared space | **[VERIFIED-BASH]**, conditional on caveat 1 |
| Eq.32 is a genuine physical relation | **[UNKNOWN]** — unchanged by this work |
| Eq.32's numerical agreement is extraordinary | **[FALSIFIED as stated]** — it is ordinary for a target of this magnitude searched over this space |
| 7:9:17 corrected for trials | **[UNKNOWN]** — enumerator not built |

---

# Addendum — 7:9:17, and it goes the other way

Built the same session. The prediction implicit in the sentence this addendum
replaces — that 7:9:17 would carry "the same uncorrected-trials caveat" — was
**wrong**, and wrong in the direction that favours the relation.

## Why a separate enumerator

Eq.32 is `prefactor × (mass ratio)^n`. Eq.31 fixes **two scale-free ratios with a
triple of small integers**. Different grammar, different null, different limiting
uncertainty. Reusing the Eq.32 enumerator would have measured the wrong space.

**Metric** — the paper's own: the relation is scale-free, so a triple is scored by
the *largest* residual over the three masses at the best free scale, precisely
because anchoring on one boson makes that boson exact by construction. In logs
with `u_i = ln m_i − ½ ln n_i` the minimax residual is `(max u − min u)/2`, exact
and optimiser-free.

**Anchor** `[VERIFIED-BASH]`: (7,9,17) gives **0.0500 %**, against the paper's
stated "< 0.05 %". Z-anchored cross-check reproduces the paper's 125.33 and 80.420.

## Result

| N (simplicity bound) | coprime triples | p |
|---|---|---|
| 17 | 613 | **0.0040** |
| **20** | 997 | **0.0040** |
| 25 | 2 017 | 0.0093 |
| 30 | 3 472 | 0.0196 |
| 40 | 8 410 | 0.0463 |
| 50 | 16 648 | 0.0785 |

**(7,9,17) is the unique best triple all the way to N = 50** — none of 16 648
candidates beats it. At N = 20 the median random target manages only 0.64 %,
thirteen times worse.

Robustness to the null's window, at N = 20: p = 0.0051, 0.0060, 0.0024, < 0.0005
for target ranges ×1.2, ×1.5, ×2.0, ×3.0. **Stable against the window, sensitive
to N.**

## The comparison, and why it must be stated weakly — correction 2026-08-10

An earlier draft of this addendum wrote "about forty times less likely to be
coincidental", from 0.16 / 0.004. **Withdrawn.** The arithmetic is right and the
inference is not: the two p-values come from grammars of different dimension
(Eq.32's is one-dimensional, this one two-dimensional) and from different
pre-specified spaces. Comparing them as measures of evidential strength requires
harmonising the null spaces first, which has not been done.

| | space | dimension | p |
|---|---|---|---|
| Eq.32 | 35 672 statable expressions | 1-D log scale | **0.16** |
| 7:9:17 | 997 coprime triples, N ≤ 20 | 2-D ratio space | **0.004** |

Defensible statement: *under its own declared grammar each relation carries a
measured trials factor, and that factor is substantially smaller for 7:9:17.*
Not: *7:9:17 is forty times better evidence.*

## Objections checked, with what each returned

Raised by an external reading of this finding; each was verified rather than
accepted or dismissed. `[VERIFIED-BASH]` throughout.

| objection | outcome |
|---|---|
| 997 ≠ C(20,3) = 1140 — where did 143 go? | **Answered.** The gcd = 1 filter removes multiples: (14,18,34) states the same proportion as (7,9,17). They are duplicates, not competitors. Deduplication, not a post-hoc filter — but it had not been documented, and now is. |
| The claim is in **squared** masses; does working in mass units change the null's geometry? | **No.** The metric ratio squared-units / mass-units is exactly 2.000000 for every triple — a monotone rescaling, so rank and p are identical. Mass units are reported because that is the paper's own convention. |
| Ordering W/Z/H adds a 3! = 6 trials factor | **It does not.** `m_W < m_Z < m_H` forces `a < b < c`: assigning (17,9,7) would require m_W²/m_Z² = 17/9 > 1. The assignment is not free. |
| The null should sample ratio space, not integer triples (their "Null B") | **Already does.** The code randomises the *target* log-ratios, not the candidate triples. The existing null is Null B. |
| Add a measurement-space null (their "Null C") | **Run, and it is the strongest single result here.** Drawing 3000 pseudo-datasets from the PDG uncertainties, (7,9,17) is the best triple in **100.0 %** of them. The rank is not an artefact of the central values. |

## Open — and the reason the status is *moderate*, not *strong*

**Null D, grammar expansion, has not been run.** Rationals, small composites,
affine forms and alternative integer parametrisations were never admitted to the
space. Each would raise the trials factor by an unmeasured amount.

**Researcher degrees of freedom precede the enumeration.** The grammar — integers,
coprime, ≤ 20, minimax metric, ordered — was declared before *scanning*, which is
not the same as before *knowing the answer*. Every choice was made by someone who
already knew (7,9,17). No enumeration removes that, and it is the reason this is
recorded as moderate evidence for an unusually close small-integer structure in a
physically motivated observable space, and not as evidence of a mechanism.

## What the enumerator actually established, which is more durable than 0.004

```
p = p(grammar, metric, null model)
```

| N | 17 | 20 | 25 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|
| p | 0.0040 | 0.0040 | 0.0093 | 0.0196 | 0.0463 | 0.0785 |

A twentyfold swing from a choice with no principled basis. Eq.32's
one-dimensional grammar showed no comparable sensitivity. **Significance turned
out to be a property of the search space as much as of the number** — and that,
rather than any particular p, is what the exercise measured.

This is the same shape as this project's β₁/β₂ result one level down: there, the
data constrained a combination far better than either parameter; here, the data
constrain the ratio pair well while the *significance* depends on which region of
that space is allowed to count as simple. In both cases the headline quantity is
less uniquely determined than the headline fit suggests.

## Paper updated accordingly

`paper/main.tex` now carries: the result with its bound, the gcd/ordering/units
clarifications, Null C, the explicit statement that the two p-values are **not
directly comparable**, and the admission that both grammars were chosen after the
relations were known. Compiles clean, 14 pages, 0 undefined.

## Why the N-dependence is stronger here

Prefactor-power expressions cover a one-dimensional log scale densely: 35 672
values across ten decades hit 0.06 % almost always. Triples cover a
**two-dimensional** ratio space, where matching to the same precision needs
quadratically more candidates, and their count grows as N³. Hence p rises twentyfold
from N = 20 to N = 50 while Eq.32's showed no comparable sensitivity.

**p ≈ 0.004 must never be quoted without its bound.**

## A second observation

The 0.0500 % residual already sits **below the 0.0879 % the data can resolve**
(dominated by `σ_H = 0.11` GeV). The relation agrees as closely as current
measurements permit, so **m_H precision is a discriminant alongside the W-mass
combination** — the paper named only the latter.

## Paper updated

`paper/main.tex` §Conclusions previously stated this correction "has not been
computed". Replaced with the result, the bound, the robustness range and the
forty-fold comparison; the assessment table row now carries
`trials-corrected p = 0.004 (a,b,c ≤ 20)`. Compiles clean, 14 pages.

## Artifacts

`ratio_triple_look_elsewhere.py` — this folder. Vectorised over the triple set,
seed 20260810, ruff clean, verifies the anchor against `paper/main.tex` before
scanning.

## Artifacts

`eq32_look_elsewhere.py` — this folder. Declares the space in code, verifies the
anchor before scanning, ruff clean, seed fixed at 20260810.
