# Artifacts — H1e (AGN feedback confound)

## cccp_coolcore_partial.csv

**Provenance:** cluster names, z, and cool-core/high-entropy classification for the
CCCP sample (Mahdavi et al. 2013, arXiv:1210.3689), obtained via `WebFetch` on
`ar5iv.labs.arxiv.org/html/1210.3689` with a summarization prompt targeting Table 1/2.

**Evidence level: `[INFERRED-WEBFETCH]`, not `[VERIFIED-REAL]`.** This is an
AI-summarized extraction of the source table, not a direct read of the raw table by
this session. Per this project's audit-verification-gate.md ("agent's [VERIFIED] =
your [INFERRED]"), the same discipline applies to WebFetch's own summarization layer.
**Before this data is used in any computed correlation, it must be cross-checked
against the primary table directly** (e.g. fetching the raw HTML/PDF table rows, not
a prose summary of them).

**Known gaps:**
- 49 rows extracted here vs. N=50 in the paper's own stated sample size — one cluster
  is missing from this extraction and needs to be identified and added.
- Only name/z/dynamical-state flag present. M_WL, M_HE, M_gas, T_x, wX (needed to
  reproduce H1a/c/d's delta_M and E_ICM, and required for the actual H1e partial
  correlation test) are NOT yet in this file — Phase 1 of claim.md's two-phase plan.

**Status:** partial, Phase 1 groundwork only. Not sufficient on its own to run any
part of the H1e test.
