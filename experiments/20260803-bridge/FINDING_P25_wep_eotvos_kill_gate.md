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

**[CORRECTED after skeptic review, same day — a real completeness gap,
not a framing issue.]** The original version computed the test body's
acceleration from `F_km` alone. The skeptic found this misses two real
contributions: `F_mm`, which dominates the denominator `|a₁+a₂|` and was
silently omitted from `η_Eötvös`'s printed form, and `F_kk`, which
contributes its **own** composition-dependent term (quadratic in `κ`,
scaling as `1/r⁴` — different from `F_km`'s linear-in-`κ`, `1/r³` term).
The original positive control (matching `K·r/M` across two bodies) is
kept, but its diagnostic *limit* is now stated: both the `F_km` and `F_kk`
composition pieces share the *same* `K·r/M` dependence, so that control
cannot tell whether `F_kk` was correctly included — it passes either way,
exactly the failure mode `FINDING_two_charge_completion.md §6` already
warns about ("a control that switches off the feature under test cannot
test it"). A genuinely differentiating check (the two pieces' different
`r`-power) is added instead. §§2–3 below are rewritten with the full
`F_mm+F_km+F_kk` calculation; §3's "structural opposite" framing is also
softened — see the Skeptic Verdict section for the complete breakdown.

## 1. Method

Reused P24's own already-verified `tiers_from_kernel` machinery (sympy,
not re-derived by hand) for the **full** force `F_mm+F_km+F_kk` between a
light test body `(M,K,r)` and a heavy fixed source `A`. Computed
`a = F_total/M` for two test bodies of different composition (`1`, `2`) in
the *same* source field.

## 2. Result (corrected — full `mm+km+kk`, sympy-verified)

```
a_1 = A·M_A·g²/r²  −2·A·g·κ·K_A·r_A/(c²r³)          [composition-independent]
    + K_1 · [6·A·κ²·K_A·r_1·r_A/(M_1·c⁴r⁴) − 2·A·g·κ·M_A·r_1/(M_1·c²r³)]   [composition-dependent]
```

The composition-**independent** part (`F_mm` entirely, plus `F_km`'s
source-only term) cancels identically from `a₁−a₂` — verified by setting
`K_1=K_2=0` in `a₁−a₂` and confirming the result is `0`.

The composition-**dependent** coefficient of `K₁` has **two independent
pieces**, verified as genuinely distinct (not a duplicate) by their
different power of `κ` and of `r`:

```
F_km-derived piece (κ¹, ~1/r³):  −2·A·g·κ·M_A·r_1/(M_1·c²r³)
F_kk-derived piece (κ², ~1/r⁴):   6·A·κ²·K_A·r_A·r_1/(M_1·c⁴r⁴)
```

Corrected `η_Eötvös = 2|a₁−a₂|/|a₁+a₂|`, using the **full** `a₁`, `a₂` in
both numerator and denominator (the original version used `F_km` alone in
the denominator, which understates it — `F_mm` dominates in reality):

```
η_Eötvös = 2κ|3K₁K_AM₂κr₁r_A − K₁M₂M_Ac²gr r₁ − 3K₂K_AM₁κr₂r_A + K₂M₁M_Ac²gr r₂|
           / |3K₁K_AM₂κ²r₁r_A − K₁M₂M_Ac²gκr r₁ + 3K₂K_AM₁κ²r₂r_A − K₂M₁M_Ac²gκr r₂
              − 2K_AM₁M₂c²gκr r_A + M₁M₂M_Ac⁴g²r²|
```

**Positive control, with its diagnostic limit now stated explicitly**:
setting `K₂·r₂/M₂ = K₁·r₁/M₁` forces `a₁−a₂=0` — but since *both*
composition pieces above share this same ratio, this control passes
identically whether `F_kk` is included or omitted. It does not discriminate
the specific completeness error the skeptic found.

**The genuinely differentiating check**: the two composition pieces have
different powers of `κ` (`κ¹` vs. `κ²`) and of `r` (`1/r³` vs. `1/r⁴`) —
verified symbolically that subtracting both explicit pieces from the
sympy-computed `d(a₁)/d(K₁)` leaves a residual of exactly `0`, confirming
they are independent, additive, both real contributions.

**Codimension-1 cancellation surface** — a second escape route beyond
`K/M` universality: solving `[F_km-piece + F_kk-piece] = 0` for `κ` gives
`κ = M_A·c²·g·r/(3·K_A·r_A)` — a specific (fine-tuned, not generic) relation
among the parameters that would also hide the violation even if `K/M` is
*not* universal. Not claimed to be natural or likely; only that it exists
and was not named in the original version.

## 3. Consequence — a conditional, not unconditional, asymmetry between the two sectors

**[Corrected after skeptic review — "structural asymmetry" and the
unconditional yes/no table below overstated this.]** The g-sector (P23)
and k-sector (this finding) behave differently under composition, but the
opposition is **conditional**, not structural-full-stop:

| sector | acceleration depends on test body's own charge? | EP-test visible? |
|---|---|---|
| `g` (monopole) | no — degenerate with `G` (P23), **exactly zero**, unconditionally | **no** — structurally evades EP tests |
| `κ` (dipole) | yes, **if** `K/M` is non-universal and outside the codimension-1 surface above | conditionally — magnitude depends on how far `K/M` is from universal |

