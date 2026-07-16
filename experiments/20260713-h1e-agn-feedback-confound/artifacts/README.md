# Artifacts — H1e (AGN feedback confound)

## cccp_mahdavi2013_merged.csv — Phase 1 deliverable, SUPERSEDES cccp_coolcore_partial.csv

**Provenance:** Tables 1 and 2 of Mahdavi et al. 2013 (arXiv:1210.3689), extracted
programmatically with `pdfplumber` directly from the downloaded PDF
(`arxiv.org/pdf/1210.3689`, ~1MB, downloaded with explicit user permission
2026-07-13), not summarized by an AI intermediary.

**Evidence level: `[VERIFIED-DIRECT-READ]`.** Row count confirmed 50/50 for both
tables with zero name mismatches on join. Individual values cross-checked against
the rendered page images (Read tool page view) for the first several rows — exact
match. Internal sanity check: median(M_hydro/M_WL)=0.854 and ratio-of-sums=0.881
both bracket the paper's own stated "~10% average underestimate" (the naive
arithmetic mean, 0.967, is pulled up by a few low-S/N outlier clusters with large
M_WL uncertainty, e.g. MS1231.3+1542 at M_WL=0.6±0.4 -- confirmed a real reported
value, not a parsing artifact, by checking against the raw extracted text).

**Columns:** cluster_name, z, L_X (1e45 erg/s), T_X (keV) [Table 1]; r500_WL (Mpc),
M_WL, M_Gas, M_hydro (all 1e14 Msun), K0 (keV cm^2, central entropy -- the
cool-core/AGN-feedback proxy H1e needs), D_BCG (kpc), wX (already used in H1c),
P3/P0 [Table 2]; plus derived `delta_M_1e14Msun` = M_WL - M_hydro and
`E_ICM_proxy_MgasTx` = M_Gas * T_X, matching H1a/c/d's own definitions
(`experiments/20260701-h1c-morphology-mass-bias/estimand.md`).

**Why K0 (central entropy) instead of a separate radio/X-ray-cavity catalog:** K0 is
already a standard, quantitative, continuous AGN-feedback proxy in the literature
(low K0 = cool-core = strong central AGN feedback regulating the cooling flow; high
K0 = non-cool-core = weak/absent regulation -- McNamara & Nulsen review; this exact
K0 threshold is what the paper itself uses to define cool-core vs non-cool-core in
its Fig. 3). It sits in the same table as M_WL/M_Gas/M_hydro, so no external catalog
fetch was needed -- this closes Phase 2's "stretch goal" from claim.md at no extra
cost.

**Reproducibility:** `table1_raw.txt` / `table2_raw.txt` are the raw pdfplumber text
extractions (committed so the CSV is regenerable without re-downloading the PDF);
`parse_mahdavi2013.py` parses them into the merged CSV. Re-run: `python
parse_mahdavi2013.py` from this directory.

**Known gap carried over from cccp_coolcore_partial.csv:** that file's binary
cool-core/high-entropy flag (49/50 rows, WebFetch-summarized) is superseded by K0
here and should not be used for anything further -- kept only for audit trail of
what changed between the two extraction attempts.

**Status:** Phase 1 complete. Ready for Phase 2 (join the pre-registered H1e
criterion from claim.md against `E_ICM_proxy_MgasTx`, `delta_M_1e14Msun`, `M_WL`,
and `K0_keVcm2` -- partial correlation not yet computed).
