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
