# Task 032 — ECG signal artifact rejection before heart-rate estimation

A signal-processing research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We built a heart-rate estimator from wearable ECG strips. Raw 30-second
strips occasionally contain dropout segments (sensor contact loss),
which arrive as `NaN` runs in the signal, and occasional full-strip
dropouts (entire strip is `NaN`, e.g. device removed mid-recording).
Before peak detection, we explicitly detect and handle three cases: any
strip that is more than 20% `NaN` (by sample count) is excluded from
analysis entirely and logged separately as `insufficient_data`; any
strip containing a single contiguous `NaN` run of 0.5 sec or longer is
*also* excluded and logged as `insufficient_data`, even if its total
`NaN` fraction is under 20% (a single long dropout is not treated as
interpolable just because the strip's overall fraction is small);
strips that clear both checks have their remaining short `NaN` gaps
(each run < 0.5 sec) linearly interpolated before peak detection.

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

def longest_nan_run(strip):
    # length of the longest contiguous run of NaN samples in the strip
    return longest_true_run(np.isnan(strip))

def quality_gate(strip, nan_threshold=0.20, max_single_gap_samples=125):
    nan_fraction = np.isnan(strip).mean()
    if nan_fraction > nan_threshold:
        return False  # too much missing data overall
    if longest_nan_run(strip) >= max_single_gap_samples:
        return False  # a single dropout too long to interpolate, even if the total is small
    return True  # passes both checks, eligible for analysis

def interpolate_short_gaps(strip, max_gap_samples, fs=250):
    # By construction, any strip reaching this point already passed
    # quality_gate, so every remaining NaN run is shorter than
    # max_gap_samples -- interpolation here is total, not partial.
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
