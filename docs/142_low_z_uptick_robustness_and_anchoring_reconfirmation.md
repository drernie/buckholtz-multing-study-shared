# docs/142 — low-z "uptick" robustness check + anchoring-parity reconfirmation

**Date:** 2026-08-12
**Origin:** TJB circulated a draft Reddit headline (group email, 2026-08-12) claiming his
framework "closes up to 100%" of the Hubble tension and hints the Hubble constant "could
start rising again" (low-positive-z uptick), citing an "independent AI re-run" as
verification. This doc records a cheap, decisive check of the one claim among the three
that had not already been assessed by this project (the anchoring-artifact finding, P2/
docs/127, already covers the "100%" claim; the AI-re-run wording is a provenance/labeling
question, not a numeric one).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION · L0 descriptive
**Scripts:** `scripts/plot_hubble_anchoring.py` (pre-existing, re-run for current numbers),
`scripts/low_z_uptick_robustness_check.py` (new).

---

## 1. Scope limit, stated up front

TJB's actual current chart (the one behind the 2026-08-12 email) was not available to us —
no image was attached to what we received. Both checks below run against
**`data/hz_cc.csv`** — 27 real, independent Moresco+2022 cosmic-chronometer points,
FLRW-independent, not derived from Table A1 or any MULTING fit — not against TJB's own
rendered curve, which we do not have pixel data for. If his "uptick" is a feature of a
fitted model curve rather than the raw data itself, §3 below bounds how much support the
raw observations alone can offer that fit; it does not test the fit's own machinery.

## 2. Anchoring-parity reconfirmation (re-run of P2 / docs/127, current numbers)

```
free fit          : H0=68.77, Om=0.317  chi2=12.8
anchor Planck 67.36:  chi2=13.5 (Om=0.317 fixed) / 13.0 (Om=0.340 floated)
anchor SH0ES  73.04:  chi2=19.2 (Om=0.317 fixed) / 14.7 (Om=0.257 floated)
```

**Δχ² = 5.7 favoring Planck at fixed Ωm; ≈1.7 favoring Planck with Ωm floated.** The real
chronometer data prefer the low anchor, not the SH0ES one — reconfirms P2's original
finding (MULTING's background is q-blind/degenerate with ΛCDM; the z≈0 gap in the anchored
chart is the anchor choice, not model physics) with current code, unchanged from the prior
run.

## 3. Low-z uptick — leave-one-out + weighted bootstrap

**Method:** fit the free ΛCDM baseline to all 27 points (H0=68.77, Ωm=0.317). On the
low-z subsample (`z<0.3`, 9 points — "low positive z" per TJB's own phrase), fit a
weighted quadratic to the *residuals* from that baseline; the curvature coefficient `c`
is the test statistic (`c<0` = residuals bend upward as `z→0`, the "uptick read
right-to-left" shape TJB described). Leave-one-out: refit dropping each of the 9 points
once. Bootstrap: 2000 resamples, each point perturbed within its own `sigma_Hz` (fixed
seed `20260812`, stated before running, not tuned after).

```
[FULL-SAMPLE CURVATURE] c = -306.22 km/s/Mpc per z^2   (negative = uptick-shaped)

[LEAVE-ONE-OUT] 0/9 sign flips — every single-point deletion keeps c negative

[BOOTSTRAP] 2000 resamples:
  c: mean=-261.32, 95% CI=[-2297.56, +1692.74]
  fraction of resamples with c<0: 59.9%
  95% CI excludes zero: FALSE
```

## 4. Result — the LOO/bootstrap split is the finding

**Leave-one-out alone would say "robust"** — the point estimate's sign never flips when
any single point is dropped. **The bootstrap says otherwise** — the 95% CI is enormous
and straddles zero, and only 60% of resamples (barely above a coin flip) even land on the
same sign as the point estimate. At current low-z chronometer precision (error bars of
12–37 km/s/Mpc on H(z) values of 69–89), **the data cannot resolve curvature at this scale
in either direction** — this is not evidence for an uptick, and it is not evidence against
one either. It is a genuine null result driven by measurement precision, not a refutation.

**This is also a clean illustration of why LOO alone is an inadequate robustness check**:
LOO tests whether one influential point is driving a conclusion; it does not test whether
the conclusion is statistically distinguishable from noise at all. Both are needed
together — exactly the design the mini-sprint asked for.

## 5. Qualitative notes (not separately computed here)

- **Timeline:** the uptick claim first appears in TJB's 2026-08-02 chart update; the
  original 2026-07-20 chart carried no such claim. A plain, observable timeline fact — not
  a claim about intent or process.
- **Model complexity:** the AI-service transcripts report materially different β_d/β_q
  fits (0.78, 4.5, 4.25 for β_d alone across three services) — MULTING as operationalized
  via Table A1 has more effective free parameters and less parameter stability than ΛCDM's
  fixed (H0, Ωm). A fair AIC/BIC comparison would need to account for this; not computed
  here (cheap follow-up, not yet executed).

## 6. What this does NOT establish

1. **Anything about TJB's own rendered chart or fitted curve** — only about what the raw,
   independent chronometer data themselves can and cannot currently support at low z.
2. **That no low-z uptick exists.** The bootstrap CI is uninformative in both directions;
   absence of resolving power is not evidence of absence.
3. **An AIC/BIC number for the model-complexity question** (§5) — noted, not computed.
4. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction and about what
   the cited public data supports, not a claim about TJB's own unpublished theory or
   process.

## Reproduction

```bash
python scripts/plot_hubble_anchoring.py
python scripts/low_z_uptick_robustness_check.py
```
