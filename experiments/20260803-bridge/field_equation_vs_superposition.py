"""Solve the field equation instead of superposing pairwise forces.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · unblock step 2 of FINDING_lq2_test_outcome.md

WHY. The pairwise treatment of MULTING's force law diverges: the shell factors
C_3, C_4 blow up as the field point approaches the shell, so K_4 = inf and K_3 is
regulator-dependent. That divergence is not in the theory -- it is in the method.
Expanding Phi in powers of eps FIRST and then superposing each 1/r^n term
separately assumes linear superposition, and the covariant completion is
nonlinear precisely in the kinetic sector.

WHAT REPLACES IT. Under the canonical field chi (dchi/dPhi = sqrt(f)) the field
equation collapses exactly:

    div(f grad Phi) - (1/2) f'|grad Phi|^2  ==  sqrt(f) * lap(chi)      [sympy-verified]

so lap(chi) = rho * Phi'(chi), and in vacuum lap(chi) = 0 to ALL orders. chi
therefore obeys a LINEAR equation: it superposes, and Newton's shell theorem
holds for it exactly (C = 1, the one shell factor that never diverged). All the
nonlinearity sits in the algebraic map

    Phi(chi) = [(1 + 3 eps chi)^(2/3) - 1] / (2 eps),
    F        = -grad Phi = -(1 + 3 eps chi)^(-1/3) grad chi.

So the correct recipe is: solve ONE linear Poisson equation for chi with the real
matter distribution, then apply an algebraic function. No shell integrals, no
C_k, no divergence, for any rho.

THE TEST BUILT ON THAT. The pairwise-kSZ model becomes a single Newtonian kernel
modulated by the potential, replacing three separately-superposed kernels two of
which do not exist:

    p_kSZ(r) = -A * K_2(r) * (1 + lam * chihat(r))^(-1/3)

with chihat(r) = chi(r)/chi(r_ref) and lam = 3 eps chi(r_ref) -- the size of the
nonlinear correction at r_ref, dimensionless and directly interpretable. One new
parameter, not two, because the field picture leaves no independent l_q.

TWO HONEST WARNINGS, both checked below rather than asserted.
 1. Phi depends on chi ABSOLUTELY, not only through its gradient, so the theory
    is NOT invariant under chi -> chi + const. The zero point is physical. In a
    cosmological setting it is fixed by a boundary condition at infinity that
    nobody has specified. Sensitivity to it is measured, not assumed away.
 2. A smooth monotonic modulation of an amplitude-profiled kernel may simply be
    reabsorbed by that amplitude. If so the data constrain nothing and the fit
    must say so instead of reporting a bound.
"""

import sys
from pathlib import Path

import numpy as np
from scipy.interpolate import interp1d

HERE = Path(__file__).resolve().parent
KSZ = HERE.parent / "20260802-ksz-force-law"
sys.path.insert(0, str(KSZ))

import h5py  # noqa: E402
from ksz_exact_kernel_fit import (  # noqa: E402
    H_LITTLE,
    RFIT_HI,
    RFIT_LO,
    build_kernel,
    c_shell,
    profile_chi2,
)

ART = KSZ / "artifacts"
R_REF = 100.0  # Mpc, where lam is defined


def potential_from_accel(r_grid: np.ndarray, g: np.ndarray, r_max: float) -> np.ndarray:
    """chi(r) = int_r^r_max g dr', i.e. the potential whose gradient is the
    Newtonian acceleration g, with chi(r_max) = 0. The upper limit is the IR
    boundary condition warning 1 is about; it is varied by the caller."""
    rr = np.linspace(r_grid.min(), r_max, 2000)
    gg = np.interp(rr, r_grid, g, left=g[0], right=0.0)
    cum = np.concatenate([[0.0], np.cumsum(np.diff(rr) * 0.5 * (gg[1:] + gg[:-1]))])
    return np.interp(r_grid, rr, cum[-1] - cum)


