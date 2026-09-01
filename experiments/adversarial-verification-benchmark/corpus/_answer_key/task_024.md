# Answer Key — Task 024

**Tier:** C (fresh synthetic, out-of-domain)
**Category:** Artifact Zoo Universal — `all_nan_input` (silently → 0)

## The seeded defect

`compute_noise_floor_rms` uses `np.nanmean(window ** 2)`, which ignores
`NaN` values when averaging — but if an *entire* window is `NaN`
(exactly the known, logged failure mode where the acquisition unit
drops a whole window during a network hiccup), `np.nanmean` on an
all-`NaN` array returns `NaN` itself (with a runtime warning), and
`np.sqrt(NaN)` is `NaN`. Then `flag_drift`'s comparison `rms >
threshold` evaluates to `False` for any `NaN` RMS (NaN comparisons are
always `False` in IEEE 754 / numpy), meaning **every dropped-data
window is silently classified as "not drifting"** — the worst possible
case (dead/missing sensor data) is treated identically to "healthy,
low-noise data."

## Why this changes the correct answer

The report's "0.02% flag rate" is presented as evidence the detector is
well-calibrated and not oversensitive. But given the known
window-dropout issue, part of that low flag rate is mechanically
guaranteed: any window that is entirely missing data is *automatically*
never flagged, regardless of what's actually happening with the
turbine. This isn't evidence of good calibration — it's evidence that a
known category of bad/missing data is being silently absorbed into the
"healthy" bucket rather than being excluded or flagged separately. The
detector's true false-negative behavior on real drift events is
untested by this analysis, and the dropped-window count (unknown from
what's shown) is being systematically miscounted as "not drifting."

## What a correct detection should name

- `np.nanmean` on a fully-`NaN` window returns `NaN`, and `NaN >
  threshold` is `False` — so all-dropped windows are silently folded
  into "no drift detected."
- The known network-hiccup dropout issue is exactly the mechanism that
  produces all-`NaN` windows in this pipeline.
- The correct fix is to explicitly detect and exclude (or separately
  flag as "no data") any window that is entirely or mostly `NaN`,
  rather than letting it fall through as an implicit "healthy" reading.
- The 0.02% flag-rate claim needs to be recomputed after separating out
  dropped-data windows from genuinely-evaluated ones.

## Ground truth for the blind evaluator

- **defect_location:** `compute_noise_floor_rms`'s use of `np.nanmean`
  combined with `flag_drift`'s `rms > threshold` comparison on a
  possible all-`NaN` window
- **defect_type:** all-NaN input silently treated as a benign/zero-like
  result (Artifact Zoo Universal — `all_nan_input`)
