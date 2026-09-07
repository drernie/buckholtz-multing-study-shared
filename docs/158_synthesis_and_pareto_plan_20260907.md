# docs/158 — Synthesis of all research to date, comparison with our own code, and a Pareto plan toward peer review

**Date:** 2026-09-07 (evening, after four same-day retractions)
**Status:** DRAFT · NOT COMMITTED · L0 = descriptive/planning (not a new hypothesis;
the routing hook fired on the word "hypothesis" inside quoted external text — per
`meta-loop.md` § CLASSIFY that is quotation, not assertion)
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` · `NO_AUTHOR_ERROR`
**Inputs:** `CURRENT_EVIDENCE_STATE.md` §1-7.6, `docs/145`, `docs/147`, `docs/153`,
`docs/156`, `FINDING_P215_P216_P217_RETRACTION_after_step8a.md`, two external
re-readings supplied by the user today (treated as data; every load-bearing claim
in them re-verified below or marked `[UNKNOWN]`), TJB's `multing_core.py`.

---

## 0. Scorecard — the two external re-readings against what is actually verified

| their claim | verified status | note |
|---|---|---|
| Sec. 2.3 `ä/a → H(z)` integration is kinematically inconsistent | **algebra CORRECT, alarm RESOLVED in v82's favour** `[VERIFIED-code]` | `multing_core.py:150-158` documents its integrand as `−Ḣ`, not `ä/a`; with that, `d(H²)/dz = 2HH'` exactly. Only the name misleads. They accept this in their second pass. |
| `H → ṁ → F_acc → H` must be a self-consistent ODE; unknown which `H` is used | **RESOLVED: it is NOT self-consistent** `[VERIFIED-code]` | `m_dot(z) = 1.1 · Hlcdm_si(z) · M_of(z)` — Planck ΛCDM `H`, not MULTING's own. See §3 — and ΛCDM enters through **three more** channels. |
| DESI-DR1 CC (arXiv:2608.13178, 13 Aug) is a post-freeze test; archive 8 Aug, preprint 14 Aug | **dates WRONG, conclusion WEAKENED** `[VERIFIED-api]` | Archive `updated` **11 Aug**; Zenodo preprint **19 Aug**. +2 d vs code, −6 d vs posting. Their refined label — *"frozen-parameter out-of-sample against a post-freeze derived observable"* — acceptable **only with the 2-day caveat stated**. |
| `k_ICM` defined for nodes; `k_universal` undefined | **agrees** with our retraction | v82:207, v82:1028, v82:1461-1463 |
| "No Lagrangian" is too broad; real gap is field/action completion for the `1/s³`, `1/s⁴` channels | **correct refinement of Q006** | Already in repo as `P203`/`P204` (Racine–Flanagan: mass dipole `l=1` vanishes for any GR-vacuum theory). `U(s) = −C₀/s + C₁/2s² − C₂/3s³` trivially exists for frozen coefficients. |
| Near-cancellation of `F^(1)`/`F^(2)`, condition number ~200 | **matches v82's own admission** (1514, 1721); **our joint propagation NEVER done** | `P196`/`P197` tested concentration only, and structurally ruled it out. A joint Monte Carlo through `multing_core` is a real gap. |
| `∂(ä/a)/∂k = 2H·∂H/∂k − ∂(−Ḣ)/∂k` | **correct**, and it is exactly the term our ICM branch omitted | |
| AIC ≈ +1.4, BIC ≈ +2.9 vs ΛCDM | `[UNKNOWN]` — not recomputed | Trivial; low priority; v82 itself argues parameter-count penalties mis-measure its adaptivity. |
| P215: `β_d ≲ 2.2–3.0×10⁻⁵`, 5.2–5.3 orders | **STALE — retracted before their text was written** | Factor of 2; zero-dof control; conclusion inverted (v6:652-675). Disregard. |

---

## 1. What this project has actually established (survives every check to date)

