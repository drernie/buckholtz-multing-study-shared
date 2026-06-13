"""
Tests for LOO epsilon analysis and Illustris-TNG k_A proxy scripts.

These are unit tests for the analysis machinery, NOT hypothesis validation.
Labels: UNIT_TEST · NOT_VALIDATION · INTERNAL_TEST_ONLY
"""

from __future__ import annotations

import builtins
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import illustris_tng_k_a as tng_mod  # noqa: E402
import loo_epsilon_analysis as loo_mod  # noqa: E402

# ── LOO module tests ───────────────────────────────────────────────────────────


class TestPearsonR:
    def test_perfect_positive(self) -> None:
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert loo_mod.pearson_r(x, x) == pytest_approx(1.0, abs=1e-6)

    def test_perfect_negative(self) -> None:
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [-1.0, -2.0, -3.0, -4.0, -5.0]
        assert loo_mod.pearson_r(x, y) == pytest_approx(-1.0, abs=1e-6)

    def test_zero_variance_returns_nan(self) -> None:
        x = [1.0, 1.0, 1.0]
        y = [1.0, 2.0, 3.0]
        assert math.isnan(loo_mod.pearson_r(x, y))

    def test_short_list_returns_nan(self) -> None:
        assert math.isnan(loo_mod.pearson_r([1.0, 2.0], [1.0, 2.0]))

    def test_known_correlation(self) -> None:
        x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        y = [2.1, 3.9, 6.2, 7.8, 10.1, 12.0]
        r = loo_mod.pearson_r(x, y)
        assert r > 0.99


def pytest_approx(val: float, abs: float = 1e-6):  # noqa: A002
    """Minimal approx helper for pure-assert testing."""

    class Approx:
        def __eq__(self, other: object) -> bool:
            if not isinstance(other, float):
                return False
            return abs_(other - val) <= abs  # noqa: B023

        def __repr__(self) -> str:
            return f"≈{val}"

    abs_ = builtins_abs
    return Approx()


builtins_abs = builtins.abs


class TestEpsilonData:
    def test_epsilon_length(self) -> None:
        assert len(loo_mod.EPS) == 11

    def test_epsilon_all_positive(self) -> None:
        assert all(e > 0 for e in loo_mod.EPS)

    def test_epsilon_peak_at_z040(self) -> None:
        """ε peaks at z=0.40 (index 3) as documented in Table A1."""
        idx_peak = loo_mod.EPS.index(max(loo_mod.EPS))
        assert loo_mod.Z[idx_peak] == 0.40

    def test_epsilon_non_monotone(self) -> None:
        """ε must not be monotone — core constraint for k_A analysis."""
        diffs = [loo_mod.EPS[i + 1] - loo_mod.EPS[i] for i in range(len(loo_mod.EPS) - 1)]
        sign_changes = sum(1 for i in range(len(diffs) - 1) if diffs[i] * diffs[i + 1] < 0)
        assert sign_changes >= 2, "ε(z) must have ≥2 sign changes to be non-monotone"


class TestProxies:
    def test_virial_proxy_monotone(self) -> None:
        """Virial k_A ∝ H(z)^(4/3) must be monotonically increasing with z."""
        vals = [loo_mod.proxy_virial(z) for z in loo_mod.Z]
        diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        assert all(d > 0 for d in diffs), "Virial proxy must be monotone increasing"

    def test_gaussian_peaks_at_target(self) -> None:
        """Gaussian bell must peak at specified z_peak."""
        z_peak = 0.40
        vals = [loo_mod.proxy_gaussian(z, z_peak=z_peak) for z in loo_mod.Z]
        peak_idx = vals.index(max(vals))
        assert loo_mod.Z[peak_idx] == z_peak

    def test_gaussian_symmetric(self) -> None:
        """Gaussian must be symmetric around z_peak."""
        for z_peak in [0.40, 1.00]:
            v_left = loo_mod.proxy_gaussian(z_peak - 0.1, z_peak=z_peak)
            v_right = loo_mod.proxy_gaussian(z_peak + 0.1, z_peak=z_peak)
            assert abs(v_left - v_right) < 1e-10

    def test_lognormal_peak_positive(self) -> None:
        """LogNormal proxy must be positive everywhere."""
        for z in loo_mod.Z:
            val = loo_mod.proxy_lognormal(z, mu=0.0, sigma_ln=1.0)
            assert val > 0


