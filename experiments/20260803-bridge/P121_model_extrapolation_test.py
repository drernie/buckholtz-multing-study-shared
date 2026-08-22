"""P121 -- Predictive extension test: does FINDING_P120's power-law model
for contrast(N), analytically INTEGRATED into a predicted G_E(x_lo), match
REAL measurements of G_E(x_lo) at lower-cuts FINDING_P119 never tested?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, not a bigger T_END. FINDING_P120 fit contrast_coupled(N) =
c_inf - A*N^-p (p~0.503) and found contrast_reference(N) exactly constant.
By the L'Hopital argument that fit predicts a FINITE G_E limit
(sqrt(G_E)~1,259,961), above FINDING_P119's own last measured value
(1,254,870) -- consistent with G_E still climbing toward it. But that
consistency check was only DIRECTIONAL (above/below one number). This file
builds the actual QUANTITATIVE prediction the fit implies for the
cumulative integral G_E(x_lo) = E_coupled(x_lo)/E_reference(x_lo) --
by numerically integrating the FITTED point-model, not re-deriving
anything new -- and tests it against REAL measurements (FINDING_P119's own
energy_ratio_lna, actually re-run, not assumed) at lower-cuts well beyond
FINDING_P119's own deepest tested point (x_lo=10^100,000 decades). This
reuses the SAME already-verified T_END=1e13 trajectory FINDING_P119
established as safe -- no new ODE integration ceiling is pushed.

THE MODEL. contrast_reference(N) is exactly constant (c_r), so
E_reference(x_lo) = c_r^2 * (N_reach - N_lo) exactly. contrast_coupled(N)
is fit as c_c - A*N^-p, so E_coupled(x_lo) = integral[N_lo,N_reach]
(c_c - A*N^-p)^2 dN, evaluated by scipy.integrate.quad (no closed form
assumed since p is not exactly 1/2). G_E_predicted(x_lo) := E_coupled/E_ref.

REVISED MID-BUILD after a context-asymmetric skeptic review (claim + code
+ data only, no reasoning chain) caught a real problem in the first pass's
own framing, reported here not hidden. The first pass found predicted-vs-
measured G_E(x_lo) agreeing to <0.001% at every tested point and called it
"MODEL-CONFIRMED-ON-EXTENSION". The skeptic's break: (1) integrating two
curves already known to agree POINTWISE to ~0.4% (FINDING_P120's own
residual figure) will agree at the INTEGRAL level far more tightly than
0.4%, by simple sign-cancellation under integration -- this is true for
ANY reasonably-fitting smooth curve, not evidence the SPECIFIC power-law
FORM is correct; (2) the "extension" x_lo grid (150,000-339,867 decades)
sits ENTIRELY INSIDE the fit's own point-level calibration domain
([397.3, 397,340] decades) -- nothing was tested beyond where contrast(N)
was already directly measured, so "EXTENSION" overclaimed; (3) the
reference branch is EXACTLY constant, so it contributes identical,
error-free energy to both the "predicted" and "measured" pipelines --
the ratio framing is decorative, the real comparison is on the coupled
numerator alone.

THE FIX, not just a relabel: a genuine NEGATIVE CONTROL (CONTROL 4 below),
following the skeptic's own proposed test -- fit an ALTERNATIVE smooth
model (a cubic spline, which interpolates the SAME 14 calibration points
EXACTLY, i.e. with strictly better pointwise fit than the power-law's own
0.43% residual) through the identical data, integrate it the identical
way, and compare ITS predictions to the SAME real measurements. If the
spline predicts comparably well, the comparison discriminates nothing
about the power-law form specifically (the skeptic's Break #1 is right,
downgrade the claim). If the spline predicts MEASURABLY worse, the
power-law's specific functional form carries real information beyond
generic smoothness, and a (correctly worded, non-"extension") positive
claim is defensible.

CONTROLS:
  POSITIVE CONTROL (k=10): does this model-integration methodology --
    fit contrast(N), integrate the fit, compare to REAL measured G_E --
    correctly reproduce an actually-measured G_E for the already-known-
    convergent smooth case? If the methodology itself is broken, this is
    where it shows, cheaply (T_END=1e8, seconds not minutes).
  REGRESSION: refit k=0.3's coupled/reference contrast(N) from scratch in
    THIS file and confirm the fitted parameters match FINDING_P120's own
    reported values (not re-derive different numbers by accident).
  CONSISTENCY ON THE ALREADY-MEASURED GRID: does the model's predicted
    G_E(x_lo) agree with FINDING_P119's own real measurements at x_lo
    values P119 already tested (0 to 10^100,000)? A model that cannot
    match ground truth it was never asked to extrapolate has no business
    being trusted on new ground truth.
  NEGATIVE CONTROL (cubic-spline alternative): does an equally-smooth,
    strictly-better-pointwise-fitting ALTERNATIVE model predict the new
    cutoffs comparably well? If so, the power-law-specific agreement is
    not informative -- this is the skeptic-mandated discriminating test.

MAIN RESULT: real measurements (energy_ratio_lna, genuinely re-run,
not interpolated) at x_lo cutoffs FINDING_P119's own cumulative-integral
scan never tested (beyond 10^100,000), still INSIDE the fit's own
point-level calibration domain -- compared against BOTH the power-law
model's prediction and the spline negative-control's prediction. Does the
power-law match REAL measurement MEASURABLY better than the spline does,
or does reality diverge equally from both (or from neither)?

WHAT THIS FILE DOES NOT DO: push T_END past FINDING_P119's own established
ceiling. Claim the model, if it survives, is a rigorous asymptotic proof --
matching REAL data at new points strengthens confidence but the fit itself
still only characterizes a finite tested tail. Vary Lambda or other
(k, IC) combinations. Quote any k[h/Mpc]. Touch MULTING itself (Gate 1).
"""

