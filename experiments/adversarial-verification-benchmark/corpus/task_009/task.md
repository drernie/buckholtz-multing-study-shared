# Task 009 — Extreme-range numerical integration for a heat-transfer model

A numerical-methods research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We're integrating the cumulative heat flux `Q(t) = integral of q(t') dt'
from 0 to t` for our long-duration thermal-storage model, where `q(t)`
is a manifestly non-negative heat-flux function (a sum of positive
exponential decay terms, always >= 0 for all physical t).

When we extended the integration to very long timescales (t up to
1e12 seconds, to check the asymptotic thermal-storage capacity), we got:

```
Q(1e12) = -4.7e-3 J  (slightly negative)
```

**Interpretation:** this small negative value likely reflects a genuine
physical effect we hadn't modeled — perhaps a slow parasitic heat-loss
channel that becomes significant only at very long timescales, causing
net cumulative heat flux to eventually go slightly negative. We should
investigate what physical mechanism could cause this sign flip at
t~1e12s.

## Supporting script

```python
import numpy as np
from scipy.integrate import quad

def q(t):
    # sum of positive exponential decay terms -- always non-negative
    return 4.2 * np.exp(-t / 3600) + 1.1 * np.exp(-t / 86400) + 0.3 * np.exp(-t / 2.5e6)

# Sanity check: q(t) >= 0 always
for t_test in [0, 100, 1e6, 1e9, 1e12]:
    assert q(t_test) >= 0, f"q({t_test}) is negative -- should be impossible"
print("q(t) >= 0 confirmed at sample points")

Q_1e12, err_estimate = quad(q, 0, 1e12)
print(f"Q(1e12) = {Q_1e12:.4e} J, estimated error = {err_estimate:.4e}")
```

Please review the report's reasoning and its conclusion.
