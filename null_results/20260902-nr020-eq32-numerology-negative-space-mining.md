# NR-020 — Eq.32 vs. the historical record of physics "numerology": a
# negative-space-mining decisive test (timing-based H1 FALSIFIED; DoF-based
# fallback applied)

**CORRECTION (2026-09-02, same day, found while running `/consilience` to
synthesize this file with NR-019 and the project's own look-elsewhere
result):** Stage 7's claim "Eq.32 has made no subsequent out-of-sample
prediction using its own fixed parameters" is **WRONG**. This project's own
`experiments/20260810-eq32-look-elsewhere/FINDING_eq32_look_elsewhere.md`
(2026-08-10, not cross-referenced when this file was written) already names
one: **m_τ = 1776.840 MeV if Eq.32 is exact.** Checked against Belle II's
2023 measurement (1777.09 ± 0.08 ± 0.11 MeV, arXiv:2305.19116/PhysRevD.108.
032006 — genuinely independent, predates and does not reference Eq.32):
**1.84σ tension** — not a clean confirmation, not a decisive rejection.
Stage 7's applied verdict below is otherwise unaffected (DoF/prediction-
structure still places Eq.32 in the "hasn't cleared the survivor bar"
region — the correction *sharpens* that reading, since a checked, mildly-
tense prediction is weaker for the hypothesis than an as-yet-unmade one,
not stronger) — but "zero predictions" must be read as "one prediction,
checked, ambiguous," not "none exist." Full synthesis with this correction
folded in: `experiments/20260803-bridge/CONSILIENCE_eq32.md`.

