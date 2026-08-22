# FINDING P89 — **F-CONFIRMED.** `f` survives the second implementation too

**Status:** built, run, outlier probed, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P89_f_through_the_reconstruction.py`, `p89_outlier_probe.py`

> `FINDING_P88` met Perelman condition 5 for `ε(k)` **and for nothing else**, and
> registered a falsifiable prediction naming `f` as the cheapest next target —
> *"if a second implementation of `f` instead **disagrees** above `1e-4`, then the
> agreement demonstrated there is specific to `ε(k)` and does not license
> treating the shared solver as verified."*
>
> This is that test. The prediction survives.

---

## The design decision that decides whether this gate measures anything

`f ≈ 1.046`. Roughly **96 % of it is the matter-domination growing mode** `δ ∝ a`,
which both implementations reproduce trivially — P88's own lock mass already got
`f = 1` to `1.004e-06` with the coupling off. A relative comparison **on `f`**
would therefore be dominated by the part that *cannot fail*, and would report a
small number no matter what the coupling sector did.

So the pre-registered criterion is on

```
Δf := f(ĝ=1) − f(ĝ=0)
```

where the coupling is the whole signal. The `rel(f)` column is printed beside it
purely for scale — and it comes out **two orders of magnitude smaller**, which is
exactly the inflation the wrong criterion would have produced.

## What is independent, and what deliberately is not

The **solver** is P88's (`N = ln a`, `a` as the axis, `H` from the Friedmann
constraint algebraically, 8 state variables, `DOP853`) — measured to share no
computational code with P76, not merely asserted. The **difference operator** is
new here and differs structurally too: P82 steps `ln t` and divides by the
measured `d ln a`; P89 differences in `N = ln a` **directly**, so one difference
and no division. Two things differ at once relative to P82 — that is deliberate,
and if a discrepancy appeared, isolating which ingredient carried it would be a
separate step.

---

## Controls

| | check | result |
|---|---|---|
| **L1** | external lock mass `f → 1` where `Ω_φ` small | worst `2.418e-05` vs `1e-3` → **PASSES** |
| **L2a** | discrimination — the wrong quantity must land far from `f` | min separation `3.0000 > 2` → **PASSES** |
| **L2b** | identity `f_raw − f = −3 + d ln(1−ĝφ̄)/d ln a`, coupling factor **live** | worst `1.894e-11 < 1e-6` → **PASSES** |
| **L3** | Euler sign flipped in the reconstruction only | `12.5 %` → **PASSES** |

`Ω_φ` is printed beside every `f` because P82's trap applies unchanged: our
background is **not** pure matter domination, so an `f` below 1 could be *correct
physics* wearing the costume of a broken pipeline. The assertion is made only
where `Ω_φ < 1e-3` (measured `3.67e-05 / 3.56e-06 / 8.84e-07`).

### L2 failed first, by its own construction — and the failure found something in P82

The first L2 asserted `f_raw − f = −3` **exactly**, and failed at `5.123e-03`.
That target was inherited from P82. But `Δ_m = δ·ρ_phys` with
`ρ_phys = (C/a³)(1 − ĝφ̄)`, so the exact statement is

```
f_raw − f = −3 + d ln(1 − ĝφ̄) / d ln a
```

and the second term **vanishes identically at `ĝ=0`**. Measured directly, it
accounts for the observed offsets to `1.8e-11`:

| `a` | observed offset | `d ln(1−φ̄)/d ln a` | match |
|---|---|---|---|
| `1e4` | `−0.005122628` | `−0.005122628` | `1.790e-11` |
| `1e5` | `−0.001341194` | `−0.001341194` | `2.654e-12` |
| `4e5` | `+0.000016473` | `+0.000016473` | `9.574e-13` |

**The reconstruction was right and the control was wrong** — the sixth control
this session to fail by its own construction.

**And this is a fact about P82:** its negative control reported *exactly*
`3.000000` because it was run **at `ĝ=0` only**, where the coupling factor is
identically 1. It did its job — distinguishing the contrast from the raw
perturbation — but **the coupled background was never exercised by it.** The
replacement here splits the two things the original conflated: **L2a** the
discrimination (the control's actual job) and **L2b** the identity with the
factor **live at `ĝ=1`**. Sharper than P82's, not weaker: the `ĝ=1` row *can* fail.

---

## Part B — the deliverable

`Δf`, reconstruction vs P82, at **matched `a`**:

| `k` | `a=1e4` | `a=1e5` | `a=4e5` |
|---|---|---|---|
| `3` | `1.705e-06` | **`6.690e-05`** | `4.639e-06` |
| `10` | `6.752e-08` | `3.254e-06` | `1.875e-07` |
| `30` | `1.273e-07` | `8.541e-07` | `2.439e-07` |

**Why matched `a` and not P82's matched `t`:** P76 built `t_of_a` precisely
because two runs with different couplings sit at *different* `a` at the same `t`,
so comparing at equal `t` imports a background artifact into a perturbation
comparison. Had the reconstruction been compared against P82's published
equal-`t` values, a convention difference would have been indistinguishable from
an implementation disagreement — the species of error `FINDING_P78`'s A3 made.

**Part D measured that convention difference** rather than assuming it small:
`5.476e-07 / 4.532e-08 / 1.139e-08` at `k = 3 / 10 / 30`. Any future quote of `Δf`
should still say which convention it is, but at this precision it is not the
dominant term.

---

## The verdict scraped, so the scrape was probed before being quoted

`6.690e-05` against a `1e-4` threshold is **not a margin**, and it is an outlier —
neighbours sit at `1e-6…1e-7`. The structure was not noise either: `a=1e5` is the
worst point at **every** `k`, and the discrepancy grows sharply as `k` falls.
Part D had already ruled out the evaluation convention (two orders too small).

`p89_outlier_probe.py` refined **both** difference steps together, pre-registering
`≥10×` drop → scheme artifact, `<2×` → real implementation difference:

| `h` (recon) | `dlnt` (P82) | `Δf` recon | `Δf` P82 | rel |
|---|---|---|---|---|
| `1e-3` | `1e-2` | `0.040407513509` | `0.040227793218` | `4.468e-03` |
| `1e-4` | `1e-3` | `0.040413639418` | `0.040410936026` | `6.690e-05` |
| `1e-5` | `1e-4` | `0.040413701313` | `0.040413674161` | `6.718e-07` |
| `1e-6` | `1e-5` | `0.040413701859` | `0.040413701680` | `4.422e-09` |

Each `10×` refinement drops the difference by roughly `100×` — **second-order
convergence**, the signature of central-difference truncation on both sides, not
of an implementation difference. Total `1.01e+06×`. → **STEP-LIMITED.**

**So the worst point is truncation.** At matched refinement the two codes agree
there to `4.422e-09` — four orders below the threshold. The pre-registered verdict
still rests on the **original** table (`6.690e-05 < 1e-4`); the refinement is
post-hoc and is reported as an explanation of that value, not as a substitute for it.

### The diagnostic that refuted its own story

`Δf` subtracts two numbers near 1 to get one near `0.04`, so cancellation was the
obvious suspect. The condition number `|f|/|Δf|` was printed to check it:

| `k` | `a=1e4` | `a=1e5` | `a=4e5` |
|---|---|---|---|
| `3` | `25.57` | `25.74` | `25.95` |
| `10` | `22.83` | `22.82` | `22.84` |
| `30` | `22.42` | `22.39` | `22.40` |

It varies by `14 %` across the whole grid and **does not peak at the outlier** —
`25.74` sits *between* its two neighbours. Cancellation is **not** the mechanism.
The diagnostic was built to be able to support that story and it declined to.

---

## Verdict

**F-CONFIRMED.** Worst relative difference on `Δf` = `6.690e-05` < `1e-4`, and that
worst value is demonstrably truncation, converging to `4.422e-09` under refinement.

**P88's registered prediction survives its first real test: the agreement it
demonstrated was not specific to `ε(k)`.** Perelman condition 5 now extends to `f`
— at the **same** rung, *independently-written code*, and no higher.

### Not established

- **Nothing above that rung.** The same person wrote both implementations; a
  different **model**, a **blind replication**, and a **new physical experiment**
  all remain absent. **Strong**, not *Very strong*.
- **That the shared equations are right.** A reconstruction tests the
  implementation, never the specification. Two faithful solutions of the same
  wrong equations agree beautifully.
- `μ_tot == 1`, the viability boundary, the scaling group — **untouched**, each
  still needing its own reconstruction.
- Nothing observational. `NO_BRIDGE_FITTING` untouched. Gate 1 holds — nothing
  here transfers to MULTING.
