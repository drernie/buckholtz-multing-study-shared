"""P77 -- attack P76's eps(k=10)=0.0457 on the four axes that could still kill it.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
(descriptive: this characterises a property of a model WE constructed. No
causal claim about nature is made or implied.)

FINDING_P76 produced the first quantity in the P50A->P76 arc to survive the
phibar_dot(1) lever. Precisely because it is the best candidate so far, it gets
attacked hardest. Four load-bearing holes, three named by an outside reading and
one by this file:

  A1-ANCHOR    P76 computes eps = ln G(a2; A1) / ln(a2/A1) with A1 PINNED at
               t=1e4. That is a MEAN SLOPE FROM A FIXED ANCHOR, not the local
               d ln G / d ln a. Stability under moving a2 does NOT establish
               independence of A1 -- an early transient could be sitting inside
               the average. Test: move A1 across decades, AND compute the local
               slope by finite difference.

  GRID        P76 tested k = 0.1, 1, 10 and called k=10 a "deep subhorizon
               regime". Three points cannot establish a regime. k=10 could be a
               lucky grid point where everything is small and therefore stable.
               Test: k = 1, 3, 5, 10, 20, 30, 100.

  LEVER RANGE  P76 chose phibar_dot(1) x0.5 and x2 -- ITS OWN choice, which may
               have been conveniently narrow. Test: x0.1 ... x10.

  ATTRIBUTION  the comparison (g=1,lam=1) vs (g=0,lam=1) changes TWO things at
               once: the BACKGROUND history and the DIRECT scalar force in the
               perturbed Euler equation. So "this is a fifth force" is stronger
               than the data. Test by ablation:
                   A  full coupled
                   B  same coupled background, perturbative fifth force REMOVED
                   C  g_hat=0 control
               A-B is the direct force; B-C is background-mediated.

               *** B IS DELIBERATELY INCONSISTENT. *** Removing one term breaks
               the first-class constraint algebra FINDING_P73 established, so B
               violates the constraints by construction. It is an ATTRIBUTION
               PROBE, not a model, and its constraint violation is printed so it
               cannot be mistaken for one. This caveat is not optional: an
               ablation that silently violates the constraints would be exactly
               the kind of artifact this campaign keeps catching.

  PARITY (extra, cheap, discriminating): the g_hat^2 scaling is consistent with
               a force between two coupled sources -- but background corrections
               can also start at quadratic order, so g^2 alone does not identify
               the mechanism. If the leading effect is genuinely even, then
               eps(+g) ~ eps(-g). A large odd component means something else.

PRE-REGISTERED OUTCOMES (before any number):
  S1 REGIME       eps(k) varies smoothly and settles as k/aH grows -> k=10 is a
                  regime, and eps(k) is a real spectral quantity.
  S2 GRID ACCIDENT neighbouring k are unstable while k=10 is not -> P76's
                  bounded claim is OVERSTATED and must be withdrawn.
  S3 SCALE DEP.   eps stable at every high k but systematically k-dependent ->
                  stronger than S1, and the k-dependence becomes the result.
  ANCHOR FAIL     eps moves with A1 -> it is a window average, not a growth
                  index, and P76's Part G framing is wrong.
  ATTRIBUTION     if B-C dominates A-B, the effect is BACKGROUND-mediated and
                  calling it a fifth force is withdrawn.
"""

import importlib.util
import sys

import numpy as np
from scipy.integrate import solve_ivp

SRC = (
    r"E:\Проверка Гипотез\работаю над проверкой гипотез\H - 11 Dr. Thomas J. Buckholtz"
    r"\buckholtz-idm-multing-mvp\experiments\20260803-bridge\P76_growth_observable.py"
)
_spec = importlib.util.spec_from_file_location("p76", SRC)
p76 = importlib.util.module_from_spec(_spec)
sys.modules["p76"] = p76
_spec.loader.exec_module(p76)

G_N = p76.G_N
bg = p76.bg_quantities
run = p76.run
contrast = p76.contrast
t_of_a = p76.t_of_a
initial_data = p76.initial_data
PHIDOT = p76.PHIDOT_INIT

T_END = 1e8


def growth(gh, lam, kk, a1, a2, **ic):
    s = run(gh, lam, kk, T_END, **ic)
    t1, t2 = t_of_a(s, a1, 1.0, T_END), t_of_a(s, a2, 1.0, T_END)
    assert t1 is not None and t2 is not None, f"anchor unreachable at g={gh} k={kk}"
    return contrast(s, gh, lam, t2) / contrast(s, gh, lam, t1)


