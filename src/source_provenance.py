"""Source Provenance System — Track Origin and Permission for All Values

PURPOSE:
Prevent silent mixing of values from different sources (manuscript vs audit vs AI).
Each value of each symbol carries a provenance tag with source, derivation status,
and use permission.

DESIGN:
- ProvenanceTag: immutable record of value origin
- ProvenanceRegistry: central registry of all tagged values
- Automatic conflict detection when multiple values exist for same symbol

INTEGRATION [CORRECTED 2026-09-07 — the arrow was backwards]:
- This module imports `beta_provenance`, not the other way round.
  `beta_provenance.py` does not import anything from here (verified: its
  only imports are `dataclasses` and `typing`). The original line claimed
  "beta_provenance.py uses this system for beta values", which was never
  true in code.
- `beta_provenance` itself IS live and well-wired: `beta_definitions.py`,
  `report.py`, this module, two tests and `scripts/brai_beta.py` use it.
- This module and `conflict_resolver.py` sit ON TOP of it and nothing
  above them uses either. Status: PARKED, see `docs/158`. Do NOT wire
  into `provenance_audit.py` — that module works at the CHAIN level
  (which assumption a step incurs), while this one works at the VALUE
  level (which number a symbol carries). They are different concerns.
- Known non-fit if revived for symbol-MEANING collisions (the live
  problem: `A` as field normalization vs `A` as a body subscript; `eta`
  as kappa/g vs `eta_q`): `ProvenanceTag` keys on (symbol, value) and so
  reads a collision as two competing VALUES of one quantity. It would
  need a namespace/meaning field it does not have.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class SourceType(Enum):
    """Where did this value come from?"""

    MANUSCRIPT_TABLE = "manuscript_table"  # Author's published table
    MANUSCRIPT_TEXT = "manuscript_text"  # Author's prose description
    MANUSCRIPT_EQUATION = "manuscript_equation"  # Explicit equation in manuscript
    AI_TRANSCRIPT = "ai_transcript"  # AI-generated supplementary materials
    AUDIT_RECONSTRUCTION = "audit_reconstruction"  # Our inference from patterns
    SUPPLEMENTARY_NOTE = "supplementary_note"  # Supplementary materials (author or AI)
    SOURCE_MISSING = "source_missing"  # Mentioned but not defined
    EXTERNAL_REFERENCE = "external_reference"  # Cited from external paper/database

    def __str__(self) -> str:
        return self.value


class DerivationStatus(Enum):
    """How was this value obtained?"""

    FITTED = "fitted"  # Fitted to observational data
    DERIVED = "derived"  # Derived from first principles
    ASSUMED = "assumed"  # Assumed without derivation
    RECONSTRUCTED = "reconstructed"  # Reconstructed by audit from hints
    INFERRED = "inferred"  # Inferred from context
    UNKNOWN = "unknown"  # Derivation method unclear
    REPORTED_NO_DERIVATION = "reported_no_derivation"  # Reported but not explained

    def __str__(self) -> str:
        return self.value


class UsePermission(Enum):
    """What computational uses are allowed?"""

    ALLOWED_FOR_FIT_REPRODUCTION_ONLY = "allowed_for_fit_reproduction_only"  # Retrodiction only
    ALLOWED_FOR_TOY_MODELING = "allowed_for_toy_modeling"  # Exploratory analysis with disclaimer
    ALLOWED_FOR_PREDICTION = "allowed_for_prediction"  # Can make predictions
    DO_NOT_USE = "do_not_use"  # Blocked (numerology, circular)
    REQUIRES_CLARIFICATION = "requires_clarification"  # Blocked pending author response
    MANUSCRIPT_CANONICAL = "manuscript_canonical"  # Author's definitive value

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class ProvenanceTag:
    """Immutable provenance record for a single value.

    Each value of each symbol gets exactly one ProvenanceTag.
    Tags are never modified — create new tag for updated information.
    """

    # Core identity
    symbol: str  # e.g., "beta_d", "beta_q", "H0"
    value: float  # Numerical value

    # Source information
    source_type: SourceType  # Where it came from
    manuscript_identifier: str | None = None  # e.g., "preprints202511.0598.v6.pdf"
    location: str | None = None  # e.g., "Appendix A.3, Table A1, row 5"

    # Epistemological status
    derivation_status: DerivationStatus = DerivationStatus.UNKNOWN
    use_permission: UsePermission = UsePermission.REQUIRES_CLARIFICATION

    # Verification
    verification_date: date | None = None  # When was this manually verified?
    verified_by: str = "audit_system"  # Who verified (human or system)?

    # Context
    notes: str = ""  # Free-text notes, warnings, caveats
    uncertainty: float | None = None  # Uncertainty if available
    units: str = "dimensionless"  # Physical units

    # Conflict tracking
    conflicts_with: list[str] = field(default_factory=list)  # List of conflicting tag IDs

    @property
    def tag_id(self) -> str:
        """Unique identifier for this provenance tag."""
        source_abbrev = {
            SourceType.MANUSCRIPT_TABLE: "MT",
            SourceType.MANUSCRIPT_TEXT: "MX",
            SourceType.MANUSCRIPT_EQUATION: "EQ",
            SourceType.AI_TRANSCRIPT: "AI",
            SourceType.AUDIT_RECONSTRUCTION: "AR",
            SourceType.SUPPLEMENTARY_NOTE: "SN",
            SourceType.SOURCE_MISSING: "SM",
            SourceType.EXTERNAL_REFERENCE: "EX",
        }
        abbrev = source_abbrev.get(self.source_type, "??")
        return f"{self.symbol}_{abbrev}_{self.value:.4f}"

    def is_authoritative(self) -> bool:
        """Is this value from author's primary work (not AI/audit)?"""
        authoritative_sources = {
            SourceType.MANUSCRIPT_TABLE,
            SourceType.MANUSCRIPT_TEXT,
            SourceType.MANUSCRIPT_EQUATION,
        }
        return self.source_type in authoritative_sources

    def allows_computation(self, use_case: str) -> bool:
        """Check if this value can be used for given computational use case.

        Args:
            use_case: One of "fit_reproduction", "toy_modeling", "prediction"

        Returns:
            True if use is allowed, False otherwise
        """
        use_case_map = {
            "fit_reproduction": {
                UsePermission.ALLOWED_FOR_FIT_REPRODUCTION_ONLY,
                UsePermission.ALLOWED_FOR_PREDICTION,
                UsePermission.MANUSCRIPT_CANONICAL,
            },
            "toy_modeling": {
                UsePermission.ALLOWED_FOR_TOY_MODELING,
                UsePermission.ALLOWED_FOR_PREDICTION,
            },
            "prediction": {
                UsePermission.ALLOWED_FOR_PREDICTION,
            },
        }

        allowed = use_case_map.get(use_case, set())
        return self.use_permission in allowed

    def to_dict(self) -> dict:
        """Export to dictionary for serialization."""
        return {
            "tag_id": self.tag_id,
            "symbol": self.symbol,
            "value": self.value,
            "source_type": str(self.source_type),
            "manuscript_identifier": self.manuscript_identifier,
            "location": self.location,
            "derivation_status": str(self.derivation_status),
            "use_permission": str(self.use_permission),
            "verification_date": self.verification_date.isoformat()
            if self.verification_date
            else None,
            "verified_by": self.verified_by,
            "notes": self.notes,
            "uncertainty": self.uncertainty,
            "units": self.units,
            "conflicts_with": self.conflicts_with,
        }


