# Upstream sources — not vendored

The upstream analysis code is NOT copied into this repository (it is third-party
and would fail our lint gate; modifying it would corrupt the reference). Fetch it
from the public release accompanying arXiv:2604.14327:

    github.com/patogallardo/pairwiseksz_mond

Files referenced in our work:

| File | What it defines |
|---|---|
| `export_sdss_pairwise_curve.py` | `g(r) = [1/(1+xi(r))] * I(r)/r**2`, `I(r) = int_6^r xi(r')r'^2 dr'` — the PAIR-WEIGHTED kernel, feeds `fit1.py` |
| `fit2.py` | uses `I(r)/r**2` with NO `1/(1+xi)` factor — the exponent fit that produces n = 2.1 +- 0.3 |

The disagreement between those two conventions is a real upstream
inconsistency, not a reading error on our side. It moves our endpoint by 21%
(see `docs/132` and `task3_xi_covariance.py`). We report both.

Data files in this directory ARE vendored unmodified: `dr6.hdf`,
`xi_zbin2.dat`, `covariances_sdss_g.txt`, `sdss_g_sqrtg.csv`.
