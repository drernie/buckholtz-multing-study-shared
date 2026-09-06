"""E11 -- rerun P193/P194's Fisher forecasts against E8's corrected degeneracy
baseline (Moresco's CC covariance on the 31 real points).

See CLAIM_E11_fisher_forecasts_under_covariance.md -- endpoint, MCID and the
'% shrinkage is the misleading metric' trap were fixed BEFORE this file.

Reuse strategy (no physics copied):
  * P194 supplies the fit point, SCAN_ZS, P193_ZS, augmented_chi2, hessian_eig,
    semi_axis, the analytic Jacobian pieces (E1_E2_at_z) and its own controls.
  * E8 supplies the covariance construction and the covariance-weighted chi2.
  * The synthetic term is taken from P194 EXACTLY, as
        synth(h0a,b1,b2) = augmented_chi2(...) - chi2_fixed_h0anchor(...)
    (augmented_chi2 is base + synth by construction), then added to the
    covariance-weighted base. This guarantees the regression control below is
    a real identity, not a re-implementation that happens to agree.

Two estimators, cross-checked (P193/P194's own discipline):
  * numeric Hessian of the full chi2 (hessian_eig) -- used for the controls
    and at sigma=10%;
  * analytic Fisher F = J^T C^-1 J (real points) + sum_synth g g^T / sigma^2,
    Hessian = 2F -- used for the sigma grid, exactly as P194 does. WHY: at
    sigma_synth = 1% the synthetic curvature is ~1e4x the baseline's and a
    fixed finite-difference step (h=1e-4) returns negative eigenvalues
    (P191's own docstring warns of this; the first run of this file
    reproduced it). P194 avoids the problem by using the analytic Fisher for
    its sigma grid; this file follows P194.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import numpy as np
from E8_full_covariance_propagation import build_cov_cc, embed_33, fetch_mm20, make_chi2_cov
from P194_fisher_dense_scan import (
    B1_FIT,
    B2_FIT,
    BOUNDARY_Z,
    H0A_FIT,
    KMSMPC_TO_SI,
    P193_ZS,
    SCAN_ZS,
    Z_SHOES,
    E1_E2_at_z,
    H_of_z_kms,
    _dense_zgrid_through,
    analytic_fisher_eig,
    augmented_chi2,
    chi2_fixed_h0anchor,
    hessian_eig,
    semi_axis,
    z33,
)
from scipy.linalg import cho_factor, cho_solve

SIGMAS = (0.01, 0.03, 0.10)  # P194's own grid
# WHY these extra points, added after Step 8a skeptic pass (A4): no z=12-16
# H(z) measurement program exists on any roadmap, and the EXISTING z<2
# chronometers themselves carry 5-10% errors -- sigma_synth=10% at z=14 is
# already optimistic. P193/P194's own grid stops at 10%, quietly avoiding the
# regime (weaker synthetic points) where the baseline choice could plausibly
# start to matter. Scanned here, not asserted against an MCID (no prior
# claim was made about this regime to test).
SIGMAS_WIDE = (0.30, 0.50, 1.00)
E8_BASELINE_SMALL_EIG = {"Moresco default": 17.455, "stress": 9.269}  # FINDING_E8 table


# ---------------------------------------------------------------------------
# Covariance-weighted chi2 with P194's synthetic term, unchanged
# ---------------------------------------------------------------------------
def make_augmented_chi2_cov(C33):
    base_cov = make_chi2_cov(C33)

    def chi2(h0a, b1, b2, synth_zs, synth_sigma_rel):
        synth = augmented_chi2(h0a, b1, b2, synth_zs, synth_sigma_rel) - chi2_fixed_h0anchor(
            h0a, b1, b2
        )
        return base_cov(h0a, b1, b2) + synth

    return chi2


# ---------------------------------------------------------------------------
# Analytic Fisher with a full covariance on the real points
# ---------------------------------------------------------------------------
def _jacobian_rows(zs):
    zdense = _dense_zgrid_through(np.array(zs))
    H_dense = H_of_z_kms(zdense, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    H_at = np.interp(zs, zdense, H_dense)
    J = np.zeros((len(zs), 2))
    for i, (z, H_z) in enumerate(zip(zs, H_at, strict=True)):
        E1, E2 = E1_E2_at_z(z)
        J[i, 0] = (B1_FIT * E1) / (2.0 * H_z * KMSMPC_TO_SI**2)
        J[i, 1] = (B2_FIT * E2) / (2.0 * H_z * KMSMPC_TO_SI**2)
    return J, H_at


def analytic_fisher_cov(C33, synth_zs=None, synth_sigma_rel=None):
    J_real, _ = _jacobian_rows(list(z33))
    cf = cho_factor(C33)
    F = J_real.T @ cho_solve(cf, J_real)
    if synth_zs:
        J_s, H_s = _jacobian_rows(list(synth_zs))
        for g, H_z in zip(J_s, H_s, strict=True):
            F += np.outer(g, g) / (synth_sigma_rel * H_z) ** 2
    return F


def small_eig(C33, synth_zs=None, synth_sigma_rel=None):
    """Small Hessian eigenvalue (2*F convention). C33=None -> P194's own
    diagonal analytic Fisher, so the diagonal column is P194's code verbatim."""
    if C33 is None:
        return 2.0 * analytic_fisher_eig(synth_zs or None, synth_sigma_rel)[0][0]
    eig, _ = np.linalg.eigh(analytic_fisher_cov(C33, synth_zs, synth_sigma_rel))
    return 2.0 * eig[0]


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
def test_regression_zero_modelling_reproduces_p194(mm20):
    """Covariance path with modelling terms zeroed == P194's diagonal path,
    at P193's set and sigma=10%, to <0.1% (numeric Hessian both sides)."""
    C0 = embed_33(build_cov_cc(mm20, [], None))
    chi2c = make_augmented_chi2_cov(C0)
    eig_c, _, _ = hessian_eig(
        lambda h, a, b: chi2c(h, a, b, P193_ZS, 0.10), H0A_FIT, B1_FIT, B2_FIT
    )
    eig_d, _, _ = hessian_eig(
        lambda h, a, b: augmented_chi2(h, a, b, P193_ZS, 0.10), H0A_FIT, B1_FIT, B2_FIT
    )
    rel = abs(eig_c[0] - eig_d[0]) / eig_d[0]
    assert rel < 1e-3, f"regression: {eig_c[0]:.4f} vs P194 {eig_d[0]:.4f} ({rel:.2e})"
    return eig_d[0]


