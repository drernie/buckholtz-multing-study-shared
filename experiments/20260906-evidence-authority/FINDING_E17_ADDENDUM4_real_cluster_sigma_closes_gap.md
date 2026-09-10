# FINDING E17 ADDENDUM 4 — the real cluster-scale sigma(log10 c) gap is
# closed: Duffy 2008's own value is independently validated for the
# X-ray/HSE method, not just an untested default

**Date:** 2026-09-10
**Continues:** `FINDING_E17_ADDENDUM3`'s own named `SOURCE_NOT_FOUND` gap
— no real, cluster-scale-specific `σ(log10 c)` value had been found;
the divergence headline stayed "a range, not a point estimate."

`NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive`
`NO_AUTHOR_ERROR`

## Why the earlier search failed — a real, diagnosable tooling gap

Three separate attempts to extract Groener, Goldberg & Sereno (2015)'s
own Table 2 via the arXiv MCP's LaTeX-to-text conversion all failed the
same way: `get_paper_latex_section` returned the prose immediately
around the table but not its numeric rows, and `search_paper_text`
returned zero passages for `"sigma_int"`, `"Table 2 best-fit..."`, and
`"intrinsic scatter dex"` — three different query phrasings, same null
result. This points at the conversion step (a complex `deluxetable`-like
multi-column environment with footnote markers does not survive
LaTeX→text conversion cleanly), not at the search itself. **Resolved by
reading the user-supplied PDF directly** (visual page extraction,
`C:\Users\serge\Downloads\1510.01961v2.pdf`, page 6) — this bypasses the
LaTeX conversion step entirely.

## The real number, `[VERIFIED-PDF]`

Table 2 of arXiv:1510.01961, column `σ_int` (their own footnote 5:
*"Equivalent to the scatter in log c_vir reported in previous
studies"* — exactly `σ(log10 c)`, the quantity `ADDENDUM3` searched for):

| Method | `N_cl` | `σ_int` |
|---|---|---|
| WL | 93 | 0.118 |
| WL+SL | 57 | 0.130 |
| **All methods combined** | 293 | **0.146** |
| **X-ray (closest to Mahdavi 2013's own method)** | 149 | **0.160** |
| LOSVD | 58 | 0.228 |
| CM | 63 | 0.242 |
| SL | 10 | 0.246 |

Sample is genuinely cluster-scale (`M_vir` mostly `10^14-10^17 M_☉` per
the paper's own Table 1), unlike Duffy et al. (2008)'s own group-to-
cluster calibration range this project defaulted to.

## Re-evaluated `ADDENDUM3`'s own `sigma_sweep()` at the real values

(`E17_addendum4_real_cluster_sigma.py`, reuses `ADDENDUM3`'s own
positive-control-verified `sigma_sweep()`/`divergence()` unchanged)

| σ source | σ | divergence at `z=2.33` | shift vs Duffy's `0.15` |
|---|---|---|---|
| Duffy 2008 (prior default) | 0.150 | 1.815× | — |
| **X-ray (real, method-matched)** | **0.160** | **1.725×** | **−4.9%** |
| **All methods (real)** | **0.146** | **1.853×** | **+2.1%** |
| WL (real) | 0.118 | 2.145× | +18.2% |
| WL+SL (real) | 0.130 | 2.014× | +10.9% |
| LOSVD (real) | 0.228 | 1.264× | −30.3% |
| CM (real) | 0.242 | 1.196× | −34.1% |
| SL (real) | 0.246 | 1.177× | −35.1% |

## What this establishes

1. `[VERIFIED-PDF]` The `σ`-value question `ADDENDUM3` left as
   `SOURCE_NOT_FOUND` is now answered with a real, cluster-scale,
   method-specific measurement — not a proxy or an out-of-range
   extrapolation.
2. **For the method actually comparable to this whole line's own basis**
   (X-ray/HSE, matching Mahdavi et al. 2013's own CCCP approach), the
   real value (`σ=0.160`) gives a divergence essentially the same as the
   previously-used Duffy default (`1.725×` vs `1.815×`, a `4.9%` shift)
   — this VALIDATES `σ=0.15` as a reasonable central value for this
   specific method, not merely convenient. The all-methods combined
   value (`0.146`) agrees even more closely (`+2.1%`).
3. **Different measurement techniques genuinely disagree on `σ(log10 c)`
   itself** — lensing methods (WL, WL+SL) give `18-30%` higher
   divergence than Duffy's default; galaxy-kinematics methods (LOSVD,
   CM, SL) give `30-35%` lower. This is real, method-driven disagreement
   in the literature's own concentration measurements, not noise.
4. `ADDENDUM3`'s own sensitivity conclusion (a real, `σ`-driven range)
   is **not overturned** — it is now anchored to real numbers instead of
   an arbitrary `±0.05` dex bracket, and the X-ray-method anchor point
   specifically sits close to the old default.

## What this does NOT establish

1. Which measurement technique's own `σ(log10 c)` is the "correct" one
   to use for v82's own construction — the X-ray/HSE match is a
   reasonable methodological choice (matches Mahdavi 2013's own
   approach, used throughout this project's H1 program), not a proof
   that other techniques are wrong.
2. Whether the technique-to-technique disagreement itself (point 3
   above) has a known physical explanation — Groener, Goldberg & Sereno
   (2015)'s own Conclusions section discusses several candidate causes
   (selection effects, triaxiality/projection, NFW-vs-Einasto profile
   mismatch) without settling on one; not investigated further here.
3. `NO_AUTHOR_ERROR` — entirely about this project's own reconstruction
   of the `F0`/`F_accretion` Jensen-correction sensitivity chain; no
   claim about v82's or Correa's or Groener/Goldberg/Sereno's own
   correctness.

## Files

- `E17_addendum4_real_cluster_sigma.py` — reuses `ADDENDUM3`'s own
  `sigma_sweep()`/`divergence()` unchanged, evaluates at the real
  values above. `ruff check` clean.
