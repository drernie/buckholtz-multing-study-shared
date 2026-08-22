# FINDING P99 — **NO JOINT FIT.** The two-point shape match itself fails before the out-of-sample check is ever reached

**Status:** built, run, verdict investigated further than the pre-registered
scan alone before being trusted — a "closest approach at the grid edge"
signal was followed up rather than reported as-is.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P99_shape_of_H_across_epochs.py`

> `FINDING_P98` closed the `P93`–`P98` single-anchor sub-arc and named what
> would differ in **kind**: an observable sensitive to the **shape** of
> `H(a)` across multiple epochs, not a single number at or through one epoch.
> This file built that test — and it never got past its own first gate.

---

## The design, in one line

`κ` (internal→physical `H`) cancels exactly out of `shape(a) := H(a)/H(a_today)`,
so matching this **purely internal** ratio to flat-`Λ`CDM's own shape at **two**
epochs is a well-posed `2×2` system in the completion's two remaining free
numbers (`Λ_internal`, `a_today`) — unlike every `P93`–`P98` step, which forced
multiple conditions onto **one** remaining unknown after `κ` (or the epoch
itself) already dropped out. Two additional, never-fitted redshifts
(`z=1.0`, `z=3.0`) were reserved as a genuine out-of-sample check.

**Control passed:** `shape(a_today; z=0) = 1.0` exactly, `shape_LCDM(0) = 1.0`
exactly — checked, not assumed.

## Part A — the pre-registered scan found zero crossings

`z_fit1=0.5` fixes `a_today` for each `Λ`; `g(Λ) := shape(z=1.5) − shape_LCDM(1.5)`:

| `Λ` | `a_today` | `g(Λ)` |
|---|---|---|
| `2.084e-16` | `218519.72` | `+2.905e-06` |
| `5.429e-16` | `158812.25` | `+3.862e-06` |
| `1.414e-15` | `115419.04` | `+6.166e-06` |
| … | … | … |
| `1.152e-12` | `12360.70` | `+5.259e-05` |
| `3.000e-12` | `8983.57` | `+1.616e-05` |

**Positive everywhere, zero sign changes.** The *smallest*-`Λ` row had the
smallest `g` — a signal that could mean a nearby root, or could mean nothing.
It was followed up rather than trusted at face value.

## The follow-up, done before writing any verdict

**Below the tested floor:** a finer scan from `8.0×10⁻¹⁷` to `2.084×10⁻¹⁶`
shows `g` **plateauing** at `+2.2×10⁻⁶` to `+2.9×10⁻⁶` (`≈9×10⁻⁷` relative to
`shape_LCDM(1.5)≈2.368`) — then, below `≈1.1×10⁻¹⁶`, the **inner root itself
stops resolving** (no bracket for `a_today`). This is an infrastructure wall,
not a sign change: `g` does not cross zero on its way down, it goes flat and
then the search can no longer be measured at all.

**Above the tested ceiling:** `Λ=4×10⁻¹²` gives `g=+7.613×10⁻⁵` — *larger*
than at `3×10⁻¹²`, confirming `g(Λ)` is **not monotonic** across the range.
`Λ=6×10⁻¹²` overflows the integrator entirely (an uncaught `ValueError`,
surfaced only by this manual extension — the pre-registered scan's own 12
grid points never landed there, so the original run's `exit=0` result stands
unaffected; the gap is noted as a robustness limitation of `H_at_a`'s missing
guard, not fixed here since it is outside the tested range this finding
scores).

**So the closest approach — `≈9×10⁻⁷` relative, at `Λ≈1.2×10⁻¹⁶` — sits at a
genuine boundary the search cannot see past, in either direction.** This is
reported plainly rather than smoothed into either "proven no root" (`P95`'s
standard) or "root nearby, just extend the range" (unsupported by what was
actually found — extending *did* run, and hit walls, not crossings).

---

## Verdict — **NO JOINT FIT**

No `(Λ_internal, a_today)` pair, within the range this file's infrastructure
can resolve, matches flat-`Λ`CDM's shape at **both** `z=0.5` and `z=1.5`
simultaneously. **The out-of-sample check at `z=1.0`/`z=3.0` was never
reached** — there was no fitted pair to evaluate it against. `SHAPE-MATCHES`
and `SHAPE-DIVERGES` both presupposed a completed two-point fit; neither
applies. No `k[h/Mpc]` number is quoted.

### How this compares to `P93`–`P98`, honestly

This is **not** as clean a negative result as `FINDING_P95`'s proof
(`Ω_φ≥0` identically, ruling out every `Λ` with certainty). Here, the
closest approach is remarkably tight — tighter in relative terms
(`≈9×10⁻⁷`) than any single-anchor gap in the whole arc, including `P97`'s
`~0.06%` — but it is bounded by search infrastructure on both sides rather
than by a proven structural impossibility. **Whether a genuine root exists
just past either wall is not established here.**

### What this does establish

The completion's `H(a)` shape does **not** flexibly span the two-degree-of-freedom
space needed to hit flat-`Λ`CDM's shape at two independent, well-separated
redshifts — at least not for any `Λ` this file's solver can safely traverse.
Combined with `FINDING_P93`–`P98`'s single-anchor results, **seven** distinct
attempts across two structurally different kinds of test (same-epoch/integral
anchors, and now a two-epoch shape match) have now failed to pin down or even
successfully calibrate `Λ_internal` against standard cosmology.

### Not established

- Whether a genuine root exists beyond either infrastructure wall — the inner
  root's unresolved region below `Λ≈1.1×10⁻¹⁶`, or the integrator's overflow
  above `Λ≈4×10⁻¹²`. Extending either boundary safely would need its own
  numerical work (a robustly guarded `H_at_a`, and possibly a differently
  parametrized inner search), not attempted here.
- Whether a **different** pair of fit epochs (`z_fit1`, `z_fit2`) would fare
  differently — not tested.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file — `shape_LCDM` is a textbook formula, not a fit to any
  survey's `H(z)` data.
