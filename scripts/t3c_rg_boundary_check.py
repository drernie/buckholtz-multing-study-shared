"""T3c — Does 7:9:17 survive as an RG BOUNDARY CONDITION on the gauge couplings?

NOT_VALIDATION / NO_AUTHOR_ERROR. This is our own independent test of an
internally generated hypothesis (not TJB's claim). T3b already exhausted the
"7:9:17 as a pole-mass ratio" reading (multiplicative kappa leaves a +3.7-3.8
sigma residual). A DIFFERENT reading survives that check: maybe 7:9:17 is a
boundary condition on the running GAUGE COUPLINGS at some high scale mu*, not on
the pole masses. The Buckholtz tree relations give

    sin^2(theta_W) = 1 - 7/9 = 2/9  ==>  tan^2(theta_W) = (2/9)/(7/9) = 2/7 ,
    m_H^2/m_Z^2 = 17/9            ==>  lambda = (17/72)(g^2 + g'^2)   [tree].

Hypothesis under test:  g'^2(mu*) / g^2(mu*) = 2/7   at some physically
motivated scale mu*, found by SOLVING the RGE -- NOT by choosing mu* to fit.
Decisive cross-check: impose lambda(mu*) = (17/72)(g^2+g'^2)(mu*) as a boundary
condition, run lambda back to m_Z, and ask whether it reproduces m_H = 125.2 GeV
INDEPENDENTLY of how mu* was located.

--------------------------------------------------------------------------------
Beta functions used (1-loop SM). Coefficients verified this session (2026-07-22):

  Gauge (GUT-normalized g1 = sqrt(5/3) g'):
     (16 pi^2) dg_i/dt = b_i g_i^3 ,  (b1,b2,b3) = (41/10, -19/6, -7)
     [VERIFIED-WEBSEARCH: standard SM values, consistent with Buttazzo et al.
      1307.3536 "Investigating the near-criticality of the Higgs boson"; same
      coefficients quoted in Machacek-Vaughn and the PDG review of RGE running.]

  Top Yukawa (GUT norm):
     (16 pi^2) dy_t/dt = y_t ( 9/2 y_t^2 - 17/20 g1^2 - 9/4 g2^2 - 8 g3^2 )
     [VERIFIED-WEBSEARCH: standard 1-loop SM top-Yukawa beta function.]

  Higgs quartic (convention V = lambda |H|^4, m_H^2 = 2 lambda v^2, so
  lambda(m_Z) ~ 0.129; Buttazzo/Degrassi convention):
     (16 pi^2) dlambda/dt = 24 lambda^2 + 12 lambda y_t^2 - 6 y_t^4
        - 3 lambda (3 g2^2 + g'^2) + (3/8)[ 2 g2^4 + (g2^2 + g'^2)^2 ]
     [VERIFIED-WEBSEARCH standard Buttazzo form. NOTE: a web hit returned a
      factor-2-different variant (12 lambda^2, -12 y_t^4); that is a DIFFERENT
      lambda normalization. We use the V=lambda|H|^4 / m_H^2=2 lambda v^2
      convention consistently for BOTH the initial condition and the beta, so
      the convention cancels. The lambda sector is a SECONDARY cross-check; the
      verdict is fixed by the gauge sector alone, which at 1-loop is independent
      of y_t and lambda.]

Initial conditions at mu = m_Z (PDG 2024, MS-bar) [VERIFIED]:
  alpha_EM(m_Z)^-1 = 127.951 ,  sin^2(theta_W)_MSbar(m_Z) = 0.23129 ,
  alpha_s(m_Z) = 0.1179 ,  y_t(m_Z) ~ 0.95 ,  lambda(m_Z) = m_H^2/(2 v^2).

ANTI-POST-HOC DISCIPLINE: mu* is obtained by SOLVING tan^2(theta_W)(mu) = 2/7
along the trajectory. It is NOT chosen. If the only solution sits at an
unmotivated scale (or does not exist above m_Z), that is the finding.
"""

from __future__ import annotations

import math

