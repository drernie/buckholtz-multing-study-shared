# FINDING P116 — **`SMOOTH-SINGLE-FEATURE`**: the transient's `~40%` contribution traces a smooth curve, as predicted — but the deep-cut tail values are still drifting in reach

**Status:** built, resolution-checked, reach-sensitivity checked (and that
control genuinely *failed* at the deep end — reported, not hidden). Tests
`FINDING_P115`'s own registered falsifiable prediction directly.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P116_transient_contribution_scan.py`

> `FINDING_P114`'s own follow-up check found the Integrated Energy Growth
> Observable swings by `~40%` between a lower limit at `x_lo=1` (`≈a_star`)
> and `x_lo=100` (well past the transient) — but only two endpoints were
> tested. User-directed: scan intermediate cuts to see whether the
> transition is smooth (one dominant transient, per `FINDING_P111`) or
> discontinuous (something else going on).

---

## The scan

Fixed `a_reach` at the largest well-converged value this arc established
(`1e8·a_star`, `T_END=3e9`), swept `x_lo = a_lo/a_star` densely from `1` to
`100`.

## Result — a clean, single-peaked, monotonic curve

`√G_E` rises gently from `389,236` (`x_lo=1`) to a broad peak at
**`x_lo=5`** (`√G_E=400,424`), then declines **monotonically all the way to
`x_lo=100`** (`√G_E=294,281`) — no sign flips, no discontinuous jumps, no
secondary bumps. Total swing `x_lo=1→100`: `24.4%` at this (more fully
converged) reach.

**Resolution control**: passes cleanly — `n=8000…64000` agree to `<0.01%`
at both the peak and the tail.

**Monotonicity-after-peak**: confirmed — every point from the peak onward
is `≤` the previous one.

## A control that genuinely failed, reported not hidden

**Reach-sensitivity control**: comparing `a_reach=1e7·a_star` to the
committed `1e8·a_star`, the peak (`x_lo=5`) shifts by only `0.83%` — but the
tail (`x_lo=100`) shifts by **`17.79%`** — well past the `10%` threshold.
**Deep cuts converge in `a_reach` far more slowly than shallow ones**:
excising most of the transient leaves a much smaller total (`8.66×10¹⁰` at
`x_lo=100` vs `1.5×10¹¹` at `x_lo=1`), so the same fixed additional
contribution from pushing `a_reach` further is a *larger fraction* of a
*smaller* total, and needs more decades of reach to settle. This is why
`FINDING_P114`/`P115`'s own `x_lo=1` convergence checks passed so cleanly
(`<0.3%`) while this scan's deep end does not.

---

## Verdict — **`SMOOTH-SINGLE-FEATURE`**, with an honest reach caveat on the tail

The shape conclusion is solid and reach-independent: a single peak near
`x_lo=5`, monotonic decline thereafter, confirmed at both `a_reach=1e7` and
`1e8`. **This confirms `FINDING_P115`'s registered prediction**: the `~40%`
swing `FINDING_P114` found is the genuine, continuous cumulative signature
of `FINDING_P111`'s single dominant transient being progressively excised —
not a sampling accident between two arbitrarily-chosen endpoints, and not
evidence of a second, distinct feature.

**But the precise numbers at the deep end (`x_lo≳50`) are not final.** The
reach-sensitivity control failed there — those values are this scan's best
current estimate at the largest safely-reachable `a_reach`, still drifting,
not the settled numbers `x_lo=1` already is (per `FINDING_P114`/`P115`'s own
clean convergence checks).

### Not established

- Final, fully-reach-converged values for the deep-cut tail (`x_lo≳50`) —
  only the *shape*, not the precise numbers, is established with confidence
  there.
- The physical mechanism setting the peak's specific location (`x_lo≈5`) —
  noted as broadly consistent with, but not identical to, `FINDING_P111`'s
  own report of `δφ` itself peaking near `x=20–100` (a different quantity;
  `contrast` need not peak where `δφ` does).
- Which lower-limit convention (`a0`, `a_star`, or another) is "more
  correct" — a scope choice, not determined here.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