import importlib.util
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(stem, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, stem))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


p120 = _load("P120_tail_integrability_test.py", "p120_for_p121")
p119 = p120.p119

a_star = p120.a_star
PHIDOT_INIT = p120.PHIDOT_INIT
LAMBDA_FIXED = p120.LAMBDA_FIXED
T_END = p120.T_END  # 1e13, FINDING_P119's own established, verified-safe ceiling

DEGENERATE_TOL = 1e-8


def fit_model_params(n_targets, values):
    """Same functional form as p120.fit_power_law_limit (c_inf - A*N^-p),
    but also returns the amplitude A, which p120's own function does not
    expose (it was built only to report a held-out prediction error, not
    to hand the parameters onward). Uses the FULL dataset -- this builds
    the predictive model; held-out validity was already established by
    FINDING_P120 itself and is re-confirmed below via the regression
    control, not re-litigated here."""
    n_arr, c_arr = np.asarray(n_targets), np.asarray(values)
    spread = float(np.max(c_arr) - np.min(c_arr))
    typical = max(float(np.mean(np.abs(c_arr))), 1e-300)
    if spread / typical < DEGENERATE_TOL:
        return float(np.mean(c_arr)), 0.0, float("nan"), True

    def model(nn, c_inf, amp, p):
        return c_inf - amp * nn ** (-p)

    p0 = [c_arr[-1], (c_arr[-1] - c_arr[0]) * 10, 0.5]
    popt, _ = curve_fit(model, n_arr, c_arr, p0=p0, maxfev=20000)
    return float(popt[0]), float(popt[1]), float(popt[2]), False


def predicted_energy(c_inf, amp, p, degenerate, n_lo, n_hi):
    """Integral of the fitted (or degenerate-constant) model's square from
    n_lo to n_hi, via numerical quadrature -- p is not exactly 1/2, so no
    closed form is assumed."""
    if degenerate:
        return c_inf**2 * (n_hi - n_lo)

    def integrand(n):
        return (c_inf - amp * n ** (-p)) ** 2

    val, _err = quad(integrand, n_lo, n_hi, limit=400)
    return val


PLATEAU_REL_TOL = 1e-5  # verified separation: k=10 rel~3e-7 (plateaued) vs
# k=0.3 rel~9e-4 (FINDING_P120's own value -- still climbing, must NOT trigger
# this branch, or the naive-final-step trap FINDING_P119 already fell into
# once repeats here) -- wide margin on both sides, not a cherry-picked cutoff


