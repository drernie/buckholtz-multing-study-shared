"""SAFE_NOW negative-control diagnostics for MULTING Table A1 specificity.

Safety labels:
- INTERNAL_ONLY
- DIAGNOSTIC_ONLY
- SAFE_NOW
- NO_VALIDATION
- NO_REFUTATION
- NO_MCMC
- NO_PUBLIC_CLAIMS
- AUTHOR_NOT_REQUIRED

This module intentionally does not implement or infer a physical F_oP -> H_MULT(z)
bridge. It uses the extracted Table A1 H_MULT column as a reported-table surrogate
for deterministic specificity diagnostics.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

RANDOM_SEED = 20260531
N_SHUFFLES = 100
N_RANDOM_BETA = 100

DIAGNOSTIC_LABELS = {"PASS", "WARN", "FAIL", "INCONCLUSIVE"}
BREAKTHROUGH_CLASSIFICATIONS = {
    "STRONG_SPECIFICITY_SIGNAL",
    "PARTIAL_SPECIFICITY",
    "NON_SPECIFIC_REPRODUCTION",
    "METHOD_FAILURE_AS_DISCOVERY",
    "INCONCLUSIVE",
}

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TABLE_A1_PATH = REPO_ROOT / "data" / "table_a1_reported.csv"

SAFETY_LABELS = [
    "INTERNAL_ONLY",
    "DIAGNOSTIC_ONLY",
    "SAFE_NOW",
    "NO_VALIDATION",
    "NO_REFUTATION",
    "NO_MCMC",
    "NO_PUBLIC_CLAIMS",
    "AUTHOR_NOT_REQUIRED",
]

REQUIRED_INPUTS = [
    ("docs/87_negative_control_test_plan.md", "Negative-control planning context"),
    ("docs/90_multing_physical_verification_upgrade_plan.md", "Optional physical upgrade plan"),
    ("src/table_a1_independent_recomputation.py", "Existing recomputation helpers"),
    ("docs/68_hflrw_provenance_recovery.md", "H_FLRW provenance context"),
    ("docs/81_multi_ai_reproducibility_comparison.md", "Multi-AI comparison context"),
    ("data/table_a1_reported.csv", "Table A1 reported values"),
]


@dataclass(frozen=True)
class TableA1Data:
    """Minimal numeric Table A1 fields used by SAFE_NOW diagnostics."""

    source_path: str
    z: np.ndarray
    h_obs: np.ndarray
    sigma_h: np.ndarray
    h_flrw: np.ndarray
    h_mult: np.ndarray
    beta_d: float
    beta_q: float


@dataclass(frozen=True)
class InputRecord:
    """Input-file provenance record for report output."""

    file: str
    found: bool
    role: str
    notes: str


@dataclass(frozen=True)
class DiagnosticResult:
    """Single diagnostic result."""

    name: str
    metric_name: str
    original_value: float | None
    control_values: tuple[float, ...]
    label: str
    interpretation: str
    metrics: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class BatteryResult:
    """Full negative-control battery result."""

    test_id: str
    status: str
    random_seed: int
    n_shuffles: int
    n_random_beta: int
    inputs: tuple[InputRecord, ...]
    row_permutation: DiagnosticResult
    randomized_beta: DiagnosticResult
    synthetic_lcdm: DiagnosticResult
    breakthrough_classification: str
    next_recommended_step: str


def load_table_a1_data(path: Path | str = DEFAULT_TABLE_A1_PATH) -> TableA1Data:
    """Load reported Table A1 data from CSV.

    The CSV contains comment metadata; pandas skips those comment rows.
    """
    source = Path(path)
    df = pd.read_csv(source, comment="#")
    required = ["z", "H_obs", "sigma_H", "H_FLRW", "H_MULT"]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required Table A1 columns: {missing}")

    z = df["z"].to_numpy(dtype=float)
    order = np.argsort(z)
    return TableA1Data(
        source_path=str(source),
        z=z[order],
        h_obs=df["H_obs"].to_numpy(dtype=float)[order],
        sigma_h=df["sigma_H"].to_numpy(dtype=float)[order],
        h_flrw=df["H_FLRW"].to_numpy(dtype=float)[order],
        h_mult=df["H_MULT"].to_numpy(dtype=float)[order],
        beta_d=4.5,
        beta_q=18.0,
    )


def normalized_rmse(observed: np.ndarray, predicted: np.ndarray, sigma: np.ndarray) -> float:
    """Compute normalized RMSE; lower is better."""
    residual = (np.asarray(predicted) - np.asarray(observed)) / np.asarray(sigma)
    return float(np.sqrt(np.mean(residual**2)))


def reported_h_mult_surrogate(data: TableA1Data, target_z: np.ndarray) -> np.ndarray:
    """Interpolate the reported H_MULT table values onto target z values.

    This is not a physical bridge. It is a deterministic reported-table surrogate
    used to test whether the extracted table curve is specific to its z structure.
    """
    return np.interp(target_z, data.z, data.h_mult)


def label_fraction_as_good_or_better(fraction: float) -> str:
    """Label row-permutation diagnostic result."""
    if fraction < 0.05:
        return "PASS"
    if fraction < 0.20:
        return "WARN"
    return "FAIL"


def label_random_beta_percentile(percentile: float | None) -> str:
    """Label randomized beta result."""
    if percentile is None or np.isnan(percentile):
        return "INCONCLUSIVE"
    if percentile >= 95.0:
        return "PASS"
    if percentile >= 80.0:
        return "WARN"
    return "FAIL"


def label_synthetic_ratio(ratio: float | None) -> str:
    """Label synthetic Lambda-CDM specificity result."""
    if ratio is None or np.isnan(ratio):
        return "INCONCLUSIVE"
    if ratio > 3.0:
        return "PASS"
    if ratio >= 1.5:
        return "WARN"
    return "FAIL"


def run_row_permutation_control(
    data: TableA1Data | None = None,
    seed: int = RANDOM_SEED,
    n_shuffles: int = N_SHUFFLES,
) -> DiagnosticResult:
    """Run deterministic row-permutation negative control."""
    data = data or load_table_a1_data()
    rng = np.random.default_rng(seed)
    original_metric = normalized_rmse(data.h_obs, data.h_mult, data.sigma_h)
    control_metrics: list[float] = []

    for _ in range(n_shuffles):
        shuffled_z = rng.permutation(data.z)
        predicted = reported_h_mult_surrogate(data, shuffled_z)
        control_metrics.append(normalized_rmse(data.h_obs, predicted, data.sigma_h))

    controls = np.asarray(control_metrics, dtype=float)
    fraction = float(np.mean(controls <= original_metric))
    label = label_fraction_as_good_or_better(fraction)
    interpretation = {
        "PASS": "Original table appears more structured than shuffled controls.",
        "WARN": "Some specificity signal, but not strong under shuffled controls.",
        "FAIL": "Shuffled controls fit too often; specificity is weak.",
    }[label]

    return DiagnosticResult(
        name="row_permutation_negative_control",
        metric_name="fraction_as_good_or_better",
        original_value=original_metric,
        control_values=tuple(float(value) for value in controls),
        label=label,
        interpretation=interpretation,
        metrics={
            "fraction_as_good_or_better": fraction,
            "control_min": float(np.min(controls)),
            "control_median": float(np.median(controls)),
            "control_max": float(np.max(controls)),
        },
    )


def derive_beta_ranges_from_reported_values(
    reported_pairs: tuple[tuple[float, float], ...] = ((0.78, 0.19), (4.5, 18.0), (4.25, 8.10)),
) -> tuple[tuple[float, float], tuple[float, float]]:
    """Derive conservative diagnostic beta ranges from reported AI-service values."""
    beta_d_values = np.array([pair[0] for pair in reported_pairs], dtype=float)
    beta_q_values = np.array([pair[1] for pair in reported_pairs], dtype=float)
    return (
        (float(np.min(beta_d_values)), float(np.max(beta_d_values))),
        (float(np.min(beta_q_values)), float(np.max(beta_q_values))),
    )


def run_randomized_beta_diagnostic(
    data: TableA1Data | None = None,
    seed: int = RANDOM_SEED,
    n_random_beta: int = N_RANDOM_BETA,
) -> DiagnosticResult:
    """Run randomized beta diagnostic scaffold.

    No source-confirmed beta -> H_MULT(z) routine exists in the current project.
    To avoid inventing physics, this diagnostic samples beta pairs deterministically
    for reproducibility but labels the specificity result INCONCLUSIVE.
    """
    data = data or load_table_a1_data()
    rng = np.random.default_rng(seed)
    beta_d_range, beta_q_range = derive_beta_ranges_from_reported_values()
    beta_d_samples = rng.uniform(beta_d_range[0], beta_d_range[1], size=n_random_beta)
    beta_q_samples = rng.uniform(beta_q_range[0], beta_q_range[1], size=n_random_beta)

    sampled_pairs = tuple(
        (float(beta_d), float(beta_q)) for beta_d, beta_q in zip(beta_d_samples, beta_q_samples)
    )

    return DiagnosticResult(
        name="randomized_beta_diagnostic",
        metric_name="reported_beta_percentile",
        original_value=None,
        control_values=(),
        label="INCONCLUSIVE",
        interpretation=(
            "No source-confirmed beta-to-H_MULT routine is available; random beta "
            "samples are reproducible, but beta specificity cannot be evaluated."
        ),
        metrics={
            "reported_beta_d": data.beta_d,
            "reported_beta_q": data.beta_q,
            "beta_d_range": beta_d_range,
            "beta_q_range": beta_q_range,
            "sampled_pairs_preview": sampled_pairs[:5],
            "reason": "<unknown>beta-to-H_MULT routine not available</unknown>",
        },
    )


def generate_synthetic_lcdm(
    z: np.ndarray,
    h0: float = 70.0,
    omega_m: float = 0.3,
    omega_lambda: float = 0.7,
    omega_k: float = 0.0,
) -> np.ndarray:
    """Generate deterministic synthetic flat/non-flat Lambda-CDM H(z)."""
    z_arr = np.asarray(z, dtype=float)
    e_squared = (
        omega_m * (1.0 + z_arr) ** 3
        + omega_k * (1.0 + z_arr) ** 2
        + omega_lambda
    )
    return h0 * np.sqrt(e_squared)


def run_synthetic_lcdm_specificity_test(data: TableA1Data | None = None) -> DiagnosticResult:
    """Compare reported H_MULT surrogate fit to original vs synthetic Lambda-CDM table."""
    data = data or load_table_a1_data()
    original_metric = normalized_rmse(data.h_obs, data.h_mult, data.sigma_h)
    synthetic_h = generate_synthetic_lcdm(data.z)
    synthetic_metric = normalized_rmse(synthetic_h, data.h_mult, data.sigma_h)
    ratio = float(synthetic_metric / original_metric) if original_metric > 0 else np.nan
    label = label_synthetic_ratio(ratio)
    interpretation = {
        "PASS": "Synthetic Lambda-CDM table is distinguishable under the reported-table surrogate.",
        "WARN": "Synthetic Lambda-CDM table is partially distinguishable under the surrogate.",
        "FAIL": "Synthetic Lambda-CDM table is reproduced about as well as the original.",
        "INCONCLUSIVE": "Synthetic Lambda-CDM specificity could not be evaluated.",
    }[label]

    return DiagnosticResult(
        name="synthetic_lcdm_specificity_test",
        metric_name="synthetic_to_original_metric_ratio",
        original_value=original_metric,
        control_values=(float(synthetic_metric),),
        label=label,
        interpretation=interpretation,
        metrics={
            "synthetic_metric": float(synthetic_metric),
            "ratio": ratio,
            "h0": 70.0,
            "omega_m": 0.3,
            "omega_lambda": 0.7,
            "omega_k": 0.0,
        },
    )


def collect_input_records(repo_root: Path = REPO_ROOT) -> tuple[InputRecord, ...]:
    """Collect input-file presence records for the report."""
    records: list[InputRecord] = []
    for relative_path, role in REQUIRED_INPUTS:
        path = repo_root / relative_path
        found = path.exists()
        notes = "available" if found else "<unknown>file not found</unknown>"
        records.append(InputRecord(file=relative_path, found=found, role=role, notes=notes))
    return tuple(records)


def classify_breakthrough_candidate(results: tuple[DiagnosticResult, ...]) -> str:
    """Classify combined diagnostic outcome without validation/refutation language."""
    labels = [result.label for result in results]
    decisive_labels = [label for label in labels if label != "INCONCLUSIVE"]

    if not decisive_labels:
        return "INCONCLUSIVE"
    if all(label == "PASS" for label in labels):
        return "STRONG_SPECIFICITY_SIGNAL"
    if all(label == "FAIL" for label in decisive_labels) and len(decisive_labels) == len(labels):
        return "METHOD_FAILURE_AS_DISCOVERY"
    if "FAIL" in decisive_labels:
        return "NON_SPECIFIC_REPRODUCTION"
    if "PASS" in decisive_labels or "WARN" in decisive_labels:
        return "PARTIAL_SPECIFICITY"
    return "INCONCLUSIVE"


def choose_next_step(classification: str) -> str:
    """Choose exactly one next recommended step."""
    if classification == "STRONG_SPECIFICITY_SIGNAL":
        return "Fisher identifiability pre-analysis"
    if classification in {"NON_SPECIFIC_REPRODUCTION", "METHOD_FAILURE_AS_DISCOVERY"}:
        return "model-selection protocol"
    if classification == "PARTIAL_SPECIFICITY":
        return "systematics budget"
    return "stop and ask author clarification"


def run_negative_control_battery(
    seed: int = RANDOM_SEED,
    n_shuffles: int = N_SHUFFLES,
    n_random_beta: int = N_RANDOM_BETA,
    table_path: Path | str = DEFAULT_TABLE_A1_PATH,
) -> BatteryResult:
    """Run all SAFE_NOW diagnostics deterministically."""
    data = load_table_a1_data(table_path)
    row = run_row_permutation_control(data, seed=seed, n_shuffles=n_shuffles)
    beta = run_randomized_beta_diagnostic(data, seed=seed, n_random_beta=n_random_beta)
    synthetic = run_synthetic_lcdm_specificity_test(data)
    classification = classify_breakthrough_candidate((row, beta, synthetic))

    return BatteryResult(
        test_id="negative_control_battery_001",
        status="completed_or_partial",
        random_seed=seed,
        n_shuffles=n_shuffles,
        n_random_beta=n_random_beta,
        inputs=collect_input_records(),
        row_permutation=row,
        randomized_beta=beta,
        synthetic_lcdm=synthetic,
        breakthrough_classification=classification,
        next_recommended_step=choose_next_step(classification),
    )


def _format_float(value: float | None) -> str:
    if value is None or np.isnan(value):
        return "NA"
    return f"{value:.6g}"


def _control_distribution_summary(result: DiagnosticResult) -> str:
    if result.name == "row_permutation_negative_control":
        return (
            f"min={result.metrics['control_min']:.4g}, "
            f"median={result.metrics['control_median']:.4g}, "
            f"max={result.metrics['control_max']:.4g}"
        )
    if result.name == "randomized_beta_diagnostic":
        return result.metrics["reason"]
    if result.name == "synthetic_lcdm_specificity_test":
        return f"synthetic_metric={result.metrics['synthetic_metric']:.4g}"
    return "NA"


def generate_markdown_report(result: BatteryResult) -> str:
    """Generate required markdown report."""
    diagnostics = [result.row_permutation, result.randomized_beta, result.synthetic_lcdm]
    lines: list[str] = [
        "# Negative-Control Diagnostics for MULTING Table Specificity",
        "",
        "## Safety labels",
        "",
        *SAFETY_LABELS,
        "",
        "## 1. Purpose",
        "",
        (
            "This is a specificity diagnostic for extracted MULTING/Table A1 values. "
            "It is diagnostic-only work and cannot support validation or refutation of "
            "MULTING, FLRW, w_eff, or any physical bridge."
        ),
        "",
        "## 2. Inputs",
        "",
        "| File | Found? | Role | Notes |",
        "|---|---|---|---|",
    ]

    for record in result.inputs:
        lines.append(
            f"| `{record.file}` | {'YES' if record.found else 'NO'} | {record.role} | {record.notes} |"
        )

    lines.extend(
        [
            "",
            "## 3. Method",
            "",
            f"- Random seed: `{result.random_seed}`.",
            f"- Row-permutation control: `{result.n_shuffles}` fixed-seed permutations.",
            (
                "- Randomised beta diagnostic: deterministic beta samples from reported-value "
                "ranges; labelled INCONCLUSIVE because no beta-to-H_MULT routine is source-confirmed."
            ),
            (
                "- Synthetic Lambda-CDM test: H0=70.0, Omega_m=0.3, "
                "Omega_lambda=0.7, Omega_k=0.0 on the Table A1 z-grid."
            ),
            "- Metric: normalized RMSE using the extracted H uncertainty column.",
            "- Thresholds: row permutation uses 0.05/0.20 fraction gates; synthetic test uses ratio >3 PASS and >=1.5 WARN.",
            "",
            "## 4. Results",
            "",
            "| Test | Metric | Original | Control distribution | Diagnostic label | Interpretation |",
            "|---|---:|---:|---|---|---|",
        ]
    )

    for diagnostic in diagnostics:
        metric_value = diagnostic.metrics.get(diagnostic.metric_name)
        if metric_value is None and diagnostic.name == "synthetic_lcdm_specificity_test":
            metric_value = diagnostic.metrics.get("ratio")
        lines.append(
            "| "
            f"{diagnostic.name} | "
            f"{diagnostic.metric_name}={_format_float(float(metric_value)) if metric_value is not None else 'NA'} | "
            f"{_format_float(diagnostic.original_value)} | "
            f"{_control_distribution_summary(diagnostic)} | "
            f"{diagnostic.label} | "
            f"{diagnostic.interpretation} |"
        )

    lines.extend(
        [
            "",
            "## 5. Breakthrough candidate assessment",
            "",
            f"Classification: **{result.breakthrough_classification}**",
            "",
            (
                "Allowed wording: this result may raise or lower confidence in specificity "
                "and may justify follow-up diagnostics. It does not validate or refute a model."
            ),
            "",
            "## 6. What this means",
            "",
            "- This raises or lowers confidence in table specificity only.",
            "- This can support or weaken the case for further testing.",
            "- This may justify Fisher/model-selection follow-up if specificity is strong enough.",
            "- This may indicate that the reproduction method is too flexible if controls perform well.",
            "",
            "Forbidden interpretations:",
            "- MULTING is validated.",
            "- MULTING is refuted.",
            "- Buckholtz is right or wrong.",
            "- Any AI service is correct.",
            "",
            "## 7. Limitations",
            "",
            "- No MCMC.",
            "- No out-of-sample cosmological data.",
            "- No author-confirmed F_oP -> H_MULT bridge.",
            "- Beta provenance remains unresolved.",
            "- The randomised beta diagnostic is inconclusive without a beta-to-H_MULT routine.",
            "- Diagnostic-only status.",
            "",
            "## 8. Next recommended step",
            "",
            result.next_recommended_step,
            "",
            "## 9. Reproducibility manifest",
            "",
            "```yaml",
            "test_id: negative_control_battery_001",
            f"status: {result.status}",
            "claim_boundary: diagnostic_only",
            f"random_seed: {result.random_seed}",
            f"n_shuffles: {result.n_shuffles}",
            f"n_random_beta: {result.n_random_beta}",
            "input_files:",
        ]
    )

    for record in result.inputs:
        lines.append(f"  - file: {record.file}")
        lines.append(f"    found: {str(record.found).lower()}")

    lines.extend(
        [
            "outputs:",
            "  - docs/91_negative_control_results.md",
            "tests:",
            f"  row_permutation: {result.row_permutation.label}",
            f"  randomized_beta: {result.randomized_beta.label}",
            f"  synthetic_lcdm: {result.synthetic_lcdm.label}",
            "can_support_validation: false",
            "can_support_refutation: false",
            "can_support_public_claim: false",
            "```",
            "",
        ]
    )

    return "\n".join(lines)


def write_markdown_report(result: BatteryResult, path: Path | str) -> Path:
    """Write markdown report to disk."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(generate_markdown_report(result), encoding="utf-8")
    return output_path


def main() -> None:
    """Run the battery and write the project report."""
    result = run_negative_control_battery()
    write_markdown_report(result, REPO_ROOT / "docs" / "91_negative_control_results.md")


if __name__ == "__main__":
    main()
