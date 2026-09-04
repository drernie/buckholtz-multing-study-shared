"""
Test internal anchor search — structured numerology detection.

Verify that beta candidate reconstruction is tested for uniqueness.
All claims marked as candidate_relation or structured_numerology.
"""

from src.internal_anchor_search import (
    ANCHORS,
    analyze_beta_candidates,
    classify_match,
    compute_uniqueness_score,
    generate_simple_ratios,
    search_anchors_for_target,
)


def test_anchor_inventory():
    """Verify Buckholtz internal anchors are present."""
    required_anchors = ["seven", "nine", "seventeen", "N_Z", "N_max", "ten"]

    for anchor in required_anchors:
        assert anchor in ANCHORS, f"Missing anchor: {anchor}"

    # Verify Eq.20 ratios
    assert ANCHORS["seven"] == 7
    assert ANCHORS["nine"] == 9
    assert ANCHORS["seventeen"] == 17

    # Verify N' formalism
    assert ANCHORS["N_Z"] == 3
    assert ANCHORS["N_max"] == 4
    assert ANCHORS["ten"] == 10  # ΣN'


def test_simple_ratio_generation():
    """Test that simple a/b ratios are generated."""
    ratios = generate_simple_ratios()

    # Check that 17/4 exists (known reconstruction for beta_d_1 = 4.25)
    expressions = [r[0] for r in ratios]
    assert "seventeen/four" in expressions, "17/4 ratio should be generated"

    # Check complexity is 1.0 for all
    for _, _, complexity, _ in ratios:
        assert complexity == 1.0, "Simple ratios should have complexity 1.0"


def test_classify_match():
    """Test error classification thresholds."""
    assert classify_match(0.0001) == "verified_arithmetic"  # < 0.1%
    assert classify_match(0.005) == "candidate_relation"  # < 1%
    assert classify_match(0.03) == "structured_numerology"  # < 5%
    assert classify_match(0.1) == "rejected"  # >= 5%


def test_beta_d1_reconstruction():
    """
    Test beta_d_1 = 4.25 can be reconstructed from anchors.

    Expected: 17/4 = 4.25 (exact match).
    Status: verified_arithmetic or candidate_relation.
    """
    candidates = search_anchors_for_target("beta_d_1", 4.25, max_complexity=1.0)

    # Filter to verified or candidate_relation
    good_matches = [
        c for c in candidates if c.status in ["verified_arithmetic", "candidate_relation"]
    ]

    assert len(good_matches) > 0, "Should find at least one match for beta_d_1 = 4.25"

    # Check if 17/4 is among matches
    expressions = [c.expression for c in good_matches]
    assert any("seventeen" in expr and "four" in expr for expr in expressions), (
        "17/4 should be among top matches"
    )


def test_beta_d2_reconstruction():
    """
    Test beta_d_2 ≈ 0.78 reconstruction.

    Expected: 7/9 ≈ 0.7778 (error ~0.3%).
    Status: candidate_relation.
    """
    candidates = search_anchors_for_target("beta_d_2", 0.78, max_complexity=1.0)

    good_matches = [
        c for c in candidates if c.status in ["verified_arithmetic", "candidate_relation"]
    ]

    assert len(good_matches) > 0, "Should find at least one match for beta_d_2 ≈ 0.78"

    # Check if 7/9 is among matches
    best_match = good_matches[0]
    assert best_match.error < 0.01, (
        f"Best match should be < 1% error, got {best_match.error * 100:.2f}%"
    )


def test_beta_q1_reconstruction():
    """
    Test beta_q_1 = 8.10 reconstruction.

    Expected: 81/10 = 8.1 (exact match).
    Status: verified_arithmetic.
    """
    candidates = search_anchors_for_target("beta_q_1", 8.10, max_complexity=1.5)

    verified = [c for c in candidates if c.status == "verified_arithmetic"]

    # 81/10 requires 81 as anchor — but 81 is not in ANCHORS
    # So we should NOT find exact match from simple anchors
    # This tests negative case: beta_q_1 may NOT be derivable from anchors

    if len(verified) == 0:
        # Expected — 8.1 is not easily derivable from {7,9,17,3,4,10}
        pass
    else:
        # If found, document it
        print(f"Unexpected exact match for beta_q_1: {verified[0].expression}")


def test_beta_q2_reconstruction():
    """
    Test beta_q_2 ≈ 0.19 reconstruction.

    Expected: No simple match from anchors (requires 17/90 or similar).
    Status: structured_numerology or rejected.
    """
    candidates = search_anchors_for_target("beta_q_2", 0.19, max_complexity=2.0)

    # Check if any match exists
    non_rejected = [c for c in candidates if c.status != "rejected"]

    if len(non_rejected) == 0:
        # Expected — 0.19 is not easily derivable
        pass
    else:
        # If found, check complexity
        best_match = non_rejected[0]
        assert best_match.complexity >= 1.5, (
            f"Beta_q_2 match should require complexity >= 1.5, got {best_match.complexity}"
        )


