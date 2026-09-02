# NR-021 — Formalizing H1' (DoF-ratio criterion): data collection run,
# real N=11 (not 30-60), two independent problems found, point estimate
# runs opposite to H1's own predicted direction

**Date:** 2026-09-02
**Continues:** `STAT_PROTOCOL_H1prime_dof_criterion.md`'s own "next step,
not started" — actual literature search + coding + delegated blind-check
+ regression, per explicit user go-ahead ("го собирай").
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (a methodology exercise about a
historical-record criterion, not a new physical claim about Eq.32 or
MULTING)

---

## What was attempted

Literature search for ≥55 additional real, well-documented historical
"numerical-coincidence" physics cases (beyond NR-020's original 5:
Titius-Bode, Eddington-137, Dirac LNH, Koide, Balmer), to reach the
N≈60 the protocol's own power analysis found necessary, then a
3-predictor logistic regression per that protocol.

## What was actually found — a real feasibility ceiling, not laziness

Multiple rounds of targeted search (WebSearch + arXiv, ~20 queries)
found **6 more real, well-documented, coherently-codeable cases**, for
a total of **N=11** — nowhere near 30, let alone 60:

| Case | Year | Outcome | Source |
|---|---|---|---|
| Gell-Mann-Okubo mass formula | 1961/62 | SURVIVED (predicted Ω⁻, 0.72% off) | en.wikipedia.org/wiki/Gell-Mann–Okubo_mass_formula |
| Kepler's Mysterium Cosmographicum | 1596 | FAILED (abandoned on better data) | en.wikipedia.org/wiki/Mysterium_Cosmographicum |
| Wyler's formula for α | 1969 | FAILED (real math error found, arbitrary radius=1) | PhysRevLett.27.1545 |
| Lenz's 6π⁵ ≈ m_p/m_e | 1951 | SURVIVED (weak — never refuted, but also never tested) | fermatslibrary.com/s/the-ratio-of-proton-and-electron-masses |
| Moseley's law | 1913 | SURVIVED (predicted undiscovered elements Z=43,61,75) | en.wikipedia.org/wiki/Moseley%27s_law |
| Nambu sum rule (τ-mass) | 1980 | SURVIVED, but MIXED (same model's top-quark prediction was later wrong) | PhysRevD.22.2921 |

**Many candidate leads did not qualify** for this narrow reference class
(a simple, few-parameter algebraic identity between measured constants —
NOT a full theory): Bohr-Sommerfeld quantization (a whole theoretical
framework, not a simple formula), SU(5) proton-decay (many-parameter
GUT), Garrett Lisi's E8 (framework, and its "test" is absence-of-
detection, not a clean pass/fail), Bethe-Weizsäcker mass formula
(continuously-refined multi-nucleus fit, not a single fixed-target
identity), Sommerfeld's 1916 "miracle" (right numbers for the wrong
mechanism — genuinely interesting but doesn't fit the DoF-ratio framing
cleanly, excluded rather than forced), Titius-Bode-on-exoplanets
(contested/ambiguous outcome in the literature itself, excluded to avoid
forcing a fake-precise binary code).

**This is itself the first honest finding**: the reference class NR-020
implicitly defined (Eq.32-shaped: prefactor/exponent/ratio matching a
target constant) is narrower in the real historical record than a quick
read suggested. N≈60 is very unlikely to be reachable without either
broadening the reference class (compromising coding coherence) or
including poorly-documented/fringe cases (compromising evidence
quality) — a real, reportable constraint, not a failure to search hard
enough.

## Blind inter-rater check (delegated, per protocol) — the more
## important finding, found BEFORE the regression even ran

A fresh `Agent(skeptic)` with zero context from this session independently
coded 4 of the 11 cases (Titius-Bode, Koide, Gell-Mann-Okubo, Kepler)
from the same raw facts, with no access to this session's own codings.

