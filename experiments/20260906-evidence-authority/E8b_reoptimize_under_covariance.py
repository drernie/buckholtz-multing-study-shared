"""E8b -- NOT pre-registered; added after E8's Endpoint 1 showed the sign of
dchi2(free LCDM - MULTING spotlighted) flipping under Moresco's covariance.

E8 compared the two models at the parameter values each was optimised to
under DIAGONAL errors. That is not a fair comparison under a different error
model: each side should be re-optimised under the covariance it is being
scored with. This file does that, for both:

  * flat LCDM, 2 free params (H0, Om)         -- well-conditioned, Nelder-Mead
  * MULTING,   3 free params (H0anchor,b1,b2) -- the (b1,b2) valley is the
    whole P176 finding, so the optimiser is started at TJB's own spotlighted
    values and run with a tight tolerance; convergence is checked by
    restarting from two other Table II rows and requiring agreement.

Reported per variant: best chi2 for each model, and dchi2 = LCDM - MULTING.
A positive dchi2 means MULTING fits better. This file makes no claim about
which model is "right" -- a |dchi2| of order 1 on ~30 dof is not evidence for
either; the question is only whether the sign and size E8 found survive
re-optimisation.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

from E8_full_covariance_propagation import (
    LCDM_FIXED,
    LCDM_FREE,
    TABLE_II,
    build_cov_cc,
    chi2_fixed_h0anchor,
    chi2_lcdm_cov,
    chi2_lcdm_diag,
    embed_33,
    fetch_mm20,
    make_chi2_cov,
    moresco_mask,
)
from scipy.optimize import minimize


def opt_lcdm(chi2_fn, x0=(70.0, 0.3)):
    res = minimize(
        lambda p: chi2_fn(p[0], p[1]),
        x0,
        method="Nelder-Mead",
        options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 4000},
    )
    return res.fun, res.x


def opt_multing(chi2_fn, x0):
    """Optimise in rescaled coordinates (P176's own convention: raw b1~1e10,
    b2~1e17 differ by 7 orders; unrescaled Nelder-Mead is meaningless)."""
    h0, b1, b2 = x0

    def f(p):
        return chi2_fn(p[0], p[1] * b1, p[2] * b2)

    res = minimize(
        f,
        (h0, 1.0, 1.0),
        method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-9, "maxiter": 20000},
    )
    return res.fun, (res.x[0], res.x[1] * b1, res.x[2] * b2)


if __name__ == "__main__":
    mm20 = fetch_mm20()
    mask = moresco_mask()

    # Positive control: re-optimising under DIAGONAL must recover TJB's own
    # reported optima (free LCDM 16.31 at H0=71.83, Om=0.2724; MULTING 15.75).
    f_l, x_l = opt_lcdm(chi2_lcdm_diag)
    f_m, x_m = opt_multing(chi2_fixed_h0anchor, TABLE_II["unconstrained_spotlighted"][:3])
    assert abs(f_l - LCDM_FREE["chi2_tjb"]) / LCDM_FREE["chi2_tjb"] < 5e-3, f_l
    assert abs(x_l[0] - LCDM_FREE["H0"]) < 0.1 and abs(x_l[1] - LCDM_FREE["Om"]) < 0.005, x_l
    # WHY two separate bounds: TJB reports chi2 to 2 decimals (15.75), so the
    # exact value at his own parameters is anywhere in [15.745, 15.755). The
    # first run of this control failed at 15.7515 against a +1e-3 tolerance --
    # a rounding artefact, not an optimiser failure. So: (i) the optimiser must
    # not do WORSE than the exact chi2 at its own starting point (a real
    # monotonicity check), and (ii) the result must sit within half a unit of
    # TJB's last printed digit.
    start_chi2 = chi2_fixed_h0anchor(*TABLE_II["unconstrained_spotlighted"][:3])
    assert f_m <= start_chi2 + 1e-6, (f_m, start_chi2)
    assert abs(f_m - TABLE_II["unconstrained_spotlighted"][3]) <= 0.005 + 1e-6, f_m
    print(
        f"PC diag re-opt: LCDM {f_l:.3f} @ H0={x_l[0]:.2f} Om={x_l[1]:.4f} (TJB 16.31 @ 71.83/0.2724): PASS"
    )
    print(
        f"PC diag re-opt: MULTING {f_m:.4f} (start {start_chi2:.4f}; TJB prints 15.75; "
        f"not worse than start, within rounding): PASS\n"
    )

    variants = {
        "diag (as everyone uses)": None,
        "Moresco default [spsooo+imf], all 31 corr": (["spsooo", "imf"], None),
        "Moresco default, only his 15 corr": (["spsooo", "imf"], mask),
        "stress [sps+imf], all 31 corr": (["sps", "imf"], None),
    }

    print("=" * 100)
    print(
        f"{'variant':<44} {'LCDM*':>8} {'H0':>6} {'Om':>7}  {'MULT*':>8} {'H0a':>6}  {'dchi2':>7} {'conv':>5}"
    )
    print("=" * 100)
    for vname, spec in variants.items():
        if spec is None:
            cl = chi2_lcdm_diag
            cm = chi2_fixed_h0anchor
        else:
            C33 = embed_33(build_cov_cc(mm20, *spec))
            cl = lambda H0, Om, C=C33: chi2_lcdm_cov(H0, Om, C)  # noqa: E731
            cm = make_chi2_cov(C33)

        fl, xl = opt_lcdm(cl, x0=(LCDM_FREE["H0"], LCDM_FREE["Om"]))

        # MULTING: start from three Table II rows; require the best two to agree
        starts = ["unconstrained_spotlighted", "pct_50", "planck_exact_100pct"]
        outs = sorted(opt_multing(cm, TABLE_II[s][:3]) for s in starts)
        fm, xm = outs[0]
        conv = "ok" if abs(outs[1][0] - outs[0][0]) < 0.05 else "WARN"

        print(
            f"{vname:<44} {fl:8.3f} {xl[0]:6.2f} {xl[1]:7.4f}  {fm:8.3f} {xm[0]:6.2f}  {fl - fm:+7.3f} {conv:>5}"
        )

    print(
        "\n(dchi2 > 0: MULTING fits better; < 0: free LCDM fits better. |dchi2| ~ 1 on ~30 dof is not"
    )
    print(
        " evidence for either model -- the question is only whether E8's sign flip survives re-optimisation.)"
    )
    print(
        f"\nFor reference, fixed Planck LCDM (not re-optimised): diag {chi2_lcdm_diag(LCDM_FIXED['H0'], LCDM_FIXED['Om']):.2f}"
    )