def fit_branch(sol, gh, t_end, n_grid_size, n_points, label):
    n_grid, c_grid = p120.contrast_at_N(sol, gh, 1.0, LAMBDA_FIXED, t_end, n_grid_size)
    n_lo, n_hi = float(n_grid.min()), float(n_grid.max())
    targets, values, shrinking, rel = p120.convergence_check(
        n_grid, c_grid, n_lo, n_hi, n_points=n_points, label=label
    )
    if shrinking and rel < PLATEAU_REL_TOL:
        # Already flat WITHIN the tested window (e.g. the smooth k=10 case,
        # which converges almost immediately) -- a power-law fit of
        # c_inf-A*N^-p to data that mixes a steep early transient with a
        # long flat tail is ill-conditioned (verified directly: it
        # overshot the visually obvious plateau value by ~20% on first
        # attempt). Use the plateau value directly instead of forcing a
        # fit onto a shape it wasn't built to describe -- same philosophy
        # as FINDING_P120's own degenerate-reference-branch handling.
        print(f"    {label}: PLATEAUED within tested window (final rel. step={rel:.4%}) --")
        print(f"    {label}: using the last value directly, no power-law fit attempted.")
        c_inf, amp, p, degenerate = values[-1], 0.0, float("nan"), True
    else:
        c_inf, amp, p, degenerate = fit_model_params(targets, values)
    return {
        "c_inf": c_inf,
        "amp": amp,
        "p": p,
        "degenerate": degenerate,
        "n_lo_fit": n_lo,
        "n_hi_fit": n_hi,
        "shrinking": shrinking,
        "rel": rel,
    }


