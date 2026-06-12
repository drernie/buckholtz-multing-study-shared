"""M7-B 5:1 dark-isomer ratio audit.

Claim (paper Sec 2.6/2.9/4.5; canonical source lines 767-772, 980-981, 1340+):
  5 dark isomers : 1 ordinary isomer -> "(5+):1" dark:ordinary ratios;
  author himself cites the observed "(~5.4):1" density ratio (line 772).

Question: does 5-isomer counting PREDICT Omega_DM/Omega_b, or is it an
integer-counting match with the excess ("pluses") unexplained?

Labels: NOT_VALIDATION / NOT_REFUTATION / M7_DARK_ISOMER_AUDIT /
        INTEGER_COUNTING_CHECK / COSMOLOGY_RATIO_CHECK / AUTHOR_DERIVATION_NEEDED
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CLAIMED_INTEGER = 5.0  # 5 dark isomers / 1 OM isomer

# Observed ratio — author's own figure (local source line 772): (~5.4):1
AUTHOR_CITED = 5.4

# EXTERNAL_STANDARD_PHYSICS cross-check (Planck 2018: Om_c h2=0.1200+-0.0012,
# Om_b h2=0.02237+-0.00015 -> ratio 5.364 +- ~0.065)
PLANCK_RATIO = 5.364
PLANCK_SIGMA = 0.065

# Sanity note: isomer neutron-like baryons are heavier than H-atom by ~0.08%
# (m_n - m_p - m_e = 0.782 MeV / 938.8 MeV); equal-number counting would lift
# each dark isomer's mass density by only ~0.0008 — irrelevant vs the 7% gap.
NEUTRON_MASS_SHIFT_FRACTION = (939.5654 - 938.2721 - 0.5110) / (938.2721 + 0.5110)


def main() -> dict:
    diff_author = AUTHOR_CITED - CLAIMED_INTEGER
    diff_planck = PLANCK_RATIO - CLAIMED_INTEGER
    out = {
        "test": "M7-B 5:1 dark-isomer ratio audit",
        "labels": [
            "NOT_VALIDATION", "NOT_REFUTATION", "M7_DARK_ISOMER_AUDIT",
            "INTEGER_COUNTING_CHECK", "COSMOLOGY_RATIO_CHECK",
            "AUTHOR_DERIVATION_NEEDED",
        ],
        "claim_source_lines": [767, 768, 769, 772, 980, 981, 1340],
        "claimed_integer_ratio": CLAIMED_INTEGER,
        "observed": {
            "author_cited_line772": AUTHOR_CITED,
            "planck2018_crosscheck": {
                "ratio": PLANCK_RATIO, "sigma": PLANCK_SIGMA,
                "provenance": "EXTERNAL_STANDARD_PHYSICS (Planck 2018 Om_c/Om_b)",
            },
        },
        "comparison": {
            "abs_diff_vs_author_cited": diff_author,
            "pct_diff_vs_author_cited": diff_author / AUTHOR_CITED * 100,
            "abs_diff_vs_planck": diff_planck,
            "pct_diff_vs_planck": diff_planck / PLANCK_RATIO * 100,
            "pull_sigma_vs_planck": diff_planck / PLANCK_SIGMA,
        },
        "derivation_check": {
            "equal_density_per_isomer_derived": False,
            "thermal_history_provided": False,
            "note": (
                "Paper posits 6 isomer particle sets but provides no mechanism "
                "fixing EQUAL cosmological density per isomer (no isomer-level "
                "baryogenesis/thermal history). Sec 4.5 lists speculative "
                "options for the '+' excess (axions, reach-6 energy outflow, "
                "non-decaying neutral baryon analogs, neutrino-analog density) "
                "without quantitative derivation."
            ),
            "author_acknowledges_gap": True,
        },
        "sanity_note_neutron_mass_shift": {
            "fraction": NEUTRON_MASS_SHIFT_FRACTION,
            "comment": (
                "Even if every dark isomer is purely neutron-like, equal baryon "
                "number gives only ~+0.08% mass density per isomer — cannot "
                "supply the ~7% excess (5.0 -> 5.36)."
            ),
        },
        "interpretation": "approximate post-hoc integer-counting match",
        "verdict": "PARTIAL",
        "verdict_reason": (
            "Integer counting (5 dark isomers) lands ~7% below the observed "
            "ratio (5.36-5.4); literal 5.0 is ~5.6 sigma from the Planck "
            "cross-check, and the paper's '(5+):1' phrasing absorbs the gap "
            "into unquantified 'pluses'. No physical derivation fixes equal "
            "density per isomer; thermal history absent (author acknowledges "
            "via Sec 4.5 speculative options). Numerical closeness is not a "
            "derivation; claim survives only as a candidate counting basis."
        ),
    }
    return out


if __name__ == "__main__":
    result = main()
    (ROOT / "reports" / "m7_b_5to1_dark_isomer_ratio_audit.json").write_text(
        json.dumps(result, indent=2)
    )
    print(json.dumps(result, indent=2))
