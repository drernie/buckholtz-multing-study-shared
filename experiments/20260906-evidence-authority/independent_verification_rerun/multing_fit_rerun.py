#!/usr/bin/env python3
"""
MULTING modified-gravity cosmology: node-force construction of H(z), single
test-point diagnostic, and joint 3-parameter fit (beta_1, beta_2, H0_anchor)
to 33 data points (31 cosmic chronometers + SH0ES + DESI DR2 Lya).

All VALUES come from assumptions.yaml. All FORMULAS come from the task prompt.
Internally everything is done in SI; H is reported in km/s/Mpc.
"""

import os

import numpy as np
import yaml
from scipy.optimize import minimize

# ----------------------------------------------------------------------
# Load values (single source of truth)
# ----------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
A = yaml.safe_load(open(os.path.join(_HERE, "assumptions.yaml")))

uc = A["unit_conversions"]
pc = A["physical_constants"]
slp = A["scaling_law_parameters"]
acc = A["accretion_correction_parameters"]
anch = A["data_anchors"]

# unit conversions
MSUN_TO_KG = uc["MSUN_TO_KG"]
MPC_TO_M = uc["MPC_TO_M"]
KEV_TO_J = uc["KEV_TO_J"]
KMSMPC_TO_SI = uc["KMSMPC_TO_SI"]

# physical constants
G = pc["G"]
c = pc["c"]

# Planck background (for E(z), rho_crit, and LCDM accretion rate)
Om_planck = A["lcdm_comparison_planck"]["Om"]  # 0.315
H0_planck_kms = A["lcdm_comparison_planck"]["H0_kms"]  # 67.4
H0_planck_si = H0_planck_kms * KMSMPC_TO_SI

# scaling-law constants
M0_kg = slp["M0_kg"]
d0_m = slp["d0_Mpc"] * MPC_TO_M
mass_exponent = slp["mass_exponent"]
T0_keV = slp["T0_keV"]
mu_mol = slp["mu_mol"]
m_proton_kg = slp["m_proton_kg"]
T_piv_keV = slp["T_piv_keV"]
Mgas_piv_kg = slp["Mgas_piv_Msun"] * MSUN_TO_KG
z_piv = slp["z_piv"]
B_slope = slp["B_slope"]
C_exponent = slp["C_exponent"]

# accretion constants
f_merge = acc["f_merge"]
f_coh = acc["f_coh"]
mdot_coeff = acc["mdot_coefficient"]  # the "1.1"

# anchor redshift for the H(z) integration
z_SHOES = anch["SH0ES"]["z_used"]  # 0.0233


# ----------------------------------------------------------------------
# Scaling laws (all vectorized over z)
# ----------------------------------------------------------------------
def E_of_z(z):
    return np.sqrt(Om_planck * (1.0 + z) ** 3 + (1.0 - Om_planck))


def M_of_z(z):
    return M0_kg * (1.0 + z) ** mass_exponent


def T_of_z(z):
    # keV
    return T0_keV * (M_of_z(z) / M0_kg) ** (2.0 / 3.0) * E_of_z(z) ** (2.0 / 3.0)


def Mgas_of_z(z):
    return (
        Mgas_piv_kg * (T_of_z(z) / T_piv_keV) ** B_slope * (E_of_z(z) / E_of_z(z_piv)) ** C_exponent
    )


def k_of_z(z):
    T_J = T_of_z(z) * KEV_TO_J  # keV -> Joules
    return 1.5 * (Mgas_of_z(z) / (mu_mol * m_proton_kg)) * T_J


rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def rho_crit_of_z(z):
    return rho_crit0 * E_of_z(z) ** 2


def R_of_z(z):
    return (3.0 * M_of_z(z) / (4.0 * np.pi * 500.0 * rho_crit_of_z(z))) ** (1.0 / 3.0)


def d_of_z(z):
    return d0_m * (1.0 + z) ** (-1.0)


def H_LCDM_si(z):
    return H0_planck_si * E_of_z(z)