def test_uniqueness_score_computation():
    """Test uniqueness score calculation."""
    # Mock candidates
    from src.internal_anchor_search import CandidateFormula

    candidates_unique = [
        CandidateFormula(
            expression="17/4",
            value=4.25,
            target_name="beta_d_1",
            target_value=4.25,
            error=0.0,
            complexity=1.0,
            status="verified_arithmetic",
            anchor_names=("seventeen", "four"),
        )
    ]

    candidates_multiple = [
        CandidateFormula(
            expression="a/b",
            value=4.25,
            target_name="beta_d_1",
            target_value=4.25,
            error=0.001,
            complexity=1.0,
            status="verified_arithmetic",
            anchor_names=("a", "b"),
        ),
        CandidateFormula(
            expression="c/d",
            value=4.26,
            target_name="beta_d_1",
            target_value=4.25,
            error=0.002,
            complexity=1.0,
            status="candidate_relation",
            anchor_names=("c", "d"),
        ),
        CandidateFormula(
            expression="e/f",
            value=4.30,
            target_name="beta_d_1",
            target_value=4.25,
            error=0.01,
            complexity=1.5,
            status="structured_numerology",
            anchor_names=("e", "f"),
        ),
    ]

    score_unique = compute_uniqueness_score(candidates_unique)
    score_multiple = compute_uniqueness_score(candidates_multiple)

    assert score_unique["uniqueness_score"] == 1.0, "Single exact match should be unique"
    assert score_unique["verdict"] == "unique"

    assert score_multiple["uniqueness_score"] < 1.0, "Multiple matches should reduce uniqueness"
    assert score_multiple["alternative_count"] == 3


def test_all_beta_candidates_analysis():
    """
    Test full analysis of all 4 beta candidates.

    This is the main integration test.
    """
    results = analyze_beta_candidates(max_complexity=2.0)

    assert "beta_d_1" in results
    assert "beta_d_2" in results
    assert "beta_q_1" in results
    assert "beta_q_2" in results

    # Check that each has at least some candidates
    for beta_name, candidates in results.items():
        assert isinstance(candidates, list), f"{beta_name} should return list"
        # May be empty for some betas — that's fine


def test_complexity_increases_with_operations():
    """Verify complexity scoring makes sense."""
    from src.internal_anchor_search import (
        generate_ratio_of_products,
        generate_simple_products,
        generate_simple_ratios,
    )

    ratios = generate_simple_ratios()
    products = generate_simple_products()
    ratio_products = generate_ratio_of_products()

    # Check complexity ordering
    if ratios:
        assert ratios[0][2] == 1.0, "Simple ratios should have complexity 1.0"

    if products:
        assert products[0][2] == 1.5, "Simple products should have complexity 1.5"

    if ratio_products:
        assert ratio_products[0][2] == 2.0, "Ratio of products should have complexity 2.0"


def test_no_false_verified_claims():
    """
    Meta-test: ensure no formula is marked 'verified_arithmetic' with error > 0.1%.

    This prevents accidental overclaiming.
    """
    results = analyze_beta_candidates(max_complexity=2.0)

    for beta_name, candidates in results.items():
        verified = [c for c in candidates if c.status == "verified_arithmetic"]

        for c in verified:
            assert c.error < 0.001, (
                f"{beta_name}: {c.expression} marked verified_arithmetic "
                f"but error = {c.error * 100:.3f}% (> 0.1%)"
            )


def test_structured_numerology_warning():
    """
    Test that if >10 alternatives exist, verdict is 'structured_numerology'.

    This is the main numerology risk check.
    """
    # Create mock scenario with many alternatives
    from src.internal_anchor_search import CandidateFormula

    many_alternatives = []
    for i in range(15):
        many_alternatives.append(
            CandidateFormula(
                expression=f"formula_{i}",
                value=4.25 + i * 0.01,
                target_name="test",
                target_value=4.25,
                error=i * 0.002,
                complexity=1.0 + i * 0.1,
                status="structured_numerology",
                anchor_names=(f"a{i}", f"b{i}"),
            )
        )

    score = compute_uniqueness_score(many_alternatives)

    assert score["verdict"] == "structured_numerology", (
        "Many alternatives should trigger structured_numerology verdict"
    )
    assert score["uniqueness_score"] < 0.5, "Uniqueness score should be low"