class ProvenanceRegistry:
    """Central registry of all provenance-tagged values.

    Responsibilities:
    - Store all ProvenanceTags
    - Detect conflicts (multiple values for same symbol)
    - Retrieve canonical value for given use case
    - Export conflict reports
    """

    def __init__(self):
        self._tags: dict[str, ProvenanceTag] = {}  # tag_id -> ProvenanceTag
        self._by_symbol: dict[str, list[str]] = {}  # symbol -> [tag_id, tag_id, ...]

    def register(self, tag: ProvenanceTag) -> None:
        """Register a new provenance tag.

        Automatically detects conflicts with existing tags for same symbol.
        """
        tag_id = tag.tag_id

        if tag_id in self._tags:
            # Exact same tag already registered — skip
            return

        # Store tag
        self._tags[tag_id] = tag

        # Index by symbol
        if tag.symbol not in self._by_symbol:
            self._by_symbol[tag.symbol] = []
        self._by_symbol[tag.symbol].append(tag_id)

    def get_all_values(self, symbol: str) -> list[ProvenanceTag]:
        """Get all registered values for a given symbol."""
        tag_ids = self._by_symbol.get(symbol, [])
        return [self._tags[tid] for tid in tag_ids]

    def has_conflict(self, symbol: str) -> bool:
        """Check if symbol has multiple conflicting values."""
        tags = self.get_all_values(symbol)

        if len(tags) <= 1:
            return False

        # Check if values differ beyond floating-point tolerance
        values = [tag.value for tag in tags]
        value_range = max(values) - min(values)

        # Conflict if range > 1% of mean value
        mean_value = sum(values) / len(values)
        return value_range > 0.01 * abs(mean_value)

    def get_canonical(
        self,
        symbol: str,
        use_case: str = "fit_reproduction",
        prefer_source: SourceType | None = None,
    ) -> ProvenanceTag | None:
        """Get canonical value for symbol given use case.

        Precedence rules:
        1. If prefer_source specified, use that source if available
        2. Manuscript table > manuscript text > manuscript equation
        3. Authoritative sources > audit reconstruction
        4. Must have appropriate use_permission for use_case

        Args:
            symbol: Symbol to look up (e.g., "beta_d")
            use_case: "fit_reproduction", "toy_modeling", or "prediction"
            prefer_source: Optional preferred source type

        Returns:
            ProvenanceTag if canonical value found, None otherwise
        """
        tags = self.get_all_values(symbol)

        if not tags:
            return None

        # Filter by use permission
        allowed_tags = [tag for tag in tags if tag.allows_computation(use_case)]

        if not allowed_tags:
            return None

        # Apply preference if specified
        if prefer_source:
            preferred = [tag for tag in allowed_tags if tag.source_type == prefer_source]
            if preferred:
                return preferred[0]

        # Precedence: manuscript_table > manuscript_text > manuscript_equation > others
        source_priority = [
            SourceType.MANUSCRIPT_TABLE,
            SourceType.MANUSCRIPT_TEXT,
            SourceType.MANUSCRIPT_EQUATION,
            SourceType.EXTERNAL_REFERENCE,
            SourceType.SUPPLEMENTARY_NOTE,
            SourceType.AUDIT_RECONSTRUCTION,
            SourceType.AI_TRANSCRIPT,
        ]

        for source_type in source_priority:
            matches = [tag for tag in allowed_tags if tag.source_type == source_type]
            if matches:
                return matches[0]

        # Fallback: return first allowed tag
        return allowed_tags[0]

    def export_conflict_summary(self) -> dict[str, list[dict]]:
        """Export summary of all conflicts for logging.

        Returns:
            Dict mapping symbol -> list of conflicting tag dicts
        """
        conflicts = {}

        for symbol in self._by_symbol.keys():
            if self.has_conflict(symbol):
                conflicts[symbol] = [tag.to_dict() for tag in self.get_all_values(symbol)]

        return conflicts

    def count_conflicts(self) -> int:
        """Count total number of symbols with conflicts."""
        return sum(1 for symbol in self._by_symbol.keys() if self.has_conflict(symbol))

    def list_symbols(self) -> list[str]:
        """List all registered symbols."""
        return sorted(self._by_symbol.keys())


# Global registry instance
_global_registry = ProvenanceRegistry()


def get_registry() -> ProvenanceRegistry:
    """Get global provenance registry singleton."""
    return _global_registry


def register_value(
    symbol: str,
    value: float,
    source_type: SourceType,
    derivation_status: DerivationStatus,
    use_permission: UsePermission,
    **kwargs,
) -> ProvenanceTag:
    """Convenience function to create and register a provenance tag.

    Args:
        symbol: Symbol name (e.g., "beta_d")
        value: Numerical value
        source_type: Where it came from
        derivation_status: How it was obtained
        use_permission: What uses are allowed
        **kwargs: Additional ProvenanceTag fields

    Returns:
        Created ProvenanceTag
    """
    tag = ProvenanceTag(
        symbol=symbol,
        value=value,
        source_type=source_type,
        derivation_status=derivation_status,
        use_permission=use_permission,
        **kwargs,
    )

    get_registry().register(tag)
    return tag
