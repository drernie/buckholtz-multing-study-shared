"""F9 — 17 null results as a timeline, grouped by which research thread
each one killed: bridge-candidate mechanisms (NR-001..009, 016..018), the
H1 cluster-correlation cycle (NR-010..015), and RG-boundary (NR-017 also
belongs to the mechanism-search group, listed once).

Data: parsed directly from null_results/INDEX.md's own table -- the single
canonical registry this project maintains for REJECT/KILL verdicts.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import re
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[3]
INDEX = HERE / "null_results" / "INDEX.md"
OUT = Path(__file__).parent / "f9_null_results_timeline.png"

text = INDEX.read_text(encoding="utf-8")
# escaped pipes inside cells (\|) would break a naive split -- protect them first.
protected = text.replace(r"\|", "\x00")
rows = re.findall(
    r"^\| (NR-\d+) \| (\d{4}-\d{2}-\d{2}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", protected, re.M
)
rows = [
    (r[0], r[1], r[2].replace("\x00", "|"), r[3].replace("\x00", "|"), r[4].replace("\x00", "|"))
    for r in rows
]
print(f"parsed {len(rows)} null-result entries")
assert len(rows) == 17, (
    f"expected 17 entries, parsed {len(rows)} -- check INDEX.md format before trusting this figure"
)

GROUPS = {
    # NR-013 was originally grouped under "H1 cluster cycle" here. Phase D
    # (Agent(skeptic), context-blind, 2026-08-11) checked it against its own
    # file: NR-013's Branch field reads "R011 -- the MULTING dipole/
    # quadrupole cosmic-acceleration mechanism, tested via
    # src/pearson_fit.py" -- the bridge/parametrization thread, not the
    # delta_M/E_ICM cluster-mass-bias thread H1 is about. pearl_registry/
    # INDEX.md's own 2026-07-18 row agrees, listing NR-013 among the
    # bridge-thread REJECTs (NR-001/002/003/004/005/008/009/013). Moved here.
    "bridge mechanism": {
        "NR-001",
        "NR-002",
        "NR-003",
        "NR-004",
        "NR-005",
        "NR-007",
        "NR-008",
        "NR-009",
        "NR-013",
        "NR-016",
        "NR-017",
        "NR-018",
    },
    "H1 cluster cycle": {"NR-010", "NR-011", "NR-012", "NR-014", "NR-015"},
}
group_of = {}
for g, ids in GROUPS.items():
    for i in ids:
        group_of[i] = g

colors = {"bridge mechanism": "#3b6ea5", "H1 cluster cycle": "#c0392b"}

fig, ax = plt.subplots(figsize=(11, 6))
for i, (nr_id, dt, slug, _verdict, _why) in enumerate(rows):
    g = group_of.get(nr_id, "other")
    c = colors.get(g, "#999999")
    ax.barh(i, 1, left=0, color=c, height=0.6)
    ax.text(1.03, i, f"{nr_id}  {dt}  {slug}", va="center", fontsize=8)

ax.set_yticks([])
ax.set_ylim(-0.5, len(rows) - 0.5)
ax.set_xlim(0, 4.2)
ax.invert_yaxis()
ax.set_xticks([])
ax.set_title(f"{len(rows)} null results, June-August 2026 — two research threads killed cleanly")
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colors.values()]
ax.legend(handles, colors.keys(), loc="lower right", fontsize=9)
for spine in ax.spines.values():
    spine.set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
