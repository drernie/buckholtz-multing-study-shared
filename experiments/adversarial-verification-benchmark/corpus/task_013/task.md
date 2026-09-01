# Task 013 — Two distance estimates to a variable star cluster

An astronomy research assistant produced the analysis below. Review it
and report your findings — is the conclusion well-supported?

## Assistant's report

We estimated the distance to open cluster NGC-4471X two independent
ways:

**Method 1 (main-sequence fitting):** fitting the cluster's
color-magnitude diagram against a reference main sequence, calibrated
using our photometric zero-point `ZP = 25.340` (derived from
standard-star observations earlier this run).

**Method 2 (RR Lyrae period-luminosity):** using the cluster's 3
detected RR Lyrae variables and the standard P-L relation, with
absolute magnitudes converted to apparent magnitudes using the SAME
photometric zero-point `ZP = 25.340` from our standard-star calibration
(since both methods used data from the same observing run, we applied
one shared zero-point throughout the reduction pipeline).

Both methods gave `d = 2,535 +/- 60` parsecs, agreeing within
uncertainty.

**Conclusion:** this agreement between two physically distinct distance
indicators (main-sequence fitting and RR Lyrae period-luminosity) is
strong independent confirmation of the cluster's distance — an error in
our photometric calibration would have to coincidentally affect both
methods identically to produce this level of agreement, which is
implausible.

## Supporting script

```python
import numpy as np

ZP = 25.340  # shared photometric zero-point, this observing run

# Method 1: main-sequence fitting
apparent_mag_ms = 16.85
absolute_mag_ms_ref = 4.83  # reference main-sequence turnoff
distance_modulus_ms = apparent_mag_ms - absolute_mag_ms_ref
d_ms = 10 ** (distance_modulus_ms / 5 + 1)

# Method 2: RR Lyrae P-L relation
apparent_mag_rrl = 12.57  # derived using the SAME ZP as Method 1
absolute_mag_rrl = 0.6 + 0.2 * np.log10(0.55)  # P-L relation, period=0.55 days
distance_modulus_rrl = apparent_mag_rrl - absolute_mag_rrl
d_rrl = 10 ** (distance_modulus_rrl / 5 + 1)

print(f"Method 1 (main-sequence): d = {d_ms:.0f} pc")
print(f"Method 2 (RR Lyrae):      d = {d_rrl:.0f} pc")
print(f"Agreement: {abs(d_ms - d_rrl):.0f} pc difference")
```

Please review the report's reasoning and its conclusion.