**Date:** 2026-09-02
**Skill:** `/negative-space-miner`, requested by user, run in full (Stages
-1 through 8, Attack delegated per Context Asymmetry Rule).
**Distinct from `NR-019`:** NR-019 was an INTERNAL mechanism-hunt (does any
Lie-group/algebra structure DERIVE Eq.32's coefficient/exponent?) —
REJECT, consolidated, 3 attempts. This file is an EXTERNAL literature
question (how have OTHER numerical physics "coincidences" historically
fared, and does that give a testable criterion applicable to Eq.32?) —
a genuinely different angle, not a repeat.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION ·
NO_AUTHOR_ERROR · L0 descriptive (historical/literature question + one
applied diagnostic test, not a new physical claim about MULTING)

---

## Stage -1 — Topic filter

An aggregated meta-literature on "numerology vs. real physics" DOES
already exist (Amir/Lemeshko/Tokieda 2016 base-rate paper; the
"number theory vs. numerology" discourse; Kragh's history-of-physics
writing on Eddington). Per this skill's own rule: this caps the
Novelty ceiling — the historical map below largely confirms/aggregates
what specialists already know, rather than surfacing a hidden structure
nobody has assembled. The value here is in **applying** a decisive
test to Eq.32 specifically, not in discovering new history.

## Stage 0 — Baseline (Eq.32)

1. **Claim:** TJB's Eq.32, (4/3)(m_τ/m_e)^12 = α_EM/α_G, matches to
   0.0135% — presented as a significant finding linking particle-mass
   scales to gravity.
2. **Mechanism:** none proposed by TJB himself — an empirically noticed
   match, no theoretical derivation in the preprint.
3. **Confirming observations:** the precision of the match itself
   (0.0135%), using recognized CODATA-class constants.
4. **Variables the theory treats as essential:** exponent 12 (not
   derived), coefficient 4/3 (not derived), the specific choice of
   m_τ/m_e (not m_μ/m_e or another pair).
5. **What it should predict if real:** [context from this project's own
   prior work, not re-derived here] a look-elsewhere recalibration
   already exists (`docs/145`) — used as background, not repeated.

## Stage 1-2 — External search + Map of Conflicts

Real sources only, evidence-marked. `SOURCE_NOT_FOUND` used nowhere below
— all 5 rows below have a real, checkable source.

| Source | Year(s) | Effect size | Expected | What happened | Method | Failure label |
|---|---|---|---|---|---|---|
| **Titius-Bode law** [VERIFIED-REAL: en.wikipedia.org/wiki/Titius–Bode_law, arXiv:0806.3532] | 1772→1846 | Exact fit, 6-7/7 known bodies incl. Ceres | Physical law of orbital spacing from disk formation | Neptune (1846) didn't fit — failed on first genuinely new test after acceptance | a=0.4+0.3·2ⁿ, tuned post-hoc to already-known distances ("Titius discovered the relation after playing with number sequences") | `methodological` — documented post-hoc curve-fit |
| **Eddington's exact α⁻¹=137** [VERIFIED-REAL: arXiv:1510.04046 (Kragh), sciencedirect S0960077906010149] | 1929-1944 | Exact integer, matched then-measured value | First-principles derivation of a fundamental constant | Rejected by physics community ("complete nonsense," "romantic poetry, not physics"); true value 137.036, not exactly 137 — precision itself failed as measurement improved | Idiosyncratic QM interpretation, single author, target value already known when 137 was adopted | `methodological`/`measurement` |
| **Dirac Large Numbers Hypothesis** [VERIFIED-REAL: en.wikipedia.org/wiki/Dirac_large_numbers_hypothesis, arXiv:1603.06474] | 1937→1970s | ~10⁴⁰ coincidence, EM/gravity force ratio vs. cosmic age | Real link between cosmology and microphysics | Independent isotope-ratio tests disagreed by orders of magnitude (¹³C/¹²C: predicted 4.3, observed 1.1×10⁻²; ⁴⁰K/³⁹K: predicted 14, observed 1.3×10⁻¹⁴) | Coincidence between quantities of different physical origin, no proposed causal bridge | `causal`/`measurement` |
| **Koide formula** [VERIFIED-REAL: arXiv:hep-ph/0508039, en.wikipedia.org/wiki/Talk:Koide_formula, arXiv:2108.05787] | 1982→present (44 yr, open) | (Σm)/(Σ√m)²=2/3 exactly, within precision at every re-measurement | Simple lepton-mass relation | NOT refuted in 44 years — survives every precision refinement of m_τ; mechanism still unagreed, status explicitly "unsolved mystery" | Formula proposed BEFORE τ mass was measured precisely; correctly anticipated it | `unexplained` — the one surviving case |
| **Base-rate calibration** [VERIFIED-REAL: Amir/Lemeshko/Tokieda 2016, arXiv:1603.00299] | 2016 | N/A — meta-analysis | — | Quantifies how often "surprisingly simple" constant matches arise by pure chance in a wide search space — a real null model, not zero | Statistical null-model analysis across physical constants | `methodological` — direct tool for base-rate estimation |

## Stage 3 — Cluster structure

- **Post-hoc curve-fit** (Titius-Bode, Eddington): parameters chosen
  AFTER the target value was known; failed on first out-of-sample test.
- **No proposed causal bridge** (Dirac LNH): coincidence between unrelated
  physical domains, no mechanism offered; failed on independent data.
- **Unexplained-but-surviving** (Koide): low parameter count, made a real
  prediction before the target was known; not refuted, mechanism unknown.

Ruling Theory Trap check: three distinct labels, each explaining a
different sub-cluster — no single "master" candidate forced onto all.

## Stage 4 — Repair Hypothesis H1 (as formulated, before attack)

**H1: post-hoc vs. a priori parameter-fixing timing** predicts survival.
Switching variable: was the formula's specific numerical target already
known to the author before its free parameters (exponent, coefficient,
choice of quantities) were fixed?

Duhem-Quine qualifier, Rescue-unfalsifiability check, and a pre-registered
numeric threshold (a concrete archival yes/no question, not a vague
"sufficient control") were all written explicitly before delegating the
attack — see the full formulation in the skill-invocation transcript.

## Stage 6 — Attack (delegated, context-blind, per Context Asymmetry Rule)

**Verdict: FALSIFIED.** Full skeptic report on file (session transcript);
key findings:

1. **Killing counter-example: the Balmer formula (1885).** Documentedly
   post-hoc — Balmer was handed 4 known hydrogen wavelengths and searched
   for a numerical fit, exactly Titius-Bode-style curve-fitting. It then
   **survived every subsequent out-of-sample test**: predicted further
   lines in the same series, generalized by Rydberg, correctly predicted
   entire NEW spectral series (Lyman, Paschen, Brackett, Pfund) decades
   later, and became the empirical target Bohr's 1913 model was built to
   reproduce. This directly falsifies H1's claimed DIRECTION — a
   documented post-hoc formula that did NOT fail.
2. **Reduces to a generic statistical fact.** "Parameters fixed on
   already-known data generalize worse than independently-fixed
   parameters" is ordinary train/test overfitting, not a physics-specific
   insight — no predictive content beyond Statistics 101.
3. **Self-admitted ad hoc rescue.** H1's own formulation already needed
   an escape hatch for Dirac's LNH ("may need a second dimension") before
   leaving the room — 1 of 4 supporting cases already required rescuing.
4. **Koide's own history is messier than presented** — the formula was
   fit against 3 already-known masses; what "survived" is precision
   *refinement* consistency across 44 years, not a fresh independent
   prediction the way Balmer's was.

**All 3 of H1's own (retroactively identifiable) kill criteria fired.**

## Kill Analysis (per Minimal Relaxation Rule)

**Killed:** the timing-based (a priori vs. post-hoc) mechanism, H1 as
literally stated. It does not survive Balmer as a counter-example and
does not add content beyond generic overfitting.

**NOT killed:**
- The historical map itself (Stage 2) — all 5 sources remain valid,
  independently checked.
- The skeptic's own **fallback**, offered unprompted while falsifying
  H1: rank candidates by **(free parameters + effective ansatz-search
  space) / (independent data points genuinely fit)** — this is the
  mainstream DoF/overfitting explanation the timing-axis story was
  competing with, not extending. It handles all 5 rows above correctly
  (Balmer: 2 params → many later-predicted lines = good; Titius-Bode:
  2 params → 1 next-planet test = bad; Koide: ~0 free params given its
  chosen ansatz → many precision refinements, though the ansatz-search
  itself was informally large; Eddington: 1 integer + heavy auxiliary
  numerology = bad).

**Relaxation Map (one assumption changed, not bundled):** replace the
switching variable "timing of parameter-fixing" with "ratio of
researcher degrees of freedom to independent data points genuinely
fit" — everything else (the map, the cluster labels, the 5 sources)
stays fixed. This is H1', not yet independently attacked, offered here
only as the applied decisive test below, per the skill's own honesty
requirement not to overclaim survival without a fresh attack.

## Stage 7 — Decisive test, applied to Eq.32 (H1', not independently
## re-attacked — treat this section's verdict as provisional)

Eq.32's own degrees of freedom, counted plainly: coefficient 4/3 (not
derived), exponent 12 (not derived), choice of m_τ/m_e specifically
(not m_μ/m_e or another lepton-mass pair), choice of α_EM/α_G
specifically as the target ratio — **at minimum 3-4 free choices**,
matched against exactly **one** numerical target (the single 0.0135%
agreement itself).

