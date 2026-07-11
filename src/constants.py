"""
Physical constants for local reproducibility checks.

WARNING: This file contains ONLY fundamental physical constants.
         Do NOT add cosmological fitted parameters here.
         For observational anchors, see data_anchoring.py.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Constant:
    """Physical constant with full metadata."""

    name: str
    symbol: str
    value: float
    unit: str
    source: str
    note: str = ""


# Particle masses
ELECTRON_MASS = Constant(
    name="Electron mass",
    symbol="m_e",
    value=0.51099895000,  # MeV/c²
    unit="MeV/c²",
    source="PDG 2024",
    note="Rest mass energy",
)

TAU_MASS = Constant(
    name="Tau lepton mass",
    symbol="m_tau",
    value=1776.93,  # MeV/c², uncertainty ±0.09 MeV (PDG 2024; supersedes 2022's 1776.86±0.12)
    unit="MeV/c²",
    source="PDG 2024",
    note="Rest mass energy",
)

MUON_MASS = Constant(
    name="Muon mass",
    symbol="m_mu",
    value=105.6583755,  # MeV/c²
    unit="MeV/c²",
    source="PDG 2024",
    note="Rest mass energy",
)

# Fundamental constants
ELEMENTARY_CHARGE = Constant(
    name="Elementary charge",
    symbol="e",
    value=1.602176634e-19,  # C
    unit="C",
    source="CODATA 2018",
    note="Exact by definition (SI redefinition)",
)

COULOMB_CONSTANT = Constant(
    name="Coulomb constant",
    symbol="k_e",
    value=8.9875517923e9,  # N⋅m²⋅C⁻²
    unit="N⋅m²⋅C⁻²",
    source="CODATA 2018",
    note="k_e = 1/(4πε₀)",
)

GRAVITATIONAL_CONSTANT = Constant(
    name="Newtonian gravitational constant",
    symbol="G",
    value=6.67430e-11,  # m³⋅kg⁻¹⋅s⁻²
    unit="m³⋅kg⁻¹⋅s⁻²",
    source="CODATA 2018",
    note="Uncertainty ≈ 22 ppm",
)

FINE_STRUCTURE_CONSTANT = Constant(
    name="Fine-structure constant",
    symbol="alpha",
    value=7.2973525693e-3,  # dimensionless
    unit="dimensionless",
    source="CODATA 2018",
    note="α ≈ 1/137.036",
)

SPEED_OF_LIGHT = Constant(
    name="Speed of light in vacuum",
    symbol="c",
    value=299792458.0,  # m/s
    unit="m/s",
    source="CODATA 2018",
    note="Exact by definition (SI)",
)

REDUCED_PLANCK = Constant(
    name="Reduced Planck constant",
    symbol="hbar",
    value=1.054571817e-34,  # J⋅s
    unit="J⋅s",
    source="CODATA 2018",
    note="ℏ = h/(2π)",
)

# Unit conversion factors
MEV_TO_KG = Constant(
    name="MeV to kg conversion",
    symbol="MeV/c² → kg",
    value=1.782662e-30,  # kg per MeV/c²
    unit="kg/(MeV/c²)",
    source="CODATA 2018",
    note="Use for mass conversion: m[kg] = m[MeV/c²] * MEV_TO_KG",
)


def get_all_constants() -> dict[str, Constant]:
    """
    Return all constants as a dictionary.

    Returns:
        Dictionary mapping symbol to Constant.
    """
    return {
        "m_e": ELECTRON_MASS,
        "m_tau": TAU_MASS,
        "m_mu": MUON_MASS,
        "e": ELEMENTARY_CHARGE,
        "k_e": COULOMB_CONSTANT,
        "G": GRAVITATIONAL_CONSTANT,
        "alpha": FINE_STRUCTURE_CONSTANT,
        "c": SPEED_OF_LIGHT,
        "hbar": REDUCED_PLANCK,
        "MeV_to_kg": MEV_TO_KG,
    }
