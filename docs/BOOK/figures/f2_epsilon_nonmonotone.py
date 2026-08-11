"""F2 — epsilon(z) = (H_MULT/H_FLRW)^2 - 1 is non-monotonic, peaking near
z=0.40. This single shape is why every constant- or power-law bridge
candidate (NR-001, NR-002) and every monotone k_A(z) mechanism (NR-003,
NR-004) was rejected: none of them can produce a peak.

Data: data/table_a1_source_verified.csv (source-verified transcription,
2026-08-03 correction applied). The table's own caption: "Responses, to
our prompt, by one online service that has bases in artificial
intelligence" -- so this curve characterizes THAT response, not a MULTING
calculation (see the book's Table A1 provenance chapter). Plotted here
purely as the descriptive object several bridge candidates tried and
failed to reproduce.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[3]
CSV = HERE / "data" / "table_a1_source_verified.csv"
OUT = Path(__file__).parent / "f2_epsilon_nonmonotone.png"

with CSV.open(encoding="utf-8") as f:
    lines = [ln for ln in f if not ln.startswith("#")]
rows = list(csv.DictReader(lines))
print(f"loaded {len(rows)} rows from {CSV.name}")

z = [float(r["z"]) for r in rows]
h_mult = [float(r["H_MULT"]) for r in rows]
h_flrw = [float(r["H_FLRW"]) for r in rows]
eps = [(hm / hf) ** 2 - 1 for hm, hf in zip(h_mult, h_flrw, strict=True)]

peak_i = max(range(len(eps)), key=lambda i: eps[i])
print(f"peak: z={z[peak_i]:.2f}, epsilon={eps[peak_i]:.3f}")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(z, eps, "o-", color="#3b6ea5", lw=1.6, ms=5)
ax.axvline(z[peak_i], color="#c0392b", ls="--", lw=0.9, alpha=0.7)
ax.annotate(
    f"peak: z={z[peak_i]:.2f}\nε={eps[peak_i]:.3f}",
    xy=(z[peak_i], eps[peak_i]),
    xytext=(15, -20),
    textcoords="offset points",
    fontsize=9,
    color="#c0392b",
    arrowprops={"arrowstyle": "->", "color": "#c0392b", "lw": 0.8},
)
ax.set_xlabel("z")
ax.set_ylabel(r"$\epsilon(z) = (H_{MULT}/H_{FLRW})^2 - 1$")
ax.set_title(
    "ε(z) is non-monotonic — the shape every rejected bridge candidate\ncould not reproduce (NR-001..NR-004)"
)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
