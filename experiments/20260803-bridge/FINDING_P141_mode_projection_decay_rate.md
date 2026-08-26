# FINDING P141 — the mode-projection hypothesis is REFUTED: convergence
# exponent q(k) does not increase monotonically with k

**Date:** 2026-08-26
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Verdict:** `MODE-PROJECTION-REFUTED`, positive-control-tested
**Origin:** the decisive test named by `docs/148` (IC-sensitivity
inverse-problem synthesis, bottleneck 4) for its own sole surviving
mechanism candidate

---

## 1. Why this file

`docs/148` derived mode-projection/two-branch as the one mechanism class
satisfying all 5 already-established constraints (C1-C5, from `P79`/
`P135`/`P136`/`P138`/`P139`), with a genuinely new prediction: if the IC
lever sets the projection weight onto a fast- vs slow-decaying mode, and
scale-dependence comes from the decay-rate *separation* itself depending
on `k`, then `eps(k)`'s own convergence rate toward its late-time
asymptote — measured as the exponent `q` in `eps(N) = eps_∞ + C·N^(-q)`
— should increase monotonically with `k` (fast convergence/large `q` at
high `k`, where IC-sensitivity washes out; slow convergence/small `q` at
low `k`, where it persists).

## 2. Result

| k | q (fit, all 4 windows) | q (fit, latest 3 windows) | trustworthy? |
|---|---|---|---|
| 1 | 0.0285 | 0.4872 | **No** — fits disagree by >10× |
| 2 | 0.7662 | 0.8793 | Yes |
| 3 | 0.5219 | 0.7401 | Yes |
| 10 | 0.4101 | 0.7378 | Yes |

**Positive control**: recovered a known synthetic `q=1.5` to 13 decimal
places (`q_fit=1.4999999999999993`) from noise-free data — the fitting
machinery itself is trustworthy.

`k=1`'s own two fits disagree by more than an order of magnitude
(`0.03` vs `0.49`) — the power-law convergence regime has not been
reached there within the tested window range, so it is excluded from
the monotonicity judgment rather than trusted on either fit.

**Among the 3 trustworthy points, `q(k)` is 0.879 → 0.740 → 0.738 for
`k=2,3,10` — DECREASING then flattening, the opposite of the predicted
direction, and not monotonic in the required sense either way.**

## 3. Verdict

**`MODE-PROJECTION-REFUTED`.** The convergence-rate exponent does not
track the already-established pattern of where IC-sensitivity persists
vs. washes out. This is the 5th mechanism candidate for bottleneck 4
tested and excluded this session (after `P135` pole, `P136`
early-transient, `P138` horizon-crossing DESIGN-LIMITED, `P139` gauge
WEAKENED) — but unlike the earlier four, this one was reached through
`docs/148`'s own structured inverse-problem synthesis (deriving the
candidate FROM the constraints, not guessing it), and its own
pre-registered decisive test cleanly refutes it rather than leaving it
design-limited or merely weakened.

## 4. What this does NOT establish

1. **That no mode-decomposition mechanism exists** — only that THIS
   specific proxy (convergence rate of `eps`'s own already-measured
   windows) does not show the predicted pattern. A direct two-exponential
   decomposition of `contrast(t)` itself (harder, more error-prone, not
   attempted here) could in principle behave differently — named as a
   possible future refinement, not pursued.
2. **`k=1`'s own true convergence behavior** — the fit there is
   genuinely untrustworthy within the tested window range, not silently
   forced into either direction.
3. **IC-lever-dependence of `q(k)`** — only the canonical lever was
   tested; the secondary check `docs/148` named was not required for
   this GO/STOP decision and was not run.
4. **Anything observational.** Internal units; `NO_BRIDGE_FITTING` in
   force.
5. **Anything about MULTING itself** (Gate 1). Both completions are
   ours.

## 5. Controls

- **Positive control**: known synthetic `q=1.5` recovered to `1.4999999999999993`
  from noise-free data — fitting machinery trustworthy.
- **Cross-check**: full-window vs. latest-3-window fits compared per
  `k`; disagreement at `k=1` reported honestly, not averaged away.
- **Reuse, not re-derive**: `run`/`eps` imported directly from `P79`'s
  own module.
