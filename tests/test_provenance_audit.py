"""Tests for src/provenance_audit.py.

The two positive controls are the real, documented cases the module was built
from: the module must independently re-derive the findings that were reached by
hand in FINDING_E5 (cosmic chronometers: dependency outside sigma) and
FINDING_E2 (H0_anchor: circular). If it cannot reproduce those, it is not
auditing anything.
"""

from __future__ import annotations

from src.provenance_audit import Chain, Dependency, Finding, Step, format_report

# ── Positive control 1: the real CC case (FINDING_E5) ──────────────────────


def _cc_chain() -> Chain:
    """Cosmic chronometer H(z), as actually used in this project's pipeline."""
    return Chain(
        measures="H(z) from cosmic chronometers",
        tests_model="expansion history",
        steps=[
            Step(
                name="differential galaxy ages -> H(z)",
                avoids="expansion history",
                incurs=(
                    Dependency(
                        name="stellar population synthesis model",
                        magnitude_pct=8.91,
                        in_quoted_sigma=False,
                        correlated_across_bins=True,
                        source="Moresco+2020 arXiv:2003.07362, data_MM20.dat",
                    ),
                ),
            )
        ],
    )


def test_positive_control_cc_dependency_is_flagged_outside_sigma() -> None:
    issues = _cc_chain().audit()
    assert len(issues) == 1
    assert issues[0].finding is Finding.OUTSIDE_SIGMA
    assert "8.91%" in issues[0].detail
    assert "correlated across bins" in issues[0].detail


def test_positive_control_cc_is_not_reported_circular() -> None:
    """The CC method genuinely avoids assuming an expansion history -- the module
    must NOT call it circular just because it carries some other dependency."""
    assert all(i.finding is not Finding.CIRCULAR for i in _cc_chain().audit())


# ── Positive control 2: the real H0_anchor case (FINDING_E2) ───────────────


def test_positive_control_h0_anchor_is_flagged_circular() -> None:
    chain = Chain(
        measures="H0_anchor = sdot_0 / s_0",
        tests_model="H0",
        steps=[
            Step(
                name="cluster pairwise peculiar velocity",
                avoids="assumed expansion model in the force law",
                incurs=(
                    Dependency(
                        name="H0",
                        magnitude_pct=None,
                        source="surveys subtract an assumed Hubble flow first",
                    ),
                ),
            )
        ],
    )
    issues = chain.audit()
    assert len(issues) == 1
    assert issues[0].finding is Finding.CIRCULAR
    assert "cannot be independent evidence" in issues[0].detail


def test_circularity_beats_unquantified_for_the_same_dependency() -> None:
    """A dependency that is BOTH the model under test AND unmeasured must report
    as CIRCULAR only -- circularity is the finding that matters, and emitting
    both would double-count one problem."""
    chain = Chain(
        measures="X",
        tests_model="M",
        steps=[Step(name="s", avoids="a", incurs=(Dependency(name="M"),))],
    )
    findings = [i.finding for i in chain.audit()]
    assert findings == [Finding.CIRCULAR]


# ── Negative controls ──────────────────────────────────────────────────────


def test_negative_control_clean_chain_reports_nothing() -> None:
    """A dependency that is quantified AND carried in the quoted sigma is fine."""
    chain = Chain(
        measures="X",
        tests_model="M",
        steps=[
            Step(
                name="clean step",
                avoids="M",
                incurs=(
                    Dependency(
                        name="instrument calibration", magnitude_pct=1.2, in_quoted_sigma=True
                    ),
                ),
            )
        ],
    )
    assert chain.audit() == []
    assert chain.undeclared_steps() == []


def test_unquantified_dependency_is_flagged() -> None:
    chain = Chain(
        measures="X",
        tests_model="M",
        steps=[Step(name="s", avoids="M", incurs=(Dependency(name="unmeasured thing"),))],
    )
    issues = chain.audit()
    assert [i.finding for i in issues] == [Finding.UNQUANTIFIED]
    assert "not the same as small" in issues[0].detail


def test_model_name_match_is_case_and_whitespace_insensitive() -> None:
    chain = Chain(
        measures="X",
        tests_model="  Friedmann Equation ",
        steps=[Step(name="s", avoids="a", incurs=(Dependency(name="friedmann equation"),))],
    )
    assert [i.finding for i in chain.audit()] == [Finding.CIRCULAR]


# ── The blank-declaration case that motivated the module ───────────────────


def test_step_declaring_nothing_incurred_is_surfaced_not_passed() -> None:
    """The exact shape found in this project's own code: a step flagged as
    independent with nothing declared on the other side. It must appear as a
    blank to be filled, not silently pass the audit."""
    chain = Chain(
        measures="H(z)",
        tests_model="expansion history",
        steps=[Step(name="FLRW_independent = True", avoids="expansion history")],
    )
    assert chain.audit() == []  # nothing DECLARED, so nothing to flag
    assert chain.undeclared_steps() == ["FLRW_independent = True"]  # ...but it is visible


def test_report_renders_issues_and_blanks() -> None:
    chain = _cc_chain()
    chain.steps.append(Step(name="undeclared step", avoids="something"))
    text = format_report(chain)

    assert "OUTSIDE_SIGMA" in text
    assert "UNDECLARED (1)" in text
    assert "not yet asked" in text
    assert "H(z) from cosmic chronometers" in text
