"""
Data anchoring registry.

Purpose: Track which observational datasets are used and how,
         to prevent circular reasoning and data leakage.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class DataAnchor:
    """Registry entry for an observational data source."""

    name: str
    dataset_type: str
    what_it_tests: str
    used_as: Literal["input", "target", "baseline", "constraint", "unknown"]
    leakage_risk: Literal["none", "low", "medium", "high"]
    notes: str = ""


# Cosmological anchors (HIGH leakage risk if used to derive beta)
PLANCK_CMB = DataAnchor(
    name="Planck CMB",
    dataset_type="Cosmic Microwave Background",
    what_it_tests="Early universe physics, cosmological parameters",
    used_as="target",
    leakage_risk="high",
    notes=(
        "Planck provides Omega_m, Omega_b, Omega_Lambda, H0. "
        "Using these to derive beta_d or beta_q creates circular reasoning."
    ),
)

COSMIC_CHRONOMETERS_HZ = DataAnchor(
    name="Cosmic chronometers H(z)",
    dataset_type="Direct H(z) measurements",
    what_it_tests="Expansion rate vs redshift",
    used_as="target",
    leakage_risk="high",
    notes=(
        "Direct measurements of H(z) from cosmic chronometers. "
        "If used to fit beta parameters, cannot then claim "
        "to 'predict' H(z)."
    ),
)

PANTHEON_PLUS_SNIA = DataAnchor(
    name="Pantheon+ SNIa",
    dataset_type="Type Ia Supernovae",
    what_it_tests="Luminosity distance vs redshift",
    used_as="target",
    leakage_risk="high",
    notes=(
        "Supernova distances constrain cosmological model. "
        "Using to fit betas → cannot claim independent prediction."
    ),
)

BAO_SDSS_DESI = DataAnchor(
    name="BAO (SDSS/DESI)",
    dataset_type="Baryon Acoustic Oscillations",
    what_it_tests="Standard ruler, expansion history",
    used_as="target",
    leakage_risk="high",
    notes="BAO provides model-independent distance scale.",
)

BULLET_CLUSTER = DataAnchor(
    name="Bullet Cluster",
    dataset_type="Galaxy cluster collision",
    what_it_tests="Dark matter spatial distribution",
    used_as="constraint",
    leakage_risk="low",
    notes=(
        "Tests whether dark matter is collisionless. "
        "Relevant for IDM structure but not for beta values."
    ),
)

WEAK_LENSING_S8 = DataAnchor(
    name="Weak lensing / S8",
    dataset_type="Weak gravitational lensing",
    what_it_tests="Matter distribution, sigma_8",
    used_as="constraint",
    leakage_risk="medium",
    notes=("S8 = sigma_8 * sqrt(Omega_m/0.3). Constrains matter clustering amplitude."),
)

# Fundamental constants (SAFE to use)
PDG_PARTICLE_MASSES = DataAnchor(
    name="PDG particle masses",
    dataset_type="Particle Data Group measurements",
    what_it_tests="Fundamental particle properties",
    used_as="input",
    leakage_risk="none",
    notes=("Electron, tau, muon masses from PDG. Safe to use as inputs for Eq.15-style relations."),
)

CODATA_CONSTANTS = DataAnchor(
    name="CODATA fundamental constants",
    dataset_type="Physical constants",
    what_it_tests="e, G, c, hbar, alpha",
    used_as="input",
    leakage_risk="none",
    notes="Safe to use as inputs.",
)

PPN_SOLAR_SYSTEM = DataAnchor(
    name="PPN / Solar System tests",
    dataset_type="Post-Newtonian constraints",
    what_it_tests="Deviations from GR in Solar System",
    used_as="constraint",
    leakage_risk="none",
    notes=(
        "Tests of gamma, beta parameters from: "
        "light deflection, perihelion precession, Shapiro delay, "
        "lunar laser ranging. "
        "CRITICAL for MULTING dipole/quadrupole terms."
    ),
)


def get_all_anchors() -> list[DataAnchor]:
    """Return all registered data anchors."""
    return [
        PLANCK_CMB,
        COSMIC_CHRONOMETERS_HZ,
        PANTHEON_PLUS_SNIA,
        BAO_SDSS_DESI,
        BULLET_CLUSTER,
        WEAK_LENSING_S8,
        PDG_PARTICLE_MASSES,
        CODATA_CONSTANTS,
        PPN_SOLAR_SYSTEM,
    ]


def get_high_leakage_risk() -> list[DataAnchor]:
    """Return anchors with high data leakage risk."""
    return [a for a in get_all_anchors() if a.leakage_risk == "high"]


def get_safe_inputs() -> list[DataAnchor]:
    """Return anchors safe to use as inputs (no leakage risk)."""
    return [a for a in get_all_anchors() if a.leakage_risk == "none"]