| # | result | where | status |
|---|---|---|---|
| 1 | `F_oP` bilinear structure; **alternating-sign rule derived as a theorem**, not postulated | `docs/125`, `P1` | `[VERIFIED]` |
| 2 | Isotropic-average `k`-sector **= 0 exactly** at force level and S–S background level, any `q(a)` | double-layer theorem | `[VERIFIED]`, ~1e-16 |
| 3 | Eq.32 numerical match **0.0135%** (PDG 2024) | `CONSILIENCE_eq32.md` | match `[VERIFIED]`; mechanism hunt **exhausted, 5 niches**; Belle II m_τ gives **1.84σ tension** — ambiguous |
| 4 | Bottleneck 3 **dissolved**: `P133`'s rank-2 = `P52`'s field-normalization redundancy; rank 2 is complete | `P206`, `P52` | Step 8a ×2, both CONFIRMED-REAL |
| 5 | Fisher forecast: high-z `H(z)` shrinks the `(β₁,β₂)` ellipse 73/46/14 % at 1/3/10 % precision; z∈{12,14,16} up to 5.4× better | `P191`–`P193` | skeptic-caught bugs fixed before trust |
| 6 | **`H² < 0` at z ≈ 16.96** for TJB's own fitted `(β₁,β₂)` — model undefined beyond | `P192` | grid-converged, CONFIRMED-REAL |
| 7 | **Table A1 is AI output**, not a MULTING calculation — TJB's own caption | `docs/145` Part 8 | decisive; produced the 4 provenance gates |
| 8 | CC full covariance (Moresco): **+6.80 % shift**, inside the 8.91 % budget | 2026-09-03 | `[VERIFIED]` |
| 9 | Cen–Bahcall–Gramann 1994 Fig. 3 digitized to **0.057 %** vs its own Table 1 | sent to TJB 09-03 | `[VERIFIED]` |
| 10 | Girardi `R_vir` vs `ρ_crit` radius: **1.47× residual unexplained**; concentration **structurally ruled out** (`ratio_2b` cancels `R500`) | `P196`, `P197` | open |
| 11 | `β₁` per-**node** / `β₂` per-**pair** universality asymmetry | `P216` §5 (only survivor) | `[VERIFIED-source]` |
| 12 | v82 **assigns binary-pulsar timing to GR** and declines a GR analog | v82:1453, 1461-1463 | `[VERIFIED-source]` — external compact-object bounds test an extension v82 does not claim |
| 13 | Relativistic Fermi-gas physics of `P215`, incl. Jensen proof that uniform density is conservative | retraction §1.7 | independently confirmed |
| 14 | **Methodology:** 4 findings → 4 falsifications in one day, one common root cause; 9/11 `docs/146` failure categories caught by context-blind review | today; `docs/146` | the project's most robust product |

## 2. What is dead, retracted, or closed

`P189`, `P189b`, `P158-ADDENDUM`, `NR-020`, `NR-021`, `P214`, **`P215`, `P216`, `P217`**;
ICM branch `REFUSE(no_falsifiable_predicate_yet)` (and now flagged: it computed `∂(−Ḣ)/∂k`, not `∂(ä/a)/∂k`);
Eq.32 mechanism hunt (5 niches); bottleneck 4 (5 mechanism classes excluded); round-2 strategic arbiter.

## 3. Our code vs TJB's code — the comparison the user asked for

**`src/` (39 files, 995 tests, mypy 0) is v6-era reconstruction:** `two_charge_completion`,
`two_field_action_closure`, `cluster_data_pipeline`, `pearson_fit`, `provenance_audit`, …
**It contains no `H(z)` pipeline and no ΛCDM `E(z)`** `[VERIFIED-grep: 0 hits for Efun/E_lcdm/Hlcdm]`.

**The only `H(z)` pipeline in the project is TJB's own `multing_core.py`** (local, gitignored,
Zenodo 21204955), which `experiments/` import as-is (`_v82_shared_physics.py`, `P176`–`P193`,
`multing_fit_rerun.py`, ICM `stage1`).

**New today `[VERIFIED-code]`: ΛCDM enters MULTING's force through FOUR channels, and our
repo records only one.**

| channel | line | uses |
|---|---|---|
| `T_keV_of(z)` | 79 | `Efun(z)^(2/3)` |
| `Mgas_of(z)` | 84 | `Efun(z)/Efun(z_piv)` |
| `rho_crit(z) → R_of(z)` | 94-101 | `Efun(z)²` — **the one v82 admits** ("most significant residual circularity") and the one `P196` studied |
| **`m_dot(z) → F_accretion`** | **~140** | **`Hlcdm_si(z) = H0_planck · Efun(z)`** — not recorded anywhere in our 120 files mentioning circularity `[VERIFIED-grep, strict]` |

