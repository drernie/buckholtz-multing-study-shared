# P1: is β_q/β_d = √6/2 inevitable, or an artefact of the construction?

**Date:** 2026-08-10 · plan item P1 after the external review of the bridge track
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `two_field_action_closure.py`

---

## The reviewer's question, answered directly

**Neither, in the way the question was posed.** The two-charge construction's
individual numbers (`β_d = 2, β_q = √6`) *are* artefacts of one convention (the
lever arm identified with `r_A`), but their **ratio** is not — it is invariant
under every rescaling of the dipole moment, and it is fixed by exactly one
physical fact: **the mediator is massless.**

## 1. All three tiers are derivatives of one kernel

Reducing the construction to its skeleton: `U_mm = m_Am_BK(r)`, `U_km ~ K'(r)`,
`U_kk ~ K''(r)` for any exchange kernel `K`. Recomputing the mirror-symmetric
configuration symbolically for general `K` reproduces the earlier coefficients
exactly for `K = 1/s`:

```
U_mm = m_A m_B / r
U_km = (d_A m_B q_A + d_B m_A q_B) / r^2
U_kk = 2 d_A d_B q_A q_B / r^3
F_km = 2(...)/r^3,  F_kk = 6(...)/r^4     <- the "2" and the "6", now DERIVED
                                              from a general kernel, not asserted
```

## 2. The ratio is invariant; the individual numbers are not

Rescaling the dipole moment `p → λp` (any `κ`, any lever-arm convention) sends
`ℓ_d → λℓ_d`, `ℓ_q² → λ²ℓ_q²`, so `ℓ_q²/ℓ_d²` is exactly unchanged — checked
symbolically, difference is identically zero. **`β_d = 2` depends on the choice
`d = r_A`; `β_q/β_d = √6/2` does not.** Only the ratio is physical content; the
individual value was never a prediction to begin with.

## 3. The kernel invariant, and what actually fixes the ratio

The ratio reduces to a pure property of the exchange kernel:

```
Lambda(r) = K'''(r) K'(r) / K''(r)^2
```

| kernel | Λ |
|---|---|
| massless, `K = 1/s` | **3/2, exactly, at every r** |
| Yukawa, `K = e^{-μs}/s`, small `μr` | `3/2 − (3/4)μ²r²` — **r-dependent, ≠ 3/2** |

**[CORRECTED 2026-08-26, `P149` skeptic review]** the Yukawa row above is
an *incomplete* expansion — this script's own `sp.series` call truncated
before the next term, silently dropping a real `+(μr)³` contribution. The
correct expansion is `Λ = 3/2 − (3/4)(μr)² + (μr)³ − (5/8)(μr)⁴ + O((μr)⁵)`,
independently reverified in `FINDING_P149_massive_mediator_nearfield_hierarchy.md`
§0. Does not change this file's own conclusion (only the ratio is
physical; `β_q/β_d=√6/2` iff massless) — the cubic term is negligible at
every scale this project has used the small-`μr` limit for — but the
truncated quote should not be cited further without this correction.

**`β_q/β_d = √6/2` if and only if the mediator has no mass on the relevant
scale.** That is the physical content of the prediction — not the point-charge
scaffolding, which was only the calculational route to it. This reframes the
earlier finding: the number was never really about how the charges were laid
out; it was about whether the exchanged field is massless.

## 4. What the field theory adds beyond the earlier construction

**Action.** A linear source coupling to a canonical scalar,
`S = ∫d⁴x[½(∂φ)²] + Σᵢ∫dτ[gmᵢ + pᵢ·∇]φ(xᵢ)`, `pᵢ = κkᵢrᵢ/c²`. No ghost, no
tachyon, energy bounded below — the k-charge enters only through a derivative
coupling, exactly as required by `two_charge_completion.py`'s construction.

**The equivalence-principle obstruction, resolved by reclassification.**
`CANDIDATE-L1` (2026-07-22) found that a stable, EP-respecting, static local
action cannot give a *repulsive* `1/r³` force, and left it as an open
obstruction requiring TJB to name which standard assumption MULTING relaxes.
This construction names it: **`φ` is a fifth force, not gravity.** Its `m·m`
exchange renormalises `G` (attractive, absorbed into the measured value); the
repulsive dipole tier violates nothing, because the equivalence principle
constrains the *gravitational* sector, not a companion scalar. The relaxed
assumption is `F_oP = pure gravity` → `F_oP = gravity + one scalar fifth
force`.

**Cosmological limit — this completion cannot supply MULTING's `H(z)` eras.**
On an isotropic background, the radial-dipole average is a double layer (zero
force off-shell, proven `FINDING_dipole_shell_is_a_double_layer.md`) and the
randomly-oriented average is zero by symmetry. Either way, this completion
contributes **only a `G`-renormalisation** to the background expansion at first
order — it cannot be the mechanism behind MULTING's claimed eras of changing
expansion rate. This is now a **second, independent route** to the same
conclusion P2 reached from the archive's own numbers (MULTING is q-blind on the
background, equal to `ΛCDM@H₀=73`).

## Verdict

```
beta_q/beta_d = sqrt(6)/2       : NOT a free-construction artefact -- invariant
                                  under every rescaling of the dipole moment
Physical content of the ratio   : mediator is massless (Lambda = 3/2 <=> K=1/s)
Action                          : written, ghost-free, derivative k-coupling
EP obstruction (CANDIDATE-L1)   : RESOLVED by reclassifying phi as a fifth
                                  force, not gravity
Cosmological background         : this completion contributes G-renormalisation
                                  ONLY -- cannot generate MULTING's H(z) eras;
                                  converges independently with P2's result
```

## What this does NOT establish

1. Not a derivation of MULTING itself — a demonstration that a specific,
   minimal completion is internally consistent and that its one nontrivial
   number (the ratio) has a clean physical meaning.
2. `Λ = 3/2` was checked only for `K = 1/s` and the small-`μr` Yukawa limit; a
   confining or otherwise exotic kernel was not surveyed.
3. The "fifth force, not gravity" reclassification resolves the *sign*
   obstruction CANDIDATE-L1 raised. It does not by itself explain why nature
   would contain such a force, nor its coupling strength.
