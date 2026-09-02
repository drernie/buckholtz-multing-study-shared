# Consilience — does Eq.32 reflect a genuine physical relation?

**Date:** 2026-09-02
**Skill:** `/consilience`, requested by user, applied to synthesize 3
existing/newly-checked independent lines of evidence about TJB's Eq.32:
(4/3)(m_τ/m_e)^12 = α_EM/α_G, 0.0135% deviation.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (epistemic-status synthesis, not a new
physical claim about MULTING)

---

## [ИЗ ПРОЕКТА]

- `null_results/INDEX.md` NR-019 (2026-08-17): internal mechanism-hunt,
  3 group-theoretic derivation attempts, all REJECT.
- `null_results/20260902-nr020...md` (today): external literature
  numerology-pattern check, timing-axis hypothesis FALSIFIED by skeptic
  (Balmer counter-example), DoF-based fallback applied inline.
- `experiments/20260810-eq32-look-elsewhere/FINDING_eq32_look_elsewhere.md`
  (2026-08-10): computational null-model search, p≈0.157, AND (found only
  while writing this synthesis — NR-020 missed it) a real, named,
  falsifiable prediction (m_τ=1776.840 MeV if exact) — see Correction in
  NR-020 and Path 5 below.

No prior consilience-style synthesis of these three exists — genuinely new
integration, not a repeat.

## Step 1 — EstimandOps L0

**Question type:** Descriptive/epistemic — not causal, not classic
predictive-ML. We are classifying the evidential status of one already-
fixed, already-verified numerical fact, not estimating a population
parameter or an intervention effect.

**Estimand statement:** *"We assess, via three independently-methodled
lines of evidence already produced (or checkable) by this project, whether
Eq.32's numerical match reflects genuine structure versus an artifact of
search space and researcher degrees of freedom."*

**What this does NOT mean:**
1. Does not prove MULTING/IDM wrong as a whole (`NO_AUTHOR_ERROR`) — Eq.32
   is one isolated numerical claim within a much larger framework.
2. Does not make the 0.0135% match itself false — that arithmetic fact
   remains `[VERIFIED]` and unchanged by any path below.
3. Does not settle the question with finality — Path 5's tension is mild
   (1.84σ), not a 3σ/5σ physics-standard rejection; Belle II Run 2 (started
   2024) may sharpen this further in either direction.

## Steps 2-3 — Five paths, honestly mapped (2 of 5 are structurally N/A)

Eq.32 is a **static algebraic identity** between measured constants, not a
causal process or a population-level empirical claim — two of the skill's
five canonical paths do not apply to this KIND of claim, and are marked
N/A rather than forced:

| Путь | Applicable? | Why / why not |
|---|---|---|
| 🧠 Теоретический | ✅ | NR-019 — formal derivation attempts exist |
| 📊 Наблюдательный | ❌ N/A | No natural population/cohort to observe independently for a fixed constant identity |
| 🔬 Механистический | ❌ N/A | No intermediate causal step to block-and-test; a static identity has no process |
| 💻 Вычислительный | ✅ | `eq32-look-elsewhere` — real computational null-model search |
| 🎯 Предсказательный | ✅ | Belle II check — corrected during this synthesis, see below |

### Путь 1 — Теоретический (NR-019)

**A:** Does Eq.32's coefficient (4/3) and exponent (12) follow from a
known symmetry/invariant, the way a real physical constant relation should?
**B:** Minimum (used): existing Lie-group literature search. Good/Ideal
(not attempted): a systematic operator-basis classification.
**C:** AI-assisted literature/algebra search across 3 candidate groups.
**D:** Key test: does ANY invariant of S³, F₄/G₂/J₃(O), or the SM gauge
group give {4/3, 12} together, non-post-hoc, with an independent
prediction? **E:** `null_results/20260817-*`, `docs/145` §24.
**F:** Falsified if all 3 attempts are shown to be post-hoc relabeling
with zero independent prediction — **this already happened.**

