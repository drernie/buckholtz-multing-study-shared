# SESSION HANDOFF — M2-G4 Fisher Rank Identifiability

**Date:** 2026-06-11
**Commit before M2-G4:** efb10b1 (HEAD at start; working tree already dirty from a
parallel audit session — those files classified and left untouched/unstaged)

## Files created
- `scripts/m2_g4_fisher_rank_identifiability.py` — Jacobian/SVD/Fisher analysis
- `reports/m2_g4_fisher_rank_identifiability.md` — full report
- `reports/m2_g4_fisher_rank_identifiability.json` — machine-readable results
- `tests/test_m2_g4_identifiability.py` — 4 characterization tests
- `SESSION_HANDOFF_M2_G4.md` — this file

## Files updated
- Vault: `MASTER Source & Findings` (+ M2-G4 pointer), `M7 Starting Status` (+1 line)

## Model analyzed
Claude-specific Φ-normalization bridge (OUR_RECONSTRUCTION, NOT_AUTHOR_CONFIRMED):
`H²(z) = H²_anchor · Φ(z)/Φ(z_anchor)`, `Φ = A_m − A_d + A_q`.
Reused `src/bridge_phi.py` + `src/cluster_schedule.py` (pre-existing, parallel session).

## Parameter scenarios & rank results (σ-weighted)
| Scen | θ | rank num | rank practical | cond | verdict |
|---|---|---|---|---|---|
| A | β_d, β_q | 2 | 2 (meaningless: sens 7e-10/7e-7) | 4.7e3 | FAIL practical |
| B | + H_anchor | 3 | **1** | 2.0e12 | FAIL (anchor only) |
| C | + α_D | 4 | **2** | 7.6e11 | PARTIAL (α_D + anchor live; β dead) |
| D | + 12 free D_i | — | — | — | FAIL_BY_COUNTING (14>12) |

Key numbers: β_d max rel-sensitivity 7e-10; β_q 7e-7; α_D 4.5; H_anchor 1.0.
β_q|α_D cosine 0.861. Reconstruction at Claude's β: RMS 14.1σ vs reported H_MULT
(bridge text ≠ emitted numbers, consistent with (1+z)^0.79 finding).

## Verdict
**PASS** (gate executed) — central finding: **β-pair practically NON-IDENTIFIABLE**
under the reconstructed bridge; schedule layer (α_D, H_anchor) carries all power;
flexible schedule structurally non-identifiable. Claude's "fitted" β could not have
been constrained by the stated fit (objective flat to ~1e-7).

## Tests run
- `pytest tests/test_m2_g4_identifiability.py` → 4 passed
- Full suite → **567 passed, 12 skipped, 0 failed**; ruff clean (new files)

## Remaining blockers
- Author-confirmed bridge + cluster schedules (unchanged; needed to unlock β)

## Next recommended gate
**M7-A Eq31 mass-ratio toy-test**

## Forbidden actions (respected)
No MCMC; no LLM API; no web; no historical-data edits; no label changes; no M7;
no public claims; no new dependencies; no `git add .`; no package-mode `python -m`
for project scripts (pytest/ruff module invocation is the repo's standard).

## Reproduction
```
python scripts/m2_g4_fisher_rank_identifiability.py
python -m pytest tests/test_m2_g4_identifiability.py -q
```
