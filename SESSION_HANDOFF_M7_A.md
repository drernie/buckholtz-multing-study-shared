# SESSION HANDOFF — M7-A Eq31 Mass-Ratio Toy-Test

**Date:** 2026-06-11 · **Commit before M7-A:** 91ea667

## Claim tested
Eq. 31: (m_W)²:(m_Z)²:(m_H)² :: 7:9:17 (canonical source line 881)

## Masses used
PDG2022 / PDG2024-avg / CDF-II-2022-W (EXTERNAL_STANDARD_PHYSICS, hard-coded+cited)

## Numeric result
W-norm ratios (7, 9.0096, 16.9977); lsq mass-dev 0.005–0.05%;
Z-anchored pulls: H −0.44σ ✓; W −3.58σ (PDG22) / −3.84σ (PDG24) / +1.45σ (CDF22).
Author's "W within 1σ" reproducible only vs contested CDF-II value.

## Verdict
**PARTIAL** — approximate numerical relation; not exact; no derivation.

## Files created
scripts/m7_a_eq31_mass_ratio_toy_test.py · reports/m7_a_eq31_mass_ratio_toy_test.{md,json} ·
tests/test_m7_a_eq31_mass_ratio.py (4 tests) · SESSION_HANDOFF_M7_A.md

## Files updated
Vault MASTER (+M7-A pointer), M7 Starting Status (+result line)

## Tests run
pytest M7-A: 4 passed · M7-A+M2-G4: 8 passed · ruff clean

## Next recommended gate
M7-B 5:1 dark-isomer ratio audit

## Forbidden actions (respected)
No M7-B/C started; bridge not reopened; no MCMC; no LLM API; no web; no label/
historical changes; no public claims; no new deps; no `git add .`.

## Reproduction
python scripts/m7_a_eq31_mass_ratio_toy_test.py
python -m pytest tests/test_m7_a_eq31_mass_ratio.py -q