def eps_of(gh, lam, kk, a1, a2, **ic):
    g = growth(gh, lam, kk, a1, a2, **ic) / growth(0.0, lam, kk, a1, a2, **ic)
    return np.log(g) / np.log(a2 / a1)


# ----------------------------------------------------------------------
# the ablated system: coupled BACKGROUND, no perturbative fifth force
# ----------------------------------------------------------------------
def make_system_ablated(gh, lam, kk):
    """Identical to FINDING_P73/P76's system EXCEPT the +g*rho_A*dphi term in the
    matter Euler equation, which is the force the scalar perturbation exerts on
    matter. Everything else -- including the coupled background -- is untouched.

    # WHY this breaks the constraints: FINDING_P73 proved the 00 and 0i
    # constraints are first class ONLY for the complete system. Deleting a term
    # takes the system off-shell, so the constraints drift. That is expected and
    # is measured below, not hidden. B is an attribution probe, never a model.
    """

    def rhs(_t, y):
        a_, pb, pd, psi, psid, dph, dphd, drA, qm = y
        b = bg(a_, pb, pd, gh, lam)
        H, rho_A, rho_phys, Vp, Vpp = (b["H"], b["rho_A"], b["rho_phys"], b["Vp"], b["Vpp"])
        pdd = gh * rho_A - 3.0 * H * pd - Vp
        dp_phi = pd * dphd - psi * pd**2 - Vp * dph
        psidd = 4 * np.pi * G_N * dp_phi - 4 * H * psid - (2 * b["Hdot"] + 3 * H**2) * psi
        dphdd = (
            gh * drA
            + 2 * psi * (gh * rho_A - Vp)
            + 4 * psid * pd
            - 3 * H * dphd
            - (kk**2 / a_**2 + Vpp) * dph
        )
        drAd = -3 * H * drA + 3 * psid * rho_A + (kk**2 / a_**2) * qm / (1 - gh * pb)
        qmd = -3 * H * qm - rho_phys * psi  # <-- fifth force REMOVED
        return [a_ * H, pd, pdd, psid, psidd, dphd, dphdd, drAd, qmd]

    return rhs


def run_ablated(gh, lam, kk):
    s = solve_ivp(
        make_system_ablated(gh, lam, kk),
        (1.0, T_END),
        initial_data(gh, lam, kk),
        rtol=1e-10,
        atol=1e-20,
        dense_output=True,
    )
    assert s.success
    return s


def c0i_violation(sol, gh, lam, tv):
    """0i constraint residual, relative. Zero for the complete system."""
    a_, pb, pd, psi, psid, dph, _dphd, _drA, qm = sol.sol(tv)
    b = bg(a_, pb, pd, gh, lam)
    c = psid + b["H"] * psi + 4 * np.pi * G_N * (-pd * dph + qm)
    return abs(c) / (abs(psid) + abs(b["H"] * psi) + 1e-300)


