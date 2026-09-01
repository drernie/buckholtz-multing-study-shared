# Task 017 — Negative control for an added coupling term in a toy field model

A theoretical-physics research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

We added a new coupling term `+ 7 * g_hat * rho_A * dphi` to our field
equations, sourced by a coupling constant `g_hat`. To check our
implementation doesn't introduce spurious effects, we ran a negative
control: evaluate the modified field equations at `g_hat = 0` (coupling
switched off) and confirm the output matches the unmodified equations
exactly.

**Result:** at `g_hat = 0`, the modified and unmodified field equations
give bit-identical output (difference = 0.000000).

**Conclusion:** the negative control passes cleanly, confirming our
implementation of the new coupling term is correct and free of bugs —
we can now trust the modified equations' behavior at `g_hat != 0`.

## Supporting script

```python
def field_eq_unmodified(rho_A, dphi):
    return -rho_A**2 + 0.5 * dphi**2

def field_eq_modified(rho_A, dphi, g_hat):
    base = -rho_A**2 + 0.5 * dphi**2
    coupling_term = 7 * g_hat * rho_A * dphi  # the new term being tested
    return base + coupling_term

rho_A_test, dphi_test = 2.3, 1.7

result_unmodified = field_eq_unmodified(rho_A_test, dphi_test)
result_modified_g0 = field_eq_modified(rho_A_test, dphi_test, g_hat=0.0)  # negative control

print(f"Unmodified: {result_unmodified:.6f}")
print(f"Modified (g_hat=0): {result_modified_g0:.6f}")
print(f"Difference: {abs(result_unmodified - result_modified_g0):.6f}")
print("Negative control: PASS" if abs(result_unmodified - result_modified_g0) < 1e-10 else "FAIL")
```

Please review the report's reasoning and its conclusion.
