# FINDING P107 — **`CONVERGES-CONFIRMED` at every tested `k`, including `k=0.1`.** The strongest M1 result in the arc — and it required realizing the arc's own tool was wrong for this regime

**Status:** built, run twice — a design flaw caught mid-build was not a
bug in the code but a wrong choice of diagnostic quantity, corrected
before trusting any result.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P107_asymptotic_convergence_test.py`

> `FINDING_P106` found that `P104`/`P105`'s `eps(k;Λ)` comparisons were
> only ever snapshots — never confirmed to survive a genuine asymptotic
> reach. This file builds that reach (mirroring `P76`'s own multi-decade
> convergence check) — and along the way discovers that `eps` itself is
> the wrong quantity to test convergence on, once `Λ` dominates.

---

## Reconnaissance first — the reach is genuinely asymmetric

Before designing anything, probed how far each of `FINDING_P105`'s 6
branches can integrate before `T_END=1e8` caps them:

| `Λ` | `a_star` | `a(T_END)/a_star` | decades past crossing |
|---|---|---|---|
| `2e-17` | `368403` | `2.3×` | `0.36` |
| `1e-16` | `215443` | `11.4×` | `1.06` |
| `1e-15` | `100000` | `5948×` | `3.77` |
| `1e-14` | `46416` | `2.3×10¹²` | `12.4` |
| `1e-13` | `21544` | `3.5×10⁴²` | `39.6` (overflow-adjacent) |
| `3e-12` | `6934` | `3.3×10²²⁹` | `217` (deep float64 territory) |

Larger `Λ` means faster de Sitter expansion once it dominates — not more
physics, just faster exponential growth. The two smallest `Λ` genuinely
cannot be pushed far past their own crossing within `T_END=1e8` — a real
infrastructure limit, confirmed by probing `x=(2,5,10,20,50,100)`
directly: **4 of 6 branches resolve cleanly through `x=100`**; `Λ=1e-16`
only to `x=10`; `Λ=2e-17` only at `x=2` (`P105`/`P106`'s own point).

## A design correction caught before trusting the first result

First attempt swept `eps(k;Λ)` over the wide `x` grid, exactly as
`P105`/`P106` did. **Every branch, every `k`, came back
`NOT-CONVERGED`** — `eps` declined smoothly and almost *identically*
(`~11%` per step) regardless of `k` or `Λ`. That near-universal decay
pattern was the tell: something structural, not physical, was being
measured. Checked before writing any verdict: `G_growth` queried
directly at the same points **saturates cleanly** (e.g. `Λ=1e-15, k=1`:
`1.04638 → 1.05016 → 1.05083 → 1.05101 → 1.05107 → 1.05107`,
`0.0008%` final-step change).

**Why:** once `Λ` dominates, matter perturbation growth *freezes*
(matter dilutes away — nothing left to grow), so `G_growth` (the
coupled-vs-uncoupled ratio) stops accumulating and settles to a constant
`G_∞`. But `eps := ln(G)/ln(a2/a1)` divides a *bounded* numerator by an
*unbounded, ever-growing* denominator — it is mathematically guaranteed
to decay toward zero once `G` saturates, regardless of any `Λ`-dependence
question. This isn't a new finding — it's exactly the condition
`FINDING_P76`'s own Part G named for when `eps` is the wrong tool: *"IF
the force induces a persistent rate shift, [G] keeps rising with the
window."* `eps` was built for that regime (pure matter domination, `Λ`
never existing, `G` never stopping). Once `Λ` dominates and growth
freezes, that condition fails, and `G` itself becomes the well-defined
quantity. Corrected: convergence checked on `G_growth`, `eps` reported
alongside with its necessary decay explained, not scored.

## Results — `G_growth`, per-branch T-convergence (`x=50→100`, `<2%`)

All 4 full-reach branches converge cleanly at all 3 `k` — final-step
changes between `0.0001%` and `0.0069%`, far inside the `2%` threshold
`P76` itself used.

| `k` | converged `G_∞` range | relative spread |
|---|---|---|
| `0.1` | `[0.996876, 1.002239]` | `0.54%` |
| `1.0` | `[1.050046, 1.051074]` | `0.10%` |
| `10.0` | `[1.095357, 1.095773]` | `0.04%` |

---

## Verdict — **`CONVERGES-CONFIRMED` at every tested `k`, including `k=0.1`**

All 4 full-reach branches individually T-converge on `G_growth`, and the
converged `G_∞` values agree to well within the `5%` threshold at **every
`k`** — for the first time, `k=0.1` resolves cleanly too, closing the
question `FINDING_P105`/`P106` left open. The completion's growth
observable, evaluated at a genuinely `P76`-comparable asymptotic reach,
is `Λ`-independent here. This is the strongest form of M1 this arc has
produced — a *converged* result, not a snapshot.

### Not established

- Anything about the two limited-reach branches (`2e-17`, `1e-16`) beyond
  what was reported for them — not pushed further within `T_END=1e8`.
- That extending `T_END` past `1e8` would leave the picture unchanged for
  the limited-reach branches — not attempted, given overflow risk for the
  large-`Λ` branches already near float64 limits.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
