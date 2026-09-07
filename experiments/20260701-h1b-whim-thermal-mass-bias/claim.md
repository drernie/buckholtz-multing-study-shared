# Claim — H1b: WHIM Filament Thermal Energy vs Cluster Mass Bias

## Question type (EstimandOps L0)
[x] Predictive — does E_WHIM (filament thermal energy) predict delta_M (mass bias)?

## Relationship to H1 hierarchy
H1 (broad TJB): cosmic web IGM thermal energy = 2nd gravitational source
H1a (KILLED 2026-07-01): cluster ICM thermal energy → WL-HE mass gap; r=0.021 p=0.883
H1b (THIS): WHIM gas (T=10^5-10^7 K) in R_200-3×R_200 shell → mass gap

H1b tests a MORE PHYSICALLY MOTIVATED proxy than H1a:
- H1a used ICM (inside cluster, T>10^7 K) — confirmed NULL
- H1b uses WHIM (outside cluster, T=10^5-10^7 K) — the actual filament gas TJB refers to

## Falsifiable claim
H1b: Within a simulated cluster sample (N>100), the mass gap (M_true - M_HE)
correlates POSITIVELY with the WHIM thermal energy E_WHIM in the cluster
outskirts (R_200 < r < 3×R_200, T=10^5-10^7 K), such that clusters
embedded in denser/hotter WHIM show a larger true-to-hydrostatic mass gap.

**Pre-registered KILL criterion:** r < 0.15 AND p > 0.20 → H1b KILLED
**Pre-registered PROMOTE criterion:** r > 0.30 AND p < 0.10 → H1b PROMOTED

## Source for data
[OPTION A — only remaining path] IllustrisTNG-300, snapshot 67 (z≈0.2) or 99 (z=0):
  API: https://www.tng-project.org/api/TNG300-1/
  Reference: Springel et al. 2018, MNRAS 475, 676
  Status: registration submitted 2026-07-01, pending approval as of 2026-07-04

[OPTION C — CHECKED, DEAD 2026-07-01] Vladutescu-Zopp et al. 2025, arXiv:2506.18459:
  138 TNG clusters with soft X-ray excess (WHIM proxy) + dynamical state.
  Paper states verbatim: "we do not discuss hydrostatic masses." No mass
  bias data of any kind — cannot bypass Option A. (Radial-annulus design
  and WHIM T-range definition were still useful and adopted, see estimand.md.)

[OPTION B — CHECKED, PARTIAL 2026-07-01] Barnes et al. 2020, arXiv:2001.11508
  ("Characterizing hydrostatic mass bias with Mock-X"): has b_HSE for TNG
  clusters, but confirmed ZERO WHIM/IGM data — does not bypass Option A either.

## Counterfactual Frame
In what world is H1b true?
  → Clusters embedded in denser WHIM have larger lensing-to-HE mass gap
  → The WHIM thermal energy contributes to total gravitational potential
  → At fixed M_WL: more WHIM → more "hidden" gravity → more discrepancy

Alternative worlds (that could produce r > 0.30 WITHOUT TJB mechanism):
  1. Dynamical state mediator: disturbed clusters have both more WHIM accretion
     AND larger mass bias (from non-thermal ICM pressure) — confounded
  2. Mass scaling: more massive clusters have more WHIM AND more mass bias
     due to merger history — controlled by partial correlation

→ If r > 0.30 survives partial correlation controlling for M_true AND dynamical
  state → H1b is genuinely supported (not confounded)