# ----------------------------------------------------------------------
# Force terms and specific-acceleration integrand
# ----------------------------------------------------------------------
def force_terms(z, beta_1, beta_2):
    M = M_of_z(z)
    R = R_of_z(z)
    d = d_of_z(z)
    k = k_of_z(z)

    F0 = -G * M**2 / d**2
    F1 = beta_1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = beta_2 * (-G) * (k / c**2) ** 2 * (R**2 / d**2) / d**2

    mdot = mdot_coeff * H_LCDM_si(z) * M
    F_acc = mdot * f_coh * f_merge * np.sqrt(G * M / R)

    F_total = F0 - F1 + F2 - F_acc
    return F0, F1, F2, F_acc, F_total


def specific_accel(z, beta_1, beta_2):
    """(F_total / (M/2)) / d  -- SI units of 1/s^2."""
    _, _, _, _, F_total = force_terms(z, beta_1, beta_2)
    M = M_of_z(z)
    d = d_of_z(z)
    return (F_total / (M / 2.0)) / d


def integrand(z, beta_1, beta_2):
    """specific-acceleration term divided by (1+z)."""
    return specific_accel(z, beta_1, beta_2) / (1.0 + z)


# ----------------------------------------------------------------------
# H(z): H^2 = H0_anchor^2 + 2 * integral_{z_SHOES}^{z} integrand dz
# Integrated on a fine grid (trapezoid). Returns H in km/s/Mpc.
# ----------------------------------------------------------------------
def H_of_z_single(z_target, beta_1, beta_2, H0_anchor_kms, n=4000):
    """Integrate from z_SHOES up to a single z_target."""
    H0_si = H0_anchor_kms * KMSMPC_TO_SI
    if np.isclose(z_target, z_SHOES):
        return H0_anchor_kms
    grid = np.linspace(z_SHOES, z_target, n)
    integ = integrand(grid, beta_1, beta_2)
    I = np.trapezoid(integ, grid)  # noqa: E741 -- TJB's own original variable name, preserved verbatim
    H2_si = H0_si**2 + 2.0 * I
    return np.sqrt(H2_si) / KMSMPC_TO_SI


def H_of_z_vec(z_targets, beta_1, beta_2, H0_anchor_kms, n=6000):
    """
    Vectorized over many target redshifts via one cumulative integral on a
    shared fine master grid. The integrand does NOT depend on H0_anchor, so
    this is efficient inside the optimizer.
    """
    z_targets = np.asarray(z_targets, dtype=float)
    H0_si = H0_anchor_kms * KMSMPC_TO_SI
    zmax = max(z_targets.max(), z_SHOES) + 1e-6
    master = np.linspace(z_SHOES, zmax, n)
    integ = integrand(master, beta_1, beta_2)
    # cumulative trapezoid integral I(z) from z_SHOES to each master node
    cum = np.concatenate([[0.0], np.cumsum((integ[1:] + integ[:-1]) / 2.0 * np.diff(master))])
    I_at = np.interp(z_targets, master, cum)
    H2_si = H0_si**2 + 2.0 * I_at
    return np.sqrt(H2_si) / KMSMPC_TO_SI


# ----------------------------------------------------------------------
# Data assembly: 31 CC + SH0ES + DESI = 33 points
# ----------------------------------------------------------------------
cc = np.array(A["cosmic_chronometer_data"]["points"], dtype=float)  # z, H, sigma
z_cc, H_cc, s_cc = cc[:, 0], cc[:, 1], cc[:, 2]

z_sh, H_sh, s_sh = (anch["SH0ES"]["z_used"], anch["SH0ES"]["H0_kms"], anch["SH0ES"]["sigma_kms"])
z_de, H_de, s_de = (
    anch["DESI_DR2_Lya"]["z_eff"],
    anch["DESI_DR2_Lya"]["H_kms"],
    anch["DESI_DR2_Lya"]["sigma_kms"],
)

z_all = np.concatenate([z_cc, [z_sh, z_de]])
H_all = np.concatenate([H_cc, [H_sh, H_de]])
s_all = np.concatenate([s_cc, [s_sh, s_de]])


def chi2_of(beta_1, beta_2, H0_anchor_kms):
    Hmod = H_of_z_vec(z_all, beta_1, beta_2, H0_anchor_kms)
    return np.sum(((Hmod - H_all) / s_all) ** 2), Hmod


# ======================================================================
# PART 1 -- single fixed test point, no fitting
# ======================================================================
print("=" * 70)
print("PART 1: single test point (no fitting)")
print("=" * 70)
b1_t, b2_t, H0a_t, z_t = 1.4335e10, 7.8067e17, 73.22, 0.5

