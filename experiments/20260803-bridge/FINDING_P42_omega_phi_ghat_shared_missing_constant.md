# P42 — under one of P39's two unresolved readings, the g-sector's `Φ−Ψ` gap and the κ-sector's `Ω_φ` gap need the *identical* missing factor (`A/c²`); under the other reading they don't

**Date:** 2026-08-14
**Status:** **Corrected after context-blind skeptic review, same day.**
The core mechanical result survives — under P39's own "Reading 1" (`g`
dimensionless), the two dimensional residuals genuinely match and require
the identical missing factor. But the original version of this finding
presented that match as **unconditional**, when P39 itself left a second,
equally-unprivileged reading ("Reading 2") open — and under Reading 2 the
match **fails**. A bare code comment noted which reading was used; the
finding's own prose did not flag the reading-dependence. Corrected below
(new Step 2b in the script, §2 and §5 here) — the headline claim is now
stated as reading-1-specific, not universal. Full verdict in §6.
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

## 2. Comparing to `Φ−Ψ`'s own dimension — reading-dependent, corrected

`FINDING_P39` left `[g]` (and hence `[ĝ]=[g/c]`) genuinely unresolved
between two readings, neither privileged: **Reading 1** (`g` dimensionless,
per `P21`'s own stated assumption) and **Reading 2** (`[g]` fixed by
`P33`'s own `m_eff/m` formula requirement instead).

```
[Φ−Ψ]_reading1 = kg/m             (script assertion, matches P39's Step 7)
[Φ−Ψ]_reading2 = kg¹m⁻³s²         (script assertion, added after skeptic review)
```

**[CORRECTED per skeptic review — the consequential fix.]** ~~Identical
to `[Ω_φ]`~~ — this is only true under **Reading 1**. Under **Reading 2**,
`[Φ−Ψ]` does *not* match `[Ω_φ]` (`kg/m`) at all. An earlier draft of this
finding used Reading 1 with a bare code comment noting the choice, but
presented the resulting match in the finding's own prose as unconditional
— exactly the "silently pick one of multiple unresolved readings" pattern
this project's own methodology warns against elsewhere. The mechanical
match itself is real and correctly computed (script assertion, verified);
what was wrong was the *scope* claimed for it.

## 3. The shared missing factor — under Reading 1

For the rest of this analysis, `[Φ−Ψ]` refers to **Reading 1** only (see
§2's correction). Both `Ω_φ` and `Φ−Ψ` (under Reading 1) must be
dimensionless. Solving for what missing multiplicative factor fixes each:

```
missing (κ-sector)         = m/kg
missing (g-sector, reading1) = m/kg
```

**Identical, under Reading 1** (script assertion). Solving this exponent
system for `A`'s and `c`'s powers directly (not guessed):

```
missing = A¹ · c⁻² = A/c²
```

Verified on all three dimension components independently — the mass and
length exponents were used to *solve* for the powers of `A` and `c`; the
time exponent was then checked *separately*, as an independent
consistency test (not a free parameter silently absorbed into the solve).

## 4. What this establishes, precisely

**[CORRECTED per skeptic review — scope narrowed, see §2.]** Under P39's
Reading 1 specifically, `FINDING_P14/P17`'s κ-sector `Ω_φ` gap and
`FINDING_P38-P40`'s g-sector `Φ−Ψ` gap require the **identical** missing
factor, `A/c²`, where `A` is `FINDING_P21`'s own already-named (but never
numerically fixed) constant with `G_N`'s units. This **mechanically
confirms**, rather than merely echoes, `FINDING_P21`'s own §4
anticipation that "the same missing constant `A` enters" both channels —
but the confirmation itself is **reading-dependent**, not established
regardless of which of P39's two readings eventually turns out correct.
`FINDING_P21`'s anticipation is confirmed *for one candidate reading*,
not proven to hold universally.

## 5. What this does NOT establish

1. **`A`'s numeric value.** Only that the *same* symbolic constant, in the
   *same* combination with `c`, resolves both gaps under Reading 1 — not
   what it equals, and not under Reading 2.
2. **That the shared-constant result holds under P39's Reading 2.**
   **[Added per skeptic review.]** Explicitly checked (script §2b) and
   found to fail — `[Φ−Ψ]_reading2≠[Ω_φ]`, so no single `A^a·c^b` spans
   both under that reading. Which reading is actually correct remains
   P39's own open question; this finding does not resolve it, and its own
   headline result should not be read as reading-independent.
3. **Resolution of `FINDING_P39`'s own blocked SI comparison.** That gap
   (the `g`/`ĝ` inconsistency between `P21` and `P33`) is separate from,
   and not addressed by, this finding — confirming `A` is shared between
   two *symptoms* of the missing-normalization problem does not by itself
   fix the *underlying* `g`-unit inconsistency P39 found.
4. **That the g-sector and κ-sector mechanisms are physically the same.**
   The monopole force (g-sector) and the dipole self-energy (κ-sector)
   remain structurally distinct physical channels (P1's own multipole
   hierarchy) — only their *missing normalization constants* are shown
   to coincide (under Reading 1), which is precisely what P21 said should
   follow from both being sourced by the same underlying field `φ`.
5. **Whether `κ`'s own still-unfixed absolute scale (P14 §3-4) is
   affected.** `κ` and `A` are explicitly different quantities (P14 §6:
   "That constant is not derived anywhere in this project, is not the
   same thing as `κ`") — this finding's result is about `A` alone.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction's
   internal bookkeeping, not a claim about TJB's own unpublished theory.

## 6. Skeptic verdict (context-blind, Step 8a, 2026-08-14)

Reviewed with this finding + script + `FINDING_P14`, `FINDING_P21`, and
`P39`'s own script (for reuse fidelity), **no session history**, per
Falsification Ladder Context Asymmetry Rule.

**One real, consequential issue found:** this finding's original version
computed `[Φ−Ψ]` using only P39's own "Reading 1" for `[g]`, flagged in a
bare code comment (`# P39's own reading 1`) but **not** flagged as a
scope limitation in the finding's own prose — which presented the
resulting match as an unconditional "IDENTICAL" result. P39 itself never
privileged Reading 1 over Reading 2; silently picking one while
presenting the outcome as unconditional is the same failure mode this
project's own methodology names elsewhere ("silently pick one of multiple
unresolved readings"). Independently re-checked (both by the reviewer and
by re-running the corrected script): under Reading 2, `[Φ−Ψ]`
does *not* match `[Ω_φ]` (verified: `(1,-3,2)≠(1,-1,0)`) — confirming the
issue is real, not a false alarm.

| # | Issue | Verdict | Disposition |
|---|---|---|---|
| 1 | `[Φ−Ψ]` computed under Reading 1 only, presented as unconditional | **WEAKENED — consequential, real overclaim of scope** | Fixed: added Step 2b (explicit Reading 2 check, shown to fail), retitled the finding, scoped every claim in §2-§5 to "under Reading 1" |
| 2 | `P14`'s own quoted formulas (`p_i=u_i*m_cluster`, `E_self=(8pi/3)p_i²/r_min³`) — accurate? | CONFIRMED-REAL — checked against `P14` §6 directly, exact | No fix needed |
| 3 | Dimensional chain `n=1/length³`, `ρ_φ=n·E_self`, `Ω_φ=ρ_φ/ρ_crit` — faithful to P14's actual script, not an invented assumption? | CONFIRMED-REAL — `P14`'s own script defines `n_cluster_upper = rho_m_total / m_cluster_kg` (mass-density/mass = 1/length³), matching exactly | No fix needed |
| 4 | Is the `A/c²` algebra-solving procedure itself correct? | CONFIRMED-REAL — the solving procedure is sound; the issue was *which* reading's residual was fed into it, not the procedure | No fix needed |
| 5 | Does §5 adequately prevent overclaiming beyond the reading issue? | CONFIRMED-REAL once the reading-dependence fix is applied | Addressed by the fix above |

**What survives:** the core mechanical result — under Reading 1
specifically, `Ω_φ` and `Φ−Ψ` have the identical dimensional residual and
require the identical missing factor `A/c²` — independently re-verified
and correctly computed throughout. **What was corrected:** the scope of
the claim, from "unconditional" to "reading-1-specific," with the
Reading 2 failure now shown explicitly (not just asserted) as a new
script step. Kill classification: framing/scope only — the underlying
arithmetic was never wrong, only what it was claimed to establish.

## Reproduction

```bash
python experiments/20260803-bridge/P42_omega_phi_ghat_shared_missing_constant.py
```
