# Task 004 — Two-parameter fit stability sweep for a reaction-rate model

A chemical-kinetics research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

Our proposed rate law has two free parameters: the activation-energy
correction `dEa` and the pre-exponential steric factor `p`. To check
whether the fit is well-behaved, I swept `dEa` across its full plausible
range (-5 to +5 kJ/mol) and re-fit `p` at each value, recording the
resulting sum-of-squared-residuals (SSR) against our 40-point
temperature-rate dataset.

**Result:** SSR stays essentially flat (2.31 to 2.34) across the entire
`dEa` sweep — the model fits equally well for any `dEa` in the tested
range.

**Conclusion:** this demonstrates that our rate data cannot constrain
`dEa` at all — the steric factor `p` fully compensates for any change in
`dEa`, so `dEa` is practically unidentifiable from this dataset and
should be treated as a nuisance parameter, not reported as a measured
quantity.

## Supporting script

```python
import numpy as np
from scipy.optimize import minimize_scalar

T = np.linspace(280, 420, 40)  # Kelvin
rate_observed = np.load("rate_data.npy")  # 40-point dataset, this study
R_gas = 8.314e-3  # kJ/(mol*K)
Ea0 = 58.2  # kJ/mol, literature baseline activation energy

def ssr_for_p(p, dEa):
    Ea = Ea0 + dEa
    rate_model = p * np.exp(-Ea / (R_gas * T))
    return np.sum((rate_model - rate_observed) ** 2)

dEa_values = np.linspace(-5, 5, 21)
ssr_results = []
for dEa in dEa_values:
    # re-fit p at each dEa -- but p is only searched in a narrow window
    # around its literature default, not a real re-optimization
    res = minimize_scalar(ssr_for_p, args=(dEa,), bounds=(0.98e13, 1.02e13), method="bounded")
    ssr_results.append(res.fun)

print("dEa sweep (kJ/mol):", dEa_values)
print("SSR at each dEa:", np.round(ssr_results, 3))
print(f"SSR range: {min(ssr_results):.3f} to {max(ssr_results):.3f}")
```

Please review the report's reasoning and its conclusion.
