# FINDING P95 — **NO-ROOT, and provably so.** `Ω_m` and `Ω_Λ` cannot be jointly matched at any epoch, for any `Λ`

**Status:** built, run, verdict against pre-registered outcomes; the empirical
result is then upgraded to a proved structural fact.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P95_joint_two_anchor_solve.py`

> `FINDING_P94` registered a "third anchor" — require the completion's `Λ`,
> once converted to physical units, to reproduce the real cosmological
> constant — as the next step. Checking it by hand first produced **two
> contradictory conclusions in a row**: first that this reduces to the
> `Ω_Λ=1−Ω_m` condition `P94` already tried (not new information), then, on
> redoing it, that it is a genuinely different 2-equation system `P94` never
> tested. Two self-contradicting derivations in a row is the signal not to
> trust a third — this file settled it numerically, and the numeric answer
> then unlocked a clean proof.

---

## Why the two hand-derivations disagreed, resolved

Our internal Friedmann budget has **three** components: matter (`Ω_m`), the
added constant (`Ω_Λ`), and a residual scalar contribution
`Ω_φ = 1 − Ω_m − Ω_Λ` that `FINDING_P93` already measured as **nonzero**
(order `1e-5`–`1e-7`). Because `Ω_φ ≠ 0`, `"Ω_m=0.315"` and `"Ω_Λ=0.685"` are
**not** the same condition — flatness alone doesn't make one imply the other
while a third component exists. Jointly imposing both is a real second
equation on `(a_today, Λ_internal)`, and `P94`'s family (fixed `Λ`, vary
`a_today` against **one** condition) never tested it.

## Method — nested root-finding, not a black box

For a given `Λ`: `inner_a(Λ)` is `P94`'s own root (`Ω_m,int(a; Λ) = 0.315`
exactly). Then `g(Λ) := Ω_Λ,int(inner_a(Λ); Λ) − 0.685`. A root of `g(Λ)` gives
a `(Λ, a_today)` pair satisfying **both** conditions simultaneously.

## Result — `g(Λ)` never crosses zero

| `Λ` | `a_today` | `Ω_m` | `Ω_Λ` | `Ω_φ` | `g(Λ)` |
|---|---|---|---|---|---|
| `2.084e-16` | `218519.36` | `0.315000000` | `0.684999657` | `3.430e-07` | `−3.430e-07` |
| `5.429e-16` | `158811.93` | `0.315000000` | `0.684999705` | `2.947e-07` | `−2.947e-07` |
| `1.414e-15` | `115417.88` | `0.315000000` | `0.684994923` | `5.077e-06` | `−5.077e-06` |
| `9.598e-15` | `60962.23` | `0.315000000` | `0.684996312` | `3.688e-06` | `−3.688e-06` |
| `6.514e-14` | `32198.71` | `0.315000001` | `0.684981933` | `1.807e-05` | `−1.807e-05` |
| `4.421e-13` | `17007.43` | `0.315000009` | `0.684998731` | `1.260e-06` | `−1.260e-06` |
| `3.000e-12` | `8982.63` | `0.315000000` | `0.684959994` | `4.001e-05` | `−4.001e-05` |

*(full 12-point grid run; representative rows shown)* — **zero sign changes
across five orders of magnitude in `Λ`.** `g(Λ)` is negative everywhere. Every
`Ω_m` row lands on `0.315` to the root's own tolerance (as designed); every
`Ω_Λ` row falls **short** of `0.685` by exactly `Ω_φ`.

## The empirical result upgrades to a proof

`Ω_φ := (φ̄̇²/2 + V_scalar)/\text{tot}`, with `V_scalar = λφ̄⁴/4 ≥ 0` (even power)
and `φ̄̇²/2 ≥ 0` (a square) and `\text{tot} > 0` (required for viability). So
**`Ω_φ ≥ 0` identically** — a sum of non-negative terms over a positive total,
true at *every* point of *every* viable trajectory, not just the twelve `Λ`
values sampled.

Given `Ω_m` is pinned to exactly `0.315` by the inner root:

```
Ω_Λ = 1 − Ω_m − Ω_φ = 0.685 − Ω_φ  ≤  0.685      always
```

with equality **only** if `φ̄ = φ̄̇ = 0` simultaneously — an isolated
equilibrium point the coupled, oscillating trajectory (`ĝ=1`, `λ=1`, the
campaign's standard working point) does not sit at for any generic `a_today`.
**The joint system cannot be solved by any `Λ`, not merely none of the twelve
tried.** The scan corroborates a structural fact; it does not merely fail to
find one instance of it.

## Verdict — **NO-ROOT**

This is a **sharper, more consequential** negative result than
`FINDING_P94`'s degeneracy. `P94` said "underdetermined — more than one
`(Λ, a_today)` fits the data." `P95` says **over-constrained**: the
completion's own three-component energy budget makes it *structurally
impossible* to match Planck's `Ω_m` and `Ω_Λ` **simultaneously and exactly**,
because the model always leaks a positive, non-negotiable third component into
the budget that neither Planck number accounts for.

**No `k[h/Mpc]` number is quoted.**

### What this does and does not say about the completion

- It does **not** say the completion is wrong, or that `MULTING` is wrong
  (Gate 1 — untouched).
- It **does** say: this completion's dark-energy sector, added as a bare
  constant with no coupling to the scalar (`FINDING_P86`'s construction), can
  never exactly reproduce flat-`Λ`CDM's precise composition **while the scalar
  carries any residual energy at all** — and the scalar always does, at any
  finite epoch, given `ĝ≠0`.
- The **magnitude** of the shortfall (`Ω_φ ~ 1e-7` to `1e-4` across the range
  tried) is small — this is not a large discrepancy. But `Ω_m=0.315` and
  `Ω_Λ=0.685` are quoted by Planck to `±0.007`, and this file demanded **exact**
  equality (Gate 2 discipline: an anchor is a fixed target, not a range to
  land near). Whether the residual is small enough to fall **within** Planck's
  quoted uncertainty is a different, not-yet-asked question.

### Not established

- Whether relaxing exact equality to Planck's quoted `±0.007` uncertainty on
  `Ω_m`/`Ω_Λ` would open a viable window — a genuinely different, weaker
  target than this file used, not attempted here.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.

*(Whether a root exists for `Λ` outside `[8×10⁻¹⁷, 3×10⁻¹²]` is not on this
list — the `Ω_φ ≥ 0` argument above rules it out structurally for **any** `Λ`,
so that question is answered, not open.)*
