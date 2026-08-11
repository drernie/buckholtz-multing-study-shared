"""P14: does kappa's mere PRESENCE (each dipole's own near-field self-energy,
independent of the aggregate/cross-term cancellation P9 already proved) add a
cosmologically significant contribution to phi's own energy density?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. Continues the specific open item FINDING_P13a section 4 item 3
named: "kappa's mere presence contributes to phi's own background energy
density... regardless of whether the force it mediates angle-averages to
zero for a test particle." That force-vs-energy-density distinction is
exactly right: the total field energy from N independent dipole sources
splits as

    integral(grad(phi_total)^2) = sum_i integral(grad(phi_i)^2)         [self-energy, per-source, ORIENTATION-INDEPENDENT]
                                 + sum_{i!=j} integral(grad(phi_i).grad(phi_j))  [cross terms -- THIS is what P9's double-layer/isotropic averaging kills]

The diagonal (self-energy) piece does NOT depend on how the dipoles are
oriented relative to each other -- it is present for ANY nonzero kappa,
with no assumed asymmetry (P9's eps) or fixed mediator mass (P11's mu)
needed. This script computes it directly, using a positive control
(point-charge/monopole self-energy, a well-known closed form) before
trusting the new dipole result, then a Gate-4 (Conserved-Budget,
artifact-provenance-gates.md) upper bound on cluster number density to
avoid citing an unverified cluster mass function.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Part 1: symbolic self-energy integrals (SymPy), with a positive control
# ---------------------------------------------------------------------------

r, theta, phi_ang, r_min = sp.symbols("r theta phi r_min", positive=True)
q, p = sp.symbols("q p", positive=True)


def monopole_self_energy():
    """Positive control: E = integral (grad phi)^2 d^3x for phi=q/r, hard
    cutoff at r_min. Known closed form: E ~ q^2/r_min (up to O(1) prefactor
    depending on field-energy normalization convention)."""
    phi_mono = q / r
    dphi_dr = sp.diff(phi_mono, r)
    integrand = dphi_dr**2 * r**2 * sp.sin(theta)
    return sp.simplify(
        sp.integrate(integrand, (theta, 0, sp.pi), (phi_ang, 0, 2 * sp.pi), (r, r_min, sp.oo))
    )


def dipole_self_energy():
    """E = integral (grad phi)^2 d^3x for phi = p*cos(theta)/r^2 (the
    standard dipole potential, matching this project's own U_km normalization
    convention throughout P1/P9/P11/P12), hard cutoff at r_min."""
    phi_dip = p * sp.cos(theta) / r**2
    dphi_dr = sp.diff(phi_dip, r)
    dphi_dtheta_over_r = sp.diff(phi_dip, theta) / r
    grad2 = dphi_dr**2 + dphi_dtheta_over_r**2
    integrand = sp.simplify(grad2 * r**2 * sp.sin(theta))
    theta_integrated = sp.integrate(integrand, (theta, 0, sp.pi))
    return sp.simplify(sp.integrate(theta_integrated, (phi_ang, 0, 2 * sp.pi), (r, r_min, sp.oo)))


# ---------------------------------------------------------------------------
# Part 2: numeric evaluation -- real constants, verified not memorized
# ---------------------------------------------------------------------------

G_SI = 6.6743e-11  # m^3 kg^-1 s^-2, CODATA
C_SI = 2.998e8  # m/s
MPC_TO_M = 3.0857e22  # m per Mpc
MSUN_TO_KG = 1.989e30  # kg per solar mass
H0_KM_S_MPC = 67.4  # km/s/Mpc, Planck-consistent value already used elsewhere in this project
H0_SI = H0_KM_S_MPC * 1000 / MPC_TO_M  # s^-1

OMEGA_M = 0.315  # already used in this project's own cosmology scripts


def rho_crit_si():
    """rho_crit = 3 H0^2 / (8 pi G) -- computed, not quoted from memory."""
    return 3 * H0_SI**2 / (8 * sp.pi * G_SI)


def main() -> None:
    print("=" * 78)
    print("P14 -- DIPOLE SELF-ENERGY: does kappa's presence alone add to Omega_phi?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    print("\n[CONTROL] monopole self-energy, compare to known closed form q^2/r_min")
    e_mono = monopole_self_energy()
    print(f"  E_mono = {e_mono}")
    assert sp.simplify(e_mono - 4 * sp.pi * q**2 / r_min) == 0, "CONTROL FAILED"
    print("  -> matches 4*pi*q^2/r_min exactly (standard q^2/r_min scaling,")
    print("     up to the O(1) prefactor set by this integral's own normalization).")

    print("\n[NEW] dipole self-energy")
    e_dip = dipole_self_energy()
    print(f"  E_dip = {e_dip}")
    assert sp.simplify(e_dip - sp.Rational(8, 3) * sp.pi * p**2 / r_min**3) == 0, "unexpected form"
    print("  -> E_dip = (8*pi/3) * p^2 / r_min^3")

    print("\n[NUMERIC] cluster-scale evaluation")
    print("  Using FINDING_P6's own already-computed cluster number:")
    print("  (k/mc^2) = 1.7e-6  (dimensionless thermal-energy fraction, cluster pair)")
    k_over_mc2 = 1.7e-6

    r_cluster_mpc = 1.5  # R500-ish, Mpc -- typical massive-cluster scale used throughout this track
    m_cluster_msun = 1e15  # typical massive-cluster mass used throughout this track
    r_cluster_m = r_cluster_mpc * MPC_TO_M
    m_cluster_kg = m_cluster_msun * MSUN_TO_KG

    u_i = k_over_mc2 * r_cluster_m  # length, matches u_i = kappa*k_i*r_i/(c^2*m_i) with kappa~O(1)
    p_i = u_i * m_cluster_kg  # p_i = u_i * m_i (mass * length)
    r_min_val = (
        r_cluster_m  # cutoff = the cluster's own physical size (r_A = internal lever arm, per P1)
    )

    print(f"  u_i = (k/mc^2) * r_cluster = {u_i:.6e} m  ({u_i / MPC_TO_M:.3e} Mpc)")
    print(f"  p_i = u_i * m_cluster      = {p_i:.6e} kg*m")

    e_dip_val = float(
        (sp.Rational(8, 3) * sp.pi * p**2 / r_min**3).subs({p: p_i, r_min: r_min_val})
    )
    print(f"  E_self per cluster (raw integral units) = {e_dip_val:.6e}")

    print("\n[GATE 4 -- CONSERVED BUDGET] upper bound on cluster number density:")
    print("  assume ALL cosmic matter is packaged into clusters of this mass")
    print("  (maximally generous -- a real ceiling, per artifact-provenance-gates.md)")
    rho_crit = float(rho_crit_si())
    rho_m_total = OMEGA_M * rho_crit
    n_cluster_upper = rho_m_total / m_cluster_kg  # clusters per m^3, upper bound
    print(f"  rho_crit (computed, 3H0^2/8piG)     = {rho_crit:.6e} kg/m^3")
    print(f"  rho_m_total = Omega_m * rho_crit    = {rho_m_total:.6e} kg/m^3")
    print(f"  n_cluster (upper bound)             = {n_cluster_upper:.6e} m^-3")

    rho_phi_upper = n_cluster_upper * e_dip_val
    omega_phi_upper = rho_phi_upper / rho_crit
    print(
        f"\n  rho_phi,k-sector (upper bound)       = {rho_phi_upper:.6e} [same units as e_dip_val]"
    )
    print(f"  Omega_phi,k-sector (upper bound)     = {omega_phi_upper:.6e}")

    print("\n" + "=" * 78)
    print("VERDICT -- CORRECTED: the raw number is NOT physically meaningful")
    print("=" * 78)
    print("Self-energy channel                    : REAL, orientation-independent,")
    print("                                          separate from P9's cross-term zero")
    print(f"Omega_phi,k-sector, assuming kappa~O(1) : {omega_phi_upper:.3e}  <- NOT negligible,")
    print("                                          NOT reliable either -- see below")
    print()
    print("THE ACTUAL RESULT (found while checking the printed number against the")
    print("computed one -- caught before this was sent to skeptic or written up):")
    print()
    print("  kappa's ABSOLUTE scale has never been independently fixed anywhere in")
    print("  this project. beta_d=2 and beta_q=sqrt(6) are DIMENSIONLESS COEFFICIENTS")
    print("  multiplying (u_A+u_P), where u_i=kappa*k_i*r_i/(c^2*m_i) itself still")
    print("  scales linearly with kappa -- 'zero free parameters after kappa' (P1's")
    print("  own words) means exactly that: kappa remains free. Every prior bridge-")
    print("  track result that produced a real number did so via a RATIO (beta_q/")
    print("  beta_d, ell_q^2/ell_d^2) in which kappa cancels, or via a SEPARATE scale")
    print("  unrelated to kappa (P11/P12's mu~H0/c). This is the FIRST calculation in")
    print("  the P1-P14 sequence that depends on kappa's ABSOLUTE magnitude directly")
    print("  -- and it reveals that magnitude was never pinned down. The printed")
    print("  Omega_phi number above assumed kappa~O(1) in SI units with no basis;")
    print("  it can be made arbitrarily large or small by rescaling kappa, so it")
    print("  carries NO information as printed.")
    print()
    print("CAVEATS:")
    print("  1. [LOAD-BEARING, not minor] kappa's absolute normalization is unfixed --")
    print("     this blocks ANY absolute energy-density estimate for the k-sector,")
    print("     not just this one calculation.")
    print("  2. r_min = r_cluster is a MODELING CHOICE, not independently derived.")
    print("  3. Omega_phi (energy-density fraction) is not the same quantity as")
    print("     Archidiacono et al.'s beta (coupling-strength ratio) regardless of")
    print("     the kappa problem -- a second, independent mapping gap.")


if __name__ == "__main__":
    main()
