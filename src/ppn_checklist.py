"""PPN Checklist for MULTING Solar System Compatibility.

This module defines PPN (Parametrized Post-Newtonian) checks for assessing whether
MULTING dipole/quadrupole terms are consistent with Solar System constraints.

**Current status:** ALL checks BLOCKED — MULTING lacks weak-field metric, Solar System
limit, k_A definition, and COM frame specification.

**NO CLAIMS OF REFUTATION OR VALIDATION ARE MADE.**

This is a diagnostic checklist to track what information is missing and what questions
need to be sent to the author.
"""

from dataclasses import dataclass
from enum import Enum


class CheckStatus(Enum):
    """Status of a PPN check."""

    APPLICABLE = "applicable"  # Check applies and can be performed
    BLOCKED = "blocked"  # Check applies but missing info prevents execution
    NOT_APPLICABLE = "not_applicable"  # Check does not apply to this theory
    UNKNOWN = "unknown"  # Not yet determined if check applies


class RiskLevel(Enum):
    """Risk level if check fails."""

    NONE = "none"  # No PPN conflict expected
    LOW = "low"  # Minor deviation, likely within error bars
    MEDIUM = "medium"  # Possible conflict, needs calculation
    HIGH = "high"  # Likely excluded by current constraints
    CRITICAL = "critical"  # Definitely excluded if interpretation correct


@dataclass
class PPNCheck:
    """Single PPN compatibility check."""

    check_id: str
    name: str
    description: str
    pnn_parameter: str  # gamma, beta, alpha1, alpha2, alpha3, etc.
    observational_constraint: str
    status: CheckStatus
    risk_level: RiskLevel
    blocker: str  # What information is missing
    author_question: str  # What to ask Buckholtz
    interpretation_branch: str  # Which interpretation this applies to
    safe_wording: str  # How to describe status honestly
    unsafe_wording: str  # What NOT to say