def main() -> None:
    print("=" * 78)
    print("FIELD EQUATION vs PAIRWISE SUPERPOSITION -- pairwise kSZ, ACT DR6")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    # ---- control: the one shell factor that is exact, and stays exact -------
    c2_err = max(abs(c_shell(x, 2) - 1.0) for x in (1e-6, 0.1, 0.5, 0.9, 0.999))
    print(f"\n[CONTROL] shell theorem C_2(rho) == 1 : max error {c2_err:.3e}")
    if c2_err > 1e-8:
        print("  *** FAILED - geometry wrong, stop. ***")
        return
    print("  -> chi obeys this exactly, for every shell, at every order in eps.")
    print("     C_3 and C_4 never enter the field picture at all.")

    # ---- data ---------------------------------------------------------------
    xi_raw = np.loadtxt(ART / "xi_zbin2.dat")
    xi_interp = interp1d(xi_raw[:, 0] / H_LITTLE, xi_raw[:, 1], bounds_error=False, fill_value=0.0)
    with h5py.File(ART / "dr6.hdf", "r") as f:
        pw = f["df_pw/block0_values"][:]
        cols = [c.decode() for c in f["df_pw/block0_items"][:]]
        cov = f["df_cov/block0_values"][:]
    r_all, p_all = pw[:, cols.index("r_mp")], pw[:, cols.index("ksz_curve")]
    m = (r_all >= RFIT_LO) & (r_all <= RFIT_HI)
    r, pobs = r_all[m], p_all[m]
    cinv = np.linalg.inv(cov[np.ix_(m, m)])
    k2 = build_kernel(r, xi_interp, 2)
    print(f"\n  bins: {m.sum()} of {len(r_all)},  r = {r.min():.1f}-{r.max():.1f} Mpc")
    print(f"  K_2 finite everywhere: {np.isfinite(k2).all()}  (K_4 was inf in all 15 bins)")

    # ---- the potential, and its IR sensitivity (warning 1) ------------------
    print("\n[IR BOUNDARY] chi depends on the absolute zero point, so on r_max:")
    chis = {}
    for r_max in (225.0, 500.0, 1000.0, 3000.0):
        ch = potential_from_accel(r, k2, r_max)
        chis[r_max] = ch
        print(
            f"  r_max = {r_max:>6.0f} Mpc : chi(25) = {ch[0]:.4e}, chi(100)/chi(25) = "
            f"{np.interp(R_REF, r, ch) / ch[0]:.4f}"
        )
    print("  -> the SHAPE converges; the absolute value does not. Since Phi depends on")
    print("     chi absolutely, the theory needs a boundary condition MULTING does not give.")

    chi = chis[1000.0]
    chihat = chi / np.interp(R_REF, r, chi)

    # ---- fit the one-parameter field-picture model -------------------------
    def model(lam: float) -> np.ndarray:
        arg = 1.0 + lam * chihat
        return -k2 * np.where(arg > 0, np.abs(arg) ** (-1.0 / 3.0), np.nan)

    lam_grid = np.linspace(-0.95, 20.0, 4001)
    chi2 = np.array([profile_chi2(pobs, cinv, model(x))[0] for x in lam_grid])
    ok_fin = np.isfinite(chi2)
    i0 = int(np.nanargmin(chi2))
    chi2_newt = profile_chi2(pobs, cinv, -k2)[0]

    print("\n[FIT] p_kSZ = -A K_2 (1 + lam chihat)^(-1/3),  amplitude profiled")
    print(f"  Newtonian (lam = 0)     : chi2 = {chi2_newt:.4f}  for {len(r)} bins")
    print(f"  best fit lam            = {lam_grid[i0]:+.4f}   chi2 = {chi2[i0]:.4f}")
    print(f"  improvement             : delta chi2 = {chi2_newt - chi2[i0]:.4f} for 1 extra dof")
    good = lam_grid[ok_fin][chi2[ok_fin] <= chi2[i0] + 3.84]
    print(f"  95% interval on lam     : [{good.min():+.3f}, {good.max():+.3f}]")
    print(
        f"  every chi2 finite       : {np.isfinite(chi2).sum()}/{len(chi2)} grid points"
        "   <- contrast with the superposition model, which had none"
    )

    # ---- warning 2: is this modulation just the amplitude in disguise? -----
    print("\n[DEGENERACY CHECK] can the amplitude absorb the correction?")
    print(
        f"  chihat over the fitted range: {chihat.min():.4f} to {chihat.max():.4f}"
        f"   (ratio {chihat.max() / max(chihat.min(), 1e-12):.2f})"
    )
    for lam in (0.5, 2.0, 10.0):
        mod = model(lam)
        shape = mod / -k2
        _, amp = profile_chi2(pobs, cinv, mod)
        print(
            f"  lam = {lam:>5.1f}: modulation spans {shape.min():.4f}-{shape.max():.4f}"
            f"  (variation {100 * (shape.max() / shape.min() - 1):5.1f} %), best amp {amp:.4g}"
        )
    print("  -> if the modulation is nearly flat across the fitted range, lam is")
    print("     degenerate with A and the data constrain the theory only weakly.")


if __name__ == "__main__":
    main()