def test_floor_sigma_inf_returns_e8_baseline(chi2c, expected):
    eig, _, _ = hessian_eig(lambda h, a, b: chi2c(h, a, b, P193_ZS, 1e6), H0A_FIT, B1_FIT, B2_FIT)
    rel = abs(eig[0] - expected) / expected
    assert rel < 1e-3, f"floor: {eig[0]:.4f} vs E8 {expected:.4f} ({rel:.2e})"
    return eig[0]


def test_positive_control_covariance_is_actually_used(mm20, name, components):
    """Step 8a skeptic pass on this file: the sigma->1e-6 ceiling agreement
    across baselines (PC4) confirms the DOMINATION MECHANISM, not that the
    covariance is being read at all -- a silently-ignored-covariance bug
    would produce the identical ceiling number. This is the actual positive
    control: scale the modelling covariance by 2x and require the BASELINE
    (synth-free) small eigenvalue to move by a specific, predicted amount.
    A rank-1 term C_mod = v v^T scaled by k changes C^-1 in a way that is
    NOT simply 1/k on the eigenvalue (Sherman-Morrison), so the assertion
    checks direction (must decrease as k grows) and a loose bound, not an
    exact factor."""
    C1 = embed_33(build_cov_cc(mm20, components, None))
    mm20_2x = mm20.copy()
    for c in components:
        mm20_2x[c] = mm20_2x[c] * 2.0
    C2 = embed_33(build_cov_cc(mm20_2x, components, None))
    lam1, lam2 = small_eig(C1), small_eig(C2)
    assert lam2 < lam1, (
        f"{name}: doubling the modelling covariance must not INCREASE curvature ({lam1:.3f} -> {lam2:.3f})"
    )
    assert lam2 < 0.85 * lam1, (
        f"{name}: doubling should move lambda_small by more than 15% ({lam1:.3f} -> {lam2:.3f})"
    )
    return lam1, lam2


