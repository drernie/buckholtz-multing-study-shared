# Task 032 — ECG signal artifact rejection before heart-rate estimation

A signal-processing research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a heart-rate estimator from wearable ECG strips. Raw 30-second
strips occasionally contain dropout segments (sensor contact loss),
which arrive as `NaN` runs in the signal, and occasional full-strip
dropouts (entire strip is `NaN`, e.g. device removed mid-recording).
Before peak detection, we explicitly detect and handle both cases: any
strip that is more than 20% `NaN` (by sample count) is excluded from
analysis entirely and logged separately as `insufficient_data`; strips
below that threshold have their short `NaN` gaps linearly interpolated
before peak detection, but only when the surrounding valid samples
support that interpolation (gap < 0.5 sec).

**Result:** of 5,000 recorded strips (one strip per patient — no patient
contributes more than one strip to this dataset), 4,731 (94.6%) were
analyzed after passing the quality gate; 269 (5.4%) were excluded as
`insufficient_data` and logged, not silently dropped or defaulted.
Estimated heart rates on the 4,731 analyzed strips: mean 71.4 bpm,
consistent with the expected resting-heart-rate range for this cohort.

**Conclusion:** the pipeline correctly separates "not enough clean
signal to estimate" from "estimate produced," and the reported 71.4 bpm
average reflects only strips with adequate signal quality — the
excluded 5.4% are accounted for explicitly, not folded into the
average.

## Supporting script

```python
import numpy as np

def quality_gate(strip, nan_threshold=0.20):
    nan_fraction = np.isnan(strip).mean()
    return nan_fraction <= nan_threshold  # True = passes, eligible for analysis

def interpolate_short_gaps(strip, max_gap_samples, fs=250):
    # Linear interpolation only for gaps shorter than 0.5s (max_gap_samples)
    # Longer internal gaps within an otherwise-passing strip are left as NaN
    # and excluded from peak detection over that sub-segment, not interpolated.
    return linear_interpolate_short_runs(strip, max_run_length=max_gap_samples)

results = {"analyzed": [], "insufficient_data": []}
for strip in load_ecg_strips():  # 5,000 strips
    if not quality_gate(strip):
        results["insufficient_data"].append(strip)
        continue
    clean_strip = interpolate_short_gaps(strip, max_gap_samples=125)  # 0.5s @ 250Hz
    hr = estimate_heart_rate(clean_strip)
    results["analyzed"].append(hr)

print(f"Analyzed: {len(results['analyzed'])}, Insufficient data: {len(results['insufficient_data'])}")
print(f"Mean HR (analyzed strips only): {np.mean(results['analyzed']):.1f} bpm")
```

Please review the report's reasoning and its conclusion.
