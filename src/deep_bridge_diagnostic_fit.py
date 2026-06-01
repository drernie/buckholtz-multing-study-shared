"""Deep Bridge Diagnostic Fit — INTERNAL ONLY

PURPOSE: Fit Hamiltonian bridge H²(a) to Table A1 H_MULT (Rows 2–12) as
internal diagnostic of algebraic form flexibility and coefficient stability.

SAFETY LABELS:
- INTERNAL_DIAGNOSTIC_FIT_ONLY
- NOT_SOURCE_CONFIRMED
- NOT_VALIDATION
- NOT_PREDICTION
- MCMC_BLOCKED
- AUTHOR_CONFIRMATION_REQUIRED

DO NOT USE FOR:
- Validation of IDM/MULTING
- Refutation of IDM/MULTING
- Prediction on new z
- Public claims
- MCMC without author confirmation

FORBIDDEN WORDING:
- "validated", "proved", "solved"
- "confirmed bridge", "Buckholtz formula"
- "discovery"

USE ONLY:
- "internal diagnostic fit"
- "algebraic form flexibility check"
- "candidate bridge"
- "source-unconfirmed reconstruction"
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from scipy.optimize import least_squares

# =============================================================================
# Data Loading
# =============================================================================


def load_table_a1_rows_2_12() -> pd.DataFrame:
    """Load Table A1, exclude Row 1 (z=0 outlier)

    Returns only Rows 2–12 (z=0.15 to z=8.5).

    Row 1 excluded because:
    - sigma_MULT deviation 3.027 (27× tolerance)
    - Marked SOURCE_TABLE_OUTLIER
    - May use different convention or be special case
    """
    df = pd.read_csv("data/table_a1_reported.csv", comment="#")

    # Exclude Row 1 (z=0)
    df = df[df["z"] > 0].copy()

    # Verify we have 11 rows (Rows 2–12)
    assert len(df) == 11, f"Expected 11 rows after excluding z=0, got {len(df)}"

    return df


# =============================================================================
# Model Definition
# =============================================================================


@dataclass
class HamiltonianBridgeModel:
    """Hamiltonian bridge H²(z) model

    H²(z) = H₀² [Ω_k(1+z)² + Ω_m(1+z)³ + Ω_d(1+z)⁴ + Ω_q(1+z)⁵]

    Parameters:
    - Ω_k: curvature-like (from integration constant E)
    - Ω_m: monopole (from V_m ∝ a⁻¹)
    - Ω_d: dipole (from V_d ∝ a⁻²)
    - Ω_q: quadrupole (from V_q ∝ a⁻³)
    """

    omega_k: float
    omega_m: float
    omega_d: float
    omega_q: float


def hamiltonian_h_squared(
    z: NDArray[np.float64], params: HamiltonianBridgeModel
) -> NDArray[np.float64]:
    """Compute H²(z) from Hamiltonian bridge

    Args:
        z: redshift array
        params: HamiltonianBridgeModel

    Returns:
        H²(z) in (km/s/Mpc)²
    """
    # H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
    # Convert to H²(z):
    h2_normalized = (
        params.omega_k * (1 + z) ** 2
        + params.omega_m * (1 + z) ** 3
        + params.omega_d * (1 + z) ** 4
        + params.omega_q * (1 + z) ** 5
    )

    # Assume H₀ = 70 km/s/Mpc (will be absorbed into coefficients)
    h0 = 70.0
    return h0**2 * h2_normalized


def safe_h_of_z(z: NDArray[np.float64], params: HamiltonianBridgeModel) -> NDArray[np.float64]:
    """H(z) from the Hamiltonian bridge, guarded against non-physical H² < 0.

    WHY: during least-squares iteration the parameter vector can wander into a
    region where H²(z) < 0. Taking ``np.sqrt`` there yields NaN, which silently
    corrupts the Levenberg-Marquardt / trust-region solver (NaN residuals break
    the Jacobian update — the bug surfaced as 16 ``invalid value encountered in
    sqrt`` RuntimeWarnings). Clipping H² at 0 turns those regions into a finite,
    large penalty (H_model -> 0, residual -> -H_mult) that pushes the optimizer
    back toward physical solutions instead of feeding it NaNs. In the physical
    region (H² > 0) the result is identical to ``np.sqrt(H²)``.
    """
    h2 = hamiltonian_h_squared(z, params)
    return np.sqrt(np.clip(h2, 0.0, None))


# =============================================================================
# Fitting Functions
# =============================================================================


def compute_valid_initial_guess(
    z: NDArray[np.float64], h_mult: NDArray[np.float64]
) -> NDArray[np.float64]:
    """Compute safe initial guess that guarantees H² > 0 for all z

    Args:
        z: redshift array
        h_mult: target H_MULT values

    Returns:
        x0: [Ω_k, Ω_m, Ω_d, Ω_q] initial guess

    Strategy:
    - Start with ΛCDM-like: Ω_m ≈ 0.3, rest ≈ 0
    - Try candidates with small positive Ω_k, Ω_q to ensure H² > 0
    - Pick first candidate where H²(z) > 0 for all z
    """
    # Candidate initial guesses (order: conservative → aggressive)
    candidates = [
        np.array([0.00, 0.30, 0.00, 0.00]),  # Pure Ω_m (ΛCDM-like minus Λ)
        np.array([0.01, 0.30, 0.00, 0.01]),  # Small Ω_k, Ω_q cushion
        np.array([0.05, 0.25, -0.01, 0.02]),  # Tiny negative Ω_d
        np.array([0.10, 0.20, -0.02, 0.05]),  # Moderate exploration
    ]

    for x0 in candidates:
        params = HamiltonianBridgeModel(*x0)
        h2 = hamiltonian_h_squared(z, params)

        # Check: all H² positive and finite
        if np.all(h2 > 0) and np.all(np.isfinite(h2)):
            return x0

    # Fallback: pure Ω_m (safest, always positive)
    return np.array([0.0, 0.3, 0.0, 0.0])


def fit_unconstrained(
    z: NDArray[np.float64], h_mult: NDArray[np.float64]
) -> tuple[HamiltonianBridgeModel, dict]:
    """Unconstrained least squares fit

    Args:
        z: redshift array (Rows 2–12)
        h_mult: H_MULT values from Table A1

    Returns:
        (best_fit_model, diagnostics)
    """

    def residuals(params_vec: NDArray[np.float64]) -> NDArray[np.float64]:
        params = HamiltonianBridgeModel(*params_vec)
        h_model = safe_h_of_z(z, params)
        return h_model - h_mult

    # Initial guess: roughly ΛCDM-like
    x0 = np.array([0.0, 0.3, 0.0, 0.0])

    result = least_squares(residuals, x0, method="lm")

    best_fit = HamiltonianBridgeModel(*result.x)

    # Compute diagnostics
    h_fit = safe_h_of_z(z, best_fit)
    residuals_final = h_fit - h_mult
    mae = np.mean(np.abs(residuals_final))
    rmse = np.sqrt(np.mean(residuals_final**2))

    # Check positivity: H² > 0 for all fitted z?
    h2_values = hamiltonian_h_squared(z, best_fit)
    h2_positive = np.all(h2_values > 0)

    diagnostics = {
        "mae": mae,
        "rmse": rmse,
        "h2_positive": h2_positive,
        "residuals": residuals_final,
        "success": result.success,
        "nfev": result.nfev,
    }

    return best_fit, diagnostics


def fit_sign_constrained(
    z: NDArray[np.float64], h_mult: NDArray[np.float64]
) -> tuple[HamiltonianBridgeModel, dict]:
    """Sign-constrained least squares fit

    Constraints:
    - Ω_m ≥ 0 (monopole attractive)
    - Ω_q ≥ 0 (quadrupole attractive)
    - Ω_d ≤ 0 (dipole repulsive if accelerating)

    Args:
        z: redshift array (Rows 2–12)
        h_mult: H_MULT values from Table A1

    Returns:
        (best_fit_model, diagnostics)
    """

    def residuals(params_vec: NDArray[np.float64]) -> NDArray[np.float64]:
        params = HamiltonianBridgeModel(*params_vec)
        h_model = safe_h_of_z(z, params)
        return h_model - h_mult

    # Initial guess: safe guess that guarantees H² > 0
    x0 = compute_valid_initial_guess(z, h_mult)

    # Bounds: [Ω_k, Ω_m, Ω_d, Ω_q]
    # Ω_k: unbounded
    # Ω_m: ≥ 0
    # Ω_d: ≤ 0
    # Ω_q: ≥ 0
    bounds = (
        [-np.inf, 0.0, -np.inf, 0.0],  # lower
        [np.inf, np.inf, 0.0, np.inf],  # upper
    )

    result = least_squares(residuals, x0, bounds=bounds, method="trf")

    best_fit = HamiltonianBridgeModel(*result.x)

    # Diagnostics
    h_fit = safe_h_of_z(z, best_fit)
    residuals_final = h_fit - h_mult
    mae = np.mean(np.abs(residuals_final))
    rmse = np.sqrt(np.mean(residuals_final**2))

    h2_values = hamiltonian_h_squared(z, best_fit)
    h2_positive = np.all(h2_values > 0)

    # Check if constraints are active
    constraints_active = {
        "omega_m_at_zero": np.isclose(best_fit.omega_m, 0.0, atol=1e-6),
        "omega_d_at_zero": np.isclose(best_fit.omega_d, 0.0, atol=1e-6),
        "omega_q_at_zero": np.isclose(best_fit.omega_q, 0.0, atol=1e-6),
    }

    diagnostics = {
        "mae": mae,
        "rmse": rmse,
        "h2_positive": h2_positive,
        "residuals": residuals_final,
        "success": result.success,
        "nfev": result.nfev,
        "constraints_active": constraints_active,
    }

    return best_fit, diagnostics


# =============================================================================
# Stability Analysis
# =============================================================================


def leave_one_out_stability(
    z: NDArray[np.float64], h_mult: NDArray[np.float64], constrained: bool = True
) -> dict:
    """Leave-one-out cross-validation stability check

    Args:
        z: redshift array (11 points)
        h_mult: H_MULT values
        constrained: use sign-constrained fit if True

    Returns:
        stability diagnostics
    """
    n = len(z)
    loo_rows: list[list[float]] = []

    fit_func = fit_sign_constrained if constrained else fit_unconstrained

    for i in range(n):
        # Exclude point i
        z_loo = np.delete(z, i)
        h_loo = np.delete(h_mult, i)

        model_loo, _ = fit_func(z_loo, h_loo)
        loo_rows.append(
            [model_loo.omega_k, model_loo.omega_m, model_loo.omega_d, model_loo.omega_q]
        )

    loo_params = np.array(loo_rows)

    # Compute coefficient variation
    param_std = np.std(loo_params, axis=0)
    param_mean = np.mean(loo_params, axis=0)
    param_cv = param_std / (np.abs(param_mean) + 1e-9)  # coefficient of variation

    stability = {
        "loo_params": loo_params,
        "param_std": param_std,
        "param_mean": param_mean,
        "param_cv": param_cv,
        "max_cv": np.max(param_cv),
        "stable": np.max(param_cv) < 0.5,  # CV < 0.5 considered stable
    }

    return stability


# =============================================================================
# Baseline Comparisons
# =============================================================================


def fit_polynomial_baseline(
    z: NDArray[np.float64], h_mult: NDArray[np.float64], degree: int = 3
) -> dict:
    """Fit simple polynomial H(z) = a₀ + a₁z + a₂z² + ... as baseline

    Args:
        z: redshift array
        h_mult: H_MULT values
        degree: polynomial degree

    Returns:
        baseline diagnostics
    """
    coeffs = np.polyfit(z, h_mult, degree)
    h_poly = np.polyval(coeffs, z)
    residuals = h_poly - h_mult
    mae = np.mean(np.abs(residuals))
    rmse = np.sqrt(np.mean(residuals**2))

    return {
        "degree": degree,
        "mae": mae,
        "rmse": rmse,
        "coeffs": coeffs,
        "residuals": residuals,
    }


def compute_h_flrw(z: NDArray[np.float64]) -> NDArray[np.float64]:
    """Compute H_FLRW(z) for comparison

    Standard ΛCDM: H(z) = H₀ √[Ω_m(1+z)³ + Ω_Λ]
    """
    h0 = 70.0  # km/s/Mpc
    omega_m = 0.3
    omega_lambda = 0.7

    return h0 * np.sqrt(omega_m * (1 + z) ** 3 + omega_lambda)


# =============================================================================
# Overfitting Classification
# =============================================================================


def classify_fit_robustness(
    mae: float, rmse: float, stability: dict, n_data: int, n_params: int
) -> tuple[str, list[str]]:
    """Classify fit as ROBUST / FLEXIBLE / UNDERDETERMINED / FAILED

    Args:
        mae: mean absolute error
        rmse: root mean squared error
        stability: leave-one-out stability dict
        n_data: number of data points
        n_params: number of model parameters

    Returns:
        (classification, warnings)
    """
    warnings = []

    # Check data/parameter ratio
    ratio = n_data / n_params
    if ratio < 3:
        warnings.append(
            f"UNDERDETERMINED: {n_data} data points, {n_params} parameters (ratio {ratio:.1f} < 3)"
        )

    # Check stability
    if not stability["stable"]:
        warnings.append(f"UNSTABLE: max CV {stability['max_cv']:.2f} > 0.5")

    # Check fit quality
    if mae > 5.0:
        warnings.append(f"POOR_FIT: MAE {mae:.2f} km/s/Mpc > 5")

    # Classification logic
    if len(warnings) == 0:
        classification = "ROBUST_DIAGNOSTIC_SHAPE"
    elif "UNDERDETERMINED" in " ".join(warnings):
        classification = "UNDERDETERMINED"
    elif "UNSTABLE" in " ".join(warnings):
        classification = "FLEXIBLE_CURVE_FIT"
    else:
        classification = "FAILED"

    return classification, warnings


# =============================================================================
# Safety Guards
# =============================================================================


def is_mcmc_allowed() -> bool:
    """Check if MCMC is allowed

    Returns:
        False (always blocked)
    """
    return False


def is_prediction_allowed() -> bool:
    """Check if prediction on new z is allowed

    Returns:
        False (always blocked)
    """
    return False


def get_forbidden_wording() -> list[str]:
    """Get list of forbidden words for output

    Returns:
        List of forbidden terms
    """
    return ["validated", "proved", "solved", "confirmed bridge", "Buckholtz formula", "discovery"]


def get_safe_wording() -> list[str]:
    """Get list of safe words for output

    Returns:
        List of safe terms
    """
    return [
        "internal diagnostic fit",
        "candidate bridge",
        "algebraic form flexibility",
        "source-unconfirmed",
        "author-confirmation-required",
    ]


# =============================================================================
# Main Diagnostic Report
# =============================================================================


def run_full_diagnostic() -> dict:
    """Run full diagnostic fit suite on Table A1 Rows 2–12

    Returns:
        Complete diagnostic report
    """
    # Load data (Rows 2–12 only)
    df = load_table_a1_rows_2_12()
    z = df["z"].values
    h_mult = df["H_MULT"].values

    # Fit 1: Unconstrained
    fit_unc, diag_unc = fit_unconstrained(z, h_mult)

    # Fit 2: Sign-constrained
    fit_con, diag_con = fit_sign_constrained(z, h_mult)

    # Stability: Leave-one-out
    stability_unc = leave_one_out_stability(z, h_mult, constrained=False)
    stability_con = leave_one_out_stability(z, h_mult, constrained=True)

    # Baselines
    poly3 = fit_polynomial_baseline(z, h_mult, degree=3)
    poly4 = fit_polynomial_baseline(z, h_mult, degree=4)
    h_flrw = compute_h_flrw(z)
    flrw_mae = np.mean(np.abs(h_flrw - h_mult))

    # Classification
    class_unc, warn_unc = classify_fit_robustness(
        diag_unc["mae"], diag_unc["rmse"], stability_unc, n_data=len(z), n_params=4
    )
    class_con, warn_con = classify_fit_robustness(
        diag_con["mae"], diag_con["rmse"], stability_con, n_data=len(z), n_params=4
    )

    # Safety checks
    assert not is_mcmc_allowed(), "MCMC must remain blocked"
    assert not is_prediction_allowed(), "Prediction must remain blocked"

    report = {
        "data": {"n_points": len(z), "z_range": (z.min(), z.max()), "row_1_excluded": True},
        "fit_unconstrained": {
            "params": fit_unc,
            "mae": diag_unc["mae"],
            "rmse": diag_unc["rmse"],
            "h2_positive": diag_unc["h2_positive"],
            "stability": stability_unc,
            "classification": class_unc,
            "warnings": warn_unc,
        },
        "fit_constrained": {
            "params": fit_con,
            "mae": diag_con["mae"],
            "rmse": diag_con["rmse"],
            "h2_positive": diag_con["h2_positive"],
            "stability": stability_con,
            "classification": class_con,
            "warnings": warn_con,
            "constraints_active": diag_con["constraints_active"],
        },
        "baselines": {
            "polynomial_degree3": poly3,
            "polynomial_degree4": poly4,
            "h_flrw_mae": flrw_mae,
        },
        "safety": {
            "mcmc_blocked": True,
            "prediction_blocked": True,
            "status": "INTERNAL_DIAGNOSTIC_FIT_ONLY",
        },
    }

    return report