So the accretion loop is **not** a self-consistent ODE; it is an external ΛCDM input. Every
v82-pinned number we hold — `(β₁,β₂) = 1.4335e10 / 7.8067e17`, `P190`–`P193`, `P192`'s
z≈16.96 — inherits all four channels. That is not a defect in our code; it is a provenance
fact that must be stated wherever those numbers are quoted.

## 4. What we are missing — honest list

| # | gap | cost | why it matters |
|---|---|---|---|
| G1 | The **four-channel ΛCDM dependence** is unrecorded (only `r(z)` is) | hours | every v82 number's provenance is understated |
| G2 | **Factor-of-2** `ℓ_d = 2β_d(u_A+u_P)` vs v6 Eq. (15) — open since 2026-08-11 (`P7:143-150`), now in 2 files | hours | live, propagating arithmetic error |
| G3 | **Joint uncertainty propagation** through the `F^(1)`/`F^(2)` near-cancellation | 2 days | v82's own admitted fragility; `P196`/`P197` did one nuisance only |
| G4 | **DESI-DR1 CC out-of-sample scoring**, frozen params, full covariance | 2-3 days | first genuinely new empirical information about v82 available to us |
| G5 | AVB benchmark **underpowered**: N=16, 0 discordant pairs, p=1.0 *by construction*; treatment 12/13 vs baseline 13/13 — **did not favour treatment** | 1 week to N≥40 | the methodology paper's quantitative leg |
| G6 | Process: **Step -3 pre-work check on our own directory** never enforced (caused `P215`) | rule | `FINDING_P7` sat in the same folder |
| G7 | Process: greps on the **glued** v6 extraction while the clean one's header says PREFERRED | rule | caused `P217` §3 |
| G8 | Process: **self-limiting sections read last** — v82:1028, 1719, `multing_core:150` all in "where this breaks" prose | rule | all three killing lines today |
| G9 | Pair → population coarse-graining (bottleneck 1) | months, N-body | known; arbiter said stop |
| G10 | Field/action completion for `1/s³`, `1/s⁴` (Q006) | open-ended | known; `P203`/`P204` bound it |

---

## 5. Pareto plan toward peer review

### 5.0 The fork that decides everything: *what* gets reviewed

This project's charter (`CLAUDE.md`) is an **epistemic audit / reconstruction**, explicitly
*"NOT a validation or refutation of MULTING itself"*, with standing rules against any
evaluative-authority stance toward Dr. Buckholtz and against sending anything without an
explicit go-ahead. That rules out one path and leaves two:

| path | what | feasible? | verdict |
|---|---|---|---|
| **A — methodology paper (ours)** | *Context-blind adversarial falsification in AI-assisted research: a longitudinal case study.* Today's 4-for-4 is the centrepiece; `P214` the prequel; `docs/146` taxonomy (11 categories, real incidents); the 4 provenance gates from the Table A1 incident; AVB as pilot. Evaluates **our process**, not TJB's physics. | **HIGH** — nothing depends on TJB or on MULTING being right | **PRIMARY** |
| **B — technical results into TJB's own revision** | He wrote 09-07 he is revising. Items 5, 6, 8, 9, 10 in §1, plus G1/G3/G4 outcomes, offered as *shared results* under the correspondence rules (formal address, prose, no questions, no audit words). Authorship is his call. | HIGH, but not ours to schedule | **SECONDARY** |
| C — physics paper on MULTING under our name | — | conflicts with charter and with `feedback_no_evaluative_authority_words` | **NOT RECOMMENDED** |

### 5.1 The 20 % (ranked by information gain ÷ cost)

