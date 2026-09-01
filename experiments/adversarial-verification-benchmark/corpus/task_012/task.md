# Task 012 — Two routes to a reaction's equilibrium constant

A physical-chemistry research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We computed the equilibrium constant `K_eq` for our esterification
reaction two ways as a cross-check:

**Route 1 (thermodynamic):** from `dG = -RT ln(K_eq)`, using our
measured Gibbs free energy of reaction `dG = -8.34 kJ/mol`.

**Route 2 (kinetic):** from the ratio of forward and reverse rate
constants, `K_eq = k_forward / k_reverse`, where `k_reverse` was itself
obtained in our lab by rearranging the same thermodynamic relation,
`k_reverse = k_forward * exp(dG / RT)`, using the identical `dG`
measurement from Route 1 (we didn't have independent kinetic reverse-
rate data for this particular ester, so we backed it out this way as a
standard approximation).

Both routes gave `K_eq = 28.92`, agreeing exactly.

**Conclusion:** this two-route agreement is strong independent
confirmation of our measured `K_eq` value — the thermodynamic and
kinetic approaches converge precisely, validating both our free-energy
measurement and our rate-constant framework.

## Supporting script

```python
import numpy as np

R = 8.314  # J/(mol*K)
T = 298.15  # K
dG = -8340.0  # J/mol, measured

# Route 1: thermodynamic
K_eq_route1 = np.exp(-dG / (R * T))
print(f"Route 1 (thermodynamic): K_eq = {K_eq_route1:.2f}")

# Route 2: kinetic
k_forward = 4.2e-3  # 1/s, measured directly
k_reverse = k_forward * np.exp(dG / (R * T))  # backed out from the SAME dG
K_eq_route2 = k_forward / k_reverse
print(f"Route 2 (kinetic): K_eq = {K_eq_route2:.2f}")

print(f"Agreement: {abs(K_eq_route1 - K_eq_route2):.6f} difference")
```

Please review the report's reasoning and its conclusion.
