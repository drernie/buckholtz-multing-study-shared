"""
Smoke tests for double_inversion_plots.py — plotting side effects only.
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

These are deliberately NOT pixel-content checks (that would be theater --
asserting a PNG "looks right" without actually looking). What they DO
verify honestly: the plotting functions run to completion on real,
correctly-shaped inputs without raising, and actually write a non-empty
PNG file -- which catches real regressions (wrong argument order/type,
matplotlib API drift, broken imports) even though it says nothing about
whether the plot is scientifically meaningful.
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

from pathlib import Path

from src.cluster_schedule import ClusterRow
from src.double_inversion_grid import GridSearchResult, GridSearchSummary
from src.double_inversion_plots import (
    _output_dir,
    generate_all_plots,
    plot_grid_heatmap,
    plot_h_comparison,
    plot_isoline_for_z,
)


def _make_row(z: float = 0.0) -> ClusterRow:
    return ClusterRow(
        z=z,
        m_A=5.0e14,
        k_A=1.0e13,
        r_A=1.5,
        D=45.0,
        k_A_lo=5.0e12,
        k_A_hi=2.0e13,
        D_lo=40.0,
        D_hi=50.0,
    )


def _make_summary() -> GridSearchSummary:
    import numpy as np

    gamma_values = np.array([0.5, 1.0, 1.5])
    alpha_values = np.array([0.5, 1.0, 1.5])
    mae_grid = np.array([[1.0, 2.0, 3.0], [2.0, 1.0, 2.0], [3.0, 2.0, 1.0]])
    physical_mask = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=bool)
    best_physical = GridSearchResult(
        gamma=1.0, alpha=1.0, mae=1.0, rms_sigma=0.5, physically_admissible=True, flags=[]
    )
    best_unconstrained = GridSearchResult(
        gamma=0.5, alpha=0.5, mae=0.9, rms_sigma=0.4, physically_admissible=False, flags=["x"]
    )
    return GridSearchSummary(
        best_unconstrained=best_unconstrained,
        best_physical=best_physical,
        mae_grid=mae_grid,
        gamma_values=gamma_values,
        alpha_values=alpha_values,
        physical_mask=physical_mask,
        labels=["a", "b", "c"],
    )


class TestOutputDir:
    def test_creates_directory(self, tmp_path: Path) -> None:
        target = tmp_path / "nested" / "output"
        d = _output_dir(target)
        assert d == target
        assert d.is_dir()


class TestPlotIsolineForZ:
    def test_writes_nonempty_png(self, tmp_path: Path) -> None:
        row = _make_row(z=0.0)
        out_path = tmp_path / "isoline_z0.png"
        plot_isoline_for_z(
            row,
            H_target=70.0,
            phi_anchor=1.0,
            H_anchor=70.0,
            beta_d=4.5,
            beta_q=18.0,
            out_path=out_path,
            n=8,  # small grid -- this is a smoke test, not a resolution test
        )
        assert out_path.exists()
        assert out_path.stat().st_size > 0


class TestPlotGridHeatmap:
    def test_writes_nonempty_png(self, tmp_path: Path) -> None:
        out_path = tmp_path / "grid_heatmap.png"
        plot_grid_heatmap(_make_summary(), out_path)
        assert out_path.exists()
        assert out_path.stat().st_size > 0

    def test_handles_none_best_results(self, tmp_path: Path) -> None:
        """best_physical/best_unconstrained are Optional -- exercise the
        branch where the grid search found nothing admissible."""
        summary = _make_summary()
        summary.best_physical = None
        summary.best_unconstrained = None
        out_path = tmp_path / "grid_heatmap_empty.png"
        plot_grid_heatmap(summary, out_path)
        assert out_path.exists()
        assert out_path.stat().st_size > 0


class TestPlotHComparison:
    def test_writes_nonempty_png(self, tmp_path: Path) -> None:
        out_path = tmp_path / "h_comparison.png"
        plot_h_comparison(
            z_vals=[0.0, 0.5, 1.0],
            H_obs=[70.0, 90.0, 110.0],
            H_csv=[70.5, 89.0, 111.0],
            H_best_unc=[71.0, 88.5, 112.0],
            H_best_phys=[70.2, 89.5, 110.5],
            out_path=out_path,
        )
        assert out_path.exists()
        assert out_path.stat().st_size > 0

    def test_handles_none_optional_series(self, tmp_path: Path) -> None:
        out_path = tmp_path / "h_comparison_min.png"
        plot_h_comparison(
            z_vals=[0.0, 0.5],
            H_obs=[70.0, 90.0],
            H_csv=[70.5, 89.0],
            H_best_unc=None,
            H_best_phys=None,
            out_path=out_path,
        )
        assert out_path.exists()
        assert out_path.stat().st_size > 0


class TestGenerateAllPlots:
    def test_writes_all_expected_files(self, tmp_path: Path) -> None:
        rows = [_make_row(z=0.0), _make_row(z=1.0), _make_row(z=8.5)]
        paths = generate_all_plots(
            rows=rows,
            H_obs=[70.0, 110.0, 300.0],
            summary=_make_summary(),
            phi_anchor=1.0,
            H_anchor=70.0,
            output_dir=tmp_path,
        )
        assert len(paths) == 4  # 3 isoline plots (z=0,1,8.5) + 1 heatmap
        for p in paths:
            assert p.exists()
            assert p.stat().st_size > 0