**Result: NULL.** 3/3 attempts REJECT — post-hoc relabeling in every
case, no independent prediction from any of them. This is an informative
null (serious attempt at Strong-tier evidence, not "never tried").

### Путь 4 — Вычислительный (eq32-look-elsewhere, 2026-08-10)

**A:** Is Eq.32's precision (0.0135%) surprising given how many similarly-
simple expressions could have matched some target by chance? **B:**
Minimum/used: 170,352 candidate expressions (91 prefactors × 78 mass
pairs × 24 exponents), declared before scanning. **C:** Vectorized
enumeration + a 4000-draw randomized-target null model. **D:** Key test:
look-elsewhere p-value — fraction of random targets in the same space
matched at least as well. **E:** `experiments/20260810-eq32-look-
elsewhere/`, folded into `paper/main.tex`. **F:** Falsified as
"extraordinary" if p is not small (e.g. p > 0.05).

**Result: NULL (for "extraordinary").** p ≈ 0.157 — about 1 arbitrary
target in 6 does at least as well within the declared space. The source
file's own verdict: *"Eq.32's numerical agreement is extraordinary:
[FALSIFIED as stated] — it is ordinary for a target of this magnitude
searched over this space."* Caveat (stated in the source, carried
forward here): the search-space bounds (prefactor ≤12, exponent ≤24, 13
particles) are declared but not principled — a wider grammar would lower
p further, a narrower one would raise it.

### Путь 5 — Предсказательный (CORRECTED mid-synthesis)

**A:** Has Eq.32 made a specific, falsifiable, out-of-sample prediction —
and if so, does it hold? **B:** Minimum/used: the prediction already on
record (m_τ = 1776.840 MeV if Eq.32 is exact), checked against Belle II's
2023 measurement. **C:** N/A (arithmetic check, not AI-assisted). **D:**
Key test: |predicted − measured| in units of the measurement's own
uncertainty. **E:** this file's own arithmetic, script at
`scratchpad/eq32_belle2_check.py` (session-local, not committed —
reproducible from the numbers below). **F:** Falsified (as a clean
confirmation) if tension exceeds ~2σ; falsified (as a clean rejection) if
tension exceeds ~5σ.

**NR-020 (written earlier today) claimed this path was empty — WRONG, see
correction appended to that file.** Computed here for the first time in
this project:

```
Eq.32 prediction (exact):        m_τ = 1776.840 MeV
Belle II 2023 (independent):     m_τ = 1777.09 ± 0.08 (stat) ± 0.11 (syst) MeV
                                  combined uncertainty = 0.136 MeV
                                  tension = (1777.09 - 1776.840) / 0.136 = 1.84σ

PDG world average (NOT independent — likely close to/including the
value Eq.32 was originally anchored against):
                                  m_τ = 1776.86 ± 0.12 MeV
                                  tension = 0.17σ  <- circularity risk, not a real test
```

