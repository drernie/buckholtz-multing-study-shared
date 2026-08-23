# FINDING P123 — Does `power_law_log`'s log-correction drift toward 0, or stabilize? **`RATE-LEVELS-OFF, LEANS-DIVERGENT`** (a scale-naive first check retracted before commit)

**Status:** built, ran, and its own first verdict-logic pass was caught and
retracted before commit — a decade-scale-naivety bug, the same category
(not the same instance) as `FINDING_P119`'s own retracted `PLATEAU-FOUND`.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P123_log_correction_drift_test.py`

> User-directed ("го все по очереди" — work through the open items in
> order), the first of two follow-ups `FINDING_P122` itself named.
> `FINDING_P122` found two best-fitting models disagree on whether the
> deviation-energy integral converges: plain `power_law` (`q≈0.502>1/2`,
> converges) vs `power_law_log` (`q≈0.485–0.49<1/2`, diverges) — with
> `power_law_log` measurably beating `power_law` on held-out prediction at
> every tested window, and its own log-correction `r` drifting
> monotonically toward `0` across those windows (`-0.131 → -0.094`). Does
> that drift continue toward `0` (favoring `power_law`'s convergent
> reading), or stabilize at a nonzero value (favoring `power_law_log`'s
> divergent one)?

---

## Design

Reused `FINDING_P122`'s own already-computed `T_END=1e13` trajectory and
its exact, untouched hold-out probes (`{360000, 375000, 390000}` decades)
unchanged. Extended its `N_cut` sequence with 5 new points closer to the
hold-out boundary: `{310000, 320000, 330000, 340000, 350000}` decades,
preserving a `10,000`-decade gap from the nearest probe. Regression
control: the first 6 points reproduce `FINDING_P122`'s own committed
`q`/`r` values to `<1e-4` relative — exact.

## A scale-naive first check, caught before commit

The first pass classified `r` as `PLATEAUED` using a "last-3-points
relative spread `<5%`" check — the same *shape* of naive threshold that
sank `FINDING_P119`'s own retracted `PLATEAU-FOUND` (though not the same
instance: different file, different quantity). The bug: the original 6
points are spaced `50,000` decades apart; the 5 new ones only `10,000`
decades apart — so raw deltas between the new points look smaller
regardless of whether the underlying *rate* actually leveled off. Checked
by hand before trusting it: the decade-normalized rate was **still
shrinking monotonically** through the naive check's own "plateaued"
region (`7.16×10⁻⁸ → 5.83×10⁻⁸` per decade) — the naive check's verdict
was an artifact of the scan's own shrinking step size, not a real signal.

**Fixed** by replacing the check with a decade-normalized rate comparison
(consecutive `Δr/ΔN_cut`, not raw `Δr`) — the same discipline
`FINDING_P119`'s own corrected Check A already established for a
different quantity, applied here to a new one.

## Results — the corrected check

| Segment | decade-normalized rate |
|---|---|
| `50k→100k` | `3.185×10⁻⁷` |
| `100k→150k` | `1.562×10⁻⁷` |
| `150k→200k` | `1.083×10⁻⁷` |
| `200k→250k` | `8.563×10⁻⁸` |
| `250k→300k` | `7.162×10⁻⁸` |
| `300k→310k` (new) | `6.519×10⁻⁸` |
| `310k→320k` (new) | `6.334×10⁻⁸` |
| `320k→330k` (new) | `6.158×10⁻⁸` |
| `330k→340k` (new) | `5.991×10⁻⁸` |
| `340k→350k` (new) | `5.830×10⁻⁸` |

Across the *original* 6 points, the rate fell by nearly `5×`
(`3.19×10⁻⁷ → 7.16×10⁻⁸`). Across the *new* extension, it fell by only
`~10.6%` (ratio of last to first new-segment rate: `0.894`) — a genuine,
much gentler deceleration, not a step-size artifact this time (verified
on a like-for-like, decade-normalized basis).

## Verdict — **`RATE-LEVELS-OFF, LEANS-DIVERGENT`**

The decade-normalized rate of `r`'s change has largely stopped
decelerating within the new extension — consistent with `r` approaching a
fixed, nonzero asymptote rather than `0`. This leans toward
`power_law_log`'s own divergent reading of the deviation-energy question
being closer to correct than plain `power_law`'s convergent one —
`FINDING_P122`'s tension is **not** resolved in plain `power_law`'s favor
by this extension.

### Not established

- A rigorous asymptotic theorem for `r`'s true limiting value — this file
  tests a wider but still finite window, not the `N→∞` limit.
- Which model correctly describes the *true* tail law with certainty —
  this file characterizes the trend, it leans but does not adjudicate.
- The `ratio > 0.7` "leveled" threshold is a reasonable, stated heuristic
  chosen to separate "still decelerating substantially" (`5×` fall) from
  "barely decelerating further" (`~10%` fall) — not an independently
  calibrated constant.
- That `G_E` itself is affected by any of this — it remains established
  (`FINDING_P120`/`P122`) as convergent for any `q>0`, independent of this
  file's own result.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units,
  or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