class TestLOOAnalysis:
    def test_loo_length(self) -> None:
        """LOO must return N entries."""
        proxy = [loo_mod.proxy_gaussian(z) for z in loo_mod.Z]
        result = loo_mod.loo_analysis(proxy, loo_mod.EPS, loo_mod.Z)
        assert len(result["loo_points"]) == 11

    def test_loo_delta_r_definition(self) -> None:
        """delta_r = r_full - r_loo must be consistent."""
        proxy = [loo_mod.proxy_virial(z) for z in loo_mod.Z]
        result = loo_mod.loo_analysis(proxy, loo_mod.EPS, loo_mod.Z)
        r_full = result["r_full"]
        for pt in result["loo_points"]:
            expected_delta = round(r_full - pt["r_loo"], 4)
            assert abs(pt["delta_r"] - expected_delta) < 1e-3

    def test_virial_all_negative_r(self) -> None:
        """Virial proxy must anti-correlate with ε (expected fail baseline)."""
        proxy = [loo_mod.proxy_virial(z) for z in loo_mod.Z]
        result = loo_mod.loo_analysis(proxy, loo_mod.EPS, loo_mod.Z)
        assert result["r_full"] < 0, "Virial proxy anti-correlates with ε(z)"

    def test_lognormal_fit_r_above_threshold(self) -> None:
        """Best LogNormal fit must achieve r > 0.85 (validates fit quality)."""
        mu, sig, r = loo_mod.fit_lognormal_grid(loo_mod.Z, loo_mod.EPS)
        assert r > 0.85, f"LogNormal best r={r:.4f} must be > 0.85"

    def test_lognormal_z_peak_physical_range(self) -> None:
        """Best-fit z_peak must be in physically plausible range [0.2, 1.5]."""
        mu, sig, r = loo_mod.fit_lognormal_grid(loo_mod.Z, loo_mod.EPS)
        z_peak = math.exp(mu) - 0.01
        assert 0.2 <= z_peak <= 1.5, f"z_peak={z_peak:.3f} outside physical range [0.2, 1.5]"


# ── TNG module tests ───────────────────────────────────────────────────────────


class TestTNGProxies:
    def test_virial_proxy_monotone_all_masses(self) -> None:
        """TNG virial k_A must be monotone for all mass thresholds (NR-004 consistency)."""
        for m_min in [1e14, 5e14, 2e15]:
            vals = [tng_mod.kinetic_energy_proxy_tng(z, m_min) for z in tng_mod.Z_TARGET]
            monotone, sign_changes = tng_mod.is_monotone(vals)
            assert monotone, (
                f"TNG virial proxy must be monotone for M_min={m_min:.0e}; "
                f"got {sign_changes} sign changes"
            )

    def test_merger_proxy_non_monotone(self) -> None:
        """Merger rate proxy must show non-monotone behavior."""
        vals = [tng_mod.merger_rate_proxy(z) for z in tng_mod.Z_TARGET]
        monotone, sign_changes = tng_mod.is_monotone(vals)
        assert not monotone, "Merger proxy must be non-monotone"

    def test_merger_proxy_peak_at_low_z(self) -> None:
        """Merger proxy must peak at z < 2 (physical: mergers peak at z≈0.4–1.0)."""
        vals = [tng_mod.merger_rate_proxy(z) for z in tng_mod.Z_TARGET]
        peak_z = tng_mod.Z_TARGET[vals.index(max(vals))]
        assert peak_z <= 1.0, f"Merger proxy peak at z={peak_z}, expected ≤1.0"

    def test_merger_proxy_positive_r(self) -> None:
        """Merger proxy must correlate positively with ε(z) (r > 0.50)."""
        vals = [tng_mod.merger_rate_proxy(z) for z in tng_mod.Z_TARGET]
        r = tng_mod.pearson_r(vals, tng_mod.EPS)
        assert r > 0.50, f"Merger proxy Pearson r={r:.4f}, expected > 0.50"

    def test_normalize_range(self) -> None:
        """Normalized values must be in [0, 1]."""
        vals = [1.0, 2.0, 5.0, 3.0]
        normed = tng_mod.normalize(vals)
        assert min(normed) == pytest_approx(0.0, abs=1e-10)
        assert max(normed) == pytest_approx(1.0, abs=1e-10)

    def test_is_monotone_true(self) -> None:
        assert tng_mod.is_monotone([1.0, 2.0, 3.0, 4.0]) == (True, 0)

    def test_is_monotone_false(self) -> None:
        mono, sc = tng_mod.is_monotone([1.0, 3.0, 2.0, 4.0])
        assert not mono
        assert sc == 2

    def test_epsilon_length_tng(self) -> None:
        assert len(tng_mod.EPS) == len(tng_mod.Z_TARGET) == 11

    def test_epsilon_positive_tng(self) -> None:
        assert all(e > 0 for e in tng_mod.EPS)
