"""
Bridge stress test — does the H(z) result come from the force law or from the
kinematic translation rule?

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
2026-08-10, against Buckholtz (2026), Zenodo 10.5281/zenodo.21204955.

THE QUESTION. `multing_core.addot_over_a` returns F_total/((M/2)·d) and its own
docstring states this equals -dH/dt, explicitly NOT d̈/d. For a literal
mechanical reading F = μ·d̈ the same quantity would BE d̈/d, and the kinematic
identity d̈/d = Ḣ + H² then gives a different H(z) equation. Both are
implementable from the identical force history; they are not the same model.

    Model K (archive, "translation")   dH²/dz = 2·A_F/(1+z)
                                        i.e.  A_F = -Ḣ

    Model M (literal mechanics)        dH²/dz = 2·(H² - A_F)/(1+z)
                                        i.e.  A_F = d̈/d = Ḣ + H²

K is a quadrature; M is an ODE, because H² re-enters its own right-hand side.
Both are anchored identically: H(z_ref) = H0_anchor.

TWO PHASES, deliberately separate — the same discipline that made the beta
sensitivity result readable:

  Phase 1  fixed parameters, no refit. Asks: how much of the published H(z),
           of z_min, of the q = -1 crossing, is carried by the translation rule
           rather than by the force law?

  Phase 2  refit beta_1, beta_2 under Model M. Asks: can H(z) DISTINGUISH the
           two bridges at all? If both reach comparable chi2 after refitting,
           the answer is that it cannot, and an independent observable becomes
           necessary rather than merely desirable.

Everything uses the archive's own multing_core, its own chi2 (33 points:
31 cosmic chronometers + SH0ES + DESI, diagonal errors) and its own constants,
unmodified. The published chi2 is reproduced as an anchor before anything else.
"""

import multing_core as mc
import numpy as np
import yaml
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.optimize import minimize

# --------------------------------------------------------------------------
# Archive's own setup
# --------------------------------------------------------------------------
with open("assumptions.yaml") as f:
    A = yaml.safe_load(f)

_pts = A["cosmic_chronometer_data"]["points"]
zd = np.array([p[0] for p in _pts])
Hd = np.array([p[1] for p in _pts])
sd = np.array([p[2] for p in _pts])

Z_SHOES, H_SHOES, SIG_SHOES = 0.0233, 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8

z33 = np.concatenate([zd, [Z_SHOES], [Z_DESI]])
H33 = np.concatenate([Hd, [H_SHOES], [H_DESI]])
s33 = np.concatenate([sd, [SIG_SHOES], [SIG_DESI]])
zfine = np.sort(np.unique(np.concatenate([np.linspace(0.0, Z_DESI, 4000), z33])))

CFG = A["fitted_configurations"]["sh0es_anchored_0pct"]
H0A, B1F, B2F = CFG["H0_anchor_kms"], CFG["beta_1"], CFG["beta_2"]
CHI2_PUB = CFG["chi2_33"]
KMS = mc.KMSMPC_TO_SI


def sep(t):
    print("\n" + "=" * 76)
    print(t)
    print("=" * 76)


# --------------------------------------------------------------------------
# The two bridges
# --------------------------------------------------------------------------
def H_model_K(zgrid, H0_kms, b1, b2, zref=Z_SHOES):
    """Archive bridge: A_F = -Hdot. Pure quadrature (mc.H2_of_z, re-derived here
    on our own grid so both models share one grid and one anchor)."""
    zg = np.asarray(zgrid, float)
    aa = np.array([mc.addot_over_a(z, b1, b2) for z in zg])
    integrand = aa / (1.0 + zg)
    ds = np.concatenate(([0.0], cumulative_trapezoid(integrand, zg)))
    i0 = int(np.argmin(np.abs(zg - zref)))
    Y = (H0_kms * KMS) ** 2 + 2.0 * (ds - ds[i0])
    H = np.full_like(Y, np.nan)
    ok = Y > 0
    H[ok] = np.sqrt(Y[ok]) / KMS
    return H


