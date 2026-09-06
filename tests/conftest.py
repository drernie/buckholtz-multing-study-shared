"""Shared fixtures for wiring experiments/20260906-evidence-authority/'s
E-series scripts into pytest tests/ -q (this project's mandated commit gate).

Background: these scripts already carry their own positive-control
assertions (as module-level `test_*` functions), run only manually via
`python E8_....py`. `pytest tests/ -q` never discovered them -- a verified
blind spot from the 2026-09-06 boyko-project-radar scan: if
P176_v82_real_chi2_hessian_degeneracy.py (which E8/E8c import) or
E8_full_covariance_propagation.py itself (which E8b/E8c/E11/E12 import)
broke, the commit gate would not notice.
"""

from __future__ import annotations

import sys
from io import StringIO
from pathlib import Path

import pandas as pd
import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent
_BRIDGE_DIR = _REPO_ROOT / "experiments" / "20260803-bridge"
_EVIDENCE_DIR = _REPO_ROOT / "experiments" / "20260906-evidence-authority"
_E18_DIR = _EVIDENCE_DIR / "independent_verification_rerun"

for _p in (_BRIDGE_DIR, _EVIDENCE_DIR, _E18_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

# Real snapshot of gitlab.com/mmoresco/CCcovariance/-/raw/master/data/data_MM20.dat,
# fetched 2026-09-06 (the same session FINDING_E8/E9 used it) -- z=0.075..1.475,
# 29 rows. Frozen here for offline, deterministic tests, per this project's own
# `test_cluster_data_pipeline.py` convention (real-format snippet, not invented
# numbers). Columns renamed positionally by fetch_mm20() itself: mod->sps,
# mod_ooo->spsooo.
_DATA_MM20_REAL_TEXT = """\
# z   IMF  stlib  mod  mod_ooo
0.075 0.47 7.40 15.86 9.91
0.125 0.47 7.40 14.23 6.98
0.175 0.47 7.40 13.34 5.40
0.225 0.47 7.40 13.21 5.40
0.275 0.47 7.40 13.29 5.40
0.325 0.47 7.40 12.20 5.40
0.375 0.47 7.40 12.99 5.40
0.425 0.47 7.40 10.29 6.20
0.475 0.46 7.39 8.91 5.86
0.525 0.23 7.40 9.99 6.51
0.575 0.28 6.87 10.09 6.12
0.625 0.47 6.65 11.17 6.21
0.675 0.47 6.57 11.12 5.71
0.725 0.47 5.90 10.81 5.16
0.775 0.45 6.03 10.75 5.05
0.825 0.47 6.10 10.75 5.05
0.875 0.47 5.89 9.08 2.79
0.925 0.44 5.80 8.62 3.70
0.975 0.40 5.94 7.32 3.65
1.025 0.27 6.07 5.84 3.37
1.075 0.20 6.08 6.02 3.49
1.125 0.20 6.07 4.72 2.33
1.175 0.19 6.09 4.31 2.33
1.225 0.19 6.09 3.90 2.33
1.275 0.19 6.09 3.90 2.33
1.325 0.20 6.09 3.91 2.34
1.375 0.19 6.09 3.90 2.34
1.425 0.19 6.09 3.90 2.33
1.475 0.20 6.09 3.91 2.34
"""


@pytest.fixture(scope="session")
def mm20_real_text() -> str:
    """Raw text of the frozen real data_MM20.dat snapshot (see module
    docstring) -- for tests that exercise fetch_mm20()'s own parsing."""
    return _DATA_MM20_REAL_TEXT


@pytest.fixture(scope="session")
def mm20_real() -> pd.DataFrame:
    """The real data_MM20.dat snapshot, parsed exactly as fetch_mm20() does
    (whitespace-separated, comment header skipped, columns renamed
    positionally) -- without touching the network."""
    return pd.read_csv(
        StringIO(_DATA_MM20_REAL_TEXT),
        sep=r"\s+",
        comment="#",
        header=None,
        names=["z", "imf", "stlib", "sps", "spsooo"],
    )
