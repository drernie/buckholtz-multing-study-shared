# arXiv Submission Checklist
# Status: READY — all checks passed 2026-06-27

## Paper state (master = 235c271)
- [x] LaTeX compiles: 10 pages, 499 KB PDF, 0 undefined citations after bibtex
- [x] All tests pass: 853 passed, 12 skipped, 0 failed
- [x] Ruff clean
- [x] Look-elsewhere audit complete (rank #1, p < 2e-5)
- [x] Koide null test in paper
- [x] F₄ Casimir citation (Bincer 1993) resolved in refs.bib

## arXiv Metadata

**Title:**
Systematic Assessment of the MULTING/IDM Gravitational Framework:
Confirmed Assets, Identified Gaps, and Independent Reconstructions

**Authors:**
Sergey Boyko
Ronin Institute for Independent Scholarship
ORCID: 0009-0009-2178-5701

**Primary category:** hep-ph
**Cross-list:** gr-qc

**MSC codes (optional):** 83F05, 81V25

**Comments field:**
10 pages, no figures, 1 table. Code: https://github.com/sergeeey/buckholtz-idm-multing-study

**Report-no:** (leave blank)

**Journal-ref:** (leave blank — not submitted to journal yet)

## Abstract (plain text for arXiv form)

We present a systematic 36-point assessment of the MULTING/IDM preprint
(Buckholtz 2026, preprints202511.0598.v6), which proposes a multipole-expansion
extension of Newtonian gravity (MULTING) and an isomer-based dark-matter
framework (IDM). Using PDG 2024 constants, Planck 2018 cosmological parameters,
and the MCXC/XMM galaxy cluster catalogs, we independently verify the mass
relations in Equations (31) and (32), quantify the statistical preference for
MULTING vs. ΛCDM in H(z) data, and derive formal constraints on the IDM isomer
count from the baryon density ratio ω_DM/ω_b.

We find: (1) the empirical boson-mass relation [7:9:17] holds to <0.05% in mass
units (the scale-free ratio m_W/m_H = sqrt(7/17) holds to 0.04%, though per-boson
the W deviates by 3.8σ and H by 1.1σ when Z-anchored); the fermion-gravity link
(Eq. 32) holds at 0.17σ — both empirical assets independent of MULTING/IDM
cosmology; (2) the fermion mass spectrum (Eqs. 21-24) reproduces the muon mass
to 0.47% and quark geometric means to <0.31% using PDG 2024 constants; (3) the
MULTING dipole term is rendered negligible at cluster scales for the tabulated
β_d = 4.5, requiring β_d ≳ 10^3.2 for a 1% observational signature — formally
quantified via Birge Ratio R_B = 15.9 (β_d) and R_B = 24.1 (β_q), both with
p < 10^{-4}; (4) equal-mass N=5 IDM isomers are excluded at 5.67σ by Planck 2018,
but five isomers with m̄ = 1.074 m_p are Planck-compatible; (5) the ΔN_eff > 100σ
claim applies to a thermalized mirror sector only; gravitational-only IDM gives
ΔN_eff ≲ 10^{-40}, trivially within Planck bounds; (6) the H_FLRW baseline used
in Table A1 is inconsistent with standard ΛCDM (Planck MAE = 120 km/s/Mpc).

These results neither validate nor refute MULTING/IDM, but map precisely which
components rest on verified foundations versus which require additional physics.

## Files to upload

Upload as a .tar.gz containing:
  paper/main.tex
  paper/refs.bib

No figures. Class file: revtex4-2 (available on arXiv).

## Upload steps

1. Go to https://arxiv.org/submit
2. Start new submission
3. Select: Physics > hep-ph (primary)
4. Add cross-list: gr-qc
5. Upload main.tex + refs.bib (no figures needed)
6. Paste abstract above into the abstract field
7. Set title and authors as above
8. Add comments: "10 pages, no figures, 1 table. Code: https://github.com/sergeeey/buckholtz-idm-multing-study"
9. Submit for moderation

## Constraints (MUST NOT violate)
- NOT_VALIDATION: abstract correctly says "neither validate nor refute"
- NOT_REFUTATION: confirmed — no refutation claim
- NO_PUBLIC_CLAIMS: paper text only, no social media post without approval
- NO_EMAIL_WITHOUT_APPROVAL: do NOT email TJB about submission without explicit OK
