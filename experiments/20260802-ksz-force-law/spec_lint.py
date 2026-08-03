"""Static linter for the kSZ specification documents.

Purpose: catch, before a specification reaches human or agent review, the
classes of ambiguity that rounds 3 and 4 found by hand. It is a cheap
pre-filter, not a substitute for review: it can only find defects with a
syntactic signature.

Run:  python spec_lint.py DRAFT_SPEC_v6.md
Exit: 0 if no findings, 1 otherwise.

Each check corresponds to an item of the ten-point pre-review checklist.
A check that cannot be made syntactic is not implemented and is listed in
UNIMPLEMENTED below, so that its absence is visible rather than assumed.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

UNIMPLEMENTED = [
    "grid values match a programmatic enumeration (needs the spec's own numbers)",
    "every terminal state has a transition (needs a state graph)",
    "pseudocode is executable without choosing an algorithm (semantic)",
]

VAGUE = [
    "approximately",
    "appropriate",
    "as needed",
    "as appropriate",
    "reasonable",
    "suitable",
    "roughly",
    "about the same",
    "similar to",
    "standard practice",
    "the usual",
    "sufficiently",
    "if necessary",
    "where appropriate",
]

# Words that are only acceptable when a formula is given nearby.
NEEDS_FORMULA = [
    "relative deviation",
    "relative difference",
    "bandwidth",
    "condition number",
    "rms",
]

# Named methods that must be written out rather than cited by name.
NAMED_METHODS = [
    "Silverman",
    "Scott",
    "rule of thumb",
    "Freedman",
    "Sturges",
]

PLACEHOLDER = re.compile(r"<[a-z_]{2,}>")
CODE_FENCE = re.compile(r"```(.*?)```", re.S)
UPPER_LABEL = re.compile(r"\b[A-Z][A-Z0-9_]{5,}\b")
IDENT = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")

# Identifiers that are English or library names, not spec symbols.
STOPWORDS = set(
    """a an the and or not if for in to of at is are be with on per by from
    every each all no one two three exactly see yes true false else then
    return require otherwise while over under above below into out up down
    min max sum mean round sqrt ln log abs int float64 float dtype shape
    size order method entropy spawn_key SeedSequence default_rng standard
    normal vector matrix lower upper Cholesky factor spline cubic knot
    boundary condition scipy numpy interpolate CubicSpline bc_type quantile
    linear stats gaussian_kde random Generator PCG64 sort ascending
    physical Mpc dimensionless column row rows drawn replacement same
    stream branch branches stage stages coarse refined node nodes grid
    step bins bin sims simulations simulated observed data dataset datasets
    value values number count counts report reported reports label labels
    outcome outcomes STOP PASS FAIL FLAG this that these those it its
    which where when what how why must may never always only also both
    either neither than then thus so such as but however
    ddof int64 integers inverse invert standard_normal KDE away based zero
    A B C D W R half from_zero
    """.split()
)


@dataclass
class Finding:
    check: str
    line: int
    text: str


def _lines(doc: str) -> list[str]:
    return doc.splitlines()


def _code_blocks(doc: str) -> str:
    return "\n".join(CODE_FENCE.findall(doc))


def check_placeholders(doc: str) -> list[Finding]:
    out = []
    for i, ln in enumerate(_lines(doc), 1):
        for m in PLACEHOLDER.finditer(ln):
            out.append(Finding("placeholder", i, m.group(0)))
    return out


def check_vague(doc: str) -> list[Finding]:
    out = []
    for i, ln in enumerate(_lines(doc), 1):
        low = ln.lower()
        for w in VAGUE:
            if w in low:
                out.append(Finding("vague-word", i, w))
    return out


def _section(doc: str, header_re: str) -> str:
    """Return the text of the section whose header matches, up to the next header."""
    m = re.search(header_re, doc, re.M)
    if not m:
        return ""
    rest = doc[m.end() :]
    nxt = re.search(r"^##\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def _companion_text(doc: str) -> str:
    """Text of every normative file the document declares, concatenated.

    From v7 the specification delegates constants, library contracts and the
    state machine to machine-readable files. A term defined there is defined;
    copying the formula back into the prose would recreate the drift the
    delegation exists to prevent.
    """
    names = set(re.findall(r"`([a-z_]+\.(?:yaml|json))`", doc))
    here = Path(__file__).resolve().parent
    parts = []
    for n in sorted(names):
        p = here / n
        if p.exists():
            parts.append(p.read_text(encoding="utf-8"))
    return "\n".join(parts)


def _defines(doc: str, term: str) -> bool:
    """True if the document defines `term` — the term stands left of an '=' somewhere.

    A loose 'there is an = nearby' test produced false negatives on v5, because
    unrelated equations sit inside the same control table. The definition must
    put the term itself on the left-hand side.
    """
    # The '=' must be an assignment, not a comparison: '==', '>=', '<=' and '!='
    # all read as a definition under a naive pattern, which would let a document
    # that only COMPARES a tolerance pass the has-a-formula check.
    pat = re.compile(rf"^[^=\n]*\b{re.escape(term)}\b[^=\n]{{0,60}}(?<![=<>!])=(?!=)", re.M | re.I)
    if pat.search(doc):
        return True
    # Companion files are YAML/JSON, where a definition reads "term: value".
    # Without this the delegation of a formula to a normative file would read
    # as an undefined term, and the only way to satisfy the check would be to
    # copy the formula back into the prose — the drift the delegation prevents.
    yml = re.compile(rf"^\s*\"?{re.escape(term)}\w*\"?\s*:", re.M | re.I)
    return bool(yml.search(doc))


def check_named_methods(doc: str) -> list[Finding]:
    """A named statistical rule must be written out, not cited by name."""
    out = []
    for i, ln in enumerate(_lines(doc), 1):
        for w in NAMED_METHODS:
            scope = doc + _companion_text(doc)
            if w.lower() in ln.lower() and not _defines(scope, "bandwidth_formula"):
                out.append(Finding("named-method-without-formula", i, w))
    return out


def check_needs_formula(doc: str) -> list[Finding]:
    """A tolerance term must be defined with the term on the left of an '='."""
    out = []
    seen: set[str] = set()
    for i, ln in enumerate(_lines(doc), 1):
        low = ln.lower()
        for w in NEEDS_FORMULA:
            scope = doc + _companion_text(doc)
            if w in low and w not in seen and not _defines(scope, w.split()[-1]):
                seen.add(w)
                out.append(Finding("tolerance-without-formula", i, w))
    return out


def check_seed_roots(doc: str) -> list[Finding]:
    """Every declared seed root must be assigned to at least one consumer."""
    out = []
    decl = {}
    for i, ln in enumerate(_lines(doc), 1):
        m = re.match(r"\s*(root[A-Za-z_]*)\s*=\s*SeedSequence", ln)
        if m:
            decl[m.group(1)] = i
    for name, line in decl.items():
        uses = len(re.findall(rf"\b{re.escape(name)}\b", doc)) - 1  # minus its own declaration
        # the symbol table also names it; require a use beyond declaration+table
        if uses <= 1:
            out.append(Finding("seed-root-declared-but-unassigned", line, name))
    return out


def check_registry(doc: str) -> list[Finding]:
    """Identifiers appearing inside code fences must appear in the symbol table."""
    out = []
    reg: set[str] = set()
    table = _section(doc, r"^##\s*1\..*Symbols")
    for row in re.findall(r"^\|\s*(`[^|]+`)\s*\|", table, re.M):
        for cell in re.findall(r"`([^`]+)`", row):
            for part in cell.split(","):
                sym = part.strip()
                sym = re.sub(r"\(.*?\)", "", sym).strip()
                sym = re.sub(r"[₀-₉]", "", sym)
                if sym:
                    reg.add(sym)
    code = _code_blocks(doc)
    # Only tokens used in a code-like position are candidates. A token sitting in
    # prose inside a fence (the spec uses fences for instruction text too) is not
    # an identifier, and flagging it produced ~90 false positives on the first run.
    codelike = set()
    for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*(\(|\[|=[^=]|\)|\])", code):
        codelike.add(m.group(1))
    for m in re.finditer(r"[=+\-*/]\s*([A-Za-z_][A-Za-z0-9_]*)\b", code):
        codelike.add(m.group(1))
    seen: set[str] = set()
    for tok in sorted(codelike):
        if tok in STOPWORDS or tok in reg or tok in seen:
            continue
        if tok.isupper() and len(tok) > 4:
            continue
        seen.add(tok)
        kind = "index-not-in-registry" if len(tok) == 1 else "identifier-not-in-registry"
        out.append(Finding(kind, 0, tok))
    return out


def check_duplicate_registry(doc: str) -> list[Finding]:
    """A symbol may not be defined twice in the table."""
    out = []
    counts: dict[str, int] = {}
    table = _section(doc, r"^##\s*1\..*Symbols")
    for row in re.findall(r"^\|\s*(`[^|]+`)\s*\|", table, re.M):
        for cell in re.findall(r"`([^`]+)`", row):
            for part in cell.split(","):
                sym = re.sub(r"\(.*?\)", "", part.strip()).strip()
                if sym:
                    counts[sym] = counts.get(sym, 0) + 1
    for sym, n in counts.items():
        if n > 1:
            out.append(Finding("symbol-defined-twice", 0, f"{sym} x{n}"))
    return out


def check_file_status(doc: str) -> list[Finding]:
    """Every named input file must carry a status token."""
    out = []
    statuses = ("PRIMARY", "CONTROL", "UNUSED")
    inputs = _section(doc, r"^##\s*2\..*Inputs")
    for i, ln in enumerate(_lines(inputs), 1):
        for m in re.finditer(r"`([\w./-]+\.(hdf|dat|csv|txt))`", ln):
            if not any(s in ln for s in statuses):
                out.append(Finding("input-file-without-status", i, m.group(1)))
    return out


def check_array_draws(doc: str) -> list[Finding]:
    """A random draw must state its shape and dtype."""
    out = []
    lines = _lines(doc)
    for i, ln in enumerate(lines, 1):
        if re.search(r"standard_normal|standard normal|~\s*N\(", ln):
            window = "\n".join(lines[max(0, i - 3) : i + 4])
            if "size=" not in window and "shape" not in window.lower():
                out.append(Finding("random-draw-without-shape", i, ln.strip()[:70]))
            elif "dtype" not in window:
                out.append(Finding("random-draw-without-dtype", i, ln.strip()[:70]))
    return out


def check_grid_overdetermined(doc: str) -> list[Finding]:
    """A grid must be given exactly one way."""
    out = []
    lines = _lines(doc)
    for i, ln in enumerate(lines, 1):
        window = " ".join(lines[max(0, i - 2) : i + 3]).lower()
        has_step = "step" in window
        has_enum = "{" in window and "…" in window or "..." in window
        has_endpoints = "endpoint" in window or "both endpoints" in window
        if sum([has_step, has_enum, has_endpoints]) >= 2 and (
            "step" in ln.lower() or "endpoint" in ln.lower()
        ):
            out.append(Finding("grid-given-more-than-one-way", i, ln.strip()[:70]))
    return out


def check_labels_defined(doc: str) -> list[Finding]:
    """Every outcome label used must appear in the reporting list."""
    out = []
    labels = {m for m in UPPER_LABEL.findall(doc) if "_" in m}
    tail = doc.split("### 15.11", 1)[-1] if "### 15.11" in doc else doc
    reported = {m for m in UPPER_LABEL.findall(tail) if "_" in m}
    # document-status labels are declared as a separate, non-emitted set
    status_block = _section(doc, r"^##\s*1\..*Symbols")
    m = re.search(r"Document-status labels\*\* are(.*?)by a run\.", status_block, re.S)
    if m:
        reported |= {x for x in UPPER_LABEL.findall(m.group(1)) if "_" in x}
    for lab in sorted(labels - reported):
        out.append(Finding("label-not-in-reporting-list", 0, lab))
    return out


CHECKS = [
    ("placeholders", check_placeholders),
    ("vague words", check_vague),
    ("named methods without formula", check_named_methods),
    ("tolerances without formula", check_needs_formula),
    ("seed roots unassigned", check_seed_roots),
    ("duplicate registry entries", check_duplicate_registry),
    ("input files without status", check_file_status),
    ("random draws without shape/dtype", check_array_draws),
    ("grids given more than one way", check_grid_overdetermined),
    ("labels missing from reporting list", check_labels_defined),
    ("identifiers not in registry", check_registry),
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    path = Path(argv[1])
    doc = path.read_text(encoding="utf-8")

    total = 0
    print("=" * 78)
    print(f"spec_lint  {path.name}")
    print("=" * 78)
    for name, fn in CHECKS:
        found = fn(doc)
        status = "clean" if not found else f"{len(found)} finding(s)"
        print(f"\n[{status:>16}]  {name}")
        for f in found[:14]:
            loc = f"line {f.line}" if f.line else "—"
            print(f"      {loc:>10}  {f.text}")
        if len(found) > 14:
            print(f"      … and {len(found) - 14} more")
        total += len(found)

    print("\n" + "-" * 78)
    print(f"TOTAL: {total} finding(s)")
    print("\nNOT checked by this linter (must be caught by review):")
    for u in UNIMPLEMENTED:
        print(f"  - {u}")
    print("-" * 78)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