**Result: AMBIGUOUS, mildly unfavorable.** 1.84σ is neither a clean pass
nor a rejection by physics convention (3σ = "evidence," 5σ = "discovery/
exclusion"). But it is NOT a confirmation either — a genuine out-of-sample
check landed closer to "mild tension" than to "spot on." The PDG-average
comparison (0.17σ) is not usable as an independent test — it is close to
circular, since Eq.32's own anchor value likely draws on the same world
average.

## Step 4 — Independence Matrix

|  | Путь 1 (NR-019) | Путь 4 (look-elsewhere) | Путь 5 (Belle II) |
|---|---|---|---|
| **Путь 1** | — | ✅ independent | ⚠️ minor (NR-020's baseline cited NR-019's "no mechanism" as context; the Belle II arithmetic itself is fully independent) |
| **Путь 4** | ✅ | — | ✅ independent |
| **Путь 5** | ⚠️ | ✅ | — |

Three genuinely different methods: symbolic/group-theoretic derivation
(Путь 1), combinatorial statistical null-modeling (Путь 4), and direct
comparison against real experimental particle-physics data (Путь 5). The
one flagged overlap is conceptual (one file mentioned another's
conclusion as background), not methodological — no discount applied.

## Step 5 — Consilience Score

Two of five canonical paths are structurally N/A for this kind of claim
(a static constant identity, not a causal/biological hypothesis) — scoring
against a forced 5-path denominator would unfairly penalize a claim in a
domain where those paths don't exist to run. Scored against the **3
applicable paths** (max 3×2.5=7.5), rescaled to /10:

| Путь | Статус | Оценка | Независим? | Ключевой тест | Артефакт |
|---|---|---|---|---|---|
| Теоретический | NULL (attempted, failed) | 0 | ✅ | 3 group-theory derivations | NR-019 |
| Наблюдательный | N/A | — | — | — | — |
| Механистический | N/A | — | — | — | — |
| Вычислительный | NULL (for "extraordinary") | 0 | ✅ | look-elsewhere p≈0.157 | `eq32-look-elsewhere` |
| Предсказательный | AMBIGUOUS (mild tension) | 0.5 | ⚠️(minor) | Belle II 1.84σ | this file |
| **SCORE (of applicable 7.5 max)** | | **0.5 / 7.5 → 0.7/10** | | | |

## Synthesis — do the paths converge?

**Yes — and they converge on non-support, not on neutrality or refutation.**
Three methodologically independent approaches (formal derivation, a
declared-space statistical null model, and a real experimental check)
each, on their own terms, failed to find anything that would elevate
Eq.32 above "an unremarkable coincidence within a reasonably-declared
search space, whose one real prediction shows mild tension with the best
available independent data." No single path is decisive alone (each has
real, stated caveats — search-space arbitrariness for Path 4, only-3-
groups-tried for Path 1, one data point at 1.84σ for Path 5) — but their
**directional agreement**, reached by unrelated methods with unrelated
failure modes, is real consilience, and is a stronger statement than any
one path's own caveated verdict.

**What this does NOT establish** (repeating Step 1's estimand
boundaries, now with the evidence in hand):
1. Does not refute the 0.0135% arithmetic fact — it remains true and
   `[VERIFIED]`.
2. Does not prove Eq.32 is coincidental with certainty — 1.84σ is a real
   but modest tension, and Belle II Run 2 (started Feb 2024, larger
   dataset) could move this number in either direction.
3. Does not touch MULTING/IDM's broader claims (`NO_AUTHOR_ERROR`) — this
   is one isolated numerical relation, evaluated on its own.
4. Does not close NR-020's own still-open item (formalizing and
   independently attacking the DoF-based H1' criterion) — if anything,
   today's Belle II finding makes that formalization slightly more
   urgent, since the prediction-structure argument now has one concrete,
   checked (if ambiguous) data point instead of none.

## Recommended next step (per skill's interpretation table, adapted)

Score 0.7/10 nominally falls in "0-2: bare hypothesis, start with Path 1
or 3" — but Path 1 has already been seriously attempted (3×) and Path 3
is structurally inapplicable, so that generic recommendation doesn't
transfer cleanly. The one path with real remaining headroom is **Path 5**:
Belle II Run 2's improved tau-mass measurement (data-taking began
2024-02-20, per DESY's own announcement) will either sharpen the 1.84σ
tension toward significance or relax it toward agreement — this is a
concrete, dated, externally-driven event to watch, not something this
project can accelerate.

## Pointers

- `null_results/20260902-nr020-eq32-numerology-negative-space-mining.md`
  — correction appended same session.
- `experiments/20260810-eq32-look-elsewhere/FINDING_eq32_look_elsewhere.md`
  — source of the look-elsewhere p and the Belle-II prediction.
- `null_results/INDEX.md` NR-019 — mechanism-hunt consolidation.
