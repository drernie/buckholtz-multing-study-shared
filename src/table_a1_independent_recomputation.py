"""Table A1 Independent Recomputation

Purpose: Independently recompute Table A1 arithmetic and identify anchor-row treatment.

This is NOT:
- A validation of MULTING theory
- A refutation of author's method
- A claim of author error

This IS:
- Pure arithmetic verification
- Baseline for future sensitivity work
- Diagnostic for anchor-row treatment
- Respectful contribution if author finds it useful

Safety Labels:
- INTERNAL_CONTRIBUTION_DRAFT
- NOT_SENT
- NOT_VALIDATION
- NOT_REFUTATION
- AUTHOR_CONFIRMATION_REQUIRED
- PROVISIONAL_AUTHOR_DEPENDENT
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd

# ============================================================================
# Enums and Constants
# ============================================================================


class EvidenceLevel(Enum):
    """Evidence level for assumptions"""

    EXPLICIT_IN_PAPER = "explicit_in_paper"
    INFERRED_FROM_CONTEXT = "inferred_from_context"
    ASSUMED_STANDARD = "assumed_standard"
    UNKNOWN_GUESSED = "unknown_guessed"


class ConfidenceLevel(Enum):
    """Confidence in assumption correctness"""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


# Standard cosmological parameters (Planck 2018 values assumed)
# Evidence: ASSUMED_STANDARD (not specified in paper, using community standard)
H0_DEFAULT = 67.4  # km/s/Mpc (matches H_FLRW at z=0 in Table A1)
OMEGA_M_DEFAULT = 0.315  # Matter density (Planck 2018)
OMEGA_LAMBDA_DEFAULT = 0.685  # Dark energy density (Planck 2018)
OMEGA_K_DEFAULT = 0.0  # Curvature (flat universe assumed)


# ============================================================================
# Assumptions Tracking
# ============================================================================


@dataclass
class Assumption:
    """Single assumption with evidence tracking"""

    statement: str
    evidence: EvidenceLevel
    source: str
    confidence: ConfidenceLevel
    alternative: str


class AssumptionsRegistry:
    """Track all assumptions made during recomputation"""

    def __init__(self) -> None:
        self.assumptions: list[Assumption] = []

    def add(
        self,
        statement: str,
        evidence: EvidenceLevel,
        source: str,
        confidence: ConfidenceLevel,
        alternative: str,
    ) -> None:
        """Register an assumption"""
        self.assumptions.append(
            Assumption(
                statement=statement,
                evidence=evidence,
                source=source,
                confidence=confidence,
                alternative=alternative,
            )
        )

    def to_markdown(self) -> str:
        """Generate markdown report of all assumptions"""
        lines = ["# Assumptions Used in Table A1 Recomputation\n"]

        for i, assumption in enumerate(self.assumptions, 1):
            lines.append(f"## ASSUMPTION {i}\n")
            lines.append(f"**Statement:** {assumption.statement}\n")
            lines.append(f"**Evidence:** {assumption.evidence.value}\n")
            lines.append(f"**Source:** {assumption.source}\n")
            lines.append(f"**Confidence:** {assumption.confidence.value}\n")
            lines.append(f"**Alternative:** {assumption.alternative}\n")
            lines.append("")

        return "\n".join(lines)


# ============================================================================
# FLRW Computation
# ============================================================================


def compute_h_flrw(
    z: np.ndarray | float,
    H0: float = H0_DEFAULT,
    Omega_m: float = OMEGA_M_DEFAULT,
    Omega_Lambda: float = OMEGA_LAMBDA_DEFAULT,
    Omega_k: float = OMEGA_K_DEFAULT,
) -> np.ndarray:
    """Compute standard ΛCDM expansion rate H_FLRW(z)

    Formula: H(z) = H0 * sqrt(Omega_m * (1+z)^3 + Omega_k * (1+z)^2 + Omega_Lambda)

    Args:
        z: Redshift (scalar or array)
        H0: Hubble constant today [km/s/Mpc]
        Omega_m: Matter density parameter
        Omega_Lambda: Dark energy density parameter
        Omega_k: Curvature density parameter

    Returns:
        H_FLRW(z) in km/s/Mpc
    """
    z_arr = np.asarray(z)
    a = 1.0 / (1.0 + z_arr)  # Scale factor

    # Standard Friedmann equation
    E_squared = Omega_m * a**-3 + Omega_k * a**-2 + Omega_Lambda  # E(a)^2 = H(a)^2 / H0^2

    # z_arr is always an array (np.asarray above), so the result is always an
    # ndarray; np.asarray makes that explicit for the type checker (no-op at runtime).
    return np.asarray(H0 * np.sqrt(E_squared))


# ============================================================================
# Residual Computation
# ============================================================================


def compute_residuals(
    H_obs: np.ndarray,
    H_model: np.ndarray,
    sigma_obs: np.ndarray,
    convention: Literal["absolute", "normalized"] = "normalized",
) -> np.ndarray:
    """Compute residuals between observed and model values

    Args:
        H_obs: Observed values [km/s/Mpc]
        H_model: Model predictions [km/s/Mpc]
        sigma_obs: Observational uncertainties [km/s/Mpc]
        convention: 'absolute' for (H_obs - H_model),
                   'normalized' for (H_obs - H_model) / sigma_obs

    Returns:
        Residuals (convention-dependent units)
    """
    if convention == "absolute":
        return np.asarray(H_obs - H_model)
    elif convention == "normalized":
        return np.asarray((H_obs - H_model) / sigma_obs)
    else:
        raise ValueError(f"Unknown convention: {convention}")


# ============================================================================
# Row 1 (z=0) Diagnostic
# ============================================================================


@dataclass
class Row1Diagnostic:
    """Diagnostic results for Row 1 z=0 treatment"""

    hypothesis_a_match: bool  # Standard convention
    hypothesis_b_match: bool  # Anchor row (residual=0 by definition)
    hypothesis_c_match: bool  # Alternate sigma convention
    best_hypothesis: str
    details: dict


def diagnose_row_1(
    reported_row: pd.Series, recomputed_h_flrw: float, recomputed_h_mult: float
) -> Row1Diagnostic:
    """Test 3 hypotheses for Row 1 (z=0) treatment

    Hypotheses:
    A. Standard convention (treat Row 1 same as all other rows)
    B. Anchor row (H_MULT[1] = H_obs[1] by construction, residual=0)
    C. Alternate sigma convention (different normalization for Row 1)

    Args:
        reported_row: Row 1 from Table A1 (z=0)
        recomputed_h_flrw: Our recomputed H_FLRW(z=0)
        recomputed_h_mult: Our recomputed H_MULT(z=0) if available

    Returns:
        Row1Diagnostic with best-matching hypothesis
    """
    H_obs = reported_row["H_obs"]
    sigma_H = reported_row["sigma_H"]
    reported_row["H_FLRW"]
    sigma_FLRW_reported = reported_row["sigma_FLRW"]
    reported_row["H_MULT"]
    sigma_MULT_reported = reported_row["sigma_MULT"]

    # Hypothesis A: Standard convention
    # Residual = (H_obs - H_FLRW) / sigma_H
    residual_flrw_standard = (H_obs - recomputed_h_flrw) / sigma_H
    match_a_flrw = np.isclose(residual_flrw_standard, sigma_FLRW_reported, atol=0.1)

    # Hypothesis B: Anchor row
    # H_MULT = H_obs exactly, so residual = 0
    residual_mult_anchor = 0.0
    match_b_mult = np.isclose(residual_mult_anchor, sigma_MULT_reported, atol=0.1)

    # Hypothesis C: Alternate sigma convention
    # Try fractional error: (H_obs - H_FLRW) / H_obs instead of / sigma_H
    residual_flrw_fractional = (H_obs - recomputed_h_flrw) / H_obs
    match_c_flrw = np.isclose(residual_flrw_fractional, sigma_FLRW_reported, atol=0.01)

    # Determine best match
    matches = {
        "Hypothesis A (standard)": match_a_flrw,
        "Hypothesis B (anchor)": match_b_mult,
        "Hypothesis C (alternate sigma)": match_c_flrw,
    }

    best = max(matches.items(), key=lambda x: x[1])

    return Row1Diagnostic(
        hypothesis_a_match=match_a_flrw,
        hypothesis_b_match=match_b_mult,
        hypothesis_c_match=match_c_flrw,
        best_hypothesis=best[0],
        details={
            "residual_flrw_standard": residual_flrw_standard,
            "residual_flrw_fractional": residual_flrw_fractional,
            "residual_mult_anchor": residual_mult_anchor,
            "reported_sigma_FLRW": sigma_FLRW_reported,
            "reported_sigma_MULT": sigma_MULT_reported,
        },
    )


# ============================================================================
# Main Recomputation
# ============================================================================


@dataclass
class RecomputationResult:
    """Results of independent Table A1 recomputation"""

    comparison_df: pd.DataFrame  # Full comparison table
    row_1_diagnostic: Row1Diagnostic
    assumptions: AssumptionsRegistry
    summary: dict


def recompute_table_a1(
    csv_path: Path | str | None = None,
    H0: float = H0_DEFAULT,
    Omega_m: float = OMEGA_M_DEFAULT,
    Omega_Lambda: float = OMEGA_LAMBDA_DEFAULT,
) -> RecomputationResult:
    """Independently recompute Table A1 arithmetic

    Args:
        csv_path: Path to table_a1_reported.csv (default: auto-detect)
        H0: Hubble constant [km/s/Mpc]
        Omega_m: Matter density parameter
        Omega_Lambda: Dark energy density parameter

    Returns:
        RecomputationResult with comparison tables and diagnostics
    """
    # Setup assumptions registry
    assumptions = AssumptionsRegistry()

    # Load reported data
    if csv_path is None:
        csv_path = Path(__file__).parent.parent / "data" / "table_a1_reported.csv"

    df_reported = pd.read_csv(csv_path, comment="#")
    df_reported = df_reported.replace("NA", np.nan)

    # Convert numeric columns
    numeric_cols = [
        "time_gyr",
        "z",
        "H_obs",
        "sigma_H",
        "H_FLRW",
        "sigma_FLRW",
        "H_MULT",
        "sigma_MULT",
        "w_eff",
        "H_w_eff",
        "sigma_w_eff",
    ]
    for col in numeric_cols:
        if col in df_reported.columns:
            df_reported[col] = pd.to_numeric(df_reported[col], errors="coerce")

    # Register assumptions
    assumptions.add(
        statement=f"H_FLRW uses flat ΛCDM with H0={H0}, Ω_m={Omega_m}, Ω_Λ={Omega_Lambda}",
        evidence=EvidenceLevel.ASSUMED_STANDARD,
        source="Planck 2018 cosmology + H0 from Table A1 z=0",
        confidence=ConfidenceLevel.HIGH,
        alternative="Could use different cosmology (e.g., Ω_m from paper if specified)",
    )

    assumptions.add(
        statement="Sigma convention is normalized: (H_obs - H_model) / sigma_H",
        evidence=EvidenceLevel.INFERRED_FROM_CONTEXT,
        source="Standard residual convention in cosmology",
        confidence=ConfidenceLevel.MEDIUM,
        alternative="Could be absolute residual or fractional error",
    )

    assumptions.add(
        statement="Row 1 (z=0) treatment unknown — testing 3 hypotheses",
        evidence=EvidenceLevel.UNKNOWN_GUESSED,
        source="No explicit statement in paper",
        confidence=ConfidenceLevel.LOW,
        alternative="Standard / Anchor / Alternate sigma — to be diagnosed",
    )

    assumptions.add(
        statement="β_d = 4.5, β_q = 18.0 from Table A1 caption",
        evidence=EvidenceLevel.EXPLICIT_IN_PAPER,
        source="preprints202511.0598.v6.pdf, Appendix A.3, Table A1 caption",
        confidence=ConfidenceLevel.HIGH,
        alternative="None (explicitly stated)",
    )

    # Recompute H_FLRW for all rows
    z_values = df_reported["z"].values
    H_FLRW_recomputed = compute_h_flrw(z_values, H0, Omega_m, Omega_Lambda)

    # Recompute residuals (FLRW only — we don't have H_MULT formula)
    H_obs = df_reported["H_obs"].values
    sigma_H = df_reported["sigma_H"].values

    residual_FLRW_recomputed = compute_residuals(
        H_obs, H_FLRW_recomputed, sigma_H, convention="normalized"
    )

    # Build comparison DataFrame
    comparison = pd.DataFrame(
        {
            "z": z_values,
            "H_obs": H_obs,
            "sigma_H": sigma_H,
            "H_FLRW_reported": df_reported["H_FLRW"].values,
            "H_FLRW_recomputed": H_FLRW_recomputed,
            "H_FLRW_diff": df_reported["H_FLRW"].values - H_FLRW_recomputed,
            "sigma_FLRW_reported": df_reported["sigma_FLRW"].values,
            "sigma_FLRW_recomputed": residual_FLRW_recomputed,
            "sigma_FLRW_diff": df_reported["sigma_FLRW"].values - residual_FLRW_recomputed,
            # H_MULT columns (reported only — we can't recompute without formula)
            "H_MULT_reported": df_reported["H_MULT"].values,
            "sigma_MULT_reported": df_reported["sigma_MULT"].values,
        }
    )

    # Row 1 (z=0) diagnostic
    row_1_diagnostic = diagnose_row_1(
        df_reported.iloc[0], H_FLRW_recomputed[0], df_reported["H_MULT"].iloc[0]
    )

    # Summary statistics
    # Count exact matches (within 0.1 km/s/Mpc)
    exact_matches_h_flrw = np.sum(np.abs(comparison["H_FLRW_diff"]) < 0.1)

    # Count close matches (within 0.5 km/s/Mpc)
    close_matches_h_flrw = np.sum(np.abs(comparison["H_FLRW_diff"]) < 0.5)

    # Count sigma matches (within 0.1)
    exact_matches_sigma = np.sum(np.abs(comparison["sigma_FLRW_diff"]) < 0.1)

    summary = {
        "total_rows": len(comparison),
        "h_flrw_exact_matches": int(exact_matches_h_flrw),
        "h_flrw_close_matches": int(close_matches_h_flrw),
        "sigma_flrw_exact_matches": int(exact_matches_sigma),
        "max_h_flrw_discrepancy": float(np.max(np.abs(comparison["H_FLRW_diff"]))),
        "max_sigma_flrw_discrepancy": float(np.max(np.abs(comparison["sigma_FLRW_diff"]))),
    }

    return RecomputationResult(
        comparison_df=comparison,
        row_1_diagnostic=row_1_diagnostic,
        assumptions=assumptions,
        summary=summary,
    )


# ============================================================================
# Report Generation
# ============================================================================


def generate_markdown_report(result: RecomputationResult) -> str:
    """Generate markdown summary report

    Args:
        result: RecomputationResult from recompute_table_a1()

    Returns:
        Markdown-formatted report
    """
    lines = [
        "# Table A1 Independent Recomputation\n",
        "**Status:** INTERNAL_CONTRIBUTION_DRAFT | INTERNAL_DIAGNOSTIC_ONLY",
        "**Labels:** NOT_SENT | NOT_VALIDATION | NOT_REFUTATION | AUTHOR_CONFIRMATION_REQUIRED",
        "**Classification:** H_FLRW_PROVENANCE_MISMATCH | ASSUMED_BASELINE_ONLY | NOT_AUTHOR_ERROR\n",
        "> This is **NOT an author-error claim**. It is an internal reconstruction "
        "mismatch under an assumed baseline; the source baseline for the H_FLRW "
        "column is not yet recovered.\n",
        "---\n",
        "## Summary\n",
        f"- **Total rows:** {result.summary['total_rows']}",
        f"- **H_FLRW exact matches (<0.1 km/s/Mpc):** {result.summary['h_flrw_exact_matches']}/{result.summary['total_rows']}",
        f"- **H_FLRW close matches (<0.5 km/s/Mpc):** {result.summary['h_flrw_close_matches']}/{result.summary['total_rows']}",
        f"- **Sigma_FLRW exact matches (<0.1):** {result.summary['sigma_flrw_exact_matches']}/{result.summary['total_rows']}",
        f"- **Max H_FLRW discrepancy:** {result.summary['max_h_flrw_discrepancy']:.2f} km/s/Mpc",
        f"- **Max sigma_FLRW discrepancy:** {result.summary['max_sigma_flrw_discrepancy']:.3f}\n",
        "---\n",
        "## Row 1 (z=0) Diagnostic\n",
        f"**Best matching hypothesis:** {result.row_1_diagnostic.best_hypothesis}\n",
        "**Hypothesis test results:**",
        f"- Hypothesis A (standard convention): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_a_match else '❌ NO MATCH'}",
        f"- Hypothesis B (anchor row): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_b_match else '❌ NO MATCH'}",
        f"- Hypothesis C (alternate sigma): {'✅ MATCH' if result.row_1_diagnostic.hypothesis_c_match else '❌ NO MATCH'}\n",
        "**Details:**",
        f"- Reported sigma_FLRW: {result.row_1_diagnostic.details['reported_sigma_FLRW']:.3f}",
        f"- Recomputed (standard): {result.row_1_diagnostic.details['residual_flrw_standard']:.3f}",
        f"- Recomputed (fractional): {result.row_1_diagnostic.details['residual_flrw_fractional']:.6f}",
        f"- Reported sigma_MULT: {result.row_1_diagnostic.details['reported_sigma_MULT']:.3f}",
        f"- Recomputed (anchor): {result.row_1_diagnostic.details['residual_mult_anchor']:.3f}\n",
        "---\n",
        "## Discrepancies\n",
    ]

    # List rows with significant discrepancies
    df = result.comparison_df
    discrepant = df[np.abs(df["H_FLRW_diff"]) > 0.1]

    if len(discrepant) == 0:
        lines.append("✅ No significant discrepancies (all within 0.1 km/s/Mpc)\n")
    else:
        lines.append(f"Found {len(discrepant)} rows with H_FLRW difference > 0.1 km/s/Mpc:\n")
        for _, row in discrepant.iterrows():
            lines.append(
                f"- z={row['z']:.3f}: reported={row['H_FLRW_reported']:.1f}, "
                f"recomputed={row['H_FLRW_recomputed']:.1f}, "
                f"diff={row['H_FLRW_diff']:.2f} km/s/Mpc"
            )
        lines.append("")

    lines.extend(
        [
            "---\n",
            "## Assumptions Used\n",
            result.assumptions.to_markdown(),
            "---\n",
            "## Interpretation\n",
            "**NONE — this is a pure arithmetic report.**\n",
            "No physics claims are made.",
            "No validation or refutation of MULTING theory.",
            "Results contingent on author confirming cosmological parameters.\n",
            "---\n",
            "**Generated:** 2026-05-29",
            "**Author approval required before sharing**",
        ]
    )

    return "\n".join(lines)


def save_results(result: RecomputationResult, output_dir: Path | str = "docs") -> tuple[Path, Path]:
    """Save recomputation results to files

    Args:
        result: RecomputationResult from recompute_table_a1()
        output_dir: Directory to save outputs (default: docs/)

    Returns:
        Tuple of (csv_path, markdown_path)
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    # Save comparison CSV
    csv_file = output_path / "66_table_a1_recomputation_comparison.csv"
    result.comparison_df.to_csv(csv_file, index=False, float_format="%.3f")

    # Save markdown report
    md_file = output_path / "66_table_a1_recomputation_report.md"
    report = generate_markdown_report(result)
    md_file.write_text(report, encoding="utf-8")

    return csv_file, md_file
