"""F10 — NCG Variant C, full order-zero/first-order test: the null-space
of allowed generation-mixing operators Y_gen collapses 576 -> 8 -> 1 -> 0
as more random (a,b) algebra-element pairs are added to the first-order
constraint -- monotone, not a fluke of one sample. The single surviving
direction after 2 pairs (dimension 1, proportional to the identity, i.e.
no real mixing) is itself eliminated by a 3rd pair.

Data: re-runs experiments/20260810-ncg-spectral-triple/
variant_c_full_order_zero_first_order.py with n_pairs swept 1..4, parsing
each run's own printed null-space dimension -- not hand-copied from memory.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import re
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parents[3]
SCRIPT = (
    HERE
    / "experiments"
    / "20260810-ncg-spectral-triple"
    / "variant_c_full_order_zero_first_order.py"
)
OUT = Path(__file__).parent / "f10_ncg_nullspace_collapse.png"

results = []
for n_pairs in (1, 2, 3, 4):
    text = SCRIPT.read_text(encoding="utf-8")
    patched = re.sub(r"^n_pairs = \d+.*$", f"n_pairs = {n_pairs}", text, count=1, flags=re.M)
    tmp = SCRIPT.parent / f"_tmp_f10_npairs_{n_pairs}.py"
    tmp.write_text(patched, encoding="utf-8")
    try:
        proc = subprocess.run(
            ["python", str(tmp)],
            cwd=SCRIPT.parent,
            check=True,
            capture_output=True,
            text=True,
        )
        m = re.search(r"first-order null-space dimension.*?:\s*(\d+)", proc.stdout)
        dim = int(m.group(1))
        print(f"n_pairs={n_pairs}: null-space dim = {dim}")
        results.append((n_pairs, dim))
    finally:
        tmp.unlink()

fig, ax = plt.subplots(figsize=(7, 5))
xs = [r[0] for r in results]
ys = [r[1] for r in results]
ax.plot(xs, ys, "o-", color="#c0392b", ms=10, lw=2)
for x, y in results:
    ax.annotate(
        str(y), (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=10
    )
ax.set_yscale("symlog", linthresh=1)
ax.set_xlabel("random (a,b) algebra-element pairs added to the constraint")
ax.set_ylabel("dim{ Y_gen : first-order holds } (of 576)")
ax.set_xticks(xs)
ax.set_title("NCG Variant C: Y_gen null-space collapses monotonically to 0")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
