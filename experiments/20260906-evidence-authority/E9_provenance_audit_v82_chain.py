"""E9 -- run src/provenance_audit.py over v82's full input chain as mapped in
FINDING_E4, with the 'incurred' field filled from what this thread actually
measured or read (E2, E5) or found unmeasured.

Option 3 of the second option set. This is an application of the tool to the
real chain, not a new measurement: every entry below is sourced to a FINDING
or to v82's own text. Where v82 states a dependency but nobody has quantified
it, magnitude_pct is None on purpose -- the tool's UNQUANTIFIED verdict is the
honest state, not a gap to paper over.

The model under test is the expansion history H(z): v82's bridge exists to
produce H(z) bottom-up, so any input that already assumes an expansion
history (rho_crit(z) ∝ H(z)^2; an H0 used to subtract a Hubble flow) is
circular with respect to it. Both circular items below are TJB's OWN
diagnoses (Sec. II.F, Sec. IV.M) -- the tool re-derives his verdicts, it does
not discover them.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.provenance_audit import Chain, Dependency, Step, format_report  # noqa: E402

MODEL = "expansion history"

chain = Chain(
    measures="H(z) from MULTING's bottom-up node-pair bridge (v82 Sec. II.C-II.G)",
    tests_model=MODEL,
    steps=[
        Step(
            name="cosmic chronometer H(z), 31 pts [v82 Class I]",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="stellar population synthesis model (SFH, IMF, library, SPS)",
                    magnitude_pct=8.91,  # FINDING_E5: Moresco+2020 data_MM20 'sps' mean
                    in_quoted_sigma=False,  # errHz = sqrt(stat^2+met^2) only (E5 Result 3)
                    correlated_across_bins=True,  # Moresco README: 'fully correlated'
                    source="FINDING_E5; Moresco+2020 arXiv:2003.07362; E8 propagated it",
                ),
            ),
        ),
        Step(
            name="gas mass M_gas [v82 Class I, 'direct fit to real X-ray data']",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="X-ray mass-temperature scaling-relation calibration",
                    magnitude_pct=63.0,  # FINDING_E13: source's own sigma_{Mgas|T}=0.49 (ln-normal)
                    in_quoted_sigma=False,  # v82 quotes B,C (Eq.13) but never this scatter
                    correlated_across_bins=False,  # not stated either way in the source; not claimed
                    source="FINDING_E13; Ramos-Ceja+2025 arXiv:2511.14356 Sec.4.4, +1sigma side of "
                    "the ln-normal range [-39%,+63%]; asymmetric, this float is a representative bound",
                ),
            ),
        ),
        Step(
            name="ICM thermal energy k_X [v82 Class I]",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="X-ray mass-temperature scaling-relation calibration",
                    magnitude_pct=63.0,  # same source as gas mass: k_X = (3/2)(M_gas/mu_mol m_p) T_X
                    in_quoted_sigma=False,
                    correlated_across_bins=False,
                    source="FINDING_E13; feeds through Eq.14 from the same M_gas,X(z) as above -- "
                    "v82.md:332 states this sets the dipole/quadrupole (beta1/beta2) force terms",
                ),
            ),
        ),
        Step(
            name="temperature T_keV via self-similar step, Eq.14 [v82 Class II]",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="self-similar mass-temperature assumption",
                    magnitude_pct=None,
                    source="v82.md:569 'purely theoretical self-similar assumption of Eq. (14)'",
                ),
            ),
        ),
        Step(
            name="mass evolution m_X(z), Eq.10 [v82 Class II]",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="assumed cluster mass-accretion law",
                    magnitude_pct=None,
                    source="v82.md:586-587 'retained-theoretical'",
                ),
            ),
        ),
        Step(
            name="inter-node separation law, Sec. II.C [v82 Class II]",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="theoretical separation-evolution assumption",
                    magnitude_pct=None,
                    source="v82.md:587-589 'least FLRW-flavored... remains a theoretical assumption'",
                ),
            ),
        ),
        Step(
            name="node radius r_X(z) via rho_crit(z) [v82 Class III]",
            avoids="an assumed radius profile",
            incurs=(
                Dependency(
                    name=MODEL,  # rho_crit(z) = 3H(z)^2/8piG -- the Friedmann equation
                    source="v82.md:601-613, TJB's own diagnosis; FINDING_P199; P196-P202",
                ),
            ),
        ),
        Step(
            name="H0_anchor = sdot_0/s_0 via peculiar velocities [v82 Sec. IV.M]",
            avoids="an assumed expansion model inside the force law",
            incurs=(
                Dependency(
                    name=MODEL,  # surveys subtract an assumed H0 = H(z=0) first
                    source="v82.md:1297-1316, TJB's own diagnosis 'circular in the same sense'; FINDING_E2",
                ),
            ),
        ),
        # Anchors: not CC, not bridge inputs -- included so the report shows the
        # whole 33-point fit, and because E8 found they carry the model gap.
        Step(
            name="SH0ES anchor, z=0.0233, sigma=1.04",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="Cepheid distance ladder calibration",
                    magnitude_pct=1.4,  # 1.04/73.04
                    in_quoted_sigma=True,
                    source="Riess+2022 as used by v82; E8: +22.03 of the 21.2 chi2 gap vs fixed LCDM",
                ),
            ),
        ),
        Step(
            name="DESI DR2 Ly-alpha BAO, z=2.33, sigma=2.8",
            avoids=MODEL,
            incurs=(
                Dependency(
                    name="sound-horizon r_d from early-universe physics",
                    magnitude_pct=None,  # FINDING_E6 example 3: a theoretical prediction used as a ruler
                    source="FINDING_E6; Liu+2024 arXiv:2405.12498; v82 does not state r_d provenance",
                ),
            ),
        ),
    ],
)

if __name__ == "__main__":
    print(format_report(chain))
    issues = chain.audit()
    from collections import Counter

    c = Counter(i.finding.value for i in issues)
    print()
    print("SUMMARY: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))
    print(f"steps declaring nothing incurred: {len(chain.undeclared_steps())}")
