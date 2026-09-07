# Decision — H1b: WHIM filament thermal energy vs cluster mass bias

**Date:** 2026-09-07
**Verdict:** **PARKED** — `BLOCKED-INFRASTRUCTURE`. **The test never ran.**
**Parked record:** `parked/H1b-whim-thermal-mass-bias.md`
**Status check behind it:** `docs/159`

---

## Why this file exists

It was missing. From 2026-07-17 until today this folder contained a
`claim.md` and an `estimand.md` and nothing else — no controls, no
metrics, no verdict. From the outside that is indistinguishable from work
in progress, and it stayed that way for **seven weeks** while being, per
`NR-014`'s own addendum, *"the sole remaining real test of H1."*

This file closes that gap. It records a **park**, not a result.

## Verdict, stated so it cannot be misread

**No data was produced. Nothing was measured. Neither pre-registered
criterion was evaluated.**

Per the Substrate Gate's hard rule, `BLOCKED-INFRASTRUCTURE` is a third
outcome, distinct from PROMOTE/REPEAT/REJECT, and is **never evidence
against the claim**. This folder must not be cited as bearing on H1 in
either direction.

## What was pre-registered and remains valid

| field | value |
|---|---|
| L0 (EstimandOps) | predictive — does `E_WHIM` predict `delta_M`? |
| KILL criterion | `r < 0.15` **AND** `p > 0.20` |
| PROMOTE criterion | `r > 0.30` **AND** `p < 0.10` |
| Confounders named in advance | cluster dynamical state; mass scaling |
| Discriminator | partial correlation controlling `M_true` **and** dynamical state |

Set before any data was seen. **Revival needs execution only — no
redesign, no re-registration.**

## The blocker

`IllustrisTNG-300` (snapshot 67 at `z≈0.2`, or 99 at `z=0`) via
`https://www.tng-project.org/api/TNG300-1/`. Registration submitted
**2026-07-01**, still pending at the last verified check (2026-08-26).
**68 days** at the time of parking.

Two bypasses were checked in July and are dead, each supplying exactly one
of the two halves the test needs: Barnes et al. 2020 (arXiv:2001.11508)
has `b_HSE` but zero WHIM data; Vladutescu-Zopp et al. 2025
(arXiv:2506.18459) has a WHIM proxy for 138 TNG clusters but states
verbatim *"we do not discuss hydrostatic masses."*

## Revival Condition

Any one of the three listed in `parked/H1b-whim-thermal-mass-bias.md`.
The cheapest by far is the first: **one login by the TNG account holder**
settles whether access was granted at some point and nobody noticed.

## Pre-condition on revival — run Step 4a BEFORE the test, not after

Flagged 2026-09-07 by `hooks/ceiling_gate_guard`. H1b's thresholds were
frozen **2026-07-17**; the Floor-Ceiling Interval (FL Step 4a) entered the
stack at the end of August. **These criteria have never been checked
against a floor.**

That is not hypothetical here. The precedent the hook cites is an H1
criterion that a null model containing no mechanism at all **exceeded
about sevenfold**. And this specific dataset has already shown it: in
`NR-010` the raw correlation was `r=0.021`, yet controlling `M_WL` produced
a partial `r=-0.701` from structure alone. A partial correlation of that
size arising without the tested mechanism is exactly the floor problem.

So `PROMOTE: r > 0.30` may or may not be passable by a construction with no
WHIM physics in it. Nobody has checked.

**On revival, before running the test:**

| end | construction | question |
|---|---|---|
| **floor** | same pipeline, WHIM signal removed — shuffle `E_WHIM` across clusters, or predict `delta_M` from `M_true` and dynamical state alone | how much correlation does the design give for free? |
| **ceiling** | a performer with privileged access to the simulation's own `M_true - M_HE` decomposition | how much is attainable at all? |

Then report `efficiency = (observed - floor) / (ceiling - floor)`.

Stop conditions, resolved **before** any result is generated:

