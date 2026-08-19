"""P64 -- numeric scout of the g_hat!=0 coupled background system derived
symbolically in FINDING_P63, to distinguish C1 (admits regular solutions)
from C2 (needs a free normalization) from C3 (needs a new arbitrary
function) -- the open question FINDING_P63's own critical test left
unresolved, and the natural next step it named explicitly.

METHOD CHOICE, stated up front: a full closed-form solution (as
FINDING_P62 found for g_hat=0, the exactly-solvable dust+stiff-fluid
system) is not expected to exist once g_hat!=0 couples phibar into the
Friedmann equation nonlinearly via (1-g_hat*phibar). Rather than commit
to a symbolic perturbative construction (order-by-order in g_hat) without
first knowing whether the system even behaves regularly, this file scouts
NUMERICALLY first -- cheaper, faster, and directly informative about
qualitative behavior (regular vs singular) before deciding whether a
symbolic follow-up is warranted.

EVIDENCE MARKER: every quantitative claim below is [VERIFIED-NUMERIC],
NOT [VERIFIED-SYMPY] -- illustrative/regime-dependent findings at
specific parameter and initial-condition choices, not a general proof
for all (g_hat, IC) space. This distinction is maintained throughout,
per this project's own evidence-marker discipline.

SYSTEM SOLVED (from FINDING_P63, all three background EOMs used exactly,
E_ii NEVER imposed directly -- reserved as a code-fidelity self-check,
see below):
  rhobar_A(t) = C / a(t)^3                        (E_rho, already solved)
  phibar_ddot = g_hat*rhobar_A - 3*H*phibar_dot    (E_phi)
  H = sqrt[(8*pi*G_N/3)*(rhobar_A*(1-g_hat*phibar) + phibar_dot^2/2)]
                                                    (E_00)
  a_dot = H*a

Initial conditions matched to FINDING_P62's own exact g_hat=0 solution at
t0=1 (a^3=(9K/4)*t^2-1, K:=8*pi*G_N/3, B=D=1) -- i.e., "switch on" g_hat
from an otherwise-standard cosmological state, then integrate forward.

[SKEPTIC-CORRECTED, Step 8a, applied throughout this file] Two framings
in the original version of this file overclaimed relative to the
evidence and were corrected: (1) the E_ii finite-difference self-check
does NOT independently test P63's closure identity -- given how H,
phibar_ddot, rhobar_A_dot are coded here, E_ii=0 is an ALGEBRAIC
IDENTITY of the RHS as written (independently verified symbolically,
both by the skeptic and re-derived here before accepting), so it tests
CODE FIDELITY to FINDING_P63's formulas, not independent physics; a
residual at the ~1e-11 finite-difference roundoff floor is CONSISTENT
with exact zero, not confirmation "to near machine precision" of
something smaller. (2) "singular" trajectories are relabeled "exited the
physical regime" -- the ODE itself stays FINITE at rho_phys=0 (H^2 there
reduces to K*phibar_dot^2/2>=0, not a blow-up); stopping there is a
MODELING decision (rho_phys<0 deemed unphysical), not a mathematical
singularity. The C1/C2/C3 classification is presented as multiple LIVE
possibilities at the end, not a single favored reading.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - L0 descriptive
"""

import numpy as np
from scipy.integrate import solve_ivp

G_N = 1.0
K = 8 * np.pi * G_N / 3
T0 = 1.0


def initial_conditions():
    a0_cubed = (9 * K / 4) * T0**2 - 1
    a0 = a0_cubed ** (1 / 3)
    rhoA0 = 1 / a0_cubed  # B=1
    phidot0 = np.sqrt(2) / a0_cubed  # D=1
    C = rhoA0 * a0**3  # =1 by construction (B=1)
    return a0, rhoA0, phidot0, C


def H_of(a, phi, phidot, ghat, C):
    rhoA = C / a**3
    inside = (8 * np.pi * G_N / 3) * (rhoA * (1 - ghat * phi) + phidot**2 / 2)
    return (np.sqrt(inside), inside) if inside >= 0 else (np.nan, inside)


