# FINDING P110 — **`PARTIAL-LOCALIZED-PEAK`.** `k>1` fades fast; `k<1` hits a real numerical pole and stays open

**Status:** built, run, verdict text caught overclaiming and corrected
before reporting — the first pass said "all 5 new points confirm
localization" when only 3 of 5 were actually measurable.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P110_bound_k1_ic_sensitive_band.py`

> `FINDING_P109` found `k=1` sharply IC-sensitive (`8.18%` spread) between
> two attractor-like extremes (`k=0.1`, `k=10`). With only three points,
> that could be a narrow peak or the edge of a wider band. This file
> scans `k=0.3, 0.5, 2, 3, 5` — same `Λ`, same 7 IC variants, same
> thresholds — to bound it.

---

## A verdict-text bug caught before reporting

The first run printed `LOCALIZED-PEAK... All 5 new k points stay under
5%`. That's wrong: `k=0.3` and `k=0.5` never produced a measured spread
at all — `phibar_dot(1)×0.1` (and, at `k=0.3`, also `×0.5`) hit an
**unmeasurable numerical pole**: astronomically large, non-monotonic
`G_growth` (e.g. `23577 → 168413 → 878676 → ...`, final-step change
`20.3%`). The code correctly excluded these from the spread computation
(`NOT ALL VARIANTS CONVERGED... Excluded from spread`) — but the verdict
*text* still claimed all 5 points confirmed localization, silently
treating "excluded" as "measured low." Caught before writing anything up;
corrected to report the gap explicitly.

**This is not a new pathology** — it's exactly `FINDING_P76`'s own `G2`
diagnosis: a ratio whose denominator (the uncoupled reference run's
contrast) passes through zero near an anchor. Not a physics result, an
infrastructure limit specific to those `(k, IC)` pairs.

## Regression control — exact

Baseline IC at `k=0.1/1.0/10.0` reproduces `FINDING_P109`'s own published
`G_∞` to `~10⁻⁷` relative, before trusting anything new.

## Results

| `k` | cross-IC spread | status |
|---|---|---|
| `0.1` | `1.26%` | `FINDING_P109` |
| `0.3` | — | **unmeasured** — `φ̄̇(1)×0.1` and `×0.5` both hit poles |
| `0.5` | — | **unmeasured** — `φ̄̇(1)×0.1` hits a pole |
| `1.0` | `8.18%` | `FINDING_P109` |
| `2.0` | `4.59%` | this file |
| `3.0` | `0.32%` | this file |
| `5.0` | `0.30%` | this file |
| `10.0` | `0.09%` | `FINDING_P109` |

On the `k>1` side, the sensitivity **fades fast and monotonically**:
`8.18% → 4.59% → 0.32% → 0.30% → 0.09%`, consistent with a localized peak
at `k=1` rather than a wide band extending upward.

On the `k<1` side, nothing is established either way. Where amplitude
ICs and the milder `φ̄̇(1)` variants *did* converge, they clustered
tightly — but the variant that actually drove `k=1`'s own spread
(`φ̄̇(1)×0.1`, the most extreme value) could not be measured at either
`k=0.3` or `k=0.5`. Reporting a "low spread" there would have meant
reporting a spread computed from exactly the variants *least* likely to
show sensitivity — not a genuine confirmation.

---

## Verdict — **`PARTIAL-LOCALIZED-PEAK`**

The `k>1` side is resolved: `k=1`'s `8.18%` spread is a narrow, isolated
feature there, fading to attractor-like agreement by `k=3`–`5`. The
`k<1` side is **not resolved** — a real data gap, not a low-spread
result, caused by an unmeasurable pole in exactly the IC variant that
matters most. This file does not establish the band is one-sided; it
establishes that `k>1` fades and that `k<1` remains genuinely open.

### Not established

- The exact boundary of any sensitive region — bounded only by the 8 `k`
  values tested across `FINDING_P109` and this file, not located
  precisely.
- Whether `k<1` shows the same fast fade as `k>1` — the pole prevented
  testing the informative variant there.
- Anything at `Λ` values other than `1e-15`.
- A mechanistic explanation for why `φ̄̇(1)` matters where it does, or
  why the pole appears specifically for extreme `φ̄̇(1)` values at
  `k<1`.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical
  units, or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
