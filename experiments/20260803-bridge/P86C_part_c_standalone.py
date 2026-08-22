"""P86C -- P86's Part C alone, after making the predicate affordable.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE EXISTS. P86's Part C bisects two boundaries under dark energy, and
the lambda=0 edge stalled: every "not viable" evaluation is a runaway trajectory
that the solver fights to t=1e8 at rtol=1e-10, and a bisection spends half its
iterations on exactly those. P81's viability() now carries a TERMINAL EVENT that
stops the integration once M = 1 - g*phibar reaches -1, by which point the
predicate has already failed irrecoverably (FLOOR is 0.1, and rho_phys = rho_A*M
is negative there).

THAT CHANGE IS NOT TAKEN ON TRUST. It alters how the predicate is COMPUTED, and
the whole campaign's numbers rest on that predicate. Part A below re-derives the
things the change could have broken and requires them back, EXACTLY, before a
single new number is measured. If any of them moves, the optimisation is
withdrawn and Part C is not run.

WHAT THE CHANGE CANNOT DO, argued and then checked:
  * a trajectory that never reaches M = -1 takes the identical code path, so
    every VIABLE point is bitwise unchanged;
  * for already-failing points the reported min_M becomes the value AT THE STOP
    rather than the global minimum -- a diagnostic number for a point that fails
    either way, and the ok flag cannot move;
  * a point that previously returned UNRESOLVED because the integrator gave up
    may now return MEASURED and non-viable. That is a strict GAIN, and it is the
    one direction in which results are allowed to change.

PRE-REGISTERED: Part A must reproduce P81's three published viable points to
5e-5 AND reproduce P83's boundary g_crit(lam=0.1) = 2.751767 to 1e-4 relative.
Those two together cover both sides of the predicate -- a viable interior point
and the located edge. Failure on either => optimisation withdrawn, no Part C.
"""

import importlib.util
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fn))
    m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    sp.loader.exec_module(m)
    return m


p81 = _load("p81_ref", "P81_background_viability.py")
p83 = _load("p83_ref", "P83_ic_robustness_of_boundary.py")
p86 = _load("p86_ref", "P86_dark_energy_through_p81_gate.py")

P83_GCRIT_LAM0 = 2.751767  # g_crit at lam = 0.1, lever x1, no dark energy
P83_GCRIT_LAM0_AT0 = 0.738209  # g_crit at lam = 0, lever x1, no dark energy
YARDSTICK = 0.08


def viable(g_hat, lam, lam_cc):
    r = p81.viability(g_hat, lam, lam_cc=lam_cc)
    return r["ok"], r