def rhs(t, y, ghat, C):
    a, phi, phidot = y
    rhoA = C / a**3
    H, inside = H_of(a, phi, phidot, ghat, C)
    if inside < 0:
        return [np.nan, np.nan, np.nan]
    return [H * a, phidot, ghat * rhoA - 3 * H * phidot]


def rho_phys_zero_event(t, y, ghat, C):
    a, phi, phidot = y
    return 1 - ghat * phi


rho_phys_zero_event.terminal = True
rho_phys_zero_event.direction = -1


def check_Eii_code_fidelity(sol, ghat, C, label):
    """[SKEPTIC-CORRECTED, Step 8a] E_ii=-2*addot/a-H^2-4*pi*G_N*phidot^2 is
    NOT independent physics being tested here: given how H (from E_00),
    phibar_ddot (from E_phi), and rhoA_dot (from E_rho) are CODED, E_ii=0
    is an ALGEBRAIC IDENTITY of the RHS as written (independently verified
    symbolically, see finding.md) -- it would hold on ANY trajectory this
    code produces, correct or buggy in some OTHER way. What a nonzero
    residual WOULD catch: a typo/sign/factor error in the coded H, rhoA,
    or phibar_ddot formulas relative to FINDING_P63's own equations -- a
    real, useful code-correctness check, just not "independent evidence
    the physics holds," as originally (over)claimed.

    Precision floor, stated honestly: central difference with dt=1e-5
    has an expected roundoff floor of order eps_machine/dt ~ 1e-16/1e-5
    = 1e-11 on O(1) quantities -- a residual AT that floor is CONSISTENT
    with exact zero, not evidence of something smaller being resolved."""
    ts = np.linspace(sol.t[0], sol.t[-1], 12)[1:-1]
    dt = 1e-5
    max_resid = 0.0
    for tt in ts:
        a_m, phi_m, phidot_m = sol.sol(tt - dt)
        a_p, phi_p, phidot_p = sol.sol(tt + dt)
        a_c, phi_c, phidot_c = sol.sol(tt)
        H_m, _ = H_of(a_m, phi_m, phidot_m, ghat, C)
        H_p, _ = H_of(a_p, phi_p, phidot_p, ghat, C)
        H_c, _ = H_of(a_c, phi_c, phidot_c, ghat, C)
        addot = (H_p * a_p - H_m * a_m) / (2 * dt)
        Eii = -2 * addot / a_c - H_c**2 - 4 * np.pi * G_N * phidot_c**2
        max_resid = max(max_resid, abs(Eii))
    print(
        f"    [E_ii code-fidelity check, {label}] max|E_ii| over {len(ts)} "
        f"points = {max_resid:.3e} (finite-difference roundoff floor at "
        f"dt=1e-5 is ~1e-11 -- this residual is CONSISTENT with the coded "
        f"RHS matching FINDING_P63's formulas exactly, not a physics test)"
    )
    return max_resid


