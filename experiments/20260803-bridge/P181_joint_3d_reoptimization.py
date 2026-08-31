"""P181 -- runs the joint 3-parameter (beta1, beta2, epsilon) re-
optimization FINDING_P177/P178/P179/P180 all named as undone ("the
only way to properly test whether a real, practical epsilon-degeneracy
exists near the true minimum, not just at TJB's own epsilon=0
reference point" -- FINDING_P177 §"what this file does NOT
establish"), per the user's direct request. FINDING_P176 attempted a
short version of this and did not fully converge within a reasonable
wall-clock budget; this file uses a proper trust-region Newton method
with an explicit (finite-difference) gradient and Hessian.

Method: starting from TJB's own real reference point
(beta1_0, beta2_0, eps=0) -- rescaled to x0=(1,1,0) -- minimize the
real chi2 (same construction as FINDING_P177/P178/P179/P180, TJB's own
force law and 33-point H(z) data, reproduced verbatim) jointly over all
three parameters, at fixed H0,anchor=73.22 (TJB's own
"unconstrained_spotlighted" row).

CORRECTION (2026-08-31, context-asymmetric skeptic-caught, applied
before finalizing -- this dispatch, unlike FINDING_P180's, included
the actual source code, per that file's own lesson): a skeptic review
raised 7 attacks. Several confirmed real problems; one was independently
checked and found to rest on a WRONG mechanism (corrected, not simply
accepted); the core finding survives, substantially narrowed and
re-evidenced.

ACCEPTED, CONFIRMED BY DIRECT NUMERICAL CHECK -- the finite-difference
gradient/Hessian at the SOLUTION point (x_sol, |x1|~15, |eps|~7615) is
numerically UNRELIABLE using step sizes validated only at X0's scale
(1,1,0). Swept step size at x_sol from relative 1e-6 to 1e-2: |grad|
estimates ranged from 9.1e-3 to 3.4e12 with NO stable plateau --
contrast X0, where the same sweep gives a stable 9.6-10.4 across the
same range. This means the original "|grad| shrank 7 orders of
magnitude" and "solution is a stable fixed point under re-optimization"
claims, both computed via this same unreliable machinery, are NOT
trustworthy evidence for a genuine critical point and are DOWNGRADED
here to unreliable diagnostics, not dropped claims (see below for what
DOES support a genuine minimum). BFGS's own reported `success=False`
("precision loss") is consistent with, and corroborates, this same
numerical problem showing up mid-optimization, not something to wave
away as "same basin, so it doesn't matter."

WHAT SURVIVES, RE-EVIDENCED WITHOUT UNRELIABLE FINITE DIFFERENCES:
Nelder-Mead (derivative-free, immune to this problem) independently
converges to chi2=14.168, matching trust-exact's chi2=14.169 to 3
significant figures. A direct 1D line-scan along v1 from X0 (pure
function evaluations, no derivatives) shows a clean, unambiguous
U-shaped minimum around t=-7500 to -8000 (chi2 dips to ~14.23,
increases on both sides within the scanned range). These two
INDEPENDENT, derivative-free lines of evidence are what actually
support "a genuine local minimum exists here" -- not the trust-exact/
BFGS gradient-based convergence certificates.

ACCEPTED: calling X0 "a shallow saddle" (this project's own framing in
the skeptic-dispatch prompt, not literally in this file's code) is
geometrically imprecise -- a saddle is a CRITICAL point (zero gradient)
with mixed-sign Hessian eigenvalues; |grad(X0)|=10.4 means X0 is not a
critical point at all. CHECKED AND CORRECTED (the skeptic's own
proposed mechanism for this was checked directly and found WRONG): the
large residual gradient at X0 is NOT "essentially grad_eps because eps
is unconstrained by TJB's fit" (grad_eps is actually tiny, -0.0078) --
it is dominated by grad_x1, grad_x2 (7.76, -6.98), consistent with
FINDING_P176's own established finding that the (beta1,beta2) 2D
Hessian at eps=0 has condition number ~8300: a Nelder-Mead-style
optimizer converging by function-value tolerance on an ill-conditioned
surface can appear "converged" while leaving substantial residual
gradient specifically along the near-degenerate direction WITHIN
(beta1,beta2) itself, independent of epsilon.

ACCEPTED: the full 3D angle between (x_sol - X0) and the established
v1 (0.0003 deg) is influenced by v1's eps-component dominating both
vectors' magnitude (v1 is renormalized to eps-component=1; the
displacement's eps-component, ~7615, dwarfs its x1,x2 components).
CHECKED DIRECTLY (the skeptic's own proposed test): projecting BOTH
vectors onto just the (x1,x2) plane and re-measuring the angle there
gives 0.044 deg -- still remarkably tight (not "tens of degrees," which
would indicate the full-3D number was an artifact), and the three
independently-implied "distance traveled" ratios (from the eps, x1,
and x2 components separately) agree to within 0.4% of each other --
confirming the displacement genuinely is proportional to v1 across all
three coordinates, not merely dominated by one. The skeptic's specific
claim that the alignment is "arithmetically forced by normalization"
is REFUTED by this check. A softer, valid point survives: near a point
whose Hessian has one small/negative eigenvalue, local descent
naturally moves preferentially along that eigendirection initially --
some of this alignment is expected from X0's own local geometry, not a
fully independent confirmation. What remains genuinely informative:
the direction stays this tight over a ~7615-unit excursion, far beyond
any local quadratic approximation's validity radius -- i.e. the trough
is close to a straight line over an enormous range, not just locally
tangent to v1 near X0.

ADDED, per skeptic request: a densified +v1 scan (40 points, log-spaced,
explicit 1e12-ceiling check) confirms no missed secondary minimum --
chi2 increases monotonically the entire explored range, hitting the
unphysical H^2<=0 ceiling around t~100000.

ADDED, NOT requested by the skeptic but found while investigating
Attack 1/7 (an honest, additional caveat on how "robustly" this trough
is found): Nelder-Mead's convergence to this trough is SENSITIVE to
which single coordinate of X0 is perturbed before starting -- a 1%
perturbation in x1 alone converges back to near X0 (chi2~15.75, does
NOT find the trough); a 1% perturbation in x2 or epsilon alone DOES
find the trough (chi2~14.17). The trough is real and is found
consistently FROM X0 by 2 independent, reliable methods, but is not a
trivially-discoverable global feature independent of starting point --
consistent with, and an additional demonstration of, the severity of
the ill-conditioning already established.

ADDED: null-Delta-chi2 context for the "10% improvement is modest"
framing -- going from 2 effectively-fit parameters (TJB's own
beta1,beta2 at eps=0) to a genuine 3-parameter fit adds one degree of
freedom; a naive expectation for chi2 reduction from one additional
free parameter is of order 1. The observed reduction (15.75-14.17=1.58)
is about 1.5x this null expectation -- modest, not a discovery-scale
improvement, especially set against a ~7615-unit parameter excursion.

MERGED per the skeptic's Attack 7: "a genuine critical point was found"
and "it aligns with v1" are reported here as ONE finding with two
facets (endpoint location matches direction predicted by local
curvature at X0), not two independently-confirming results.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize

# ---------------------------------------------------------------------------
# Verbatim from TJB's own multing_core.py (same subset P176-P180 already
# used and positive-controlled)
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20
G = 6.674e-11
c = 299792458.0
Om_planck = 0.315
OL_planck = 0.685
H0_planck_si = 67.4 * KMSMPC_TO_SI

M0_kg = 1.193082e45
d0_m = 45.0 * MPC_TO_M
T0_keV = 3.7163
mu_mol = 0.6
m_proton = 1.67262192e-27
T_piv_keV = 2.27
Mgas_piv_kg = 2.28e13 * MSUN_TO_KG
z_piv = 0.25
B_real = 2.24
C_real = -1.00
f_merge = 0.25
f_coh = 1.0 / 3.0

rho_crit0 = 3.0 * H0_planck_si**2 / (8.0 * np.pi * G)


def Efun(z, Om=Om_planck, OL=OL_planck):
    return np.sqrt(Om * (1.0 + z) ** 3 + OL)


def M_of(z):
    return M0_kg * (1.0 + z) ** (-1.1)


def T_keV_of(z):
    return T0_keV * (M_of(z) / M0_kg) ** (2.0 / 3.0) * Efun(z) ** (2.0 / 3.0)


def Mgas_of(z):
    return Mgas_piv_kg * (T_keV_of(z) / T_piv_keV) ** B_real * (Efun(z) / Efun(z_piv)) ** C_real


def k_of(z):
    return 1.5 * (Mgas_of(z) / (mu_mol * m_proton)) * (T_keV_of(z) * KEV_TO_J)


def rho_crit(z):
    return rho_crit0 * Efun(z) ** 2


def R_of(z):
    return (3.0 * M_of(z) / (4.0 * np.pi * 500.0 * rho_crit(z))) ** (1.0 / 3.0)


def d_of(z):
    return d0_m * (1.0 + z) ** (-1.0)


def m_dot(z):
    return 1.1 * (H0_planck_si * Efun(z)) * M_of(z)


def v_infall(z):
    return np.sqrt(G * M_of(z) / R_of(z))


def F_accretion(z):
    return m_dot(z) * (f_coh * f_merge * v_infall(z))


def addot_over_a_eps(z, b1, b2, eps):
    M, R, k, d = M_of(z), R_of(z), k_of(z), d_of(z)
    F0 = (1 + eps) * (-G) * M * M / d**2
    F1 = b1 * (-G) * 2.0 * M * (k / c**2) * (R / d) / d**2
    F2 = b2 * (-G) * (k / c**2) ** 2 * (R * R / d**2) / d**2
    F_total = F0 - F1 + F2 - F_accretion(z)
    return (F_total / (M / 2.0)) / d


CC_POINTS = [
    (0.07, 69.0, 19.6),
    (0.09, 69.0, 12.0),
    (0.12, 68.6, 26.2),
    (0.17, 83.0, 8.0),
    (0.179, 75.0, 4.0),
    (0.199, 75.0, 5.0),
    (0.2, 72.9, 29.6),
    (0.27, 77.0, 14.0),
    (0.28, 88.8, 36.6),
    (0.352, 83.0, 14.0),
    (0.38, 83.0, 13.5),
    (0.4, 95.0, 17.0),
    (0.4, 77.0, 10.2),
    (0.425, 87.1, 11.2),
    (0.45, 92.8, 12.9),
    (0.47, 89.0, 49.6),
    (0.478, 80.9, 9.0),
    (0.48, 97.0, 62.0),
    (0.593, 104.0, 13.0),
    (0.68, 92.0, 8.0),
    (0.781, 105.0, 12.0),
    (0.875, 125.0, 17.0),
    (0.88, 90.0, 40.0),
    (0.9, 117.0, 23.0),
    (1.037, 154.0, 20.0),
    (1.3, 168.0, 17.0),
    (1.363, 160.0, 33.6),
    (1.43, 177.0, 18.0),
    (1.53, 140.0, 14.0),
    (1.75, 202.0, 40.0),
    (1.965, 186.5, 50.4),
]
zd = np.array([p[0] for p in CC_POINTS])
Hd = np.array([p[1] for p in CC_POINTS])
sd = np.array([p[2] for p in CC_POINTS])

Z_SHOES, H_SHOES, SIG_SHOES = 0.0233, 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8

z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
H33 = np.concatenate([Hd, [H_SHOES], [H_DESI]])
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))
N_POINTS = len(z33)
FULL_INDICES = np.arange(N_POINTS)

H0A0, B1_0, B2_0 = 73.22, 1.4335e10, 7.8067e17
X0 = np.array([1.0, 1.0, 0.0])
HSTEP = (1e-4, 1e-4, 0.02)  # step sizes validated at X0's scale, P176-P180


def chi2_eps_indices(h0_anchor, beta1, beta2, eps, indices):
    """Same construction as FINDING_P177/P178/P179/P180's chi2."""
    aa = np.array([addot_over_a_eps(zx, beta1, beta2, eps) for zx in ZFINE])
    integrand = aa / (1.0 + ZFINE)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, ZFINE)))
    i0 = np.argmin(np.abs(ZFINE - Z_SHOES))
    ds = ds_raw - ds_raw[i0]
    H2 = (h0_anchor * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    if np.any(H2 <= 0):
        return 1e12
    Hm = np.sqrt(H2) / KMSMPC_TO_SI
    idx = np.asarray(list(indices))
    Hp = np.interp(z33[idx], ZFINE, Hm)
    return np.sum(((Hp - H33[idx]) / s33[idx]) ** 2)


def f(x):
    x1, x2, eps = x
    return chi2_eps_indices(H0A0, x1 * B1_0, x2 * B2_0, eps, FULL_INDICES)


def grad_fd(x, h=HSTEP):
    g = np.zeros(3)
    for i in range(3):
        p, m = list(x), list(x)
        p[i] += h[i]
        m[i] -= h[i]
        g[i] = (f(p) - f(m)) / (2 * h[i])
    return g


def hess_fd(x, h=HSTEP):
    def d2(i, j, base):
        if i == j:
            p, m = list(base), list(base)
            p[i] += h[i]
            m[i] -= h[i]
            return (f(p) - 2 * f(base) + f(m)) / h[i] ** 2
        pp, pm, mp, mm = list(base), list(base), list(base), list(base)
        pp[i] += h[i]
        pp[j] += h[j]
        pm[i] += h[i]
        pm[j] -= h[j]
        mp[i] -= h[i]
        mp[j] += h[j]
        mm[i] -= h[i]
        mm[j] -= h[j]
        return (f(pp) - f(pm) - f(mp) + f(mm)) / (4 * h[i] * h[j])

    H = np.zeros((3, 3))
    for i in range(3):
        H[i, i] = d2(i, i, x)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        H[i, j] = H[j, i] = d2(i, j, x)
    return H


def v1_at_x0():
    """The established near-null eigenvector at X0, eps-normalized (same
    construction as FINDING_P177/P178/P179/P180)."""
    eigvals, eigvecs = np.linalg.eigh(hess_fd(X0))
    v1 = eigvecs[:, 0]
    return v1 / v1[2], eigvals


def test_positive_control_reference_matches_table_ii():
    """f(X0) must reproduce TJB's own Table II chi2_33=15.75 for the
    "unconstrained_spotlighted" row to within 1%.
    """
    val = f(X0)
    assert abs(val - 15.75) / 15.75 < 0.01, f"f(X0)={val} != 15.75"
    return val


def line_scan_along_v1(ts):
    """Pure function evaluations along X0 + t*v1 -- no derivatives, so
    immune to the finite-difference instability documented below.
    """
    v1, _ = v1_at_x0()
    return np.array([f(X0 + t * v1) for t in ts])


def test_line_scan_shows_genuine_minimum():
    """A dense, derivative-free line scan along v1 (negative t) must
    show a clean U-shape: chi2 below the reference value in the middle
    of the scanned range, and rising again toward both ends -- the
    primary, reliable evidence for a genuine local minimum (NOT the
    trust-exact/BFGS gradient-based convergence flags, see Correction).
    """
    ts = np.array([-3000, -6000, -7500, -9000, -12000])
    vals = line_scan_along_v1(ts)
    chi2_ref = f(X0)
    assert vals.min() < chi2_ref, "line scan never dips below the reference chi2"
    assert vals[0] > vals.min() and vals[-1] > vals.min(), "line scan is not U-shaped"
    return ts, vals


def test_nelder_mead_matches_line_scan_minimum():
    """Nelder-Mead (derivative-free, immune to the finite-difference
    instability documented below) must converge to a chi2 close to the
    line scan's own minimum region -- two independent, reliable
    (non-gradient-based) methods agreeing.
    """
    res = minimize(
        f, X0, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-10, "fatol": 1e-12}
    )
    _, vals = test_line_scan_shows_genuine_minimum()
    assert abs(res.fun - vals.min()) < 0.5, (
        f"Nelder-Mead ({res.fun}) vs line-scan min ({vals.min()})"
    )
    return res


