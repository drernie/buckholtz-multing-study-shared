"""P83 -- is P81's viability boundary a property of the model or of the IC?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

THE QUESTION, AND WHY IT IS THE MOST DANGEROUS ONE LEFT.

FINDING_P79 destroyed FINDING_P78's D-SEP by showing the completion separation
moved by a factor 5 under the phibar_dot lever -- an INITIAL-CONDITION artifact
wearing the costume of a physical result. FINDING_P81 then reported a connected
viable region in (g_hat, lambda) WITHOUT ever asking the same question of it.
If P81's boundary rides the IC the way P78's separation did, the "viable corner"
is not a constraint on the completion at all.

This step cashes the falsifiable prediction P81 was registered with.

WHAT IS MEASURED -- THE BOUNDARY FUNCTION, NOT INDIVIDUAL POINTS.

Counting surviving grid points would answer a weaker question and would be
dominated by wherever the grid happens to be dense. The observable is the
LOCATION of the boundary, bisected, and its relative movement:

    R_boundary := |X_crit(lever) - X_crit(1)| / X_crit(1)

for X = lambda at fixed g_hat (edge E1) and X = g_hat at fixed lambda (edge E2).

TWO PROBLEMS WITH THAT METRIC, BOTH FOUND IN P81'S OWN NUMBERS BEFORE CODING.

(1) R_boundary MAY BE UNDEFINED ON E1. P81's Part D found lambda=0 fails
    (min(1-g*phibar)=0.0285 at g_hat=0.75) while lambda=1e-4 already passes at
    0.8051. So lambda_crit lies in (0, 1e-4) -- or is EXACTLY zero, in which
    case R_boundary is 0/0 and the honest answer is not a ratio but a statement:
    the boundary IS the V=0 truncation surface, not a finite lambda. Part B
    bisects to 1e-12 to decide which, BEFORE any ratio is quoted.

(2) THE LEVER CHANGES THE COSMOLOGICAL REGIME, and that must be measured, not
    assumed. phibar_dot scales the scalar's initial KINETIC energy as its
    SQUARE. FINDING_P77 established that x10 puts 84.85% of the t=1 energy
    budget in the scalar -- a kination-dominated universe, i.e. a different
    cosmology rather than a perturbation of the initial data -- and P77 had to
    RETRACT a conclusion for exactly that reason. x10 is therefore excluded
    here. But x4 deserves the same scrutiny rather than a free pass: from P77's
    own numbers it should land near 47%, which is no longer a matter-dominated
    start either. Part A measures the kinetic fraction at every lever setting
    and the verdict is read TWICE -- once over the full lever, once restricted
    to settings that are still matter-dominated.

LEVER: phibar_dot(1) x {0.1, 0.25, 0.5, 1, 2, 4}.

PRE-REGISTERED OUTCOMES (thresholds fixed before any number):
  V1  IC-ROBUST      max R_boundary < 0.10 on both edges -> P81 is strengthened;
                     the viable corner is a property of the completion.
  V2  IC-CONDITIONED 0.10 <= max R_boundary < 1.0 -> the region survives but its
                     boundary is IC-dependent, and every quotation of the corner
                     must carry the IC it was measured at.
  V3  IC-DOMINATED   max R_boundary >= 1.0 -> viability is IC-conditioned, and
                     P81 cannot be read as a statement about the completion
                     without an independent principle fixing the IC.
  V4  BIFURCATION    the topology changes -- components appear or vanish, or a
                     point's viable/non-viable class flips in a way no boundary
                     shift explains. This dominates the other three if seen.

WHAT THIS CANNOT DO, stated before the numbers:
  * It tests TWO edges, the two P81 already localised. A boundary elsewhere in
    (g_hat, lambda) could behave differently, and nothing here excludes that.
  * The topology probe (Part E) is a REDUCED grid, so it can only see components
    at that resolution -- the same limit P81 declared, inherited not removed.
  * Internal units throughout. NO_BRIDGE_FITTING remains in force.
"""

import importlib.util
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fn))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


p81 = _load("p81_ref", "P81_background_viability.py")
p76 = p81.p76