PI = math.pi
K = 16.0 * PI * PI  # loop factor 16 pi^2

# ── Inputs at m_Z [VERIFIED — PDG 2024 MS-bar] ────────────────────────────────
M_Z = 91.1880  # GeV
ALPHA_EM_INV = 127.951  # alpha_EM(m_Z)^-1, MS-bar
S2W_MZ = 0.23129  # sin^2(theta_W)(m_Z), MS-bar
ALPHA_S = 0.1179  # alpha_s(m_Z)
V_HIGGS = 246.22  # GeV, Higgs vev
M_H = 125.20  # GeV

# Buckholtz tree targets
TAN2_TREE = 2.0 / 7.0  # tan^2(theta_W) = (2/9)/(7/9)
LAMBDA_COEF = 17.0 / 72.0  # lambda(mu*) = (17/72)(g^2 + g'^2)

# 1-loop gauge beta coefficients (GUT norm) [VERIFIED-WEBSEARCH]
B1, B2, B3 = 41.0 / 10.0, -19.0 / 6.0, -7.0

SEP = "=" * 76
DASH = "-" * 76


def initial_conditions() -> dict[str, float]:
    """Couplings at mu = m_Z from PDG MS-bar inputs."""
    e2 = 4.0 * PI / ALPHA_EM_INV
    g2sq = e2 / S2W_MZ  # SU(2)
    gpsq = e2 / (1.0 - S2W_MZ)  # U(1)_Y (non-GUT g')
    g1sq = (5.0 / 3.0) * gpsq  # GUT-normalized g1
    g3sq = 4.0 * PI * ALPHA_S
    lam = M_H**2 / (2.0 * V_HIGGS**2)  # V = lambda|H|^4 convention
    return {
        "g1": math.sqrt(g1sq),
        "g2": math.sqrt(g2sq),
        "g3": math.sqrt(g3sq),
        "yt": 0.95,  # y_t(m_Z) approx; gauge verdict independent of this
        "lam": lam,
    }


def gp2_over_g2(g1: float, g2: float) -> float:
    """tan^2(theta_W) = g'^2 / g^2 with g'^2 = (3/5) g1^2 (GUT norm)."""
    gpsq = (3.0 / 5.0) * g1 * g1
    return gpsq / (g2 * g2)


def derivs(y: list[float]) -> list[float]:
    """1-loop SM RGE right-hand sides. t = ln(mu / m_Z)."""
    g1, g2, g3, yt, lam = y
    g1sq, g2sq, g3sq = g1 * g1, g2 * g2, g3 * g3
    gpsq = (3.0 / 5.0) * g1sq  # non-GUT g'^2 for the quartic beta
    yt2 = yt * yt

    dg1 = B1 * g1 * g1sq / K
    dg2 = B2 * g2 * g2sq / K
    dg3 = B3 * g3 * g3sq / K
    dyt = yt * (4.5 * yt2 - (17.0 / 20.0) * g1sq - 2.25 * g2sq - 8.0 * g3sq) / K
    dlam = (
        24.0 * lam * lam
        + 12.0 * lam * yt2
        - 6.0 * yt2 * yt2
        - 3.0 * lam * (3.0 * g2sq + gpsq)
        + (3.0 / 8.0) * (2.0 * g2sq * g2sq + (g2sq + gpsq) ** 2)
    ) / K
    return [dg1, dg2, dg3, dyt, dlam]


def rk4_step(y: list[float], h: float) -> list[float]:
    k1 = derivs(y)
    k2 = derivs([yi + 0.5 * h * ki for yi, ki in zip(y, k1, strict=True)])
    k3 = derivs([yi + 0.5 * h * ki for yi, ki in zip(y, k2, strict=True)])
    k4 = derivs([yi + h * ki for yi, ki in zip(y, k3, strict=True)])
    return [
        yi + (h / 6.0) * (a + 2.0 * b + 2.0 * c + d)
        for yi, a, b, c, d in zip(y, k1, k2, k3, k4, strict=True)
    ]


