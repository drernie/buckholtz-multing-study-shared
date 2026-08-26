# SESSION HANDOFF — M7-C Thermal History / N_eff Blocker

**Date:** 2026-06-12 · **Commit before M7-C:** 5f53a37

## Claim tested

Does IDM specify enough dark-sector thermal history to compute ΔN_eff and compare to BBN/CMB constraints?

## Result

**BLOCKED** — 6/7 required thermal ingredients NOT_FOUND in preprint.

| Ingredient | Status |
|---|---|
| I1: relativistic dark species at BBN | NOT_FOUND |
| I2: T_dark/T_visible | NOT_FOUND |
| I3: decoupling temperature | NOT_FOUND |
| I4: entropy-transfer history | NOT_FOUND |
| I5: dark particle existence | AUTHOR_HINTED (preprint line 1063-1065) |
| I6: coupling/thermalization assumptions | NOT_FOUND |
| I7: explicit ΔN_eff calculation | NOT_FOUND |

Only I5 is AUTHOR_HINTED: preprint implies dark particles mirror SM ("might associate with a set of elementary particles for which there is one counterpart for each known ordinary-matter elementary particle") but gives no masses, temperatures, or relict densities.

**ΔN_eff computable: NO.** Standard formula ΔN_eff = (4/7) × (g_D/2) × (T_dark/T_ν)^4 requires all of I1-I6. None are specified.

**This blocker is independent of SC-2 / bridge (A0).** Even if bridge + cluster params were resolved, N_eff test would still be blocked.

## Verdict

**BLOCKED** — thermal history absent from preprint. AUTHOR_DERIVATION_NEEDED.

## Files created

- `scripts/m7_c_thermal_history_neff_audit.py` — audit script, source scan, computability logic
- `reports/m7_c_thermal_history_neff_audit.md` — full M7-C report
- `reports/m7_c_thermal_history_neff_audit.json` — machine-readable audit output
- `tests/test_m7_c_thermal_history_neff.py` — 12 tests (all pass)
- `SESSION_HANDOFF_M7_C.md` — this file

## Files updated

- `docs/100_hd_mavp_autopsy_internal.md` — A5 row updated with M7-C result and pointer

## Tests

M7-C: 12 passed · M7-A: 4 passed · M2-G4: 5 passed · ruff clean

## Questions unlocked for TJB (secondary — after Q1-Q3)

- Q_TH1: Were the five dark isomers ever thermally populated?
- Q_TH2: T_dark/T_visible for each sector?
- Q_TH3: Decoupling temperature?
- Q_TH4: Which dark particles relativistic at BBN/recombination?
- Q_TH5: IDM ΔN_eff prediction vs Planck 2018?

## Next recommended gate

1. User review of `docs/104` (Q1-Q3 author email) → approve or edit → send
2. TJB response to Q1-Q3 → bridge + cluster params → F1/F2 gates
3. Thermal history questions (Q_TH1-5) → follow-up email after Q1-Q3 answered

## Forbidden actions (respected)

Author email not sent; bridge not reopened; no MCMC/LLM API/web; labels & history untouched; no public claims; no push; no `git add .`.

## Reproduction

```
python scripts/m7_c_thermal_history_neff_audit.py
python -m pytest tests/test_m7_c_thermal_history_neff.py -q
```
