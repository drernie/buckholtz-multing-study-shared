# P42 — the g-sector's `Φ−Ψ` gap and the κ-sector's `Ω_φ` gap need the *identical* missing factor (`A/c²`): mechanically confirming what P21 already anticipated but never checked

**Date:** 2026-08-14
**Status:** Built, run, ruff clean, all assertions pass.
**Pending context-blind skeptic review (Step 8a) — not yet run.**
**Origin:** ninth step of the covariant-completion campaign
(`PLAN_final_goal_20260814.md`), continuing at the deliberately slower,
one-step-at-a-time pace per explicit user instruction ("продолжай P42,
медленно"). `FINDING_P21` itself already anticipated (§4): *"`Ω_φ`'s
formula (P14) is built from the same `φ` field that the dipole coupling
sources, so the same missing constant `A` enters it."* `FINDING_P39`
independently found the g-sector's `Φ−Ψ` (P38/P40) has the *same*
dimensional residual (`kg/m`) `FINDING_P17` already found for the
κ-sector's `Ω_φ` (P14) — but explicitly flagged this only as *"a striking
structural echo... NOT independently established"* (P39 §2). This step
closes exactly that gap.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P42_omega_phi_ghat_shared_missing_constant.py`, ruff clean,
all assertions pass.

## 0. Honest scope

This is a **symbol/units provenance check**, the same category as P39 and
P41 — not new physics. It re-derives `Ω_φ`'s own dimensional chain
mechanically from `FINDING_P14`'s own quoted base formulas (not from
memory or paraphrase), compares it directly to `Φ−Ψ`'s already-established
dimension (P39), and — if they match — solves for exactly what missing
factor (in terms of `FINDING_P21`'s own already-named constant `A` and a
power of `c`) would resolve *both* gaps simultaneously.

**What this does NOT do:** it does not determine `A`'s numeric value, does
not resolve P39's blocked SI comparison, and does not claim the two
*physical* mechanisms (g-sector monopole force vs. κ-sector dipole
self-energy) are otherwise the same — only that their respective
*missing normalization constants* are dimensionally identical, exactly as
P21's own §4 already said should be the case.

## 1. Re-deriving `Ω_φ`'s dimension from `FINDING_P14`'s own quoted formulas

Quoted directly from `FINDING_P14` §6 (not paraphrased):

> "`p_i = u_i * m_cluster`, `u_i` has units of length (m) → `p_i` has
> units `kg*m`" ... "`E_self = (8*pi/3) * p_i^2 / r_min^3` → units
> `(kg*m)^2 / m^3 = kg^2/m`"

Continuing through `ρ_φ=n·E_self` (`n`=number density, `1/length³`) and
`Ω_φ=ρ_φ/ρ_crit` (`ρ_crit` has standard cosmological units, `kg/m³`):

```
[p_i] = kg·m
[E_self] = kg²/m         (script assertion, matches P14's own stated value)
[Ω_φ] = kg/m             (script assertion, matches P14/P17's own stated value)
```

## 2. Comparing to `Φ−Ψ`'s own dimension (P39's established result)

```
[Φ−Ψ] = kg/m             (script assertion, matches P39's own Step 7 result)
```

**Identical** to `[Ω_φ]` — confirmed via independent re-derivation of both
quantities from their own respective source findings' formulas, not by
re-asserting the earlier "echo" observation.

## 3. The shared missing factor

Both `Ω_φ` (an energy-density fraction) and `Φ−Ψ` (a metric-perturbation
combination) must be dimensionless. Solving for what missing
multiplicative factor fixes each:

```
missing (κ-sector) = m/kg
missing (g-sector)  = m/kg
```

**Identical** (script assertion). Solving this exponent system for `A`'s
and `c`'s powers directly (not guessed):

```
missing = A¹ · c⁻² = A/c²
```

Verified on all three dimension components independently — the mass and
length exponents were used to *solve* for the powers of `A` and `c`; the
time exponent was then checked *separately*, as an independent
consistency test (not a free parameter silently absorbed into the solve).

## 4. What this establishes, precisely

`FINDING_P14/P17`'s κ-sector `Ω_φ` gap and `FINDING_P38-P40`'s g-sector
`Φ−Ψ` gap require the **identical** missing factor, `A/c²`, where `A` is
`FINDING_P21`'s own already-named (but never numerically fixed) constant
with `G_N`'s units. This **mechanically confirms**, rather than merely
echoes, `FINDING_P21`'s own §4 anticipation that "the same missing
constant `A` enters" both channels — a structural claim made a full
session's worth of findings ago (2026-08-13) and never checked until now.

## 5. What this does NOT establish

1. **`A`'s numeric value.** Only that the *same* symbolic constant, in the
   *same* combination with `c`, resolves both gaps — not what it equals.
2. **Resolution of `FINDING_P39`'s own blocked SI comparison.** That gap
   (the `g`/`ĝ` inconsistency between `P21` and `P33`) is separate from,
   and not addressed by, this finding — confirming `A` is shared between
   two *symptoms* of the missing-normalization problem does not by itself
   fix the *underlying* `g`-unit inconsistency P39 found.
3. **That the g-sector and κ-sector mechanisms are physically the same.**
   The monopole force (g-sector) and the dipole self-energy (κ-sector)
   remain structurally distinct physical channels (P1's own multipole
   hierarchy) — only their *missing normalization constants* are shown
   to coincide, which is precisely what P21 said should follow from both
   being sourced by the same underlying field `φ`.
4. **Whether `κ`'s own still-unfixed absolute scale (P14 §3-4) is
   affected.** `κ` and `A` are explicitly different quantities (P14 §6:
   "That constant is not derived anywhere in this project, is not the
   same thing as `κ`") — this finding's result is about `A` alone.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction's
   internal bookkeeping, not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P42_omega_phi_ghat_shared_missing_constant.py
```