def integrate(y0: list[float], t_end: float, n: int) -> list[tuple[float, list[float]]]:
    """Integrate from t=0 (m_Z) to t_end. Returns [(t, state), ...]."""
    h = t_end / n
    y = list(y0)
    traj = [(0.0, list(y))]
    for i in range(n):
        y = rk4_step(y, h)
        traj.append(((i + 1) * h, list(y)))
    return traj


def find_crossing(traj: list[tuple[float, list[float]]]) -> float | None:
    """Locate t where tan^2(theta_W) = 2/7, by sign change + linear interp."""
    prev_t, prev_state = traj[0]
    prev_f = gp2_over_g2(prev_state[0], prev_state[1]) - TAN2_TREE
    for t, state in traj[1:]:
        f = gp2_over_g2(state[0], state[1]) - TAN2_TREE
        if prev_f == 0.0:
            return prev_t
        if prev_f * f < 0.0:
            return prev_t + (t - prev_t) * (-prev_f) / (f - prev_f)  # linear
        prev_t, prev_f = t, f
    return None


def state_at(traj: list[tuple[float, list[float]]], t_target: float) -> list[float]:
    """Linear-interpolate the state vector at t_target."""
    prev_t, prev_state = traj[0]
    for t, state in traj[1:]:
        if (prev_t - t_target) * (t - t_target) <= 0.0:
            w = 0.0 if t == prev_t else (t_target - prev_t) / (t - prev_t)
            return [a + w * (b - a) for a, b in zip(prev_state, state, strict=True)]
        prev_t, prev_state = t, state
    return traj[-1][1]


