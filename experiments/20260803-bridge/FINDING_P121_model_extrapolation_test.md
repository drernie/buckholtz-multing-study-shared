# FINDING P121 — Model-extrapolation test, corrected after context-asymmetric skeptic review: **`NUMERICAL-CONSISTENCY-CONFIRMED, POWER-LAW-DISCRIMINATES`**

**Status:** built, ran, produced an overclaimed first-pass verdict
(`MODEL-CONFIRMED-ON-EXTENSION`), corrected after a context-asymmetric
skeptic review found the comparison circular and the framing mislabeled.
Rebuilt around a skeptic-mandated negative control (a cubic spline through
the same calibration points), rerun, verdict now defensible.
**Tier:** FL Standard. **L0 (EstimandOps):** descriptive.
**Scope tag:** `NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION`
**Artifact:** `P121_model_extrapolation_test.py`

> User-directed: "заверши P120, запускай P121" (finish P120, run P121).
> `FINDING_P120` fit `contrast_coupled(N) = c_inf - A·N^-p` (`p≈0.503`) to 14
> point-samples and found `contrast_reference(N)` exactly constant. By an
> L'Hôpital argument that predicts a finite `G_E` limit
> (`√G_E→1,259,961`) — but that check was only *directional* (above/below
> one number). This file asked whether *quantitatively* integrating the fit
> matches real, independently-computed cumulative-integral measurements at
> lower-cuts `FINDING_P119`'s own scan never tested (beyond `x_lo=10^100,000`).

---

## First pass — a real result, an overclaimed label

The first build measured predicted-vs-real `G_E(x_lo)` agreement of
`<0.001%` at every one of 9 tested points (4 already-known, 5 new), and
declared `MODEL-CONFIRMED-ON-EXTENSION`.

**Sent to a context-asymmetric skeptic** (claim + code + data only, no
reasoning chain — the same discipline used for `FINDING_P114`/`P117`'s
skeptic reviews). Verdict: **`FALSIFIED`** — as *labeled*, not as
*measured*. Three breaks, all confirmed correct on inspection:

1. **Circularity via integration-smoothing.** Integrating two curves
   already known to agree *pointwise* to `~0.4%` (`FINDING_P120`'s own
   residual figure) will agree at the *integral* level far more tightly, by
   ordinary sign-cancellation under integration — true for any reasonably
   fitting smooth curve, not evidence the specific power-law *form* is
   correct. Proposed remedy: a negative control — fit an *alternative*
   smooth form to the same points, integrate it the same way, see if it
   *also* matches.
2. **Mislabeled "extension".** The tested `x_lo` grid (`150,000`–`339,867`
   decades) sits *entirely inside* the fit's own point-level calibration
   domain (`[397.3, 397,340]` decades). Nothing was tested beyond where
   `contrast(N)` was already directly measured — only the *cumulative-
   integral cutoff* was new, not the underlying point data.
3. **Degenerate reference trivializes the ratio.** `contrast_reference(N)`
   is exactly constant, so it contributes *identical, error-free* energy to
   both the "predicted" and "measured" pipelines. The ratio framing adds no
   robustness; the real comparison is on the coupled-branch numerator alone.

## The fix — a genuine negative control, not a relabel

Built exactly what the skeptic proposed: a `scipy.interpolate.CubicSpline`
through the *same* 14 calibration points used to fit the power law. The
spline has a **strictly better pointwise fit** than the power law (exact
interpolation, `0` residual at the 14 points, vs the power law's own
`0.43%`) — if the skeptic's Break #1 is right, the spline should predict
the new cutoffs *at least* as well. If the power law *measurably*
outperforms it instead, the specific functional form carries real
information beyond generic smoothness.

Pre-registered discrimination threshold (set in code before this run):
power law's worst-case error must be `≥5×` tighter than the spline's.

## Results

**Positive control** (k=10, known-convergent): `0.0001%` agreement,
methodology itself is sound.

**Regression**: refit `c_inf=-38566.4165`, `p=0.502868` — matches
`FINDING_P120`'s own reported values to `1e-6`.

**Consistency** (already-tested grid, `x_lo=0` to `10^100,000`): both
power-law and spline agree with real measurement (`<0.03%` both), spline
occasionally *tighter* here (inside dense sampling near the calibration
points).

**Main result** (new grid, `x_lo=10^150,000` to `10^339,867` — still
interior to the fit's calibration domain, but far from any of the 14
sparse calibration points):

| x_lo (decades) | power-law rel.diff | spline rel.diff |
|---|---|---|
| 150,000 | 0.0004% | 0.0010% |
| 200,000 | 0.0000% | 0.0027% |
| 250,000 | 0.0004% | 0.0054% |
| 300,000 | 0.0007% | 0.0078% |
| 339,867 | 0.0008% | 0.0082% |

The spline's error **grows monotonically** with distance from the nearest
calibration points (`0.0010%→0.0082%`); the power law's stays flat and
small (`0.0004%→0.0008%`). Worst-case: power law `0.0008%` vs spline
`0.0082%` — a **`10.3×`** margin, safely past the pre-registered `5×`
threshold. **Discriminates: `True`.**

Per-decade rise rate decelerating across the new grid: confirmed
programmatically (matched-jump style, not eyeballed) — `True`.

---

## Verdict — **`NUMERICAL-CONSISTENCY-CONFIRMED, POWER-LAW-DISCRIMINATES`**

The power-law model does not merely match real measurement at new
cumulative-integral cutoffs (all interior to its own calibration domain,
not a true extrapolation) — it *measurably outperforms* an equally-smooth,
strictly-better-pointwise-fitting alternative. This is the skeptic-mandated
discriminating evidence: the specific functional form `c_inf - A·N^-p`
carries real information about the shape *between* the sparse calibration
points; the agreement is not a generic artifact of integrating any smooth
curve through the same 14 points.

This is deliberately a narrower, more defensible claim than the retracted
first-pass `MODEL-CONFIRMED-ON-EXTENSION` — it does not claim extrapolation
into untested territory, and it names exactly what the comparison does and
does not control for.

### Not established

- A rigorous asymptotic proof — matching new points strengthens confidence
  but does not prove the model holds past this file's own tested grid.
- Anything **beyond** the fit's own point-level calibration domain (decades
  `~397` to `~397,340`) — every `x_lo` tested here, including the "new"
  grid, sits inside that domain; only the cumulative-integral cutoff values
  are new, not the underlying `contrast(N)` data itself.
- The reference branch's contribution to any of this — it is exactly
  constant, contributes identical error-free energy to both pipelines, so
  the ratio framing does not add robustness beyond the coupled-branch
  numerator alone.
- Anything at `Λ` values, or `(k, IC)` combinations, other than the one
  tested.
- Any numeric value of `eps(k)`, `G_growth`, or `f(k)` in physical units, or
  any `k[h/Mpc]`.
- Anything about MULTING itself (Gate 1).
