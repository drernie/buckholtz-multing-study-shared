# FINDING P113 — A principled `a1` anchor, built and validated without looking at the answer first: real progress, but the phase-shift control still fails — one level more precisely understood

**Status:** built, regression-tested on the known-good case first, applied
unmodified to the failing case, retested against `FINDING_P112`'s own
controls. The anchor bug is fixed. A separate, more specific obstacle
remains, now precisely characterized.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P113_principled_a1_anchor.py`

> `FINDING_P112` traced its phase-shift control failure to the fixed
> `a1 = a_star×0.2` convention sitting inside `FINDING_P111`'s own transient,
> but declined to just substitute a value that "happened to work" — that
> would be exactly the "picking a lucky moment" the user's own design ruled
> out. This file builds a mechanistic rule instead, validates it on the
> already-passing case, and *only then* applies it to the failing one.

---

## The rule

`find_settled_anchor()`: starting from the arc's own established
`x=a/a_star=0.2` convention (not an invented new scale — the existing lower
bound already used everywhere else in this arc), walk forward through the
**coupled** run's own `|contrast(a)|`, computing the local log-log slope
`d(ln|contrast|)/d(ln a)` on a dense grid. Return the first point where that
slope stays within a fixed tolerance (`0.15`) over a fixed span (`0.3`
decades) — a genuine local power-law plateau, not a hand-picked value. The
same two constants (`SLOPE_TOL`, `SPAN_DECADES`) are fixed once, before
looking at the `k=0.3` result, and never adjusted afterward.

## Step 1 — regression check first, before trusting anything

Applied to the `k=10` baseline (the case that already passes every control
in `FINDING_P112`): the rule lands at `x=0.2002` — matching the established
convention to four significant figures. **This is not a coincidence built
into the rule** — the rule has no knowledge of `x=0.2` as a target; it
simply confirms that for a smooth case, `x=0.2` already sits in a genuine
local plateau, so the walk-forward search finds it immediately. Passing this
check first is what makes it safe to trust the rule on the failing case.

## A false start, caught before it mattered

An earlier version of the search (not in the committed file) searched from
`a0` (the very start of integration) rather than from `x=0.2`, and looked
for **any** local slope plateau. It found one almost immediately, at
`a1/a_star≈0.0006` — a false positive: near `a0`, `|contrast|` is still
essentially frozen at its tiny initial value, so the slope trivially looks
"stable" simply because nothing has started evolving yet, not because any
transient has passed. Requiring a minimum amount of prior evolution didn't
fix this (the field *does* cross a tiny, noise-level zero near `a≈28`,
already flagged in `FINDING_P112`'s own reconnaissance as `lna=-8.16`,
`a/a_star=2.8×10⁻⁴`). The fix was structural, not a threshold tweak: start
the search at the arc's own `x=0.2` convention, not at `a0`.

## Step 2 — applied unmodified to `k=0.3`

Same rule, same constants, no per-case adjustment: lands at `x=33.43` — well
past both the near-`x=1` sign-flip region (`slope=-22` there) and the
noise-level crossing, inside the flat stretch `x≈20–100` that direct
inspection of the raw slope table had already suggested (`slope` ranges from
`-1.24` at `x=20` down to `-0.29` at `x=50`, back up to `-0.66` by `x=1000`).

## Step 3 — retest `FINDING_P112`'s own controls

- **Positive control (`k=10`)**: unchanged, still passes (`RMS` `6.15%` off,
  `peak` `7.96%` off, both under `10%`) — the new anchor doesn't disturb the
  case that was already working.
- **Phase-shift control (`k=0.3`, same `W=5,10,20` sweep)**: spread drops
  from `FINDING_P112`'s `286%` to **`91.5%` (RMS) / `76.1%` (peak)** — large,
  real progress, but still above the `50%` tolerance. **Still fails.**
- **Diagnostic-only, narrower `W=1.2–3` sweep**: `G_RMS` still runs
  `0.033 → 0.073` (`80%` relative spread) — smoother and far less
  catastrophic than the wide sweep, but still a substantial, genuine change.
  This is not a formal control (not part of `FINDING_P112`'s pre-registered
  three), but it answers a natural follow-up question directly rather than
  leaving it implicit: the residual instability is **not an artifact of the
  specific `W=5–20` choice** — it persists, in reduced form, at much smaller
  widths too.

---

## Verdict — **`ANCHOR-NECESSARY-BUT-NOT-SUFFICIENT`**

The anchor bug `FINDING_P112` diagnosed was real, and fixing it — with a
rule validated for regression-safety before being trusted, not a value
chosen because it passes — produces large, genuine improvement (`286%→91%`).
But it does not close the gap on its own. The phase-shift control still
fails `FINDING_P112`'s own pre-registered `50%` tolerance, and the
diagnostic sweep shows why: `(k=0.3, φ̄̇(1)×0.1)`'s coupled `|contrast(a)|`
does not have a power-law plateau wide enough to support a window-averaged
observable at any of the widths tested here, only a *less unstable* stretch
than where the fixed convention had been sitting. No `GAP-CLOSES` or
`STILL-OPEN` verdict on `FINDING_P110`'s original `k<1` question is reported
— the required control still fails, now for a narrower, better-understood
reason than `FINDING_P112` left it in, not a resolved one.

### Not established

- Whether an even more local (sub-decade) window, or a fundamentally
  different observable construction (not a window-average at all), would
  let the phase-shift control pass here.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, `G_RMS`, `G_peak`, or `f(k)` in
  physical units, or any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