- `PROMOTE` threshold `<=` floor -> **CRITERION_INVALID**, rewrite `claim.md`
- ceiling `<` `PROMOTE` threshold -> **TASK_INFEASIBLE**
- ceiling `~=` floor -> **NO_HEADROOM**

None of the three is evidence against H1 — they say the experiment could
not have been informative as designed.

## Step 4a RESULT — run 2026-09-07, `scripts/p210_h1b_floor_check.py`

The noise half of the floor check has now been done. It does **not** clear
H1b, but it settles one of the two ways the criterion could be invalid,
and it turned up two design defects that are fixable before any data
arrives.

### Noise floor: CLEAN

95th percentile of the null partial correlation vs the PROMOTE threshold,
Monte Carlo (20k trials) agreeing with `1/sqrt(N-k-3)` to under 5 percent:

| N | null SD | 95th pct of null abs(r) | PROMOTE 0.30 sits at | reachable by noise? |
|---|---|---|---|---|
| 100 | 0.1026 | 0.197 | 2.9 sigma | no |
| 138 | 0.0867 | 0.166 | 3.5 sigma | no |
| 200 | 0.0716 | 0.138 | 4.2 sigma | no |
| 300 | 0.0582 | 0.115 | 5.2 sigma | no |

A random predictor does not reach `r > 0.30` at any planned sample size.
The `PROMOTE` bar is not passable by chance — the H1 failure the ceiling
gate warns about (a null model beating the threshold ~7x) does **not**
repeat here on the noise axis.

### Defect 1 — `KILL` has a dead band, and it widens with N

`KILL` requires `r < 0.15` **AND** `p > 0.20`. Those two clauses do not
fire together. The `r` giving exactly `p = 0.20` is:

| N | r at p=0.20 | KILL's r-clause | dead band where KILL cannot fire |
|---|---|---|---|
| 100 | 0.1306 | 0.15 | `0.131 <= r < 0.15` |
| 138 | 0.1106 | 0.15 | `0.111 <= r < 0.15` |
| 200 | 0.0915 | 0.15 | `0.092 <= r < 0.15` |
| 300 | 0.0744 | 0.15 | `0.074 <= r < 0.15` |

A result landing in that band satisfies the r-clause, fails the p-clause,
and is therefore neither killed nor promoted. **The pre-registration does
not say what happens to it**, and the larger the sample, the wider the
band — the opposite of the intended behaviour.

### Defect 2 — the undefined middle

Nothing at all is specified for `0.15 <= r <= 0.30`. At these sample sizes
that is roughly 1.5 to 3 sigma wide: precisely where a real but modest
effect would land. Combined with defect 1, the criterion is only decisive
at the two extremes.

(Minor, harmless: `PROMOTE`'s `p < 0.10` clause is redundant — any
`r > 0.30` already has `p` far below it at every planned N. It reads like
a second safeguard and is not one.)

### Still NOT cleared: the structural floor

This check used random predictors. It says nothing about a **WHIM-free but
structurally correlated** predictor — which is exactly what bit before:
`NR-010` went from raw `r = 0.021` to partial `r = -0.701` once `M_WL` was
controlled, purely from covariance structure. That floor needs the data
(shuffle `E_WHIM` preserving its marginal, or predict `delta_M` from
`M_true` and dynamical state alone) and remains open.

### Consequence for revival

Fix the bands **before** running, not after seeing a result — otherwise
the fix is unfalsifiable. Concretely: make `KILL` a single clause
(`p > 0.20` alone, or `r` below the N-dependent value above), and state
explicitly what an outcome in `0.15-0.30` means. Then run the structural
floor as the first thing the data touches.

## Standing caveat

The July bypass survey is two months stale. A refresh on 2026-09-07 could
not run (arXiv MCP timed out twice; Semantic Scholar rate-limited). That
is a failure to check, **not** a finding that no new dataset exists.

---

*PARKED — no result. `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
· NO_AUTHOR_ERROR`*
