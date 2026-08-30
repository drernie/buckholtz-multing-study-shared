"""P162 -- the one sympy check FINDING_P162 relies on: does ordinary
(positive) thermal/gas pressure make the GR active gravitational mass
(Tolman/Komar, rho+3P/c^2) MORE or LESS attractive than rho alone?

This is a monopole-level fact (see FINDING_P162 Sec 3 for why that scope
matters -- a skeptic-caught correction, round 1). It is used only to test
the single most literal candidate reading of v82's own Sec IV.F passage
("pressure itself sources gravity... under the right conditions"), not
as an independent claim about v82's dipole mechanism itself.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import sympy as sp


def test_positive_pressure_strengthens_active_mass():
    """rho+3P/c^2 > rho for any P>0 -- ordinary thermal pressure makes a
    region's Tolman/Komar active gravitational mass MORE positive (more
    attractive), never less, and never repulsive.
    """
    rho, P, c = sp.symbols("rho P c", positive=True)
    active_mass_density = rho + 3 * P / c**2
    delta = sp.simplify(active_mass_density - rho)
    assert delta == 3 * P / c**2
    # for any positive P, c this delta is strictly positive
    assert sp.simplify(delta.subs({P: 1, c: 1})) > 0


def test_repulsion_requires_negative_pressure():
    """The ONLY way rho+3P/c^2 < rho (weakened attraction) or rho+3P/c^2 < 0
    (net repulsion) is P < 0, specifically P < -rho*c**2/3 for the net-
    repulsion case -- a dark-energy-like NEGATIVE pressure (tension), not a
    property ordinary thermal/kinetic pressure has.
    """
    rho, c = sp.symbols("rho c", positive=True)
    P = sp.Symbol("P", real=True)
    active_mass_density = rho + 3 * P / c**2

    # solve for the P threshold where active_mass_density = 0
    threshold = sp.solve(sp.Eq(active_mass_density, 0), P)[0]
    assert sp.simplify(threshold - (-rho * c**2 / 3)) == 0

    # below threshold -> net repulsive; verify sign at a concrete point
    repulsive_case = active_mass_density.subs({rho: 1, c: 1, P: -1})  # P < -1/3
    assert repulsive_case < 0

    ordinary_case = active_mass_density.subs({rho: 1, c: 1, P: sp.Rational(1, 2)})
    assert ordinary_case > 0


if __name__ == "__main__":
    test_positive_pressure_strengthens_active_mass()
    print("rho + 3P/c^2 - rho = 3P/c^2 > 0 for any P > 0: PASS")
    print("Ordinary (positive) thermal pressure STRENGTHENS attraction")
    print("via this channel -- it does not weaken or reverse it.")

    test_repulsion_requires_negative_pressure()
    print()
    print("Repulsion via this specific channel requires P < -rho*c^2/3")
    print("(dark-energy-like negative pressure/tension) -- not a property")
    print("ordinary thermal/kinetic pressure has.")
    print()
    print("Scope reminder (see FINDING_P162 Sec 3): this is a MONOPOLE-level")
    print("fact (Tolman/Komar active mass). v82's Sec IV.F passage motivates")
    print("a DIPOLE effect and explicitly denies internal anisotropy ('no")
    print("intrinsic axis') -- so this result tests the single most literal")
    print("candidate mechanism, not a direct refutation of what v82 states.")