def main() -> None:
    print(SEP)
    print("T3c — 7:9:17 as an RG boundary condition:  g'^2(mu*)/g^2(mu*) = 2/7 ?")
    print(SEP)

    y0 = initial_conditions()
    print("\n[initial conditions at mu = m_Z]  [VERIFIED — PDG 2024 MS-bar]")
    for k, v in y0.items():
        print(f"  {k:>4} = {v:.5f}")
    tan2_mz = gp2_over_g2(y0["g1"], y0["g2"])
    print(f"  tan^2(theta_W)(m_Z) = g'^2/g^2 = {tan2_mz:.6f}")
    print(f"  Buckholtz target    = 2/7      = {TAN2_TREE:.6f}")
    print(f"  gap at m_Z          = {tan2_mz - TAN2_TREE:+.6f}  (measured is ALREADY above 2/7)")

    y0v = list(y0.values())

    # ── Run UP to a super-GUT scale ───────────────────────────────────────────
    t_top = math.log(1e19 / M_Z)  # up to 1e19 GeV
    up = integrate(y0v, t_top, 4000)
    print("\n" + DASH)
    print("RUNNING UP  (mu = m_Z -> 1e19 GeV):  tan^2(theta_W) trajectory")
    print(DASH)
    print(f"  {'mu [GeV]':>12}  {'g1':>7}  {'g2':>7}  {'g' + chr(39) + '^2/g^2':>9}")
    for mu_dec in [1e2, 1e3, 1e6, 1e9, 1e12, 1e15, 1e16, 1e18, 1e19]:
        t = math.log(mu_dec / M_Z)
        if t > t_top:
            continue
        s = state_at(up, t)
        print(f"  {mu_dec:12.0e}  {s[0]:7.4f}  {s[1]:7.4f}  {gp2_over_g2(s[0], s[1]):9.5f}")
    cross_up = find_crossing(up)

    # ── Run DOWN toward ~1 GeV (where the ratio decreases toward 2/7) ──────────
    t_bot = math.log(1.0 / M_Z)  # down to 1 GeV
    down = integrate(y0v, t_bot, 2000)
    cross_down = find_crossing(down)

    print("\n" + DASH)
    print("WHERE (if anywhere) does tan^2(theta_W) = 2/7 ?")
    print(DASH)
    if cross_up is not None:
        mu_star = M_Z * math.exp(cross_up)
        print(f"  crossing ABOVE m_Z at mu* = {mu_star:.4g} GeV")
    else:
        print("  NO crossing above m_Z: tan^2 increases monotonically, moving")
        print(f"  AWAY from 2/7 (from {tan2_mz:.5f} up toward ~0.4-0.6 at GUT).")
    if cross_down is not None:
        mu_star_d = M_Z * math.exp(cross_down)
        print(f"  crossing BELOW m_Z at mu* = {mu_star_d:.4g} GeV")
        print("    >> below m_Z: NOT GUT-adjacent, NOT independently motivated,")
        print("       and in the OPPOSITE direction from any unification scale.")
        print("       (Also inside the region where SM thresholds/matching apply,")
        print("        so even this number is only a leading estimate.)")
    else:
        print("  NO crossing down to 1 GeV either.")

    # ── Cross-check: lambda boundary condition, IF a mu* is used ───────────────
    print("\n" + SEP)
    print("DECISIVE CROSS-CHECK: lambda(mu*) = (17/72)(g^2+g'^2), run to m_Z")
    print(SEP)
    # Use whichever mu* the running actually produced (here: the sub-m_Z one).
    if cross_down is not None:
        t_star = cross_down
        mu_star = M_Z * math.exp(t_star)
        s_star = state_at(down, t_star)
        g1s, g2s = s_star[0], s_star[1]
        gpsq_s = (3.0 / 5.0) * g1s * g1s
        g2sq_s = g2s * g2s
        lam_bc = LAMBDA_COEF * (g2sq_s + gpsq_s)  # tree boundary condition
        print(f"  mu* (from gauge solve) = {mu_star:.4g} GeV   [SOLVED, not chosen]")
        print(f"  g^2(mu*) = {g2sq_s:.5f} , g'^2(mu*) = {gpsq_s:.5f}")
        print(f"  lambda(mu*) boundary = (17/72)(g^2+g'^2) = {lam_bc:.5f}")
        # Run lambda from mu* back to m_Z: integrate the full system from mu*.
        y_star = [g1s, g2s, s_star[2], s_star[3], lam_bc]
        back = integrate(y_star, -t_star, max(50, int(2000 * abs(t_star))))
        lam_mz = back[-1][1][4]
        mh_pred = math.sqrt(2.0 * lam_mz) * V_HIGGS
        print(f"  lambda(m_Z) after running back = {lam_mz:.5f}")
        print(f"  => m_H predicted = sqrt(2 lambda) v = {mh_pred:.2f} GeV")
        print(f"     m_H measured                     = {M_H:.2f} GeV")
        print("  NOTE: because mu* sits just BELOW m_Z, this 'cross-check' is a very")
        print("  short run and is NOT an independent high-scale prediction. At tree")
        print("  level lambda=(17/72)(g^2+g'^2) is ALGEBRAICALLY the 17:9 pattern, so")
        print("  evaluating it near m_Z reproduces m_H by construction -- it is not")
        print("  new evidence. A genuine test needs a high-scale mu*, which is absent.")
    else:
        print("  Not reachable: no gauge crossing at any sensible scale.")

    # ── Verdict ───────────────────────────────────────────────────────────────
    print("\n" + SEP)
    print("VERDICT")
    print(SEP)
    print("  FAIL (non-post-hoc). The RG trajectory of tan^2(theta_W) is")
    print("  monotonically INCREASING with scale and ALREADY exceeds 2/7 at m_Z")
    print("  (0.3009 > 0.2857). Running UP moves the couplings AWAY from the")
    print("  Buckholtz value, so there is NO high (GUT-adjacent or intermediate)")
    print("  scale mu* where g'^2/g^2 = 2/7. The only crossing is BELOW m_Z, at a")
    print("  few tens of GeV -- unmotivated, threshold-contaminated, and opposite")
    print("  in direction to unification. The lambda cross-check cannot rescue the")
    print("  pattern because no legitimate high-scale mu* exists to anchor it.")
    print("  1-loop is DECISIVE here: 2-loop gauge corrections are O(few %) and")
    print("  cannot reverse a monotonic trend that starts on the wrong side of 2/7.")


if __name__ == "__main__":
    main()
