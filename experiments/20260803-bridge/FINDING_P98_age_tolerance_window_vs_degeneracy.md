# FINDING P98 — **Q1 CONFIRMED, Q2 measured indistinguishable from `P94`'s baseline.** Six anchoring attempts, one conclusion

**Status:** built, run, verdict against pre-registered outcomes (Q1 scored;
Q2 measured by design). Both halves of `FINDING_P97`'s registered prediction
confirmed. This finding also **closes the `P93`–`P98` sub-arc**: continuing to
test single external anchors of the same basic kind has reached diminishing
returns, and that conclusion is stated explicitly rather than left implicit.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P98_age_tolerance_window_vs_degeneracy.py`

> `FINDING_P97` found `NO-ROOT` for `{Ω_m=0.315, age=13.787 Gyr}` exactly, but
> the tightest gap in the whole arc (`~0.06%`), and predicted **both** halves
> of this file's result in advance: the window opens easily (gap `<` Planck's
> own `±0.020` Gyr tolerance), and it does nothing for the degeneracy — by a
> **sharper** argument than `FINDING_P96` had, since `P97` had already shown
> age barely responds to `Λ` at all.

---

## Results

| seed | window (`a`) | `H_int` range |
|---|---|---|
| `1e4` | `[9735.783, 9779.757]` | `[5.338984e-06, 5.350390e-06]` |
| `3e4` | `[29206.983, 29338.903]` | `[1.027486e-06, 1.029681e-06]` |
| `1e5` | `[97324.062, 97797.547]` | `[1.688318e-07, 1.692204e-07]` |
| `3e5` | — | `BLOCKED-INFRASTRUCTURE` (consistent with every prior step) |

**Q1: `CONFIRMED`** on all three measurable seeds — unsurprising, and reported
as such: the gap `FINDING_P97` measured (`0.0075`–`0.0091` Gyr) was always
inside the `±0.020` Gyr tolerance, so this confirmation carries less
information than `FINDING_P96`'s did.

**Q2, measured:**

```
FINDING_P94 (exact Omega equality):    31.623095x
FINDING_P96 (tolerant Omega, Omega):   31.940700x
This file  (tolerant Omega + age):     31.690653x
ratio to FINDING_P94's baseline:        1.0021
```

**`0.21%` wider — even closer to `P94`'s original baseline than `P96`'s
`1.00%` was.** Consistent with `FINDING_P97`'s own measurement that age varies
by only `~20%` of its own value across five decades of `Λ`: a quantity that
barely responds to `Λ` in the first place gains essentially no new
discriminating power from being allowed to vary within tolerance.

---

## Closing the `P93`–`P98` sub-arc

Six consecutive anchoring attempts, each failing for its **own diagnosed
reason**, all converging on the same structural conclusion:

| step | anchor(s) | precision | result |
|---|---|---|---|
| `P93` | `Ω_Λ=0.7` alone | — | tautological — never picks an epoch |
| `P94` | `Ω_m` alone, `Λ` fixed per branch | exact | `31.6×` spread across `Λ` |
| `P95` | `Ω_m` + `Ω_Λ` jointly | exact | `NO-ROOT`, **proven** (`Ω_φ≥0`) |
| `P96` | `Ω_m` + `Ω_Λ` jointly | Planck tolerance | window opens; spread `31.9×` |
| `P97` | `Ω_m` + age jointly | exact | `NO-ROOT`, unproven, gap `~0.06%` |
| `P98` | `Ω_m` + age jointly | Planck tolerance | window opens; spread `31.7×` |

**The `Λ`-spread never moved outside `[31.6×, 31.9×]` across four different
anchor combinations and two precision regimes.** This is not six independent
near-misses — it is one finding, confirmed six ways: a **ratio or integral
observable evaluated at (or through) a single epoch fixes the completion's
composition at that epoch, but never the absolute scale of `Λ_internal`**,
because nothing in `FINDING_P86`'s construction ties `Λ_internal` to anything
the model predicts. Every anchor tried — however many, however precise,
whether instantaneous or integrated over the whole history — answers a
question about **where** the completion's trajectory sits, never **which**
trajectory (i.e., which `Λ`) it is.

**What would actually differ in kind, not just in which number is matched:**
a **theoretical** prediction for `Λ_internal` from the completion itself, or
an observable sensitive to **two structurally different epochs at once** in a
way that constrains `Λ`'s functional form rather than its value at one point
(e.g. the *shape* of `H(z)` across a redshift range, not a single number at
`z=0` and not a single integral to `z=0`). Neither is a small next step; both
are a different **kind** of step from `P93`–`P98`, and building either is a
decision that should be made deliberately, not simply the next number in the
sequence.

---

## Verdict

**Q1: `CONFIRMED`**, as predicted and with the predicted lack of surprise.
**Q2: measured, indistinguishable from `P94`'s original spread** — the
sharpest confirmation yet that no anchor of this kind touches the
degeneracy. **No `k[h/Mpc]` number is quoted.**

### Not established

- Which `Λ_internal` the completion has — now shown to survive **six**
  independent anchoring attempts of two structurally similar kinds.
- Whether a genuinely different kind of anchor (theoretical `Λ` prediction,
  or multi-epoch shape information) would resolve it — not attempted in this
  arc.
- Any numeric value of `ε(k)` or `f(k)` in physical units.
- Anything about MULTING itself (Gate 1). No dataset, no Table A1 quantity
  entered this file.
