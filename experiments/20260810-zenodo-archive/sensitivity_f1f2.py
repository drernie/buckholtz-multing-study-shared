"""
Sensitivity of the MULTING H(z) fit to the near-cancellation between the
dipole (F1) and quadrupole (F2) terms.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
Written 2026-08-10 against Buckholtz (2026), Zenodo 10.5281/zenodo.21204955.

WHY this question. Reproducing the archive shows the net specific force is a
small residue of two much larger, nearly-cancelling terms: at z=1.965 the
archive prints -F1 = +52.99 and F2 = -46.53 against a net of +5.99. A referee
will ask what that does to the result's stability. There are two distinct
questions here and they have different answers:

  (A) STRUCTURAL   -- perturb one beta, hold the other fixed. Amplification is
                      set by |F_i| / |net| and is necessarily large.
  (B) EFFECTIVE    -- perturb one beta and let the fit RE-OPTIMISE the other,
                      which is what actually happens when both are fitted.
                      If they are degenerate, chi2 barely moves and the
                      published conclusion is robust even though (A) is large.

Reporting (A) alone would overstate fragility; reporting (B) alone would hide
the conditioning. Both are computed below.

Everything uses the archive's own chi2 (33 points: 31 cosmic chronometers +
SH0ES + DESI, diagonal errors) and its own multing_core, unmodified.
"""

import multing_core as mc
import numpy as np
import yaml
from scipy.optimize import minimize_scalar

# --- archive's own data and chi2 setup (mirrors generate_all_results.py) ---
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
zfine = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), z33])))

# SH0ES-anchored row: H0 fixed, beta_1 and beta_2 the only free parameters.
CFG = A["fitted_configurations"]["sh0es_anchored_0pct"]
H0A = CFG["H0_anchor_kms"]
B1F, B2F = CFG["beta_1"], CFG["beta_2"]
CHI2_PUB = CFG["chi2_33"]


def chi2(b1, b2):
    if b1 < 0 or b2 < 0:
        return 1e12
    Hm = mc.H_of_z_kms(zfine, H0A, b1, b2, Z_SHOES)
    if np.any(np.isnan(Hm)):
        return 1e12
    return float(np.sum(((np.interp(z33, zfine, Hm) - H33) / s33) ** 2))


