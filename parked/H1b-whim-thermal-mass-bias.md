# H1b — WHIM filament thermal energy vs cluster mass bias

**Parked:** 2026-09-07
**Verdict:** **PARKED — `BLOCKED-INFRASTRUCTURE`, not archived on merit.**
**Source experiment:** `experiments/20260701-h1b-whim-thermal-mass-bias/`
(`claim.md`, `estimand.md`, both 2026-07-17; `decision.md` added 2026-09-07)
**Status check that produced this:** `docs/159`

---

## Read this first — what parking does and does not mean here

Every other entry in `parked/` was archived on a *scientific* judgement:
valid but deprioritized, method missing, circularity relocated. **This one
is different.** H1b was never run. It is parked for bookkeeping only —
so an experiment folder containing a `claim.md` and no result stops
looking like work in progress.

Per the Substrate Gate's own hard rule, **`BLOCKED-INFRASTRUCTURE` is
never evidence against the claim.** Nothing in this file may be cited as
weighing against H1, in either direction.

## Why it matters more than its parked status suggests

`NR-014`'s own addendum calls H1b *"the sole remaining real test of H1."*

Every H1 arm that was killed — H1a (`NR-010`), H1c (`NR-012`), H1d
(`NR-011`), H1e (`NR-014`) — used the **cluster-interior ICM**
(`T > 10⁷ K`, inside `R_200`). H1b is the only arm using the **WHIM**
(`T = 10⁵–10⁷ K`, `R_200 < r < 3R_200`), which its own `claim.md` calls
*"the actual filament gas TJB refers to."*

So the arm closest to the actual claim is the one that never executed.
Read as a bare list, the H1 programme looks finished; it is not.

## What is already done, and needs no rework on revival

The design is complete and was pre-registered before any data:

- **KILL:** `r < 0.15` **AND** `p > 0.20`
- **PROMOTE:** `r > 0.30` **AND** `p < 0.10`
- **Estimand:** predictive (EstimandOps L0), `E_WHIM` → `delta_M`
- **Confounders named in advance:** cluster dynamical state; mass scaling.
  Discriminator is a partial correlation controlling `M_true` **and**
  dynamical state.
- **Claim entropy** recorded, including the blocker itself as
  `N_unresolved_blockers = 1`.

**Revival cost is execution only.** No redesign, no re-registration.

## The blocker

`IllustrisTNG-300`, snapshot 67 (`z≈0.2`) or 99 (`z=0`), via
`https://www.tng-project.org/api/TNG300-1/`.
Registration submitted **2026-07-01**; still pending at the last verified
check (`docs/145`, 2026-08-26). **68 days** as of parking.

Bypasses checked in July, both dead with recorded reasons:

| option | source | why dead |
|---|---|---|
| B | Barnes et al. 2020, arXiv:2001.11508 (Mock-X) | has `b_HSE` for TNG clusters, **zero** WHIM/IGM data |
| C | Vladutescu-Zopp et al. 2025, arXiv:2506.18459 | 138 TNG clusters with a soft-X-ray WHIM proxy, but states verbatim *"we do not discuss hydrostatic masses"* |

Each has exactly one of the two halves the test needs. Neither has both.

## Revival Condition (measurable — ANY of the three)

1. **TNG-300 API access is granted.** Binary and cheap to check: one login
   by the account holder. On grant, run the pre-registered test unchanged.
2. **A published dataset pairs hydrostatic masses (or `b_HSE`) with
   WHIM/outskirts gas properties for `N > 100` clusters.** This is the
   precise gap Options B and C each half-fill. A single paper carrying
   both columns revives this immediately.
3. **A different simulation suite** with public access supplies both
   quantities at comparable resolution (e.g. any successor or mirror
   providing `M_true`, `M_HE`, and outskirts gas in `R_200–3R_200`).

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

## Bands REPAIRED 2026-09-07 — `claim.md` AMENDMENT 1

The two defects P210 found are fixed, additively and before any data
exists (`scripts/p211_h1b_criterion_repair.py`). The original criteria are
NOT rewritten; `claim.md` carries a dated AMENDMENT 1 that supersedes them
for execution.

**New rule** — one-sided 95% bounds, Fisher-z, `k = 2` controls, both
original numbers kept:

```
KILL          upper bound on r  <  0.15
PROMOTE       lower bound on r  >  0.30
INCONCLUSIVE  otherwise
```

Verified complete and disjoint over 3801 values of `r` at
`N = 100/138/200/300/500`. Dead band gone, middle defined, behaviour now
monotone in `N`.

**New binding requirement: `N >= 124`.** The repair exposed that `KILL` is
unattainable below that even for a perfectly null `r = 0` — at `N = 100`
the best achievable upper bound is `0.1672 > 0.15`. The design's own
`"N > 100"` cannot deliver a `KILL`, and a test that can only return
`PROMOTE` or `INCONCLUSIVE` is not a test of the claim.

**Deliberately left open:** how large the `KILL` bar should be is a
scientific judgement, not a statistical one. Its cost is tabulated in the
amendment (bar 0.20 -> `N >= 71`; bar 0.10 -> `N >= 274`). Not changed
unilaterally.

**Unaffected:** the structural floor. Still needs the data, still must run
first.

## Standing caveat on the July bypass search

The Option B/C survey is dated **July 2026** and is now two months stale.
A refresh was attempted on 2026-09-07 and **could not run** — arXiv MCP
timed out twice, Semantic Scholar returned a rate limit. That is a failure
to check, not a finding that nothing new exists. **Do not carry the July
conclusion forward as current** when evaluating revival condition 2.

## What this does NOT establish

1. **Nothing about whether H1 is true or false.** No data was produced.
2. **Not that the other H1 arms were wrongly killed.** `NR-010`/`011`/
   `012`/`014` stand as recorded.
3. **Not that no bypass exists** — see the standing caveat above.
4. **Nothing about MULTING** (`NO_AUTHOR_ERROR`). H1 is this project's own
   reconstruction of a testable consequence, not TJB's own text.
