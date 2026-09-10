"""E17 ADDENDUM 4 -- closes ADDENDUM3's own named "SOURCE_NOT_FOUND" gap:
a real, cluster-scale-specific sigma(log10 c) value, found this session by
reading the actual PDF of Groener, Goldberg & Sereno (2015),
"The Galaxy Cluster Concentration-Mass Scaling Relation" (arXiv:1510.01961),
Table 2 -- not extractable via the arxiv MCP's LaTeX-to-text conversion
(complex deluxetable environment did not survive conversion; confirmed by
three failed extraction attempts: get_paper_latex_section returned prose
around the table but not its numeric rows, and search_paper_text found
zero passages for "sigma_int", "Table 2 best-fit...", and "intrinsic
scatter dex" -- all failed the same way, pointing at the conversion step,
not the search). Read directly from the user-supplied PDF (page 6, visual
extraction) instead.

Real numbers, Table 2, sigma_int column (their footnote 5: "Equivalent to
the scatter in log c_vir reported in previous studies" -- exactly
sigma(log10 c), the quantity this whole thread has been after):

  CM      N_cl=63   sigma_int=0.242
  LOSVD   N_cl=58   sigma_int=0.228
  X-ray   N_cl=149  sigma_int=0.160   <- closest method to Mahdavi 2013's own
  WL      N_cl=93   sigma_int=0.118
  WL+SL   N_cl=57   sigma_int=0.130
  SL      N_cl=10   sigma_int=0.246
  All     N_cl=293  sigma_int=0.146

Sample is genuinely cluster-scale (Table 1 of that paper: M_vir mostly
10^14-10^17 Msun), unlike Duffy et al. (2008)'s own group-to-cluster
calibration range this project used by default.

This re-evaluates ADDENDUM3's own sigma_sweep() at these real values
instead of the arbitrary +/-0.05 dex bracket around Duffy's 0.15, turning
"a stated range, not a corrected point estimate" into an actual
literature-grounded number.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "20260803-bridge"))

from E17_addendum3_sigma_sweep_and_exclusion_decomposition import (  # noqa: E402
    FOCUS_POWER,
    FOCUS_Z,
    SECOND_Z,
    divergence,
    sigma_sweep,
)

# [VERIFIED-PDF] Groener, Goldberg & Sereno (2015), arXiv:1510.01961, Table 2
REAL_SIGMA_INT = {
    "X-ray (closest method to Mahdavi 2013's own)": 0.160,
    "All methods combined": 0.146,
    "WL": 0.118,
    "WL+SL": 0.130,
    "CM": 0.242,
    "LOSVD": 0.228,
    "SL": 0.246,
}
DUFFY_2008_VALUE = 0.15  # this project's own default, for comparison


def main() -> None:
    print("=" * 100)
    print("E17 ADDENDUM 4 -- real cluster-scale sigma(log10 c) from Groener, Goldberg & Sereno")
    print("(2015), arXiv:1510.01961, Table 2 -- replacing the arbitrary +/-0.05 dex bracket")
    print("=" * 100)

    sigma_values = tuple(sorted(set(list(REAL_SIGMA_INT.values()) + [DUFFY_2008_VALUE])))
    sweep = sigma_sweep(sigma_values=sigma_values, zs=(FOCUS_Z, SECOND_Z))

    base_div_233 = divergence(
        sweep[DUFFY_2008_VALUE][0][FOCUS_Z], sweep[DUFFY_2008_VALUE][1][FOCUS_POWER][FOCUS_Z]
    )
    base_div_200 = divergence(
        sweep[DUFFY_2008_VALUE][0][SECOND_Z], sweep[DUFFY_2008_VALUE][1][FOCUS_POWER][SECOND_Z]
    )
    print(f"\nReference (this project's prior default, Duffy 2008 sigma={DUFFY_2008_VALUE}):")
    print(f"  div(z=2.33)={base_div_233:.3f}  div(z=2.00)={base_div_200:.3f}")

    print(
        f"\n{'source':<45} {'sigma':>7} {'div(z=2.33)':>12} {'shift vs Duffy':>15} {'div(z=2.00)':>12}"
    )
    for label, sigma in sorted(REAL_SIGMA_INT.items(), key=lambda kv: kv[1]):
        off, jen, _excl, _c = sweep[sigma]
        div_233 = divergence(off[FOCUS_Z], jen[FOCUS_POWER][FOCUS_Z])
        div_200 = divergence(off[SECOND_Z], jen[FOCUS_POWER][SECOND_Z])
        shift = 100 * (div_233 / base_div_233 - 1.0)
        print(f"{label:<45} {sigma:7.3f} {div_233:12.3f} {shift:+14.1f}% {div_200:12.3f}")

    off_xray, jen_xray, _e, _c = sweep[
        REAL_SIGMA_INT["X-ray (closest method to Mahdavi 2013's own)"]
    ]
    div_xray_233 = divergence(off_xray[FOCUS_Z], jen_xray[FOCUS_POWER][FOCUS_Z])
    off_all, jen_all, _e2, _c2 = sweep[REAL_SIGMA_INT["All methods combined"]]
    div_all_233 = divergence(off_all[FOCUS_Z], jen_all[FOCUS_POWER][FOCUS_Z])

    print("\n=== Interpretation ===")
    print(
        f"Real cluster-scale X-ray sigma=0.160 gives divergence={div_xray_233:.3f}x at z=2.33\n"
        f"(vs {base_div_233:.3f}x at Duffy's own 0.15) -- a {100 * abs(div_xray_233 / base_div_233 - 1.0):.1f}% shift.\n"
        f"Real all-methods sigma=0.146 gives {div_all_233:.3f}x -- a "
        f"{100 * abs(div_all_233 / base_div_233 - 1.0):.1f}% shift.\n\n"
        "This VALIDATES rather than overturns the project's prior default: Duffy et al. (2008)'s\n"
        "own sigma=0.15, used throughout E17/Addendum2/Addendum3 as an untested default, turns out\n"
        "to sit almost exactly on the real, independently-measured cluster-scale value -- not\n"
        "because it was calibrated at cluster mass (it wasn't -- Duffy's own range tops out at\n"
        "10^14 Msun, per Addendum's own finding), but coincidentally. ADDENDUM3's own sensitivity\n"
        "conclusion (a real range, ~29.8%/22.9% shift at z=2.33/2.00 on the +/-0.05 dex bracket)\n"
        "is UNCHANGED in its own right -- what changes is that the choice of sigma=0.15 as the\n"
        "central/default value is now independently justified, not an unverified default."
    )


if __name__ == "__main__":
    main()
