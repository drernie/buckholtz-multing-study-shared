"""BETA-1: Controlled AI β replication audit.

Protocol:
  Each AI service receives IDENTICAL input:
    - Galaxy Cluster Parameters table (data/beta1_responses/galaxy_cluster_parameters_v1.csv)
    - Appendix A.1 Step 5 verbatim prompt (data/beta1_responses/prompt_v1.md)
  β_d and β_q are recorded per service in data/beta1_responses/{service}_response.csv.
  This script loads responses and renders a convergence verdict.

BETA-0 reference (uncontrolled, 3 services):
  Claude: β_d=4.5,  β_q=18.0
  Gemini: β_d=4.25, β_q=8.10
  ChatGPT:β_d=0.78, β_q=0.19
  Spread: β_d 5.77×, β_q 94.7× → DIVERGE

BETA-1 tests whether controlled identical input reduces the spread.

Verdicts:
  CONVERGE:       max/min < 2.0 for BOTH β_d AND β_q
  DIVERGE:        max/min ≥ 2.0 for EITHER β_d OR β_q
  PARTIAL_D_ONLY: β_d converges (< 2×), β_q diverges (≥ 2×)
  PARTIAL_Q_ONLY: β_d diverges (≥ 2×), β_q converges (< 2×)

Status implications:
  CONVERGE  → β upgrades to AI_CONSENSUS_CANDIDATE (not DO_NOT_USE)
  DIVERGE   → confirms BETA-0; β remain DO_NOT_USE; Q3 (TJB) is critical

Labels: BETA-1 · AI_CONVERGENCE_TEST · OUR_RECONSTRUCTION
        NOT_VALIDATION · NOT_REFUTATION · NOT_MODELING · NOT_THEORY_FALSE
"""

import csv
import json
import math
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data" / "beta1_responses"
REPORTS_DIR = REPO_ROOT / "reports"

# Convergence threshold: max/min ratio
CONVERGENCE_THRESHOLD = 2.0

# Minimum services for a valid verdict
MIN_SERVICES_FOR_VERDICT = 3

# BETA-0 reference data (uncontrolled, from data/supplementary_extracted/)
BETA0_REFERENCE: dict[str, dict[str, float]] = {
    "claude_notebooklm": {"beta_d": 4.5, "beta_q": 18.0},
    "gemini": {"beta_d": 4.25, "beta_q": 8.10},
    "chatgpt": {"beta_d": 0.78, "beta_q": 0.19},
}

SAFETY_LABELS = [
    "BETA-1",
    "AI_CONVERGENCE_TEST",
    "OUR_RECONSTRUCTION",
    "NOT_VALIDATION",
    "NOT_REFUTATION",
    "NOT_MODELING",
    "NOT_THEORY_FALSE",
    "NOT_AUTHOR_CONFIRMED",
]


def spread(values: list[float]) -> float:
    """Compute max/min ratio for a list of positive values.

    Returns math.inf if any value is zero or negative (undefined spread).
    Requires at least 2 values.
    """
    if len(values) < 2:
        return math.inf
    if any(v <= 0 for v in values):
        return math.inf
    return max(values) / min(values)


def verdict_from_spreads(beta_d_spread: float, beta_q_spread: float, n_services: int) -> str:
    """Return convergence verdict string."""
    if n_services < MIN_SERVICES_FOR_VERDICT:
        return "INSUFFICIENT_SERVICES"
    d_converges = beta_d_spread < CONVERGENCE_THRESHOLD
    q_converges = beta_q_spread < CONVERGENCE_THRESHOLD
    if d_converges and q_converges:
        return "CONVERGE"
    if d_converges and not q_converges:
        return "PARTIAL_D_ONLY"
    if not d_converges and q_converges:
        return "PARTIAL_Q_ONLY"
    return "DIVERGE"


def load_responses(data_dir: Path) -> dict[str, dict[str, float]]:
    """Load all {service}_response.csv files from data_dir.

    Returns dict mapping service_name → {beta_d: float, beta_q: float}.
    Skips files with FILL_IN placeholder values (template, not filled).
    """
    responses: dict[str, dict[str, float]] = {}
    for path in sorted(data_dir.glob("*_response.csv")):
        service = path.stem.replace("_response", "")
        params: dict[str, float] = {}
        try:
            with path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(filter(lambda line: not line.startswith("#"), f)):
                    param = row.get("parameter", "").strip()
                    val_str = row.get("value", "").strip()
                    if param in ("beta_d", "beta_q") and val_str not in ("", "FILL_IN"):
                        params[param] = float(val_str)
        except (ValueError, KeyError):
            continue
        if "beta_d" in params and "beta_q" in params:
            responses[service] = params
    return responses


def _beta0_analysis() -> dict:
    """Compute BETA-0 reference spread (uncontrolled baseline)."""
    bd = [v["beta_d"] for v in BETA0_REFERENCE.values()]
    bq = [v["beta_q"] for v in BETA0_REFERENCE.values()]
    sp_d = spread(bd)
    sp_q = spread(bq)
    return {
        "services": list(BETA0_REFERENCE.keys()),
        "beta_d_values": {k: v["beta_d"] for k, v in BETA0_REFERENCE.items()},
        "beta_q_values": {k: v["beta_q"] for k, v in BETA0_REFERENCE.items()},
        "beta_d_spread": round(sp_d, 3),
        "beta_q_spread": round(sp_q, 3),
        "verdict": verdict_from_spreads(sp_d, sp_q, len(BETA0_REFERENCE)),
        "note": "UNCONTROLLED — different prompts and cluster parameters per service",
    }


