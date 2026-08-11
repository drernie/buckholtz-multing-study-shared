"""F1 — Commit timeline: weekly commit counts over the project's 77 days,
with the milestones the chronology (01_CHRONOLOGY.md) already names.

Data source: `git log` on THIS repository, read live -- not a frozen file,
so the figure always matches the actual history. Run from the repo root.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt

OUT = Path(__file__).parent / "f1_commit_timeline.png"

# ---------------------------------------------------------------------------
# Pull every commit date, live, from this repo's own history.
# ---------------------------------------------------------------------------
result = subprocess.run(
    ["git", "log", "--format=%ad", "--date=short"],
    capture_output=True,
    text=True,
    check=True,
)
dates = [date.fromisoformat(d) for d in result.stdout.strip().split("\n")]
print(f"loaded {len(dates)} commit dates from git log")

first_day = min(dates)


def week_of(d: date) -> date:
    return first_day + timedelta(days=7 * ((d - first_day).days // 7))


weekly = Counter(week_of(d) for d in dates)
weeks = sorted(weekly)
counts = [weekly[w] for w in weeks]

# Milestones -- each date verified against git log in 01_CHRONOLOGY.md.
milestones = [
    (date(2026, 5, 30), "supplementary\nmaterial found"),
    (date(2026, 6, 15), "TJB answers\nQ1-Q3"),
    (date(2026, 7, 11), "PDG mass\nerror caught"),
    (date(2026, 7, 18), "NR-015: T_X\nshared-variable"),
    (date(2026, 8, 3), "Table A1 =\nAI output"),
    (date(2026, 8, 11), "NCG S3\nautomorphism"),
]

fig, ax = plt.subplots(figsize=(11, 5))
ax.bar(weeks, counts, width=6, color="#3b6ea5", alpha=0.85, edgecolor="none")
ax.set_xlabel("week")
ax.set_ylabel("commits")
ax.set_title(f"550 commits across 77 days ({first_day} → {max(dates)})")

for d, label in milestones:
    w = week_of(d)
    y = weekly.get(w, 0)
    ax.annotate(
        label,
        xy=(w, y),
        xytext=(0, 14),
        textcoords="offset points",
        ha="center",
        fontsize=7.5,
        rotation=0,
        arrowprops={"arrowstyle": "-", "color": "#c0392b", "lw": 0.8},
        color="#c0392b",
    )

ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
