"""P81 -- is there a physically viable background at all? (TZ bridge 6)

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHAT IS AND IS NOT ALREADY KNOWN.

FINDING_P63 proved the g_hat!=0 coupled background CLOSES (Bianchi-consistent).
FINDING_P64 found trajectories that EXIST numerically. Neither asked whether any
of them is physically VIABLE over a cosmological span, and those are different
questions: a system can be perfectly consistent and still drive itself into
rho_phys<0 or through the 1-g*phibar=0 surface within a decade.

The one viability datum in the whole campaign is a SINGLE POINT: FINDING_P77's
side-check I4 measured min(1-g*phibar) = 0.87 at (g_hat, lambda) = (1, 1) over
eight decades. One point is not a region, and the campaign has been quoting it
as if the corner it sits in were known.

THE PREDICATE, pre-registered in TZ_P79_P82 before any scan:

    over >= 8 decades in t:   a > 0
                              rho_phys > 0
                              min(1 - g_hat*phibar) > 0.1
                              H monotone (non-increasing)

PRE-REGISTERED OUTCOMES:
  V-REGION  a CONNECTED region of (g_hat, lambda) survives -> the completion has
            a viable corner, and the boundary of that corner is a NEW CONSTRAINT
            on the completion, which is the useful output.
  V-POINT   only isolated points survive -> the completion is fine-tuned, and
            that has to be said plainly rather than buried.
  V-NONE    nothing survives -> the completion is not viable and the arc ends.

WHAT THIS CANNOT DO, WRITTEN BEFORE THE NUMBERS.
  * A grid scan can only find what the grid resolves. "Connected" here means
    connected AT THIS RESOLUTION -- it cannot exclude holes finer than the step,
    and the file must not claim otherwise.
  * lambda and g_hat are internal-unit parameters. Nothing here maps to an
    observed cosmology; NO_BRIDGE_FITTING remains in force.
  * Viability is necessary, never sufficient. A viable corner is not evidence
    that the completion is right -- only that it is not self-destructing.

CONTROLS, chosen to be able to FAIL:
  C1  the known point (1,1) must reproduce FINDING_P77's min(1-g*phibar)=0.87.
      Measured against P77's own machinery? No -- against the number P77
      published, because P77's I4 is a side-check, not an importable function.
      Which means C1 is exactly the kind of transcription P78's A3 failure was
      about, so it is quoted to the precision P77 actually reported (2 d.p.)
      and NOT to more.
  C2  g_hat = 0 must be viable for EVERY lambda: with no coupling, 1-g*phibar
      is identically 1 and the background is the uncoupled one. If any g_hat=0
      point fails, the gate itself is broken, not the physics.
  C3  a deliberately absurd point (large g_hat) must FAIL. A gate that passes
      everything is not a gate -- the same lesson as P76's hardcoded column.
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location(
    "p76_ref", os.path.join(_HERE, "P76_growth_observable.py")
)
p76 = importlib.util.module_from_spec(_sp)
sys.modules["p76_ref"] = p76
_sp.loader.exec_module(p76)

G_N, C_MATTER = p76.G_N, p76.C_MATTER
A3_INIT, PHIDOT = p76.A3_INIT, p76.PHIDOT_INIT

T0, T_END = 1.0, 1e8  # eight decades, as the predicate requires
FLOOR = 0.1  # min(1 - g*phibar) must stay above this


def background_rhs(g_hat, lam):
    """The coupled background only -- a, phibar, phibar_dot. No perturbations."""

    def rhs(_t, y):
        a_, pb, pd = y
        rho_A = C_MATTER / a_**3
        rho_phys = rho_A * (1.0 - g_hat * pb)
        V = lam * pb**4 / 4.0
        arg = (8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V)
        H = np.sqrt(arg) if arg > 0 else 0.0
        return [a_ * H, pd, g_hat * rho_A - 3.0 * H * pd - lam * pb**3]

    return rhs


def viability(g_hat, lam, n_probe=3000):
    """Return the four predicate quantities, or a NAMED non-viable / unresolved state.

    THREE outcomes, not two -- this is the Substrate Gate rule applied to a scan.
    A point where the integrator gives up has NOT been shown non-viable; it has
    not been measured at all. Folding those two into one 'not viable' bucket is
    exactly the error the gate exists to prevent ("the test could not run" is not
    "the predicate is false"), so integrator failure returns state='unresolved'
    and is EXCLUDED from the viable set and from the failure set alike.

    Every quantity is measured on the SAME trajectory over the SAME span, so a
    point that genuinely fails does so for a named reason.
    """
    a0 = A3_INIT ** (1.0 / 3.0)
    with np.errstate(all="ignore"):  # overflow IS the signal here, not a bug
        try:
            s = solve_ivp(
                background_rhs(g_hat, lam),
                (T0, T_END),
                [a0, 0.0, PHIDOT],
                rtol=1e-10,
                atol=1e-22,
                dense_output=True,
            )
        except Exception as exc:  # noqa: BLE001 - the reason is the result here
            return {
                "ok": False,
                "state": "unresolved",
                "why": f"integrator raised {type(exc).__name__}",
            }
        if not s.success:
            return {"ok": False, "state": "unresolved", "why": "integrator gave up"}
        if s.t[-1] < T_END * 0.999:
            return {
                "ok": False,
                "state": "unresolved",
                "why": f"integrator stopped at t={s.t[-1]:.3g}",
            }

        tt = np.exp(np.linspace(np.log(T0), np.log(T_END), n_probe))
        a_, pb, pd = s.sol(tt)
        rho_A = C_MATTER / a_**3
        M = 1.0 - g_hat * pb
        rho_phys = rho_A * M
        V = lam * pb**4 / 4.0
        arg = (8.0 * np.pi * G_N / 3.0) * (rho_phys + pd**2 / 2.0 + V)
        H = np.sqrt(np.maximum(arg, 0.0))

    # a NaN anywhere means the trajectory left the representable range, which is
    # again "not measured", not "measured and failed"
    if not (np.all(np.isfinite(a_)) and np.all(np.isfinite(pb)) and np.all(np.isfinite(pd))):
        return {"ok": False, "state": "unresolved", "why": "trajectory overflowed to inf/nan"}

    # H monotone: allow a tolerance, since a probe grid can manufacture a
    # spurious rise of order the local truncation error.
    dH = np.diff(H)
    worst_rise = float(np.max(dH)) if len(dH) else 0.0
    scale = float(np.max(H)) if len(H) else 1.0
    mono = worst_rise <= 1e-9 * scale

    out = {
        "state": "measured",
        "min_a": float(np.min(a_)),
        "min_rho_phys": float(np.min(rho_phys)),
        "min_M": float(np.min(M)),
        "H_monotone": bool(mono),
        "worst_H_rise_rel": worst_rise / scale if scale else 0.0,
    }
    fails = []
    if out["min_a"] <= 0:
        fails.append("a<=0")
    if out["min_rho_phys"] <= 0:
        fails.append("rho_phys<=0")
    if out["min_M"] <= FLOOR:
        fails.append(f"min(1-g*phibar)={out['min_M']:.3g}<={FLOOR}")
    if not mono:
        fails.append("H not monotone")
    out["ok"] = not fails
    out["why"] = "; ".join(fails) if fails else "viable"
    return out


def main() -> int:
    print("=" * 78)
    print("P81 -- is there a physically viable background at all?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)
    print(f"\n  span: t = {T0:g} .. {T_END:g}  ({np.log10(T_END / T0):.0f} decades)")
    print(f"  predicate: a>0, rho_phys>0, min(1-g*phibar)>{FLOOR}, H monotone")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- CONTROLS (run before the scan, so a broken gate is caught)")
    print("-" * 78)

    print("\n  C1 -- the known point (1,1) must reproduce FINDING_P77's I4 value.")
    print("  P77 reported min(1-g*phibar) = 0.87 over eight decades. That figure")
    print("  is a side-check in P77's prose, not an importable function, so this")
    print("  IS a transcription comparison -- exactly what P78's A3 failure was")
    print("  about. It is therefore checked to the 2 d.p. P77 actually reported,")
    print("  and a tighter agreement is NOT claimed.")
    r11 = viability(1.0, 1.0)
    print(f"\n    (g,lam)=(1,1) -> min(1-g*phibar) = {r11.get('min_M', float('nan')):.4f}")
    print("    P77 I4 reported                    = 0.87")
    c1 = "min_M" in r11 and abs(round(r11["min_M"], 2) - 0.87) < 1e-9
    print(f"    agrees at 2 d.p.: {c1}")
    if not c1:
        print("    *** C1 FAILED -- this file does not reproduce the one known point.")
        print("    Nothing below may be read as being about the same system.")
        return 1

    print("\n  C2 -- g_hat = 0 must be viable at every lambda. With no coupling")
    print("  1-g*phibar is identically 1, so a failure here is a broken GATE,")
    print("  not physics.")
    c2 = True
    for lam in (0.0, 0.1, 1.0, 10.0):
        r = viability(0.0, lam)
        print(
            f"    lam={lam:<7g} ok={str(r['ok']):<6} min_M={r.get('min_M', float('nan')):.4f}"
            f"  {r['why']}"
        )
        c2 = c2 and r["ok"]
    if not c2:
        print("    *** C2 FAILED -- the gate rejects the uncoupled background.")
        return 1
    print("    PASSES.")

    print("\n  C3 -- an absurd point must FAIL. A gate that passes everything is")
    print("  not a gate (the lesson of P76's hardcoded column).")
    r_abs = viability(50.0, 1.0)
    print(f"    (g,lam)=(50,1) -> ok={r_abs['ok']}   why: {r_abs['why']}")
    if r_abs["ok"]:
        print("    *** C3 FAILED -- the gate accepts an absurd coupling.")
        return 1
    print("    PASSES -- the gate can say no.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- the scan")
    print("-" * 78)
    G_GRID = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]
    L_GRID = [0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 10.0]
    print(f"  g_hat  : {G_GRID}")
    print(f"  lambda : {L_GRID}")
    print(f"  {len(G_GRID)}x{len(L_GRID)} = {len(G_GRID) * len(L_GRID)} points\n")

    print("  legend:  OK = viable   .  = measured and NOT viable   ?  = UNRESOLVED")
    print("  '?' means the integrator could not carry the point across the span.")
    print("  Those are NOT counted as failures -- see the Substrate Gate note in")
    print("  viability(). 'Could not be measured' is a third outcome.\n")
    grid = {}
    header = "    g\\lam  " + "".join(f"{lam:>9g}" for lam in L_GRID)
    print(header)
    for g in G_GRID:
        row = ""
        for lam in L_GRID:
            r = viability(g, lam)
            grid[(g, lam)] = r
            mark = "OK" if r["ok"] else ("?" if r["state"] == "unresolved" else ".")
            row += f"{mark:>9}"
        print(f"    {g:<7g}{row}")

    n_ok = sum(1 for r in grid.values() if r["ok"])
    n_unres = sum(1 for r in grid.values() if r["state"] == "unresolved")
    n_fail = len(grid) - n_ok - n_unres
    print(f"\n    viable      : {n_ok} of {len(grid)}")
    print(f"    non-viable  : {n_fail}   (measured, predicate false)")
    print(f"    UNRESOLVED  : {n_unres}   (not measured -- never evidence either way)")

    print("\n  Only the points that are NOT viable, with the named reason.")
    print(f"\n    {'point':<14}{'state':<12}{'min(1-g*phibar)':<22}{'reason'}")
    for g in G_GRID:
        for lam in L_GRID:
            r = grid[(g, lam)]
            if r["ok"]:
                continue
            mm = r.get("min_M")
            mstr = f"{mm:.4g}" if mm is not None else "not measured"
            print(f"    ({g:g},{lam:g})".ljust(14) + f"{r['state']:<12}{mstr:<22}{r['why']}")

    print("\n  And the viable interior, for the record:")
    print(f"\n    {'g_hat':<9}" + "".join(f"{lam:>10g}" for lam in L_GRID))
    for g in G_GRID:
        row = ""
        for lam in L_GRID:
            r = grid[(g, lam)]
            row += f"{r['min_M']:>10.4f}" if r["ok"] else f"{'-':>10}"
        print(f"    {g:<9g}{row}")
    print("    (cells are min(1-g*phibar); '-' = not viable or unresolved)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- is the viable set CONNECTED at this resolution?")
    print("-" * 78)
    print("  4-neighbour flood fill on the grid. Read the caveat first: this can")
    print("  only report connectivity AT THE GRID STEP. It cannot exclude holes")
    print("  finer than the spacing, and no such claim is made.")

    ok_pts = {p for p, r in grid.items() if r["ok"]}
    gi = {g: i for i, g in enumerate(G_GRID)}
    li = {lam: i for i, lam in enumerate(L_GRID)}
    idx = {(gi[g], li[lam]) for (g, lam) in ok_pts}
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
    comps.sort(key=len, reverse=True)
    print(f"\n    connected components: {len(comps)}")
    for n, comp in enumerate(comps):
        pts = sorted((G_GRID[i], L_GRID[j]) for i, j in comp)
        shown = ", ".join(f"({g:g},{lam:g})" for g, lam in pts[:8])
        more = f" ... +{len(pts) - 8} more" if len(pts) > 8 else ""
        print(f"      #{n + 1}: {len(comp):>3} points   {shown}{more}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- is the BOUNDARY where the coarse grid says it is?")
    print("-" * 78)
    print("  Part C's caveat is that a flood fill sees nothing finer than the")
    print("  step. This does not remove that limit, but it does test the two")
    print("  places the coarse grid puts a boundary, by bisecting across them.")
    print("  If the refined points march monotonically toward the failure, the")
    print("  boundary is real and located; if they scatter, the coarse grid was")
    print("  reading noise and Part C's verdict must be read as provisional.")

    print("\n  D1 -- the lambda -> 0 edge at g_hat = 0.75, where (0.75, 0) fails")
    print("  at min(1-g*phibar) = 0.0285 while (0.75, 0.01) passes at 0.8643.")
    print(f"\n    {'lambda':<12}{'state':<12}{'min(1-g*phibar)':<20}{'viable'}")
    prev, mono_d1 = None, True
    for lam in (0.0, 1e-4, 3e-4, 1e-3, 3e-3, 0.01):
        r = viability(0.75, lam)
        mm = r.get("min_M")
        print(
            f"    {lam:<12g}{r['state']:<12}"
            + (f"{mm:<20.4f}" if mm is not None else f"{'not measured':<20}")
            + str(r["ok"])
        )
        if mm is not None and prev is not None and mm < prev - 1e-12:
            mono_d1 = False
        if mm is not None:
            prev = mm
    print(f"\n    monotone in lambda: {mono_d1}")

    print("\n  D2 -- the g_hat edge at lambda = 0.1, where (2, 0.1) passes at")
    print("  0.4850 and (3, 0.1) fails at -0.0551.")
    print(f"\n    {'g_hat':<12}{'state':<12}{'min(1-g*phibar)':<20}{'viable'}")
    prev, mono_d2 = None, True
    for g in (2.0, 2.25, 2.5, 2.75, 3.0):
        r = viability(g, 0.1)
        mm = r.get("min_M")
        print(
            f"    {g:<12g}{r['state']:<12}"
            + (f"{mm:<20.4f}" if mm is not None else f"{'not measured':<20}")
            + str(r["ok"])
        )
        if mm is not None and prev is not None and mm > prev + 1e-12:
            mono_d2 = False
        if mm is not None:
            prev = mm
    print(f"\n    monotone in g_hat: {mono_d2}")
    print("\n    READ: monotone on BOTH edges means the boundary is a genuine")
    print("    surface the coarse grid merely sampled, not an artifact of where")
    print("    the grid points happened to land. Non-monotone on either means the")
    print("    V-REGION verdict is provisional at this resolution.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    if not comps:
        print("  -> V-NONE. No point in the scanned box is viable over 8 decades.")
        print("     The completion is not viable and the arc ends here.")
    elif len(comps[0]) == 1:
        print("  -> V-POINT. Only isolated points survive; the completion is")
        print("     FINE-TUNED, and that is the finding, not a footnote.")
    else:
        print(f"  -> V-REGION. A connected region of {len(comps[0])} grid points survives.")
        print("     The completion has a viable corner. Its BOUNDARY is the new")
        print("     constraint, and that boundary -- not the interior -- is the")
        print("     part worth carrying forward.")
        if len(comps) > 1:
            print(f"     NOTE {len(comps)} components, not one: the viable set is not")
            print("     simply connected at this resolution.")
        if mono_d1 and mono_d2:
            print("     Part D found the boundary MONOTONE on both edges tested, so")
            print("     it is a surface the grid sampled rather than a grid artifact.")
        else:
            print("     *** PROVISIONAL: Part D found the boundary NON-monotone on")
            print("     an edge, so the coarse grid may be reading noise there.")

    print("\n  NOT ESTABLISHED:")
    print("   * connectivity below the grid step. A flood fill on a coarse grid")
    print("     cannot see finer holes, and none is claimed.")
    print("   * that viability means correctness. It is NECESSARY, never")
    print("     sufficient -- a background that does not destroy itself is not")
    print("     thereby right.")
    print("   * anything observational. Internal units, NO_BRIDGE_FITTING in force.")
    print("   * anything about MULTING itself (Gate 1): the completion is OURS,")
    print("     and a verdict on our reconstruction does not transfer.")
    print("   * Perelman condition 5 (external reconstruction) -- still not met.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
