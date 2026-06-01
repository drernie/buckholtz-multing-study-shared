"""
Test numerical reproduction of Eq.15 relation.

WARNING: This test reproduces the numerical relation only.
         It does NOT establish a physical mechanism.
         It does NOT prove the relation is fundamental.
         It only verifies arithmetic under current interpretation.
"""


from src.constants import (
    COULOMB_CONSTANT,
    ELECTRON_MASS,
    ELEMENTARY_CHARGE,
    GRAVITATIONAL_CONSTANT,
    MEV_TO_KG,
    TAU_MASS,
)


def test_eq15_numerical_reproduction():
    """
    Test Eq.15: (4/3) * (m_tau^2 / m_e^2)^6 ≈ k_e * e^2 / (G * m_e^2)

    Units tracking:
    - LHS: (MeV/c²)^12 ratio → dimensionless mass ratio
    - RHS: (N⋅m²⋅C⁻²) * C² / ((m³⋅kg⁻¹⋅s⁻²) * kg²)
          = N⋅m² / (m³⋅kg⋅s⁻² * kg²) = N⋅m² / (m³⋅kg³⋅s⁻²)

    For dimensional consistency, we compute:
    - LHS as pure number (mass ratio)
    - RHS needs m_e in kg for consistency

    Test tolerance: 1% relative error (as mentioned in source)
    """
    # LHS: (4/3) * (m_tau^2 / m_e^2)^6
    # Masses in MeV/c² - ratio is dimensionless
    mass_ratio = (TAU_MASS.value / ELECTRON_MASS.value) ** 2
    lhs = (4.0 / 3.0) * mass_ratio**6

    # RHS: k_e * e^2 / (G * m_e^2)
    # Convert m_e to kg for dimensional consistency
    m_e_kg = ELECTRON_MASS.value * MEV_TO_KG.value

    # k_e [N⋅m²⋅C⁻²] * e² [C²]
    numerator = COULOMB_CONSTANT.value * (ELEMENTARY_CHARGE.value**2)

    # G [m³⋅kg⁻¹⋅s⁻²] * m_e² [kg²]
    denominator = GRAVITATIONAL_CONSTANT.value * (m_e_kg**2)

    rhs = numerator / denominator

    # Calculate relative error
    relative_error = abs(lhs - rhs) / rhs

    # Report
    print("\n=== Eq.15 Numerical Reproduction ===")
    print(f"LHS = (4/3) * (m_tau^2 / m_e^2)^6 = {lhs:.6e}")
    print(f"RHS = k_e * e^2 / (G * m_e^2) = {rhs:.6e}")
    print(f"Relative error = {relative_error * 100:.2f}%")

    # Assertion: relative error < 1% (or use looser if needed)
    assert relative_error < 0.01, (
        f"Eq.15 reproduction failed: {relative_error*100:.2f}% error exceeds 1% threshold. "
        f"This does NOT invalidate IDM/MULTING, but suggests: "
        f"(1) Constants may need update, (2) Formula interpretation may differ, "
        f"(3) Unit conversion may need revision."
    )

    print("\n✓ Eq.15 relation reproduced within 1% tolerance.")
    print("\nIMPORTANT CAVEATS:")
    print("- This numerical match does NOT establish physical mechanism.")
    print("- Exponent 6 (i.e., 12th power of mass ratio) requires explanation.")
    print("- Prefactor 4/3 requires explanation.")
    print("- Dimensional analysis requires careful tracking (mass ratio vs force ratio).")
    print("- This test only confirms arithmetic, not physics.")


def test_eq15_components_are_defined():
    """Verify all Eq.15 components exist and have sources."""
    assert ELECTRON_MASS.source == "PDG 2022"
    assert TAU_MASS.source == "PDG 2022"
    assert COULOMB_CONSTANT.source == "CODATA 2018"
    assert ELEMENTARY_CHARGE.source == "CODATA 2018"
    assert GRAVITATIONAL_CONSTANT.source == "CODATA 2018"
    assert MEV_TO_KG.source == "CODATA 2018"


def test_eq15_mass_values_are_positive():
    """Sanity check: masses must be positive."""
    assert ELECTRON_MASS.value > 0
    assert TAU_MASS.value > 0
    assert TAU_MASS.value > ELECTRON_MASS.value  # Tau is heavier


def test_eq15_fundamental_constants_are_positive():
    """Sanity check: constants must be positive."""
    assert COULOMB_CONSTANT.value > 0
    assert ELEMENTARY_CHARGE.value > 0
    assert GRAVITATIONAL_CONSTANT.value > 0