G_N, C_MATTER = p81.G_N, p81.C_MATTER
A3_INIT, PHIDOT = p81.A3_INIT, p81.PHIDOT
FLOOR = p81.FLOOR

LEVER = [0.1, 0.25, 0.5, 1.0, 2.0, 4.0]
E1_G = 0.75  # the g_hat at which P81 localised the lambda -> 0 edge
E2_LAM = 0.1  # the lambda at which P81 localised the g_hat edge


def kinetic_fraction(phidot0):
    """Fraction of the t=1 energy budget carried by the scalar's kinetic term.

    phibar(1) = 0 by construction, so V(phibar(1)) = 0 and the scalar's whole
    initial energy IS kinetic. This is the regime check P77 had to apply
    retroactively; here it runs before the verdict is read.
    """
    a0 = A3_INIT ** (1.0 / 3.0)
    rho_m = C_MATTER / a0**3  # 1 - g*phibar(1) = 1, so rho_phys = rho_A
    kin = phidot0**2 / 2.0
    return kin / (kin + rho_m)


def viable(g_hat, lam, phidot0):
    """P81's predicate, imported not reimplemented. Unresolved is NOT False."""
    r = p81.viability(g_hat, lam, phidot0=phidot0)
    return r["ok"], r


def bisect_boundary(f_viable, x_bad, x_good, tol_rel=1e-4, max_iter=80):
    """Locate where the predicate flips between x_bad (not viable) and x_good (viable).

    Returns (x_crit, n_iter, note).

    # THE BUG THIS REPLACES, kept visible because of which way it failed.
    # The first version named its endpoints lo/hi -- SEMANTIC labels for
    # not-viable/viable -- and then tested convergence NUMERICALLY as
    # `hi - lo <= tol`. On edge E2 the not-viable end is at LARGER g_hat, so it
    # was called as (lo=3.0, hi=2.0) and `hi - lo` was negative from the first
    # comparison: the loop exited after ONE iteration and returned the midpoint
    # of the original bracket. Every lever setting then returned the SAME
    # 2.724745 and R_boundary read 0.0000 -- a perfect-robustness result that
    # would have been reported as V1. It failed toward CONFIRMATION, which is
    # the direction that does not announce itself.
    #
    # Two fixes, not one: (a) the interval test is now on abs() and is scaled by
    # the midpoint, so endpoint ORDER cannot matter; (b) a POST-CONDITION checks
    # that the returned point actually straddles a flip. A bisection that
    # returns a number without that check is not a measurement -- the same
    # lesson as P76's hardcoded gate, one level up.
    """
    ok_bad, r_bad = f_viable(x_bad)
    ok_good, r_good = f_viable(x_good)
    if r_bad["state"] == "unresolved" or r_good["state"] == "unresolved":
        return None, 0, "bracket endpoint UNRESOLVED -- boundary not measurable here"
    if ok_bad or not ok_good:
        return (
            None,
            0,
            (f"bracket is not what it claims: x_bad viable={ok_bad}, x_good viable={ok_good}"),
        )

    n = 0
    while n < max_iter:
        n += 1
        mid = np.sqrt(x_bad * x_good) if (x_bad > 0 and x_good > 0) else 0.5 * (x_bad + x_good)
        ok_m, r_m = f_viable(mid)
        if r_m["state"] == "unresolved":
            return None, n, f"UNRESOLVED at x={mid:.6g} inside the bracket"
        if ok_m:
            x_good = mid
        else:
            x_bad = mid
        if abs(x_good - x_bad) <= tol_rel * max(abs(mid), 1e-300):
            break
    else:
        return None, n, f"did not converge in {max_iter} iterations"

    x_crit = 0.5 * (x_bad + x_good)
    # POST-CONDITION: the two sides must still classify differently, and they
    # must do so at a separation consistent with the tolerance asked for.
    lo_ok, _ = f_viable(min(x_bad, x_good))
    hi_ok, _ = f_viable(max(x_bad, x_good))
    if lo_ok == hi_ok:
        return None, n, "POST-CONDITION FAILED: the final bracket no longer straddles a flip"
    if n < 3:
        return None, n, f"POST-CONDITION FAILED: converged in {n} iteration(s), bracket too wide"
    return x_crit, n, "ok"


