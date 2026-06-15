# Double-Inversion Diagnostic Report

**Labels:** VERIFIED_DIAGNOSTIC | NOT_VALIDATION | NOT_REFUTATION | AUTHOR_BRIDGE_NEEDED  
**Version:** v0.4.0 (2026-06-06)  
**Run:** `python audit/run_double_inversion_diagnostic.py`

---

## 1. Purpose

Test whether the reported H_MULT / H_obs curve can be reproduced from the **stated Phi-ratio bridge** using **physically admissible** D(z) and k_A(z) — not arbitrary fitted schedules.

Goal: **Does a physically admissible solution exist?** — not "find the best fit."

---

## 2. Formula used

```
Phi = m_A/D² − 2·k_A·β_d·r_A/D³ + k_A²·β_q²·r_A²/D⁴
H(z) = H₀ · sqrt(Phi(z)/Phi(0))
```

β_d=4.5, β_q=18.0 fixed (Table A1 fitted — not refitted here).  
**Provenance:** AI-transcript-reported bridge; AUTHOR_BRIDGE_NEEDED.

---

## 3. Data used

- `data/supplementary_extracted/claude_galaxy_cluster_parameters.csv`
- H_obs from `h_data_nominal` / hardcoded Table A1 list (12 rows)
- H₀ anchor = 73.0 km/s/Mpc

---

## 4. Physical constraints

| Constraint | Rule |
|------------|------|
| Separation | D > 2 r_A |
| Kinetic scale | k_A > 0 |
| Range box | k_A, D within ~order-of-magnitude of CSV stated ranges |
| Schedule | Flag extreme k_A jumps between adjacent z |

---

## 5. Stage 1 — Isoline results

For each z_i, scan (D, k_A) grid; find points where |H_bridge − H_obs| ≤ 2% · H_obs inside physical box.

**Per-bin outputs:** admissible_exists, min_k_A, min_D, csv_in_physical_box, distance_csv_to_isoline.

**Plots:** `audit/output/double_inversion/isoline_z{0.0,1.0,8.5}.png`

---

## 6. Stage 2 — Grid search results

Parametric forms (D₀, k₀ fixed from z=0 CSV — **not** fit to H):

```
D(z) = D₀ · (1+z)^(−γ)
k_A(z) = k₀ · (1+z)^(−α)
```

Grid: γ ∈ [0, 4], α ∈ [−6, 6].

Outputs:
- best unconstrained (min MAE)
- best physically admissible (min MAE with constraints)
- heatmap `grid_heatmap_mae.png`
- H(z) comparison `h_z_comparison.png`

---

## 7. Best-fit parameters

See console output from `run_double_inversion_diagnostic.py` after each run.

Typical pattern (diagnostic, not claim):
- Unconstrained minimum often at high γ (steep D falloff) matching D_required trend
- Physical admissibility may exclude much of the unconstrained minimum region

---

## 8. Do physically admissible solutions exist?

Three outcomes:

| Outcome | Interpretation |
|---------|----------------|
| **A — Physical zone exists** | Bridge can be self-consistent if D(z), k_A(z) defined in that region |
| **B — Fit only unphysical** | Table A1 implementation needs parameters outside physical box |
| **C — No smooth solution** | Alternate formula / normalization / AI fitting step suspected |

---

## 9. Interpretation boundary

- ✅ "Current **implementation** requires parameters outside physical box"
- ✅ "Constructive: author should specify independent k_A(z) rule"
- ❌ "MULTING is false"
- ❌ "Full theory falsified"
- ❌ No MCMC, no PySR, no public claims, no email

---

## Files

| Module | Role |
|--------|------|
| `src/double_inversion_isoline.py` | Stage 1 |
| `src/double_inversion_grid.py` | Stage 2 |
| `src/double_inversion_plots.py` | Figures |
| `audit/run_double_inversion_diagnostic.py` | Orchestrator |
