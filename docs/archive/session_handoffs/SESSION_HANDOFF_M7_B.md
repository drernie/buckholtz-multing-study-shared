# SESSION HANDOFF — M7-B 5:1 Dark-Isomer Ratio Audit

**Date:** 2026-06-11 · **Commit before M7-B:** 3b128dd

## Claim tested
"5 dark isomers : 1 OM isomer explains (5+):1 dark:ordinary density" (lines 767-772, 980-981, 1340+)

## Numeric result
Integer 5.0 vs author-cited 5.4 / Planck 5.364±0.065 → gap −6.8%, pull −5.6σ.
Equal-density-per-isomer NOT derived; thermal history absent; Sec 4.5 "pluses" = 4 qualitative options. Neutron-mass sanity: +0.08% max, cannot close 7%.

## Verdict
**PARTIAL** — approximate post-hoc integer-counting match; AUTHOR_DERIVATION_NEEDED.

## Files created
scripts/m7_b_5to1_dark_isomer_ratio_audit.py · reports/m7_b_...{md,json} · tests/test_m7_b_5to1_dark_isomer_ratio.py (4) · SESSION_HANDOFF_M7_B.md

## Files updated
Vault MASTER (+pointer), M7 Starting Status (+result line)

## Tests
M7-B 4 passed · ruff clean · full suite passed pre-commit

## Next recommended gate
M7-C thermal history / N_eff blocker

## Forbidden actions (respected)
M7-C not started; bridge not reopened; no MCMC/LLM API/web; labels & history untouched; no public claims; no push; no `git add .`.

## Reproduction
python scripts/m7_b_5to1_dark_isomer_ratio_audit.py
python -m pytest tests/test_m7_b_5to1_dark_isomer_ratio.py -q
