"""
Cross-registry consistency guard for beta parameter provenance.

WHY THIS TEST EXISTS (skeptic audit finding H1/C8, 2026-06-01):
Two independent modules hold beta-parameter information:
  - src/beta_definitions.py  — epistemic status (unclear / fitted / derived / ...)
  - src/beta_provenance.py    — source provenance + use permission

Latent failure mode: the two registries drift apart, so a value that
beta_provenance flags `do_not_use_for_modeling` gets framed in
beta_definitions as a usable / confirmed quantity. That is exactly the
circular-reasoning trap the whole audit project exists to prevent
(use an audit-reconstructed value to "validate" the model on the same data).

Before this guard existed, nothing enforced that the two registries agree.
These tests lock the invariant: while H(z) modeling is blocked, neither
registry may present any beta as safe to model with, and every value in
beta_definitions must have a tracked, non-confirmed source in beta_provenance.

# WHY: a passing guard here is a regression lock, not a feature test —
# if a future edit unblocks modeling with an unverified beta, this turns red.
"""

from src.beta_definitions import get_all_beta_definitions
from src.beta_provenance import (
    BETA_PROVENANCE_REGISTRY,
    get_source_confirmed_betas,
    h_z_modeling_blocked,
    is_allowed_for_modeling,
)

# Statuses in beta_definitions that would imply a value is established enough
# to use in modeling. If a shared value carries one of these while provenance
# says do_not_use_for_modeling -> contradiction between the two registries.
_CONFIRMED_LIKE_STATUSES = {"fact", "derived", "calculation"}


def _provenance_by_value() -> dict[float, list]:
    """Index the provenance registry by numerical beta value."""
    by_value: dict[float, list] = {}
    for prov in BETA_PROVENANCE_REGISTRY.values():
        by_value.setdefault(round(prov.value, 6), []).append(prov)
    return by_value


def test_every_definition_value_has_provenance_entry():
    """Every value in beta_definitions must be tracked in beta_provenance.

    Catches the drift where a candidate value exists in one registry but its
    source is untracked in the other (skeptic finding C8 — untracked source =
    circular-reasoning risk).
    """
    prov_values = {round(p.value, 6) for p in BETA_PROVENANCE_REGISTRY.values()}
    for beta in get_all_beta_definitions():
        if beta.value is None:
            continue
        assert round(beta.value, 6) in prov_values, (
            f"beta_definitions has value {beta.value} ({beta.symbol}) with no "
            f"provenance entry in BETA_PROVENANCE_REGISTRY. Untracked source = "
            f"circular-reasoning risk."
        )


def test_no_confirmed_definition_for_unusable_provenance():
    """A value flagged do_not_use_for_modeling must not be framed as confirmed.

    The H1/C8 invariant: beta_definitions must not silently promote an
    audit-reconstruction / source-missing value to a modeling-grade status.
    """
    by_value = _provenance_by_value()
    for beta in get_all_beta_definitions():
        if beta.value is None:
            continue
        provs = by_value.get(round(beta.value, 6), [])
        unusable = any(p.use_permission_status == "do_not_use_for_modeling" for p in provs)
        if unusable:
            assert beta.status not in _CONFIRMED_LIKE_STATUSES, (
                f"{beta.symbol}={beta.value} is do_not_use_for_modeling in "
                f"provenance but beta_definitions marks it '{beta.status}'. "
                f"Contradiction: do not present an unverified beta as confirmed."
            )


def test_hz_modeling_blocked_implies_no_source_confirmed_beta():
    """Core safety invariant: while H(z) is blocked, no beta is source_confirmed.

    If this ever fails, someone unblocked modeling with an unverified
    parameter -> the exact failure mode the project is built to prevent.
    """
    if h_z_modeling_blocked():
        confirmed = get_source_confirmed_betas()
        assert confirmed == [], (
            "H(z) modeling is blocked, yet some beta is marked source_confirmed: "
            f"{confirmed}. Inconsistent permission state."
        )


def test_actual_table_a1_values_are_tracked_and_fit_only():
    """The manuscript Table A1 values (4.5, 18.0) must be tracked, fit-only.

    Verified source: preprints202511.0598.v6.pdf, Appendix A, Table A1 caption
    ("the online service reported choosing beta_d = 4.5 and beta_q = 18.0").
    They must NOT be modeling-grade — they are AI-service fitted values.
    """
    by_value = _provenance_by_value()
    for actual in (4.5, 18.0):
        provs = by_value.get(round(actual, 6), [])
        assert provs, f"Table A1 value {actual} missing from provenance registry."
        assert all(p.use_permission_status == "allowed_for_fit_reproduction_only" for p in provs), (
            f"Table A1 value {actual} must be fit-reproduction-only, not modeling-grade."
        )
        assert all(not is_allowed_for_modeling(p.beta_name) for p in provs), (
            f"Table A1 value {actual} must not be allowed for modeling (fitted to H(z))."
        )