def H_model_M(zgrid, H0_kms, b1, b2, zref=Z_SHOES):
    """Literal mechanical bridge: A_F = ddot(d)/d = Hdot + H^2.
    dY/dz = 2(Y - A_F)/(1+z), Y = H^2, integrated outward from zref.

    Integrated in the DIMENSIONLESS variable y = Y / Y_ref. In SI, Y = H^2 is of
    order 5e-36, so any absolute tolerance a solver would normally be given sits
    far above the solution itself and the integration silently returns garbage.
    A first version of this function used atol=1e-30 -- 2e5 times the value being
    integrated -- and passed every internal consistency check while being wrong at
    the 1e-3 level. It was caught only by feeding the ODE the analytic ddot(a)/a
    of flat LCDM and requiring flat LCDM H(z) back: that control failed at 1.0e-3
    and passes at 2.8e-13 in the scaled form below."""
    zg = np.asarray(zgrid, float)
    Yref = (H0_kms * KMS) ** 2

    def rhs(z, y):
        return 2.0 * (y[0] - mc.addot_over_a(z, b1, b2) / Yref) / (1.0 + z)

    y = np.full(zg.shape, np.nan)
    kw = {"rtol": 1e-12, "atol": 1e-14, "method": "RK45"}

    m_up = zg >= zref
    up = zg[m_up]
    if up.size and up[-1] > zref:
        s = solve_ivp(rhs, (zref, float(up[-1])), [1.0], t_eval=up, **kw)
        if s.success:
            y[m_up] = s.y[0]
    elif up.size:
        y[m_up] = 1.0
    m_dn = zg <= zref
    dn = zg[m_dn][::-1]
    if dn.size and dn[-1] < zref:
        s = solve_ivp(rhs, (zref, float(dn[-1])), [1.0], t_eval=dn, **kw)
        if s.success:
            y[m_dn] = s.y[0][::-1]
    elif dn.size:
        y[m_dn] = 1.0
    Y = y * Yref

    H = np.full_like(Y, np.nan)
    ok = np.isfinite(Y) & (Y > 0)
    H[ok] = np.sqrt(Y[ok]) / KMS
    return H


def chi2_of(Hcurve):
    if np.any(~np.isfinite(Hcurve)):
        return np.inf
    return float(np.sum(((np.interp(z33, zfine, Hcurve) - H33) / s33) ** 2))


def turning_point(Hcurve, zmax=0.6):
    """First z where dH/dz changes sign, by interpolation on the sign change."""
    m = zfine <= zmax
    z, H = zfine[m], Hcurve[m]
    if np.any(~np.isfinite(H)):
        return None
    d = np.gradient(H, z)
    s = np.where(np.diff(np.sign(d)))[0]
    if s.size == 0:
        return None
    i = s[0]
    z0 = z[i] - d[i] * (z[i + 1] - z[i]) / (d[i + 1] - d[i])
    return float(z0), float(np.interp(z0, z, H))


def q_of(Hcurve, z):
    """q = -1 - Hdot/H^2, from the curve itself: Hdot = -(1+z) H dH/dz."""
    d = np.gradient(Hcurve, zfine)
    Hz = np.interp(z, zfine, Hcurve)
    dz = np.interp(z, zfine, d)
    Hdot_over_H2 = -(1.0 + z) * dz / Hz
    return -1.0 - Hdot_over_H2


# --------------------------------------------------------------------------
sep("0. Positive control — Model K must reproduce the published fit")
HK = H_model_K(zfine, H0A, B1F, B2F)
c_K = chi2_of(HK)
print(f"  chi2_33  computed = {c_K:.4f}   published = {CHI2_PUB}")
print(
    f"  {'OK — proceed' if abs(c_K - CHI2_PUB) < 0.05 else 'MISMATCH — stop, nothing below is trustworthy'}"
)