**Outcome agreement: strong.** 3/4 clean matches (Koide=1, Gell-Mann-
Okubo=1, Kepler=0). The 4th (Titius-Bode) the blind coder *independently*
flagged as genuinely ambiguous (Uranus 1781 fit, Neptune 1846 didn't) —
without being told this session had the same concern — a good sign for
outcome-coding reliability specifically.

**DoF-ratio agreement: poor.** Real, substantive divergence, not noise:

| Case | This session's coding | Blind coder's coding | Ratio |
|---|---|---|---|
| Titius-Bode | 0.33 | 0.6–0.8 | ~2x |
| Koide | 0.50 | ≈0 | ∞ (categorical disagreement on whether form-choice counts as DoF) |
| Gell-Mann-Okubo | 0.83 | 0.67–1.0 | ~1.2x (closest agreement) |
| Kepler | 0.17 | 1.0 (self-flagged alternate: 0.2) | ~6x |

**ansatz_size agreement: poor**, no consistent pattern (me: [3,3,3,5];
blind coder: [5,4,2,4]).

**What this means:** before reaching any power question, H1's own
PRIMARY predictor (DoF-ratio) is **not reliably codeable** from
historical facts by independent raters using the same protocol — different
reasonable people count "what counts as a free parameter" differently
(is choosing a functional FORM itself a degree of freedom, or only its
numeric coefficients?). This is a real methodological problem for H1',
independent of and arguably more serious than the sample-size problem
already found in `STAT_PROTOCOL_H1prime_dof_criterion.md`.

## The regression itself (real N=11, single-coder data)

Logistic regression (`scratchpad/h1_prime_regression.py`, statsmodels),
outcome ~ dof_ratio(z) + prestige + ansatz_size(z):

```
dof_ratio_z:  coef=+2.24, p=0.169  (WRONG DIRECTION vs H1's own prediction)
prestige:     coef=+0.04, p=0.981  (no effect, as expected -- not the mechanism)
ansatz_z:     coef=-2.93, p=0.095  (correct-direction, marginal, weakest-coded covariate)
LLR p-value = 0.153 (whole model not significant)

Simple cross-tab (median split): high DoF-ratio group 5/8 survived (62.5%),
low DoF-ratio group 1/3 survived (33%) -- again opposite to H1's
predicted direction.
```

**Not significant — expected, given N=11 is far below the protocol's own
N≈60 target** (recall the MDE analysis: N=30 could only detect OR≥5.0;
N=11 is nowhere near that). But the **point estimate runs opposite to
H1's own claimed direction** — higher DoF-ratio associated with MORE
survival in this small sample, not less.

## Kill Analysis (per Minimal Relaxation Rule)

**What this does NOT establish:**
1. Does NOT prove H1' is backwards — N=11 is small enough that this
   direction flip is fully consistent with pure sampling noise (the
   confidence interval on dof_ratio_z spans -0.95 to +5.44, comfortably
   including zero and even the originally-predicted negative direction).
2. Does NOT prove H1' is false in general — underpowered null results
   are uninformative about the true effect, not evidence against it.

**What this DOES establish, more durably than the null p-value:**
1. **A real feasibility ceiling** on reaching N≈60 for this reference
   class from accessible literature (N=11 achieved after real, serious
   search — informative in itself).
2. **A real inter-rater reliability problem** with the DoF-ratio
   predictor's own operational definition — this is the harder, more
   fundamental obstacle. A criterion that different careful coders
   estimate 2-6x apart for the same case is not yet a usable
   quantitative instrument, independent of how much data is collected.

**Relaxation Map:** the single most promising fix is not "collect more
data" (the N-30-60 problem) but **first fix the DoF-ratio operational
definition** (a precise counting rule: does choosing a functional FORM
count as 1 DoF regardless of complexity, or should form-space be
measured continuously — closer to `ansatz_size`? are the two covariates
actually double-counting the same underlying thing, which the modest
correlation baked into the earlier MDE simulation already assumed?) —
before any further data collection is worth the effort.

## What this means for Eq.32 / NR-020 (NO_AUTHOR_ERROR)

**Does not strengthen or weaken NR-020's own qualitative read** ("Eq.32
sits structurally closer to the failure cluster") — that read was based
on comparing Eq.32 informally against the *original* 5 cases, not on
this formal regression, which turned out too underpowered and too
coding-unreliable to add or subtract confidence from that qualitative
placement. NR-020's own status (provisional, `H1' not independently
attacked in its final form`) is unchanged by this file — if anything,
this file shows that a rigorous *quantitative* version of H1' is further
away than it looked from the protocol document alone, and the honest
current state of the whole H1' program is: **qualitative comparison
only, formalization attempted and found to have two independent, real
obstacles (feasibility, reliability) before power was even the binding
constraint.**

## What this file does NOT establish

1. Does not claim the 11-case dataset itself is definitive — a different,
   larger, more carefully-defined-DoF-ratio dataset could behave
   differently.
2. Does not repeat NR-020's own external-literature-vs-Eq.32 comparison —
   this file is about testing H1' as a general historical pattern, not
   about re-scoring Eq.32 itself.
3. Does not resolve which of `dof_ratio` or `ansatz_size` is the "real"
   covariate — the blind-coding check suggests they may be
   double-counting the same underlying construct (search-space size),
   not two genuinely separable dimensions.

## Artifacts

- `scratchpad/h1_prime_dataset.py` — the 11-case coded dataset
  (session-local, not committed; reproducible from this file's own
  citations).
- `scratchpad/h1_prime_regression.py` — the regression + cross-tab.
- Blind-coding transcript: this session's Agent dispatch (not separately
  saved to disk; summarized in full above).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