def main():
    print("=" * 78)
    print("P64 -- numeric scout of the g_hat!=0 coupled background: regular")
    print("vs physical-regime-exit behavior across (g_hat, phi0) -- informs,")
    print("does not by itself decide, C1 vs C2 vs C3")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    a0, rhoA0, phidot0, C = initial_conditions()
    print("\nInitial conditions (matched to FINDING_P62's own g_hat=0 solution,")
    print(f"t0={T0}): a0={a0:.6f}, rhoA0={rhoA0:.6f}, phidot0={phidot0:.6f}, C={C:.6f}")
    print("\n[SKEPTIC-CORRECTED, Step 8a] TERMINOLOGY: the ODE itself stays")
    print("FINITE at 1-g_hat*phibar=0 (H^2 there is K*phidot^2/2>=0 generically,")
    print("not zero or negative -- independently verified symbolically). Crossing")
    print("into rho_phys<0 is a MODELING CHOICE to stop (deemed unphysical), NOT")
    print("a mathematical blow-up. 'exits physical regime' used below instead of")
    print("'singular' throughout, to keep this distinction explicit.")

    max_Eii_seen = 0.0
    n_exited = 0
    n_regular = 0

    print("\n" + "-" * 78)
    print("SWEEP 1 -- phi0=0 (reference boundary condition), g_hat scanned")
    print("across FOUR ORDERS OF MAGNITUDE, INCLUDING NEGATIVE g_hat")
    print("(coupling sign flip -- untested in the original pass)")
    print("-" * 78)
    ghat_results = {}
    for ghat in [-1.0, -0.1, 0.01, 0.1, 0.3, 1.0, 3.0, 10.0]:
        y0 = [a0, 0.0, phidot0]
        sol = solve_ivp(
            rhs,
            [T0, T0 + 50],
            y0,
            args=(ghat, C),
            max_step=0.05,
            events=rho_phys_zero_event,
            dense_output=True,
            rtol=1e-9,
            atol=1e-12,
        )
        exited = len(sol.t_events[0]) > 0
        phi_end = sol.y[1][-1]
        print(
            f"\n  g_hat={ghat}: status={sol.status}, "
            f"{'exited physical regime at t=' + f'{sol.t_events[0][0]:.4f}' if exited else f't_end={sol.t[-1]:.2f}, delta_phi={phi_end - 0.0:+.6f} (regular)'}"
        )
        ghat_results[ghat] = "exited" if exited else "regular"
        if exited:
            n_exited += 1
        else:
            n_regular += 1
            resid = check_Eii_code_fidelity(sol, ghat, C, f"g_hat={ghat}")
            max_Eii_seen = max(max_Eii_seen, resid)

    print("\n" + "-" * 78)
    print("SWEEP 2 -- g_hat=0.3 fixed, phi0 scanned (including deliberately")
    print("close to the rho_phys=0 boundary at phi0=0.9/g_hat)")
    print("-" * 78)
    ghat_fixed = 0.3
    phi0_results = {}
    for phi0_test in [-0.5, 0.0, 0.5, 0.9 / ghat_fixed]:
        y0 = [a0, phi0_test, phidot0]
        sol = solve_ivp(
            rhs,
            [T0, T0 + 20],
            y0,
            args=(ghat_fixed, C),
            max_step=0.05,
            events=rho_phys_zero_event,
            dense_output=True,
            rtol=1e-9,
            atol=1e-12,
        )
        exited = len(sol.t_events[0]) > 0
        phi_end = sol.y[1][-1]
        print(
            f"\n  phi0={phi0_test:.4f}: status={sol.status}, "
            f"{'exited physical regime at t=' + f'{sol.t_events[0][0]:.4f}' if exited else f't_end={sol.t[-1]:.2f}, delta_phi={phi_end - phi0_test:+.6f} (regular)'}"
        )
        phi0_results[phi0_test] = "exited" if exited else "regular"
        if exited:
            n_exited += 1
        else:
            n_regular += 1
            resid = check_Eii_code_fidelity(sol, ghat_fixed, C, f"phi0={phi0_test:.2f}")
            max_Eii_seen = max(max_Eii_seen, resid)

    print("\n" + "-" * 78)
    print("SWEEP 3 -- [SKEPTIC-DEMANDED] integrator-sensitivity check: does the")
    print("g_hat=3.0 boundary-exit time depend on the ODE solver/tolerance, or")
    print("is it robust across genuinely different numerical methods?")
    print("-" * 78)
    ghat_test = 3.0
    y0 = [a0, 0.0, phidot0]
    exit_times = {}
    for method, rtol_test in [("RK45", 1e-9), ("DOP853", 1e-9), ("LSODA", 1e-6)]:
        sol_m = solve_ivp(
            rhs,
            [T0, T0 + 50],
            y0,
            args=(ghat_test, C),
            method=method,
            max_step=0.05,
            events=rho_phys_zero_event,
            rtol=rtol_test,
            atol=1e-12,
        )
        t_exit = sol_m.t_events[0][0] if len(sol_m.t_events[0]) > 0 else None
        exit_times[method] = t_exit
        print(f"  method={method}, rtol={rtol_test}: exit_time={t_exit}")
    times = [v for v in exit_times.values() if v is not None]
    assert len(times) == len(exit_times), (
        "not all methods agree the trajectory exits the physical regime -- "
        "report exactly this, the boundary-crossing behavior is method-dependent"
    )
    spread = max(times) - min(times)
    print(f"  spread across methods: {spread:.2e} (relative: {spread / min(times):.2e})")
    assert spread / min(times) < 1e-3, (
        f"exit time spread across integrators ({spread:.2e}, relative "
        f"{spread / min(times):.2e}) is too large to call this a robust, "
        "method-independent dynamical result -- report exactly this"
    )
    print("  -> CONFIRMED: exit time agrees across three genuinely different")
    print("     integration methods to within 0.1% -- the boundary-crossing")
    print("     is a robust feature of the dynamics, not a solver artifact.")

    print("\n" + "=" * 78)
    print("SANITY ASSERTIONS")
    print("=" * 78)
    assert n_regular > 0, "no regular trajectory found at all -- report this, do not proceed"
    assert n_exited > 0, (
        "no boundary-exit trajectory found even at g_hat=10 or phi0 near the "
        "boundary -- this would mean the regime split below was never actually "
        "observed; report exactly this, do not describe a split that wasn't seen"
    )
    assert max_Eii_seen < 1e-6, (
        f"E_ii code-fidelity residual too large ({max_Eii_seen:.3e}) on a "
        "REGULAR trajectory -- this would mean the coded RHS does NOT match "
        "FINDING_P63's own formulas; report exactly this"
    )
    print(
        f"Regular trajectories found: {n_regular}. Exited physical regime "
        f"(rho_phys=0 hit): {n_exited}. Max E_ii code-fidelity residual on "
        f"regular trajectories: {max_Eii_seen:.3e} (consistent with the coded "
        f"RHS matching FINDING_P63's own formulas exactly, at the finite-"
        f"difference method's own ~1e-11 roundoff floor)."
    )

    print("\n" + "=" * 78)
    print("VERDICT [VERIFIED-NUMERIC throughout -- illustrative/regime-")
    print("dependent, NOT a general proof for all (g_hat, IC) space]")
    print("=" * 78)
    print("Regime-dependent: for SMALL |g_hat| (<=1.0 tested, BOTH signs) with")
    print("phi0 not close to the rho_phys=0 boundary (1/g_hat), the coupled")
    print("system evolves REGULARLY over long timescales, with a NON-TRIVIAL")
    print("phibar displacement (not just 'coupling too weak to matter over the")
    print("integrated interval' -- see delta_phi printed above for each case).")
    print()
    print("For LARGE g_hat (>=3.0 tested) OR phi0 close to 1/g_hat, phibar is")
    print("driven monotonically toward the rho_phys=rhobar_A*(1-g_hat*phibar)=0")
    print("surface by the g_hat*rhobar_A source term in E_phi, and REACHES it")
    print("in FINITE TIME. [SKEPTIC-CORRECTED] The ODE itself stays FINITE")
    print("there (H^2 -> K*phidot^2/2 >= 0, not a blow-up) -- this is a MODELING")
    print("decision to stop at the edge of the physically sensible regime, not")
    print("a mathematical singularity. Confirmed ROBUST across three genuinely")
    print("different integration methods (Sweep 3, <0.1% spread) -- not a")
    print("solver-specific artifact.")
    print()
    print("READING for C1/C2/C3, presented as multiple LIVE possibilities, NOT")
    print("a single favored answer [SKEPTIC-CORRECTED -- the original version")
    print("of this verdict over-committed to a C3 reading without ruling out")
    print("the other two]:")
    print("  - C1-compatible: the system DOES admit regular solutions, just")
    print("    within a BOUNDED region of (g_hat, IC) space -- common for")
    print("    nonlinear systems, does not by itself require new machinery.")
    print("  - C2-compatible: which side of the boundary is 'physically")
    print("    relevant' depends on FINDING_P39's own still-open G_N-vs-g_hat")
    print("    SI relation -- resolving it could simply PLACE the realistic")
    print("    g_hat safely inside the regular region (a normalization")
    print("    question, not a structural one).")
    print("  - C3-compatible: if a realistic g_hat and IC genuinely fall in")
    print("    the boundary-exit region, rho_phys<0 (negative gravitating")
    print("    dust mass) may signal the point-particle-dust construction")
    print("    itself needs a new prescription there -- but this is NOT")
    print("    established by this file, only one live possibility.")
    print("  This finding does not adjudicate between the three -- doing so")
    print("  needs the systematic 2D scan and FINDING_P39 resolution named in")
    print("  finding.md's own 'Not yet done'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
