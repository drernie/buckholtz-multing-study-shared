"""
Test assumption dependency graph functionality.

Purpose: Ensure key dependencies are documented and graph functions work.
"""


from src.assumption_graph import (
    check_circular_dependency,
    get_all_dependencies,
    get_dependencies,
    get_dependency_chain,
    get_high_risk_dependencies,
    get_reverse_dependencies,
)


def test_key_nodes_exist():
    """Test that key dependency nodes are registered."""
    all_deps = get_all_dependencies()

    parents = {dep.parent for dep in all_deps}
    children = {dep.child for dep in all_deps}

    # Key nodes that should exist
    assert "H(z) fit" in parents, "H(z) fit should be a parent node"
    assert "beta_d" in children, "beta_d should be a child node"
    assert "beta_q" in children, "beta_q should be a child node"


def test_hz_fit_depends_on_both_betas():
    """H(z) fit should depend on both beta_d and beta_q."""
    hz_deps = get_dependencies("H(z) fit")

    dep_children = {dep.child for dep in hz_deps}

    assert "beta_d" in dep_children, "H(z) fit should depend on beta_d"
    assert "beta_q" in dep_children, "H(z) fit should depend on beta_q"


def test_high_risk_dependencies_marked():
    """High-risk dependencies should be properly flagged."""
    high_risk = get_high_risk_dependencies()

    assert len(high_risk) > 0, "Should have at least some high-risk dependencies"

    # Check specific high-risk items
    high_risk_pairs = {(dep.parent, dep.child) for dep in high_risk}

    assert (
        "H(z) fit",
        "beta_d",
    ) in high_risk_pairs, "H(z) fit depending on beta_d should be high-risk"
    assert (
        "H(z) fit",
        "beta_q",
    ) in high_risk_pairs, "H(z) fit depending on beta_q should be high-risk"


def test_reverse_dependencies():
    """Test reverse dependency lookup."""
    # beta_d is depended upon by multiple things
    reverse_deps = get_reverse_dependencies("beta_d")

    assert len(reverse_deps) > 0, "beta_d should have reverse dependencies"

    parents = {dep.parent for dep in reverse_deps}
    assert "H(z) fit" in parents, "H(z) fit should depend on beta_d"


def test_circular_dependency_detection():
    """Test circular dependency detection."""
    # Currently should have no circular dependencies in our registry
    # But test the function works

    # Test between two unrelated nodes (should be False)
    assert not check_circular_dependency(
        "beta_d", "beta_q"
    ), "beta_d and beta_q should not be circular"

    # Test self-dependency (would be circular if existed)
    assert not check_circular_dependency("H(z) fit", "H(z) fit"), "No self-dependency should exist"


def test_dependency_chain():
    """Test dependency chain extraction."""
    chains = get_dependency_chain("H(z) fit", max_depth=3)

    assert len(chains) > 0, "H(z) fit should have dependency chains"

    # Check that beta_d appears in at least one chain
    # Each chain is a list of node names (strings)
    beta_d_in_chain = any(any("beta_d" in str(node) for node in chain) for chain in chains)
    assert beta_d_in_chain, f"beta_d should appear in H(z) fit dependency chains. Chains: {chains}"


def test_ppn_constraints_exist():
    """MULTING terms should depend on PPN constraints."""
    all_deps = get_all_dependencies()

    ppn_deps = [dep for dep in all_deps if "PPN" in dep.child]

    assert len(ppn_deps) > 0, "PPN constraints should be in dependency graph"

    # Check specific MULTING terms
    ppn_parents = {dep.parent for dep in ppn_deps}

    assert "MULTING dipole term" in ppn_parents, "MULTING dipole should depend on PPN constraints"
    assert (
        "MULTING quadrupole term" in ppn_parents
    ), "MULTING quadrupole should depend on PPN constraints"


def test_eq15_dependencies_exist():
    """Eq.15 dependencies should be documented."""
    eq15_deps = get_dependencies("Eq.15 relation")

    assert len(eq15_deps) > 0, "Eq.15 should have dependencies documented"

    dep_children = {dep.child for dep in eq15_deps}

    assert (
        "exponent 6 mechanism" in dep_children or "prefactor 4/3 mechanism" in dep_children
    ), "Eq.15 should depend on mechanism explanations"


def test_idm_isomer_dependencies():
    """IDM 6-isomer claim should have dependencies."""
    isomer_deps = get_dependencies("6 isomers claim")

    assert len(isomer_deps) > 0, "6 isomers claim should have dependencies"

    dep_children = {dep.child for dep in isomer_deps}

    assert "isomer definition" in dep_children, "6 isomers should depend on isomer definition"
