# FINDING P219 — DESI-DR1 Cosmic Chronometers out-of-sample check on v82's
# frozen fit: the FULL test is BLOCKED (data not yet public); the BOUNDED
# n=3 check that IS possible finds neither MULTING nor ΛCDM distinguished

**Date:** 2026-09-07
**Labels:** `NOT_VALIDATION` · `NOT_REFUTATION` · `OUR_RECONSTRUCTION` ·
`NO_AUTHOR_ERROR` · L0 `descriptive`
**Artifact:** `P219_desi_dr1_cc_oos_bounded_check.py`
**Answers:** `docs/158` item 2 (Pareto plan, 2026-09-07)

---

## 1. The full test is blocked, and it is worth saying precisely why

`docs/158` specified: freeze `(β₁,β₂,H₀)` at v82's Table II values, score
against DESI-DR1 CC's own 45-point `H(z)` array (`z=0.36..0.80`, step
`0.01`) with their full covariance `C_H = C_stat + C_sys`, no refit.

That data does not exist publicly yet. `WebFetch` on the arXiv abstract
page (`arxiv.org/abs/2608.13178`, 2026-09-07) returned, quoted:

> *"Supplementary material will be provided in the journal version of the
> article, **currently under correction**."*

Per `falsification-ladder.md` Step 2a (Substrate Gate): this is
`BLOCKED-INFRASTRUCTURE`. It is not evidence for or against anything, and
approximating the missing covariance with a guessed correlation structure
would be exactly the kind of fabricated-precision move this project's own
rules forbid.

## 2. What is available, and what was done with it

The paper's own text (fetched via `mcp__arxiv__download_paper` +
`search_paper_text`) states three real numbers, verbatim:

- Central cosmographic value at the pivotal redshift `z₀≈0.57`:
  `H = 95.1 (+10.9/−6.0 stat) ± 11.3 (syst) km/s/Mpc`.
- Two **explicitly independent** local finite-difference points (the
  paper's own words: *"two additional local and **uncorrelated**
  measurements… should not be interpreted as two continuations in
  redshift… but rather as **two separate estimations**"*):
  `H(z≈0.55) = 104.5 (+13.2/−7.6 stat) ± 22.4 (syst)`,
  `H(z≈0.61) = 88.5 (+6.7/−12.6 stat) ± 8.1 (syst)`.

`P219` freezes MULTING at v82's own reported `"unconstrained_spotlighted"`
Table II row — `H0_anchor=73.22`, `β₁=1.4335e10`, `β₂=7.8067e17` — no
refit, and flat ΛCDM at Planck values (`H0=67.4`, `Ωm=0.315`), also no
refit. **PC1**, reproducing v82's own reported `χ²₃₃=15.75` at this frozen
point: `computed 15.75` — exact match, `PASS`.

## 3. Result

| DESI point | `z` | `H_DESI ± σ` | `H_MULTING` | `z_MULTING` | `H_ΛCDM` | `z_ΛCDM` |
|---|---:|---:|---:|---:|---:|---:|
| central MAP | 0.57 | 95.1 ± 14.1 | 94.9 | −0.01 | 93.0 | −0.15 |
| independent, super-massive | 0.55 | 104.5 ± 24.7 | 93.4 | −0.45 | 91.9 | −0.51 |
| independent, reddest/purest | 0.61 | 88.5 ± 12.6 | 98.0 | +0.75 | 95.3 | +0.54 |

`σ` is stat (symmetrized from the paper's own asymmetric interval — an
approximation, noted) added in quadrature with syst.

## 4. The honest verdict

**Both models are consistent with all three DESI points at well under 1σ.**
More importantly: **the difference between MULTING's and ΛCDM's own
predictions (2–3 km/s/Mpc at each point) is small compared to DESI's own
uncertainty (12–25 km/s/Mpc).** At this precision, the two models are not
distinguishable from each other, let alone individually confirmed or
excluded by DESI. This n=3 bounded check has essentially **no
discriminating power** — it is a sanity check (nothing catastrophically
wrong), not a test.

**This is exactly why `docs/158` specified the full covariance array**: only
the 45-point array's tighter, correlated constraints could plausibly
separate the two curves. That test remains blocked.

## 5. What this does and does not establish

**Establishes:** MULTING's frozen fit does not fail an elementary sanity
check against real, independent, out-of-sample `H(z)` data. Table II's own
positive control reproduces exactly.

**Does not establish:** any preference between MULTING and ΛCDM, or that
MULTING has been "tested" against DESI in any decisive sense. The
discriminating test is blocked, not passed.

## 6. Labels, precisely (per `docs/158`'s own instruction)

- **Out-of-sample:** yes — v82's own fit's "DESI point" is a DR2 Lyman-α BAO
  measurement at `z=2.33` (`FINDING_P218` context), not a chronometer.
- **NOT independent:** the 31 already-fitted CC points span `0<z<1.97`,
  overlapping `0.55-0.61`, and share the CC method's stellar-population-
  synthesis systematics.
- **NOT post-freeze:** `data/source_material/README.md`'s provenance table
  — archive updated 2026-08-11, this DESI paper posted 2026-08-13, a 2-day
  margin only.

## 7. Next step, not done here

Re-run this test with the full covariance array once the journal
supplementary material is public. Until then, `docs/158`'s item 2 stays
open at this bounded result.

## 8. Caveats

1. Asymmetric statistical errors were symmetrized by averaging — a stated
   approximation, not the paper's own convention.
2. `H_LCDM` uses Planck values only, not a fit to the 33-point set alongside
   MULTING — matches `docs/158`'s "alongside ΛCDM at Planck values."
3. No Step 8a pass on this finding.