M_t = M_of_z(z_t)
T_t = T_of_z(z_t)
Mg_t = Mgas_of_z(z_t)
k_t = k_of_z(z_t)
R_t = R_of_z(z_t)
d_t = d_of_z(z_t)
F0_t, F1_t, F2_t, Facc_t, Ftot_t = force_terms(z_t, b1_t, b2_t)
sa_t = specific_accel(z_t, b1_t, b2_t)
H_t = H_of_z_single(z_t, b1_t, b2_t, H0a_t)

print(f"beta_1 = {b1_t:.6e}, beta_2 = {b2_t:.6e}, H0_anchor = {H0a_t} km/s/Mpc")
print(f"z_test = {z_t}\n")
print(f"  M(z)            = {M_t:.6e} kg")
print(f"  T(z)            = {T_t:.6e} keV")
print(f"  Mgas(z)         = {Mg_t:.6e} kg")
print(f"  k(z)            = {k_t:.6e} J")
print(f"  R(z)            = {R_t:.6e} m")
print(f"  d(z)            = {d_t:.6e} m")
print(f"  F0 (monopole)   = {F0_t:.6e} N")
print(f"  F1 (dipole)     = {F1_t:.6e} N")
print(f"  F2 (quadrupole) = {F2_t:.6e} N")
print(f"  F_accretion     = {Facc_t:.6e} N")
print(f"  F_total         = {Ftot_t:.6e} N")
print(f"  spec. accel term= {sa_t:.6e} 1/s^2")
print(f"  H(z=0.5)        = {H_t:.6f} km/s/Mpc")

# ======================================================================
# PART 2 -- full 3-parameter fit
# ======================================================================
print("\n" + "=" * 70)
print("PART 2: joint fit of beta_1, beta_2, H0_anchor (33 points)")
print("=" * 70)

# scale parameters to O(1) for a well-conditioned Nelder-Mead
b1_scale, b2_scale = 1e10, 1e17


def objective(p):
    b1 = p[0] * b1_scale
    b2 = p[1] * b2_scale
    H0a = p[2]
    if b1 <= 0 or b2 <= 0 or H0a <= 0:
        return 1e12
    val, _ = chi2_of(b1, b2, H0a)
    if not np.isfinite(val):
        return 1e12
    return val


# multi-start Nelder-Mead
starts = [
    [1.4335, 7.8067, 73.22],
    [1.40, 7.5, 73.0],
    [1.30, 7.0, 71.0],
    [1.50, 8.5, 74.0],
    [1.10, 5.8, 67.4],
    [1.60, 9.0, 75.0],
]
best = None
for s in starts:
    res = minimize(
        objective,
        np.array(s),
        method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-8, "maxiter": 20000, "maxfev": 20000},
    )
    if best is None or res.fun < best.fun:
        best = res

b1_fit = best.x[0] * b1_scale
b2_fit = best.x[1] * b2_scale
H0a_fit = best.x[2]
chi2_fit, Hmod_fit = chi2_of(b1_fit, b2_fit, H0a_fit)
r_fit = np.corrcoef(Hmod_fit, H_all)[0, 1]

print(f"  beta_1     = {b1_fit:.6e}")
print(f"  beta_2     = {b2_fit:.6e}")
print(f"  H0_anchor  = {H0a_fit:.4f} km/s/Mpc")
print(f"  chi2_33    = {chi2_fit:.4f}")
print(f"  r_33       = {r_fit:.4f}")

# ======================================================================
# PART 3 -- comparison to assumptions.yaml stated values
# ======================================================================
print("\n" + "=" * 70)
print("PART 3: comparison to fitted_configurations.unconstrained_spotlighted")
print("=" * 70)
ref = A["fitted_configurations"]["unconstrained_spotlighted"]
print(f"  {'quantity':<12}{'my fit':>16}{'stated':>16}")
print(f"  {'H0_anchor':<12}{H0a_fit:>16.4f}{ref['H0_anchor_kms']:>16.4f}")
print(f"  {'chi2_33':<12}{chi2_fit:>16.4f}{ref['chi2_33']:>16.4f}")
print(f"  {'r_33':<12}{r_fit:>16.4f}{ref['r_33']:>16.4f}")