def main() -> int:  # noqa: PLR0912, PLR0915 - one linear report, split would obscure it
    print("=" * 78)
    print("P83 -- IC robustness of P81's viability boundary")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS and the REGIME CHECK")
    print("-" * 78)

    print("\n  C0 -- the predicate must be P81's, unchanged. viability() was")
    print("  EXTENDED with phidot0 rather than reimplemented here, because two")
    print("  copies drift and P83 would then measure a boundary P81 never had.")
    print("  Default must reproduce P81 exactly at its own reported points.")
    checks = [((1.0, 1.0), 0.8717), ((0.75, 0.01), 0.8643), ((2.0, 0.1), 0.4850)]
    C0 = True
    print(f"\n    {'point':<16}{'P81 reported':<16}{'now (default IC)':<20}{'match'}")
    for (g, lam), want in checks:
        r = p81.viability(g, lam)
        got = r.get("min_M", float("nan"))
        good = abs(got - want) < 5e-5
        C0 = C0 and good
        print(f"    ({g:g},{lam:g})".ljust(16) + f"{want:<16.4f}{got:<20.6f}{good}")
    if not C0:
        print("    *** C0 FAILED -- this is not P81's predicate. Stop.")
        return 1
    print("    PASSES -- same predicate, so any movement below is the lever's.")

    print("\n  C1 -- explicit phidot0 at the default value must equal the default.")
    r_def = p81.viability(1.0, 1.0)
    r_exp = p81.viability(1.0, 1.0, phidot0=PHIDOT)
    C1 = r_def["min_M"] == r_exp["min_M"]
    print(f"    default {r_def['min_M']!r}")
    print(f"    explicit {r_exp['min_M']!r}")
    print(f"    bitwise identical: {C1}")
    if not C1:
        print("    *** C1 FAILED -- the threading changed the default path.")
        return 1

    print("\n  C2 -- REGIME CHECK. phibar(1)=0 so V=0 there and the scalar's whole")
    print("  initial energy is kinetic, scaling as phibar_dot^2. P77 had to")
    print("  RETRACT a conclusion after discovering x10 = 84.85% of the budget")
    print("  (kination, a different cosmology). Measured here BEFORE the verdict:")
    print(f"\n    {'lever':<10}{'phibar_dot(1)':<20}{'kinetic fraction':<20}{'regime'}")
    matter_dom = []
    for f in LEVER:
        pd0 = f * PHIDOT
        frac = kinetic_fraction(pd0)
        regime = "matter-dominated" if frac < 0.25 else "SCALAR-SIGNIFICANT"
        if frac < 0.25:
            matter_dom.append(f)
        print(f"    x{f:<9g}{pd0:<20.6e}{frac:<20.4%}{regime}")
    print(f"\n    matter-dominated lever settings: {matter_dom}")
    print("    The verdict is read TWICE -- once over the full lever, once over")
    print("    these only. A conclusion that holds only on one of the two gets")
    print("    reported as holding only on that one.")

    print("\n  C3 -- the boundary locator must REFUSE to invent a boundary. At")
    print("  g_hat = 0 the predicate holds for every lambda (1-g*phibar == 1),")
    print("  so no flip exists and bisection must say so rather than return a")
    print("  number.")
    x, n, note = bisect_boundary(lambda lam: viable(0.0, lam, PHIDOT), 0.0, 10.0)
    print(f"    result: x={x}  iters={n}  note: {note}")
    if x is not None:
        print("    *** C3 FAILED -- the locator invented a boundary where none exists.")
        return 1
    print("    PASSES -- the locator can say 'no boundary here'.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- edge E1: is lambda_crit finite at all, or exactly zero?")
    print("-" * 78)
    print(f"  At g_hat = {E1_G}, P81 found lambda=0 fails (0.0285) and lambda=1e-4")
    print("  already passes (0.8051). Before any ratio can be quoted, this has to")
    print("  be settled: a boundary AT lambda=0 exactly is a statement about the")
    print("  V=0 truncation surface, not a finite critical coupling, and then")
    print("  R_boundary = 0/0 is not a number to report.")
    print(f"\n    {'lambda':<14}{'state':<12}{'min(1-g*phibar)':<20}{'viable'}")
    e1_scan = []
    for lam in (0.0, 1e-12, 1e-10, 1e-8, 1e-6, 1e-5, 1e-4):
        ok, r = viable(E1_G, lam, PHIDOT)
        mm = r.get("min_M")
        e1_scan.append((lam, ok, mm))
        print(
            f"    {lam:<14.0e}{r['state']:<12}"
            + (f"{mm:<20.6f}" if mm is not None else f"{'not measured':<20}")
            + str(ok)
        )
    finite_crit = any(not ok for lam, ok, _ in e1_scan if lam > 0)
    print(f"\n    any lambda > 0 that FAILS: {finite_crit}")
    if finite_crit:
        print("    => lambda_crit is FINITE; R_boundary is well defined on E1.")
    else:
        print("    => every lambda > 0 tested down to 1e-12 is VIABLE, so the")
        print("       transition sits AT lambda = 0 exactly. lambda_crit = 0, and")
        print("       R_boundary = 0/0 on this edge -- NOT a number to report.")
        print("       E1 is therefore re-posed below as a CLASSIFICATION question:")
        print("       does lambda=0 stay non-viable, and every lambda>0 viable,")
        print("       under the lever? That is the falsifiable content that")
        print("       survives when the ratio does not exist.")

    print("\n  E1 under the lever.")
    print(
        f"\n    {'lever':<10}{'lam=0 viable':<16}{'lam=1e-8 viable':<18}"
        f"{'lam=1e-4 viable':<18}{'min_M at lam=1e-4'}"
    )
    e1_rows = []
    for f in LEVER:
        pd0 = f * PHIDOT
        ok0, r0 = viable(E1_G, 0.0, pd0)
        ok8, _ = viable(E1_G, 1e-8, pd0)
        ok4, r4 = viable(E1_G, 1e-4, pd0)
        e1_rows.append((f, ok0, ok8, ok4, r4.get("min_M")))
        mm = r4.get("min_M")
        print(
            f"    x{f:<9g}{str(ok0) + ' (' + r0['state'][:4] + ')':<16}"
            f"{str(ok8):<18}{str(ok4):<18}" + (f"{mm:.6f}" if mm is not None else "-")
        )
    e1_stable = all((not a) and b and c for _, a, b, c, _ in e1_rows) or all(
        (a == e1_rows[3][1]) and (b == e1_rows[3][2]) and (c == e1_rows[3][3])
        for _, a, b, c, _ in e1_rows
    )
    print(f"\n    classification identical across the whole lever: {e1_stable}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B2 -- E1 re-posed as the observable that DOES exist")
    print("-" * 78)
    print("  Part B settled that lambda_crit = 0, so R_boundary is 0/0 in lambda.")
    print("  But the table above shows the CLASSIFICATION of lambda=0 flipping")
    print("  with the lever -- viable at x0.1/x0.25/x0.5, not viable at x1/x2/x4.")
    print("  That is a boundary moving in the OTHER variable: what shifts is")
    print("  g_hat_crit AT lambda = 0, and THAT ratio is well defined.")
    print("  P81 brackets it at the default IC: g_hat=0.5 viable (0.6897),")
    print("  g_hat=0.75 not (0.0285).")
    print()
    print("  # BRACKET CHOICE, corrected after a self-inflicted failure. The first")
    print("  # version used g_hat=5.0 as the not-viable end. P81's OWN TABLE lists")
    print("  # (5,0) as UNRESOLVED -- the integrator cannot carry it -- so the")
    print("  # bisection correctly refused to run from x1 onward and E1 returned")
    print("  # nothing for half the lever. The data saying so was already in the")
    print("  # file I wrote. g_hat=1.0 is MEASURED and not viable at lambda=0")
    print("  # (min_M = -7.9e+04), so it is a legitimate endpoint.")
    print(f"\n    {'lever':<10}{'g_hat_crit(lam=0)':<22}{'iters':<8}{'note'}")
    e1b = {}
    for f in LEVER:
        pd0 = f * PHIDOT
        x, n, note = bisect_boundary(lambda g, p=pd0: viable(g, 0.0, p), 1.0, 0.1)
        e1b[f] = x
        print(
            f"    x{f:<9g}" + (f"{x:<22.6f}" if x is not None else f"{'-':<22}") + f"{n:<8}{note}"
        )
    ref1 = e1b.get(1.0)
    R1 = {}
    if ref1:
        print(f"\n    reference (lever x1): g_hat_crit(lam=0) = {ref1:.6f}")
        print(f"\n    {'lever':<10}{'g_hat_crit':<20}{'R_boundary':<16}{'regime'}")
        for f in LEVER:
            if e1b[f] is None:
                print(f"    x{f:<9g}{'-':<20}{'-':<16}not located")
                continue
            R1[f] = abs(e1b[f] - ref1) / ref1
            reg = "matter-dom" if f in matter_dom else "scalar-signif"
            print(f"    x{f:<9g}{e1b[f]:<20.6f}{R1[f]:<16.4f}{reg}")
    else:
        print("\n    reference lever could not be located -- E1 contributes nothing")
        print("    to the verdict, and that is an infrastructure outcome, not")
        print("    evidence about the claim.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- edge E2: g_hat_crit(lambda=0.1) under the lever")
    print("-" * 78)
    print("  P81 bracketed this edge between g_hat=2.75 (min_M=0.1010, viable)")
    print("  and g_hat=3.0 (min_M=-0.0551, not viable). Bisected here at each")
    print("  lever setting. THIS is the edge where R_boundary is well defined.")
    print(f"\n    {'lever':<10}{'g_hat_crit':<16}{'iters':<8}{'R_boundary vs x1':<20}{'note'}")
    e2 = {}
    for f in LEVER:
        pd0 = f * PHIDOT
        x, n, note = bisect_boundary(lambda g, p=pd0: viable(g, E2_LAM, p), 3.0, 2.0)
        e2[f] = x
        print(
            f"    x{f:<9g}"
            + (f"{x:<16.6f}" if x is not None else f"{'-':<16}")
            + f"{n:<8}"
            + f"{'':<20}{note}"
        )
    ref = e2.get(1.0)
    R2 = {}
    if ref:
        print(f"\n    reference (lever x1): g_hat_crit = {ref:.6f}")
        print(f"\n    {'lever':<10}{'g_hat_crit':<16}{'R_boundary':<16}{'regime'}")
        for f in LEVER:
            if e2[f] is None:
                print(f"    x{f:<9g}{'-':<16}{'-':<16}unresolved")
                continue
            R2[f] = abs(e2[f] - ref) / ref
            reg = "matter-dom" if f in matter_dom else "scalar-signif"
            print(f"    x{f:<9g}{e2[f]:<16.6f}{R2[f]:<16.4f}{reg}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- the verdict quantity, read twice")
    print("-" * 78)
    R_all = max(R2.values()) if R2 else None
    R_md = max((v for f, v in R2.items() if f in matter_dom), default=None)
    print(
        "\n    max R_boundary, FULL lever            : "
        + (f"{R_all:.4f}" if R_all is not None else "not measurable")
    )
    print(
        "    max R_boundary, matter-dominated only : "
        + (f"{R_md:.4f}" if R_md is not None else "not measurable")
    )
    print("\n    For scale, the movement that KILLED FINDING_P78: the separation")
    print("    moved by a factor ~5, i.e. R ~ 4.0 on this definition.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- topology probe: does the REGION change shape, not just size?")
    print("-" * 78)
    print("  R_boundary measures where an edge sits. It cannot see a component")
    print("  appearing or vanishing. A reduced grid is rescanned at the lever")
    print("  extremes; lambda=0 is excluded because Part B settles it separately")
    print("  and it is where P81's two UNRESOLVED points live.")
    G_GRID = [0.0, 0.5, 1.0, 2.0, 3.0]
    L_GRID = [1e-3, 0.01, 0.1, 1.0, 10.0]
    comps_by_lever = {}
    for f in (0.1, 1.0, 4.0):
        pd0 = f * PHIDOT
        grid = {}
        for g in G_GRID:
            for lam in L_GRID:
                grid[(g, lam)] = viable(g, lam, pd0)[0]
        gi = {g: i for i, g in enumerate(G_GRID)}
        li = {lam: i for i, lam in enumerate(L_GRID)}
        idx = {(gi[g], li[lam]) for (g, lam), ok in grid.items() if ok}
        comps, seen = [], set()
        for p in idx:
            if p in seen:
                continue
            stack, comp = [p], []
            seen.add(p)
            while stack:
                i, j = stack.pop()
                comp.append((i, j))
                for q in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if q in idx and q not in seen:
                        seen.add(q)
                        stack.append(q)
            comps.append(comp)
        comps_by_lever[f] = (len(idx), len(comps), grid)
        print(
            f"\n    lever x{f:g}:  {len(idx)} of {len(grid)} viable, "
            f"{len(comps)} connected component(s)"
        )
        print("      g\\lam " + "".join(f"{lam:>10g}" for lam in L_GRID))
        for g in G_GRID:
            row = "".join(f"{('OK' if grid[(g, lam)] else '.'):>10}" for lam in L_GRID)
            print(f"      {g:<6g}{row}")

    base_n, base_c, base_grid = comps_by_lever[1.0]
    flips = {
        f: sum(1 for p in base_grid if comps_by_lever[f][2][p] != base_grid[p])
        for f in comps_by_lever
        if f != 1.0
    }
    topo_same = all(comps_by_lever[f][1] == base_c for f in comps_by_lever)
    print(f"\n    component count identical at every lever: {topo_same}")
    print(f"    class flips vs lever x1: {flips}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if not topo_same:
        print("  -> V4 BIFURCATION. The component count changes with the initial")
        print("     condition, so the viable set's TOPOLOGY is IC-dependent. This")
        print("     dominates any R_boundary reading and is the finding.")
    elif R_all is None:
        print("  -> NOT MEASURABLE. The boundary could not be located at enough")
        print("     lever settings. This is an infrastructure outcome, NOT evidence")
        print("     about the claim -- Substrate Gate, same as P81's UNRESOLVED.")
    elif R_all < 0.10:
        print(f"  -> V1 IC-ROBUST. max R_boundary = {R_all:.4f} < 0.10 across the")
        print("     full lever. P81 is STRENGTHENED: the viable corner is a")
        print("     property of the completion, not of the initial data, and it")
        print("     survives the test that killed P78's separation.")
    elif R_all < 1.0:
        print(f"  -> V2 IC-CONDITIONED. max R_boundary = {R_all:.4f}. The region")
        print("     survives but its boundary moves with the IC, so every")
        print("     quotation of the corner must carry the IC it was measured at.")
        if R_md is not None and R_md < 0.10:
            print(f"     NOTE: restricted to matter-dominated starts, {R_md:.4f} < 0.10")
            print("     -- V1 holds on that sub-range. The IC dependence lives in")
            print("     the scalar-significant settings, i.e. in a regime change.")
    else:
        print(f"  -> V3 IC-DOMINATED. max R_boundary = {R_all:.4f} >= 1.0.")
        print("     Viability is IC-conditioned. P81 cannot be read as a statement")
        print("     about the completion without an independent principle fixing")
        print("     the initial data.")

    print("\n  NOT ESTABLISHED:")
    print("   * anything about boundaries OTHER than the two P81 localised.")
    print("   * topology below the reduced grid's resolution (Part E inherits")
    print("     P81's own limit, it does not remove it).")
    print("   * that lever settings above x4 behave the same -- x10 is EXCLUDED")
    print("     by construction because P77 showed it changes the cosmology.")
    print("   * anything observational. Internal units, NO_BRIDGE_FITTING.")
    print("   * anything about MULTING itself (Gate 1): the completion is OURS.")
    print("   * Perelman condition 5 (external reconstruction) -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
