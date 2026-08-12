"""P17: two INDEPENDENT upper bounds on kappa already exist in this project's
own prior work -- from two completely different physical systems. Are they
mutually consistent, and which one is binding?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12. kappa's absolute scale has never been fixed anywhere in this
project (FINDING_P14). Two prior findings each derived a CONDITIONAL upper
bound on kappa from a real, independent physical system, without either
recognizing the other:

  FINDING_P7 (binary pulsar J0737-3039, rotational-only k):  IF this
    project's own derived beta_d=2 (FINDING_two_charge_completion.md) is to
    survive the pulsar-timing bound on ell_d/r, kappa must be <~ 0.06.
    (P7's own caveat, added after the P14 skeptic review, already states
    this number -- re-derived here from P7's own base inputs, not quoted.)

  FINDING_P14 (cosmological self-energy, Gate-4 cluster-density ceiling):
    Omega_phi(kappa) ~ 3.28e11 * kappa^2 (self-energy channel alone,
    P15/P16 later confirmed cross-terms are ~1e-4..1e-9 of self-energy at
    realistic cluster separations, so neglecting them here is justified,
    not just assumed). Omega_phi<=1 requires kappa <~ 1.75e-6.

Both are recomputed here from each finding's own stated base inputs (not
copy-pasted results) so this script is independently checkable without
re-running P7.py or P14's script.

SCOPE: this does NOT fix kappa. Both bounds are one-sided upper bounds
(kappa could, for all either constraint says, be exactly zero). This only
checks whether the two independent bounds are mutually consistent, and by
how much one dominates the other.
"""

import math

# ---------------------------------------------------------------------------
# Bound 1: FINDING_P7 -- binary pulsar J0737-3039, rotational-only k,
# beta_d=2 (this project's own derived value) required to survive.
# ---------------------------------------------------------------------------

beta_d_derived = 2  # FINDING_two_charge_completion.md, zero free params after kappa
u_A_rotational_at_kappa1 = 0.23  # m, FINDING_P7 S3, from pulsar A's P=22.7ms rotation, at kappa=1
pulsar_ell_d_over_r_bound = 0.055  # FINDING_unsuppressed_observable_periastron.md's timing bound


def kappa_bound_from_pulsar():
    """beta_d_max_allowed(kappa) = pulsar_bound / (2*kappa*u_A_at_kappa1);
    solve for kappa such that beta_d_derived == beta_d_max_allowed(kappa)."""
    # beta_d_derived = pulsar_ell_d_over_r_bound / (2 * kappa * u_A_rotational_at_kappa1)
    return pulsar_ell_d_over_r_bound / (2 * beta_d_derived * u_A_rotational_at_kappa1)


# ---------------------------------------------------------------------------
# Bound 2: FINDING_P14 -- cosmological self-energy, Gate-4 cluster-density
# ceiling. Re-derived compactly from the same base physical inputs P14 used
# (not copied as a result) -- see P14_dipole_self_energy_omega_bound.py for
# the full sympy derivation of the (8*pi/3)*p^2/r_min^3 self-energy formula
# and the monopole positive control; reused here as an already-verified
# closed form, only the numeric evaluation is repeated.
# ---------------------------------------------------------------------------

G_SI = 6.6743e-11
C_SI = 2.998e8
MPC_TO_M = 3.0857e22
MSUN_TO_KG = 1.989e30
H0_KM_S_MPC = 67.4
H0_SI = H0_KM_S_MPC * 1000 / MPC_TO_M
OMEGA_M = 0.315

k_over_mc2 = 1.7e-6  # FINDING_P6
r_cluster_mpc = 1.5
m_cluster_msun = 1e15


def kappa_bound_from_cosmology():
    r_cluster_m = r_cluster_mpc * MPC_TO_M
    m_cluster_kg = m_cluster_msun * MSUN_TO_KG
    u_i_at_kappa1 = k_over_mc2 * r_cluster_m  # m, matches u_i=kappa*k_i*r_i/(c^2*m_i) at kappa=1
    p_i_at_kappa1 = u_i_at_kappa1 * m_cluster_kg
    r_min = r_cluster_m
    e_self_at_kappa1 = (8 * math.pi / 3) * p_i_at_kappa1**2 / r_min**3

    rho_crit = 3 * H0_SI**2 / (8 * math.pi * G_SI)
    rho_m_total = OMEGA_M * rho_crit
    n_cluster_upper = rho_m_total / m_cluster_kg

    rho_phi_at_kappa1 = n_cluster_upper * e_self_at_kappa1
    omega_phi_at_kappa1 = rho_phi_at_kappa1 / rho_crit
    # Omega_phi(kappa) = omega_phi_at_kappa1 * kappa^2 (self-energy ~ p_i^2 ~ kappa^2)
    return omega_phi_at_kappa1, math.sqrt(1.0 / omega_phi_at_kappa1)


def main() -> None:
    print("=" * 78)
    print("P17 -- ARE FINDING_P7's AND FINDING_P14's INDEPENDENT KAPPA BOUNDS")
    print("       MUTUALLY CONSISTENT? WHICH ONE IS BINDING?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    kappa_pulsar = kappa_bound_from_pulsar()
    print("\n[BOUND 1 -- FINDING_P7, binary pulsar J0737-3039]")
    print(f"  beta_d (this project's derived value)   = {beta_d_derived}")
    print(f"  u_A at kappa=1 (rotational, P=22.7ms)    = {u_A_rotational_at_kappa1} m")
    print(f"  pulsar-timing bound on ell_d/r            = {pulsar_ell_d_over_r_bound}")
    print(f"  -> kappa required for beta_d=2 to survive : kappa <~ {kappa_pulsar:.4f}")
    print("     (matches FINDING_P7's own caveat figure, ~0.06, re-derived not quoted)")

    omega_phi_1, kappa_cosmo = kappa_bound_from_cosmology()
    print("\n[BOUND 2 -- FINDING_P14, cosmological self-energy / Gate-4]")
    print(f"  Omega_phi at kappa=1 (self-energy channel) = {omega_phi_1:.4e}")
    print(f"  -> kappa required for Omega_phi<=1         : kappa <~ {kappa_cosmo:.4e}")
    print("     (matches FINDING_P14's own caveat figure, ~1e-6, re-derived not quoted)")

    ratio = kappa_pulsar / kappa_cosmo
    orders = math.log10(ratio)
    print("\n[COMPARISON]")
    print(
        f"  kappa_pulsar_bound / kappa_cosmo_bound = {ratio:.3e}  ({orders:.2f} orders of magnitude)"
    )
    print("  -> a kappa satisfying the COSMOLOGICAL bound automatically satisfies the")
    print("     PULSAR-survival bound too, with enormous margin -- NO TENSION between")
    print("     the two independent constraints.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Two independent physical systems (binary pulsar orbital dynamics; cosmological")
    print("self-energy budget) give upper bounds on kappa that DO NOT CONTRADICT each")
    print("other -- the cosmological bound is the binding (tighter) one, by")
    print(f"~{orders:.1f} orders of magnitude.")
    print()
    print("THIS DOES NOT FIX KAPPA. Both bounds are one-sided (kappa <~ X); neither")
    print("provides a lower bound or a specific value. Kappa could be anywhere from 0")
    print(f"up to ~{kappa_cosmo:.2e} and satisfy both constraints -- including exactly zero,")
    print("in which case the entire k-sector dipole coupling this whole bridge track has")
    print("been probing would simply vanish. The open problem from FINDING_P14 (kappa's")
    print("absolute scale is unfixed project-wide) remains open after this finding.")


if __name__ == "__main__":
    main()
