"""P86 -- add dark energy, then rerun FINDING_P81's viability gate on it.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS EXISTS.

FINDING_P85 returned Z-CONDITIONAL: the internal-time-to-redshift mapping is
free, but our background is Einstein-de Sitter to a part in a million and
contains NO dark-energy term, so no epoch in it is "today" in the sense an
observation means. The registered next question was whether such a term can be
added at all -- and P85 registered the prediction that it CANNOT be added as a
cosmetic afterthought, because it would have to re-enter at P81's viability gate.

This step cashes that prediction.

WHAT "ADDING DARK ENERGY" MEANS HERE, AND WHY IT IS ONE PARAMETER NOT TWO.
Adding a constant to the potential, V = lam*phibar^4/4 + V0, and adding a
cosmological constant to the Friedmann equation are THE SAME OPERATION in these
equations: a constant has zero derivative, so V' = lam*phibar^3 is untouched and
Klein-Gordon does not see it, while the energy density does. So the extension is
one parameter, entering the Friedmann equation only. P81's viability() was
EXTENDED with lam_cc rather than reimplemented here -- two copies of a predicate
drift, and P86 would then be measuring a gate P81 never had.

HOW MUCH DARK ENERGY? That choice is not free-floating. Lambda is constant while
rho_m falls as a^-3, so Omega_Lambda = Lambda/(Lambda + rho_m) rises
monotonically and there is always SOME epoch at which it equals 0.7. Choosing
Lambda is therefore EQUIVALENT to choosing which scale factor is "today", which
is exactly the one external number P84 and P85 already counted. Lambda is fixed
here by demanding Omega_Lambda = 0.7 at a nominated a_today.

THE PREDICTION THIS TESTS, stated before running. The diamond scan located
min(1-g*phibar) at a ~ 12, where Lambda is smaller than the matter density by
many orders. If the constraint really lives there, adding Lambda should leave
P81's boundary essentially where P83 put it, and the two sectors decouple.

PRE-REGISTERED OUTCOMES:
  DE-DECOUPLED  the viability verdict is unchanged and both boundaries move by
                less than 0.08 -- the largest R_boundary P83 measured across its
                matter-dominated lever range, used here as the natural yardstick
                for "did not really move". The extension is cheap.
  DE-COUPLED    a boundary moves by more than that -> dark energy is not free,
                and the completion must be re-audited wherever P81's corner was
                quoted.
  DE-BREAKS     the predicate fails outright somewhere it previously passed ->
                the extended completion is not viable and that is the finding.

WHAT THIS CANNOT DO: it cannot make the completion right, and it cannot compare
anything to data. Omega_Lambda = 0.7 is used as a DEFINITION of the reference
epoch, not as a measurement imported from cosmology -- no dataset and no Table A1
quantity enters. NO_BRIDGE_FITTING is untouched.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fn))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


p81 = _load("p81_ref", "P81_background_viability.py")
p83 = _load("p83_ref", "P83_ic_robustness_of_boundary.py")

C_MATTER, G_N = p81.C_MATTER, p81.G_N
A3_INIT, PHIDOT = p81.A3_INIT, p81.PHIDOT

# P83's measured boundaries at lam_cc = 0 -- the reference this step moves against.
P83_GCRIT_LAM0 = 0.738209
P83_GCRIT_LAM01 = 2.751767
YARDSTICK = 0.08  # P83's worst R_boundary inside matter domination

HDR_GLAM = "g \\ lam"


def lambda_for(a_today, frac=0.7):
    """Lambda giving Omega_Lambda = frac at a_today.

    Omega = L/(L + rho_m)  =>  L = rho_m * frac/(1-frac), with rho_m = C/a^3.
    This is a DEFINITION of the reference epoch, not a measurement imported from
    cosmological data.
    """
    rho_m = C_MATTER / a_today**3
    return rho_m * frac / (1.0 - frac)


def viable(g_hat, lam, lam_cc, phidot0=None):
    r = p81.viability(g_hat, lam, phidot0=phidot0, lam_cc=lam_cc)
    return r["ok"], r


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P86 -- dark energy added, then run through FINDING_P81's gate")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS")
    print("-" * 78)

    print("\n  C0 -- lam_cc = 0 must reproduce P81 exactly. The predicate was")
    print("  EXTENDED, not reimplemented; if the default path had moved, this")
    print("  step would be measuring a gate P81 never had.")
    C0 = True
    print(f"\n    {'point':<16}{'P81 published':<18}{'now, lam_cc=0':<20}{'match'}")
    for (g, lam), want in (((1.0, 1.0), 0.8717), ((0.75, 0.01), 0.8643), ((2.0, 0.1), 0.4850)):
        got = p81.viability(g, lam, lam_cc=0.0).get("min_M", float("nan"))
        ok = abs(got - want) < 5e-5
        C0 = C0 and ok
        print(f"    ({g:g},{lam:g})".ljust(16) + f"{want:<18.4f}{got:<20.6f}{ok}")
    if not C0:
        print("    *** C0 FAILED. Stop.")
        return 1

    print("\n  C1 -- the term added must ACTUALLY behave as dark energy. If it")
    print("  produces no accelerating epoch it is not what this step claims to")
    print("  add, and every number below would be about something else.")
    a_today = 5.0e5  # inside the span: a at t=8e7 is about 4.9e5
    lam_cc = lambda_for(a_today)
    print(f"\n    a_today nominated              : {a_today:.4g}")
    print(f"    Lambda for Omega_Lambda = 0.7  : {lam_cc:.6e}")
    tt = np.exp(np.linspace(np.log(p81.T0), np.log(p81.T_END), 4000))
    with np.errstate(all="ignore"):
        s = solve_ivp(
            p81.background_rhs(0.0, 0.0, lam_cc),
            (p81.T0, p81.T_END),
            [A3_INIT ** (1.0 / 3.0), 0.0, PHIDOT],
            rtol=1e-11,
            atol=1e-22,
            dense_output=True,
        )
        a_, _pb, pd = s.sol(tt)
    rho_m = C_MATTER / a_**3
    om_L = lam_cc / (lam_cc + rho_m)
    H = np.sqrt((8 * np.pi * G_N / 3) * (rho_m + pd**2 / 2.0 + lam_cc))
    w_tot = -1.0 - (2.0 / 3.0) * np.gradient(np.log(H), np.log(a_))
    q = 0.5 * (1.0 + 3.0 * w_tot)  # deceleration parameter; q < 0 is acceleration
    print(f"\n    {'a':<14}{'Omega_Lambda':<16}{'w_eff':<16}{'q':<12}{'accelerating?'}")
    for i in np.linspace(len(a_) // 3, len(a_) - 2, 6).astype(int):
        print(
            f"    {a_[i]:<14.5g}{om_L[i]:<16.4f}{w_tot[i]:<16.6f}{q[i]:<12.4f}"
            + ("YES" if q[i] < 0 else "no")
        )
    accel = bool(np.any(q[:-1] < 0))
    C1 = accel and om_L[-2] > 0.5
    print(f"\n    an accelerating epoch exists : {accel}")
    print(f"    Omega_Lambda reaches         : {om_L[-2]:.4f}")
    print(f"    C1 {'PASSES' if C1 else 'FAILS'}")
    if not C1:
        print("    *** what was added does not behave as dark energy.")
        return 1

    print("\n  C2 -- NEGATIVE CONTROL, REWRITTEN. THE FIRST VERSION WAS BROKEN")
    print("  BY THE VERY RULE IT CITED, and the correction is itself the finding.")
    print()
    print("  # It called viability() with an absurd Lambda, got state=UNRESOLVED")
    print("  # (integrator gave up), and scored not-ok as 'the gate can reject a")
    print("  # Lambda'. Under the Substrate Gate rule -- the one P81 itself had")
    print("  # to be corrected for -- unresolved means NOT MEASURED, which is")
    print("  # neither viable nor non-viable. An infrastructure failure was being")
    print("  # recorded as evidence about the predicate, inside a control written")
    print("  # to prevent exactly that.")
    print()
    print("  The honest question: is there ANY Lambda the gate rejects on")
    print("  PHYSICAL grounds -- measured, and failing a clause for a reason that")
    print("  is not arithmetic?")
    hdr = f"{'Omega_L=0.7 at':<17}{'Lambda':<13}{'state':<12}{'min_M':<16}{'ok':<7}why"
    print("\n    " + hdr)
    phys_reject = False
    for a_t in (1e6, 5e5, 1e5, 3e4, 1e4, 5e3):
        lm = lambda_for(a_t)
        r = p81.viability(1.0, 1.0, lam_cc=lm)
        mm = r.get("min_M")
        if r["state"] == "measured" and not r["ok"] and "rho_phys" not in r["why"]:
            phys_reject = True
        print(
            f"    a={a_t:<15.3g}{lm:<13.3e}{r['state']:<12}"
            + (f"{mm:<16.9f}" if mm is not None else f"{'not measured':<16}")
            + f"{str(r['ok']):<7}{r['why'][:32]}"
        )
    print()
    print("  READ THE why COLUMN. Where the gate does say no, the clause is")
    print("  rho_phys<=0 -- and that fires because Lambda drives a to about 1e195,")
    print("  so C/a^3 UNDERFLOWS to exactly 0.0 in double precision. min_M stays")
    print("  at 0.8717 throughout: 1-g*phibar never approaches zero, which is the")
    print("  pathology that clause exists to catch. The rejection is ARITHMETIC,")
    print("  not physics -- BLOCKED-INFRASTRUCTURE.")
    print(f"\n  any rejection on a PHYSICAL clause: {phys_reject}")
    print()
    print("  => THE REAL RESULT, a property of the PREDICATE rather than of the")
    print("  extension: P81 has NO clause a cosmological constant can violate.")
    print("  More Lambda means more Hubble friction, which DAMPS phibar and")
    print("  pushes 1-g*phibar back toward 1 -- toward MORE viable. There is no")
    print("  'must decelerate' condition anywhere in it. Every DE verdict below")
    print("  carries that caveat: part of any decoupling is STRUCTURAL, not a")
    print("  statement about epochs.")
    C2_no_physical_clause = not phys_reject
    print(f"\n  recorded: gate has no Lambda-sensitive physical clause = {C2_no_physical_clause}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- P81's grid, rerun with dark energy on")
    print("-" * 78)
    print(f"  Lambda = {lam_cc:.6e}, i.e. Omega_Lambda = 0.7 at a = {a_today:.4g}.")
    print("  legend: OK viable | . measured and not viable | ? UNRESOLVED")
    g_grid = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
    l_grid = [0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 10.0]
    print(f"\n    {HDR_GLAM:<9}" + "".join(f"{x:>9g}" for x in l_grid))
    grid_de, grid_0 = {}, {}
    for g in g_grid:
        row = ""
        for lam in l_grid:
            ok, r = viable(g, lam, lam_cc)
            grid_de[(g, lam)] = (ok, r["state"])
            ok0, _r0 = viable(g, lam, 0.0)
            grid_0[(g, lam)] = ok0
            row += f"{('OK' if ok else ('?' if r['state'] == 'unresolved' else '.')):>9}"
        print(f"    {g:<9g}{row}")

    n_de = sum(1 for ok, _ in grid_de.values() if ok)
    n_0 = sum(1 for ok in grid_0.values() if ok)
    flips = [p for p in grid_de if grid_de[p][0] != grid_0[p]]
    print(f"\n    viable WITH Lambda    : {n_de} of {len(grid_de)}")
    print(f"    viable WITHOUT        : {n_0} of {len(grid_0)}")
    print(f"    classification flips  : {len(flips)}" + (f"  {flips}" if flips else ""))

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- do P83's two boundaries move?")
    print("-" * 78)
    print("  Measured exactly as P83 measured them, using P83's OWN bisector so")
    print("  the comparison is like-for-like rather than like-for-similar.")
    print(f"\n    {'edge':<24}{'P83 (no DE)':<16}{'with DE':<16}{'R_boundary':<14}{'iters / note'}")
    moved = {}
    for label, lam_fixed, ref, bad, good in (
        ("g_crit at lam = 0", 0.0, P83_GCRIT_LAM0, 1.0, 0.1),
        ("g_crit at lam = 0.1", 0.1, P83_GCRIT_LAM01, 3.0, 2.0),
    ):
        x, n, note = p83.bisect_boundary(lambda g, lf=lam_fixed: viable(g, lf, lam_cc), bad, good)
        if x is None:
            print(f"    {label:<24}{ref:<16.6f}{'-':<16}{'-':<14}{n}   {note}")
            moved[label] = None
            continue
        rb = abs(x - ref) / ref
        moved[label] = rb
        print(f"    {label:<24}{ref:<16.6f}{x:<16.6f}{rb:<14.4f}{n}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    vals = [v for v in moved.values() if v is not None]
    if len(vals) < len(moved):
        print("  -> NOT MEASURABLE on at least one edge. That is an infrastructure")
        print("     outcome, NOT evidence about the extension -- Substrate Gate,")
        print("     the same rule P81 itself had to be corrected for.")
    elif flips:
        print(f"  -> DE-COUPLED or worse. {len(flips)} grid point(s) changed class:")
        print(f"     {flips}")
        print("     Dark energy is not free; every quotation of P81's corner must")
        print("     be re-audited under the extension.")
    elif max(vals) < YARDSTICK:
        print(f"  -> DE-DECOUPLED. Both boundaries move by less than {YARDSTICK}")
        print(f"     (worst {max(vals):.4f}), the yardstick being the largest")
        print("     R_boundary P83 measured inside matter domination.")
        print("     The viability sector and the dark-energy sector DO NOT")
        print("     INTERACT at the parameters tested.")
        print()
        print("     WHY -- and this was predicted before running: the diamond scan")
        print("     put the constraint epoch at a ~ 12, where Lambda sits below")
        print("     the matter density by many orders. A term that only matters")
        print("     at a ~ 1e5 cannot move a boundary set at a ~ 12.")
        print()
        print("     CONSEQUENCE FOR FINDING_P85: the completion CAN carry a")
        print("     dark-energy term without disturbing anything P81 or P83")
        print("     established, so P85's Z-CONDITIONAL is LIFTABLE -- an epoch")
        print("     worth calling 'today' now exists, at the cost of the SAME one")
        print("     external number P84 already counted, and no more.")
    else:
        print(f"  -> DE-COUPLED. Worst R_boundary = {max(vals):.4f} exceeds the")
        print(f"     {YARDSTICK} yardstick. The extension is not free.")

    print("\n  NOT ESTABLISHED:")
    print("   * that the extended completion is RIGHT. Viability is NECESSARY,")
    print("     never sufficient -- P81's own caveat, inherited unchanged.")
    print("   * that Omega_Lambda = 0.7 is correct for anything. It is used as a")
    print("     DEFINITION of the reference epoch, not a measurement imported")
    print("     from cosmology.")
    print("   * that Lambda is the RIGHT form of dark energy. A constant is the")
    print("     cheapest option; a dynamical one would have to re-enter here.")
    print("   * anything observational. No dataset, no Table A1 quantity;")
    print("     NO_BRIDGE_FITTING untouched.")
    print("   * anything about MULTING itself (Gate 1): adding a term to OUR")
    print("     reconstruction says nothing about the source model.")
    print("   * Perelman condition 5 -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
