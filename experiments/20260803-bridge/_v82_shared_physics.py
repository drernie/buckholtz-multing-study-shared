"""Shared TJB v82 physics kernel for the P177-P185 degeneracy thread.

Extracted 2026-09-01 (boyko-project-radar housekeeping pass) after an
independent re-check found this exact block byte-for-byte identical
across P178-P185 (8 files), and identical to P177 except for a
docstring-only difference in addot_over_a_eps -- 9 files total, not
11: P175/P176 predate this convention and use a structurally different
physics scaffolding (addot_over_a without eps, no CC_POINTS), so they
are correctly left untouched.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np

MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
c = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
B_real = 2.24
C_real = -1.00
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z):
    return Mgas_piv_kg * (T_keV_of(z) / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z):
    return 1.5 * (Mgas_of(z) / (mu_mol * m_proton)) * (T_keV_of(z) * KEV_TO_J)


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def m_dot(z):
    return 1.1 * (H0_planck_si * Efun(z)) * M_of(z)


def v_infall(z):
    return np.sqrt(G * M_of(z) / R_of(z))


def F_accretion(z):
    return m_dot(z) * (f_coh * f_merge * v_infall(z))


def addot_over_a_eps(z, b1, b2, eps):
    """TJB's own addot_over_a, with F0 -> (1+eps)*F0 -- FINDING_P165's
    own monopole-tier perturbation, applied here to the REAL force law
    (not an idealized local expansion). eps=0 recovers TJB's own
    published force law exactly (verified as a positive control below).
    """
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    F0 = (1 + eps) * (-G) * M * M / d**2
    F1 = b1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M / 2.0)) / d
