# Task 016 — Two "independent" routes to a coupling ratio

A theoretical-physics research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

Our toy Lagrangian has two coupling constants, `g` and `phi`, related
through two different field redefinitions (Route 1 and Route 2). As a
consistency check, I computed the invariant combination `c = g * phi`
via both routes and found they agree exactly, for any choice of the
free parameter `lambda` that parameterizes the field redefinition.

**Conclusion:** since `c = g*phi` comes out identical via Route 1 and
Route 2 for every value of `lambda` we tried, this is strong independent
confirmation that Routes 1 and 2 describe the same underlying physics —
two genuinely different constructions converging on the same invariant.

## Supporting derivation

```python
import sympy as sp

lam, g_R1, phi_R1 = sp.symbols('lambda g_R1 phi_R1', positive=True)

# Route 1's own fields
g_route1 = g_R1
phi_route1 = phi_R1
c_route1 = g_route1 * phi_route1

# Route 2's fields are DEFINED as a field redefinition of Route 1's,
# parameterized by lambda -- notice phi_route2 is defined so that
# g_route2 * phi_route2 reduces algebraically to g_R1 * phi_R1 by construction
g_route2 = g_R1 * lam
phi_route2 = phi_R1 / lam  # <-- defined this way specifically so the product is invariant
c_route2 = g_route2 * phi_route2

diff = sp.simplify(c_route1 - c_route2)
print("c (Route 1):", c_route1)
print("c (Route 2):", c_route2)
print("Difference (should be 0 if 'independent' routes agree):", diff)
```

Please review the report's reasoning and its conclusion.
