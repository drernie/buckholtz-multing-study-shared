"""P85 -- can internal time be mapped to observed redshift?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE QUESTION FINDING_P84 LEFT SHARP.

P84 established that eps and f carry no unit convention at all, and that the
bridge for eps(k) costs exactly ONE external number -- physical a*H at a
reference epoch. It also named what that does NOT settle: which epoch of our
internal history corresponds to an observed z.

That question is answered here, and the first thing to notice is that it is NOT
a units problem. Redshift is a RATIO of scale factors,

    1 + z = a_ref / a

so it is automatically invariant under P84's S1 (a -> b*a). No scaling freedom
stands in the way. What stands in the way, if anything does, is whether our
background is a cosmology in which any epoch deserves the name "today".

WHAT OUR BACKGROUND ACTUALLY CONTAINS. Matter with rho_A = C/a^3, and a scalar
which FINDING_P82 measured to redshift like RADIATION (w -> 1/3) and which falls
to Omega_phi ~ 7e-07 by the end of the span. There is no cosmological constant,
no dark-energy component, and nothing that turns the expansion over. So the
expectation -- stated before measuring -- is that our H(a) is Einstein-de Sitter
to high accuracy at late times, and that a z-mapping is therefore legitimate
only where EdS itself is.

PRE-REGISTERED OUTCOMES:
  Z-DIRECT      the mapping costs one number AND our H(a) tracks a realistic
                expansion history over a useful range -> z may be quoted plainly.
  Z-CONDITIONAL the mapping costs one number, but H(a) is EdS-like, so z may be
                quoted ONLY with the explicit scope "matter-dominated universe,
                no dark energy" -- and comparisons to data are then limited to
                redshifts where EdS is an acceptable approximation.
  Z-BLOCKED     no consistent mapping exists even in principle.

WHAT THIS FILE WILL NOT DO: fit anything to Table A1 or to any dataset. The
deviation measured in Part D is an INTERNAL property of our own reconstruction,
computed against an analytic EdS reference, and NO_BRIDGE_FITTING is untouched.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "p76_ref", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_spec)
sys.modules["p76_ref"] = p76
_spec.loader.exec_module(p76)

G_N, C_MATTER = p76.G_N, p76.C_MATTER
A3_INIT, PHIDOT = p76.A3_INIT, p76.PHIDOT_INIT
T0, T_END = 1.0, 1e8


def background(g_hat, lam, lam_cc=0.0, phidot0=None, a0=None, n=4000, C=None):
    """Coupled background, with an OPTIONAL cosmological constant lam_cc.

    # WHY lam_cc exists at all: it is never used for physics here. It is the
    # NEGATIVE CONTROL for Part C -- a detector that reports "this is EdS" must
    # be shown to report something else when handed a background that is not.
    """
    a_init = A3_INIT ** (1.0 / 3.0) if a0 is None else a0
    pd_init = PHIDOT if phidot0 is None else phidot0
    C_use = C_MATTER if C is None else C

    def rhs(_t, y):
        a_, pb, pd = y
        rho_A = C_use / a_**3
        rho_phys = rho_A * (1.0 - g_hat * pb)
        arg = (8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + lam * pb**4 / 4.0 + lam_cc)
        H = np.sqrt(arg) if arg > 0 else 0.0
        return [a_ * H, pd, g_hat * rho_A - 3.0 * H * pd - lam * pb**3]

    with np.errstate(all="ignore"):
        s = solve_ivp(
            rhs,
            (T0, T_END),
            [a_init, 0.0, pd_init],
            rtol=1e-11,
            atol=1e-22,
            dense_output=True,
        )
        if not s.success:
            return None
        tt = np.exp(np.linspace(np.log(T0), np.log(T_END), n))
        a_, pb, pd = s.sol(tt)
    if not np.all(np.isfinite(a_)):
        return None
    rho_A = C_use / a_**3
    rho_phys = rho_A * (1.0 - g_hat * pb)
    rho_phi = pd**2 / 2.0 + lam * pb**4 / 4.0
    H = np.sqrt(np.maximum((8 * np.pi * G_N / 3) * (rho_phys + rho_phi + lam_cc), 0.0))
    # EdS reference: the SAME matter content, nothing else. Analytic, external.
    H_eds = np.sqrt((8 * np.pi * G_N / 3) * rho_A)
    return {
        "t": tt,
        "a": a_,
        "pb": pb,
        "pd": pd,
        "H": H,
        "H_eds": H_eds,
        "rho_A": rho_A,
        "rho_phys": rho_phys,
        "rho_phi": rho_phi,
        "omega_phi": rho_phi / (rho_phys + rho_phi + lam_cc),
    }


def w_eff(r):
    """Total effective equation of state from the expansion alone.

    w_eff = -1 - (2/3) d ln H / d ln a. Matter gives 0, radiation 1/3, Lambda -1.
    Computed from H(a) only, so it needs no knowledge of what is IN the model --
    which is what makes it usable as a detector rather than a restatement.
    """
    lnH, lna = np.log(r["H"]), np.log(r["a"])
    return -1.0 - (2.0 / 3.0) * np.gradient(lnH, lna)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P85 -- can internal time be mapped to observed redshift?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS")
    print("-" * 78)

    print("\n  C1 -- with g_hat=0 and lam=0 and the scalar's energy negligible,")
    print("  H must approach the EdS law H = sqrt(8*pi*G*rho_A/3) EXACTLY. That")
    print("  target is analytic and external to this project.")
    r0 = background(0.0, 0.0)
    if r0 is None:
        print("    *** C1 UNRESOLVED -- the reference run could not be carried.")
        return 1
    late = r0["a"] > r0["a"][0] * 100
    ratio = r0["H"][late] / r0["H_eds"][late]
    print(f"\n    {'a':<16}{'H / H_EdS':<18}{'Omega_phi'}")
    for i in np.linspace(0, late.sum() - 1, 5).astype(int):
        j = np.where(late)[0][i]
        print(
            f"    {r0['a'][j]:<16.6g}{r0['H'][j] / r0['H_eds'][j]:<18.12f}{r0['omega_phi'][j]:.3e}"
        )
    C1 = abs(ratio[-1] - 1.0) < 1e-6
    print(f"\n    final H/H_EdS - 1 = {ratio[-1] - 1:.3e}   =>  C1 {'PASSES' if C1 else 'FAILS'}")
    if not C1:
        print("    *** the uncoupled background is not EdS. Nothing below can be read.")
        return 1

    print("\n  C2 -- the w_eff detector must be able to say NOT-EdS. Handed a")
    print("  background with a cosmological constant it must report w_eff moving")
    print("  toward -1. A detector that reports 'matter' for everything is not a")
    print("  detector -- the lesson of P76's hardcoded gate.")
    rho_late = C_MATTER / (r0["a"][-1] ** 3)
    r_cc = background(0.0, 0.0, lam_cc=rho_late * 30.0)
    if r_cc is None:
        print("    *** C2 UNRESOLVED.")
        return 1
    w_cc, w_plain = w_eff(r_cc), w_eff(r0)
    print(f"\n    {'a':<16}{'w_eff (no CC)':<20}{'w_eff (with CC)'}")
    for i in np.linspace(len(r0["a"]) // 2, len(r0["a"]) - 2, 4).astype(int):
        print(f"    {r0['a'][i]:<16.6g}{w_plain[i]:<20.9f}{w_cc[i]:.9f}")
    C2 = w_cc[-2] < w_plain[-2] - 0.05
    print(f"\n    C2 {'PASSES' if C2 else 'FAILS'} -- the detector distinguishes them.")
    if not C2:
        print("    *** w_eff cannot tell a Lambda universe from a matter one.")
        return 1

    print("\n  C3 -- 1+z = a_ref/a must be invariant under P84's S1 (a -> b*a),")
    print("  since it is a RATIO. If it is not, the mapping has a units problem")
    print("  after all and P84's conclusion needs revisiting.")
    # # THE FIRST VERSION OF C3 WAS NOT A TEST OF S1 AT ALL. It scaled a0 by 7
    # # and left C alone -- but S1 is a -> b*a TOGETHER WITH C -> b^3*C. With C
    # # fixed, rho_A = C/a^3 drops by 343x at the start: a different universe, not
    # # a relabelled one, and the 5.3e-03 discrepancy it reported was honest. Same
    # # class of error as P84's S2 symbolic test and P83's bracket endpoint: a
    # # transformation called a symmetry while not being one.
    _B = 7.0
    rb = background(0.0, 0.0, a0=(A3_INIT ** (1.0 / 3.0)) * _B, C=C_MATTER * _B**3)
    z_plain = r0["a"][-1] / r0["a"][len(r0["a"]) // 2] - 1
    z_scaled = rb["a"][-1] / rb["a"][len(rb["a"]) // 2] - 1
    print(f"\n    1+z between mid-span and end, a0 as usual : {1 + z_plain:.12f}")
    print(f"    1+z between the same two, FULL S1 with b=7 : {1 + z_scaled:.12f}")
    C3 = abs(z_scaled / z_plain - 1) < 1e-6
    print(
        f"    relative difference {abs(z_scaled / z_plain - 1):.3e}  =>  "
        f"C3 {'PASSES' if C3 else 'FAILS'}"
    )

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- what the mapping costs, and what it does not buy")
    print("-" * 78)
    print("  1 + z = a_ref/a. Choosing WHICH epoch is a_ref is one number, and")
    print("  P84 already showed a*H at a reference epoch is one number too --")
    print("  they are the SAME choice, not two. So the z-mapping adds NO further")
    print("  external input beyond what P84 counted.")
    print()
    print("  That is the cheap half. The expensive half is whether the epoch so")
    print("  chosen deserves the name 'today', which is a question about the")
    print("  CONTENT of the background, not about units. Part C measures it.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- is our background a cosmology anyone could call realistic?")
    print("-" * 78)
    r1 = background(1.0, 1.0)
    if r1 is None:
        print("    *** UNRESOLVED.")
        return 1
    w1 = w_eff(r1)
    print("\n  w_eff = -1 - (2/3) dlnH/dlna, from the expansion alone.")
    print("  matter 0 | radiation 1/3 | Lambda -1")
    print(f"\n    {'a':<16}{'w_eff (g=1,lam=1)':<22}{'Omega_phi':<16}{'H/H_EdS'}")
    idx = np.linspace(len(r1["a"]) // 8, len(r1["a"]) - 2, 7).astype(int)
    for i in idx:
        print(
            f"    {r1['a'][i]:<16.6g}{w1[i]:<22.9f}{r1['omega_phi'][i]:<16.3e}"
            f"{r1['H'][i] / r1['H_eds'][i]:.9f}"
        )
    w_final = w1[-2]
    print(f"\n    w_eff at the end of the span : {w_final:+.6f}")
    print(f"    Omega_phi there              : {r1['omega_phi'][-2]:.3e}")
    print("    dark-energy component        : NONE -- there is no such term in")
    print("                                   the action this campaign built.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- the coupling's own imprint on H(a), measured internally")
    print("-" * 78)
    print("  H/H_EdS with the coupling on is the closest internal analogue of the")
    print("  H_MULT/H_FLRW ratio this campaign has circled since the start. It is")
    print("  computed against an ANALYTIC EdS reference with the same matter")
    print("  content -- no dataset, no Table A1, nothing fitted.")
    print(f"\n    {'a':<14}{'g=0,lam=1':<18}{'g=1,lam=1':<18}{'difference'}")
    r_off = background(0.0, 1.0)
    for i in idx:
        d_on = r1["H"][i] / r1["H_eds"][i]
        d_off = r_off["H"][i] / r_off["H_eds"][i]
        print(f"    {r1['a'][i]:<14.6g}{d_off:<18.9f}{d_on:<18.9f}{d_on - d_off:+.3e}")
    print("\n  The coupled and uncoupled ratios both tend to 1 from above as the")
    print("  scalar dilutes; the DIFFERENCE between them is the coupling's imprint")
    print("  on the expansion, and it is what a z-comparison would have to detect.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    eds_like = abs(w_final) < 0.02
    if not (C1 and C2 and C3):
        print("  -> controls failed; no verdict may be read.")
        return 1
    if eds_like:
        print(f"  -> Z-CONDITIONAL. w_eff = {w_final:+.6f}, i.e. MATTER to within")
        print("     2%, with Omega_phi already at the 1e-06 level and NO")
        print("     dark-energy term anywhere in the action. Our background is")
        print("     Einstein-de Sitter at late times.")
        print()
        print("     THE MAPPING ITSELF IS FREE. 1+z = a_ref/a is a ratio, so it is")
        print("     S1-invariant (C3), and choosing a_ref is the SAME single")
        print("     external number P84 already counted -- the z-mapping adds")
        print("     nothing to the bridge's cost.")
        print()
        print("     WHAT IS NOT FREE is the meaning of the epoch chosen. An EdS")
        print("     universe has no accelerating phase, so no epoch in our")
        print("     trajectory is 'today' in the sense a real observation means.")
        print("     z may therefore be quoted ONLY with the scope attached:")
        print("     matter-dominated, no dark energy -- which restricts any")
        print("     comparison to redshifts where EdS is itself acceptable.")
        print()
        print("     THIS IS NOT A UNITS PROBLEM AND Q005 IS NOT THE BLOCKER.")
        print("     Earlier in this campaign I flagged Q005 as the likely")
        print("     obstacle to the time mapping. It is not: the obstacle is that")
        print("     the completion as built contains no dark energy. That is a")
        print("     statement about the MODEL, not about missing information from")
        print("     the author, and no answer from anyone would change it.")
    else:
        print(f"  -> Z-DIRECT candidate: w_eff = {w_final:+.6f} is NOT matter-like,")
        print("     so the background carries something beyond matter plus a")
        print("     diluting scalar. That would need identifying before z is")
        print("     quoted, and it is not what the action was built to contain.")

    print("\n  NOT ESTABLISHED:")
    print("   * that EdS is or is not adequate at any particular redshift. That")
    print("     is a judgement about observational tolerance, not measured here.")
    print("   * anything about MULTING itself (Gate 1): the completion is OURS,")
    print("     and its lacking dark energy says nothing about the source model.")
    print("   * any comparison to data. NO_BRIDGE_FITTING untouched -- the EdS")
    print("     reference in Part D is analytic, not fitted.")
    print("   * Perelman condition 5 -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
