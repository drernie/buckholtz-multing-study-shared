"""P91 -- the viability boundary g_crit(lambda) through P88's implementation.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

REVISION 2. Revision 1 returned B-SUSPICIOUS-TIGHT and was withdrawn by its own
pre-registered rule. p91_tightness_probe.py then measured the cause, and it was
not one cause but two -- one a real result, one a defect in this file's own
control. Both are recorded rather than silently fixed, and both change the
design.

  (a) THE AGREEMENT WAS REAL, ON BOTH EDGES. Re-locating each flip at tol 1e-13
      instead of 1e-4:
        lambda=0    0.7382122147416424 vs 0.7382122147462467  ->  6.24e-12
        lambda=0.1  2.751764836587313  vs 2.7517648365591185  ->  1.02e-11
      The 2.220e-16 that triggered the withdrawal was alignment luck between two
      dyadic grids, not shared state.

  (b) THE lambda=0.1 CONTROL FAILED BY ITS OWN CONSTRUCTION -- the eighth this
      session and this one entirely mine. Revision 1 chose "different brackets"
      by eye: (3.5, 1.5) against P83's (3.0, 2.0). But (3.5+1.5)/2 = 2.5 =
      (3.0+2.0)/2. Same first midpoint; one extra step later the reconstruction
      sits at bracket (3.0, 2.5), exactly where P81 already was, and from there
      the paths COINCIDE -- 12 of 13 midpoints shared, identical final bracket,
      bitwise identical answer. That edge's "perfect agreement" demonstrated
      only that bisection is deterministic.

FOUR CONSEQUENCES FOR THE DESIGN, all sharpenings rather than relaxations.

  1. INDEPENDENCE IS MEASURED, NOT CHOSEN. Every bisection records its path.
     "The brackets look different" is not a measurement; "the paths diverged"
     is. The lambda=0.1 bracket also moves to (3.37, 1.93) -- midpoint 2.65,
     not 2.5 -- but the post-condition is what enforces the property.

  2. INDEPENDENCE IS MEASURED ON THE SEARCHES THAT ARE ACTUALLY SCORED. The
     merge is a COARSE-tolerance phenomenon: once the midpoints get within
     1e-11 of the flip the two predicates disagree and the paths separate
     regardless of where they started, which is exactly why the tight run
     returned two different numbers on the merged edge. So the post-condition
     is applied to the tight searches -- they must SEPARATE before converging.
     Applying it to the coarse paths instead would throw away a valid
     measurement because of a defect in a number that is not being scored.

  3. THE SCORED QUANTITY CHANGES. Revision 1 scored the tol=1e-4 answers and
     pre-registered "better than 1e-8 means shared state". That inference was
     WRONG: two bisections each land within tol of the true flip, so their
     mutual difference can be anything from 1e-16 to 1e-4 depending on how the
     dyadic grids align. It measures grid alignment, not agreement. What
     carries information is where each predicate ACTUALLY flips.

     This also REFUTES a prediction I registered in FINDING_P89 -- "the boundary
     should reproduce ONLY to its bisection tolerance (about 1e-4) and NOT
     better". It reproduces about eight orders better. The prediction confused
     the precision of the SEARCH with the accuracy of the ANSWER.

  4. PART C IS AIMED AT THE RIGHT OBJECT. P81 decides the clause by a min over
     3000 sampled points; the reconstruction decides it by a TERMINAL EVENT on
     the continuous trajectory, so no probe grid can change its answer -- if the
     event never fires, no dip below FLOOR occurred anywhere, on any grid. That
     is why revision 1's Part C found exactly 0.000e+00 when it varied the
     RECONSTRUCTION's n_probe: it was varying something the answer does not use.
     The real question was always whether P81's SAMPLED min steps over a dip, so
     P81's n_probe is varied here instead.

WHAT THE RECONSTRUCTION CAN AND CANNOT EXPRESS (unchanged, still measured in
Part 0 rather than assumed). P81 fails a point on any of four clauses: a <= 0,
rho_phys <= 0, min(1 - g*phibar) <= FLOOR, H non-monotone. Because P88's
formulation uses a AS THE INDEPENDENT VARIABLE, "a <= 0" is vacuous here and
"H non-monotone" cannot be surveyed where H -> 0. So the comparison is licensed
ONLY IF min(1-g*phibar) is what binds at the boundary.

  The predicate's span is defined in t and the reconstruction has no t, so
  rather than substituting an a-based span -- which would silently change the
  predicate -- t is carried as a DERIVED state variable, dt/dN = 1/H, and the
  run stops when t reaches T_END. The roles of t and a are exactly SWAPPED
  relative to P76/P81.

PRE-REGISTERED OUTCOMES (revision 2):
  B-NOT-COMPARABLE   Part 0 shows a clause other than min(1-g*phibar) binding,
                     or no edge passes the independence post-condition.
  B-CONFIRMED        tight-tolerance flip agreement < 1e-8 on every independent
                     edge -- the two implementations locate the same boundary.
  B-MARGINAL         between 1e-8 and 1e-4 -> named, not smoothed.
  B-DISCREPANT       worse than 1e-4 -> the boundary LOCATION is
                     discretization-dependent in a way eps, f and mu were not.

PART C, PRE-REGISTERED SEPARATELY: if P81's boundary moves when ITS OWN n_probe
is varied, then P81's boundary is PARTLY A PROPERTY OF ITS PROBE GRID -- a fact
about the claim, not about either implementation. Diamond D1 says phibar is
monotone at lambda=0 and oscillates at lambda!=0, so movement is expected at
lambda=0.1 and not at lambda=0. If lambda=0.1 does NOT move, the concern is
unfounded and D1's picture needs revisiting.

WHAT THIS CANNOT DO: same person wrote both implementations; a reconstruction
tests the implementation, never the specification; nothing observational;
Gate 1 holds.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p81 = _load("P81_background_viability.py", "p81_for_boundary")

G_N, C_M = 1.0, 1.0
A3_0 = 6.0 * np.pi - 1.0
A_0 = A3_0 ** (1.0 / 3.0)
U_0 = np.sqrt(2.0) / A3_0
T0, T_END = 1.0, 1e8
FLOOR = 0.1
N_PROBE = 3000
TIGHT = 1e-12
MIN_SEPARATED = 3  # tight paths must diverge for at least this many midpoints


# ---------------------------------------------------------------------------
# THE RECONSTRUCTION. a is the axis; t is INTEGRATED. Roles swapped vs P76/P81.
# ---------------------------------------------------------------------------


def _H_of(a, phi, u, g, lam):
    rho_phys = (C_M / a**3) * (1.0 - g * phi)
    arg = (8.0 * np.pi * G_N / 3.0) * (rho_phys + u * u / 2.0 + lam * phi**4 / 4.0)
    return np.sqrt(arg) if arg > 0 else 0.0


def bg_rhs_lnA(g, lam):
    """d/dN of (phibar, phibar_dot, t) with N = ln a. dt/dN = 1/H is the swap."""

    def f(N, y):
        a = np.exp(N)
        phi, u, _t = y
        H = _H_of(a, phi, u, g, lam)
        if H <= 0.0:
            return np.zeros(3)
        rho_A = C_M / a**3
        return np.array([u, g * rho_A - 3.0 * H * u - lam * phi**3, 1.0]) / H

    return f


def _floor_event(g):
    """Terminal event on (1 - g*phibar) - FLOOR.

    # WHY this makes the reconstruction's answer grid-free, which the tightness
    # probe made visible: the integrator locates the crossing on the CONTINUOUS
    # trajectory. If it never fires, no dip below FLOOR happened anywhere -- so
    # the min over any probe grid is above FLOOR and the classification is the
    # same for every grid. P81's SAMPLED min can, in principle, step over a dip,
    # which is what Part C now tests.
    """

    def ev(_N, y):
        return (1.0 - g * y[0]) - FLOOR

    ev.terminal = True
    ev.direction = -1
    return ev


def _t_event():
    def ev(_N, y):
        return y[2] - T_END

    ev.terminal = True
    ev.direction = 1
    return ev


def viable_recon(g, lam, n_probe=N_PROBE, grid="t"):
    """Three outcomes, exactly as P81: viable / non-viable / unresolved.

    grid="t"  probe points log-uniform in t, matching P81's sampling semantics.
    grid="N"  probe points uniform in N, natural for this formulation.
    Neither can change the CLASSIFICATION -- the terminal event decides it --
    which is itself a measured fact rather than a design intention; see the
    module docstring, consequence 4.
    """
    with np.errstate(all="ignore"):
        try:
            s = solve_ivp(
                bg_rhs_lnA(g, lam),
                (np.log(A_0), np.log(A_0) + 60.0),
                [0.0, U_0, T0],
                method="DOP853",
                rtol=1e-10,
                atol=1e-22,
                dense_output=True,
                events=[_floor_event(g), _t_event()],
            )
        except Exception as exc:  # noqa: BLE001 - the reason IS the result here
            return {"ok": False, "state": "unresolved", "why": f"raised {type(exc).__name__}"}
        if not s.success:
            return {"ok": False, "state": "unresolved", "why": "integrator gave up"}
        if len(s.t_events[0]):
            return {
                "ok": False,
                "state": "measured",
                "min_M": FLOOR,
                "why": f"1-g*phibar fell through FLOOR at a={np.exp(s.t_events[0][0]):.4g}",
            }
        if not len(s.t_events[1]):
            return {
                "ok": False,
                "state": "unresolved",
                "why": f"t reached only {s.y[2][-1]:.3g} of {T_END:.3g}",
            }

        n_end = float(s.t_events[1][0])
        if grid == "N":
            NN = np.linspace(np.log(A_0), n_end, n_probe)
        else:
            NN_fine = np.linspace(np.log(A_0), n_end, 40 * n_probe)
            t_fine = s.sol(NN_fine)[2]
            t_want = np.exp(np.linspace(np.log(T0), np.log(T_END), n_probe))
            NN = np.interp(np.clip(t_want, t_fine[0], t_fine[-1]), t_fine, NN_fine)
        phi = s.sol(NN)[0]
        if not np.all(np.isfinite(phi)):
            return {"ok": False, "state": "unresolved", "why": "trajectory overflowed"}

    min_M = float(np.min(1.0 - g * phi))
    ok = min_M > FLOOR
    return {
        "ok": ok,
        "state": "measured",
        "min_M": min_M,
        "why": "viable" if ok else f"min(1-g*phibar)={min_M:.6g}<={FLOOR}",
    }


# ---------------------------------------------------------------------------
# Bisection, written here and PATH-RECORDING. P83's own is not imported: a
# shared searcher would make "independent search" false while looking fine.
# ---------------------------------------------------------------------------


def bisect(f_ok, x_bad, x_good, tol_rel=1e-4, max_iter=200):
    """Returns (x_crit, path, note). path is every midpoint tested, in order."""
    ob, og = f_ok(x_bad), f_ok(x_good)
    if ob["state"] == "unresolved" or og["state"] == "unresolved":
        return None, [], "bracket endpoint UNRESOLVED"
    if ob["ok"] or not og["ok"]:
        return None, [], f"bracket is not what it claims: bad->{ob['ok']}, good->{og['ok']}"
    path = []
    for _ in range(max_iter):
        mid = 0.5 * (x_bad + x_good)
        r = f_ok(mid)
        if r["state"] == "unresolved":
            return None, path, f"UNRESOLVED at g={mid:.8g}"
        path.append(mid)
        if r["ok"]:
            x_good = mid
        else:
            x_bad = mid
        if abs(x_good - x_bad) <= tol_rel * max(abs(mid), 1e-300):
            break
    else:
        return None, path, f"did not converge in {max_iter}"
    if f_ok(x_bad)["ok"] == f_ok(x_good)["ok"]:
        return None, path, "POST-CONDITION FAILED: bracket no longer straddles a flip"
    if len(path) < 3:
        return None, path, f"POST-CONDITION FAILED: {len(path)} iteration(s)"
    return 0.5 * (x_bad + x_good), path, "ok"


def n_separated(p, q):
    """How many of the shorter path's midpoints are NOT shared with the other.

    # WHY a count of DIFFERENCES rather than of overlap: two searches that merge
    # early still separate near the flip, and it is the separation that shows
    # each one resolved its OWN predicate. Overlap alone would condemn a valid
    # measurement for a defect in a number that is not being scored.
    """
    common = {round(v, 15) for v in p} & {round(v, 15) for v in q}
    return min(len(p), len(q)) - len(common)


EDGES = (
    # label, lambda, recon bracket, P83's bracket.
    # The lambda=0.1 recon bracket was (3.5, 1.5) in revision 1 -- midpoint 2.5,
    # identical to P83's -- which merged the two searches. Moved to (3.37, 1.93),
    # midpoint 2.65. The post-condition below is what ENFORCES independence;
    # this choice only makes it likely.
    ("lambda=0", 0.0, (0.9, 0.2), (1.0, 0.1)),
    ("lambda=0.1", 0.1, (3.37, 1.93), (3.0, 2.0)),
)


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P91 rev2 -- the viability boundary through P88's implementation")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART 0 -- WHICH CLAUSE ACTUALLY BINDS AT THE BOUNDARY?")
    print("-" * 78)
    print("  The reconstruction can express only min(1-g*phibar): 'a<=0' is")
    print("  vacuous when a is the axis, and 'H non-monotone' is not surveyable")
    print("  where H -> 0. The comparison is licensed ONLY IF that clause binds.")
    p81_coarse, binds_ok = {}, True
    for label, lam, _rb, (pb, pg) in EDGES:
        x, path, note = bisect(lambda g, lm=lam: p81.viability(g, lm), pb, pg)
        if x is None:
            print(f"\n  {label}: P81 side did not bisect -- {note}")
            print("  BLOCKED-INFRASTRUCTURE, not evidence about the claim.")
            return 1
        p81_coarse[label] = x
        print(f"\n  {label}: P81 re-bisected here (not P83's published value)")
        print(f"    -> {x:.9f}  ({len(path)} iterations)")
        for side, gv in (("just below", x * (1 - 1e-3)), ("just above", x * (1 + 1e-3))):
            r = p81.viability(gv, lam)
            print(f"    {side:<12}g={gv:<12.8f}ok={str(r['ok']):<6}why={r['why'][:52]}")
            if not r["ok"] and "1-g*phibar" not in r["why"]:
                binds_ok = False
    print(f"\n    min(1-g*phibar) binds at both boundaries: {binds_ok}")
    if not binds_ok:
        print("\n  -> B-NOT-COMPARABLE. Another clause binds; no comparison reported.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- THE FLIPS, AT TOL 1e-12, WITH INDEPENDENCE MEASURED")
    print("-" * 78)
    print("  The coarse tol=1e-4 answers are shown for continuity with P83, but")
    print("  their MUTUAL closeness carries no information -- each lands within")
    print("  tol of its own flip, so the gap between them measures how two dyadic")
    print("  grids align. Revision 1 scored exactly that and had to withdraw.")
    print()
    print("  Independence is measured on the TIGHT searches, which are the ones")
    print(f"  scored: their paths must differ in at least {MIN_SEPARATED} midpoints.")
    print(f"\n    {'edge':<13}{'flip recon':<21}{'flip P81':<21}{'sep':<6}{'relative'}")
    rels, coarse_rel = {}, {}
    for label, lam, (rb, rg), (pb, pg) in EDGES:
        xr, _pr, _nr = bisect(lambda g, lm=lam: viable_recon(g, lm), rb, rg)
        if xr is not None:
            coarse_rel[label] = abs(xr / p81_coarse[label] - 1.0)
        fr, pr, nr = bisect(lambda g, lm=lam: viable_recon(g, lm), rb, rg, tol_rel=TIGHT)
        fp, pp, npt = bisect(lambda g, lm=lam: p81.viability(g, lm), pb, pg, tol_rel=TIGHT)
        if fr is None or fp is None:
            print(f"    {label:<13}not measured -- {nr if fr is None else npt}")
            rels[label] = None
            continue
        sep = n_separated(pr, pp)
        if sep < MIN_SEPARATED:
            print(f"    {label:<13}EXCLUDED -- tight paths separated only {sep} times")
            rels[label] = None
            continue
        rels[label] = abs(fr / fp - 1.0)
        print(f"    {label:<13}{fr:<21.15f}{fp:<21.15f}{sep:<6}{rels[label]:.3e}")
    print(f"\n    {'edge':<13}{'coarse recon rel vs P81 (UNINFORMATIVE, for the record)'}")
    for label, v in coarse_rel.items():
        print(f"    {label:<13}{v:.3e}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- is P81's boundary partly a property of ITS probe grid?")
    print("-" * 78)
    print("  P81 decides the clause by a min over sampled points; the")
    print("  reconstruction decides it by a terminal EVENT on the continuous")
    print("  trajectory, so no grid can change its answer. Revision 1 varied the")
    print("  RECONSTRUCTION's n_probe and got exactly 0.000e+00 -- it was varying")
    print("  something the answer does not use. The real question is whether")
    print("  P81's SAMPLED min steps over a dip, so P81's n_probe varies here.")
    print("  D1: phibar is monotone at lambda=0, oscillating at lambda!=0.")
    print(f"\n    {'edge':<13}{'P81 n_probe':<14}{'g_crit P81':<20}{'vs n=3000'}")
    moved = {}
    for label, lam, _rb, (pb, pg) in EDGES:
        base, vals = None, []
        for npb in (300, 3000, 30000):
            x, _p, note = bisect(lambda g, lm=lam, q=npb: p81.viability(g, lm, n_probe=q), pb, pg)
            if x is None:
                print(f"    {label:<13}{npb:<14}not measured -- {note}")
                continue
            if npb == 3000:
                base = x
            vals.append((npb, x))
        for npb, x in vals:
            print(f"    {label:<13}{npb:<14}{x:<20.9f}{abs(x / base - 1.0):.3e}")
        moved[label] = max((abs(x / base - 1.0) for _q, x in vals), default=float("nan"))
    print(f"\n    lambda=0   moves by {moved.get('lambda=0', float('nan')):.3e}  (expected: ~0)")
    print(f"    lambda=0.1 moves by {moved.get('lambda=0.1', float('nan')):.3e}  (expected: >0)")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    vals = [v for v in rels.values() if v is not None]
    if not vals:
        print("  -> B-NOT-COMPARABLE. No edge passed the independence")
        print("     post-condition, or none was measurable.")
    elif max(vals) < 1e-8:
        print(f"  -> B-CONFIRMED. Worst tight-tolerance flip agreement {max(vals):.3e}")
        print("     < 1e-8 on every independent edge. The two implementations")
        print("     locate the SAME boundary.")
        print()
        print("     AND THIS REFUTES MY OWN PREDICTION from FINDING_P89, that the")
        print("     boundary would reproduce ONLY to the bisection tolerance and")
        print("     NOT better. It reproduces about eight orders better. The")
        print("     tolerance is a property of the SEARCH, not of the boundary,")
        print("     and tightening the search keeps improving the agreement.")
        print()
        print("     Perelman condition 5 covers eps, f, mu and now the boundary --")
        print("     all four at the 'independently-written code' rung, no higher.")
    elif max(vals) < 1e-4:
        print(f"  -> B-MARGINAL. Worst flip agreement {max(vals):.3e}. Named, not smoothed.")
    else:
        print(f"  -> B-DISCREPANT. Worst flip agreement {max(vals):.3e}. The boundary")
        print("     LOCATION is discretization-dependent in a way eps, f and mu")
        print("     were not.")

    print("\n  SCOPE, from Part 0 and Part A:")
    print("   * only the min(1-g*phibar) clause is reconstructed.")
    print("   * only edges whose tight searches were MEASURED to separate.")
    print("\n  NOT ESTABLISHED:")
    print("   * anything above the 'independently-written code' rung.")
    print("   * that the shared EQUATIONS are right.")
    print("   * anything observational. Gate 1 holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