## Claim Entropy (Perelman)
N_unsupported_HIGH = 1 (TJB mechanism; awaiting empirical test)
N_hidden_assumptions = 2 (WHIM in R_200-3R_200 is relevant; T range 10^5-10^7 K captures TJB's component)
N_missing_negative_controls = 1 (no negative control yet)
N_ambiguous_definitions = 1 (WHIM boundary: some papers use 3R_200, some use 5R_200)
N_unresolved_blockers = 1 (TNG API access not yet set up)
Total claim_entropy = 6 → must decrease with each experimental step

## Literature context
- Three Hundred (2024): CONNECTIVITY ≠ mass bias [VERIFIED-REAL] — but this tests count, not E_WHIM
- FLAMINGO (2024): external pressure IS relevant but non-thermal motions dominate
- Vladutescu-Zopp+2025: WHIM soft X-ray excess ∝ cluster dynamical state
- H1b test: GENUINELY NOVEL — no paper tests E_WHIM(shell) vs delta_M directly

## Status
[NEEDS-DATA, WAITING_FOR_THE300_REPLY] Experiment designed. Data access pending.
Current experimental status: IN-PROGRESS (literature survey complete, including a
2026-07-17 re-check for TNG-API bypasses — see estimand.md Options D/E; data
analysis not started).
Next action: Options B/C/D (Barnes 2020, Vladutescu-Zopp 2025, TNG-Cluster public
zarr catalog) all checked and confirmed dead as technical bypasses. Option E
(The Three Hundred, arXiv:2503.05011 + arXiv:2111.01903, same 324-cluster
collaboration) is dead as a public download, but the CONFIRMED-CORRECT access
route per the collaboration's own MNRAS Data Availability Statement (Gianfagna
et al. 2023, arXiv:2211.08372: "shared on request to THE THREE HUNDRED
collaboration") — data request drafted and **SENT 2026-07-17** [USER-REPORTED]
to [third-party email redacted]. Now awaiting reply (no fixed next_check date
yet; check back in ~2-3 weeks if silent). Otherwise: await TNG API approval
(16+ days unresolved, no action pending on that front).

---

# AMENDMENT 1 — 2026-09-07 — decision bands repaired

**The original criteria above are NOT rewritten.** They stand as the
2026-07-17 record. This section supersedes them for execution, and states
why that is legitimate.

## Why amending is allowed here

Changing a decision rule *after* seeing a result is p-hacking. Changing
one *before any data exists* is repairing a broken instrument.

**H1b has produced no data.** Its folder holds `claim.md`, `estimand.md`
and `decision.md` — no metrics, no controls, no results. That is
checkable by `ls`, and it is the whole basis for this amendment being
clean. If any result had existed, the correct move would have been to
report the defective criterion alongside the result, not to fix it.

## What was wrong (`scripts/p210_h1b_floor_check.py`)

1. **`KILL` had a dead band that widened with N.** It required
   `r < 0.15` **AND** `p > 0.20`, but `p = 0.20` corresponds to
   `r = 0.131 / 0.111 / 0.092 / 0.074` at `N = 100 / 138 / 200 / 300` —
   all *below* 0.15. A result in `[that value, 0.15)` satisfied the
   r-clause, failed the p-clause, and was neither killed nor promoted.
   More data made the band **wider**, which is backwards.
2. **The middle was undefined.** Nothing was specified for
   `0.15 ≤ r ≤ 0.30`, roughly 1.5–3σ wide — precisely where a real but
   modest effect would land.
3. Minor: `PROMOTE`'s `p < 0.10` never binds at any planned `N`. It reads
   as a second safeguard and is not one.

## The repaired rule (`scripts/p211_h1b_criterion_repair.py`)

Both original numbers are kept. The hypothesis is directional
(*"correlates POSITIVELY"*), so bounds are one-sided at 95%, on the
Fisher-z scale with `se = 1/√(N−k−3)`, `k = 2` controls:

```
KILL          upper 95% one-sided bound on r   <  0.15
PROMOTE       lower 95% one-sided bound on r   >  0.30
INCONCLUSIVE  otherwise
```

Verified over a 3801-point grid of `r ∈ [−0.95, 0.95]` at
`N = 100, 138, 200, 300, 500`: **every possible result maps to exactly one
verdict; `KILL` and `PROMOTE` never overlap; there is no gap.** Behaviour
is now monotone in `N` — more data makes a decisive verdict *more*
reachable.

## A required sample size the original design never derived

| N | `KILL` reachable? | max observed `r` still giving `KILL` | min observed `r` giving `PROMOTE` |
|---|---|---|---|
| 100 | **NO** | unattainable | 0.4449 |
| 138 | yes | 0.0085 | 0.4237 |
| 200 | yes | 0.0330 | 0.4031 |
| 300 | yes | 0.0550 | 0.3845 |
| 500 | yes | 0.0770 | 0.3657 |

**`KILL` is unattainable below `N = 124`, even for a perfectly null
`r = 0`** — at `N = 100` the best achievable upper bound is `0.1672`.
The original design specified only *"N > 100"*, which **cannot deliver a
`KILL`**. A test that can only return `PROMOTE` or `INCONCLUSIVE` is not a
test of the claim.

**Binding requirement added: `N ≥ 124`.** If the eventual sample cannot
reach it, say so *before* running.

## One choice deliberately NOT made here

`KILL` at 0.15 means *"we can rule out an effect as large as `r = 0.15`."*
How large that bar should be is a judgement about what counts as "no
effect" — scientific, not statistical — and is **left open**. Its cost:

| `KILL` bar | min `N` for `KILL` |
|---|---|
| 0.10 | 274 |
| **0.15 (current)** | **124** |
| 0.20 | 71 |
| 0.25 | 47 |
| 0.30 | 34 |

Relaxing the bar to 0.20 makes `KILL` reachable at `N ≥ 71`, at the cost
of a weaker claim when it fires. **Not changed unilaterally.**

## Still open, and unaffected by this amendment

The **structural floor**. Everything above concerns the *noise* floor. A
WHIM-free but structurally correlated predictor could still clear
`PROMOTE` through covariance alone — `NR-010`, on real cluster data, went
from raw `r = 0.021` to partial `r = −0.701` once `M_WL` was controlled.
Testing that needs the data and must be the **first** thing the data
touches, before the primary result is computed.

---

# AMENDMENT 2 — 2026-09-07 — KILL bar, sign subtype, frozen null models

Additive, like AMENDMENT 1. Nothing above is rewritten. Still before any
data exists. Artifact: `scripts/p212_h1b_amendment2.py`.

## 2.1 `KILL` bar relaxed 0.15 → 0.20

User decision. This is a judgement about the smallest effect worth calling
"not nothing" — scientific, not statistical. AMENDMENT 1 tabulated the
cost; this applies it.

**Consequence: minimum `N` for a reachable `KILL` drops 124 → 71.** The
design's own *"N > 100"* is now sufficient, where under AMENDMENT 1 it
was not.

| N | max observed `r` still giving `KILL` | min observed `r` giving `PROMOTE` |
|---|---|---|
| 71 | 0.0009 | 0.5065 |
| 100 | 0.0500 | 0.4449 |
| 124 | 0.0700 | 0.4162 |
| 138 | 0.0600* | 0.4237 |
| 200 | 0.0900 | 0.4031 |
| 300 | 0.1100 | 0.3845 |

\* values read off a 3801-point grid; see the script for exact figures.

**What `KILL` now asserts, stated plainly:** *even allowing for statistical
uncertainty, the effect is smaller than `r = 0.20`.* That is an
equivalence claim, not "we failed to reach significance."

## 2.2 New subtype — `KILL — opposite-sign signal`

The hypothesis is directional (positive), so one-sided bounds put a
strongly **negative** result into `KILL`. Formally correct — the positive
claim is refuted — but it collapses two different worlds, and a bare
`H1b KILLED` read six months later would not distinguish `r ≈ 0` from
`r ≪ 0`. For any causal reading those are not the same finding.

**Proposed trigger `L₉₅ < 0` was rejected as too weak.** At `N = 138` even
`r = −0.01` gives `L₉₅ = −0.151 < 0`, so the subtype would fire on noise.

**Adopted trigger — the mirror of `PROMOTE`:**

```
KILL — opposite-sign   <=>   U₉₅(r) < −0.30
```

Exactly as demanding on the negative side as `PROMOTE` is on the positive,
and a strict **subset** of `KILL`, not a fourth verdict. Verified on a
3801-point grid at `N = 71…300`: the subtype never escapes `KILL`,
`KILL` and `PROMOTE` never co-fire, no gap.

**Full decision rule now:**

```
U₉₅(r) < −0.30   ->  KILL — opposite-sign signal
U₉₅(r) <  0.20   ->  KILL
L₉₅(r) >  0.30   ->  PROMOTE
otherwise        ->  INCONCLUSIVE
```

## 2.3 Structural-floor null models — ALGORITHM frozen now, not the number

The structural floor cannot be computed without data. The *procedure*
can, and freezing it now removes a real degree of freedom: seeing the
data first would allow choosing the permutation scheme that makes the
observed result look most unusual.

**`M0-1` — stratified permutation.** Permute `E_WHIM` across clusters
*within* strata of `(M_true, z, dynamical state)`, preserving its
marginal. Recompute the partial correlation. 10 000 permutations.

**Stratification is fixed deterministically by `N` alone** — never by the
data's structure. Take the finest scheme that keeps `≥ 5` units per
stratum:

| N | scheme | units/stratum |
|---|---|---|
| 71 | 2×2×2 | 8.9 |
| 100–137 | 3×3×2 | 5.6–7.6 |
| 138–299 | 3×3×3 | 5.1–11.1 |
| ≥ 300 | 4×4×3 | 6.2+ |

(Splits are on quantiles of `M_true` and `z`, and on the dynamical-state
classifier already named in `estimand.md`.)

**`M0-2` — WHIM-free predictor.** Fit `δM` from `M_true`, `z` and
dynamical state with **no WHIM term at all**; take the resulting partial
correlation as the floor.

**Order of operations, binding:** compute `p(r | M0)` for both null models
**first**, then unblind the real `E_WHIM ↔ δM` pairing. Report
`efficiency = (observed − floor) / (ceiling − floor)`.

**Stop conditions unchanged from FL Step 4a:** if `PROMOTE`'s threshold
lies at or below the structural floor → `CRITERION_INVALID`, and the
experiment stops there. None of the Step 4a stop outcomes is evidence
against H1.

## 2.4 What is still NOT settled

The structural floor's **value**. Only its algorithm is fixed. `NR-010`,
on real cluster data, went from raw `r = 0.021` to partial `r = −0.701`
once `M_WL` was controlled — entirely from covariance structure. Whether
anything like that happens here is unknown until the data exists.