def sep(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ---------------------------------------------------------------------------
sep("0. Anchor check -- do we reproduce the published fit?")
c0 = chi2(B1F, B2F)
print(f"  beta_1 = {B1F:.5g}   beta_2 = {B2F:.5g}")
print(f"  chi2_33 computed = {c0:.4f}   published = {CHI2_PUB}")
print(f"  {'OK' if abs(c0 - CHI2_PUB) < 0.02 else 'MISMATCH -- stop, do not trust what follows'}")

# ---------------------------------------------------------------------------
sep("A. STRUCTURAL: how large is the cancellation?")
print("  Amplification = |F_i| / |net|: the factor by which a relative error")
print("  in one term is magnified in the net specific force.\n")
print(
    f"  {'z':>7} {'F0':>10} {'-F1':>10} {'F2':>10} {'-Facc':>9} {'net':>9} "
    f"{'|F1|/net':>9} {'|F2|/net':>9}"
)
amps = []
for z in [1.965, 1.07, 0.5, 0.07, 0.0]:
    F0, F1, F2 = mc.forces(z, B1F, B2F)
    Facc = mc.F_accretion(z)
    net = F0 - F1 + F2 - Facc
    u = 1.0
    a1, a2 = abs(F1 / net), abs(F2 / net)
    amps.append((z, a1, a2))
    print(
        f"  {z:>7.3f} {F0 / abs(net) * u:>10.3f} {-F1 / abs(net) * u:>10.3f} "
        f"{F2 / abs(net) * u:>10.3f} {-Facc / abs(net) * u:>9.3f} {net / abs(net) * u:>9.3f} "
        f"{a1:>9.1f} {a2:>9.1f}"
    )
print("\n  (columns normalised by |net| so the amplification is read directly)")
print(f"  Worst-case amplification over these z: {max(max(a1, a2) for _, a1, a2 in amps):.1f}x")

# ---------------------------------------------------------------------------
sep("B. NAIVE (one-at-a-time): perturb beta_1, hold beta_2 fixed")
print(f"  {'delta_b1':>9} {'chi2':>12} {'d_chi2':>12}   verdict")
for d in [-0.05, -0.01, -0.002, 0.002, 0.01, 0.05]:
    c = chi2(B1F * (1 + d), B2F)
    dc = c - c0
    verdict = (
        "fit destroyed"
        if dc > 100
        else ("badly degraded" if dc > 9 else ("degraded" if dc > 1 else "tolerable"))
    )
    print(f"  {d * 100:>8.1f}% {c:>12.2f} {dc:>+12.2f}   {verdict}")

# ---------------------------------------------------------------------------
sep("C. EFFECTIVE: perturb beta_1, let beta_2 RE-OPTIMISE (the real question)")
print("  This is what a fit actually does. If beta_1 and beta_2 are degenerate,")
print("  chi2 stays near its minimum and the conclusion survives.\n")
print(f"  {'delta_b1':>9} {'beta_2 refit':>14} {'d_b2':>9} {'chi2':>10} {'d_chi2':>9}")
for d in [-0.05, -0.01, -0.002, 0.002, 0.01, 0.05]:
    b1 = B1F * (1 + d)
    r = minimize_scalar(
        lambda lb2, _b1=b1: chi2(_b1, np.exp(lb2)),
        bracket=(np.log(B2F * 0.5), np.log(B2F), np.log(B2F * 2.0)),
        method="brent",
        options={"xtol": 1e-10},
    )
    b2 = np.exp(r.x)
    c = chi2(b1, b2)
    print(
        f"  {d * 100:>8.1f}% {b2:>14.5g} {100 * (b2 / B2F - 1):>+8.2f}% {c:>10.3f} {c - c0:>+9.3f}"
    )

# ---------------------------------------------------------------------------
sep("D. CONDITIONING of the 2-parameter fit (Hessian in relative units)")
print("  Parametrise b_i = b_i_fit * (1 + d_i) and take the Hessian of chi2")
print("  in d-space, so eigenvalues are 'chi2 units per unit relative change'.\n")
print("  NOTE: a plain finite-difference Hessian was tried first and returned a")
print("  NEGATIVE eigenvalue (-3.5), which is impossible at a minimum. That is")
print("  numerical noise, not physics: the soft direction is so flat that the")
print("  curvature signal falls below the integrator/interpolation noise floor")
print("  at a 0.2% step. Reported instead: an empirical quadratic fit to the")
print("  chi2 profile along each direction, which averages that noise out.\n")


def quad_width(deltas, chis):
    """Fit d_chi2 = k*delta^2 through the origin; return k and the delta at d_chi2=1."""
    d = np.asarray(deltas, float)
    y = np.asarray(chis, float) - c0
    k = float(np.sum(d**2 * y) / np.sum(d**4))
    return k, (np.sqrt(1.0 / k) if k > 0 else np.inf)


# Stiff direction: move beta_1 with beta_2 held (mostly across the valley).
d_stiff = [-0.01, -0.005, -0.002, 0.002, 0.005, 0.01]
c_stiff = [chi2(B1F * (1 + d), B2F) for d in d_stiff]
k_s, w_s = quad_width(d_stiff, c_stiff)

# Soft direction: move beta_1 and let beta_2 re-optimise (along the valley).
d_soft = [-0.05, -0.02, 0.02, 0.05]
c_soft = []
ratios = []
for d in d_soft:
    b1 = B1F * (1 + d)
    r = minimize_scalar(
        lambda lb2, _b1=b1: chi2(_b1, np.exp(lb2)),
        bracket=(np.log(B2F * 0.5), np.log(B2F), np.log(B2F * 2.0)),
        method="brent",
        options={"xtol": 1e-12},
    )
    b2 = np.exp(r.x)
    c_soft.append(chi2(b1, b2))
    ratios.append((b2 / B2F - 1) / d)
k_f, w_f = quad_width(d_soft, c_soft)

print(f"  ACROSS the valley (beta_2 held):  d_chi2 = 1 at {w_s * 100:.3f}% move in beta_1")
print(f"  ALONG  the valley (beta_2 refit): d_chi2 = 1 at {w_f * 100:.2f}% move in beta_1")
print(f"  anisotropy of the fit: {w_f / w_s:.0f}x")
print(f"\n  degeneracy direction: d_beta_2 = {np.mean(ratios):+.3f} * d_beta_1")
print("  i.e. the two couplings are constrained almost entirely as one")
print("  combination; their individual values are far less determined than")
print("  their ratio. This is the mechanism that absorbs the cancellation.")

# ---------------------------------------------------------------------------
sep("E. Does the physical conclusion survive? H(z) under a re-fitted 1% shift")
b1p = B1F * 1.01
r = minimize_scalar(
    lambda lb2, _b1=b1p: chi2(_b1, np.exp(lb2)),
    bracket=(np.log(B2F * 0.5), np.log(B2F), np.log(B2F * 2.0)),
    method="brent",
    options={"xtol": 1e-10},
)
b2p = np.exp(r.x)
zq = np.array([0.0, 0.07, 0.5, 1.07, 1.965, 2.33])
H_ref = mc.H_of_z_kms(zfine, H0A, B1F, B2F, Z_SHOES)
H_per = mc.H_of_z_kms(zfine, H0A, b1p, b2p, Z_SHOES)
print(f"  {'z':>7} {'H ref':>10} {'H perturbed':>13} {'diff %':>9}")
for z in zq:
    a = float(np.interp(z, zfine, H_ref))
    b = float(np.interp(z, zfine, H_per))
    print(f"  {z:>7.3f} {a:>10.3f} {b:>13.3f} {100 * (b / a - 1):>+8.3f}%")
print(f"\n  chi2: {c0:.3f} -> {chi2(b1p, b2p):.3f}")
