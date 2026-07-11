"""Tests for src/negative_control_tests.py — SAFE_NOW diagnostics.

INTERNAL_ONLY - DIAGNOSTIC_ONLY - NO_VALIDATION - NO_REFUTATION (same status
as the module under test; preserved deliberately below).

Named test_negative_control_battery.py, NOT test_negative_control_tests.py:
tests/test_negative_control_tests.py already exists as a namesake stub that
never imports src.negative_control_tests at all (it only tests inline copies
of formulas: numpy determinism, a hand-typed chi2 expression, a hand-typed
LCDM formula) -- found by the 2026-07-11 code audit. Editing that file is
blocked by this machine's own global permission rule Edit(**/*tests.py), a
deliberate guardrail against casual test edits, so it is left alone here;
this file provides the real coverage instead. Whether to edit, rename, or
remove the old stub is the user's call, flagged separately, not made here.

Before this file existed, test_row_permutation/test_randomised_beta/
test_synthetic_lcdm, the three functions src/negative_control_tests.py exists
to protect, had zero test coverage. They are exercised for real below,
against the real data/table_a1_reported.csv (12 rows, transcribed 2026-05-29).

IMPORTANT interpretive note, not a test-writing shortcut: the H(z) model used
here, h_model = h_data[0] * sqrt((1+z)^(3(1+beta_d)) + beta_q), is a toy
diagnostic stand-in, NOT a derived MULTING/IDM closure -- no such closure
exists anywhere in this codebase (H_MULT is TABLE_REPORTED, not computed; see
tests/test_table_a1_reported_data.py::test_h_mult_is_table_reported_not_computed).
Running these controls for the first time shows OVERALL FAIL (Test 2 and
Test 3 fail) for TJB's Table A1 caption values beta_d=4.5, beta_q=18.0 under
this toy formula. That is pinned below as the current, real, reproducible
output of this diagnostic -- it is evidence about how this particular toy
functional form behaves on the reported H_obs curve, not a claim about
MULTING/IDM as a framework, which is exactly what the module's own
NO_VALIDATION/NO_REFUTATION marking already says.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from src.negative_control_tests import (
    RandomisedBetaResult,
    RowPermutationResult,
    SyntheticLCDMResult,
    extract_h_data_and_beta,
    load_table_a1_rows_2_12,
)
from src.negative_control_tests import (
    test_randomised_beta as run_randomised_beta,
)
from src.negative_control_tests import (
    test_row_permutation as run_row_permutation,
)
from src.negative_control_tests import (
    test_synthetic_lcdm as run_synthetic_lcdm,
)

DATA_MISSING = pytest.mark.skipif(
    not Path("data/table_a1_reported.csv").exists(),
    reason="data/table_a1_reported.csv not present",
)


@pytest.fixture(scope="module")
def table_a1_inputs():
    df = load_table_a1_rows_2_12()
    return extract_h_data_and_beta(df)


@DATA_MISSING
def test_load_table_a1_rows_2_12_shape():
    """Real Table A1 data (rows 2-12, z>0) loads with the expected row count."""
    df = load_table_a1_rows_2_12()
    assert len(df) == 11
    assert (df["z"] > 0).all()


@DATA_MISSING
def test_row_permutation_runs_on_real_data(table_a1_inputs):
    z, h_obs, beta_d, beta_q = table_a1_inputs
    result = run_row_permutation(z, h_obs, beta_d, beta_q)
    assert isinstance(result, RowPermutationResult)
    assert result.verdict in {"PASS", "WARN", "FAIL"}
    assert 0.0 <= result.p_value <= 1.0
    # Regression pin: reported beta fits the real row order far better than
    # shuffled row orders (p~0 means ~0/100 shuffles beat the real ordering).
    assert result.p_value < 0.05, (
        f"row-permutation p_value drifted to {result.p_value:.4f} (was ~0.0) -- "
        "the reported chi2 no longer beats shuffled row orderings"
    )


@DATA_MISSING
def test_randomised_beta_runs_on_real_data(table_a1_inputs):
    z, h_obs, beta_d, beta_q = table_a1_inputs
    result = run_randomised_beta(z, h_obs, beta_d, beta_q)
    assert isinstance(result, RandomisedBetaResult)
    assert result.verdict in {"PASS", "WARN", "FAIL"}
    assert 0.0 <= result.percentile <= 100.0
    # Regression pin, NOT a validation gate: the reported beta_d=4.5,
    # beta_q=18.0 currently beats only ~13% of random (beta_d,beta_q) draws
    # under this toy formula -- i.e. FAIL, most random draws fit better. This
    # is a real, reproducible property of the toy formula + reported data,
    # tracked here so a future change (data or formula) is visible, not
    # silently drifting. It is not evidence against MULTING/IDM (no derived
    # H(z) closure exists to test in the first place -- see module docstring).
    assert 0.0 <= result.percentile < 40.0, (
        f"randomised-beta percentile drifted to {result.percentile:.1f}% "
        "(was ~13%) -- re-examine before updating this pin"
    )


@DATA_MISSING
def test_synthetic_lcdm_runs_on_real_data(table_a1_inputs):
    z, h_obs, beta_d, beta_q = table_a1_inputs
    result = run_synthetic_lcdm(z, h_obs, beta_d, beta_q)
    assert isinstance(result, SyntheticLCDMResult)
    assert result.verdict in {"PASS", "WARN", "FAIL"}
    assert result.chi2_ratio >= 0.0
    # Regression pin: a synthetic LCDM curve run through the SAME toy formula
    # and a coarse (beta_d,beta_q) sweep currently fits almost perfectly
    # (ratio ~0), meaning this toy functional form is flexible enough to fit
    # a pure-LCDM curve too -- it does not discriminate MULTING from LCDM by
    # itself. That is a property of the toy diagnostic formula's flexibility,
    # not a statement about the (still undefined) MULTING H(z) closure.
    assert result.chi2_ratio < 0.5, (
        f"synthetic-LCDM ratio drifted to {result.chi2_ratio:.4f} (was ~0.0) -- "
        "re-examine before updating this pin"
    )


@DATA_MISSING
def test_negative_control_battery_verdict_is_pinned(table_a1_inputs):
    """Master pin: run all three controls together, as main() does, and pin
    the overall verdict so a change in any control is visible at the top
    level, not just per-control. Current overall verdict is FAIL (2 of 3
    controls fail under the toy formula) -- see module docstring for why
    that is diagnostic information, not a validation/refutation claim."""
    z, h_obs, beta_d, beta_q = table_a1_inputs
    r1 = run_row_permutation(z, h_obs, beta_d, beta_q)
    r2 = run_randomised_beta(z, h_obs, beta_d, beta_q)
    r3 = run_synthetic_lcdm(z, h_obs, beta_d, beta_q)
    verdicts = {r1.verdict, r2.verdict, r3.verdict}
    assert verdicts == {"PASS", "FAIL"}, (
        f"overall verdict pattern changed: row_perm={r1.verdict}, "
        f"rand_beta={r2.verdict}, lcdm={r3.verdict} (expected one PASS, two FAIL)"
    )
