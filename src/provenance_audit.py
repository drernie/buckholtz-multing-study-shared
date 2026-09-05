"""Audit a measurement chain for hidden model dependence.

Implements the two-field classification developed in
`experiments/20260906-evidence-authority/FINDING_E6_generalized_classification.md`:
a step's declared class says which assumption it AVOIDS, which is not the same
as what it depends on INSTEAD. The failure mode this catches is the one measured
in FINDING_E5 -- cosmic chronometer H(z) correctly avoids assuming an expansion
history, and simultaneously carries a ~6.8% stellar-population-modelling
systematic that is fully correlated across redshift bins and absent from its
quoted error bar.

Three checks, each corresponding to a real, documented incident:

1. CIRCULAR      -- a step's incurred dependency is the very model under test
                    (v82 Sec. II.F's r_X(z) via rho_crit(z); Sec. IV.M's
                    H0_anchor via peculiar-velocity surveys).
2. UNQUANTIFIED  -- a step declares a dependency but no one has measured how
                    big it is. Not necessarily fatal; it is unknown, and that
                    is different from small.
3. OUTSIDE_SIGMA -- the dependency IS quantified but is not carried in the
                    quoted uncertainty, so downstream chi^2 under-quotes error
                    (the CC/errHz case, FINDING_E5 Result 3).

Deliberately NOT a solver or a corrector. It reports what a chain declares
about itself, so an unstated assumption becomes a visible blank rather than an
implicit pass. Declarations are the analyst's, and a wrong declaration produces
a wrong report -- garbage in, garbage out is the intended contract.

NOT_VALIDATION * OUR_RECONSTRUCTION * NO_AUTHOR_ERROR
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class Finding(StrEnum):
    """What an audit can say about one step."""

    CIRCULAR = "CIRCULAR"
    UNQUANTIFIED = "UNQUANTIFIED"
    OUTSIDE_SIGMA = "OUTSIDE_SIGMA"


@dataclass(frozen=True)
class Dependency:
    """One thing a measurement step depends on instead of the assumption it avoids.

    `magnitude_pct` is the size of the dependency as a percentage of the measured
    quantity, or None when nobody has measured it. `in_quoted_sigma` records
    whether that size is already carried in the step's reported uncertainty --
    the distinction that FINDING_E5's skeptic pass showed is load-bearing, since
    comparing a systematic against a sigma that excludes it by construction is
    incoherent.
    """

    name: str
    magnitude_pct: float | None = None
    in_quoted_sigma: bool = False
    correlated_across_bins: bool = False
    source: str = ""


@dataclass(frozen=True)
class Step:
    """One link in a measurement chain."""

    name: str
    avoids: str
    incurs: tuple[Dependency, ...] = ()


@dataclass(frozen=True)
class Issue:
    step: str
    dependency: str
    finding: Finding
    detail: str


@dataclass
class Chain:
    """A measurement chain audited against the model it is used to test."""

    measures: str
    tests_model: str
    steps: list[Step] = field(default_factory=list)

    def audit(self) -> list[Issue]:
        """Report every declared dependency that is circular, unmeasured, or
        quantified-but-not-propagated. Order is stable: by step, then by
        declaration order, so a diff of two audits is readable."""
        issues: list[Issue] = []
        model = self.tests_model.strip().casefold()

        for step in self.steps:
            for dep in step.incurs:
                if dep.name.strip().casefold() == model:
                    issues.append(
                        Issue(
                            step=step.name,
                            dependency=dep.name,
                            finding=Finding.CIRCULAR,
                            detail=(
                                f"step depends on '{dep.name}', which is the model under "
                                f"test ('{self.tests_model}'); the measurement cannot be "
                                f"independent evidence about it"
                            ),
                        )
                    )
                    continue

                if dep.magnitude_pct is None:
                    issues.append(
                        Issue(
                            step=step.name,
                            dependency=dep.name,
                            finding=Finding.UNQUANTIFIED,
                            detail=(
                                f"'{dep.name}' is declared but its size has never been "
                                f"measured -- unknown, which is not the same as small"
                            ),
                        )
                    )
                elif not dep.in_quoted_sigma:
                    corr = " and is correlated across bins" if dep.correlated_across_bins else ""
                    issues.append(
                        Issue(
                            step=step.name,
                            dependency=dep.name,
                            finding=Finding.OUTSIDE_SIGMA,
                            detail=(
                                f"'{dep.name}' is {dep.magnitude_pct:.2f}% of the measured "
                                f"quantity{corr}, but is not carried in the quoted "
                                f"uncertainty; a chi^2 using that sigma under-quotes error"
                            ),
                        )
                    )
        return issues

    def undeclared_steps(self) -> list[str]:
        """Steps that claim to avoid something but declare nothing incurred.

        Not automatically an error -- but FINDING_E5 found exactly one such step
        in this project's own pipeline (cosmic chronometers flagged
        `FLRW_independent = True` with nothing on the other side), and it was
        carrying a real ~6.8% dependency. A blank here means 'not yet asked',
        never 'nothing there'.
        """
        return [s.name for s in self.steps if not s.incurs]


def format_report(chain: Chain) -> str:
    """Plain-text audit report, suitable for pasting into a finding document."""
    lines = [
        f"Measurement chain: {chain.measures}",
        f"Used to test:      {chain.tests_model}",
        f"Steps:             {len(chain.steps)}",
        "",
    ]

    issues = chain.audit()
    if issues:
        lines.append(f"ISSUES ({len(issues)}):")
        for i in issues:
            lines.append(f"  [{i.finding.value}] {i.step} -> {i.dependency}")
            lines.append(f"      {i.detail}")
    else:
        lines.append("ISSUES: none among declared dependencies.")

    blanks = chain.undeclared_steps()
    if blanks:
        lines.append("")
        lines.append(f"UNDECLARED ({len(blanks)}) -- 'not yet asked', not 'nothing there':")
        for name in blanks:
            lines.append(f"  {name}")

    return "\n".join(lines)