def run_audit(data_dir: Path | None = None) -> dict:
    """Run BETA-1 audit. Returns results dict and writes report JSON."""
    if data_dir is None:
        data_dir = DATA_DIR

    beta0 = _beta0_analysis()
    beta1_responses = load_responses(data_dir)

    if beta1_responses:
        bd1 = [v["beta_d"] for v in beta1_responses.values()]
        bq1 = [v["beta_q"] for v in beta1_responses.values()]
        sp_d1 = spread(bd1)
        sp_q1 = spread(bq1)
        n = len(beta1_responses)
        beta1_verdict = verdict_from_spreads(sp_d1, sp_q1, n)
        beta1_status = "ANALYZED"
    else:
        sp_d1 = sp_q1 = None
        beta1_verdict = "AWAITING_RESPONSES"
        beta1_status = "AWAITING_RESPONSES"
        n = 0

    # Compare beta0 vs beta1 spread reduction (if beta1 data present)
    if sp_d1 is not None and sp_q1 is not None:
        spread_reduction_d = round(beta0["beta_d_spread"] / sp_d1, 3) if sp_d1 > 0 else None
        spread_reduction_q = round(beta0["beta_q_spread"] / sp_q1, 3) if sp_q1 > 0 else None
    else:
        spread_reduction_d = None
        spread_reduction_q = None

    results: dict = {
        "audit": "BETA-1",
        "gate": "AI_CONVERGENCE_TEST",
        "protocol_version": "v1",
        "labels": SAFETY_LABELS,
        "convergence_threshold": CONVERGENCE_THRESHOLD,
        "min_services_required": MIN_SERVICES_FOR_VERDICT,
        "beta0_reference": beta0,
        "beta1": {
            "status": beta1_status,
            "n_services": n,
            "services": list(beta1_responses.keys()),
            "beta_d_values": {k: v["beta_d"] for k, v in beta1_responses.items()}
            if beta1_responses
            else {},
            "beta_q_values": {k: v["beta_q"] for k, v in beta1_responses.items()}
            if beta1_responses
            else {},
            "beta_d_spread": round(sp_d1, 3) if sp_d1 is not None else None,
            "beta_q_spread": round(sp_q1, 3) if sp_q1 is not None else None,
            "verdict": beta1_verdict,
            "spread_reduction_d": spread_reduction_d,
            "spread_reduction_q": spread_reduction_q,
        },
        "status_implications": {
            "CONVERGE": "β upgrades to AI_CONSENSUS_CANDIDATE — controlled prompting resolves ambiguity",
            "DIVERGE": "confirms BETA-0 finding — ambiguity is intrinsic to underdetermined fitting; β remain DO_NOT_USE; Q3 critical",
            "PARTIAL_D_ONLY": "β_d robust under controlled prompting; β_q remains ambiguous",
            "PARTIAL_Q_ONLY": "β_q robust under controlled prompting; β_d remains ambiguous",
            "AWAITING_RESPONSES": "fill data/beta1_responses/{service}_response.csv and re-run",
        },
        "next_step": _next_step(beta1_verdict),
        "safety_notes": [
            "NOT modeling H_MULT(z) — β values are inputs to fitting, not predictive parameters",
            "NOT validating or refuting MULTING — this is a convergence test of AI responses",
            "NOT claiming β values are canonical — all remain AI_MEDIATED_CANDIDATE or DO_NOT_USE",
        ],
    }

    report_path = REPORTS_DIR / "beta1_controlled_replication.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results


def _next_step(verdict: str) -> str:
    if verdict == "AWAITING_RESPONSES":
        return (
            "Query each AI service with data/beta1_responses/prompt_v1.md. "
            "Record β_d and β_q in {service}_response.csv. Then re-run this script."
        )
    if verdict == "CONVERGE":
        return "β values show AI consensus under controlled prompting. Upgrade status to AI_CONSENSUS_CANDIDATE. Share with TJB as Q3 context."
    if verdict == "DIVERGE":
        return "β divergence confirmed as intrinsic to underdetermined fitting. β remain DO_NOT_USE. Q3 (TJB author values) is now the only resolution path."
    if verdict in ("PARTIAL_D_ONLY", "PARTIAL_Q_ONLY"):
        return "Partial convergence. Investigate which cluster variables drive remaining divergence. Consider follow-up BETA-1b with fixed k_A."
    return "Collect more service responses (minimum 3 required)."


if __name__ == "__main__":
    results = run_audit()
    verdict = results["beta1"]["verdict"]
    status = results["beta1"]["status"]
    print("\nBETA-1 Controlled Replication Audit")
    print(f"Status:  {status}")
    print(f"Verdict: {verdict}")
    if results["beta1"]["n_services"] > 0:
        print(
            f"Services ({results['beta1']['n_services']}): {', '.join(results['beta1']['services'])}"
        )
        print(
            f"β_d spread: {results['beta1']['beta_d_spread']}×  (threshold < {CONVERGENCE_THRESHOLD}×)"
        )
        print(
            f"β_q spread: {results['beta1']['beta_q_spread']}×  (threshold < {CONVERGENCE_THRESHOLD}×)"
        )
    print(
        f"\nBETA-0 reference: β_d {results['beta0_reference']['beta_d_spread']}×, β_q {results['beta0_reference']['beta_q_spread']}× → {results['beta0_reference']['verdict']}"
    )
    print(f"\nNext step: {results['next_step']}")
    print("\nReport written to: reports/beta1_controlled_replication.json")
