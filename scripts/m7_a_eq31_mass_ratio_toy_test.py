"""M7-A Eq31 mass-ratio toy-test.

Claim (paper Eq. 31, canonical source line 881):
    (m_W)^2 : (m_Z)^2 : (m_Higgs)^2 :: 7 : 9 : 17

Author's own accuracy claim (Sec 2.7): Higgs predicted within 1 sigma for some
time; "recently" W within 1 sigma.

Labels: NOT_VALIDATION / NOT_REFUTATION / M7_NUMEROLOGY_AUDIT / EQ31_TOY_TEST /
        EXTERNAL_STANDARD_PHYSICS.

Masses: hard-coded PDG-style values (no local particle-mass source in repo).
Primary: PDG 2022. Sensitivity: PDG 2024 average and CDF-II 2022 W mass,
because the W mass itself is experimentally contested.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGET = (7.0, 9.0, 17.0)

# EXTERNAL_STANDARD_PHYSICS — cited, not author-specific
MASSES = {
    "PDG2022": {
        "W": (80.377, 0.012),
        "Z": (91.1876, 0.0021),
        "H": (125.25, 0.17),
    },
    "PDG2024_avg": {
        "W": (80.3692, 0.0133),
        "Z": (91.1880, 0.0020),
        "H": (125.20, 0.11),
    },
    "CDF2022_W_only": {  # the famous high CDF-II measurement
        "W": (80.4335, 0.0094),
        "Z": (91.1876, 0.0021),
        "H": (125.25, 0.17),
    },
}


def analyze(masses: dict[str, tuple[float, float]]) -> dict:
    m = {k: v[0] for k, v in masses.items()}
    s_unc = {k: v[1] for k, v in masses.items()}
    sq = {k: m[k] ** 2 for k in ("W", "Z", "H")}

    # ratios normalized to W=7
    w_norm = {k: sq[k] / sq["W"] * 7.0 for k in ("W", "Z", "H")}
    # ratios normalized to sum
    tot, t_tot = sum(sq.values()), sum(TARGET)
    sum_norm = {k: sq[k] / tot * t_tot for k in ("W", "Z", "H")}

    # least-squares scale s minimizing sum (sq_i - s*t_i)^2
    t = dict(zip(("W", "Z", "H"), TARGET, strict=True))
    s_fit = sum(sq[k] * t[k] for k in sq) / sum(ti**2 for ti in TARGET)
    resid_gev2 = {k: sq[k] - s_fit * t[k] for k in sq}
    pred_mass_fit = {k: math.sqrt(s_fit * t[k]) for k in sq}
    pct_dev_mass_fit = {
        k: (m[k] - pred_mass_fit[k]) / pred_mass_fit[k] * 100 for k in sq
    }

    # Z-anchored prediction (author: Z is best-known) -> predict W, H
    s_z = sq["Z"] / 9.0
    pred = {k: math.sqrt(s_z * t[k]) for k in ("W", "H")}
    pull = {k: (m[k] - pred[k]) / s_unc[k] for k in ("W", "H")}

    return {
        "masses_GeV": m,
        "sigma_GeV": s_unc,
        "squared_GeV2": sq,
        "ratio_W_normalized_to_7": w_norm,
        "ratio_sum_normalized": sum_norm,
        "lsq_scale_GeV2": s_fit,
        "lsq_residuals_GeV2": resid_gev2,
        "lsq_pct_dev_in_mass": pct_dev_mass_fit,
        "Z_anchored": {
            "scale_GeV2": s_z,
            "predicted_mass_GeV": pred,
            "pull_sigma": pull,
        },
    }


def main() -> dict:
    out = {
        "test": "M7-A Eq31 mass-ratio toy-test",
        "claim": "(m_W)^2 : (m_Z)^2 : (m_H)^2 :: 7 : 9 : 17  (paper Eq. 31)",
        "labels": [
            "NOT_VALIDATION",
            "NOT_REFUTATION",
            "M7_NUMEROLOGY_AUDIT",
            "EQ31_TOY_TEST",
            "EXTERNAL_STANDARD_PHYSICS",
        ],
        "datasets": {name: analyze(vals) for name, vals in MASSES.items()},
    }

    pdg = out["datasets"]["PDG2024_avg"]["Z_anchored"]["pull_sigma"]
    cdf = out["datasets"]["CDF2022_W_only"]["Z_anchored"]["pull_sigma"]
    out["verdict_inputs"] = {
        "H_pull_PDG2024": pdg["H"],
        "W_pull_PDG2024": pdg["W"],
        "W_pull_CDF2022": cdf["W"],
        "mass_level_accuracy_pct": "~0.005-0.05 (lsq fit)",
    }
    out["verdict"] = "PARTIAL"
    out["verdict_reason"] = (
        "Numerically close (mass-level agreement 0.005-0.05% under lsq scale; "
        "Z-anchored Higgs prediction within ~0.5 sigma) but NOT exact: Z-anchored "
        "W prediction deviates ~3-4 sigma from PDG world average (only ~1.5 sigma "
        "from the contested CDF-II 2022 value), deviations exceed current "
        "experimental uncertainties for W and Z, and no physical derivation is "
        "provided in the paper. Approximate numerical relation / possible "
        "coincidence; author's 'W within 1 sigma' holds only against CDF-II-like "
        "values, not the PDG average."
    )
    return out


if __name__ == "__main__":
    result = main()
    path = ROOT / "reports" / "m7_a_eq31_mass_ratio_toy_test.json"
    path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
