# P25 — the k-sector predicts a genuine, composition-dependent WEP violation, unlike the g-sector

**Date:** 2026-08-13
**Origin:** user-directed roadmap (P24→P27), second item: after P24
established `η=κ/g` unifies the cross-sector force ratios, does the new
k-sector force survive local/laboratory tests of the weak equivalence
principle (WEP)? P23's skeptic review already established the **g-sector**
(monopole, universal coupling to mass) is degenerate with `G` and evades
equivalence-principle tests structurally. This finding asks the parallel
question for the **k-sector** (dipole coupling `κ`, structurally different
since it couples to `kᵢ`, not simply to mass).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P25_wep_eotvos_kill_gate.py`

## 1. Method

Reused P24's own already-verified `F_km` expression unchanged (sympy, not
re-derived by hand). Computed the acceleration of a light test body
`(M,K,r)` falling toward a fixed heavy source `A` — `a = F_km/M` — for two
test bodies of different composition (`1`, `2`) in the *same* source field.

## 2. Result

```
a_1 = -2·A·g·κ·K_1·M_A·r_1/(M_1·c²·r³) − 2·A·g·κ·K_A·r_A/(c²·r³)
a_2 = -2·A·g·κ·K_2·M_A·r_2/(M_2·c²·r³) − 2·A·g·κ·K_A·r_A/(c²·r³)
```

Each acceleration splits **cleanly** into a source-only term (identical for
both test bodies — `K_A`, `r_A`, no dependence on the test body at all) plus
a term proportional to the test body's **own** `Kᵢ·rᵢ/Mᵢ` — its dipole
moment per unit mass (`pᵢ=κ·Kᵢ·rᵢ/c²` per the action, so this is exactly
`pᵢ/Mᵢ`).

The source-only term **cancels identically** from `a₁−a₂` (verified
symbolically, not assumed):

```
a_1 − a_2 = -2·A·g·κ·M_A/c²r³ · [K_1·r_1/M_1 − K_2·r_2/M_2]
```

**Positive control**: setting `K_2·r_2/M_2 = K_1·r_1/M_1` (matched dipole-
moment-per-mass across the two bodies) forces `a_1−a_2 = 0` **exactly** —
confirms the violation is driven purely by the composition ratio
`Kᵢ·rᵢ/Mᵢ`, not by mass or radius separately.

## 3. Consequence — a real structural asymmetry between the two sectors

The g-sector (P23) and k-sector (this finding) behave **oppositely** under
composition:

| sector | acceleration depends on test body's own charge? | EP-test visible? |
|---|---|---|
| `g` (monopole) | no — degenerate with `G` (P23) | **no** — structurally evades EP tests |
| `κ` (dipole) | **yes** — via `Kᵢ·rᵢ/Mᵢ` | **yes** — exactly the signature Eötvös-type experiments detect |

This is a genuine, falsifiable prediction of this project's own
reconstruction: **unless `K/M` (per-unit-mass "second charge") happens to
be universal across ordinary materials — nothing in this project's cited
files claims or requires that — the k-sector predicts a real, nonzero
equivalence-principle violation**, in principle detectable by existing
torsion-balance or space-based (e.g. MICROSCOPE-class) experiments.

## 4. What this does NOT establish — the kill-gate is not yet closed

1. **A numeric value for `η_Eötvös`.** The symbolic expression
   `η_Eötvös = 2|a₁−a₂|/|a₁+a₂|` is derived, but evaluating it requires (a)
   a real, independently-verified experimental EP-bound (e.g. MICROSCOPE's
   actual reported sensitivity) and (b) a real or estimated value for how
   much `Kᵢ·rᵢ/Mᵢ` varies across ordinary laboratory materials (beryllium
   vs. titanium, etc.) — **neither has been attempted here**. Both would
   require external fetches with the same precision discipline P22 applied
   (not from memory, cross-checked, honestly caveated).
2. **Whether the construction survives or is killed by existing WEP
   data.** This finding establishes *that* a real, computable violation
   exists and *what it depends on* — not *how large* it is. The "kill
   gate" the user's roadmap named is therefore **not yet closed** — this is
   the necessary structural first step, not the final verdict.
3. **Any claim about `kᵢ`'s actual physical origin or expected material
   dependence.** `FINDING_P7_k_definition_resolved_from_corpus.md` (cited,
   not re-read in full here) established `k`'s definition from the corpus;
   whether it varies significantly across ordinary matter compositions is
   a separate, unaddressed question.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P25_wep_eotvos_kill_gate.py
```

## Skeptic verdict (context-blind, Step 8a)

*Pending — to be run with only this file + `P25_wep_eotvos_kill_gate.py` +
`P24_gk_matching_eta_invariant.py` +
`FINDING_P24_gk_matching_eta_invariant.md` (skeptic review pending on P24
itself — flagged, not resolved) + `FINDING_P23_target_population_confirmed_universal.md`
(corrected version), no session history.*
