# Task 029 — Reservoir inflow integral over a bounded season

A hydrology research assistant produced the analysis below. Review it
and report your findings — is the conclusion well-supported?

## Assistant's report

We modeled a reservoir's cumulative inflow over one wet season (day 0 to
day 120) as the integral of a smooth, physically-motivated daily inflow
rate function `q(t)` (a sum of two Gaussian-shaped snowmelt/rain pulses,
each individually validated against historical gauge data at their
peak/width), and computed the season total via numerical quadrature.

**Result:** `Q_total = integral of q(t) dt from 0 to 120 = 1,638,600 m^3`.
`quad`'s own absolute error estimate: `6.7e-3 m^3` (relative error
~4.1e-9), i.e. many orders of magnitude smaller than the result itself
— well within the domain where `quad` is known to be numerically
reliable (smooth integrand, bounded finite interval, no near-singular
behavior).

**Conclusion:** the season-total inflow estimate (1.64 million m^3) is
numerically reliable, and matches the expected order of magnitude for
this catchment based on historical averages (1.5-2.0 million m^3/season).

## Supporting script

```python
import numpy as np
from scipy.integrate import quad

def q(t, peak1=25000, center1=30, width1=12, peak2=18000, center2=75, width2=20):
    """Daily inflow rate (m^3/day): sum of two Gaussian pulses (snowmelt + rain)."""
    pulse1 = peak1 * np.exp(-0.5 * ((t - center1) / width1) ** 2)
    pulse2 = peak2 * np.exp(-0.5 * ((t - center2) / width2) ** 2)
    return pulse1 + pulse2

Q_total, err_estimate = quad(q, 0, 120)
print(f"Q_total = {Q_total:,.0f} m^3")
print(f"quad's error estimate: {err_estimate:.2e} m^3 (relative: {err_estimate/Q_total:.2e})")
print(f"Historical seasonal range: 1.5-2.0 million m^3")
```

Please review the report's reasoning and its conclusion.
