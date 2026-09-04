"""
Tests for cluster_data_pipeline.py.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Scope note (revised 2026-09-05, per external review): step1_mcxc/
step2_psz2/step5_hz call real external services (VizieR via astroquery,
GitLab HTTP). The network call itself (`_vizier_download`, `requests.get`)
is monkeypatched at that exact I/O boundary -- everything downstream
(z-filtering, ID normalization, coordinate cross-match, Y_SZ conversion,
hardcoded-table fallback) runs for real and is asserted on. This is a
narrower mock than "stub the whole function to return what the test
wants" -- it tests real local logic, not the mock. step4_export and
main() are covered too: step4_export has no network dependency at all;
main()'s CLI argument plumbing (--max-rows/--z-max/--data-dir reaching
the right step functions) is exercised with all 5 steps monkeypatched.
Not covered: the astroquery-missing-dependency SystemExit branch in
main() -- exercising it needs import-machinery mocking (patching
builtins.__import__) whose fragility outweighed the value here.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import src.cluster_data_pipeline as cdp
from src.cluster_data_pipeline import (
    _sexagesimal_to_deg,
    e_thermal_path_a,
    e_thermal_path_b,
    step1_mcxc,
    step2_psz2,
    step3_merger_flags,
    step4_export,
    step5_hz,
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


class TestStep1Mcxc:
    """_vizier_download is monkeypatched (the real network boundary);
    everything after it -- sexagesimal conversion, dropna, z-filter,
    mass scaling, cluster_id stripping, CSV write -- runs for real."""

    def _fake_raw(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "MCXC": [" MCXC J0658.5-5556 ", "MCXC J9999.9-9999", "MCXC J8888.8-8888"],
                "RAJ2000": ["06 58 30.0", "10 00 00.0", ""],  # row 3: blank RA -> NaN
                "DEJ2000": ["-55 56 00", "-10 00 00", "-20 00 00"],
                "z": [0.296, 0.9, 0.1],  # row 2: z > z_max=0.5 -> filtered
                "M500": [15.0, 5.0, 5.0],
                "R500": [1.98, 1.0, 1.0],
            }
        )

    def test_filters_and_transforms(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(cdp, "_vizier_download", lambda *a, **k: self._fake_raw())
        df = step1_mcxc(tmp_path, row_limit=100, z_max=0.5)

        # row 2 (z=0.9 > z_max) and row 3 (blank RA -> NaN, dropped) both gone
        assert len(df) == 1
        row = df.iloc[0]
        assert row["cluster_id"] == "MCXC J0658.5-5556"  # stripped
        assert row["ra_deg"] == pytest.approx(104.625, abs=1e-6)
        assert row["dec_deg"] == pytest.approx(-55.933333, abs=1e-4)
        assert row["M500c_Msun"] == pytest.approx(15.0e14, rel=1e-9)  # x1e14 scaling
        assert (tmp_path / "mcxc.csv").exists()


class TestStep2Psz2:
    """_vizier_download monkeypatched; name-join, coordinate fallback,
    Y5R500 unit conversion, and E_thermal derivation all run for real."""

    def _input_df(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "cluster_id": ["MCXC J1111.1-1111", "MCXC J2222.2-2222", "MCXC J3333.3-3333"],
                "ra_deg": [200.0, 50.0001, 300.0],
                # row C: valid but far from any PSZ2 entry below (must stay in
                # [-90, 90] -- SkyCoord builds ALL unmatched rows in one batch,
                # so an out-of-range value here breaks the coordinate fallback
                # for row B too, not just row C -- caught the hard way once).
                "dec_deg": [10.0, -30.0001, 80.0],
                "z": [0.2, 0.3, 0.1],
            }
        )

    def _fake_psz2_raw(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "PSZ2": ["PSZ2 G001", "PSZ2 G002"],
                "RAJ2000": [200.0, 50.0],  # row 2: 0.0001 deg from cluster_id B -> <60"
                "DEJ2000": [10.0, -30.0],
                "Y5R500": [100.0, 200.0],  # x0.001 -> 0.1, 0.2 arcmin^2
                "MCXC": ["J1111.1-1111", "--"],  # row 1: name match; row 2: coord fallback
            }
        )

    def test_name_join_and_coordinate_fallback(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(cdp, "_vizier_download", lambda *a, **k: self._fake_psz2_raw())
        out = step2_psz2(self._input_df(), row_limit=100)

        row_a = out[out["cluster_id"] == "MCXC J1111.1-1111"].iloc[0]  # matched by name
        assert row_a["Y500_arcmin2"] == pytest.approx(0.1, rel=1e-9)
        assert row_a["ICM_proxy_type"] == "Y_SZ_derived_LCDM"
        assert math.isfinite(row_a["Ethermal_c2_Msun"])

        row_b = out[out["cluster_id"] == "MCXC J2222.2-2222"].iloc[0]  # matched by coords
        assert row_b["Y500_arcmin2"] == pytest.approx(0.2, rel=1e-9)

        row_c = out[out["cluster_id"] == "MCXC J3333.3-3333"].iloc[0]  # no match
        assert math.isnan(row_c["Y500_arcmin2"])
        assert row_c["ICM_proxy_type"] == "not_available"

    def test_download_failure_leaves_nan(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def _raise(*a: object, **k: object) -> pd.DataFrame:
            raise RuntimeError("VizieR unreachable")

        monkeypatch.setattr(cdp, "_vizier_download", _raise)
        out = step2_psz2(self._input_df(), row_limit=100)
        assert out["Y500_arcmin2"].isna().all()
        assert (out["ICM_proxy_type"] == "not_available").all()


class TestStep4Export:
    """No network dependency at all -- pure DataFrame reshaping + CSV write."""

    def _post_step3_df(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "cluster_id": ["A", "B"],
                "catalog": ["MCXC-I", "MCXC-I"],
                "ra_deg": [10.0, 20.0],
                "dec_deg": [-10.0, -20.0],
                "z": [0.1, 0.2],
                "M500c_Msun": [1e14, 2e14],
                "M500c_method": ["X-ray_Lx_scaling", "X-ray_Lx_scaling"],
                "R500c_Mpc": [1.0, 1.2],
                "Y500_arcmin2": [np.nan, 0.1],
                "ICM_proxy_type": ["not_available", "Y_SZ_derived_LCDM"],
                "Ethermal_c2_Msun": [np.nan, 5.0e7],
                "dynamical_state": ["unknown", "disturbed"],
                "merger_exclusion_flag": [False, True],  # B is merger-excluded
                "merger_exclusion_reason": ["", "named_known_merger"],
            }
        )

    def test_writes_raw_and_clean_csv(self, tmp_path: Path) -> None:
        clean = step4_export(self._post_step3_df(), tmp_path)

        raw_path = tmp_path / "catalogs" / "clusters_raw.csv"
        clean_path = tmp_path / "clusters_clean.csv"
        assert raw_path.exists()
        assert clean_path.exists()

        raw_df = pd.read_csv(raw_path)
        assert len(raw_df) == 2  # both clusters kept in raw
        assert len(clean) == 1  # merger-excluded cluster B dropped from clean
        assert clean.iloc[0]["cluster_id"] == "A"
        assert "TX_keV" in raw_df.columns and raw_df["TX_keV"].isna().all()
        assert (
            raw_df["source_url"] == "https://cdsarc.u-strasbg.fr/viz-bin/cat/J/A+A/534/A109"
        ).all()


class TestStep5Hz:
    def test_network_failure_falls_back_to_hardcoded_table(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        def _raise_get(*a: object, **k: object) -> object:
            raise ConnectionError("network unavailable")

        monkeypatch.setattr("requests.get", _raise_get)
        df = step5_hz(tmp_path)

        assert len(df) == len(cdp._HZ_CC_DATA)
        assert (df["source"] == "Moresco+2022_arXiv:2201.07241").all()
        assert (df["method"] == "cosmic_chronometer").all()
        assert (df["FLRW_independent"]).all()
        assert (tmp_path / "hz_cc.csv").exists()

    def test_live_fetch_used_when_available(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        class _FakeResponse:
            text = "# header comment\n0.10 70.0 5.0\n0.20 75.0 6.0\n"

            def raise_for_status(self) -> None:
                return None

        monkeypatch.setattr("requests.get", lambda *a, **k: _FakeResponse())
        df = step5_hz(tmp_path)

        assert len(df) == 2  # only the 2 real data lines, comment skipped
        assert df.iloc[0]["z"] == pytest.approx(0.10)
        assert df.iloc[1]["Hz_km_s_Mpc"] == pytest.approx(75.0)


class TestMain:
    """CLI argument plumbing -- all 5 real steps monkeypatched to no-ops
    so this only exercises main()'s own wiring, not the pipeline again."""

    def test_cli_args_reach_step_functions(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        calls: dict[str, object] = {}

        def _fake_step1(out_dir: Path, row_limit: int, z_max: float) -> pd.DataFrame:
            calls["step1"] = (out_dir, row_limit, z_max)
            return pd.DataFrame({"z": [0.1], "merger_exclusion_flag": [False]})

        def _fake_step2(df: pd.DataFrame, row_limit: int) -> pd.DataFrame:
            calls["step2"] = row_limit
            return df

        def _fake_step3(df: pd.DataFrame) -> pd.DataFrame:
            calls["step3"] = True
            return df

        def _fake_step4(df: pd.DataFrame, data_dir: Path) -> pd.DataFrame:
            calls["step4"] = data_dir
            return df.assign(Ethermal_c2_Msun=np.nan)

        def _fake_step5(data_dir: Path) -> pd.DataFrame:
            calls["step5"] = data_dir
            return pd.DataFrame({"z": [0.1, 0.2]})

        monkeypatch.setattr(cdp, "step1_mcxc", _fake_step1)
        monkeypatch.setattr(cdp, "step2_psz2", _fake_step2)
        monkeypatch.setattr(cdp, "step3_merger_flags", _fake_step3)
        monkeypatch.setattr(cdp, "step4_export", _fake_step4)
        monkeypatch.setattr(cdp, "step5_hz", _fake_step5)
        monkeypatch.setattr(
            "sys.argv",
            [
                "cluster_data_pipeline.py",
                "--max-rows",
                "50",
                "--z-max",
                "0.7",
                "--data-dir",
                str(tmp_path),
            ],
        )

        cdp.main()

        assert calls["step1"] == (tmp_path, 50, 0.7)
        assert calls["step2"] == 50
        assert calls["step3"] is True
        assert calls["step4"] == tmp_path
        assert calls["step5"] == tmp_path
        assert (tmp_path / "catalogs").is_dir()
