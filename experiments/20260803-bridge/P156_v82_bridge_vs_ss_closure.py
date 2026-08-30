"""P156 — v82's kinematic F->H(z) bridge vs. this project's own Shtanov-Sahni
background closure (P152/docs/127): tier structure comparison + G_eff check
applied to v82's own printed force law, plus the primary-source correction
of an initial (agent-drafted) claim about v82's s(z)-a(z) relation.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR

Origin: dispatched after Dr. Buckholtz gave access to his current, more
developed preprint (v82, Preprints.org 202608.0943v1). A first pass by
Agent(boyko-agent) proposed a verdict ("BRIDGES-FORMALLY-DISTINCT-NOT-
CONTRADICTORY") that a context-asymmetric skeptic review (auto-triggered,
same session) found overstated on two of its four supporting claims, and
that direct primary-source reading (this file's author, reading v82 pp.5-6
and p.14 directly) found to be WRONG on a third, load-bearing claim (the
"s(z)=d0/(1+z) exactly" premise). This script keeps only what survived
independent, tool-verified re-derivation.

Runtime: <1s (pure sympy limits, no N-body/Monte-Carlo).
"""

import sympy as sp

r, C = sp.symbols("r C", positive=True)


def g_eff_ratio(f_expr, rvar):
    """S-S background closure criterion: G_eff/G = lim_{r->oo} [f(r) - r f'(r)]
    for phi(r) = -(G/r) f(r). See docs/127 / P152 for the general derivation;
    this re-applies it to v82's own printed kernels, not our own.
    """
    fprime = sp.diff(f_expr, rvar)
    return sp.limit(f_expr - rvar * fprime, rvar, sp.oo)


def test_tier_g_eff_matches_v82_kernel_structure():
    """v82 Eqs (2)-(4) [VERIFIED-PDF pp.4-5]:
      F^(0) = -G m_A m_P / s^2                         (monopole,  n=0 in f=C r^-n)
      F^(1) = +G beta1 (k_A m_P r_A + k_P m_A r_P) / (2 c^2 s^3)   (dipole,    n=1)
      F^(2) = -G beta2 k_A k_P r_A r_P c^-4 / s^4        (quadrupole, n=2)
    These are the SAME radial-exponent tiers as docs/127's own f-class
    assignment for MULTING's monopole/dipole/quadrupole pair kernel
    (independently corroborated by NR-018's Ground-1 indexing, U ~ s^-1,s^-2,s^-3
    for the potentials these forces come from). Positive control: n=0 (monopole)
    must NOT vanish; n=1,2 (dipole/quadrupole) must vanish; negative control
    (f=C r^2, not of the docs/125 kernel family) must diverge, not spuriously
    read as zero.
    """
    results = {}
    for n in (0, 1, 2):
        f = C * r ** (-sp.Integer(n))
        results[n] = g_eff_ratio(f, r)

    assert results[0] == C, "monopole G_eff must be nonzero (positive control)"
    assert results[1] == 0, "dipole G_eff must vanish under this closure"
    assert results[2] == 0, "quadrupole G_eff must vanish under this closure"

    negative_control = g_eff_ratio(C * r**2, r)
    assert negative_control in (sp.oo, -sp.oo), (
        "negative control (f=C r^2) must diverge -- the criterion must "
        "discriminate, not annihilate every input"
    )
    return results, negative_control


# --- Table III [VERIFIED-PDF p.14], hard-coded from the printed table, NOT
# recomputed -- this project has not reproduced v82's own fit. Values are the
# force-term shares of the gross force budget |F0|+|F1|+|F2|+|F_acc|, spotlighted
# solution (H_0,anchor=73.22).
TABLE_IIIA_SPOTLIGHTED = {
    # z:     (F0_pct, F1_dipole_pct, F2_quad_pct, net_pct)
    1.965: (-0.06, +52.99, -46.53, +5.99),
    1.07: (-0.06, +53.04, -46.54, +6.09),
    0.5: (-0.05, +52.14, -47.48, +4.28),
    0.070: (-0.05, +49.76, -49.89, -0.49),
}


def test_monopole_negligible_at_every_tabulated_z():
    """Direct, non-extrapolated fact from Table IIIa: at all four z v82 tabulates,
    the monopole (the ONLY tier our S-S closure criterion has anything to say
    about) is a negligible share of the gross force budget, while the two
    k-dependent tiers (dipole+quadrupole -- the tiers our closure criterion
    zeroes) dominate it. This requires no extrapolation and no use of the
    (corrected-away, see FINDING) s(z)=d0/(1+z) premise.
    """
    for z, (f0, f1, f2, _net) in TABLE_IIIA_SPOTLIGHTED.items():
        assert abs(f0) < 0.1, f"monopole share should be ~0.05-0.06%% at z={z}"
        k_dependent_share = abs(f1) + abs(f2)
        assert k_dependent_share > 95.0, (
            f"k-dependent (dipole+quadrupole) share should dominate at z={z}"
        )


if __name__ == "__main__":
    tiers, neg = test_tier_g_eff_matches_v82_kernel_structure()
    print("G_eff/G limits by tier (n=0,1,2):", tiers)
    print("negative control (f=C r^2):", neg)
    test_monopole_negligible_at_every_tabulated_z()
    print("Table IIIa monopole-negligible check: PASS at all 4 tabulated z")