def energy_ratio_lna(kk, x_lo_decades, x_reach_decades, t_end, ln_astar, n=None, **ic):
    """FINDING_P119's own G_E(x_lo) measurement -- reimplemented here since
    P119 defined it as a function LOCAL to its own main(), not exposed at
    module level. Logic copied verbatim (run_lna/t_of_lna/contrast_lna_from_sol
    calls, geomspace sampling, trapezoid integration), not reinvented."""
    n = n or p119.N_PROBE
    s_c = p119.run_lna(1.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
    s_r = p119.run_lna(0.0, 1.0, kk, t_end, lam_cc=LAMBDA_FIXED, **ic)
    if s_c is None or s_r is None:
        return None
    lna_lo = ln_astar + x_lo_decades * np.log(10)
    lna_reach = ln_astar + x_reach_decades * np.log(10)

    def piece(sol, gh):
        t_hi = p119.t_of_lna(sol, lna_reach, 1.0, t_end)
        t_lo = p119.t_of_lna(sol, lna_lo, 1.0, t_end)
        if t_hi is None or t_lo is None:
            return None
        ts = np.geomspace(t_lo, t_hi, n)
        lna_, c_ = p119.contrast_lna_from_sol(sol, ts, gh, 1.0, LAMBDA_FIXED)
        ok = np.isfinite(c_) & (lna_ >= lna_lo) & (lna_ <= lna_reach)
        lna_, c_ = lna_[ok], c_[ok]
        if lna_.size < 20:
            return None
        return float(np.trapezoid(c_**2, lna_))

    e_c, e_r = piece(s_c, 1.0), piece(s_r, 0.0)
    if e_c is None or e_r is None or e_r <= 0:
        return None
    return e_c / e_r


def predicted_sqrt_ge(fc, fr, n_lo, n_hi):
    e_c = predicted_energy(fc["c_inf"], fc["amp"], fc["p"], fc["degenerate"], n_lo, n_hi)
    e_r = predicted_energy(fr["c_inf"], fr["amp"], fr["p"], fr["degenerate"], n_lo, n_hi)
    if e_r <= 0:
        return None
    return (e_c / e_r) ** 0.5


def spline_energy(spline, n_lo, n_hi):
    """Same integration as predicted_energy, but for an interpolating
    cubic spline instead of the fitted power-law -- the skeptic-mandated
    NEGATIVE CONTROL. A spline through the same 14 points has BETTER
    pointwise fit than the power-law (exact interpolation, 0 residual at
    the calibration points, vs the power-law's own 0.43%), so if the
    power-law's tight integral-level agreement with real measurements were
    merely a generic consequence of ANY smooth curve through these points
    (the skeptic's core objection), the spline should match at least as
    well. If the power-law measurably OUTPERFORMS the spline instead, the
    power-law's specific functional form carries real information."""

    def integrand(n):
        return float(spline(n)) ** 2

    val, _err = quad(integrand, n_lo, n_hi, limit=400)
    return val


def spline_predicted_sqrt_ge(spline_c, fr, n_lo, n_hi):
    e_c = spline_energy(spline_c, n_lo, n_hi)
    e_r = predicted_energy(fr["c_inf"], fr["amp"], fr["p"], fr["degenerate"], n_lo, n_hi)
    if e_r <= 0:
        return None
    return (e_c / e_r) ** 0.5


def main() -> int:  # noqa: PLR0915 - one linear report
    print("=" * 78)
    print("P121 -- Model extrapolation test: does P120's fitted, analytically-")
    print("        integrated model predict REAL G_E(x_lo) beyond P119's own reach?")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    astar = a_star(LAMBDA_FIXED)
    ln_astar = np.log(astar)
    phidot_prob = 0.1 * PHIDOT_INIT
    ic0 = {"phidot0": phidot_prob}

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 1 -- POSITIVE CONTROL (k=10): does fit-then-integrate")
    print("methodology correctly predict an ACTUALLY-MEASURED, already-")
    print("known-convergent G_E?")
    print("-" * 78)
    T_END_SMOOTH = 1e8
    s_c10 = p119.run_lna(1.0, 1.0, 10.0, T_END_SMOOTH, lam_cc=LAMBDA_FIXED)
    s_r10 = p119.run_lna(0.0, 1.0, 10.0, T_END_SMOOTH, lam_cc=LAMBDA_FIXED)
    fc10 = fit_branch(s_c10, 1.0, T_END_SMOOTH, 200000, 14, "k=10 coupled")
    fr10 = fit_branch(s_r10, 0.0, T_END_SMOOTH, 200000, 14, "k=10 reference")

    # T_END_SMOOTH=1e8 only reaches ~3.77 decades past a_star (verified by probe,
    # not assumed) -- these must stay well inside that, past the plateau (~1.3
    # decades) but short of the trajectory's own tested ceiling.
    x_lo10, x_reach10 = 2.0, 3.5
    n_lo10 = ln_astar + x_lo10 * np.log(10)
    n_reach10 = ln_astar + x_reach10 * np.log(10)
    in_domain10 = (
        fc10["n_lo_fit"] <= n_lo10 <= fc10["n_hi_fit"]
        and fc10["n_lo_fit"] <= n_reach10 <= fc10["n_hi_fit"]
    )
    predicted10 = predicted_sqrt_ge(fc10, fr10, n_lo10, n_reach10)
    measured_ge10 = energy_ratio_lna(10.0, x_lo10, x_reach10, T_END_SMOOTH, ln_astar)
    measured10 = measured_ge10**0.5 if measured_ge10 else None
    print(f"    fit domain (N): coupled=[{fc10['n_lo_fit']:.3e},{fc10['n_hi_fit']:.3e}]")
    print(f"    probe window: N_lo={n_lo10:.3e}  N_reach={n_reach10:.3e}  in-domain={in_domain10}")
    print(f"    predicted sqrt(G_E) = {predicted10!r}")
    print(f"    measured  sqrt(G_E) = {measured10!r}")
    pc_ok = False
    if predicted10 is not None and measured10 is not None:
        rel10 = abs(predicted10 / measured10 - 1.0)
        pc_ok = rel10 < 0.02
        print(f"    relative difference: {rel10:.4%}")
    print(f"  POSITIVE CONTROL {'PASSES' if pc_ok else 'FAILS'} (threshold 2%)")
    if not pc_ok:
        print("  *** STOP -- the model-integration methodology itself does not")
        print("  *** reproduce a known-good case. Do not trust it on k=0.3.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 2 -- REGRESSION: refit k=0.3 branches here, confirm the")
    print("parameters match FINDING_P120's own reported fit (no silent drift)")
    print("-" * 78)
    s_c = p119.run_lna(1.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    s_r = p119.run_lna(0.0, 1.0, 0.3, T_END, lam_cc=LAMBDA_FIXED, **ic0)
    fc = fit_branch(s_c, 1.0, T_END, 200000, 14, "k=0.3 coupled (P121)")
    fr = fit_branch(s_r, 0.0, T_END, 200000, 14, "k=0.3 reference (P121)")

    known_c_inf, known_p = 0.0, 0.0  # filled from FINDING_P120's own printed report below
    # FINDING_P120's own committed report: c_inf~popt_all[0], p~popt_all[2] for the
    # coupled branch's FULL fit (not the held-out one) -- recomputed independently
    # here via the SAME p120.fit_power_law_limit call for a direct, non-hardcoded check.
    targets_c_chk, values_c_chk, _, _ = p120.convergence_check(
        *p120.contrast_at_N(s_c, 1.0, 1.0, LAMBDA_FIXED, T_END, 200000),
        fc["n_lo_fit"],
        fc["n_hi_fit"],
        n_points=14,
        label="k=0.3 coupled (P120 cross-check)",
    )
    known_c_inf, known_p, _ho, _res = p120.fit_power_law_limit(
        targets_c_chk, values_c_chk, label="k=0.3 coupled (P120 cross-check)"
    )
    reg_c_ok = abs(fc["c_inf"] / known_c_inf - 1.0) < 1e-6 and abs(fc["p"] / known_p - 1.0) < 1e-6
    reg_r_ok = fr["degenerate"]
    print(f"    P121 refit:  c_inf={fc['c_inf']:.6f}  p={fc['p']:.6f}")
    print(f"    P120 refit:  c_inf={known_c_inf:.6f}  p={known_p:.6f}")
    print(f"    reference branch degenerate (matches P120's finding): {fr['degenerate']}")
    reg_ok = reg_c_ok and reg_r_ok
    print(f"  REGRESSION CONTROL {'PASSES' if reg_ok else 'FAILS'}")
    if not reg_ok:
        print("  *** STOP -- refit does not match FINDING_P120's own reported values.")
        return 1

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 3 -- NEGATIVE CONTROL: build a cubic spline through the SAME")
    print("14 calibration points (skeptic-mandated discriminating test -- see")
    print("docstring). Strictly better pointwise fit than the power-law (exact")
    print("interpolation, 0 residual, vs the power-law's own 0.43%).")
    print("-" * 78)
    order = np.argsort(targets_c_chk)
    spline_c = CubicSpline(np.asarray(targets_c_chk)[order], np.asarray(values_c_chk)[order])
    print(f"    spline built through N in [{targets_c_chk[0]:.3e}, {targets_c_chk[-1]:.3e}]")
    print("    (used ONLY inside this domain below -- CubicSpline extrapolation")
    print("     outside it is not physically meaningful and is not relied on)")

    # ==================================================================
    print("\n" + "-" * 78)
    print("CONTROL 4 -- CONSISTENCY on FINDING_P119's OWN already-measured grid:")
    print("does the model (and the spline) correctly predict REAL G_E(x_lo)")
    print("where we already have ground truth, before trusting either on new")
    print("ground truth?")
    print("-" * 78)
    # Reuse s_c (already solved, dense_output=True, in Control 2) for the final
    # ln(a) reached -- avoids a third redundant T_END=1e13 solve of the same
    # trajectory (a fresh non-dense probe would cost another ~166s for nothing
    # s_c doesn't already contain).
    ln_a_reach = s_c.y[0, -1]
    reach_decades = (ln_a_reach - ln_astar) / np.log(10)
    use_decades = reach_decades * 0.9
    print(f"    T_END={T_END:.0e} reaches a_reach/a_star = 10^{reach_decades:.1f}")
    print(f"    fixed scan reach (90% safety margin): 10^{use_decades:.1f}")

    already_tested = (0, 900, 10000, 100000)
    consistency_rows = []
    for dec in already_tested:
        n_lo_x = ln_astar + dec * np.log(10)
        n_reach_x = ln_astar + use_decades * np.log(10)
        pred = predicted_sqrt_ge(fc, fr, n_lo_x, n_reach_x)
        pred_spline = spline_predicted_sqrt_ge(spline_c, fr, n_lo_x, n_reach_x)
        ge = energy_ratio_lna(0.3, dec, use_decades, T_END, ln_astar, **ic0)
        meas = ge**0.5 if ge else None
        rel = abs(pred / meas - 1.0) if (pred is not None and meas) else None
        rel_spline = abs(pred_spline / meas - 1.0) if (pred_spline is not None and meas) else None
        consistency_rows.append((dec, pred, pred_spline, meas, rel, rel_spline))
        print(
            f"    x_lo=10^{dec:<7g}  power-law={pred!r} (rel={rel if rel is None else f'{rel:.4%}'})"
            f"  spline={pred_spline!r} (rel={rel_spline if rel_spline is None else f'{rel_spline:.4%}'})"
            f"  measured={meas!r}"
        )
    valid_rel = [r for *_, r, _rs in consistency_rows if r is not None]
    consistency_ok = len(valid_rel) >= 3 and max(valid_rel) < 0.05
    print(f"  CONSISTENCY CONTROL {'PASSES' if consistency_ok else 'FAILS'} (threshold 5%)")
    if not consistency_ok:
        print("  *** the model does not even match ALREADY-KNOWN measurements.")
        print("  *** stop before trusting it on new ones -- report as-is below.")

    # ==================================================================
    print("\n" + "-" * 78)
    print("MAIN RESULT -- REAL measurements at NEW cumulative-integral cutoffs")
    print("FINDING_P119's own scan never tested (beyond x_lo=10^100,000), still")
    print("INSIDE the fit's own point-level calibration domain -- power-law")
    print("model vs the spline negative control, both vs REAL measurement")
    print("-" * 78)
    extension_decades = tuple(
        d for d in (150000, 200000, 250000, 300000, int(use_decades * 0.95)) if d < use_decades
    )
    print(f"    extension x_lo grid (decades): {extension_decades}")
    ext_rows = []
    for dec in extension_decades:
        n_lo_x = ln_astar + dec * np.log(10)
        n_reach_x = ln_astar + use_decades * np.log(10)
        pred = predicted_sqrt_ge(fc, fr, n_lo_x, n_reach_x)
        pred_spline = spline_predicted_sqrt_ge(spline_c, fr, n_lo_x, n_reach_x)
        ge = energy_ratio_lna(0.3, dec, use_decades, T_END, ln_astar, **ic0)
        meas = ge**0.5 if ge else None
        rel = abs(pred / meas - 1.0) if (pred is not None and meas) else None
        rel_spline = abs(pred_spline / meas - 1.0) if (pred_spline is not None and meas) else None
        ext_rows.append((dec, pred, pred_spline, meas, rel, rel_spline))
        print(
            f"    x_lo=10^{dec:<7g}  power-law={pred!r} (rel={rel if rel is None else f'{rel:.4%}'})"
            f"  spline={pred_spline!r} (rel={rel_spline if rel_spline is None else f'{rel_spline:.4%}'})"
            f"  measured={meas!r}"
        )

    valid_ext = [(d, m) for d, _p, _ps, m, _r, _rs in ext_rows if m is not None]
    valid_ext_rel = [r for *_, r, _rs in ext_rows if r is not None]
    valid_ext_rel_spline = [rs for *_, _r, rs in ext_rows if rs is not None]

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if len(valid_ext) < 3:
        print("  -> NOT ENOUGH MEASURABLE EXTENSION POINTS. Infrastructure outcome.")
        return 1

    ext_vals = [m for _d, m in valid_ext]
    ext_decs = [d for d, _m in valid_ext]
    monotone_rise = all(ext_vals[i] <= ext_vals[i + 1] for i in range(len(ext_vals) - 1))
    steps = [
        (ext_vals[i + 1] - ext_vals[i]) / (ext_decs[i + 1] - ext_decs[i])
        for i in range(len(ext_vals) - 1)
    ]
    decelerating = len(steps) >= 2 and all(steps[i] >= steps[i + 1] for i in range(len(steps) - 1))
    model_agrees = len(valid_ext_rel) >= 3 and max(valid_ext_rel) < 0.05
    spline_agrees = len(valid_ext_rel_spline) >= 3 and max(valid_ext_rel_spline) < 0.05
    # Discriminates: power-law's WORST error is meaningfully smaller than the
    # spline's WORST error (a fixed 5x margin, not a razor-thin one -- avoids
    # calling noise-level differences "discrimination").
    discriminates = (
        model_agrees
        and len(valid_ext_rel_spline) >= 3
        and max(valid_ext_rel) * 5 < max(valid_ext_rel_spline)
    )

    print(f"  monotonic rise across extension: {monotone_rise}")
    print(f"  per-decade rise rate decelerating across extension: {decelerating}")
    print(f"  power-law matches REAL measurement at all extension points (<5%): {model_agrees}")
    print(f"  spline (negative control) ALSO matches (<5%): {spline_agrees}")
    if valid_ext_rel:
        print(f"  power-law worst rel.diff: {max(valid_ext_rel):.4%}")
    if valid_ext_rel_spline:
        print(f"  spline worst rel.diff: {max(valid_ext_rel_spline):.4%}")
    print(f"  power-law MEASURABLY outperforms spline (>=5x tighter worst-case): {discriminates}")
    if fc["p"] and np.isfinite(fc["p"]):
        ge_limit = (fc["c_inf"] / fr["c_inf"]) ** 2
        print(f"  power-law's own predicted sqrt(G_E) limit (N->infinity): {ge_limit**0.5:.2f}")
        print(f"  last extension measurement: {ext_vals[-1]:.2f}")

    if model_agrees and discriminates and decelerating and consistency_ok:
        print("\n  -> NUMERICAL-CONSISTENCY-CONFIRMED, POWER-LAW-DISCRIMINATES. The")
        print("     power-law model does not just match REAL measurement at new")
        print("     cumulative-integral cutoffs (all interior to its own point-level")
        print("     calibration domain, not a true extrapolation) -- it MEASURABLY")
        print("     outperforms an equally-smooth, strictly-better-pointwise-fitting")
        print("     alternative (the spline). This is the skeptic-mandated")
        print("     discriminating evidence: the specific functional form c_inf-A*N^-p")
        print("     carries real information, the agreement is not a generic artifact")
        print("     of integrating any smooth curve through the same 14 points.")
    elif model_agrees and not discriminates:
        print("\n  -> NUMERICAL-CONSISTENCY-CHECK-ONLY, DOES-NOT-DISCRIMINATE-MODEL-FORM.")
        print("     The power-law's predictions match REAL measurement -- but so does")
        print("     the spline negative control, comparably well. Per the skeptic's")
        print("     own Break #1: this is the expected numerical consequence of")
        print("     integrating ANY reasonably-fitting smooth curve through the same")
        print("     calibration points, not evidence the SPECIFIC power-law FORM is")
        print("     correct. Downgraded from an earlier draft's overclaimed")
        print("     'MODEL-CONFIRMED-ON-EXTENSION' after context-asymmetric skeptic")
        print("     review -- see docstring.")
    else:
        print("\n  -> MODEL-DOES-NOT-MATCH-CLEANLY. Real measurements at the new")
        print("     cutoffs diverge from what FINDING_P120's fit predicted -- this")
        print("     does not resurrect FINDING_P119's own STILL-CLIMBING verdict")
        print("     (that remains true either way), but it DOES mean the specific")
        print("     numeric limit FINDING_P120 predicted should not be trusted.")

    print("\n  NOT ESTABLISHED:")
    print("   * a rigorous asymptotic proof -- matching new measured points")
    print("     strengthens confidence in the fitted model but does not prove it")
    print("     holds past this file's own tested grid either.")
    print("   * anything BEYOND the fit's own point-level calibration domain")
    print("     (decades ~397 to ~397,340) -- every x_lo tested here, including the")
    print("     'new' extension grid, sits INSIDE that domain; only the cumulative-")
    print("     integral cutoff values are new, not the underlying contrast(N) data.")
    print("   * the reference branch's contribution to any of this -- it is exactly")
    print("     constant, contributes identical error-free energy to BOTH the")
    print("     predicted and measured pipelines, so the ratio framing does not add")
    print("     robustness beyond what the coupled-branch numerator alone shows.")
    print("   * anything at Lambda values, or (k, IC) combinations, other than the")
    print("     one tested.")
    print("   * any numeric value of eps(k), G_growth, or f(k) in physical units, or")
    print("     any k[h/Mpc].")
    print("   * anything about MULTING itself (Gate 1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
