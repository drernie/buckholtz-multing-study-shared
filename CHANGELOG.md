# Changelog

All notable changes to this project are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.3.0] — 2026-06-01 — Reference-grade hardening

Engineering + epistemic hardening pass. **No scientific claims changed**: all
`blocked` / `unclear` / `provisional` / `NOT_VALIDATION` markers are preserved,
H_MULT(z) remains blocked, and no outreach/publication is implied.

### Added
- `LICENSE` (MIT, Sergey Kuts).
- `.github/workflows/ci.yml` — CI on Python 3.11 / 3.12 / 3.13: ruff (blocking),
  mypy (advisory), pytest + coverage.
- `docs/WHAT_THIS_REPRODUCES.md` — scope clarification: the audit reproduces an
  AI-service-mediated computation, not Buckholtz physics.
- `tests/test_beta_registry_consistency.py` — cross-registry drift guard (4 invariants).
- `src/deep_bridge_diagnostic_fit.py::safe_h_of_z` — sqrt guard against negative H².
- Regression tests for the silent-NaN fix; source-attribution tests for beta candidates.
- `ai_service_source` field on `BetaDefinition`; coverage config in `pyproject`.

### Fixed
- **Silent NaN**: `fit_unconstrained` / `fit_sign_constrained` no longer feed NaN
  to the least-squares solver when H² < 0 (was 16 `invalid value encountered in
  sqrt` RuntimeWarnings, corrupting the LM/TRF Jacobian update).
- Removed 17 `__pycache__` files erroneously tracked in git.
- `warnings.warn` now passes `stacklevel=2` (ruff B028).
- Repo-wide ruff cleanup (72 fixes: import sort, f-strings, `X | None`, whitespace).

### Changed
- Beta candidates re-framed as **AI-service outputs** (Gemini / ChatGPT), not
  Buckholtz model versions; each now cross-references `beta_provenance.py` (the
  single source of truth). Replaces the tautological beta status test.
- `OUTREACH_TEMPLATE.md` marked **DEPRECATED** (stale beta values; superseded by
  the active correspondence log and `docs/93`).
- Docs truth-synced: test count 62 → 533, coverage TBD → 72%, status reflects
  active collaboration rather than cold "ready for outreach".
- `pyproject` version 0.1.0 → 0.3.0; author set.

### Verified
- 533 tests pass, 12 skipped, 0 failures · coverage 72% · ruff clean.

## [0.2.0] — 2026-05-29 — Appendix A1 forensic extraction
- Word-level forensic extraction of Appendix A1 Steps 3–7.
- Documented that the H_MULT(z) computational formula is missing (bridge under-specified).
- Confirmed β_d=4.5, β_q=18.0 as fitted (Table A1 caption), not derived.

## [0.1.0] — 2026-05-27 — MVP
- Initial epistemic audit scaffold: registry, numerology penalty, assumption graph,
  data-anchoring leakage guard, Eq.15 arithmetic reproduction, rosetta stone.