This is a genuine, falsifiable prediction of this project's own
reconstruction, correctly scoped: **`MODEL_SPEC_AUDIT.md` itself flags the
`k_A,k_P` row as `OPEN` — "postulate, not sharply defined"** — whether
`K/M` varies across ordinary materials is not resolved anywhere in this
project. If `K/M` turns out to be even approximately universal (plausible
if `kᵢ` correlates with mass the way ordinary matter's nucleon count does),
the k-sector's Eötvös signal is **numerically suppressed toward the
g-sector's exact zero**, not qualitatively opposite to it — these are not
the same statement, and the original version conflated them.

## 4. What this does NOT establish — the kill-gate is not yet closed

1. **A numeric value for `η_Eötvös`.** Evaluating the corrected closed
   form requires (a) a real, independently-verified experimental EP-bound
   (e.g. MICROSCOPE's actual reported sensitivity) and (b) a real or
   estimated value for how `Kᵢ·rᵢ/Mᵢ` varies across ordinary laboratory
   materials — **neither attempted here**. Both would require external
   fetches with P22's same precision discipline.
2. **Whether the construction survives or is killed by existing WEP
   data.** This finding establishes *that* a real, computable, conditional
   violation exists and *what it depends on* — not *how large* it is nor
   *whether the condition holds*. The "kill gate" is **not yet closed**.
3. **`kᵢ`'s actual physical origin or expected material dependence.**
   `FINDING_P7_k_definition_resolved_from_corpus.md` (cited, not re-read
   in full here) established `k`'s definition from the corpus; whether it
   varies across ordinary matter compositions — the single fact that would
   settle §3's question — is unaddressed anywhere in this project.
4. **[Added after skeptic review] Whether the lab-scale physical-dipole
   picture is even coherent.** The construction models each body as a
   physical dipole (charges at `±rᵢ/2`, lever arm = the body's own
   radius) — motivated for megaparsec-scale galaxy clusters. Whether that
   same picture is a sensible model for a centimeter-scale, kilogram-mass
   laboratory test body (which has no obvious intrinsic dipole moment in
   the same sense) is not addressed anywhere in this finding or its
   sources.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P25_wep_eotvos_kill_gate.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `P24_gk_matching_eta_invariant.py`,
`FINDING_P24_gk_matching_eta_invariant.md`, and
`FINDING_P23_target_population_confirmed_universal.md` (corrected
versions) — no session history. The skeptic's own tool access lacked a
Python runtime; it verified the algebra entirely by hand from the cited
files' own printed output, cross-checked here independently with sympy
before accepting (soundness check: does the claimed missing term actually
appear, and does it actually change the printed answer? — confirmed yes,
by direct symbolic computation, not just by re-reading the argument).
Five sub-verdicts, per Step 8a (not merged):

- **(A)** Reuse/setup fidelity from P24: **CONFIRMED-REAL** — `F_km`
  identical to P24's own printed form; A↔B asymmetry concern raised in the
  review checked and found not real (P24's `F_km` is manifestly symmetric
  under A↔B swap; the "fixed source, falling test body" framing is a
  coordinate choice, not a hidden physical bias).
- **(B)** Completeness of the acceleration calculation: **WEAKENED, and
  the single most important finding of this review** — `F_km` alone omits
  `F_mm` (dominates the denominator) and `F_kk` (an additional
  composition-dependent term of opposite functional form). *Applied: FIXED
  — full `mm+km+kk` calculation throughout §2, independently re-verified
  by sympy before accepting.*
- **(C)** Positive control's diagnostic strength: **WEAKENED** — the
  control cannot discriminate the specific completeness error found in
  (B), since both composition pieces share the same `K·r/M` dependence;
  same failure mode this project's own `FINDING_two_charge_completion.md
  §6` already warns about. *Applied: limit stated explicitly; a
  genuinely differentiating check (different `r`-power) added.*
- **(D)** "Structural opposite of `g`" framing: **WEAKENED** — presented
  as an unconditional binary opposition when it is actually conditional on
  `kᵢ`'s material dependence, which `MODEL_SPEC_AUDIT.md` itself flags
  `OPEN`. *Applied: §3's table and framing corrected to state the
  condition explicitly, distinguishing "structurally zero" (`g`) from
  "conditionally small or large" (`κ`).*
- **(E)** Adequacy of §4's own scope-limiting language: **WEAKENED** — the
  original §4 disclaimed the *numeric* gap but not the *symbolic-form*
  gap (missing `F_kk`, missing `F_mm` in the denominator), the
  cancellation surface, or the lab-scale dipole-geometry coherence
  question. *Applied: all three added as new §4 items.*

**Not a core-predicate-false kill.** The qualitative claim — the k-sector
*can* produce a real, falsifiable, composition-dependent acceleration
difference, structurally different from the g-sector's exact zero — is
strengthened, not overturned, by including the full calculation (a second
independent mechanism was found, not removed). What was withdrawn is the
overclaimed *unconditional* framing and the incomplete symbolic form,
both now corrected.