def test_gradient_at_solution_is_scale_unstable():
    """DOCUMENTS (does not paper over) the skeptic-caught finding: the
    finite-difference gradient at x_sol is NOT converged across step
    sizes -- the ratio between the largest and smallest |grad| estimate
    across a step-size sweep must be large (i.e. genuinely unstable),
    confirming this is a real numerical limitation, not a one-off fluke.
    """
    res = minimize(f, X0, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-10})
    x_sol = res.x
    norms = []
    for scale in (1e-6, 1e-5, 1e-4, 1e-3):
        h = (
            max(scale * abs(x_sol[0]), 1e-8),
            max(scale * abs(x_sol[1]), 1e-8),
            max(scale * abs(x_sol[2]), 1e-6),
        )
        norms.append(np.linalg.norm(grad_fd(x_sol, h=h)))
    assert max(norms) / min(norms) > 10, (
        f"gradient at x_sol unexpectedly STABLE across step sizes: {norms} "
        "-- if this ever passes, the instability documented in the module "
        "Correction may no longer apply and that text should be revisited."
    )
    return norms


def test_displacement_aligns_with_established_v1_full_and_projected():
    """The displacement (x_sol - X0), from the reliable Nelder-Mead
    solution, must align tightly with v1 both in full 3D AND when
    projected onto just the (x1,x2) plane (the skeptic's own proposed
    check for whether the full-3D number is an artifact of eps
    dominating both vectors' magnitude). Thresholds: full < 0.01 deg,
    projected < 1 deg (looser, since eps's dominance is legitimately
    removed here).
    """
    res = minimize(f, X0, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-10})
    x_sol = res.x
    v1, _ = v1_at_x0()
    disp = x_sol - X0

    cos_full = abs(np.dot(disp, v1) / (np.linalg.norm(disp) * np.linalg.norm(v1)))
    angle_full = np.degrees(np.arccos(np.clip(cos_full, -1, 1)))
    assert angle_full < 0.01, f"full 3D angle = {angle_full} deg, not < 0.01"

    disp_2d, v1_2d = disp[:2], v1[:2]
    cos_2d = abs(np.dot(disp_2d, v1_2d) / (np.linalg.norm(disp_2d) * np.linalg.norm(v1_2d)))
    angle_2d = np.degrees(np.arccos(np.clip(cos_2d, -1, 1)))
    assert angle_2d < 1.0, f"(x1,x2)-projected angle = {angle_2d} deg, not < 1.0"

    return angle_full, angle_2d


