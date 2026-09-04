"""
Tests for cluster_data_pipeline.py — pure-logic units only.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Scope note: step1_mcxc/step2_psz2/step4_export/step5_hz and main() all
perform real network I/O (VizieR via astroquery, GitLab HTTP) and are
deliberately NOT covered here — mocking them out would test the mocks,
not the pipeline, and hitting the network from a unit test is flaky by
construction. This file covers the genuinely pure functions instead:
thermal-energy formulas, sexagesimal coordinate conversion, and the
merger-exclusion DataFrame logic.
"""

from __future__ import annotations

import math

import pandas as pd
import pytest

from src.cluster_data_pipeline import (
    _sexagesimal_to_deg,
    e_thermal_path_a,
    e_thermal_path_b,
    step3_merger_flags,
)


class TestEThermalPathA:
    def test_zero_gas_mass_gives_zero_energy(self) -> None:
        assert e_thermal_path_a(0.0, 5.0) == 0.0

    def test_linear_in_gas_mass(self) -> None:
        """E = (3/2)(Mgas/mu*mp)*kB*T is exactly linear in Mgas at fixed T."""
        e1 = e_thermal_path_a(1e13, 5.0)
        e2 = e_thermal_path_a(2e13, 5.0)
        assert e2 == pytest.approx(2 * e1, rel=1e-9)

    def test_linear_in_temperature(self) -> None:
        """E is exactly linear in T_X at fixed Mgas."""
        e1 = e_thermal_path_a(1e13, 5.0)
        e2 = e_thermal_path_a(1e13, 10.0)
        assert e2 == pytest.approx(2 * e1, rel=1e-9)

    def test_reference_value(self) -> None:
        """Regression anchor -- computed from the formula itself (no
        external validation source exists for this synthetic input);
        catches accidental changes to the constants/exponents."""
        assert e_thermal_path_a(1e13, 5.0) == pytest.approx(130988974.51, rel=1e-6)


class TestEThermalPathB:
    def test_returns_finite_positive_for_physical_input(self) -> None:
        e = e_thermal_path_b(1e-4, 0.1)
        assert math.isfinite(e)
        assert e > 0

    def test_increases_with_redshift_at_fixed_y(self) -> None:
        """D_A(z) is non-monotonic in general LCDM, but over 0.1-0.5 the
        angular-diameter distance is still rising, so E ~ D_A^2 should be
        larger at higher z for this specific pair (a genuine physical
        assertion checked with real astropy Planck18, not a tautology)."""
        e_low = e_thermal_path_b(1e-4, 0.1)
        e_high = e_thermal_path_b(1e-4, 0.5)
        assert e_high > e_low

    def test_linear_in_y500(self) -> None:
        e1 = e_thermal_path_b(1e-4, 0.3)
        e2 = e_thermal_path_b(2e-4, 0.3)
        assert e2 == pytest.approx(2 * e1, rel=1e-9)


class TestSexagesimalToDeg:
    def test_known_bullet_cluster_coordinates(self) -> None:
        """1E 0657-56 / MCXC J0658.5-5556 RA/Dec, hand-verified:
        06h58m30s = (6 + 58/60 + 30/3600) * 15 deg = 104.625 deg;
        -55d56m00s = -(55 + 56/60) deg."""
        ra, dec = _sexagesimal_to_deg(pd.Series(["06 58 30.0"]), pd.Series(["-55 56 00"]))
        assert ra[0] == pytest.approx(104.625, abs=1e-6)
        assert dec[0] == pytest.approx(-55.933333, abs=1e-4)

    def test_blank_and_none_become_nan(self) -> None:
        ra, dec = _sexagesimal_to_deg(pd.Series(["", None]), pd.Series(["", None]))
        assert all(math.isnan(v) for v in ra)
        assert all(math.isnan(v) for v in dec)


class TestStep3MergerFlags:
    def _make_df(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "cluster_id": [
                    "MCXC J0658.5-5556",  # full-form hard-exclude (Bullet Cluster)
                    "J0014.3-3023",  # bare-form hard-exclude (Abell 2744)
                    "J1234.5-6789",  # ordinary cluster, not excluded
                ]
            }
        )

    def test_full_form_id_excluded(self) -> None:
        out = step3_merger_flags(self._make_df())
        row = out[out["cluster_id"] == "MCXC J0658.5-5556"].iloc[0]
        assert row["merger_exclusion_flag"] is True or row["merger_exclusion_flag"] == True  # noqa: E712
        assert row["dynamical_state"] == "disturbed"
        assert row["merger_exclusion_reason"] == "named_known_merger"

    def test_bare_form_id_excluded(self) -> None:
        out = step3_merger_flags(self._make_df())
        row = out[out["cluster_id"] == "J0014.3-3023"].iloc[0]
        assert bool(row["merger_exclusion_flag"]) is True
        assert row["dynamical_state"] == "disturbed"

    def test_ordinary_cluster_not_excluded(self) -> None:
        out = step3_merger_flags(self._make_df())
        row = out[out["cluster_id"] == "J1234.5-6789"].iloc[0]
        assert bool(row["merger_exclusion_flag"]) is False
        assert row["dynamical_state"] == "unknown"
        assert row["merger_exclusion_reason"] == ""

    def test_exclusion_count(self) -> None:
        out = step3_merger_flags(self._make_df())
        assert int(out["merger_exclusion_flag"].sum()) == 2
