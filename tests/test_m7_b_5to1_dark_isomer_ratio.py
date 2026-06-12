"""M7-B characterization tests. NOT_VALIDATION / NOT_REFUTATION."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.m7_b_5to1_dark_isomer_ratio_audit import main  # noqa: E402


def test_gap_is_about_seven_percent():
    r = main()
    assert 6.0 < abs(r["comparison"]["pct_diff_vs_planck"]) < 8.0


def test_literal_five_excluded_by_planck_crosscheck():
    r = main()
    assert abs(r["comparison"]["pull_sigma_vs_planck"]) > 5.0


def test_no_derivation_recorded():
    r = main()
    d = r["derivation_check"]
    assert d["equal_density_per_isomer_derived"] is False
    assert d["thermal_history_provided"] is False


def test_neutron_mass_shift_cannot_close_gap():
    r = main()
    assert r["sanity_note_neutron_mass_shift"]["fraction"] < 0.001