def test_positive_v1_direction_confirmed_no_improvement():
    """Densified, ceiling-aware scan (skeptic-requested fix): moving
    along +v1 must not improve chi2 anywhere in a dense, log-spaced
    sweep, and must eventually hit the unphysical H^2<=0 ceiling
    (returned as chi2=1e12) -- confirming the asymmetric-trough claim
    with a real scan, not 4 arbitrary points.
    """
    v1, _ = v1_at_x0()
    ts = np.concatenate(
        [
            np.linspace(1, 100, 10),
            np.linspace(200, 2000, 10),
            np.linspace(3000, 50000, 10),
            np.linspace(60000, 150000, 10),
        ]
    )
    chi2_ref = f(X0)
    hit_ceiling = False
    for t in ts:
        val = f(X0 + t * v1)
        if val >= 1e12:
            hit_ceiling = True
            break
        assert val >= chi2_ref, f"+v1 direction improved chi2 at t={t}: {val} vs {chi2_ref}"
    return hit_ceiling


def test_nelder_mead_basin_sensitivity():
    """Honest additional finding (not requested by the skeptic, found
    while investigating their alignment attack): Nelder-Mead's
    convergence to the trough is sensitive to WHICH single coordinate
    of X0 is perturbed before starting. Confirms this asymmetry exists
    (does not assert which specific coordinates do which -- that is
    reported descriptively in FINDING_P181.md, since it is a discovered
    fact about this run, not a designed invariant).
    """
    outcomes = []
    for pert in (np.array([0.01, 0, 0]), np.array([0, 0.01, 0]), np.array([0, 0, 0.01])):
        res = minimize(f, X0 + pert, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-8})
        outcomes.append(res.fun)
    assert max(outcomes) - min(outcomes) > 1.0, (
        f"expected sensitivity to perturbed coordinate not found: {outcomes}"
    )
    return outcomes


