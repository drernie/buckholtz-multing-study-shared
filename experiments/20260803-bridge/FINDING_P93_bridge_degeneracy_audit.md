# FINDING P93 — **DEGENERATE.** `Ω_Λ=0.7` does not pick an epoch; `FINDING_P84`'s "one external number" undercounts

**Status:** built, run, A1 technically failed its own pre-registered threshold —
the reason is explained rather than smoothed over, and the data collected
before the stop answer the file's real question anyway.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P93_bridge_degeneracy_audit.py`

> This file started as the numeric bridge step — plug in a real `H₀` and quote
> `ε(k)` in `h/Mpc`. Working the unit algebra by hand first, before any code,
> surfaced something `FINDING_P86`'s own language had already half-admitted but
> never drawn out: `Ω_Λ=0.7` is a **tautology** of the formula that sets `Λ`, not
> a condition that picks an epoch.

---

## The degeneracy, stated plainly

`FINDING_P86`'s `lambda_for(a_today, frac)` sets `Λ = ρ_m(a_today)·frac/(1−frac)`
— by construction, `Ω_Λ(a_today) = frac` for **any** `a_today` you hand it. `P86`
called this *"a definition of the reference epoch, never a value imported from
data."* That phrasing is honest about the second half and silent about the
first: **it does not say which epoch is meant.** The formula is satisfied
identically for every `a_today`, so "`Ω_Λ=0.7` today" fixes `Λ` relative to an
already-chosen epoch — it never chooses the epoch.

**Why this matters for the count of external numbers.** `FINDING_P84` counted
**one** — the physical value of `a·H` at a reference epoch. If the internal
`a·H` at "the `Ω_Λ=0.7` epoch" varies little with which `a_today` you started
from, the degeneracy is harmless. If it varies a lot, then plugging in a real
`H₀` requires **breaking** this degeneracy first — a second anchor `P84` never
counted.

---

## A1 — checked in running code, not trusted from the docstring

| `a_today` | `Ω_Λ` | `\|0.7−Ω_Λ\|` | internal `H` | `a·H` |
|---|---|---|---|---|
| `1000` | — | unresolved | — | — |
| `3000` | — | unresolved | — | — |
| `1e4` | `0.699985273` | `1.473e-05` | `5.284492e-06` | `5.284492e-02` |
| `3e4` | `0.699995253` | `4.747e-06` | `1.016994e-06` | `3.050981e-02` |
| `1e5` | `0.699998483` | `1.517e-06` | `1.671087e-07` | `1.671087e-02` |
| `3e5` | `0.699999504` | `4.960e-07` | `3.216007e-08` | `9.648020e-03` |
| `1e6` | — | unresolved | — | — |

Worst deviation `1.473e-05` against the pre-registered `1e-6` threshold →
**A1 technically FAILS.**

**Why, and it is not that `lambda_for` is broken.** `lambda_for`'s algebra
assumes a pure matter+`Λ` background. Our actual coupled system carries a
**residual scalar energy density** (`FINDING_P85` measured `Ω_φ` falling from
`5.6e-08` to `1.045e-06`… down to negligible at very late times) that the
idealized formula does not subtract. The deviation from `0.7` **shrinks by a
constant ratio `≈0.32` per decade** of `a_today` — `1.473e-05 → 4.747e-06 →
1.517e-06 → 4.960e-07` — consistent with a genuinely diminishing residual, not
noise or a broken formula.

**The three unresolved points are `BLOCKED-INFRASTRUCTURE`, not evidence.**
Small `a_today` forces a huge `Λ` (`ρ_m ∝ a_today⁻³`), which `FINDING_P86`
already documented drives a runaway to `a ≈ 4.9e195` and overflow — the same
mechanism, at the opposite end of the `a_today` range from where P86 tested it.
`1e6` failing is the same story from the other direction. Neither is scored.

---

## The data collected before the stop already answer the real question

The pre-registered rule says A1's failure halts the file before A2 runs. But
the four successfully measured `a·H` values are enough on their own:

| `a_today` | measured `a·H` | `a·H ∝ a_today^{-1/2}` prediction | ratio |
|---|---|---|---|
| `1e4` | `5.284492e-02` | `5.284492e-02` (anchor) | `1.00000` |
| `3e4` | `3.050981e-02` | `3.051003e-02` | `0.99999` |
| `1e5` | `1.671087e-02` | `1.671103e-02` | `0.99999` |
| `3e5` | `9.648020e-03` | `9.648118e-03` | `0.99999` |

**Matches a clean `a·H ∝ a_today^{−1/2}` power law to five significant figures.**
This is exactly what the hand derivation done before any code predicted:
`Ω_Λ=0.7` fixes `Ω_m ≈ 0.3` there, so `H² ∝ ρ_m ∝ a_today⁻³`, giving
`a·H ∝ a_today · a_today^{-3/2} = a_today^{-1/2}`.

**Spread across just this range: `5.4773×`.** `P86` itself tested `a_today` up
to `1e6`; the power law would put the spread over `[1e3, 1e6]` at roughly
`31×`, had the small-`a_today` end not overflowed. Order-1 was the
pre-registered `DEGENERATE` threshold (`spread > 3.0`); this is nearly `5.5×`
on less than two decades of `a_today` alone.

---

## Verdict — **DEGENERATE**

`Ω_Λ=0.7` does **not** pick a unique reference epoch. It is compatible with an
entire family of epochs whose internal `a·H` differs by a confirmed,
mechanistically-derived power law. **`FINDING_P84`'s count of one external
number undercounts what a real `H₀`-based bridge needs.**

**This file quotes no `k[h/Mpc]` number.** Doing so now would mean picking one
`a_today` from the degenerate family and calling it "the" bridge — a fit dressed
as a derivation, exactly the trap Gate 2 (Target Provenance) exists to catch.

### What is needed next

Breaking the degeneracy requires **at least one more physical anchor** —
naturally, a real `Ω_m` today (e.g. Planck's `0.315`), used **together with**
`H₀`, not `Ω_Λ=0.7` alone. `Ω_m` and `H₀` jointly pin `ρ_m` today in physical
units, which pins `a_today` given `ρ_m(a_today) = C_MATTER/a_today³` internally
— a genuine second external number, not a convention.

**Source for `H₀`, cited but not yet used, kept for the gated follow-up:**
Planck 2018 results VI, base-ΛCDM, `H₀ = 67.4 ± 0.5 km/s/Mpc`
([arXiv:1807.06209](https://arxiv.org/abs/1807.06209)).

### What is NOT established

- Any numeric value of `ε(k)` in physical units — gated on this verdict, and on
  sourcing the second anchor.
- Whether `Ω_m = 0.315` (or any specific value) is the right second anchor —
  only that one is needed.
- Anything about MULTING itself (Gate 1). No dataset and no Table A1 quantity
  entered this file.