| # | action | days | output | gate |
|---|---|---|---|---|
| **1** | **Hygiene at source**: record the 4-channel ΛCDM finding (G1); fix the factor of 2 in `FINDING_unsuppressed_observable_periastron.md` and close `P7:143-150` (G2); add the three process rules (G6-G8) to `CLAUDE.md` | **1** | every downstream number honest | ruff/pytest |
| **2** | **DESI-DR1 CC out-of-sample test** (G4): `(β₁,β₂,H₀)` frozen at Table II values, `H_MULTING(z)` on the DESI grid, `χ² = ΔHᵀ C⁻¹ ΔH` with **their** covariance, ΛCDM at Planck values alongside. Label exactly: *frozen-parameter OOS, +2-day margin vs code archive, same CC method, different galaxy sample.* No refit. | **2-3** | one number + one figure, shareable | Step 8a on the script **before** any number is quoted; result to TJB only on explicit go-ahead |
| **3** | **Joint Monte Carlo propagation** (G3): sample `(T₀, M_gas pivot, R, f_coh)` jointly through `multing_core`, propagate to `H(z)` and to the `F^(1)`/`F^(2)` residual | **2** | fragility quantified, not asserted | Step 8a |
| **4** | **Methodology paper v0** (Path A): sections = problem · protocol (frozen `protocol_v1.0/`) · taxonomy · four case studies (`P214`, `P215`, `P216`, `P217`) with root cause · AVB pilot **reported as inconclusive** · limitations. arXiv cs.AI / cs.SE first. | **3-5** | draft | **Submission Gate** (integrity.md): context-blind skeptic on the *draft*; ≥9 `[VERIFIED]` checklist items; text↔figure consistency; **24 h cooling-off after "READY"** |
| 5 | AVB **N → 40** (G5), pre-registered McNemar, only if Path A targets a journal rather than arXiv-first | 5-7 | quantitative leg | Oracle Adequacy Gate on the evaluator |

**Total to an arXiv-ready methodology draft + a DESI result in hand: ~2 weeks.**

### 5.2 The 80 % to skip (explicitly)

- More bottleneck-1 analytics — `docs/156` proved the literal step unbuildable; the arbiter said **stop**, not iterate.
- Q001 (4/3 coefficient) — exhausted across 5 niches; `CLAUDE.md` forbids re-running them.
- New `β` fits or `β`-from-first-principles — BETA-1 HOLD, TJB-blocked.
- Compact-object / EP bounds on `β` — v82 cedes the regime to GR (1461-1463) and `k` is undefined there; three attempts died today.
- AIC/BIC beyond one sanity line — v82's own adaptivity argument makes it non-decisive.
- Pair → population derivation — needs N-body, months, and is bottleneck 1 under another name.

### 5.3 Standing constraints that bind every item above

- **Nothing to TJB without a fresh, explicit, per-instance go-ahead.** "Act autonomously" never covers sending.
- Formal address, prose, share results, ask nothing, no audit/verify/review vocabulary.
- `NO_AUTHOR_ERROR` on every artifact. Path A must be written so that MULTING is a *case*, never a *target*.
- Every v82-pinned number carries the four-channel provenance note (§3).
- If a v83 appears: new artifact, Gate 1, re-diff before any prior result is quoted.

### 5.4 What "peer-reviewable" concretely requires, per gate

| requirement | Path A status now | to do |
|---|---|---|
| Falsifiable central claim | *"context-blind adversarial review catches defect classes that same-context review misses"* | state as descriptive + one pre-registered predictive test (AVB N≥40) |
| Positive control | today's 4/4 + `P214` — real defects, independently re-verified | write up with line-anchored evidence |
| Negative control | AVB clean tasks (3 of 3 had real problems — itself a finding) | report honestly |
| Independent reproduction | **none above "same model, isolated context"** (`falsification-ladder.md` strength ladder) | cheapest upgrade: a different model as Run-3 evaluator; an outside reader on the draft |
| Statistics | N=16, p=1.0 by construction | N≥40 or reframe as qualitative case study |
| Provenance | full — every citation line-anchored, every retraction in place | keep |

---

## 6. One-paragraph verdict

The project's durable product is not a verdict on MULTING — its charter forbids one and
its evidence does not support one either way. It is (i) a small set of hard technical
results about the published construction (`H² < 0` at z≈17; the four ΛCDM input channels;
the CC covariance shift; the field-normalization redundancy; the alternating-sign theorem),
each with line-anchored provenance, and (ii) a **documented, reproducible failure of the
naïve workflow and success of the adversarial one**, culminating in four same-day
retractions with a single verified root cause. Path A publishes (ii) with (i) as its
material. Path B returns (i) to the author who is revising. Everything else is the 80 %.