def get_ppn_checks() -> list[PPNCheck]:
    """Return all PPN checks for MULTING.

    Returns:
        List of PPNCheck objects.
    """
    return [
        PPNCheck(
            check_id="PPN-1",
            name="Light Deflection (γ parameter)",
            description=(
                "Check if MULTING predicts γ = 1 (GR value) for Solar System light "
                "deflection. Cassini constraint: γ - 1 = (2.1 ± 2.3) × 10⁻⁵."
            ),
            pnn_parameter="gamma",
            observational_constraint="γ - 1 = (2.1 ± 2.3) × 10⁻⁵ (Cassini)",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.HIGH,
            blocker="Weak-field metric missing. Cannot extract γ parameter.",
            author_question=(
                "Does MULTING have a weak-field metric? If so, what is γ_MULTING "
                "for Solar System?"
            ),
            interpretation_branch=("Branch 1 (local mass dipole), Branch 4 (metric modification)"),
            safe_wording=(
                "Cannot assess γ parameter without weak-field metric. Author "
                "clarification required."
            ),
            unsafe_wording="MULTING is ruled out by Cassini light deflection.",
        ),
        PPNCheck(
            check_id="PPN-2",
            name="Perihelion Precession (β parameter)",
            description=(
                "Check if MULTING predicts β = 1 (GR value) for Mercury perihelion "
                "shift. Constraint: β - 1 = (-4.1 ± 7.8) × 10⁻⁵."
            ),
            pnn_parameter="beta",
            observational_constraint="β - 1 = (-4.1 ± 7.8) × 10⁻⁵ (Mercury)",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.HIGH,
            blocker="Weak-field metric missing. Cannot extract β parameter.",
            author_question=(
                "Does MULTING have a weak-field metric? If so, what is β_MULTING "
                "for Solar System?"
            ),
            interpretation_branch=("Branch 1 (local mass dipole), Branch 4 (metric modification)"),
            safe_wording=(
                "Cannot assess β parameter without weak-field metric. Author "
                "clarification required."
            ),
            unsafe_wording="MULTING is excluded by Mercury perihelion observations.",
        ),
        PPNCheck(
            check_id="PPN-3",
            name="Preferred Frame (α₁ parameter)",
            description=(
                "Check if MULTING introduces preferred cosmic rest frame. Lunar laser "
                "ranging constraint: α₁ < 10⁻⁴."
            ),
            pnn_parameter="alpha1",
            observational_constraint="α₁ < 10⁻⁴ (lunar laser ranging)",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.CRITICAL,
            blocker=(
                "k_A definition missing. COM frame not specified. Unclear if dipole "
                "is velocity-dependent relative to cosmic rest frame."
            ),
            author_question=(
                "Is MULTING Lorentz-invariant, or does it introduce a preferred "
                "cosmic rest frame? If preferred frame, how does it satisfy α₁ < 10⁻⁴?"
            ),
            interpretation_branch=(
                "Branch 2 (kinetic energy dipole), Branch 3 (velocity-dependent)"
            ),
            safe_wording=(
                "Cannot assess preferred-frame effects without k_A definition and "
                "COM frame specification."
            ),
            unsafe_wording="MULTING violates Local Lorentz Invariance.",
        ),
        PPNCheck(
            check_id="PPN-4",
            name="CMB Dipole (α₂ parameter)",
            description=(
                "Check if MULTING modifies CMB dipole amplitude. Constraint: " "|α₂| < 4×10⁻⁷."
            ),
            pnn_parameter="alpha2",
            observational_constraint="|α₂| < 4×10⁻⁷ (CMB dipole)",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.CRITICAL,
            blocker="Same as PPN-3: k_A, COM frame, preferred frame unclear.",
            author_question=(
                "Does MULTING dipole term affect CMB dipole observations? What is " "α₂_MULTING?"
            ),
            interpretation_branch="Branch 3 (velocity-dependent)",
            safe_wording=(
                "Cannot assess CMB dipole effects without understanding dipole "
                "term's frame-dependence."
            ),
            unsafe_wording="MULTING is ruled out by CMB dipole constraints.",
        ),
        PPNCheck(
            check_id="PPN-5",
            name="Local Applicability (Scale Cutoff)",
            description=(
                "Check if dipole/quadrupole terms vanish at Solar System scales "
                "(r << r_d). If yes, PPN checks may not apply."
            ),
            pnn_parameter="N/A (applicability check)",
            observational_constraint="N/A",
            status=CheckStatus.UNKNOWN,
            risk_level=RiskLevel.NONE,
            blocker=("Cutoff function missing. Unclear if dipole ~ f(r/r_d) with f(r << r_d) → 0."),
            author_question=(
                "Does dipole term vanish for r << r_d (Solar System scale << cluster " "scale)?"
            ),
            interpretation_branch="Branch 5 (cluster-scale only)",
            safe_wording=(
                "If dipole is cluster-scale only (r ~ Mpc), Solar System PPN checks "
                "may not apply. Requires author confirmation."
            ),
            unsafe_wording="MULTING passes Solar System tests.",
        ),
        PPNCheck(
            check_id="PPN-6",
            name="Dipole COM Frame Behavior",
            description=(
                "Check if dipole term vanishes in center-of-mass frame of the system. "
                "If yes, dipole may be coordinate artifact."
            ),
            pnn_parameter="N/A (frame-dependence check)",
            observational_constraint="N/A",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.MEDIUM,
            blocker="Mathematical derivation of dipole in COM frame missing.",
            author_question=(
                "Does MULTING dipole term vanish when computed in the center-of-mass "
                "frame of the system?"
            ),
            interpretation_branch="Branch 2 (kinetic energy dipole)",
            safe_wording=(
                "Cannot determine if dipole is physical or frame-dependent without "
                "COM frame analysis."
            ),
            unsafe_wording="MULTING dipole violates COM frame invariance.",
        ),
        PPNCheck(
            check_id="PPN-7",
            name="Ordinary Matter Coupling",
            description=(
                "Check if dipole/quadrupole terms couple to ordinary matter (Sun, "
                "planets) or only to dark matter."
            ),
            pnn_parameter="N/A (applicability check)",
            observational_constraint="N/A",
            status=CheckStatus.BLOCKED,
            risk_level=RiskLevel.HIGH,
            blocker="Ordinary vs dark matter coupling specification missing.",
            author_question=(
                "Do dipole/quadrupole terms apply to ordinary Solar System matter, "
                "or only to dark matter?"
            ),
            interpretation_branch="All branches",
            safe_wording=(
                "If dipole couples only to dark matter, Solar System PPN checks "
                "may not apply. Requires author confirmation."
            ),
            unsafe_wording="MULTING violates Solar System constraints.",
        ),
    ]


