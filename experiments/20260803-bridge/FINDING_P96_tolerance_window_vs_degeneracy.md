# FINDING P96 — **Q1 CONFIRMED, Q2 completely untouched.** Planck's tolerance resolves the over-constraint and does nothing for the degeneracy

**Status:** built, run, verdict against pre-registered outcomes (Q1 only; Q2
measured, not scored, by design).
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P96_tolerance_window_vs_degeneracy.py`

> `FINDING_P95` proved exact equality between `Ω_m=0.315` and `Ω_Λ=0.685` is
> structurally impossible for any `Λ`, and registered that relaxing to
> Planck's own `±0.007` uncertainty should open a window, since the measured
> shortfall (`Ω_φ ~ 1e-7`–`1e-4`) is orders below that tolerance. It does.
> **This file exists to say, with a number, what opening that window does and
> does not fix** — conflating the two would be exactly the overclaim this step
> was built to prevent.

---

## Two questions, kept explicitly separate

- **Q1** (`FINDING_P95`'s question — over-constraint): for a **given** `Λ`,
  does *some* `a_today` put both `Ω_m` and `Ω_Λ` inside Planck's tolerance
  band simultaneously?
- **Q2** (`FINDING_P94`'s question — degeneracy): **which** `Λ` is correct?
  Loosening a per-`Λ` constraint cannot narrow a choice *across* `Λ` values —
  if exact equality already had multiple `Λ` solutions (`P94`'s `31.6×`
  spread), a looser tolerance admits an equal-or-wider range, not a narrower
  one.

## Results

| seed | window (`a`) | `H_int` range in window |
|---|---|---|
| `1e4` | `[9665.166, 9871.724]` | `[5.315706e-06, 5.369092e-06]` |
| `3e4` | `[28995.132, 29614.799]` | `[1.023006e-06, 1.033280e-06]` |
| `1e5` | `[96651.628, 98717.212]` | `[1.680958e-07, 1.697838e-07]` |
| `3e5` | — | `BLOCKED-INFRASTRUCTURE` (same as `P94`/`P95`, excluded) |

Each window is narrow — roughly `±1–2%` in `a`, and `H_int` within a single
`Λ`'s window varies by well under `1%`. **Q1: `CONFIRMED`** on all three
measurable `Λ`.

**Q2, measured:**

```
FINDING_P94 (exact equality):  31.623095x spread in H_int across four Lambda
This file (Planck tolerance):  31.9407x   spread in H_int across the windows
ratio:                          1.0100   -- 1% WIDER, not narrower
```

The spread did **not** shrink. It could not have: loosening a constraint that
already had multiple solutions only ever admits an equal-or-larger solution
set.

---

## Verdict

**Q1: `CONFIRMED`**, exactly as `FINDING_P95` predicted — the over-constraint
found there is an artifact of demanding *exact* equality to two numbers
Planck itself only quotes to `±0.007`; under that real uncertainty, the
completion's `Ω_m`/`Ω_Λ` composition fits comfortably.

**Q2: unresolved, and now quantified as unresolved** rather than left
ambiguous. **No `k[h/Mpc]` number is quoted** — not because Q1 failed, but
because Q1 was never the question that blocks the bridge. The blocking
question is Q2, and this file confirms directly that nothing tried across
`P93`–`P96` touches it: `Λ_internal` remains a free parameter of the
completion, and three different anchoring strategies (`Ω_Λ=0.7` convention,
`Ω_m` alone, `Ω_m`+`Ω_Λ` jointly at exact or tolerant precision) have now all
failed to pin it, each failing for a **different, explicitly diagnosed**
reason:

| step | anchor tried | result |
|---|---|---|
| `P93` | `Ω_Λ=0.7` convention | tautological — never picks an epoch |
| `P94` | `Ω_m` alone, `Λ` fixed per branch | `31.6×` spread across `Λ` |
| `P95` | `Ω_m` **and** `Ω_Λ` jointly, exact | structurally impossible (`Ω_φ≥0`) |
| `P96` | `Ω_m` **and** `Ω_Λ` jointly, Planck tolerance | window opens; `Λ` spread **unchanged** |

### What would actually touch Q2

Per `FINDING_P94`'s own diagnosis, restated here because `P96` confirms it
rather than superseding it: a ratio-type anchor (however many, however
precise) fixes the **composition** at whatever epoch the search lands on, never
the **absolute scale** of `Λ_internal` itself. Resolving Q2 needs information
about the **shape** of `H(a)` across *multiple* epochs — e.g. the age of the
universe (an integral over the full expansion history, sensitive to `Λ`'s
functional history in a way a same-epoch ratio is not) — not another
same-epoch ratio, however tight its tolerance.

### Not established

- Which `Λ_internal` the completion has — still open, and now shown to survive
  four independent anchoring attempts.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
