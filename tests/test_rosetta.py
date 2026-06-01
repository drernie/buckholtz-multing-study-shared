"""Smoke / characterization tests for the Buckholtz<->mainstream Rosetta registry.

Exercises the public API (was 0% covered) and locks the structural invariants:
every entry is well-formed, confidence buckets are disjoint, lookup is
case-insensitive with a real miss path.
"""

from src.rosetta import (
    ROSETTA_ENTRIES,
    RosettaEntry,
    get_all_rosetta_entries,
    get_high_confidence_mappings,
    get_low_confidence_mappings,
    lookup_term,
)


def test_all_entries_present_and_typed():
    entries = get_all_rosetta_entries()
    assert len(entries) == len(ROSETTA_ENTRIES)
    assert len(entries) >= 1
    assert all(isinstance(e, RosettaEntry) for e in entries)


def test_every_entry_well_formed():
    """Each mapping must name both sides, a valid confidence, and a caveat."""
    for e in get_all_rosetta_entries():
        assert e.buckholtz_term, "missing buckholtz_term"
        assert e.possible_mainstream_analogue, "missing mainstream analogue"
        assert e.confidence in {"low", "medium", "high"}, f"bad confidence: {e.confidence}"
        assert e.caveat, "mapping must carry a caveat (uncertainty is explicit)"


def test_confidence_buckets_are_consistent_and_disjoint():
    low = get_low_confidence_mappings()
    high = get_high_confidence_mappings()
    assert all(e.confidence == "low" for e in low)
    assert all(e.confidence == "high" for e in high)
    low_terms = {e.buckholtz_term for e in low}
    high_terms = {e.buckholtz_term for e in high}
    assert not (low_terms & high_terms), "low and high confidence must be disjoint"


def test_lookup_term_hit_miss_and_case_insensitive():
    known = get_all_rosetta_entries()[0].buckholtz_term
    found = lookup_term(known)
    assert found is not None
    assert found.buckholtz_term == known
    # case-insensitive (lookup lowercases both sides)
    assert lookup_term(known.upper()) is not None
    # genuine miss returns None
    assert lookup_term("not-a-real-buckholtz-term-zzz") is None