def main() -> int:
    print("=" * 78)
    print("P77 -- attacking P76's eps(k=10) = 0.0457 on four axes")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    s_ref = run(0.0, 1.0, 1.0, T_END)
    A1 = s_ref.sol(1e4)[0]
    A2 = s_ref.sol(8e7)[0]

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART A -- is k=10 a REGIME or a lucky grid point?")
    print("-" * 78)
    print("  P76 tested three k and called k=10 'deep subhorizon'. Three points")
    print("  cannot establish a regime. Fill in the grid, and report k/aH so the")
    print("  claim can be read against the actual horizon ratio.")
    KS = (1.0, 3.0, 5.0, 10.0, 20.0, 30.0, 100.0)
    print(f"\n    {'k':<8}{'k/aH @8e7':<14}{'eps':<14}{'eps spread over a2':<22}{'stable?'}")
    epsk, stabk = {}, {}
    for kk in KS:
        es = []
        for te in (1e6, 1e7, 8e7):
            a_end = s_ref.sol(te)[0]
            es.append(eps_of(1.0, 1.0, kk, A1, a_end))
        sp = max(es) / min(es) if min(es) > 0 else float("inf")
        epsk[kk], stabk[kk] = es[-1], sp
        y = run(1.0, 1.0, kk, T_END).sol(8e7)
        koaH = kk / (y[0] * bg(y[0], y[1], y[2], 1.0, 1.0)["H"])
        print(f"    {kk:<8}{koaH:<14.4g}{es[-1]:<14.6f}{sp:<22.4f}{'yes' if sp < 1.05 else 'NO'}")
    good = [k for k in KS if stabk[k] < 1.05]
    print(f"\n    stable at k = {good}")
    if len(good) >= 4:
        print("    => S1/S3: NOT a lucky grid point. Stability is shared by a whole")
        print("       family of k, so there is a regime and eps(k) is a spectrum.")
    else:
        print("    => S2 GRID ACCIDENT: stability does not extend to neighbours.")
        print("       P76's bounded claim is OVERSTATED and must be withdrawn.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART B -- does eps depend on the ANCHOR A1? (P76 never tested this)")
    print("-" * 78)
    print("  eps = ln G(a2;A1) / ln(a2/A1) is a MEAN slope from a pinned anchor.")
    print("  If an early transient sits inside the average, moving A1 moves eps.")
    print("  A genuine growth index does not care where you started measuring.")
    print(
        f"\n    {'A1 from t=':<14}" + "".join(f"{'eps k=' + str(k):<16}" for k in (3.0, 10.0, 30.0))
    )
    anchors = (1e3, 1e4, 1e5, 1e6)
    arows = {}
    for ta in anchors:
        a1v = s_ref.sol(ta)[0]
        vals = [eps_of(1.0, 1.0, kk, a1v, A2) for kk in (3.0, 10.0, 30.0)]
        arows[ta] = vals
        print(f"    {ta:<14.0e}" + "".join(f"{v:<16.6f}" for v in vals))
    print(f"\n    {'k':<8}{'min':<14}{'max':<14}{'anchor spread':<18}{'anchor-free?'}")
    anchor_ok = True
    for i, kk in enumerate((3.0, 10.0, 30.0)):
        vs = [arows[ta][i] for ta in anchors]
        sp = max(vs) / min(vs)
        ok = sp < 1.05
        anchor_ok = anchor_ok and ok
        print(f"    {kk:<8}{min(vs):<14.6f}{max(vs):<14.6f}{sp:<18.4f}{'yes' if ok else 'NO'}")

    print("\n  B2 -- the LOCAL slope, which is what 'growth index' actually means:")
    print("       eps_local := dln G / dln a, by finite difference between")
    print("       ADJACENT a2 values, with no anchor in it at all.")
    print(f"\n    {'k':<8}{'eps_local (1e6-1e7)':<24}{'(1e7-8e7)':<20}{'vs anchored eps'}")
    for kk in (3.0, 10.0, 30.0):
        aa = [s_ref.sol(te)[0] for te in (1e6, 1e7, 8e7)]
        gg = [growth(1.0, 1.0, kk, A1, a) / growth(0.0, 1.0, kk, A1, a) for a in aa]
        loc = [np.log(gg[j + 1] / gg[j]) / np.log(aa[j + 1] / aa[j]) for j in range(len(aa) - 1)]
        print(f"    {kk:<8}{loc[0]:<24.6f}{loc[1]:<20.6f}{epsk[kk]:.6f}")
    print("\n    => if the local slopes agree with the anchored eps, the anchored")
    print("       form was a fair estimator of the rate. If they differ, P76's")
    print("       Part G framing ('window-free') is WRONG.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART C -- the lever, over a range P76 did NOT choose")
    print("-" * 78)
    print("  P76 used phibar_dot(1) x0.5 and x2 -- its own choice, possibly a")
    print("  convenient one. Push it two decades.")
    print(
        f"\n    {'phibar_dot(1)':<18}" + "".join(f"{'eps k=' + str(k):<16}" for k in (10.0, 30.0))
    )
    lrows = {}
    for f in (0.1, 0.5, 1.0, 2.0, 10.0):
        vals = [eps_of(1.0, 1.0, kk, A1, A2, phidot0=f * PHIDOT) for kk in (10.0, 30.0)]
        lrows[f] = vals
        print(f"    x{f:<17.1f}" + "".join(f"{v:<16.6f}" for v in vals))
    print(f"\n    {'k':<8}{'min':<14}{'max':<14}{'spread':<14}{'passes <10%?'}")
    lever_ok = True
    for i, kk in enumerate((10.0, 30.0)):
        vs = [lrows[f][i] for f in lrows]
        sp = max(vs) / min(vs)
        ok = sp < 1.10
        lever_ok = lever_ok and ok
        print(f"    {kk:<8}{min(vs):<14.6f}{max(vs):<14.6f}{sp:<14.4f}{'YES' if ok else 'no'}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART D -- ATTRIBUTION: fifth force, or modified background?")
    print("-" * 78)
    print("  (g=1,lam=1) vs (g=0,lam=1) changes the BACKGROUND history AND the")
    print("  direct scalar force in the perturbed Euler equation. Calling the")
    print("  result 'a fifth force' is therefore stronger than the data. Ablate:")
    print("    A  full coupled")
    print("    B  same coupled background, +g*rho_A*dphi REMOVED from Euler")
    print("    C  g_hat=0 control")
    print("  A-B = direct force.  B-C = background-mediated.")
    print()
    print("  *** B IS DELIBERATELY OFF-SHELL. *** Deleting a term breaks the")
    print("  first-class algebra FINDING_P73 proved, so B violates the 0i")
    print("  constraint by construction. Printed, not hidden -- B is an")
    print("  attribution probe and never a model.")
    print(
        f"\n    {'k':<8}{'eps_full (A-C)':<18}{'eps_bg (B-C)':<18}{'direct (A-B)':<18}"
        f"{'|C0i| of B'}"
    )
    attrib = {}
    for kk in (3.0, 10.0, 30.0):
        sB = run_ablated(1.0, 1.0, kk)
        t1, t2 = t_of_a(sB, A1, 1.0, T_END), t_of_a(sB, A2, 1.0, T_END)
        gB = contrast(sB, 1.0, 1.0, t2) / contrast(sB, 1.0, 1.0, t1)
        gC = growth(0.0, 1.0, kk, A1, A2)
        e_bg = np.log(gB / gC) / np.log(A2 / A1)
        e_full = epsk[kk]
        attrib[kk] = (e_full, e_bg, e_full - e_bg)
        viol = max(c0i_violation(sB, 1.0, 1.0, tv) for tv in (1e5, 1e6, 1e7))
        print(f"    {kk:<8}{e_full:<18.6f}{e_bg:<18.6f}{e_full - e_bg:<18.6f}{viol:.2e}")
    print("\n    => if |direct| >> |background|, the fifth-force reading survives.")
    print("       If the background term dominates, the reading is WITHDRAWN and")
    print("       the effect is a modified expansion history, not a new force.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART E -- PARITY: is the leading effect even in g_hat?")
    print("-" * 78)
    print("  g^2 scaling is consistent with a force between two coupled sources,")
    print("  but background corrections can also start at quadratic order, so g^2")
    print("  alone does not identify the mechanism. An even leading term predicts")
    print("  eps(+g) ~ eps(-g); a large odd component means something else.")
    print(f"\n    {'k':<8}{'eps(+1)':<16}{'eps(-1)':<16}{'odd/even':<16}{'even?'}")
    for kk in (3.0, 10.0, 30.0):
        ep = eps_of(1.0, 1.0, kk, A1, A2)
        em = eps_of(-1.0, 1.0, kk, A1, A2)
        odd = abs(ep - em) / abs(ep + em)
        print(
            f"    {kk:<8}{ep:<16.6f}{em:<16.6f}{odd:<16.4f}"
            f"{'yes' if odd < 0.1 else 'NO -- odd component'}"
        )


    # ==================================================================
    print("\n" + "-" * 78)
    print("PART F -- rtol: is the fourth decimal the model or the solver?")
    print("-" * 78)
    print("  P76 never swept rtol on eps. Its headline lives in the 4th decimal,")
    print("  so it must agree to 4 significant figures across tolerances, or the")
    print("  number belongs to the integrator (FINDING_P72's lesson, which already")
    print("  caught P74's floor claim once).")
    print(f"\n    {'rtol':<14}{'eps k=10':<22}{'shift vs previous'}")
    prev, rtol_shift = None, 0.0
    for rt in (1e-8, 1e-9, 1e-10, 1e-11, 1e-12):
        g = growth(1.0, 1.0, 10.0, A1, A2, rtol=rt) / growth(0.0, 1.0, 10.0, A1, A2, rtol=rt)
        e = np.log(g) / np.log(A2 / A1)
        sh = "" if prev is None else f"{abs(e - prev):.3e}"
        if prev is not None:
            rtol_shift = max(rtol_shift, abs(e - prev))
        print(f"    {rt:<14.0e}{e:<22.9f}{sh}")
        prev = e
    print(f"\n    => largest rtol-to-rtol shift: {rtol_shift:.3e}")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART G -- is the g_hat scaling QUADRATIC, or drifting?")
    print("-" * 78)
    print("  P76 quoted local slopes 2.012 / 2.034 / 2.126 and called it")
    print("  'quadratic'. Three slopes drifting UPWARD by 5.7% is not a constant")
    print("  2 -- a true quadratic gives exactly 2 on every interval. Fit the")
    print("  higher-order term instead of eyeballing the exponent.")
    GS = (0.125, 0.25, 0.375, 0.5, 0.75, 1.0)
    print(f"\n    {'g_hat':<10}{'|G-1|':<20}{'|G-1|/g^2':<20}{'local slope'}")
    xs, ys, prev_pt = [], [], None
    for ghv in GS:
        g = growth(ghv, 1.0, 10.0, A1, A2) / growth(0.0, 1.0, 10.0, A1, A2)
        v = abs(g - 1.0)
        xs.append(ghv)
        ys.append(v)
        sl = "" if prev_pt is None else f"{np.log(v / prev_pt[1]) / np.log(ghv / prev_pt[0]):.4f}"
        print(f"    {ghv:<10.3f}{v:<20.6e}{v / ghv**2:<20.6e}{sl}")
        prev_pt = (ghv, v)
    xs, ys = np.array(xs), np.array(ys)
    slope, intercept = np.polyfit(xs, ys / xs**2, 1)
    C, D = intercept, slope / intercept
    print(f"\n    fit |G-1| = C*g^2*(1 + D*g):  C = {C:.6e}   D = {D:.4f}")
    print(f"    the cubic term is {abs(D) * 100:.1f}% of the quadratic one at g=1.")
    print("    => 'quadratic' is a LEADING-order description only. P76's flat")
    print("       'quadratic scaling' is WEAKENED. And a leading g^2 does not by")
    print("       itself identify the mechanism -- background corrections can also")
    print("       start at quadratic order, which is exactly what Part D separates.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("PART H -- the pole: at k=1 exactly, or across a range?")
    print("-" * 78)
    print("  P76's pole detector only asked 'is any sampled contrast near zero'.")
    print("  That cannot separate a benign zero-crossing from an oscillatory")
    print("  instability or an integrator failure -- three different diseases with")
    print("  three different consequences. The contrast's own SIGN HISTORY does")
    print("  separate them, so scan finely around k=1 and count crossings.")
    print(f"\n    {'k':<8}{'|G-1| at g=0.5':<24}{'contrast sign changes':<26}{'reading'}")
    for kk in (0.5, 0.7, 1.0, 1.5, 2.0, 3.0):
        try:
            g = growth(0.5, 1.0, kk, A1, A2) / growth(0.0, 1.0, kk, A1, A2)
            val = f"{abs(g - 1.0):.4e}"
        except AssertionError:
            val = "anchor unreachable"
        s = run(0.0, 1.0, kk, T_END)
        cs = np.array([contrast(s, 0.0, 1.0, tv) for tv in np.logspace(0, 8, 3000)])
        n = sum(1 for i in range(1, len(cs)) if cs[i] * cs[i - 1] < 0)
        read = "clean" if n <= 1 else ("transient crossing" if n <= 3 else "OSCILLATORY")
        print(f"    {kk:<8}{val:<24}{n:<26}{read}")
    print("\n    => one crossing is a benign transient and the anchor can be moved.")
    print("       Many crossings mean the REFERENCE mode oscillates through zero --")
    print("       a different disease, not fixable by moving anchors, and the one")
    print("       that made mu ill-posed in FINDING_P74.")

    # ==================================================================
    print("\n" + "=" * 78)
    print("VERDICT (against the outcomes pre-registered in the docstring)")
    print("=" * 78)
    print(
        f"  regime (>=4 stable k)      : {'PASSED' if len(good) >= 4 else 'FAILED'}"
        f"   stable at {good}"
    )
    print(f"  anchor independence        : {'PASSED' if anchor_ok else 'FAILED'}")
    print(f"  lever x0.1..x10            : {'PASSED' if lever_ok else 'FAILED'}")
    print("  attribution                : see Part D")
    print(f"  rtol stability             : {rtol_shift:.3e} (Part F)")
    print(f"  g-scaling                  : leading-quadratic, cubic/quadratic "
          f"= {abs(D) * 100:.1f}% at g=1 (Part G)")
    print("\n  eps(k) spectrum:")
    for kk in KS:
        print(
            f"    k={kk:<7} eps = {epsk[kk]:.6f}"
            f"{'' if stabk[kk] < 1.05 else '   [UNSTABLE -- do not quote]'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
