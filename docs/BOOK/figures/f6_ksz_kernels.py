"""F6 — the kSZ dipole/quadrupole kernels C_3(rho), C_4(rho): closed forms
that diverge (log and linear respectively) as a pair separation approaches
the cluster radius (rho -> 1), which is why an explicit UV regulator
(excision half-width eps, principal-value split) is required before any
fit -- not an optional refinement.

Formulas: state_machine.yaml / DRAFT_SPEC_v6.md section 5 (this repo's own
frozen kSZ specification):
    Pp(rho)  = 1 / (2*(1 - rho^2))
    Lam(rho) = ln|(1+rho)/(1-rho)| / (4*rho)
    G3(rho)  = Pp(rho) + Lam(rho)

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent / "f6_ksz_kernels.png"

rho = np.linspace(0.01, 0.999, 2000)
Pp = 1.0 / (2 * (1 - rho**2))
Lam = np.log(np.abs((1 + rho) / (1 - rho))) / (4 * rho)
G3 = Pp + Lam

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(rho, Pp, label=r"$P_p(\rho)$ — pole part (linear divergence)", color="#3b6ea5")
ax.plot(rho, Lam, label=r"$\Lambda(\rho)$ — log part (log divergence)", color="#2e8b57")
ax.plot(rho, G3, label=r"$G_3(\rho) = P_p + \Lambda$", color="#c0392b", lw=2)
ax.axvline(1.0, color="black", ls=":", lw=0.8)
ax.set_ylim(0, 30)
ax.set_xlabel(r"$\rho = s/R$")
ax.set_ylabel("kernel value")
ax.set_title(
    r"kSZ kernel diverges at $\rho \to 1$ — an explicit UV cutoff (excision $\epsilon$) is required"
)
ax.legend(fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT}")
print(
    f"Pp(0.99) = {1.0 / (2 * (1 - 0.99**2)):.2f}   Pp(0.999) = {1.0 / (2 * (1 - 0.999**2)):.2f}  (linear blow-up)"
)