**Critically:** unlike Balmer (2 params → correctly predicted dozens of
independent NEW spectral lines afterward) or Koide (~0 free params given
its ansatz → the SAME fixed formula re-tested against decades of
improving τ-mass measurements), **Eq.32 has made no subsequent
out-of-sample prediction using its own fixed parameters** — there is no
"Eq.33" that reuses the same coefficient/exponent choice to correctly
anticipate a number not already known when Eq.32 was constructed.

**Applied verdict:** by the DoF/prediction-structure criterion that
actually survived the attack (not by the falsified timing criterion),
**Eq.32 currently sits structurally closer to the Titius-Bode/Eddington
failure cluster than to the Koide/Balmer survival cluster** — not
because any mechanism has shown it false, but because it has not yet
cleared the one bar that historically separates survivors from failures
in this specific literature: an independent, out-of-sample prediction
made with the same fixed parameters, before that prediction's target
was known.

## What this does NOT establish

1. **Does not claim Eq.32 is false or wrong** — a formula sitting in the
   "not yet cleared the bar" region is not thereby refuted; Koide itself
   sat in a similarly unproven position for years before a very close
   analogue would be checkable, and remains open 44 years later.
2. **Does not repeat or supersede `NR-019`'s mechanism-hunt** — that
   asked "can Eq.32 be DERIVED"; this asks "does Eq.32's historical
   *pattern* (parameter count vs. subsequent predictions) resemble
   surviving or failed numerology" — a different, complementary
   question.
3. **H1' (the DoF-based fallback) has NOT itself been independently,
   adversarially attacked** — it is the skeptic's own honest fallback
   after falsifying H1, offered as the best-supported alternative in
   the same report, not a freshly-defended Repair Hypothesis in its own
   right. A rigorous version would need the dataset the skeptic itself
   specified (≥30 historical cases, blind-coded, regression-controlled
   for prestige/DoF) — not attempted here.
4. **Does not identify a concrete, buildable "Eq.33"-style prediction**
   TJB's own framework could make to clear the bar — that would be the
   natural next step if this angle is pursued further, not attempted
   here.
5. **Novelty status: capped at `closely related`**, per this skill's own
   rule — Stage 8 (`/novelty-assessment`) was not separately delegated,
   and Stage -1 already flagged that meta-literature on "numerology vs.
   real physics" pre-exists this run.

## Confidence (per skill's own template, not one number)

- evidence strength: HIGH for the historical map (5 real, checkable
  sources); MEDIUM for the applied verdict on Eq.32 (H1' not
  independently attacked)
- novelty: LOW-MEDIUM (capped, per Stage -1 + no delegated novelty check)
- plausibility: MEDIUM — DoF/prediction-structure is the mainstream
  statistical explanation for this whole literature, not a stretch
- falsifiability: HIGH — a concrete "Eq.33" independent prediction test
  is namable (Stage 7), just not built here
- experimental tractability: HIGH — cheap to formalize and check further
- attack status: `survived weak attack` for H1' (skeptic offered it as
  a fallback within the same inline attack, not a fresh delegated
  attack of its own) — NOT `survived`

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
