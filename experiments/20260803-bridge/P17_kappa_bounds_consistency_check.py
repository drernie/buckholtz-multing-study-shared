"""P17: two pre-existing upper bounds on kappa exist in this project's own
prior work. Do they contradict each other, and does either check out?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
2026-08-12, corrected 2026-08-12 after context-blind skeptic review.
kappa's absolute scale has never been fixed anywhere in this project
(FINDING_P14). Two prior findings each derived a CONDITIONAL upper bound
on kappa from a real, independent physical system, without either
recognizing the other:

  FINDING_P7 (binary pulsar J0737-3039, rotational-only k):  IF this
    project's own derived beta_d=2 (FINDING_two_charge_completion.md) is to
    survive the pulsar-timing bound on ell_d/r, kappa must be <~ 0.06.
    (P7's own caveat, added after the P14 skeptic review, already states
    this number -- re-derived here from P7's own base inputs, not quoted.)

  FINDING_P14 (cosmological self-energy, Gate-4 cluster-density ceiling):
    Omega_phi(kappa) ~ 3.28e11 * kappa^2 (self-energy channel alone;
    FINDING_P15/FINDING_P16 confirmed cross-terms are ~4e-5..1.4e-4 of
    self-energy at realistic cluster separations -- CORRECTED after
    skeptic review, an earlier draft of this docstring cited P15's own
    already-retracted ~1e-9 figure). Omega_phi<=1 requires kappa <~ 1.75e-6.

Both are recomputed here from each finding's own stated base inputs (not
copy-pasted results) so this script is independently checkable without
re-running P7.py or P14's script.

SCOPE: this does NOT fix kappa. Both bounds are one-sided upper bounds
(kappa could, for all either constraint says, be exactly zero).

[CORRECTED after skeptic review -- read before trusting kappa_cosmo_bound.]
Omega_phi as computed by FINDING_P14's own formula (reused unchanged here)
has units kg/m, not dimensionless: p_i has units kg*m, so
(8*pi/3)*p_i**2/r_min**3 has units kg**2/m, and Omega_phi = rho_phi/rho_crit
inherits kg/m overall. A missing normalization constant (units m/kg) is
silently assumed to be 1 -- its true value is unknown. kappa_cosmo_bound's
NUMERIC value is therefore unverified, not just imprecise; the kappa**2
SCALING relationship remains valid regardless. Full detail:
FINDING_P14 section 6 and FINDING_P17's own corrected write-up.

Also corrected: "consistent, no tension" for two one-sided upper bounds is
close to a tautology (kappa<=A and kappa<=B never contradict; the only
question is which of A, B is smaller), and the two bounds' underlying
assumption sets never overlap -- see FINDING_P17 for the full discussion.
This script prints the raw comparison; do not read "no tension" as a
substantive cross-check without reading the finding's own corrected caveats.
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
    print("  [CORRECTED after skeptic review:] Omega_phi as computed has units kg/m, not")
    print("  dimensionless (p_i is kg*m, so p_i^2/r_min^3 is kg^2/m) -- a missing")
    print("  normalization constant is silently assumed =1. kappa_cosmo_bound's NUMERIC")
    print("  value is therefore unverified, not just imprecise. See FINDING_P14 section 6.")

    ratio = kappa_pulsar / kappa_cosmo
    orders = math.log10(ratio)
    print("\n[COMPARISON]")
    print(
        f"  kappa_pulsar_bound / kappa_cosmo_bound = {ratio:.3e}  ({orders:.2f} orders of magnitude)"
    )
    print("  [CORRECTED after skeptic review:] for two ONE-SIDED upper bounds, 'no")
    print("  tension' is logically equivalent to 'the tighter bound is tighter' -- not")
    print("  independent information. The two bounds also rest on non-overlapping")
    print("  assumption sets (P7: beta_d=2 + rotational-k reading; P14: Gate-4 + r_min")
    print("  choice + unresolved P14-section-1 tension + the units issue above), and the")
    print("  vast scale disparity between a single pulsar and a cosmological population")
    print("  made contradiction essentially impossible from the outset. See FINDING_P17.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("Two one-sided upper bounds on kappa, from different physical systems, do not")
    print(f"contradict -- the cosmological figure is numerically smaller, by ~{orders:.1f}")
    print("orders of magnitude. [CORRECTED:] this comparison is close to tautological for")
    print("one-sided bounds and does not constitute a substantive independent cross-check")
    print("-- see FINDING_P17's corrected 'Are the two bounds consistent?' section.")
    print()
    print("THIS DOES NOT FIX KAPPA. Both bounds are one-sided (kappa <~ X); neither")
    print("provides a lower bound or a specific value. Kappa could be anywhere from 0")
    print(f"up to ~{kappa_cosmo:.2e} and satisfy both constraints -- including exactly zero,")
    print("in which case the entire k-sector dipole coupling this whole bridge track has")
    print("been probing would simply vanish. The open problem from FINDING_P14 (kappa's")
    print("absolute scale is unfixed project-wide) remains open after this finding, and is")
    print("now joined by a second, separate open problem: the missing normalization")
    print("constant needed to make Omega_phi dimensionally meaningful at all.")


if __name__ == "__main__":
    main()
