"""
Epistemic registry: central data model for claims, parameters, and equations.

All records MUST have an explicit status marker to prevent silent assumptions.
"""

from dataclasses import dataclass
from typing import Literal

# Status taxonomy
Status = Literal[
    "fact",  # Verified measurement/observation
    "calculation",  # Reproduced numerical result
    "hypothesis",  # Proposed but not yet tested
    "inference",  # Logical conclusion from verified facts
    "assumption",  # Chosen premise without derivation
    "fitted",  # Phenomenological fit to data
    "derived",  # Mathematically derived from other claims
    "unknown",  # Status not determined
    "unclear",  # Conflicting or ambiguous information
    "requires_source_verification",  # Source needed or source unclear
]


@dataclass(frozen=True)
class SourceRef:
    """Reference to a source document or communication."""

    id: str
    title: str
    location: str  # DOI, URL, page number, email date, etc.
    url: str | None = None
    note: str = ""


@dataclass(frozen=True)
class Claim:
    """A falsifiable claim or assertion."""

    id: str
    text: str
    status: Status
    source: SourceRef | None
    testable: bool
    failure_condition: str | None  # What would falsify this claim
    notes: str = ""

    def __post_init__(self):
        """Validate claim invariants."""
        if self.status == "fact" and self.source is None:
            raise ValueError(
                f"Claim {self.id} marked as 'fact' but has no source. "
                "Facts require source attribution."
            )


@dataclass(frozen=True)
class Parameter:
    """A physical or mathematical parameter."""

    name: str
    symbol: str
    value: float | None
    units: str
    status: Status
    source: SourceRef | None
    interpretation: str  # What this parameter represents
    notes: str = ""

    def __post_init__(self):
        """Validate parameter invariants."""
        if self.status == "fact" and self.value is not None and self.source is None:
            raise ValueError(
                f"Parameter {self.symbol} has a value and status 'fact' "
                f"but no source. Facts require source attribution."
            )


@dataclass(frozen=True)
class EquationRecord:
    """Record of an equation or mathematical relation."""

    id: str
    label: str  # e.g., "Eq.15", "MULTING dipole term"
    expression_text: str  # LaTeX or plain text
    symbols: list[str]  # List of symbols used
    status: Status
    source: SourceRef | None
    dimensional_status: Literal[
        "not_checked",
        "passed",
        "failed",
        "requires_clarification",
    ]
    notes: str = ""

    def __post_init__(self):
        """Validate equation invariants."""
        if self.status not in ["requires_source_verification", "unknown", "unclear"]:
            if self.source is None:
                raise ValueError(
                    f"Equation {self.id} has status '{self.status}' "
                    f"but no source. Non-placeholder equations require sources."
                )
