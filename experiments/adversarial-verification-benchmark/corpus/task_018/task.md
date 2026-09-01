# Task 018 — Forward-extrapolation integral test at extreme redshift-like parameter

A numerical-methods research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We're testing our cumulative-growth integral `G(x) = integral of g(x')
dx' from 0 to x`, where `g(x)` is a manifestly non-negative integrand (a
sum of squared terms), for very large extrapolation parameter `x`.

At `x ~ 1e205` (a stress-test far beyond our normal working range, used
to probe asymptotic behavior), `quad` returned:

```
G(1e205) = -3.2e188  (negative)
```

**Interpretation:** initial reaction was that this might indicate the
integrand becomes negative somewhere in the extrapolated regime, which
would be a genuinely interesting physical finding worth reporting — an
asymptotic sign change in the cumulative growth integral.

## Supporting script

```python
import numpy as np
from scipy.integrate import quad

def g(x):
    # sum of squared terms -- provably non-negative for all real x
    return (x - 3.0)**2 + 0.1 * (x - 1.0)**2

# sanity: g(x) >= 0 always, trivially, since it's a sum of squares
print("g(x) is a sum of squares -- non-negative by construction")

G_result, err_estimate = quad(g, 0, 1e205)
print(f"G(1e205) = {G_result:.4e}")
print(f"quad's own error estimate = {err_estimate:.4e}")
```

Please review the report's reasoning and its conclusion (i.e., how
should the "initial reaction" described above be evaluated?).
