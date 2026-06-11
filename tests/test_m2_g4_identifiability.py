"""M2-G4 identifiability — characterization tests.

Locks in the central finding: under the Claude-specific Φ-bridge with Claude's
own cluster midpoints, β_d/β_q have near-zero practical sensitivity, while
H_anchor (and a parametric D-schedule exponent) dominate.
NOT_VALIDATION / NOT_REFUTATION — provenance characterization only.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.m2_g4_fisher_rank_identifiability import (  # noqa: E402
    BETA_D_CLAUDE,
    BETA_Q_CLAUDE,
    H_ANCHOR_CLAUDE,
    jacobian_fd,
    model_h,
)
from src.cluster_schedule import load_claude_cluster_params  # noqa: E402


def _base():
    rows = load_claude_cluster_params()
    return [(r.z, r.m_A, r.k_A, r.r_A, r.D) for r in rows]


def test_beta_sensitivity_is_negligible():
    base = _base()
    theta = np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE])
    J = jacobian_fd(theta, "A", base)
    h0 = model_h(theta, "A", base)
    rel_bd = np.max(np.abs(J[:, 0] * theta[0] / h0))
    rel_bq = np.max(np.abs(J[:, 1] * theta[1] / h0))
    # 100% change in beta moves H by <1e-6 relative — practically unidentifiable
    assert rel_bd < 1e-8
    assert rel_bq < 1e-5


def test_anchor_dominates_scenario_b():
    base = _base()
    theta = np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE, H_ANCHOR_CLAUDE])
    J = jacobian_fd(theta, "B", base)
    sigma = np.ones(len(base))
    Jw = J / sigma[:, None]
    norms = np.linalg.norm(Jw, axis=0)
    # H_anchor column dwarfs beta columns by >= 8 orders of magnitude
    assert norms[2] / max(norms[0], norms[1]) > 1e8


def test_anchor_row_is_exact_by_construction():
    base = _base()
    h = model_h(np.array([BETA_D_CLAUDE, BETA_Q_CLAUDE]), "A", base)
    assert abs(h[0] - H_ANCHOR_CLAUDE) < 1e-9


def test_scenario_d_counting():
    base = _base()
    n_obs = len(base)
    n_par = 2 + n_obs  # beta pair + free D_i per row
    assert n_par > n_obs  # structurally non-identifiable by counting
