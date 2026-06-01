"""
Test beta normalization math — verify numerical relations between candidates.

All discovered relations are marked as candidate_relation (hypothesis, not fact).
"""

from src.beta_definitions import (
    BETA_D_CANDIDATE_1,
    BETA_D_CANDIDATE_2,
    BETA_Q_CANDIDATE_1,
    BETA_Q_CANDIDATE_2,
)


def test_beta_d_ratio_is_not_integer():
    """Beta_d candidates are not related by a simple integer factor."""
    ratio = BETA_D_CANDIDATE_1.value / BETA_D_CANDIDATE_2.value
    # Ratio is 5.4487..., not close to any integer ≤10
    assert not (4.9 < ratio < 5.1)  # not 5
    assert not (5.9 < ratio < 6.1)  # not 6


def test_beta_d_ratio_close_to_11_over_2():
    """Beta_d_1 ≈ (11/2) × beta_d_2 within 1% (candidate relation)."""
    ratio = BETA_D_CANDIDATE_1.value / BETA_D_CANDIDATE_2.value
    expected_ratio = 11 / 2  # 5.5
    relative_error = abs(ratio - expected_ratio) / expected_ratio

    # This is a candidate_relation, not a fact
    assert relative_error < 0.01, (
        f"Candidate relation: beta_d_1 ≈ (11/2) × beta_d_2. "
        f"Actual ratio: {ratio:.4f}, expected: {expected_ratio}, "
        f"error: {relative_error*100:.2f}%"
    )


def test_beta_q_ratio_close_to_128_over_3():
    """Beta_q_1 ≈ (128/3) × beta_q_2 within 0.1% (candidate relation)."""
    ratio = BETA_Q_CANDIDATE_1.value / BETA_Q_CANDIDATE_2.value
    expected_ratio = 128 / 3  # 42.6666...
    relative_error = abs(ratio - expected_ratio) / expected_ratio

    # This is a candidate_relation, not a fact
    assert relative_error < 0.001, (
        f"Candidate relation: beta_q_1 ≈ (128/3) × beta_q_2. "
        f"Actual ratio: {ratio:.4f}, expected: {expected_ratio:.4f}, "
        f"error: {relative_error*100:.2f}%"
    )


def test_beta_q_over_beta_d_candidate_1():
    """Beta_q_1 / beta_d_1 ≈ 19/10 within 0.5% (candidate relation)."""
    ratio = BETA_Q_CANDIDATE_1.value / BETA_D_CANDIDATE_1.value
    expected_ratio = 19 / 10  # 1.9
    relative_error = abs(ratio - expected_ratio) / expected_ratio

    assert relative_error < 0.005, (
        f"Candidate relation: beta_q_1 / beta_d_1 ≈ 19/10. "
        f"Actual: {ratio:.4f}, expected: {expected_ratio}, "
        f"error: {relative_error*100:.2f}%"
    )


def test_beta_q_over_beta_d_candidate_2():
    """Beta_q_2 / beta_d_2 ≈ 1/4 within 3% (candidate relation)."""
    ratio = BETA_Q_CANDIDATE_2.value / BETA_D_CANDIDATE_2.value
    expected_ratio = 1 / 4  # 0.25
    relative_error = abs(ratio - expected_ratio) / expected_ratio

    assert relative_error < 0.03, (
        f"Candidate relation: beta_q_2 / beta_d_2 ≈ 1/4. "
        f"Actual: {ratio:.4f}, expected: {expected_ratio}, "
        f"error: {relative_error*100:.2f}%"
    )


def test_cross_product_beta_d1_times_beta_q2():
    """Beta_d_1 × beta_q_2 ≈ beta_d_2 within 4% (candidate relation)."""
    product = BETA_D_CANDIDATE_1.value * BETA_Q_CANDIDATE_2.value
    expected = BETA_D_CANDIDATE_2.value
    relative_error = abs(product - expected) / expected

    assert relative_error < 0.04, (
        f"Candidate relation: beta_d_1 × beta_q_2 ≈ beta_d_2. "
        f"Actual product: {product:.4f}, expected: {expected}, "
        f"error: {relative_error*100:.2f}%"
    )


def test_hidden_scale_extraction_consistency():
    """
    If beta_d_2 = beta_d_1 / L_ref^2 and beta_q_2 = beta_q_1 / L_ref^4,
    then L_ref extracted from both should be consistent within 15%.

    Candidate hypothesis: L_ref ~ 2.3–2.6 Mpc (galaxy group scale).
    """
    import math

    # Extract L_ref from beta_d
    L_ref_from_d = math.sqrt(BETA_D_CANDIDATE_1.value / BETA_D_CANDIDATE_2.value)

    # Extract L_ref from beta_q
    L_ref_from_q = (BETA_Q_CANDIDATE_1.value / BETA_Q_CANDIDATE_2.value) ** (1 / 4)

    relative_difference = abs(L_ref_from_d - L_ref_from_q) / L_ref_from_d

    assert relative_difference < 0.15, (
        f"Hidden scale hypothesis: L_ref from beta_d and beta_q should match. "
        f"L_ref(beta_d) = {L_ref_from_d:.3f}, "
        f"L_ref(beta_q) = {L_ref_from_q:.3f}, "
        f"difference: {relative_difference*100:.1f}%"
    )

    # Check that L_ref is in plausible range for galaxy group scale
    assert (
        2.0 < L_ref_from_d < 3.0
    ), f"L_ref ~ {L_ref_from_d:.2f} Mpc is in galaxy group scale range (2–3 Mpc)"


def test_all_candidate_relations_are_marked():
    """
    Ensure test docstrings explicitly mark relations as 'candidate_relation'.

    This is a meta-test to prevent accidental claims of fact.
    """
    import inspect

    # Get all test functions in this module
    current_module = inspect.getmodule(inspect.currentframe())
    test_functions = [
        obj
        for name, obj in inspect.getmembers(current_module)
        if inspect.isfunction(obj) and name.startswith("test_beta")
    ]

    for func in test_functions:
        docstring = func.__doc__ or ""
        if "beta" in docstring.lower():
            # Check that 'candidate' appears in docstring
            assert "candidate" in docstring.lower(), (
                f"Test {func.__name__} mentions beta but does not mark as 'candidate_relation'. "
                f"All numerical relations between betas are hypotheses, not facts."
            )