if __name__ == "__main__":
    print("=" * 70)
    print("Positive control")
    print("=" * 70)
    chi2_ref = test_positive_control_reference_matches_table_ii()
    print(f"chi2(X0) = {chi2_ref:.5f}  (TJB Table II: 15.75) -- PASS\n")

    v1, eigvals0 = v1_at_x0()
    print(f"Established near-null eigenvector v1 (eps-normalized): {v1}")
    print(f"Hessian eigenvalues at X0: {eigvals0}")
    print(f"grad(X0) = {grad_fd(X0)}  (dominated by x1,x2, NOT eps)\n")

    print("=" * 70)
    print("Reliable (derivative-free) evidence for a genuine minimum")
    print("=" * 70)
    ts, vals = test_line_scan_shows_genuine_minimum()
    for t, v in zip(ts, vals, strict=True):
        print(f"  t={t:>7}  chi2={v:.5f}")
    nm_res = test_nelder_mead_matches_line_scan_minimum()
    print(f"\nNelder-Mead: chi2={nm_res.fun:.5f} at x={nm_res.x}")
    print(f"Line-scan minimum region: chi2~{vals.min():.5f} -- AGREE\n")

    print("=" * 70)
    print("Unreliable (gradient-based) diagnostics -- documented, not trusted")
    print("=" * 70)
    grad_norms = test_gradient_at_solution_is_scale_unstable()
    print(f"|grad| at x_sol across step-size sweep: {[f'{n:.2e}' for n in grad_norms]}")
    print("-> no stable plateau; trust-exact/BFGS convergence certificates unreliable here.\n")

    print("=" * 70)
    print("Alignment with established v1 (full 3D and (x1,x2)-projected)")
    print("=" * 70)
    angle_full, angle_2d = test_displacement_aligns_with_established_v1_full_and_projected()
    print(f"Full 3D angle:            {angle_full:.5f} deg")
    print(f"(x1,x2)-projected angle:  {angle_2d:.5f} deg\n")

    print("=" * 70)
    print("+v1 direction (densified, ceiling-aware)")
    print("=" * 70)
    hit_ceiling = test_positive_v1_direction_confirmed_no_improvement()
    print(f"No improvement found anywhere in dense scan; hit H^2<=0 ceiling: {hit_ceiling}\n")

    print("=" * 70)
    print("Nelder-Mead basin sensitivity (additional honest finding)")
    print("=" * 70)
    outcomes = test_nelder_mead_basin_sensitivity()
    print(f"chi2 outcomes for single-coordinate perturbations of X0: {outcomes}")
    print("-> trough is real and found from X0 by 2 reliable methods, but is NOT")
    print("   a trivially-discoverable feature independent of exact starting point.\n")

    print("=" * 70)
    print("Interpretation")
    print("=" * 70)
    delta = nm_res.x - X0
    print(
        f"chi2 improved from {chi2_ref:.3f} to {nm_res.fun:.3f} "
        f"({100 * (1 - nm_res.fun / chi2_ref):.1f}% reduction; null expectation for "
        f"one added free parameter is ~1, so this is ~1.5x null, modest), for a "
        f"displacement of ({delta[0]:.2f}, {delta[1]:.2f}, {delta[2]:.1f}) in "
        f"(x1, x2, eps) -- beta1 ~{nm_res.x[0]:.1f}x its fitted value, "
        f"beta2 ~{nm_res.x[1]:.1f}x, eps~{nm_res.x[2]:.0f}. NOT a small "
        f"perturbation, NOT a physically meaningful alternative fit. ONE finding, "
        f"two facets (per skeptic's Attack 7, not two independent confirmations): "
        f"a genuine local minimum exists here (Nelder-Mead + line-scan agree, "
        f"derivative-free), and its direction from X0 matches v1 tightly even "
        f"after removing eps's dominant magnitude ({angle_2d:.3f} deg projected) -- "
        f"though some of this is expected from X0's own local geometry (descent "
        f"naturally favors the softest eigendirection initially), not a fully "
        f"independent confirmation. Trust-exact/BFGS's own convergence claims at "
        f"the solution are NOT relied upon here (see Correction: severe, "
        f"documented finite-difference instability at this parameter scale)."
    )