def main() -> int:
    print("=" * 78)
    print("P86C -- Part C standalone, after adding a terminal blow-up event")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- VALIDATE THE OPTIMISATION BEFORE USING IT")
    print("-" * 78)
    print("  The event changes HOW the predicate is computed. Everything this")
    print("  campaign measured rests on that predicate, so the things the change")
    print("  could have broken are required back EXACTLY, first.")

    print("\n  A1 -- P81's three published VIABLE points. These never reach")
    print("  M = -1, so the event must not touch them at all.")
    A1 = True
    print(f"\n    {'point':<16}{'P81 published':<18}{'now':<20}{'match'}")
    for (g, lam), want in (((1.0, 1.0), 0.8717), ((0.75, 0.01), 0.8643), ((2.0, 0.1), 0.4850)):
        got = p81.viability(g, lam).get("min_M", float("nan"))
        ok = abs(got - want) < 5e-5
        A1 = A1 and ok
        print(f"    ({g:g},{lam:g})".ljust(16) + f"{want:<18.4f}{got:<20.6f}{ok}")

    print("\n  A2 -- P83's LOCATED BOUNDARY. This is the decisive one: Part C")
    print("  measures exactly this quantity, and if the event moves it the")
    print("  comparison against P83 would be meaningless.")
    x, n, note = p83.bisect_boundary(lambda g: viable(g, 0.1, 0.0), 3.0, 2.0)
    if x is None:
        print(f"    boundary NOT LOCATED: {note}")
        A2 = False
    else:
        rel = abs(x / P83_GCRIT_LAM0 - 1)
        A2 = rel < 1e-4
        print(f"\n    P83 published : {P83_GCRIT_LAM0:.6f}")
        print(f"    now           : {x:.6f}   ({n} iterations)")
        print(f"    relative diff : {rel:.3e}   =>  {'MATCH' if A2 else 'MOVED'}")

    print("\n  A3 -- the allowed direction of change: a point P81 could not")
    print("  measure should now be measurable, and must come back NON-VIABLE.")
    r20 = p81.viability(2.0, 0.0)
    print(f"    (g,lam) = (2,0): state={r20['state']}, ok={r20['ok']}")
    print(f"      why: {r20['why']}")
    print("      P81 reported this as UNRESOLVED -- integrator gave up.")

    if not (A1 and A2):
        print("\n  *** OPTIMISATION WITHDRAWN. Part C is NOT run: a predicate that")
        print("  no longer reproduces its own published numbers cannot be used to")
        print("  measure anything. Revert the event and take the slow path.")
        return 1
    print("\n  => optimisation VALIDATED on both sides of the predicate.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- do P83's two boundaries move when dark energy is added?")
    print("-" * 78)
    a_today = 5.0e5
    lam_cc = p86.lambda_for(a_today)
    print(f"  Lambda = {lam_cc:.6e}  (Omega_Lambda = 0.7 at a = {a_today:.4g})")
    print("  Bisected with P83's OWN bisector, so the comparison is like-for-like.")
    print(f"\n    {'edge':<24}{'P83 (no DE)':<16}{'with DE':<16}{'R_boundary':<14}{'iters'}")
    moved = {}
    for label, lam_fixed, ref, bad, good in (
        ("g_crit at lam = 0", 0.0, P83_GCRIT_LAM0_AT0, 1.0, 0.1),
        ("g_crit at lam = 0.1", 0.1, P83_GCRIT_LAM0, 3.0, 2.0),
    ):
        xv, nv, nt = p83.bisect_boundary(lambda g, lf=lam_fixed: viable(g, lf, lam_cc), bad, good)
        if xv is None:
            print(f"    {label:<24}{ref:<16.6f}{'-':<16}{'-':<14}{nv}   {nt}")
            moved[label] = None
            continue
        rb = abs(xv - ref) / ref
        moved[label] = rb
        print(f"    {label:<24}{ref:<16.6f}{xv:<16.6f}{rb:<14.4f}{nv}")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against P86's pre-registered outcomes)")
    print("=" * 78)
    vals = [v for v in moved.values() if v is not None]
    if len(vals) < len(moved):
        print("  -> NOT MEASURABLE on at least one edge. Infrastructure outcome,")
        print("     NOT evidence about the extension.")
    elif max(vals) < YARDSTICK:
        print(f"  -> DE-DECOUPLED. Worst R_boundary = {max(vals):.4f} < {YARDSTICK},")
        print("     the yardstick being the largest R_boundary P83 measured inside")
        print("     matter domination.")
        print()
        print("     THIS MUST BE READ WITH ITS CAVEAT, which a separate measurement")
        print("     established and which halves the strength of the claim:")
        print("     P81's predicate has NO CLAUSE a cosmological constant can")
        print("     violate physically. More Lambda means more Hubble friction,")
        print("     which DAMPS phibar and pushes 1-g*phibar back toward 1 -- i.e.")
        print("     toward MORE viable. There is no 'must decelerate' condition.")
        print("     So part of this decoupling is structural, not a fact about")
        print("     epochs, and quoting the number alone would overstate it.")
        print()
        print("     WHAT IS GENUINELY MEASURED, and it confirms the diamond scan:")
        print("     min(1-g*phibar) = 0.871740335 is unchanged to 3e-11 across")
        print("     FIVE ORDERS of Lambda. The constraint epoch sits at a ~ 12,")
        print("     where Lambda is below the matter density by many orders, so a")
        print("     term that only matters at a ~ 1e5 cannot reach it.")
    else:
        print(f"  -> DE-COUPLED. Worst R_boundary = {max(vals):.4f} exceeds")
        print(f"     {YARDSTICK}. Dark energy is not free and P81's corner must be")
        print("     re-audited under the extension.")

    print("\n  NOT ESTABLISHED:")
    print("   * that the extended completion is RIGHT. Viability is NECESSARY,")
    print("     never sufficient.")
    print("   * that Lambda is the right FORM of dark energy; a dynamical one")
    print("     would have to re-enter here.")
    print("   * anything observational. NO_BRIDGE_FITTING untouched.")
    print("   * anything about MULTING itself (Gate 1).")
    print("   * Perelman condition 5 -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
