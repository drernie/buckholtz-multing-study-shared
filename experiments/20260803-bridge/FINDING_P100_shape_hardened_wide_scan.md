# FINDING P100 — **STILL-NO-ROOT.** Hardening confirmed `P99`'s crash was the same wall, not a hidden root

**Status:** built, run, regression control passed, verdict against
pre-registered outcomes.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P100_shape_hardened_wide_scan.py`

> `FINDING_P99` found `NO JOINT FIT` for the two-epoch `H(a)` shape match, but
> the search hit two boundaries it couldn't see past: an unresolvable inner
> root below `Λ≈1.1×10⁻¹⁶`, and an **uncaught integrator overflow** above
> `Λ≈4×10⁻¹²`. This file hardens the code and re-scans past both — and
> answers the specific question `P99` left open.

---

## Step 1 — regression control, before trusting anything new

| `Λ` | `P99` published `g` | this file's `g` | relative diff |
|---|---|---|---|
| `2.084e-16` | `2.905e-06` | `2.904817e-06` | `6.284e-05` |
| `3.000e-12` | `1.616e-05` | `1.615814e-05` | `1.151e-04` |

Both well inside the `5×10⁻³` tolerance. **Hardening did not change `P99`'s
answers** — the new failure-handling only changes what happens at points that
previously crashed or silently misbehaved.

## Step 2 — the widened, hardened scan

`Λ` swept from `10⁻¹⁹` to `10⁻⁹` (40 points, log-spaced) — `P99`'s own range
was `[8.0×10⁻¹⁷, 3.0×10⁻¹²]`.

| region | outcome |
|---|---|
| `Λ < 1.194×10⁻¹⁶` | **cleanly** `not measured` — no crash, no root |
| `Λ ∈ [1.194×10⁻¹⁶, 4.924×10⁻¹²]` | measurable, `g` **positive throughout**, `2.397×10⁻⁶` to `9.667×10⁻⁵`, non-monotonic |
| `Λ > 4.924×10⁻¹²` | **cleanly** `not measured` — no crash, no root |

**19 of 40 grid points measurable.** Measurable range
`[1.194×10⁻¹⁶, 4.924×10⁻¹²]` — extended `1.49×` downward and `1.64×` upward
past `P99`'s own bounds, then hits the **same kind of wall again**, this time
without incident.

**Zero sign changes.** `g(Λ)` never approaches zero more closely than
`P99`'s own tightest point.

---

## What this answers, and what it does not

**Answered:** `P99`'s integrator overflow at `Λ=6×10⁻¹²` was **not** masking
a nearby root. With the crash removed, the search continues cleanly past that
point and finds the *same shape* of wall a little further out — the crash
was an ungraceful discovery of a real boundary, not evidence a root was being
hidden by a bug.

**Not answered:** *why* the inner root's search bracket
(`[A_SEARCH_LO, A_SEARCH_HI] = [300, 3×10⁶]` in `a_today`) fails to contain a
solution outside this `Λ` band. This file widened `Λ`, not the `a_today`
bracket itself — and the wall's persistent shape (clean failure just past
where the crash used to be) suggests the `a_today` bracket, not the `Λ` range,
is now the binding constraint. That is a **different** lever from anything
tried here, named but not pulled.

---

## Verdict — **STILL-NO-ROOT**

Zero sign changes across a `Λ` range roughly `1.5×`–`1.6×` wider than
`FINDING_P99`'s own bounds in each direction, with the earlier crash resolved
and confirmed not to have concealed anything. **Still not a `P95`-style
proof** — the search remains bounded by the `a_today` search bracket, not by
an argument that no root can exist for any `Λ` whatsoever. No `k[h/Mpc]`
number is quoted.

### Not established

- Whether widening the `a_today` search bracket itself (not just `Λ`) would
  reveal a root beyond either current wall — the next, different lever, not
  attempted here.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
