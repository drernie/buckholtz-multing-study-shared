"""Regression tests for FINDING_P205's identifiability break condition.

`scripts/p205_identifiability_break_condition.py` was committed in `eee76c3`
as the constructive answer to bottleneck 4 (`FINDING_P133`'s structural
non-identifiability of `(A, g, kappa)`), but carried no coverage in
`tests/` -- so `pytest tests/ -q`, this project's mandated commit gate,
would not have noticed if it broke. Same blind spot `conftest.py`'s own
docstring records for the E-series scripts.

These tests deliberately RECOMPUTE the algebra from scratch with sympy
rather than only calling the script's `main()`. Calling `main()` would
only re-run the script's own internal assertions -- circular. The
recomputation here is an independent check of the same mathematical
claims; the smoke test at the end additionally confirms the script itself
still runs clean.

Claims under regression guard (from `FINDING_P205`):
  1. P133's observable set has Jacobian rank 2, not 3.
  2. The cause is the exact identity `O2 = O1 * O3^2`.
  3. A candidate monomial `A^a g^b kappa^c` raises the rank to 3 iff
     `2a != b + c`.
  4. Therefore a direct measurement of any single parameter suffices,
     and no further O1/O2/O3-family observable ever does.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import sympy as sp

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT = _REPO_ROOT / "scripts" / "p205_identifiability_break_condition.py"

A, G, K = sp.symbols("A g kappa", positive=True)

# FINDING_P133's own three observables.
O1 = A * G**2  # monopole-monopole
O2 = A * K**2  # dipole-dipole
O3 = K / G  # cross-sector ratio (eta)


def _rank(*exprs: sp.Expr) -> int:
    return sp.Matrix(list(exprs)).jacobian([A, G, K]).rank()


def _break_functional(a: int, b: int, c: int) -> int:
    return 2 * a - b - c


def test_p133_observable_set_has_rank_two() -> None:
    """Positive control: the degeneracy P205 builds on is real."""
    assert _rank(O1, O2, O3) == 2


def test_full_parameter_set_would_have_rank_three() -> None:
    """Sanity check on the machinery: a trivially identifiable set is
    correctly classified as rank 3, so rank 2 above is a real finding and
    not a broken rank computation."""
    assert _rank(A, G, K) == 3


def test_degeneracy_is_the_o2_identity_exactly() -> None:
    """`O2 - O1*O3^2` vanishes identically, not just at sampled points."""
    assert sp.simplify(O2 - O1 * O3**2) == 0


@pytest.mark.parametrize(
    ("exps", "should_break"),
    [
        ((1, 0, 0), True),  # A alone
        ((0, 1, 0), True),  # g alone
        ((0, 0, 1), True),  # kappa alone
        ((1, 1, 1), False),  # A g kappa
        ((2, 4, 0), False),  # A^2 g^4 == O1^2, negative control: must NOT break
        ((2, 2, 0), True),  # A^2 g^2: L = 2, breaks -- NOT the same as O1^2
        ((1, 2, 0), False),  # == O1, negative control: must NOT break
        ((0, -1, 1), False),  # == O3, negative control: must NOT break
        ((2, 1, 0), True),  # asymmetric, off the 2a = b + c plane
        ((0, 2, 0), True),  # g^2 alone
        ((1, 3, -1), False),  # 2 == 3 + (-1), degenerate despite odd exponents
    ],
)
def test_break_condition_predicts_recomputed_rank(
    exps: tuple[int, int, int], *, should_break: bool
) -> None:
    """The criterion `2a != b + c` must agree with the rank actually
    recomputed from a fresh 4x3 Jacobian, for every candidate."""
    a, b, c = exps
    candidate = A**a * G**b * K**c
    recomputed_rank = _rank(O1, O2, O3, candidate)
    predicted_rank = 3 if _break_functional(a, b, c) != 0 else 2
    assert recomputed_rank == predicted_rank
    assert (recomputed_rank == 3) is should_break


def test_no_recombination_of_existing_observables_ever_breaks_it() -> None:
    """Products and ratios of the existing channels stay degenerate.

    This is the negative half of P205's claim, and the practically
    important one: it says precision on the existing channels is not the
    bottleneck, so no amount of it can help.
    """
    for combo in (O1 * O2, O1 / O2, O1 * O3, O2 / O3, O1 * O2 * O3, O1 / (O2 * O3)):
        assert _rank(O1, O2, O3, combo) == 2


def test_script_still_runs_clean() -> None:
    """Smoke test: the committed script's own controls still pass."""
    result = subprocess.run(  # noqa: S603
        [sys.executable, str(_SCRIPT)],
        capture_output=True,
        text=True,
        cwd=_REPO_ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "BREAK CONDITION" in result.stdout
    assert "2a != b + c" in result.stdout
