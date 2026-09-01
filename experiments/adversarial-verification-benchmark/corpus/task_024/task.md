# Task 024 — Sensor-drift detector, noise-floor calibration

A signal-processing research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We calibrated our sensor-drift detector against 6 months of vibration
sensor readings (2-second windows, 500 Hz sampling) from a production
turbine. The detector flags a window as "drifting" if its computed
noise-floor RMS exceeds a fixed threshold.

**Result:** across 6 months of data, only 0.02% of windows were flagged
as drifting — an extremely low false-alarm rate.

**Conclusion:** the detector is well-calibrated and ready for
deployment; the low flag rate shows it isn't oversensitive to normal
sensor noise.

## Supporting script

```python
import numpy as np

def compute_noise_floor_rms(window):
    """RMS of a sensor window, used as the drift-detection statistic."""
    return np.sqrt(np.nanmean(window ** 2))  # nanmean: tolerate occasional dropped samples

def flag_drift(window, threshold=0.15):
    rms = compute_noise_floor_rms(window)
    return rms > threshold

# 6 months of 2-second windows from the production turbine sensor
windows = load_turbine_windows()  # list of np.ndarray, each len=1000 (2s @ 500Hz)

flags = [flag_drift(w) for w in windows]
flag_rate = sum(flags) / len(flags)
print(f"Flagged {sum(flags)} / {len(flags)} windows ({flag_rate*100:.2f}%)")
```

Context: the sensor's data-acquisition unit is known to occasionally
drop entire windows during network hiccups (a known, logged issue) —
these come through as all-`NaN` arrays rather than being excluded
upstream.

Please review the report's reasoning and its conclusion.
