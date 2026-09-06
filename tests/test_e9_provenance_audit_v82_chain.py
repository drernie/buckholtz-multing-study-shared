"""Wire experiments/20260906-evidence-authority/E9_provenance_audit_v82_chain.py
into pytest tests/ -q. The underlying src/provenance_audit.py already has real
tests; this file guards the CHAIN DATA (v82's 10-input map) against silent
breakage or accidental edits, which src/provenance_audit.py's own tests
cannot see.
"""

from __future__ import annotations

from collections import Counter

from E9_provenance_audit_v82_chain import chain

from src.provenance_audit import Finding


def test_chain_audit_runs_without_crashing():
    issues = chain.audit()
    assert isinstance(issues, list)


def test_chain_has_both_circular_items_tjb_diagnosed():
    """Sec. II.F (node radius) and Sec. IV.M (H0_anchor) are TJB's OWN named
    circularities -- the tool must still find both, not just one."""
    issues = chain.audit()
    circular_steps = {i.step for i in issues if i.finding == Finding.CIRCULAR}
    assert any("node radius" in name for name in circular_steps)
    assert any("H0_anchor" in name for name in circular_steps)


def test_gas_mass_and_thermal_energy_are_outside_sigma_after_e13():
    """FINDING_E13 updated exactly these 2 entries (gas mass, thermal energy)
    from UNQUANTIFIED to OUTSIDE_SIGMA (63.0%) -- regression guard for that
    edit. A third step (cosmic chronometer H(z)) is also OUTSIDE_SIGMA, but at
    8.91% from the earlier, separate FINDING_E5 -- not this test's target."""
    issues = chain.audit()
    e13_steps = {
        "gas mass M_gas [v82 Class I, 'direct fit to real X-ray data']",
        "ICM thermal energy k_X [v82 Class I]",
    }
    outside_sigma_e13 = [
        i for i in issues if i.finding == Finding.OUTSIDE_SIGMA and i.step in e13_steps
    ]
    assert len(outside_sigma_e13) == 2
    for issue in outside_sigma_e13:
        assert "63.00%" in issue.detail


def test_undeclared_steps_is_empty():
    """Every step in this chain declares at least one Dependency -- if a step
    silently declares nothing, that is a real gap in the chain, not a pass."""
    assert chain.undeclared_steps() == []


def test_summary_counter_matches_step_count_minus_the_one_in_quoted_sigma_step():
    """Every step in this chain has exactly one Dependency, so it can produce
    at most one issue. Exactly one step (the SH0ES anchor, whose Cepheid
    calibration IS carried in its quoted sigma -- in_quoted_sigma=True)
    correctly produces none, per audit()'s own OUTSIDE_SIGMA branch. So the
    issue count is step count minus 1, not step count -- regression guard for
    that specific step's in_quoted_sigma flag."""
    issues = chain.audit()
    counts = Counter(i.finding.value for i in issues)
    assert sum(counts.values()) == len(chain.steps) - 1
    assert counts == {"UNQUANTIFIED": 4, "OUTSIDE_SIGMA": 3, "CIRCULAR": 2}
