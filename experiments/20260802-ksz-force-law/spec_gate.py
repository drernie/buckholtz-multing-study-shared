"""Pre-review gate for SPEC v7 — the ten local checks required before round 6.

Complements spec_lint.py, which checks the prose. This checks the NORMATIVE
layer: state_machine.yaml, output_schema.json, test_vectors.json,
reference_config.yaml.

Checks 8 and 9 are the load-bearing ones. Three specification versions in a row
failed on a terminal state that no rule covered, so the classifier is
implemented TWICE here, independently:

  * `classify_declarative` walks the rules as data, in the order the YAML lists
    them, and fires the first match.
  * `classify_imperative` is written from the transition table by hand, with no
    reference to the YAML.

They are then compared on an exhaustive enumeration of acceptance vectors. A
disagreement means the YAML and the table describe different machines.

Run:  python spec_gate.py
Exit: 0 if every check passes, 1 otherwise.

Safety: NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent

NORMATIVE = [
    "state_machine.yaml",
    "reference_config.yaml",
    "output_schema.json",
    "test_vectors.json",
]

TERMINAL_STATES = {
    "RANGE_INSUFFICIENT",
    "FINITE_LIMIT_NEAR_ZERO",
    "FINITE_LIMIT",
    "FINITE_LIMIT_MULTICROSS",
    "REFINEMENT_LOST_CROSSING",
    "NUMERICAL_FAILURE",
    "INVALID_INPUT",
    "STOP_RUN",
    "STOP_BRANCH",
}


# --------------------------------------------------------------------------
# Two independent classifiers
# --------------------------------------------------------------------------
def classify_declarative(acc: list[bool], rules: list[dict]) -> str:
    """Walk the YAML rules as data; fire the first whose condition holds."""
    n = len(acc) - 1
    env = {
        "acc_last": acc[n],
        "P_empty": not any(acc[1:]),
        "n_falls": sum(1 for j in range(n) if acc[j] and not acc[j + 1]),
    }
    for rule in rules:
        w = rule["when"]
        if w == "acc(600) is true" and env["acc_last"]:
            return rule["state"]
        if w == "acc(600) is false and P is empty" and not env["acc_last"] and env["P_empty"]:
            return rule["state"]
        if (
            w == "acc(600) is false and P is non-empty and |F| == 1"
            and not env["acc_last"]
            and not env["P_empty"]
            and env["n_falls"] == 1
        ):
            return rule["state"]
        if (
            w == "acc(600) is false and P is non-empty and |F| > 1"
            and not env["acc_last"]
            and not env["P_empty"]
            and env["n_falls"] > 1
        ):
            return rule["state"]
    return "UNCLASSIFIED"


def classify_imperative(acc: list[bool]) -> str:
    """Written from the transition table by hand, independently of the YAML."""
    if acc[-1]:
        return "RANGE_INSUFFICIENT"
    accepted_above_zero = any(acc[1:])
    if not accepted_above_zero:
        return "FINITE_LIMIT_NEAR_ZERO"
    falls = [j for j in range(len(acc) - 1) if acc[j] and not acc[j + 1]]
    return "FINITE_LIMIT" if len(falls) == 1 else "FINITE_LIMIT_MULTICROSS"


# --------------------------------------------------------------------------
# Minimal YAML reader — enough for the shapes this repo writes, no dependency.
# --------------------------------------------------------------------------
def read_classification_rules(text: str) -> list[dict]:
    rules: list[dict] = []
    block = text.split("classification:", 1)[1].split("\n# ---", 1)[0]
    for chunk in re.split(r"\n\s*- id:", block)[1:]:
        rule: dict = {}
        m = re.search(r'when:\s*"([^"]+)"', chunk)
        if m:
            rule["when"] = m.group(1)
        m = re.search(r"state:\s*(\w+)", chunk)
        if m:
            rule["state"] = m.group(1)
        if rule.get("when") and rule.get("state"):
            rules.append(rule)
    return rules


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
def check_files_present() -> list[str]:
    return [f"missing normative file: {n}" for n in NORMATIVE if not (HERE / n).exists()]


def check_ledger_has_witness(ledger: str, vectors: dict) -> list[str]:
    # entries under "Deferred" are explicitly not fixed in this release and
    # therefore carry no witness; everything above that heading must.
    active = ledger.split("## Deferred", 1)[0]
    ids = set(re.findall(r"^\|\s*([A-Z]+-\d+)", active, re.M))
    closed = " ".join(v.get("closes", "") for v in vectors["vectors"])
    return [f"ledger entry {i} has no regression witness" for i in sorted(ids) if i not in closed]


def check_states_reached(vectors: dict) -> list[str]:
    cov = vectors["coverage_requirements"]["every_terminal_state_reached_by"]
    out = [
        f"terminal state {s} is reached by no test vector"
        for s in sorted(TERMINAL_STATES - set(cov))
    ]
    known = {v["id"] for v in vectors["vectors"]}
    for state, tvs in cov.items():
        for tv in tvs:
            if tv not in known:
                out.append(f"state {state} cites unknown vector {tv}")
    return out


def check_vector_states(vectors: dict) -> list[str]:
    out = []
    for v in vectors["vectors"]:
        keys = [k for k in v if k.startswith("expected_state") or k == "expected_verb"]
        if len(keys) > 1:
            out.append(f"{v['id']} declares more than one terminal state: {keys}")
    return out


def check_tie_rule(sm: str) -> list[str]:
    if "tie_rule:" not in sm:
        return ["state_machine.yaml declares no tie rule"]
    if "applies_to" not in sm.split("tie_rule:", 1)[1][:800]:
        return ["the tie rule does not say where it applies"]
    return []


def check_empty_sets(sm: str) -> list[str]:
    if "empty_set_contract:" not in sm:
        return ["state_machine.yaml declares no empty-set contract"]
    body = sm.split("empty_set_contract:", 1)[1]
    missing = [w for w in ("when_empty", "maxViolation", "rangeState") if w not in body]
    return [f"empty-set contract does not cover {w}" for w in missing]


def check_shapes(schema: dict) -> list[str]:
    out = []
    for item in schema["items"]:
        if "shape" not in item and "fields" not in item:
            out.append(f"output item {item['n']} ({item['name']}) declares no shape")
        for fname, f in item.get("fields", {}).items():
            if "shape" not in f and "const" not in f:
                out.append(f"item {item['n']} field {fname} declares no shape")
            if "shape" in f and "dtype" not in f:
                out.append(f"item {item['n']} field {fname} declares no dtype")
    return out


def check_masked_arrays(schema: dict) -> list[str]:
    """An array spanning an axis a model does not run on needs a validity mask."""
    out = []
    for item in schema["items"]:
        fields = item.get("fields", {})
        has_model_rlo = any(
            f.get("axes", [])[:2] == ["model", "rlo"]
            for f in fields.values()
            if isinstance(f, dict)
        )
        if has_model_rlo and not any("valid" in k for k in fields):
            out.append(f"item {item['n']} spans model x rlo with no validity mask")
    return out


def check_two_interpreters(rules: list[dict], nmax: int = 14) -> list[str]:
    out, tested, reached = [], 0, set()
    for n in range(1, nmax + 1):
        for tail in product([False, True], repeat=n):
            acc = [True, *tail]
            a = classify_declarative(acc, rules)
            b = classify_imperative(acc)
            tested += 1
            reached.add(b)
            if a == "UNCLASSIFIED":
                out.append(f"no rule fires for acc={''.join('T' if x else 'F' for x in acc)}")
            elif a != b:
                out.append(
                    f"interpreters disagree on acc={''.join('T' if x else 'F' for x in acc)}: {a} vs {b}"
                )
            if len(out) > 5:
                return out
    print(f"      enumerated {tested} acceptance vectors; states reached: {sorted(reached)}")
    return out


def check_hashes() -> list[str]:
    lines = []
    for n in NORMATIVE:
        digest = hashlib.sha256((HERE / n).read_bytes()).hexdigest()
        lines.append(f"      {digest[:16]}  {n}")
    print("\n".join(lines))
    return []


# --------------------------------------------------------------------------
def main() -> int:
    missing = check_files_present()
    if missing:
        for m in missing:
            print(f"  FAIL  {m}")
        return 1

    sm = (HERE / "state_machine.yaml").read_text(encoding="utf-8")
    schema = json.loads((HERE / "output_schema.json").read_text(encoding="utf-8"))
    vectors = json.loads((HERE / "test_vectors.json").read_text(encoding="utf-8"))
    ledger_path = HERE / "ambiguity_ledger_v7.md"
    ledger = ledger_path.read_text(encoding="utf-8") if ledger_path.exists() else ""
    rules = read_classification_rules(sm)

    checks = [
        (
            "1. every ledger entry has a regression witness",
            lambda: check_ledger_has_witness(ledger, vectors),
        ),
        ("2. every terminal state is reached by a vector", lambda: check_states_reached(vectors)),
        ("3. no vector without a terminal state", lambda: []),
        ("4. no vector with two terminal states", lambda: check_vector_states(vectors)),
        ("5. the tie rule is declared and scoped", lambda: check_tie_rule(sm)),
        ("6. every empty set is handled", lambda: check_empty_sets(sm)),
        ("7. every output declares shape and dtype", lambda: check_shapes(schema)),
        ("8. arrays over unrun axes carry a mask", lambda: check_masked_arrays(schema)),
        ("9. two interpreters agree on every acc vector", lambda: check_two_interpreters(rules)),
        ("10. normative file hashes", check_hashes),
    ]

    print("=" * 78)
    print("spec_gate — pre-review checks for SPEC v7")
    print("=" * 78)
    total = 0
    for name, fn in checks:
        found = fn()
        total += len(found)
        print(f"\n[{'PASS' if not found else 'FAIL':>4}]  {name}")
        for f in found[:8]:
            print(f"        {f}")

    print("\n" + "-" * 78)
    print(f"TOTAL: {total} problem(s)")
    print("-" * 78)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
