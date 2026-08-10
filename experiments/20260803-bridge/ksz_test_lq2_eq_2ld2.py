"""Test the R7 covariant-completion prediction l_q^2 = 2 l_d^2 against real data.

NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
2026-08-10 · closes the "carry it to a test" step for FINDING_R7_collapses_to_one_action.md

WHAT IS BEING TESTED, AND WHAT IT IS BEING TESTED AGAINST.
The R7 action fixes the quadrupole length scale in terms of the dipole one:
l_q^2 = 2 l_d^2, with no free parameter left over once l_d is set. The pairwise
kSZ likelihood in experiments/20260802-ksz-force-law constrains exactly those two
quantities directly from data -- l_d = A3/A2 [Mpc] and l_q2 = A4/A2 [Mpc^2] --
and it already builds the K_4 kernel the quadrupole needs. It never scanned it:
every fit there was one-dimensional in l_d, with l_q2 held at zero. So the test
is one grid away and needs no new data, no new kernel, and no beta_d/beta_q
conversion (which is assumption-laden and is deliberately not used here).

WHY NOT TEST AGAINST beta_d = 4.5, beta_q = 18.0. Those are Table A1's values.
They were FITTED by an online AI service to the observed H(z) -- the prompt in
data/beta1_responses/prompt_v1.md says so in its own words -- so using them as a
validation target would test the fitting procedure, not the theory (Gate 2). The
kSZ data are independent of both.

CONTROL. The parent module's shell-theorem check, C_2(rho) == 1 identically, is
re-run here before anything else and is a hard stop. It is a control with an
independently known answer: if the geometry is wrong it fails, and no number
below may then be believed. This is the only reason the K_4 kernel -- which has
no such closed-form check of its own -- is trusted at all.
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
R7_SLOPE = 2.0  # the prediction: l_q2 = R7_SLOPE * l_d^2


def main() -> None:
    print("=" * 78)
    print("R7 PREDICTION l_q^2 = 2 l_d^2  vs  pairwise-kSZ (ACT DR6 + arXiv:2604.14327)")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION  |  L0: descriptive")
    print("=" * 78)

    # ---- CONTROL FIRST: shell theorem, known answer, hard stop -------------
    rhos = [1e-6, 0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999]
    c2_err = max(abs(c_shell(float(x), 2) - 1.0) for x in rhos)
    print(f"\n[CONTROL] shell theorem C_2(rho) == 1 : max error {c2_err:.3e}")
    if c2_err > 1e-8:
        print("  *** CONTROL FAILED - geometry wrong. Nothing below is believable. STOP. ***")
        return
    print("  -> passed to machine precision; K_3 and K_4 geometry trusted.")

    # ---- data --------------------------------------------------------------
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
    print(f"  bins: {m.sum()} of {len(r_all)},  r = {r.min():.1f}-{r.max():.1f} Mpc")

    k2, k3, k4 = (build_kernel(r, xi_interp, k) for k in (2, 3, 4))

    # ---- 2D scan, amplitude profiled analytically --------------------------
    ld_grid = np.linspace(-60.0, 60.0, 481)
    lq_grid = np.linspace(-3000.0, 6000.0, 601)
    chi2 = np.empty((len(ld_grid), len(lq_grid)))
    for i, ld in enumerate(ld_grid):
        base = k2 - ld * k3
        for j, lq in enumerate(lq_grid):
            chi2[i, j] = profile_chi2(pobs, cinv, -(base + lq * k4))[0]
    i0, j0 = np.unravel_index(np.argmin(chi2), chi2.shape)
    chi2_min = chi2[i0, j0]
    ld_hat, lq_hat = ld_grid[i0], lq_grid[j0]

    chi2_null = profile_chi2(pobs, cinv, -k2)[0]  # pure Newtonian monopole
    print("\n[2D FIT]  free (l_d, l_q2), amplitude profiled")
    print(f"  best fit      : l_d = {ld_hat:+.2f} Mpc,  l_q2 = {lq_hat:+.1f} Mpc^2")
    print(
        f"  chi2_min      = {chi2_min:.3f}   (Newtonian-only chi2 = {chi2_null:.3f},"
        f" delta = {chi2_null - chi2_min:.3f} for 2 extra dof)"
    )
    if lq_hat > 0 and ld_hat != 0:
        print(
            f"  implied ratio : l_q2 / l_d^2 = {lq_hat / ld_hat**2:+.3f}   (R7 predicts {R7_SLOPE})"
        )

    # ---- the actual test: is the R7 line inside the allowed region? ---------
    # Along l_q2 = 2 l_d^2 the model has ONE free parameter (l_d), so the
    # comparison against the 2-parameter best fit costs 1 dof.
    ld_line = np.linspace(-60.0, 60.0, 4801)
    chi2_line = np.array(
        [profile_chi2(pobs, cinv, -(k2 - ld * k3 + R7_SLOPE * ld**2 * k4))[0] for ld in ld_line]
    )
    kk = int(np.argmin(chi2_line))
    d_chi2 = chi2_line[kk] - chi2_min
    ok = ld_line[chi2_line <= chi2_line[kk] + 3.84]

    print("\n[TEST] restricting to the R7 one-parameter family l_q2 = 2 l_d^2")
    print(
        f"  best l_d on the line : {ld_line[kk]:+.3f} Mpc  -> l_q2 = {R7_SLOPE * ld_line[kk] ** 2:.2f} Mpc^2"
    )
    print(f"  chi2 on line         = {chi2_line[kk]:.3f}")
    print(f"  delta chi2 vs free 2D= {d_chi2:.3f}   (1 dof: 3.84 = 95%, 6.63 = 99%)")
    print(f"  95% CI on l_d along the R7 line: [{ok.min():+.2f}, {ok.max():+.2f}] Mpc")
    verdict = (
        "NOT EXCLUDED at 95%"
        if d_chi2 <= 3.84
        else "excluded at 95% but not 99%"
        if d_chi2 <= 6.63
        else "EXCLUDED at 99%"
    )
    print(f"  -> the R7 constraint is {verdict}.")

    # ---- how much does the data actually say about the ratio? --------------
    # If the free 2D fit is itself consistent with l_q2 = 0, then the test above
    # is passed by a model that is simply not being probed -- report that.
    chi2_ld_only = float(min(profile_chi2(pobs, cinv, -(k2 - ld * k3))[0] for ld in ld_line))
    print("\n[DISCRIMINATION CHECK] what is the data able to distinguish?")
    print(f"  chi2 (l_q2 = 0, l_d free)     = {chi2_ld_only:.3f}")
    print(f"  chi2 (2D free)                = {chi2_min:.3f}")
    print(
        f"  delta                         = {chi2_ld_only - chi2_min:.3f}"
        "   <- if small, l_q2 is unconstrained and the test above is vacuous"
    )
    slopes = [0.0, 0.5, 1.0, R7_SLOPE, 4.0, 10.0]
    print(
        f"\n  chi2 along l_q2 = s * l_d^2 for several s (s={R7_SLOPE} is R7,"
        " s=4 is the AI-fitted beta ratio):"
    )
    for s in slopes:
        c = float(
            min(profile_chi2(pobs, cinv, -(k2 - ld * k3 + s * ld**2 * k4))[0] for ld in ld_line)
        )
        print(f"    s = {s:>5.1f} : chi2_min = {c:8.3f}   delta vs 2D free = {c - chi2_min:6.3f}")


if __name__ == "__main__":
    main()
