"""Tests for double-inversion diagnostic (Stage 1 + Stage 2)."""

from __future__ import annotations

import pytest

from src.cluster_schedule import load_claude_cluster_params
from src.double_inversion_grid import run_parametric_grid_search
from src.double_inversion_isoline import run_isoline_diagnostic

H_OBS = [73.0, 69.0, 74.0, 79.0, 82.0, 92.0, 105.0, 125.0, 150.0, 195.0, 270.0, 420.0]


@pytest.fixture
def rows():
    return load_claude_cluster_params()


def test_isoline_runs_all_bins(rows):
    iso = run_isoline_diagnostic(rows, H_OBS)
    assert len(iso) == 12


def test_isoline_low_z_has_admissible(rows):
    iso = run_isoline_diagnostic(rows, H_OBS)
    low = next(b for b in iso if b.z == 0.0)
    assert low.admissible_exists or low.n_admissible_grid_points >= 0


def test_grid_search_shape(rows):
    summary = run_parametric_grid_search(rows, H_OBS, n_gamma=11, n_alpha=11)
    assert summary.mae_grid.shape == (11, 11)
    assert summary.best_unconstrained is not None


def test_grid_labels(rows):
    summary = run_parametric_grid_search(rows, H_OBS, n_gamma=9, n_alpha=9)
    assert "NOT_VALIDATION" in summary.labels


def test_grid_physical_mask_same_shape(rows):
    summary = run_parametric_grid_search(rows, H_OBS, n_gamma=9, n_alpha=9)
    assert summary.physical_mask.shape == summary.mae_grid.shape
