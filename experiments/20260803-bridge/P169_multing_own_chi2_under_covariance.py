"""P169 -- direct continuation of FINDING_P168's own named residual gap:
recompute MULTING's own chi^2 under the SAME Cosmic-Chronometer systematic
covariance treatment (Moresco et al. 2020, arXiv:2003.07362) already
applied to the physically-empty dummy model in P167/P168, using v82's own
H_MULT(z) construction and its own published best-fit parameters -- not a
re-derivation from the paper's prose (which P161/P165 already found does
NOT state the node-mass baseline numerically), but a faithful
reimplementation of TJB's own cited supplemental Zenodo code archive.

SOURCE [VERIFIED-zenodo, downloaded 2026-08-31, user-approved download]:
T.J. Buckholtz, "Supplemental material for 'Multi-Tier Newtonian
Gravity...'", Zenodo, DOI: 10.5281/zenodo.21204955 (v82's own ref [33]),
file zenodo_archive_v17.zip, containing code/multing_core.py +
code/assumptions.yaml + code/generate_all_results.py. All constants and
functions below are independently RE-TYPED from those two files (read as
plain text, cross-checked against each other for internal consistency --
they matched exactly), NEVER executed from the downloaded archive. This
resolves the specific gap FINDING_P161/P165 flagged as unavailable from
the paper's own prose: the node-mass baseline M0=1.193082e45 kg (~6e14
Msun, consistent with the illustrative "5-6x10^14 Msun" comparison mass
v82's own text mentions at a different point) was never stated in the
paper text itself (confirmed by a full-file search of the ~2279-line
extracted text), only in this code archive's assumptions.yaml.

METHODOLOGICAL CORRECTION vs FINDING_P168's own stated expectation: P168
said this recomputation "would need full numerical integration of v82's
own dynamics" implying a coupled 2nd-order (s,z,H) system solved in
cosmic time t (the framing FINDING_P161's own LOCAL Taylor-expansion
machinery used). Reading TJB's own actual code shows the REAL global
computation is simpler: d(z)=d0/(1+z) is a fixed kinematic power law (not
separately integrated from the force law), and H^2(z) is built by direct
1-D quadrature (trapezoidal rule) of a single algebraic integrand,
addot_over_a(z) -- computed by TJB's own multing_core.py, docstring name
suggests s-double-dot/s, but the code's own comment flags that within
this specific numerical construction it is USED as -dH/dt directly (a
modeling choice named in the paper's Sec IV.R, not re-litigated here) --
over a redshift grid, anchored at z=Z_SHOES=0.0233. No coupled-ODE
shooting method is needed; this made the full-fidelity recomputation
requested here tractable in a way P168's own framing did not anticipate.

Positive control: this file's own reimplementation of TJB's H(z)
construction, combined with his own PUBLISHED best-fit (H0_anchor, beta1,
beta2) from Table II, must reproduce chi2_33=15.75 (unconstrained) and
15.78 (SH0ES-anchored) via the SAME diagonal-sigma fit procedure his own
generate_all_results.py uses -- confirming the reimplementation is
faithful BEFORE trusting anything computed from it under a different
(GLS-covariance) objective.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize

# ---------------------------------------------------------------------------
# Constants [VERIFIED-zenodo, code/assumptions.yaml + code/multing_core.py,
# cross-checked between the two files -- they agree exactly]
# ---------------------------------------------------------------------------
MSUN_TO_KG = 1.98847e30
MPC_TO_M = 3.08567758e22
KEV_TO_J = 1.602176634e-16
KMSMPC_TO_SI = 3.24077929e-20

G = 6.674e-11
C_LIGHT = 299792458.0

OM_PLANCK = 0.315
OL_PLANCK = 0.685
H0_PLANCK_SI = 67.4 * KMSMPC_TO_SI

M0_KG = 1.193082e45
D0_M = 45.0 * MPC_TO_M
T0_KEV = 3.7163
MU_MOL = 0.6
M_PROTON_KG = 1.67262192e-27

T_PIV_KEV = 2.27
MGAS_PIV_KG = 2.28e13 * MSUN_TO_KG
Z_PIV = 0.25
B_REAL = 2.24
C_REAL = -1.00

RHO_CRIT0 = 3.0 * H0_PLANCK_SI**2 / (8.0 * np.pi * G)

F_MERGE = 0.25
F_COH = 1.0 / 3.0

Z_SHOES = 0.0233
H_SHOES, SIG_SHOES = 73.04, 1.04
Z_DESI, H_DESI, SIG_DESI = 2.33, 236.1, 2.8


# ---------------------------------------------------------------------------
# Scaling laws + force law + H(z) construction [VERIFIED-zenodo,
# code/multing_core.py, re-typed verbatim from the read source, not
# executed from the archive]
# ---------------------------------------------------------------------------
def _e_fun(z, om=OM_PLANCK, ol=OL_PLANCK):
    return np.sqrt(om * (1.0 + z) ** 3 + ol)


def _m_of(z):
    return M0_KG * (1.0 + z) ** (-1.1)


def _t_kev_of(z):
    return T0_KEV * (_m_of(z) / M0_KG) ** (2.0 / 3.0) * _e_fun(z) ** (2.0 / 3.0)


def _mgas_of(z):
    return (
        MGAS_PIV_KG * (_t_kev_of(z) / T_PIV_KEV) ** B_REAL * (_e_fun(z) / _e_fun(Z_PIV)) ** C_REAL
    )


def _k_of(z):
    return 1.5 * (_mgas_of(z) / (MU_MOL * M_PROTON_KG)) * (_t_kev_of(z) * KEV_TO_J)


def _rho_crit(z):
    return RHO_CRIT0 * _e_fun(z) ** 2


def _r_of(z):
    return (3.0 * _m_of(z) / (4.0 * np.pi * 500.0 * _rho_crit(z))) ** (1.0 / 3.0)


def _d_of(z):
    return D0_M * (1.0 + z) ** (-1.0)


def _forces(z, beta_1, beta_2):
    m, r, k, d = _m_of(z), _r_of(z), _k_of(z), _d_of(z)
    f0 = (-G) * m * m / d**2
    f1 = beta_1 * (-G) * 2.0 * m * (k / C_LIGHT**2) * (r / d) / d**2
    f2 = beta_2 * (-G) * (k / C_LIGHT**2) ** 2 * (r * r / d**2) / d**2
    return f0, f1, f2


def _hlcdm_si(z):
    return H0_PLANCK_SI * _e_fun(z)


def _m_dot(z):
    return 1.1 * _hlcdm_si(z) * _m_of(z)


def _v_infall(z):
    return np.sqrt(G * _m_of(z) / _r_of(z))


def _dv_coh(z):
    return F_COH * F_MERGE * _v_infall(z)


def _f_accretion(z):
    return _m_dot(z) * _dv_coh(z)


def _addot_over_a(z, b1, b2):
    f0, f1, f2 = _forces(z, b1, b2)
    f_total = f0 - f1 + f2 - _f_accretion(z)
    return (f_total / (_m_of(z) / 2.0)) / _d_of(z)


def h2_of_z(zgrid, h0_anchor_kms, b1, b2, zref):
    zg = np.atleast_1d(np.asarray(zgrid, dtype=float))
    order = np.argsort(zg)
    zgs = zg[order]
    aa = np.array([_addot_over_a(zx, b1, b2) for zx in zgs])
    integrand = aa / (1.0 + zgs)
    ds_raw = np.concatenate(([0.0], cumulative_trapezoid(integrand, zgs)))
    i0 = np.argmin(np.abs(zgs - zref))
    ds = ds_raw - ds_raw[i0]
    h2 = np.empty_like(ds)
    h2[order] = (h0_anchor_kms * KMSMPC_TO_SI) ** 2 + 2.0 * ds
    return h2


def h_of_z_kms(zgrid, h0_anchor_kms, b1, b2, zref):
    h2 = h2_of_z(zgrid, h0_anchor_kms, b1, b2, zref)
    h = np.full_like(h2, np.nan)
    valid = h2 > 0
    h[valid] = np.sqrt(h2[valid]) / KMSMPC_TO_SI
    return h


# ---------------------------------------------------------------------------
# Data [VERIFIED-arXiv, same 31-point CC compilation + SH0ES + DESI as
# P167/P168, cross-checked against 2 independent primary sources there]
# ---------------------------------------------------------------------------
CC_DATA = [
    (0.0700, 69.0, 19.6),
    (0.0900, 69.0, 12.0),
    (0.1200, 68.6, 26.2),
    (0.1700, 83.0, 8.0),
    (0.1791, 75.0, 4.0),
    (0.1993, 75.0, 5.0),
    (0.2000, 72.9, 29.6),
    (0.2700, 77.0, 14.0),
    (0.2800, 88.8, 36.6),
    (0.3519, 83.0, 14.0),
    (0.3802, 83.0, 13.5),
    (0.4000, 95.0, 17.0),
    (0.4004, 77.0, 10.2),
    (0.4247, 87.1, 11.2),
    (0.4497, 92.8, 12.9),
    (0.4700, 89.0, 49.6),
    (0.4783, 80.9, 9.0),
    (0.4800, 97.0, 62.0),
    (0.5929, 104.0, 13.0),
    (0.6797, 92.0, 8.0),
    (0.7812, 105.0, 12.0),
    (0.8754, 125.0, 17.0),
    (0.8800, 90.0, 40.0),
    (0.9000, 117.0, 23.0),
    (1.0370, 154.0, 20.0),
    (1.3000, 168.0, 17.0),
    (1.3630, 160.0, 33.6),
    (1.4300, 177.0, 18.0),
    (1.5300, 140.0, 14.0),
    (1.7500, 202.0, 40.0),
    (1.9650, 186.5, 50.4),
]
assert len(CC_DATA) == 31
FULL_33 = CC_DATA + [(Z_SHOES, H_SHOES, SIG_SHOES), (Z_DESI, H_DESI, SIG_DESI)]
Z33 = np.array([d[0] for d in FULL_33])
H33 = np.array([d[1] for d in FULL_33])
S33 = np.array([d[2] for d in FULL_33])

MULTING_UNCONSTRAINED = {
    "H0_anchor": 73.22,
    "beta_1": 1.4335e10,
    "beta_2": 7.8067e17,
    "chi2_paper": 15.75,
}
MULTING_SH0ES_ANCHORED = {
    "H0_anchor": 73.04,
    "beta_1": 1.4233e10,
    "beta_2": 7.7443e17,
    "chi2_paper": 15.78,
}

_ZFINE = np.sort(np.unique(np.concatenate([np.linspace(0, Z_DESI, 500), Z33])))


def _model_at_33(h0a, b1, b2):
    hm = h_of_z_kms(_ZFINE, h0a, b1, b2, Z_SHOES)
    if np.any(np.isnan(hm)):
        return None
    return np.interp(Z33, _ZFINE, hm)


def _diagonal_chi2(h0a, b1, b2):
    hp = _model_at_33(h0a, b1, b2)
    if hp is None:
        return 1e12
    return float(np.sum(((hp - H33) / S33) ** 2))


# ---------------------------------------------------------------------------
# Positive control: reproduce v82's own Table II chi2_33 exactly, via the
# SAME diagonal-sigma objective his own generate_all_results.py uses.
# ---------------------------------------------------------------------------
def test_positive_control_reproduces_table_ii_unconstrained():
    c = MULTING_UNCONSTRAINED
    chi2 = _diagonal_chi2(c["H0_anchor"], c["beta_1"], c["beta_2"])
    assert abs(chi2 - c["chi2_paper"]) < 0.02


def test_positive_control_reproduces_table_ii_sh0es_anchored():
    c = MULTING_SH0ES_ANCHORED
    chi2 = _diagonal_chi2(c["H0_anchor"], c["beta_1"], c["beta_2"])
    assert abs(chi2 - c["chi2_paper"]) < 0.02


# ---------------------------------------------------------------------------
# GLS covariance [VERIFIED-arXiv abstract, arXiv:2003.07362, same
# construction as P168 -- rank-1 SPS/IMF systematic, restricted to the
# first 31 (Cosmic Chronometer) points, SH0ES/DESI excluded]
# ---------------------------------------------------------------------------
Z_LO, FRAC_LO = 0.2, 0.054
Z_HI, FRAC_HI = 1.5, 0.023


def _systematic_fraction(z, restrict_to_paper_range):
    if restrict_to_paper_range and not (Z_LO <= z <= Z_HI):
        return 0.0
    z_clamped = min(max(z, Z_LO), Z_HI)
    t = (z_clamped - Z_LO) / (Z_HI - Z_LO)
    return FRAC_LO + t * (FRAC_HI - FRAC_LO)


_N_CC = len(CC_DATA)


def _build_covariance(restrict_to_paper_range, n_cc=_N_CC):
    n = len(FULL_33)
    cov = np.zeros((n, n))
    frac_h = np.zeros(n)
    for i, (z, h, sigma) in enumerate(FULL_33):
        cov[i, i] = sigma**2
        if i < n_cc:
            frac_h[i] = _systematic_fraction(z, restrict_to_paper_range) * h
    cov += np.outer(frac_h, frac_h)
    return cov


def _gls_chi2(h0a, b1, b2, cov_inv):
    hp = _model_at_33(h0a, b1, b2)
    if hp is None:
        return 1e12
    resid = hp - H33
    return float(resid @ cov_inv @ resid)


def test_positive_control_gls_zero_amplitude_matches_diagonal():
    """GLS with a zero-amplitude covariance (pure diagonal) must recover
    this file's own diagonal chi2 exactly, for both Table II rows --
    confirms the GLS machinery reduces correctly before trusting it on
    the real covariance.
    """
    cov = np.diag(S33**2)
    cov_inv = np.linalg.inv(cov)
    for c in (MULTING_UNCONSTRAINED, MULTING_SH0ES_ANCHORED):
        gls = _gls_chi2(c["H0_anchor"], c["beta_1"], c["beta_2"], cov_inv)
        diag = _diagonal_chi2(c["H0_anchor"], c["beta_1"], c["beta_2"])
        assert abs(gls - diag) < 0.01


# ---------------------------------------------------------------------------
# (A) Evaluate MULTING's own PUBLISHED best-fit under GLS, no refit
# ---------------------------------------------------------------------------
def evaluate_published_fit_under_gls(restrict_to_paper_range):
    cov = _build_covariance(restrict_to_paper_range)
    cov_inv = np.linalg.inv(cov)
    out = {}
    for label, c in (
        ("unconstrained", MULTING_UNCONSTRAINED),
        ("sh0es_anchored", MULTING_SH0ES_ANCHORED),
    ):
        out[label] = _gls_chi2(c["H0_anchor"], c["beta_1"], c["beta_2"], cov_inv)
    return out


# ---------------------------------------------------------------------------
# (B) Refit MULTING's own model under GLS -- fair apples-to-apples
# comparison against P168's own GLS-refit dummy model.
# ---------------------------------------------------------------------------
def refit_unconstrained_under_gls(cov_inv, guess):
    def obj(p):
        h0a, b1, b2 = p
        if h0a <= 0 or b1 < 0 or b2 < 0:
            return 1e12
        return _gls_chi2(h0a, b1, b2, cov_inv)

    r = minimize(
        obj,
        guess,
        method="Nelder-Mead",
        options={"xatol": 1e-4, "fatol": 1e-9, "maxiter": 20000, "maxfev": 20000},
    )
    return r.x, r.fun


def refit_anchored_under_gls(cov_inv, guess, h0_fixed=H_SHOES):
    def obj(p):
        b1, b2 = p
        if b1 < 0 or b2 < 0:
            return 1e12
        return _gls_chi2(h0_fixed, b1, b2, cov_inv)

    r = minimize(
        obj,
        guess,
        method="Nelder-Mead",
        options={"xatol": 1e-3, "fatol": 1e-8, "maxiter": 10000, "maxfev": 10000},
    )
    return (h0_fixed, r.x[0], r.x[1]), r.fun


def robust_refit_unconstrained_under_gls(cov_inv, guess, n_random_starts=15, seed=20260831):
    """Skeptic-caught robustness check (2026-08-31): plain Nelder-Mead on
    the raw (H0_anchor~1e1, beta1~1e10, beta2~1e17) coordinates risks
    premature convergence -- the scale mismatch means xatol/fatol in
    absolute units are essentially meaningless for the beta2 direction.
    This function rescales all three coordinates to O(1) around `guess`
    (so xatol/fatol are meaningful in every direction) and multi-starts
    from `n_random_starts` random points within +-30-50% of `guess`,
    returning the best of all runs -- if the plain single-start refit in
    `refit_unconstrained_under_gls` were stuck at a bad local optimum,
    this would find something meaningfully lower.
    """
    rng = np.random.default_rng(seed)
    h0_0, b1_0, b2_0 = guess

    def obj_scaled(p):
        h0a, b1, b2 = p[0] * h0_0, p[1] * b1_0, p[2] * b2_0
        if h0a <= 0 or b1 < 0 or b2 < 0:
            return 1e12
        return _gls_chi2(h0a, b1, b2, cov_inv)

    starts = [[1.0, 1.0, 1.0]] + [
        [1.0 + rng.uniform(-0.3, 0.3), 1.0 + rng.uniform(-0.5, 0.5), 1.0 + rng.uniform(-0.5, 0.5)]
        for _ in range(n_random_starts)
    ]
    best = None
    for s0 in starts:
        r = minimize(
            obj_scaled,
            s0,
            method="Nelder-Mead",
            options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 50000, "maxfev": 50000},
        )
        if best is None or r.fun < best[1]:
            best = (r.x, r.fun)
    h0a, b1, b2 = best[0][0] * h0_0, best[0][1] * b1_0, best[0][2] * b2_0
    return (h0a, b1, b2), best[1]


def robust_refit_anchored_under_gls(
    cov_inv, guess, h0_fixed=H_SHOES, n_random_starts=15, seed=20260831
):
    """Same robustness treatment as `robust_refit_unconstrained_under_gls`,
    for the 2-parameter (beta1, beta2) anchored case."""
    rng = np.random.default_rng(seed)
    b1_0, b2_0 = guess

    def obj_scaled(p):
        b1, b2 = p[0] * b1_0, p[1] * b2_0
        if b1 < 0 or b2 < 0:
            return 1e12
        return _gls_chi2(h0_fixed, b1, b2, cov_inv)

    starts = [[1.0, 1.0]] + [
        [1.0 + rng.uniform(-0.5, 0.5), 1.0 + rng.uniform(-0.5, 0.5)] for _ in range(n_random_starts)
    ]
    best = None
    for s0 in starts:
        r = minimize(
            obj_scaled,
            s0,
            method="Nelder-Mead",
            options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 50000, "maxfev": 50000},
        )
        if best is None or r.fun < best[1]:
            best = (r.x, r.fun)
    b1, b2 = best[0][0] * b1_0, best[0][1] * b2_0
    return (h0_fixed, b1, b2), best[1]


def test_robust_refit_matches_plain_refit_no_hidden_local_optimum():
    """Skeptic-caught (2026-08-31): confirms the plain single-start refit
    used for the headline numbers is NOT stuck at a bad local optimum due
    to badly-scaled Nelder-Mead coordinates. Rescaled + 16-start search
    must not find anything meaningfully (>0.05) lower than the plain
    refit, for both variants and both rows.
    """
    for restrict in (False, True):
        cov = _build_covariance(restrict)
        cov_inv = np.linalg.inv(cov)
        c_u, c_a = MULTING_UNCONSTRAINED, MULTING_SH0ES_ANCHORED

        _, chi2_u_plain = refit_unconstrained_under_gls(
            cov_inv, [c_u["H0_anchor"], c_u["beta_1"], c_u["beta_2"]]
        )
        _, chi2_u_robust = robust_refit_unconstrained_under_gls(
            cov_inv, [c_u["H0_anchor"], c_u["beta_1"], c_u["beta_2"]]
        )
        assert chi2_u_plain - chi2_u_robust < 0.05

        _, chi2_a_plain = refit_anchored_under_gls(cov_inv, [c_a["beta_1"], c_a["beta_2"]])
        _, chi2_a_robust = robust_refit_anchored_under_gls(cov_inv, [c_a["beta_1"], c_a["beta_2"]])
        assert chi2_a_plain - chi2_a_robust < 0.05


def test_positive_control_refit_at_zero_amplitude_recovers_paper_optimum():
    """Refitting under a zero-systematic GLS objective, starting from
    v82's own published optimum, must NOT find anything meaningfully
    better than v82's own reported chi2 -- confirms the refit machinery
    (not just point-evaluation) is behaving sanely before trusting its
    output on the real covariance.
    """
    cov = np.diag(S33**2)
    cov_inv = np.linalg.inv(cov)
    c = MULTING_UNCONSTRAINED
    _, chi2 = refit_unconstrained_under_gls(cov_inv, [c["H0_anchor"], c["beta_1"], c["beta_2"]])
    assert chi2 <= c["chi2_paper"] + 0.01
    assert chi2 > c["chi2_paper"] - 0.5


# ---------------------------------------------------------------------------
# P168's own already-computed dummy-model GLS-refit results [VERIFIED-file,
# FINDING_P168, committed f977808 -- cited for direct comparison, not
# recomputed here]
# ---------------------------------------------------------------------------
P168_DUMMY_GLS = {
    "variant_a_all_31": {"unconstrained": 13.989, "anchored": 14.008},
    "variant_b_paper_range": {"unconstrained": 13.637, "anchored": 13.637},
}


if __name__ == "__main__":
    test_positive_control_reproduces_table_ii_unconstrained()
    test_positive_control_reproduces_table_ii_sh0es_anchored()
    print(
        "Positive control: reimplementation reproduces v82's own Table II chi2_33 "
        "(15.75 unconstrained, 15.78 anchored) via diagonal-sigma fit: PASS"
    )

    test_positive_control_gls_zero_amplitude_matches_diagonal()
    print(
        "Positive control: GLS machinery at zero systematic amplitude matches "
        "diagonal chi2 exactly: PASS"
    )

    test_robust_refit_matches_plain_refit_no_hidden_local_optimum()
    print(
        "Positive control (skeptic-caught, 2026-08-31): rescaled + 16-start refit "
        "does not find anything meaningfully lower than the plain single-start "
        "refit, in either variant -- the plain refit is not stuck at a bad local "
        "optimum: PASS"
    )

    test_positive_control_refit_at_zero_amplitude_recovers_paper_optimum()
    print(
        "Positive control: refit machinery at zero systematic amplitude does not "
        "improve meaningfully on v82's own published optimum: PASS"
    )

    print("\n=== (A) MULTING's PUBLISHED best-fit, evaluated (not refit) under GLS ===")
    for variant, restrict in (
        ("Variant A (all 31 CC points)", False),
        ("Variant B (paper's own range [0.2,1.5] only)", True),
    ):
        res = evaluate_published_fit_under_gls(restrict)
        print(f"\n{variant}:")
        for label, c in (
            ("unconstrained", MULTING_UNCONSTRAINED),
            ("sh0es_anchored", MULTING_SH0ES_ANCHORED),
        ):
            print(
                f"  {label}: chi2_GLS(published fit)={res[label]:.3f}  "
                f"(diagonal chi2_paper={c['chi2_paper']})  "
                f"delta={res[label] - c['chi2_paper']:+.3f}"
            )

    print(
        "\n=== (B) MULTING REFIT under GLS -- fair comparison to P168's own "
        "dummy-model GLS refit ==="
    )
    for variant_key, variant_label, restrict in (
        ("variant_a_all_31", "Variant A (all 31 CC points)", False),
        ("variant_b_paper_range", "Variant B (paper's own range [0.2,1.5] only)", True),
    ):
        cov = _build_covariance(restrict)
        cov_inv = np.linalg.inv(cov)
        c_u, c_a = MULTING_UNCONSTRAINED, MULTING_SH0ES_ANCHORED
        _, chi2_u = refit_unconstrained_under_gls(
            cov_inv, [c_u["H0_anchor"], c_u["beta_1"], c_u["beta_2"]]
        )
        _, chi2_a = refit_anchored_under_gls(cov_inv, [c_a["beta_1"], c_a["beta_2"]])
        dummy = P168_DUMMY_GLS[variant_key]
        print(f"\n{variant_label}:")
        print(
            f"  MULTING refit (k=3, unconstrained): chi2_GLS={chi2_u:.3f}   "
            f"vs dummy (P168) chi2_GLS={dummy['unconstrained']:.3f}   "
            f"MULTING-dummy={chi2_u - dummy['unconstrained']:+.3f}"
        )
        print(
            f"  MULTING refit (k=2, SH0ES-anchored): chi2_GLS={chi2_a:.3f}   "
            f"vs dummy (P168) chi2_GLS={dummy['anchored']:.3f}   "
            f"MULTING-dummy={chi2_a - dummy['anchored']:+.3f}"
        )
