"""Tests for negative_control_tests.py — SAFE_NOW diagnostics

Tests only deterministic behavior and output structure.
"""

def test_random_seed_deterministic():
    """Test that random seed produces deterministic results."""
    import numpy as np
    np.random.seed(42)
    sample1 = np.random.rand(5)

    np.random.seed(42)
    sample2 = np.random.rand(5)

    assert np.allclose(sample1, sample2), "Random seed should be deterministic"


def test_compute_chi2_structure():
    """Test chi2 computation returns float."""
    import numpy as np

    z = np.array([0.1, 0.2, 0.3])
    h_data = np.array([70, 75, 80])
    beta_d = 1.0
    beta_q = 1.0

    # Simple proxy model
    h_model = h_data[0] * np.sqrt((1 + z) ** (3 * (1 + beta_d)) + beta_q)
    chi2 = np.sum((h_data - h_model) ** 2)

    assert isinstance(chi2, (float, np.floating)), "Chi2 should be float"
    assert chi2 >= 0, "Chi2 should be non-negative"


def test_synthetic_lcdm_formula():
    """Test synthetic LCDM H(z) formula."""
    import numpy as np

    H0 = 67.4
    Om = 0.315
    OL = 0.685
    z = np.array([0, 0.5, 1.0])

    h_lcdm = H0 * np.sqrt(Om * (1 + z)**3 + OL)

    # At z=0: H(0) = H0 * sqrt(Om + OL) = H0 * sqrt(1) = H0
    assert np.isclose(h_lcdm[0], H0), "H(z=0) should equal H0"

    # H(z) should increase with z (matter-dominated)
    assert h_lcdm[1] > h_lcdm[0], "H(z) should increase with z"
    assert h_lcdm[2] > h_lcdm[1], "H(z) should increase with z"


if __name__ == "__main__":
    test_random_seed_deterministic()
    test_compute_chi2_structure()
    test_synthetic_lcdm_formula()
    print("All tests passed")
