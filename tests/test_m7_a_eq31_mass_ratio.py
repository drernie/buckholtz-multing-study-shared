"""M7-A Eq31 characterization tests. NOT_VALIDATION / NOT_REFUTATION."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.m7_a_eq31_mass_ratio_toy_test import MASSES, analyze  # noqa: E402


def test_ratio_close_at_permille_level():
    r = analyze(MASSES["PDG2022"])["ratio_W_normalized_to_7"]
    assert abs(r["Z"] - 9.0) < 0.02
    assert abs(r["H"] - 17.0) < 0.05


def test_higgs_within_about_one_sigma_z_anchored():
    pull = analyze(MASSES["PDG2022"])["Z_anchored"]["pull_sigma"]["H"]
    assert abs(pull) < 1.2


def test_w_excluded_at_3sigma_against_pdg_average():
    pull22 = analyze(MASSES["PDG2022"])["Z_anchored"]["pull_sigma"]["W"]
    pull24 = analyze(MASSES["PDG2024_avg"])["Z_anchored"]["pull_sigma"]["W"]
    assert abs(pull22) > 3.0
    assert abs(pull24) > 3.0


def test_w_compatible_only_with_cdf2022():
    pull = analyze(MASSES["CDF2022_W_only"])["Z_anchored"]["pull_sigma"]["W"]
    assert abs(pull) < 2.0
