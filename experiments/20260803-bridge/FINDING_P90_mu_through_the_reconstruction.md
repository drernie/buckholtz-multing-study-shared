# FINDING P90 — **M-CONFIRMED.** The identity is a property of the equations, and P74's blind spot was an artifact of where it looked

**Status:** built, run, verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P90_mu_through_the_reconstruction.py`

---

## The prediction this tests was partly my own mis-specification

`FINDING_P89` registered:

> *"`μ_tot`, being an algebraic identity among background and perturbation
> variables at a single point, should reproduce at **roundtrip precision**
> (`1e-12` or better) with **no step-refinement ladder** needed at all."*

That was written before looking at `μ_tot`'s definition, and **half of it is
vacuous.**

```
μ_tot = −(k²/a²)·ψ / (4πG(Δ_m + Δ_φ))
```

is the perturbed Einstein **(00) constraint** rearranged. It is not a number a
code computes and might get wrong — it is `1` **by construction** in any code
that solves the constraint, P76's and P88's alike. "The two implementations agree
on `μ_tot` to `1e-12`" would measure only that both satisfy a constraint each was
built to satisfy. Reporting that as cross-implementation agreement would have been
the **ninth** instance of this campaign's recurring failure.

So the vacuous ratio is not reported, and three testable things replace it.

---

## N1 — the discrimination check, run **first**

`FINDING_P74` documented that its own lock mass was **blind** to a fabricated
`+7·ĝ·ρ_A·δφ` term — residuals *identical* — and honestly **weakened its own
Part B** over it. The reason is now visible: **P74 evaluated that control at
`ĝ=0`, where the term is identically zero.**

Both directions were pre-registered, each able to fail:

| `ĝ` | `k` | clean `\|μ_tot−1\|` | fabricated `\|μ_tot−1\|` | ratio |
|---|---|---|---|---|
| `0` | `0.1` | `1.635359e-13` | `1.635359e-13` | `1` |
| `0` | `1` | `1.887379e-15` | `1.887379e-15` | `1` |
| `0` | `10` | `3.774758e-15` | `3.774758e-15` | `1` |
| `1` | `0.1` | `1.120215e-13` | `1.547128e-03` | `1.38e+10` |
| `1` | `1` | `3.108624e-15` | `1.450135e-04` | `4.66e+10` |
| `1` | `10` | `2.220446e-15` | `1.387265e-06` | `6.25e+08` |

**P74's blindness reproduced exactly** (ratio `1`, to every printed digit) **and
repaired** (amplification ≥ `6.25e+08` once the coupling is on).

**So the blind spot was never intrinsic — it was an artifact of where P74
looked.** That matters beyond bookkeeping: P74 *weakened a real conclusion* on
the strength of a control that could not have detected anything at the coupling
it was run at.

> **This is the second such control in two days.** `FINDING_P89` found the same
> shape in P82's negative control — reported *exactly* `3.000000` because it too
> ran at `ĝ=0`, where its coupling factor is identically `1`. A pattern, not a
> coincidence: **when a control is run at `ĝ=0`, every term that carries the
> coupling vanishes, and the control certifies only the uncoupled skeleton.**

## N2 — what the identity **cannot** see

A term added to `Δ_m` and **subtracted** from `Δ_φ` cancels in the total:

| `k` | `μ_tot` shift | `μ_m` shift |
|---|---|---|
| `0.1` | `0.000e+00` | `9.091e-02` |
| `1` | `0.000e+00` | `9.091e-02` |
| `10` | `0.000e+00` | `9.091e-02` |

**Honest reading of the two halves.** The `μ_m` column is *arithmetically forced* —
a `10 %` shift of `Δ_m` moves `μ_m ∝ 1/Δ_m` by exactly `1/1.1 − 1 = 0.0909`, which
is why all three `k` agree to four digits. It carries almost no information. **The
content is the other column:** `μ_tot` is blind to it at *exactly* `0.000e+00`, not
merely "small". That is the precise statement of what a `μ_tot` check certifies —
and what it does not.

---

## Part A — the identity under an **independent** discretization

P88's solver imposes the **background** Friedmann constraint algebraically but
**evolves** the perturbations; nothing in it forces the perturbed (00) constraint
to stay satisfied. The target `1` is **external** — the Einstein equations — and
owes nothing to P76.

| `k` | `a=1000` | `a=1e4` | `a=5e4` |
|---|---|---|---|
| `0.1` | `5.2811e-12` | `5.0304e-13` | `1.1202e-13` |
| `1` | `8.3267e-14` | `6.2172e-15` | `3.1086e-15` |
| `10` | `4.4409e-16` | `4.4409e-15` | `2.2204e-15` |

Worst `5.2811e-12` against P74's stated `1e-8` → **the identity HOLDS.** It is a
property of the equations, not of P76's discretization.

*(P74 reported `9.07e-11` for its own solver. The two are **not** directly
comparable — different point grids — so no claim is made that one solver is
better. Observed, and left there.)*

**Left unexplained:** the residual worsens toward small `k` and small `a` — `μ_tot`
carries `k²` in the numerator, so both numerator and denominator shrink together
and conditioning degrades. **Observed, not measured** — no mechanism is narrated
for a direction merely seen (P87's lesson).

## Part B — `μ_m`, the non-trivial number

`μ_m = −(k²/a²)·ψ / (4πG·Δ_m)` uses the **matter** comoving density alone, so it
is pinned to nothing and genuinely differs from `1`. Compared against P74's own
`mu_of` at **matched `a`**:

| `k` | `a=1000` | `a=1e4` | `a=5e4` |
|---|---|---|---|
| `0.1` | `1.773e-11` | `1.287e-12` | `9.015e-14` |
| `1` | `5.906e-13` | `3.311e-13` | `3.002e-13` |
| `10` | `2.220e-14` | `1.776e-14` | `7.683e-14` |

Worst `1.773e-11`, seven orders below the `1e-4` threshold.

## Part C — the surviving half of the prediction

`ε` and `f` both needed a differencing step, and both showed a refinement ladder
spanning `~1e6`. `μ` has **no difference operator at all** — it is pointwise in the
state vector — so the only knob is solver `rtol`:

| recon `rtol` | `μ_m` recon | relative vs P74 |
|---|---|---|
| `1e-08` | `0.999990048051405` | `8.510e-12` |
| `1e-10` | `0.999990048060266` | `3.517e-13` |
| `1e-12` | `0.999990048060202` | `2.875e-13` |

Spread `29.6×` across four orders of `rtol` — and the last two points differ by
only `1.2×`, i.e. **the floor has been reached**. Against `1e6×` for the
differencing ladders, **no ladder is needed**: the agreement is already at `1e-11`
at the *loosest* tolerance tried.

### Scoring my own prediction honestly

- **Qualitative half — "no step-refinement ladder needed" — CONFIRMED.**
- **Numeric half — "`1e-12` or better" — MISSED by one to two orders.** The
  measured worst values are `5.3e-12` (identity) and `1.8e-11` (`μ_m`). Both are
  roundoff-scale and neither is a problem, but the prediction named `1e-12` and
  the measurement is not `1e-12`. Recorded as missed rather than rounded in my
  favour.
- **Structural half — "`μ_tot` reproduces" — WITHDRAWN AS VACUOUS**, for the
  reason given at the top.

---

## Verdict

**M-CONFIRMED.** Identity `5.281e-12 < 1e-8` under an independent discretization;
`μ_m` agrees with P74 to `1.773e-11 < 1e-4`; both negative controls behaved as
pre-registered, including the one that had to *fail* in a predicted direction.

**Perelman condition 5 now covers `ε(k)`, `f`, and `μ`** — all three at the
**independently-written code** rung and no higher.

### What the identity does not certify

Any error that **cancels between the matter and scalar branches**. `μ_tot` is
blind to it by construction — measured at exactly `0.000e+00`, not assumed — and
only `μ_m` sees it.

### Not established

- **Nothing above that rung.** Same person wrote both implementations; a different
  **model**, a **blind replication**, and a **new physical experiment** all remain
  absent. **Strong**, not *Very strong*.
- **That the shared equations are right.** A reconstruction tests the
  implementation, never the specification.
- **The viability boundary and the scaling group** — untouched. The boundary is
  the remaining registered target, and P89 predicted it should reproduce **only**
  to its bisection tolerance (`≈1e-4`) and **not better**.
- Nothing observational. `NO_BRIDGE_FITTING` untouched. Gate 1 holds.
