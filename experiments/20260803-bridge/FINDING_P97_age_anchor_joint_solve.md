# FINDING P97 — **NO-ROOT again, but the gap collapses to `~0.06%`.** Age doesn't resolve the degeneracy either, and this time the mechanism is not proven

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P97_age_anchor_joint_solve.py`

> `FINDING_P96` registered the age of the universe — an **integral** over the
> full expansion history, structurally different from a same-epoch ratio like
> `Ω_m`/`Ω_Λ` — as the next candidate to break the `Λ_internal` degeneracy.
> Sourced properly first: `t₀ = 13.787 ± 0.020 Gyr` and the Hubble-time
> conversion constant, both verified via `WebSearch` rather than trusted from
> memory (Planck 2018 VI, arXiv:1807.06209).

---

## The physical quantity, derived before any code

`H = d(ln a)/dt`, and `ln(a)` is the same dimensionless quantity in either
description (`a`'s own rescaling drops out of a derivative) — only `t`'s unit
convention differs (`FINDING_P84`'s `S2`). So if `t_physical = τ·t_internal`
for one constant `τ`, then `H_physical = H_internal/τ`, giving
`τ = H_internal(a_today)/H_0`. The age at `a_today` is then

```
physical_age [Gyr] = t_internal(a_today) · H_internal(a_today) · HubbleTimeGyr(H_0)
```

with `HubbleTimeGyr(H_0) = 977.79/H_0[km/s/Mpc]` — a **pure unit conversion**
(`Mpc→km`, `Gyr→s`, both exact), verified this session, not measured
cosmological data. `t_internal(a_today)` is read directly off the
already-solved trajectory — `P94`/`P95`'s own `brentq` root already computes
it; this file is the first to **keep** it rather than discard it.

## Control — deep matter domination, checked before trusting the rest

| `a` | `t·H` | deviation from `2/3` |
|---|---|---|
| `5` | `0.663044` | `3.622e-03` |
| `15` | `0.701584` | `3.492e-02` |
| `50` | `0.659304` | `7.363e-03` |
| `150` | `0.664901` | `1.765e-03` |
| `500` | `0.665816` | `8.504e-04` |

Converges toward the textbook Einstein–de Sitter value `age = 2/(3H)` — a
result external to this project — as `a` grows, worst deviation `8.5×10⁻⁴` at
`a=500`. The bump at `a=15` is expected, not a defect: it sits at diamond
D1/D2's constraint epoch (`a≈12.18`), where the coupling's imprint on `H` is
largest. **Control passes.**

## Part A — the scan

| `Λ` | `a_today` | `Ω_m` | age (Gyr) | `g(Λ)` |
|---|---|---|---|---|
| `2.084e-16` | `218519.36` | `0.315000000` | `13.796148` | `+0.009148` |
| `5.429e-16` | `158811.93` | `0.315000000` | `13.796129` | `+0.009129` |
| `1.414e-15` | `115417.88` | `0.315000000` | `13.796043` | `+0.009043` |
| `3.685e-15` | `83881.96` | `0.315000000` | `13.796046` | `+0.009046` |
| `9.598e-15` | `60962.23` | `0.315000000` | `13.795975` | `+0.008975` |
| `2.500e-14` | `44304.29` | `0.315000000` | `13.795744` | `+0.008744` |
| `6.514e-14` | `32198.71` | `0.315000001` | `13.795627` | `+0.008627` |
| `1.697e-13` | `23401.50` | `0.315000007` | `13.795703` | `+0.008703` |
| `4.421e-13` | `17007.43` | `0.315000009` | `13.795535` | `+0.008535` |
| `1.152e-12` | `12359.36` | `0.315000002` | `13.794577` | `+0.007577` |
| `3.000e-12` | `8982.63` | `0.315000000` | `13.794463` | `+0.007463` |

**Zero sign changes.** `g(Λ)` is positive everywhere — the completion's age at
`Ω_m=0.315` always slightly **overshoots** `13.787 Gyr`.

---

## What is different from `FINDING_P95`, stated plainly

**The gap is far tighter.** `P95`'s `Ω_φ` shortfall spanned `3.4×10⁻⁷` to
`4.0×10⁻⁵` — up to two orders of variation across the `Λ` grid. Here `g(Λ)`
ranges only `0.0075` to `0.0091` Gyr — a **`~0.06%` relative** discrepancy,
varying by barely `20%` of its own value across five decades of `Λ`. This is
the tightest near-miss in the entire `P93`–`P97` arc.

**And, honestly, unproven.** `P95`'s `NO-ROOT` came with a **proof**:
`Ω_φ = (φ̄̇²/2+V_scalar)/\text{tot} ≥ 0` identically, forcing
`Ω_Λ ≤ 1-Ω_m` with no escape. No equivalent algebraic argument is offered
here. `g(Λ)`'s near-constancy across five orders of magnitude in `Λ` — rather
than tracking `Λ` the way `P95`'s `Ω_φ` did — suggests the excess age is not
primarily sourced by the dark-energy term at all, but this is **observed, not
derived**. Per this campaign's own discipline (P87's lesson), no mechanism is
narrated for a pattern merely seen.

---

## Verdict

**`NO-ROOT`.** The completion cannot match both `Ω_m=0.315` and the real age
`13.787 Gyr` at any epoch, for any `Λ` in `[8×10⁻¹⁷, 3×10⁻¹²]`. Closest
approach: `Λ=3.000×10⁻¹²`, `|g|=0.0075` Gyr. **No `k[h/Mpc]` number is
quoted.**

### Reading this against the arc so far

| step | anchor pair | result |
|---|---|---|
| `P93` | `Ω_Λ=0.7` alone | tautological |
| `P94` | `Ω_m` alone, `Λ` fixed | `31.6×` spread |
| `P95` | `Ω_m` + `Ω_Λ`, exact | `NO-ROOT`, **proven** (`Ω_φ≥0`) |
| `P96` | `Ω_m` + `Ω_Λ`, tolerant | window opens, spread **unchanged** |
| `P97` | `Ω_m` + age, exact | `NO-ROOT`, **unproven**, gap `~0.06%` |

A genuinely different kind of anchor (an integral, not a same-epoch ratio)
produced a genuinely different **kind** of near-miss — far tighter, without
the clean positivity proof `P95` had. Given `P96`'s own finding that Planck's
`±0.007` tolerance easily absorbed `P95`'s gap, and this gap is smaller still
in relative terms, the natural next check — not attempted here — is whether
Planck's `±0.020` Gyr tolerance on the age similarly absorbs this one. Unlike
`P96`, that would not by itself say anything new about the `Λ`-degeneracy
(Q2) — the same caution `P96` raised applies here without having to re-derive
it.

### Not established

- Why `g(Λ)` is nearly constant across five orders of magnitude in `Λ`,
  rather than tracking it the way `P95`'s `Ω_φ` did — observed, not explained.
- Whether Planck's own `±0.020` Gyr age uncertainty opens a window (not
  attempted; would answer only the over-constraint question, not the
  `Λ`-degeneracy, per `P96`'s already-established caution).
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
