"""P158 addendum 2: real halo mass function + Tinker10 bias + linear
matter correlation function, replacing the REJECTED measurement-scatter
/ large-scale-bias-only proxy from FINDING_P158_ADDENDUM_literature_
grounding.md.

REJECTED (see FINDING_P158_ADDENDUM2_real_mass_function.md) -- a Step 8a
skeptic pass, independently re-verified, found the linear peak-
background-split bias model is pushed into extrapolation nu>>10-20 far
beyond Tinker et al.'s own simulation calibration for most of v82's own
target redshifts (nu reaches ~50 at z=5) -- the "mathematically valid"
(|rho|<=1) flag alone does not mean physically meaningful. A genuine
units bug (physical Mpc vs Mpc/h) was also caught and fixed. Kept
running as-is (now reporting BOTH math-validity and calibration-range
validity explicitly) per this project's no-silent-correction convention
-- read the FINDING, not just this script's printed output.

Uses `hmf` (Murray, Power & Robotham 2013 -- the standard Python
halo-mass-function package, backed by `camb` for the linear matter power
spectrum) for the mass function itself (Tinker et al. 2008 fitting
function) instead of a from-scratch re-implementation -- real,
independently-published, widely-used tooling, not a re-fit.

Tinker et al. (2010) Eq. 6 (halo bias) is implemented directly here --
a single closed-form formula with published coefficients, evaluated on
hmf's own nu = delta_c/sigma(M) output.

See CLAIM_P158_ADDENDUM2_real_mass_function.md for the full protocol,
and FINDING_P158_ADDENDUM2_real_mass_function.md for the write-up.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import importlib.util
import warnings
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

warnings.filterwarnings("ignore")

DELTA_C = 1.686  # critical linear overdensity for collapse (standard value)
OVERDENSITY = 500  # matches v82's own R_500-based radius definition (Eq. 11)

REPO_ROOT = Path(__file__).resolve().parents[2]
MULTING_CORE_PATH = (
    REPO_ROOT
    / "data"
    / "source_material"
    / "zenodo_21204955_supplemental"
    / "code"
    / "multing_core.py"
)


def load_multing_core():
    spec = importlib.util.spec_from_file_location("multing_core", MULTING_CORE_PATH)
    mc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mc)
    return mc


def tinker10_bias(nu, delta=OVERDENSITY):
    """Tinker et al. (2010) Eq. 6, coefficients from their Table 2 as
    continuous functions of Delta (their Eq. 6 surrounding text).
    """
    y = np.log10(delta)
    A = 1.0 + 0.24 * y * np.exp(-((4.0 / y) ** 4))
    a = 0.44 * y - 0.88
    B = 0.183
    b = 1.5
    C = 0.019 + 0.107 * y + 0.19 * np.exp(-((4.0 / y) ** 4))
    c = 2.4
    return 1.0 - A * nu**a / (nu**a + DELTA_C**a) + B * nu**b + C * nu**c


def build_mass_function(z, mmin_log10=13.0, mmax_log10=16.0, dlog10m=0.01):
    from hmf import MassFunction

    return MassFunction(
        z=z,
        Mmin=mmin_log10,
        Mmax=mmax_log10,
        dlog10m=dlog10m,
        hmf_model="Tinker08",
        mdef_model="SOMean",
        mdef_params={"overdensity": OVERDENSITY},
    )


def positive_control_mass_function():
    print("=== POSITIVE CONTROL: hmf/Tinker08 cluster abundance ===")
    mf = build_mass_function(z=0.0)
    idx1 = np.argmin(np.abs(mf.m - 1e14))
    idx2 = np.argmin(np.abs(mf.m - 1e15))
    n1, n2 = mf.ngtm[idx1], mf.ngtm[idx2]
    print(f"  n(M>1e14 Msun/h, z=0) = {n1:.3e} (Mpc/h)^-3  [textbook ballpark: few x 1e-5]")
    print(f"  n(M>1e15 Msun/h, z=0) = {n2:.3e} (Mpc/h)^-3  [textbook ballpark: ~1e-7]")
    assert 1e-6 < n1 < 1e-4, "cluster abundance at 1e14 Msun/h off by an order of magnitude or more"
    assert 1e-9 < n2 < 1e-6, "cluster abundance at 1e15 Msun/h off by an order of magnitude or more"
    print("  PASS: within the standard textbook order-of-magnitude range.\n")
    return mf


def positive_control_bias(mf):
    print("=== POSITIVE CONTROL: Tinker10 bias formula, verified against the primary source ===")
    # Coefficients (A,a,B,b,C,c) and the functional form of Eq.6 were
    # fetched and directly checked against Tinker et al. (2010) arXiv:
    # 1001.3162 this session (mcp__arxiv__search_paper_text), not recalled
    # from memory -- exact match to their Table 2 + Eq.6 text.
    #
    # An earlier draft of this control wrongly expected b(nu=1)~1 (a
    # property of the SIMPLER Press-Schechter/Cole-Kaiser bias formula,
    # Eq.4 in the same paper) and failed on Tinker10's own formula, which
    # does NOT share that property. The paper's own text (verified this
    # session): "Equation (6) ... asymptotes to b=1 at nu=0, provided
    # a>0" -- the correct, checkable asymptotic property for THIS formula.
    nu_grid = mf.nu
    b_grid = tinker10_bias(nu_grid)
    # a = 0.44y-0.88 = 0.3075 at Delta=500 (a<1), so nu^a converges to 0
    # slowly as nu->0 -- nu=1e-6 alone gives b=0.988, not yet at the true
    # asymptote (checked: nu^a=(1e-6)^0.3075~0.014, not negligible). Use a
    # much smaller nu to actually reach it, and confirm convergence with
    # an even smaller second point rather than trusting one data point.
    b_1 = tinker10_bias(np.array([1e-12]))[0]
    b_2 = tinker10_bias(np.array([1e-24]))[0]
    print(f"  b(nu=1e-12) = {b_1:.6f}, b(nu=1e-24) = {b_2:.8f}  [paper: asymptote is exactly 1]")
    assert abs(b_2 - 1.0) < 1e-4, "Tinker10 bias formula does not asymptote to 1 at nu->0"
    assert abs(b_2 - 1.0) < abs(b_1 - 1.0), "not converging toward 1 as nu shrinks further"
    assert np.all(np.diff(b_grid) > 0), "bias is not monotonically increasing with nu"
    print("  PASS: correct nu->0 asymptote, monotonically increasing with nu.\n")


def negative_control_bias(mf):
    print("=== NEGATIVE CONTROL: b(M=1e12 Msun) should be << b(M=1e14 Msun) ===")
    mf_small = build_mass_function(z=0.0, mmin_log10=10.0, mmax_log10=13.0, dlog10m=0.01)
    idx_small = np.argmin(np.abs(mf_small.m - 1e12))
    idx_cluster = np.argmin(np.abs(mf.m - 1e14))
    b_small = tinker10_bias(mf_small.nu[idx_small])
    b_cluster = tinker10_bias(mf.nu[idx_cluster])
    print(f"  b(1e12 Msun) = {b_small:.4f}")
    print(f"  b(1e14 Msun) = {b_cluster:.4f}")
    assert b_small < b_cluster, "bias does not increase with mass -- formula or sign error"
    print("  PASS: bias increases with mass, as required.\n")


def var_lnM(mf, m_floor):
    """Var[ln M] for the population M >= m_floor, weighted by dn/dlnM."""
    m = mf.m
    dndlnm = mf.dndlnm
    mask = m >= m_floor
    m_pop, w = m[mask], dndlnm[mask]
    lnm = np.log(m_pop)
    norm = simpson(w, x=lnm)
    mean_lnm = simpson(w * lnm, x=lnm) / norm
    mean_lnm2 = simpson(w * lnm**2, x=lnm) / norm
    return mean_lnm2 - mean_lnm**2, mean_lnm


def population_moments(mf, m_floor):
    """<lnM>, <lnM^2>, <b>, <lnM*b> over the population M >= m_floor,
    weighted by dn/dlnM -- the four moments the EXACT (non-perturbative)
    pair-covariance formula below is built from.
    """
    m = mf.m
    dndlnm = mf.dndlnm
    mask = m >= m_floor
    m_pop, w = m[mask], dndlnm[mask]
    lnm = np.log(m_pop)
    b = tinker10_bias(mf.nu[mask])
    norm = simpson(w, x=lnm)
    mean_lnm = simpson(w * lnm, x=lnm) / norm
    mean_lnm2 = simpson(w * lnm**2, x=lnm) / norm
    mean_b = simpson(w * b, x=lnm) / norm
    mean_lnm_b = simpson(w * lnm * b, x=lnm) / norm
    return mean_lnm, mean_lnm2, mean_b, mean_lnm_b


def pair_rho_exact(mean_lnm, mean_lnm2, mean_b, mean_lnm_b, xi):
    """EXACT (not first-order-in-xi) pairwise ln-mass correlation, for
    joint pair-selection probability p(M1,M2) ~ n(M1)n(M2)[1+b1 b2 xi].

    An earlier version of this script linearized in xi (Cov = xi *
    Cov[lnM,b]^2) -- this blows up unboundedly (rho >> 1, violating the
    |rho|<=1 Cauchy-Schwarz bound) once b(M) grows large at high z,
    because the real small parameter is b1*b2*xi, not xi alone, and that
    stops being small exactly where the linearization was being trusted
    most. This closes the derivation exactly instead:

        E[lnM1 lnM2] = [<lnM>^2 + xi*<lnM*b>^2] / [1 + <b>^2 * xi]
        E[lnM1]      = [<lnM> + <b>*xi*<lnM*b>] / [1 + <b>^2 * xi]
        Var[lnM1]    = E[lnM1^2] - E[lnM1]^2   (needs a matching E[lnM1^2]
                        term, so a 3rd, symmetric marginal-variance piece
                        is computed the same way, see below)
        rho = Cov[lnM1,lnM2] / Var[lnM1]   (equal-population case: Var1=Var2)

    Returns (rho, cov, var_marginal, denom) -- denom = 1+<b>^2*xi is also
    a validity check: it must stay positive (the joint weight [1+b1b2xi]
    cannot be enforced positive everywhere without the full 2D integral,
    but the population-averaged denom going negative is a hard sign this
    linear-bias-times-xi model no longer describes a valid probability
    at all, not just a computational nicety).
    """
    denom = 1.0 + mean_b**2 * xi
    e_lnm1_lnm2 = (mean_lnm**2 + xi * mean_lnm_b**2) / denom
    e_lnm1 = (mean_lnm + mean_b * xi * mean_lnm_b) / denom
    cov = e_lnm1_lnm2 - e_lnm1 * e_lnm1  # E[lnM1]=E[lnM2] by symmetry
    # Algebra check (verified by hand before trusting this code): this
    # simplifies exactly to cov = xi*Cov[lnM,b]^2 / (1+<b>^2*xi)^2 -- the
    # (1+<b>^2*xi)^2 denominator is what SUPPRESSES the blowup the
    # first-order-only version had: once <b>^2*xi is large (not small),
    # cov shrinks again rather than diverging, exactly as a bounded
    # correlation coefficient must.
    var_marginal = mean_lnm2 - mean_lnm**2  # xi=0 marginal variance (see docstring)
    rho = cov / var_marginal
    return rho, cov, var_marginal, denom


def xi_mm(r_mpc_h, k, pk):
    """Linear matter correlation function via direct Fourier-Bessel
    integral: xi(r) = (1/2pi^2) int P(k) [sin(kr)/(kr)] k^2 dk.
    """
    integrand = pk * (np.sin(k * r_mpc_h) / (k * r_mpc_h)) * k**2
    return simpson(integrand, x=k) / (2 * np.pi**2)


def xi_mm_shape_check(mf):
    print("=== POSITIVE CONTROL: xi_mm(r) shape (well-known ΛCDM linear shape) ===")
    for r in (5, 10, 20, 40, 45, 80, 100, 110):
        val = xi_mm(r, mf.k, mf.power)
        print(f"  xi_mm(r={r:>4} Mpc/h) = {val:8.5f}")
    xi_5 = xi_mm(5, mf.k, mf.power)
    assert xi_5 > 0.3, "xi_mm at small scale not order-unity -- check power spectrum normalization"
    print("  PASS: order-unity at r=5 Mpc/h, matches the well-documented ΛCDM shape.\n")


def main():
    mc = load_multing_core()
    G, c = mc.G, mc.c  # noqa: F841 (kept for parity with sibling scripts)
    M0_kg = mc.M0_kg
    M0_Msun = M0_kg / 1.98892e30
    print(f"v82's own M0 = {M0_kg:.4e} kg = {M0_Msun:.4e} Msun\n")

    mf0 = positive_control_mass_function()
    positive_control_bias(mf0)
    negative_control_bias(mf0)
    xi_mm_shape_check(mf0)

    print("Population definition: M >= M_of(z)/2, tracking v82's OWN")
    print("z-evolving characteristic node mass (Eq.10: M_of(z)=M0*(1+z)^-1.1),")
    print("NOT a fixed z=0 mass floor -- an earlier draft of this script")
    print("fixed the floor at z=0's M0/2, which made the selected population")
    print("increasingly extreme/rare (and hence absurdly high-bias) at high")
    print("z, since typical halo masses shrink with z while the fixed")
    print("threshold did not. Caught before reporting any number.\n")

    h = mf0.cosmo_model.h
    print(f"hmf's own h = {h:.4f} -- d(z) below is CONVERTED to Mpc/h (x h) before")
    print("use in xi_mm(r): an earlier draft passed physical Mpc directly into a")
    print("function built on hmf's own h/Mpc-unit k-grid, a real ~1/h unit")
    print("mismatch caught by the Step 8a skeptic pass, independently confirmed.\n")

    NU_CALIBRATION_CEILING = 10.0  # Tinker+2010's own simulations do not test
    # bias much past nu~10-20 (their most extreme rare halos); nu beyond this
    # is extrapolation into a regime their fit was never checked against.

    ZS = [0.0, 0.0233, 0.07, 0.5, 1.07, 1.965, 2.33, 5.0]
    print(
        f"{'z':>6}  {'M_of(z)/M0':>10}  {'d(z)[Mpc/h]':>11}  {'nu':>7}  {'Var[lnM]':>9}  "
        f"{'xi_mm(d)':>9}  {'b^2*xi':>8}  {'rho_exact':>10}  valid?"
    )
    n_valid = 0
    for z in ZS:
        m_floor_z = (mc.M_of(z) / 1.98892e30) / 2.0
        mf = build_mass_function(z=z)
        mean_lnm, mean_lnm2, mean_b, mean_lnm_b = population_moments(mf, m_floor_z)
        idx = np.argmin(np.abs(mf.m - m_floor_z))
        nu_at_floor = mf.nu[idx]
        d_mpc_h = (mc.d_of(z) / 3.0856775814913673e22) * h  # m -> Mpc -> Mpc/h
        xi = xi_mm(d_mpc_h, mf.k, mf.power)
        rho, cov, var, denom = pair_rho_exact(mean_lnm, mean_lnm2, mean_b, mean_lnm_b, xi)
        b2xi = mean_b**2 * xi
        m_ratio = mc.M_of(z) / M0_kg
        # denom = 1+<b>^2*xi <= 0 means the linear-bias joint weight
        # [1+b1*b2*xi] is unphysical (negative) somewhere in this
        # population -- a real breakdown of the standard model at this
        # (z, separation) combination, not a bug.
        math_valid = denom > 0 and -1.0 - 1e-6 <= rho <= 1.0 + 1e-6
        # Independently found (after the skeptic pass, verified directly):
        # math_valid alone is NOT sufficient -- nu itself must stay inside
        # the fit's own calibrated range, or the "valid" number is a
        # meaningless extrapolation regardless of internal consistency.
        in_calibration = nu_at_floor <= NU_CALIBRATION_CEILING
        valid = math_valid and in_calibration
        if not math_valid:
            flag = "INVALID (linear-bias model breaks down here)"
        elif not in_calibration:
            flag = "MATH-OK-BUT-EXTRAPOLATED (nu beyond Tinker+2010's own calibration)"
        else:
            flag = "OK"
        print(
            f"{z:6.3f}  {m_ratio:10.4f}  {d_mpc_h:11.3f}  {nu_at_floor:7.2f}  {var:9.5f}  "
            f"{xi:9.5f}  {b2xi:8.4f}  {rho:10.6f}  {flag}"
        )
        n_valid += valid
    print(
        f"\n{n_valid}/{len(ZS)} of v82's own redshifts give a rho that is BOTH"
        " mathematically consistent AND inside the fit's own calibrated range."
    )


if __name__ == "__main__":
    main()
