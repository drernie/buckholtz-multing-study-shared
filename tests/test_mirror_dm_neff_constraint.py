"""
Tests for Mirror DM / N_eff constraint script.

Labels: EXTERNAL_STANDARD_PHYSICS · IF_MIRROR_DM_INTERPRETATION
Scope:  INTERNAL_DIAGNOSTIC_ONLY
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from mirror_dm_neff_constraint import (
    DELTA_N_EFF_BOUND_1SIGMA,
    ELECTRON_TO_NEFF,
    INTERPRETATIONS,
    N_ISOMERS,
    N_MIRROR_NU,
    PHOTON_TO_NEFF,
    delta_neff,
    sigma_from_neff,
    x_max,
)

# ── Physics constants ─────────────────────────────────────────────────────────


def test_photon_to_neff_formula():
    """(8/7) × (11/4)^(4/3) ≈ 4.40."""
    expected = (8 / 7) * (11 / 4) ** (4 / 3)
    assert math.isclose(PHOTON_TO_NEFF, expected, rel_tol=1e-12)


def test_photon_to_neff_approximate():
    """Sanity: photon factor is between 4.35 and 4.45."""
    assert 4.35 < PHOTON_TO_NEFF < 4.45


def test_electron_to_neff_formula():
    """(16/7) × (11/4)^(4/3) = 2 × PHOTON_TO_NEFF."""
    expected = 2 * PHOTON_TO_NEFF
    assert math.isclose(ELECTRON_TO_NEFF, expected, rel_tol=1e-12)


def test_n_isomers():
    assert N_ISOMERS == 5


def test_n_mirror_nu():
    assert N_MIRROR_NU == 3


def test_planck_bound():
    assert DELTA_N_EFF_BOUND_1SIGMA == 0.40


# ── Core formulas ─────────────────────────────────────────────────────────────


def test_delta_neff_zero_at_x0():
    """At x=0, no dark sector → ΔN_eff = 0."""
    assert delta_neff(PHOTON_TO_NEFF, 5, 0.0) == 0.0


def test_delta_neff_scales_as_x4():
    """ΔN_eff doubles when x increases by 2^(1/4)."""
    coeff = PHOTON_TO_NEFF
    x1 = 0.3
    x2 = x1 * 2**0.25
    ratio = delta_neff(coeff, 1, x2) / delta_neff(coeff, 1, x1)
    assert math.isclose(ratio, 2.0, rel_tol=1e-10)


def test_delta_neff_linear_in_sectors():
    """ΔN_eff doubles when n_sectors doubles."""
    coeff = PHOTON_TO_NEFF
    x = 0.3
    d1 = delta_neff(coeff, 1, x)
    d2 = delta_neff(coeff, 2, x)
    assert math.isclose(d2, 2 * d1, rel_tol=1e-12)


def test_x_max_roundtrip():
    """x_max(n, bound) → ΔN_eff(x_max) == bound."""
    for interp in INTERPRETATIONS:
        xm = x_max(interp.coeff_per_sector, N_ISOMERS)
        dneff_at_xm = delta_neff(interp.coeff_per_sector, N_ISOMERS, xm)
        assert math.isclose(dneff_at_xm, DELTA_N_EFF_BOUND_1SIGMA, rel_tol=1e-10), (
            f"Roundtrip failed for {interp.interp_id}: "
            f"ΔN_eff({xm:.4f}) = {dneff_at_xm:.4f} ≠ {DELTA_N_EFF_BOUND_1SIGMA}"
        )


# ── All interpretations ruled out at x=1 ─────────────────────────────────────


def test_all_interps_ruled_out_at_x1():
    """Every interpretation gives ΔN_eff >> 0.40 at equal temperatures."""
    for interp in INTERPRETATIONS:
        dn = delta_neff(interp.coeff_per_sector, N_ISOMERS, 1.0)
        assert dn > DELTA_N_EFF_BOUND_1SIGMA * 10, (
            f"{interp.interp_id}: ΔN_eff={dn:.2f} not >> {DELTA_N_EFF_BOUND_1SIGMA}"
        )


def test_minimal_interp_delta_neff_x1():
    """Interpretation A at x=1: ΔN_eff ≈ 22.0 (5 × 4.40)."""
    interp_A = next(i for i in INTERPRETATIONS if i.interp_id == "A_minimal")
    dn = delta_neff(interp_A.coeff_per_sector, N_ISOMERS, 1.0)
    assert math.isclose(dn, 5 * PHOTON_TO_NEFF, rel_tol=1e-10)
    assert 21.0 < dn < 23.0


def test_full_mirror_interp_delta_neff_x1():
    """Interpretation C at x=1: ΔN_eff = 5 × (PHOTON + ELECTRON + 3×NU)."""
    interp_C = next(i for i in INTERPRETATIONS if i.interp_id == "C_full_mirror")
    expected_coeff = PHOTON_TO_NEFF + ELECTRON_TO_NEFF + N_MIRROR_NU * 1.0
    expected_total = N_ISOMERS * expected_coeff
    dn = delta_neff(interp_C.coeff_per_sector, N_ISOMERS, 1.0)
    assert math.isclose(dn, expected_total, rel_tol=1e-10)
    assert dn > 70.0  # well above any Planck constraint


# ── x_max values are physically reasonable ───────────────────────────────────


def test_x_max_minimal_below_one():
    """Even minimal interpretation requires T_dark < T_SM."""
    interp_A = next(i for i in INTERPRETATIONS if i.interp_id == "A_minimal")
    assert x_max(interp_A.coeff_per_sector, N_ISOMERS) < 1.0


def test_x_max_full_mirror_strictest():
    """Full mirror (C) has tightest constraint: smallest x_max."""
    xmax_vals = [x_max(i.coeff_per_sector, N_ISOMERS) for i in INTERPRETATIONS]
    assert xmax_vals[0] > xmax_vals[1] > xmax_vals[2]


def test_x_max_full_mirror_below_0_35():
    """Full mirror interpretation: T_dark/T_SM < 0.35."""
    interp_C = next(i for i in INTERPRETATIONS if i.interp_id == "C_full_mirror")
    assert x_max(interp_C.coeff_per_sector, N_ISOMERS) < 0.35


def test_x_max_minimal_below_0_45():
    """Minimal interpretation: T_dark/T_SM < 0.45."""
    interp_A = next(i for i in INTERPRETATIONS if i.interp_id == "A_minimal")
    assert x_max(interp_A.coeff_per_sector, N_ISOMERS) < 0.45


# ── sigma check ───────────────────────────────────────────────────────────────


def test_sigma_at_x1_is_large():
    """At x=1, all interpretations are >50σ above Planck."""
    for interp in INTERPRETATIONS:
        dn = delta_neff(interp.coeff_per_sector, N_ISOMERS, 1.0)
        sig = sigma_from_neff(dn)
        assert sig > 50.0, f"{interp.interp_id}: only {sig:.1f}σ above Planck"


# ── JSON report ───────────────────────────────────────────────────────────────


def test_json_report_exists_after_run():
    """Run the audit and verify JSON output is valid."""
    from mirror_dm_neff_constraint import run_audit

    result = run_audit()

    assert result["gate"] == "M7-C-supplement-mirror-dm"
    assert result["n_isomers"] == 5
    assert len(result["interpretations"]) == 3
    assert all(r["status_at_x1"] == "RULED_OUT" for r in result["interpretations"])
    assert len(result["conclusions"]) >= 4

    json_path = Path(__file__).parent.parent / "reports" / "mirror_dm_neff_constraint.json"
    assert json_path.exists(), "JSON report not written"
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert data["gate"] == "M7-C-supplement-mirror-dm"
