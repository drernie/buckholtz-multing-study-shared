# FINDING P111 — **`TRANSIENT-OSCILLATION`, not a ratio pole.** `P110`'s own attribution was wrong — corrected, diagnosed, and honestly left unfixed

**Status:** built, run, `FINDING_P110`'s own diagnostic claim checked
directly and found incorrect — corrected before anything else was built
on it.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P111_diagnose_k_lt_1_phidot_pole.py`

> `FINDING_P110` attributed its `k<1` pole to `FINDING_P76`'s own `G2`
> "ratio whose denominator crosses zero" pathology — **by analogy,
> without checking**. This file checked it directly. It was wrong.

---

## `P110`'s own claim, checked and rejected

Step 1: does the *reference* (`g_hat=0`) run's contrast — the quantity
that would have to cross zero for a `G2`-style denominator pole — cross
zero anywhere in the tested range? **No.** It grows smoothly and stays
one-signed throughout: `4.25×10⁻³` (`x=0.2`) → `3.06×10⁻²` (`x=100`).
`FINDING_P110`'s attribution was made by analogy to a superficially
similar prior pathology, not verified against the actual quantity — and
it was wrong. Corrected here, before building anything further on it.

## The actual mechanism

The **coupled** (`g_hat=1`) run's own field perturbation `δφ` is the
culprit. At `(k=0.3, φ̄̇(1)×0.1)` it runs from `-1.7×10⁻⁴` (`x=0.2`)
through `+5.15` (`x=1`), oscillating in sign, peaking near
`x=20`–`100` (`~6570`), then **declining** (`1004` by `x=5000`) — a
large transient overshoot, not a monotonic runaway. Checked whether this
is an equation-of-motion singularity (`(1-ĝφ̄)→0`, the real mechanism
behind `FINDING_P76`'s own `μ`/`G2` poles): `φ̄` itself stays at
`10⁻⁵`–`10⁻⁸` throughout, nowhere near `1/ĝ=1` — **ruled out**. The same
overshoot-then-decay pattern was confirmed at all three of
`FINDING_P110`'s poled `(k, IC)` combinations before generalizing.

## The attempted fix — mirroring `P108`'s own precedent, and why it fails here

`FINDING_P108` fixed an under-reach problem by widening `T_END`.
Applied the same trick here, for `(k=0.3, φ̄̇(1)×0.1)`:

| `T_END` | `a(T_END)/a_star` | `G_growth` |
|---|---|---|
| `1e8` | `5948` | `18777` |
| `3e8` | `5.3×10¹¹` | `-463754` |
| `1e9` | `3.5×10³⁹` | `-722516` |

**`G_growth` goes negative.** A sign flip is only possible if the
coupled contrast itself crosses zero beyond the `T_END=1e8` reach. So
the decay seen within `T_END=1e8` was not settling toward a finite,
nonzero asymptote — it was the leading edge of a **damped oscillation**
that crosses zero repeatedly. Widening the window doesn't fix this; it
just relocates *where* the next zero-crossing happens to fall.

---

## Verdict — **`TRANSIENT-OSCILLATION`, correctly diagnosed, honestly not fixed**

Neither `FINDING_P76`'s fix (anchor relocation, for a denominator pole)
nor `FINDING_P108`'s fix (`T_END` extension, for under-reach) resolves
this — both address genuinely different failure modes. Point-sampled
`G_growth`, evaluated at any fixed `x`, is structurally the wrong tool
once the coupled contrast oscillates through zero. This is the same
"wrong tool for this regime" lesson `FINDING_P107` taught for `eps`, in
the opposite direction: there, a bounded numerator over an ever-growing
denominator; here, an oscillating numerator sampled at a single point.
A genuine resolution needs an envelope- or RMS-based observable — named,
not built here.

**Not attempting to force a number here is the correct call**, not a
shortfall: manufacturing a "converged" value by picking a lucky `x` that
happens to avoid a zero-crossing would be indistinguishable from noise
and would misrepresent what's actually happening in this regime.

### Not established

- An envelope- or RMS-based observable that *would* be well-defined for
  these `(k, IC)` combinations — not built here, a materially larger
  undertaking.
- Whether this transient-oscillation mechanism appears at other `(k,
  IC)` combinations not yet tested — only the three `FINDING_P110`
  already flagged were checked.
- Anything about MULTING itself (Gate 1).
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical
  units, or any `k[h/Mpc]`.