# --------------------------------------------------------------------------
sep("PHASE 1 — same force history, same betas, no refit")
HM = H_model_M(zfine, H0A, B1F, B2F)
c_M = chi2_of(HM)

print(f"\n  {'z':>7} {'H  Model K':>12} {'H  Model M':>12} {'difference':>12}")
for z in [0.0, 0.07, 0.2, 0.5, 1.07, 1.965, 2.33]:
    a = float(np.interp(z, zfine, HK))
    b = float(np.interp(z, zfine, HM))
    print(f"  {z:>7.3f} {a:>12.3f} {b:>12.3f} {100 * (b / a - 1):>+11.2f}%")

print(f"\n  chi2_33   Model K = {c_K:10.3f}")
print(
    f"            Model M = {c_M:10.3f}"
    if np.isfinite(c_M)
    else "            Model M = not finite on the grid"
)

tK, tM = turning_point(HK), turning_point(HM)
print("\n  turning point (dH/dz = 0, equivalently q = -1):")
print(
    f"    Model K : z = {tK[0]:.5f}, H = {tK[1]:.3f}" if tK else "    Model K : none below z = 0.6"
)
print(
    f"    Model M : z = {tM[0]:.5f}, H = {tM[1]:.3f}" if tM else "    Model M : NONE below z = 0.6"
)

print("\n  deceleration parameter q(z):")
print(f"  {'z':>7} {'q  Model K':>12} {'q  Model M':>12}")
for z in [0.0, 0.1, 0.2, 0.5, 1.0]:
    print(f"  {z:>7.2f} {q_of(HK, z):>12.4f} {q_of(HM, z):>12.4f}")

# --------------------------------------------------------------------------
sep("PHASE 2 — refit beta_1, beta_2 under Model M. Can H(z) tell them apart?")


def chi2_M(p):
    b1, b2 = p
    if b1 <= 0 or b2 <= 0:
        return 1e12
    return chi2_of(H_model_M(zfine, H0A, b1, b2))


best = None
for f1, f2 in [(1.0, 1.0), (0.5, 0.5), (2.0, 2.0), (0.1, 0.1), (10.0, 10.0)]:
    r = minimize(
        chi2_M,
        [B1F * f1, B2F * f2],
        method="Nelder-Mead",
        options={"xatol": 1e-4, "fatol": 1e-8, "maxiter": 4000, "maxfev": 4000},
    )
    if best is None or r.fun < best.fun:
        best = r
b1M, b2M = best.x
c_M_refit = best.fun

print(f"  start beta_1 = {B1F:.5g}   ->  refit {b1M:.5g}   ({100 * (b1M / B1F - 1):+.1f}%)")
print(f"  start beta_2 = {B2F:.5g}   ->  refit {b2M:.5g}   ({100 * (b2M / B2F - 1):+.1f}%)")
print(f"\n  chi2_33   Model K (published fit) = {c_K:.3f}")
print(f"            Model M (refitted)       = {c_M_refit:.3f}")
print(f"            difference               = {c_M_refit - c_K:+.3f}")

HMr = H_model_M(zfine, H0A, b1M, b2M)
tMr = turning_point(HMr)
print("\n  Model M after refit:")
print(
    f"    turning point : z = {tMr[0]:.5f}, H = {tMr[1]:.3f}"
    if tMr
    else "    turning point : NONE below z = 0.6"
)
print(
    f"    H(0)          : {float(np.interp(0.0, zfine, HMr)):.3f}   (Model K: {float(np.interp(0.0, zfine, HK)):.3f})"
)

print("\n  ---- verdict on identifiability ----")
if np.isfinite(c_M_refit) and abs(c_M_refit - c_K) < 2.0:
    print("  The two bridges reach comparable chi2 on the same 33 points.")
    print("  H(z) alone does NOT identify which bridge is correct; an independent")
    print("  observable is required, not merely desirable.")
else:
    print("  The two bridges do NOT reach comparable chi2. H(z) carries")
    print("  information about which translation rule is in force.")
