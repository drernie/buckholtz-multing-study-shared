# claim.md — local expansion vs intracluster thermal energy

**Experiment id:** `20260907-icm-expansion-correlation`
**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR`
**Origin:** Ernest Prabhakar's 2026-09-06 follow-up (thread
`1a0738a363392c69`, message `1a073cd3905dd1eb`), naming this as *"the only
place I see you having an asymmetric advantage."*

**VERDICT OF THIS DOCUMENT: `REFUSE(no_falsifiable_predicate_yet)` — the
Zero-Signal Gate does not pass, and the reason is structural, not
cosmetic. Do not proceed to code. See §3 and §8.**

---

## 1. Step -3 — Novelty check (run FIRST, per FL; it changed the task)

`[VERIFIED-tool]` `grep` over `null_results/INDEX.md`, `parked/INDEX.md`,
`pearl_registry/INDEX.md` and all `FINDING_*.md`.

### 1.1 An adjacent formulation was already designed, run, and KILLED

| item | date | content |
|---|---|---|
| pearl row 83 `[DIAMOND]` | 2026-06-30 | *"TJB's mechanism (IGM thermal energy as SOURCE) occupies EXACTLY the gap where Verlinde fails"* |
| pearl row 84 `[GOLD]` | 2026-06-30 | *"Cheapest differentiating test between H1(TJB) and H0(ΛCDM): archival regression `(M_lensing − M_hydrostatic) ~ E_ICM/c²`… H1 passes if `r>0.4 p<0.05`; H1 dies if `r<0.2`."* |
| **NR-010** | **2026-07-01** | **KILLED.** `r(delta_M, M_gas×T_x) = 0.021, p = 0.883`, CCCP `N=50` (Mahdavi+2013). Pre-registered threshold, `~91%` power to detect `r=0.4`. Classified `signature_absent`. |
| NR-011 / NR-012 / NR-014 | Jul 2026 | mass-split, morphology-split, AGN-feedback mediation — all `mechanism_killed` |
| NR-015 | 2026-07-18 | surviving partial correlation traced to `T_X`; index's own correction records that **none of the four controlled for `T_X`** |

### 1.2 …but NR-010 does **not** transfer, and says so itself

Two independent reasons, both in NR-010's own text:

1. **Different dependent variable.** NR-010 regresses **mass bias**
   (`delta_M = M_WL − M_HE`). Ernest's proposal is about **local
   expansion**. These are different observables, not two names for one.
2. **Different source scale.** NR-010's own *Root cause* section:
   *"H1a tests cluster-interior ICM, which is a **narrower quantity** than
   TJB's actual mechanism (cosmic-web IGM/WHIM in filaments and nodes).
   Cluster ICM sits inside the virial radius and is dominated by
   relaxation state, not the filament-scale thermal reservoir the
   mechanism proposes."*

NR-010's *Forbidden use* section is explicit: *"Do NOT cite NR-010 as
evidence against the broad TJB mechanism (H1)."* This document obeys that.

### 1.3 Correction to a claim made in-session on 2026-09-07

Earlier today I told the user, verbatim: **«Эту величину не посчитал
никто. Ни TJB, ни мы.»** That was **wrong on the second half**, and the
error has a traceable cause worth recording rather than deleting.

- What `FINDING_E21` actually says (2026-09-06): *"**v82** does NOT
  currently compute or claim any quantitative version of this
  correlation."* That is a statement about **v82**, not about this
  project.
- `E21` goes on, in the same section: *"Actually running such a test …
  is a **substantial, separate undertaking, out of this finding's own
  scope** — named here, not attempted,"* and registers it as a pearl
  candidate.

So the correct statement is: **v82 does not compute it; this project has
not run *this* observable either — but it did run an adjacent one and
killed it, and it had already named this candidate the day before.** The
framing «не на старой карте вообще / появилась час назад» was an
overstatement.

**Cause:** I searched on the *letter's wording* instead of on the
*structure of what was computed* — the exact failure mode this project's
own memory records as
`method_index_not_citation_graph`: *«Не искать по формулировке claim'а —
искать по структуре.»* Second occurrence; the first was `P206`
(bottleneck 3 rediscovered 8 days later).

---

## 2. Step -2 — EstimandOps L0 classification

**`causal`.** The proposition is not "are these two quantities
associated" (descriptive) nor "can thermal energy forecast expansion"
(predictive) — MULTING asserts thermal energy *sources* a repulsive term
that *drives* local expansion. A merely associational result would not
support the claim, and standard structure formation supplies a competing
causal path for the same association (§4).

Consequence, per `estimand-ops.md`: a DAG and the four identifiability
checks are **required** before any result counts. Not attempted here,
because the gate below fails first.

---

## 3. Step -5 — Zero-Signal Gate

| field | content | pass? |
|---|---|---|
| **Entity** | Cluster/node-scale thermal reservoir (`E_th`, via `M_gas × T_X` or the node-scale IGM/WHIM analogue) and the expansion rate in its neighbourhood | ✅ |
| **Falsifiable predicate** | *MULTING predicts `∂H_local/∂E_th > 0` at strength X* | ❌ **CANNOT BE FILLED** |
| **Measurable outcome** | correlation coefficient + sign against a stated threshold | ⚠️ conditional on the predicate and on §5 |

**The predicate cannot be filled from the corpus.** `E21`'s twelve-group
enumeration of everything v82's own archive computes found no numbered
result of the form *"local `H` variation should correlate with nearby
cluster thermal energy at strength X."* The mechanism is present in the
construction; the quantitative consequence is not derived anywhere — not
by TJB, not here.

**Therefore: `REFUSE(no_falsifiable_predicate_yet)`.** Per FL's own hard
rule, issuing REFUSE is the correct output; structuring an unfalsifiable
input is not.

---

## 4. Step 4a preview — the FLOOR, which is the real crux

Even if the predicate were derived, the test's discriminating power turns
on a question that must be answered **before** any run:

> What correlation does a null model containing **no MULTING at all**
> already produce between `E_th` and local expansion?

**`[CORRECTED 2026-09-07, external review]` — the first draft of this
section asserted a single "unavoidable path" and implied its sign. That
was stronger than anything shown. Original wording kept here so the
correction is visible: *"Standard structure formation supplies an
unavoidable path: `E_th ↑ ⇐ M ↑ ⇒ denser environment ⇒ stronger infall
⇒ local expansion ↓`."*

Correct status: that chain is **one plausible competing hypothesis**, not
an established floor. At least five distinct paths connect the two sides,
and they do not obviously share a sign:**

```
M → T_X                       (mass–temperature scaling)
M → v_pec                     (massive haloes sit in stronger flows)
environment → T_X, v_pec      (density field drives both)
merger state → T_X, v_pec     (disturbed systems inflate both)
selection + estimator effects  (catalog cuts, proxy construction)
```

**Therefore: `sign(astrophysical floor) = UNKNOWN`.** It has to be
*derived or measured*, not assumed — and doing so is its own task, not a
paragraph in this file.

Two possibilities, with opposite consequences:

| case | consequence |
|---|---|
| Floor correlation is **negative**, MULTING predicts **positive** | genuinely discriminating — the strongest available version of this test, and the reason it is worth keeping alive |
| Floor correlation has the **same sign** as MULTING's | `CRITERION_INVALID` — a criterion a mechanism-free construction already passes |

`NR-010` is a warning here, not a proof: in its (different) observable
the direction came out **reversed** from the H1a prediction — *"hot
clusters show LESS bias."* Sign intuition in this family has already
failed once.

**This floor must be computed before the observed value, not after.**

---

## 5. Feasibility — checked, not assumed

`[VERIFIED-tool]` inventory of `data/`:

| side of the regression | status |
|---|---|
| **Independent variable** (`E_th`) | ✅ present — `data/mcxc.csv`, `data/chexmate_combined.csv`, `data/chexmate_real_TX.csv`, `data/clusters_clean.csv` |
| **Dependent variable** (local expansion) | ❌ **absent — no peculiar-velocity / Cosmicflows / local-`H` dataset anywhere in the repo** |

Ernest's *"testable against existing X-ray cluster catalogs without
waiting for a new survey"* is **half right**: the X-ray half is in hand;
the local-expansion half is neither in hand nor a catalog column. It
requires a peculiar-velocity field (Cosmicflows-class), which is a
separate acquisition, and `E21` already judged this *"a substantial,
separate undertaking."*

**Additional hazard, named now:** v82 flags `H0,anchor` derived via
peculiar velocities as **Class III circular** (Sec. IV.M) — and this
project's own `provenance_audit` tool independently re-flagged it. A test
whose dependent variable is built from peculiar velocities risks
importing that same circularity. Any design must show it does not.

---

## 6. The structural finding: items 1 and 2 are one item

The predicate of §3 is *`∂H_local/∂E_th`*, i.e. the response of expansion
to the **`k` charge**. `P213` established that `k`'s two admissible
readings differ by a factor **`6.8×10⁸`** in `|Δψ|`:

| reading of `k` | consequence for this test |
|---|---|
| **broad** (binding, rotational, degeneracy) | `E_th` is the wrong independent variable — the reservoir is far larger than the thermal part, and the regressor is mis-specified |
| **narrow** (thermal specifically) | `E_th` is the right regressor, and the test is well posed |

So **this experiment is gated on the same single question that gates
MICROSCOPE**: `MODEL_SPEC_AUDIT` §5's *"Every unresolved row above
terminates at the same place: what is `k`?"* — the question already
drafted for the author and **held**
(`P3_k_definition_question_DRAFT_HELD.md`).

**`[CORRECTED 2026-09-07, external review]`** The first draft said the
two items *"are the same item"* — too strong, and kept here rather than
deleted. Precise statement:

> They are **two distinct observational branches sharing one upstream
> bottleneck.**

MICROSCOPE and the local-expansion test still require **different
observable mappings and different data**; what they share is that neither
predicate can be written down until `k` is defined. Fixing `k` unblocks
both, but does not merge them into one experiment.

---

## 7. What this claim does NOT establish

1. **Not that the correlation is absent.** No test was run here. `NR-010`
   is a different observable at a different scale and does not transfer.
2. **Not that Ernest is wrong.** His structural judgement — that this is
   the one mechanism-level, low-`z`, non-fit-shaped claim in the vicinity
   — is *endorsed* by this document. What is corrected is only the
   feasibility half of his sentence.
3. **Not a claim about MULTING** (`NO_AUTHOR_ERROR`). The missing
   predicate is a fact about what v82's archive computes, established by
   `E21`'s own enumeration.
4. **Not that the test is unbuildable.** It is unbuildable *today*, on
   *this* data, without *that* definition.

---

## 8. Decision

**`REFUSE(no_falsifiable_predicate_yet)`. No code. Not promoted to an
active experiment.**

Three unblock conditions, cheapest first — **any one** moves this to a
real Standard-Ladder experiment:

1. **`k`'s reading is fixed** (author's answer, or a theorem that `k` is
   a rigid conserved scalar). Decides whether `E_th` is even the right
   regressor. Already drafted, held.
2. **The predicate is derived independently** — a labelled
   `OUR_RECONSTRUCTION` extension computing `∂H_local/∂E_th` from the
   `F_oP` chain, carrying its own `k`-reading assumption explicitly. This
   is the route that does **not** require TJB, and it is the one worth
   costing.
3. **A local-expansion dataset is identified** whose construction is
   demonstrably independent of the `H0,anchor` peculiar-velocity chain
   (§5's hazard).

**Registered, not shelved:** this goes to `pearl_registry/INDEX.md` per
`E21`'s own already-stated intent, with the floor question of §4 as its
`falsifiable_prediction` and condition 1 above as its
`trigger_condition`.