def test_analytic_matches_fd(C33, chi2c, synth_zs, sig, tol):
    """P193/P194's own control, now under covariance: analytic Fisher must
    agree with the finite-difference Hessian. Run at baseline (tol 5%) and
    at the augmented sigma=10% case (tol 10%), as P194 does."""
    eig_fd, _, _ = hessian_eig(
        lambda h, a, b: chi2c(h, a, b, synth_zs, sig), H0A_FIT, B1_FIT, B2_FIT, h=1e-6
    )
    eig_an = small_eig(C33, synth_zs, sig)
    rel = abs(eig_an - eig_fd[0]) / abs(eig_fd[0])
    assert rel < tol, f"analytic vs FD small eig: {eig_an:.4f} vs {eig_fd[0]:.4f} ({rel:.2%})"
    return rel


if __name__ == "__main__":
    mm20 = fetch_mm20()
    variants = {
        "diag (P193/P194)": None,
        "Moresco default": embed_33(build_cov_cc(mm20, ["spsooo", "imf"], None)),
        "stress": embed_33(build_cov_cc(mm20, ["sps", "imf"], None)),
    }

    # ---- controls ---------------------------------------------------------
    p194_ref = test_regression_zero_modelling_reproduces_p194(mm20)
    print(
        f"PC1 regression: zero-modelling covariance path == P194 diagonal at {{12,14,16}}, "
        f"sigma=10%: lambda_small={p194_ref:.3f}: PASS"
    )
    comps_by_name = {"Moresco default": ["spsooo", "imf"], "stress": ["sps", "imf"]}
    for name in ("Moresco default", "stress"):
        chi2c = make_augmented_chi2_cov(variants[name])
        fl = test_floor_sigma_inf_returns_e8_baseline(chi2c, E8_BASELINE_SMALL_EIG[name])
        print(f"PC2 floor ({name}): sigma->inf returns E8 baseline {fl:.3f}: PASS")
        r0 = test_analytic_matches_fd(variants[name], chi2c, [], None, 0.05)
        r1 = test_analytic_matches_fd(variants[name], chi2c, P193_ZS, 0.10, 0.10)
        print(
            f"PC3 analytic Fisher vs FD Hessian ({name}): baseline {r0:.2%}, "
            f"augmented {{12,14,16}}@10% {r1:.2%}: PASS"
        )
        l1, l2 = test_positive_control_covariance_is_actually_used(mm20, name, comps_by_name[name])
        print(
            f"PC6 covariance actually used ({name}): doubling modelling terms moves "
            f"baseline lambda_small {l1:.3f} -> {l2:.3f}: PASS (rules out silent fallback "
            f"the sigma->0 ceiling test alone cannot rule out -- Step 8a finding)"
        )
    # ceiling: sigma->0, synthetic dominates, error model must not matter.
    # Analytic route (validated vs FD at h=1e-6 in PC3); FD at any fixed h is
    # unreliable this far into the stiff regime -- see module docstring.
    ce = {name: small_eig(C, P193_ZS, 1e-6) for name, C in variants.items()}
    spread = (max(ce.values()) - min(ce.values())) / max(ce.values())
    assert spread < 0.01, f"ceiling spread {spread:.2%}"
    print(f"PC4 ceiling: sigma->0 small eig agrees across error models to {spread:.2e}: PASS")
    zb = _dense_zgrid_through(np.array([BOUNDARY_Z + 0.05]))
    Hb = H_of_z_kms(zb, H0A_FIT, B1_FIT, B2_FIT, Z_SHOES)
    assert np.any(np.isnan(Hb[zb > BOUNDARY_Z])) and not np.any(np.isnan(Hb[zb <= 16.5]))
    print("PC5 domain boundary z=16.957 unchanged (depends on fiducial model, not errors): PASS\n")

    # ---- Q2: absolute attainable width, P193's window (analytic, as P194) ----
    print("=" * 96)
    print(
        "Q2 -- ABSOLUTE post-augmentation width t_aug = sqrt(2/lambda_small) at P193's {12,14,16}"
    )
    print("      analytic Fisher for the sigma grid, exactly as P194; % shrinkage shown ONLY to")
    print("      demonstrate why it is the misleading metric")
    print("=" * 96)
    print(
        f"{'error model':<18} {'sigma':>6} {'lam_base':>9} {'t_base':>7} {'lam_aug':>10} "
        f"{'t_aug':>7} {'% shrink':>9}"
    )
    q2 = {}
    for name, C in variants.items():
        lb = small_eig(C)
        for sig in SIGMAS:
            la = small_eig(C, P193_ZS, sig)
            tb, ta = semi_axis(lb), semi_axis(la)
            q2[(name, sig)] = (lb, tb, la, ta)
            print(
                f"{name:<18} {sig:6.0%} {lb:9.3f} {tb:7.1%} {la:10.1f} {ta:7.2%} {1 - ta / tb:9.1%}"
            )

    print("\n[Step 8a skeptic, A4] EXPLORATORY -- weaker sigma_synth, where domination weakens:")
    for name, C in variants.items():
        lb = small_eig(C)
        for sig in SIGMAS_WIDE:
            la = small_eig(C, P193_ZS, sig)
            tb, ta = semi_axis(lb), semi_axis(la)
            q2[(name, sig)] = (lb, tb, la, ta)
            print(
                f"{name:<18} {sig:6.0%} {lb:9.3f} {tb:7.1%} {la:10.3f} {ta:7.2%} {1 - ta / tb:9.1%}"
            )

    # ---- Q1: ranking over SCAN_ZS, single-point profile at 10% --------------
    print("\n" + "=" * 96)
    print(
        "Q1 -- single-point shrink profile over P194's SCAN_ZS at sigma=10%: does the RANKING survive?"
    )
    print("=" * 96)
    profiles = {}
    for name, C in variants.items():
        lb = small_eig(C)
        profiles[name] = {
            z: 1.0 - semi_axis(small_eig(C, [z], 0.10)) / semi_axis(lb) for z in SCAN_ZS
        }
    print(f"{'z':>5} " + " ".join(f"{n:>18}" for n in variants))
    for z in SCAN_ZS:
        print(f"{z:5.1f} " + " ".join(f"{profiles[n][z]:18.2%}" for n in variants))
    rank = {n: sorted(SCAN_ZS, key=lambda z, p=profiles[n]: -p[z]) for n in variants}
    print("\nranking (best first):")
    for n in variants:
        print(f"  {n:<18} {rank[n]}")
    same_top3 = all(rank[n][:3] == rank["diag (P193/P194)"][:3] for n in variants)
    print(f"top-3 identical across error models: {same_top3}")

    # ---- MCID -----------------------------------------------------------------
    print("\n" + "=" * 96)
    print("MCID (pre-registered in CLAIM_E11)")
    print("=" * 96)
    for sig in SIGMAS:
        t_diag = q2[("diag (P193/P194)", sig)][3]
        for name in ("Moresco default", "stress"):
            t_cov = q2[(name, sig)][3]
            fac = t_cov / t_diag
            verdict = "MATERIAL" if fac > 1.5 else "not material"
            print(
                f"Q2 sigma={sig:4.0%} {name:<16}: t_aug {t_diag:.3%} -> {t_cov:.3%}, "
                f"factor {fac:.3f} -> {verdict} (threshold 1.5x)"
            )
    print(
        f"Q1 ranking: top-3 unchanged = {same_top3}; boundary unchanged = True"
        f"  -> {'not material' if same_top3 else 'MATERIAL'}"
    )