def get_blockers_summary() -> dict[str, list[str]]:
    """Return summary of all blockers preventing PPN checks.

    Returns:
        Dictionary mapping blocker category to list of check IDs.
    """
    checks = get_ppn_checks()
    blockers: dict[str, list[str]] = {
        "no_metric": [],
        "no_k_A": [],
        "no_com_frame": [],
        "no_cutoff": [],
        "no_coupling_spec": [],
        "unknown_applicability": [],
    }

    for check in checks:
        if "metric" in check.blocker.lower():
            blockers["no_metric"].append(check.check_id)
        if "k_a" in check.blocker.lower():
            blockers["no_k_A"].append(check.check_id)
        if "com" in check.blocker.lower():
            blockers["no_com_frame"].append(check.check_id)
        if "cutoff" in check.blocker.lower():
            blockers["no_cutoff"].append(check.check_id)
        if "coupling" in check.blocker.lower():
            blockers["no_coupling_spec"].append(check.check_id)
        if check.status == CheckStatus.UNKNOWN:
            blockers["unknown_applicability"].append(check.check_id)

    return blockers


def get_author_questions() -> list[str]:
    """Extract all author questions from PPN checks.

    Returns:
        List of questions to send to Dr. Buckholtz.
    """
    checks = get_ppn_checks()
    questions = []
    seen = set()

    for check in checks:
        if check.author_question not in seen:
            questions.append(f"**{check.check_id}:** {check.author_question}")
            seen.add(check.author_question)

    return questions


def print_ppn_status():
    """Print PPN check status report."""
    checks = get_ppn_checks()

    print("=" * 80)
    print("PPN COMPATIBILITY CHECK STATUS (MULTING Solar System Limit)")
    print("=" * 80)
    print()

    # Status summary
    status_counts = dict.fromkeys(CheckStatus, 0)
    for check in checks:
        status_counts[check.status] += 1

    print("STATUS SUMMARY:")
    print(f"  APPLICABLE: {status_counts[CheckStatus.APPLICABLE]}")
    print(f"  BLOCKED: {status_counts[CheckStatus.BLOCKED]}")
    print(f"  NOT APPLICABLE: {status_counts[CheckStatus.NOT_APPLICABLE]}")
    print(f"  UNKNOWN: {status_counts[CheckStatus.UNKNOWN]}")
    print()

    # Blocked checks
    blocked = [c for c in checks if c.status == CheckStatus.BLOCKED]
    if blocked:
        print(f"BLOCKED CHECKS ({len(blocked)}):")
        for check in blocked:
            print(f"  [{check.check_id}] {check.name}")
            print(f"    Blocker: {check.blocker}")
            print()

    # Blockers summary
    blockers = get_blockers_summary()
    print("BLOCKER CATEGORIES:")
    for category, check_ids in blockers.items():
        if check_ids:
            print(f"  {category}: {', '.join(check_ids)}")
    print()

    # Author questions
    questions = get_author_questions()
    print(f"AUTHOR QUESTIONS ({len(questions)}):")
    for question in questions:
        print(f"  {question}")
    print()

    print("=" * 80)
    print("CONCLUSION: PPN check is currently BLOCKED.")
    print("No claims of refutation or validation can be made without author response.")
    print("=" * 80)


if __name__ == "__main__":
    print_ppn_status()
