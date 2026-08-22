# FINDING P92 — **O-SCALES + C-DIVERGES.** P81's sampled boundary does not converge, and the campaign's default `n_probe` was lucky, not accurate

**Status:** built, run (two background instances accidentally raced and were
reconciled to one completed run), verdict against pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifacts:** `P92_grid_sensitivity_vs_oscillation_count.py`,
`p92_which_clause_probe.py`

> Registered by `FINDING_P91` to test whether its `λ=0.1` grid-sensitivity
> (`1.774e-04` movement at 300 probes) scales with **oscillation count** rather
> than with `λ` as such. It does. But the convergence control this file also
> carried — because "the sensitivity scales" and "the two predicates agree" are
> different questions — returned the more consequential answer.

---

## Part A + B — four boundaries, none guessed

No bracket assumed anywhere; each located by a geometric scan first.
`λ=1` and `λ=10` had never been located in this campaign before this file.

| `λ` | `ĝ_crit` (event-located exact limit) | turning points at the boundary |
|---|---|---|
| `0` | `0.738212214739` | `0` |
| `0.1` | `2.751764836585` | `216` |
| `1` | `3.518052822000` | `332` |
| `10` | `4.733977969229` | `562` |

`λ=0` has **exactly zero** turning points — an independent corroboration of
diamond D1's monotonicity claim, now measured on the boundary trajectory itself
rather than at an interior point. The count grows sub-linearly in `λ`
(`×1.5–1.7` per decade of `λ`), which the `H_monotone` clause-probe used as
evidence its own hypothesis test was well-posed.

## Part C — the `n_probe` ladder against the exact limit

| `λ` | `n=300` | `n=1000` | `n=3000` | `n=10000` | `n=30000` | `n=100000` |
|---|---|---|---|---|---|---|
| `0` | `9.116e-12` | `9.116e-12` | `9.116e-12` | `9.116e-12` | `9.116e-12` | `9.116e-12` |
| `0.1` | `2.163e-04` | `3.090e-06` | `9.746e-12` | `3.694e-07` | `4.074e-07` | `4.136e-07` |
| `1` | `3.024e-04` | `1.415e-06` | `1.448e-11` | `1.415e-06` | `1.406e-06` | `1.415e-06` |
| `10` | `2.379e-04` | `5.578e-07` | `1.448e-07` | `9.907e-06` | `9.857e-06` | `9.925e-06` |

*(relative difference against the reconstruction's event-located flip, at each `n_probe`)*

**`λ=0` is flat at roundoff** — 9.116e-12 at every `n_probe` from 300 to 100000,
which is the correct behaviour when the sampled minimum sits exactly at the
trajectory's endpoint (D1's monotone case: no probe grid can miss it).

**Every `λ≠0` row is non-monotone**, and at every one of them **`n=3000` is the
best point on the ladder** — by a wide margin, often near machine precision
(`9.746e-12`, `1.448e-11`). Neighbouring `n_probe` values are three to five
orders worse. At `λ=1`, `n=1000` and `n=10000` return the **exact same float**,
`3.518047843884` — bitwise, verified separately.

---

## What this actually is, and why it is not "3000 is well-converged"

A non-monotone sequence that is best at one interior point and worse on both
sides is the signature of a **sampled minimum snagging a narrow feature**: the
true `min(1−ĝφ̄)` over the trajectory sits in a window of `t` narrow compared to
one oscillation period, and whether a given probe grid happens to place a point
inside that window is a matter of **alignment**, not of point count. `n=1000`
and `n=10000` returning the identical float is direct evidence of this — two
grids of very different density landing on the same feature (or missing the same
one) and producing the same bisection answer.

**This is the same shape this session has caught repeatedly** — agreement too
precise for what produced it (`P88`'s `k=30` cancellation, `P91`'s revision-1
dyadic-grid luck) — applied here to the campaign's own **default** `n_probe`
value. `3000` is not special; it is simply the point in this six-value ladder
that happened to land closest to the true dip. Nothing tested here shows it
would remain the best choice at a different `λ`, a different anchor, or a
different probe-grid density scheme (log-`t` vs linear-`N`, per `P91`).

---

## Scoring against the pre-registration

**The registered prediction — `O-SCALES`.**

| `λ` | turns | `\|3000 vs 30000\|` |
|---|---|---|
| `0` | `0` | `0.000e+00` |
| `0.1` | `216` | `4.074e-07` |
| `1` | `332` | `1.406e-06` |
| `10` | `562` | `1.000e-05` |

`λ=1` moves between `3000` and `30000` (**True**), and the sampling error grows
monotonically with the measured turning-point count (**True**). Both conditions
of the pre-registered `O-SCALES` outcome hold. **The mechanism is oscillation
sampling**, confirmed rather than merely plausible.

**The convergence control — `C-DIVERGES`.**

```
converges toward the exact limit: {0.0: True, 0.1: False, 1.0: False, 10.0: False}
```

Three edges out of four **fail** to converge as `n_probe → 100000`. Sampling is
**not** the whole difference between the two predicates at `λ≠0`, and the
residual mechanism is **unidentified** — this file does not claim to know why
`λ=0.1` settles `4.1e-07` away rather than converging to zero, only that it does.

---

## Verdict

**`O-SCALES`**, and **`C-DIVERGES`** at every oscillating `λ` tested.

### Consequence for the whole campaign, not only for this file

**`n_probe=3000` is the default every published boundary in this campaign was
computed at** — `FINDING_P81`, `FINDING_P83`'s robustness sweep,
`FINDING_P86`'s dark-energy grid, all of it. This file shows that at `3000` the
agreement with the exact predicate is the **best point on a non-monotone ladder
by three to five orders of magnitude**, at every `λ≠0` tested — not because
`3000` is well-converged, but because it happens to land near a narrow feature
the neighbouring grid sizes miss.

That does **not** mean the published boundaries are wrong. It means their
**quoted precision** — implicitly the `1e-4` bisection tolerance — does not
capture this source of error, which this file measured directly at up to
`1e-5` (`λ=10`) and which is not guaranteed to stay that small at `λ` values
this campaign has not yet probed.

### Not established

- **Why** `λ≠0` boundaries fail to converge — the residual mechanism after
  ruling out `H`-monotonicity (the clause probe) and grid-alignment (this file's
  own observation) is unidentified.
- Whether the same non-monotone snagging happens at other anchors, other
  probe-grid conventions, or `λ` values between those tested.
- Anything about the shared equations, anything observational. Gate 1 holds.
