# Technical memorandum — MULTING H(z) consolidated audit

**Date:** 2026-08-03 · **Status:** companion to the letter and one-pager sent
to Dr. Buckholtz; this document carries the derivations, full tables, and
reproduction commands the letter and one-pager deliberately omit.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive

**Scope.** Everything below is certified: C1–C5C plus the MCXC screening
(branch C). Nothing from the parked MULTING+ tournament thread (cascade
auxiliary-field EFT, `P(X)`+worldline multipoles, dipole-polarization,
NR-019, NR-020) appears here — that material has not passed the same gates
and is tracked separately in
`experiments/20260803-bridge/HANDOFF_multing_plus_next_session.md`.

---

## 1. The local force law and its potential

Published force law:

```
F(r,z) = -A2(z)/r^2 + A3(z)/r^3 - A4(z)/r^4
```

The radial part of the potential follows by direct integration, uniquely up
to the ordinary additive freedom:

```
U(r,z) = -A2(z)/r + A3(z)/(2r^2) - A4(z)/(3r^3) + C(z)
```

`C(z)` does not affect the local force (`-dU/dr` kills it) and is not
assumed to be a cosmological energy density without a covariant definition
of `T_mu_nu` — that assumption is exactly what Sections 2 and 6 test and
find insufficient in its simplest form.

**Status: mathematically defined; nothing in this memo refutes it.**

## 2. The standard pair-fluid bridge — closed within a stated scope

**Claim tested:** does the pair-interaction energy of a pure inverse-power
potential, mapped to an effective fluid via the standard configurational
(virial) route, produce a negative-pressure (dark-energy-like) component?

For `U_s(r) = C_s r^{-s}`, Euler's identity applied **pair by pair, before
any averaging**:

```
s * dU/ds = -s*U   =>   p = (s/3) rho   =>   w = s/3
```

So the three MULTING terms map to `w = 1/3, 2/3, 1` — all positive
pressure, none capable of driving acceleration.

**Verification.** Derived blind (analyst given only the definitions and the
potential form, not the answer or its sign). Confirmed symbolically and
numerically across 360 configurations to `7×10⁻¹⁶`. Certificate:
`experiments/20260803-bridge/audit/CERT_C2_C3.md`.

**Scope — read literally.** This closes:
- pure inverse-power potential (no cutoff modification)
- the *standard configurational pair-fluid* mapping specifically
- positive-density pair populations

This does **not** close:
- a covariant field-theoretic completion (an action whose stress-energy
  sources the FLRW background directly)
- a polarisation/vector-tensor sector
- Buchert-type backreaction or other explicit non-perturbative averaging
  rules
- nonlocal actions

Registered as a negative result: `null_results/20260803-nr018-pair-potential-effective-fluid.md`.

### 2.1 The amplitude question (C4) — our implementation failed, the claim's direction did not

A separate, harder question — even granting the *sign* problem in §2 could
somehow be evaded, does the pair-interaction energy of a realistic cluster
population reach cosmologically relevant density at all — was tested twice,
independently (Path A: this project; Path B: independent reconstruction).

```
Path A dipole at ell_d = 8 Mpc :  3.9e-05  of rho_crit
Path B dipole at ell_d = 8 Mpc : ~3e-08    of rho_crit
difference: 3.11 orders of magnitude
```

Frozen criterion (>2 orders = FAIL): **C4 FAILS.** Root cause: Path A's
`n=1e-4 Mpc⁻³, M=1e15 M☉` gives `rho_eff/rho_m = 2.52` — 252% of all matter
in the universe, not the "generous ceiling" it was described as. Path B's
proper mass-function weighting gives `Ω_pair ~ 10⁻⁷`, a defensible range of
`10⁻⁸`–`10⁻⁶` — **three orders further from relevance** than originally
claimed, strengthening rather than weakening the qualitative conclusion.
Certificate: `experiments/20260803-bridge/audit/CERT_C4_amplitude.md`.

**Conserved-budget lesson (kept for reproducibility, not asserted as
physics):** before any population integral, print `n<M>/rho_available`.
This one check would have caught the error immediately.

## 3. Table A1 is a data-conditioned AI construction, not a MULTING calculation

**Source text, verbatim** (`data/source_material/buckholtz_preprints202511.0598.v6_pymupdf-clean.md`, pp. 38–39):

> "Table A1 shows responses, to our prompt, by one online service that has
> bases in artificial intelligence."
>
> "the responses that Table A1 shows are not necessarily trustworthy or
> directly useful"
>
> "Regarding H-MULT, the online service reported choosing βd = 4.5 and
> βq = 18.0."

**Independent confirmation, computed before this caption was read:**
`H-w_eff` reproduces `H-data` to 0.29% rms (vs 7.91% for `H-FLRW`) — a fit
signature; `H-FLRW` fits no standard cosmology without `Ω_m` below the
baryon density; the transcription was checked field-by-field
(104 of 108 numeric fields matched our working copy; 4 corrected, see
`data/table_a1_source_verified.csv` header).

**Supplementary transcripts (`CERT_C5A_supplementary.md`).** Three AI
services were tried; each states its own methodology in its own recap
table:

| service | β_d | β_q | stated method |
|---|---|---|---|
| ChatGPT | 0.78 | 0.19 | "Best-fit value minimizing RMS deviation from H-data" |
| Claude | 4.5 | 18.0 | "Best-fit value (from page 21 optimization section)" |
| Gemini | 4.25 | 8.10 | "Determined value from fitting" |

Table A1 = the Claude row (`β_d=4.5, β_q=18.0` matches uniquely).
`h0_anchor = 73.0` (the observed value) stated explicitly in two of the
three recaps, giving `H_MULT(0) = H_obs(0)`, `σ_MULT=0` — normalisation,
not agreement. Spread across services: `β_d` 5.8×, `β_q` 94.7×.

**Verdict: `DATA_CONDITIONED_CONSTRUCTION`.** Not a forward prediction; a
fit to the observations it is then compared against. Certificates:
`CERT_C1_provenance.md`, `CERT_C5A_supplementary.md`.

## 4. The later H(z) curve is a separate, unpublished, unidentified artifact

**Identity.** `ARTIFACT_EMAIL_2026-08-02_MULTING_INTRO_V6`
(`multing_intro_figure_v6.pdf`), matplotlib 3.10.8, created
2026-07-30T18:09:58Z, received by email 2026-08-02. Predecessor found:
`image002.png` (2026-07-20 message) — same 31 CC points, same DESI z=2.33,
same SH0ES anchor, caption "MULTING (anchored to SH0ES)".

**The preprint contains no figures at all.** `grep -c -i "figure"` = 0 on
both the preprint and the supplementary text. The object this project spent
weeks calling "Figure 3" does not exist in the published material — it was
this email attachment throughout. Certificate: `CERT_C5B_figure3.md`.

**Positive control on the digitiser, before any comparison.** The figure's
blue reference curve, fit to flat ΛCDM:

```
H0 = 67.37, Omega_m = 0.3152, rms = 0.002%
```

Planck 2018 recovered to two parts in 100,000 — the extraction pipeline is
trustworthy independent of what it finds on the unknown curve.

**Result: the curve does not render Table A1.**

| z | curve | Table A1 `H_MULT` | deviation |
|---|---|---|---|
| 0.00 | 73.9 | 73.0 | +1.2% |
| 0.06 | 72.6 | 70.2 | +3.4% |
| 0.14 | 72.6 | 73.5 | −1.2% |
| 0.25 | 75.4 | 78.8 | −4.3% |
| 0.40 | 83.0 | 83.1 | −0.1% |
| 0.65 | 101.2 | 91.4 | +10.7% |
| 1.00 | 130.4 | 104.2 | +25.1% |
| 1.50 | 172.1 | 126.5 | +36.1% |
| 2.10 | 218.6 | 151.8 | +44.0% |

rms 21.1%. Below `z=0.4` the two agree to a few percent and change sign
once; above it the divergence is one-sided and monotone. Nor is the curve
ΛCDM re-anchored: `MULTING/ΛCDM` ratio spans 0.980–1.088 across the range
(10.3% spread, crosses unity).

**The `z=1.965` boundary.** The figure's own legend marks four regimes of
one curve: dotted (future, `z<0`), solid (data-grounded, `0≤z≤1.07`),
dashed ("CC-calibrated only"), dotted ("beyond calibration") — the last
transition sits at `z=1.965`. The `44%` divergence at `z≈2.1` is **past**
that boundary; **within** it, the largest divergence is `36%` at `z=1.5`. A
curvature scan finds no kink at either `z=1.07` or `z=1.965` (ratio to
median curvature 0.4× and 1.1× respectively) — the four-regime split is
stylistic, one smooth curve underlies it.

**Generator-family tests — none fit.**

| family | free params | rms |
|---|---|---|
| flat ΛCDM | 2 | 3.99% |
| flat wCDM | 3 | 3.72% |
| ΛCDM + curvature | 3 | 3.42% |
| CPL `w0-wa` | 4 | 3.55% |
| `w=-1+A tanh((z-zt)/Δ)` | 5 | degenerate (`Ωm=-173`) |

Control, same fit applied to the *known* blue curve: 0.0019%. A 2000-fold
asymmetry — the orange curve genuinely resists every FLRW-fluid family
tried, which is consistent with (not evidence against) a real modified
gravitational response.

**Verdict: `UNPUBLISHED_NON_IDENTIFIABLE_ARTIFACT`.** Excluded: hand-drawn,
rendering of Table A1, rescaled ΛCDM, every FLRW fluid family tried.
Certificate: `CERT_C5C_orange_curve_provenance.md`.

## 5. MCXC geometric screening — the repulsive-window structural relation

The force law's bracket changes sign:

```
F(r) ∝ -(1/r^2)[1 - ell_d/r + ell_q^2/r^2]
```

Repulsion occurs for `s_- < s < s_+`, `s_± = (ell_d ± sqrt(ell_d²−4ell_q²))/2`,
which exists **only if `ell_d > 2 ell_q`**. Equivalently:

```
ell_q >= ell_d / 2   =>   attractive at every separation
```

**Test against real data.** 1742 MCXC clusters, projected (transverse)
separation `r_p` — immune to peculiar-velocity/Fingers-of-God contamination
that corrupted a first 3D-separation attempt (withdrawn). Since true 3D
separation `s ≥ r_p` always, counting `r_p < s_+` gives a **strict upper
bound** on repelled pairs, no selection-function modelling required.

| `ℓ_d` [Mpc] | `ℓ_q` [Mpc] | upper bound on repelled pairs | median dispersal |
|---|---|---|---|
| 4 | 0 | 0.81% | 15.4 Gyr |
| 8 (kSZ bound) | 0 | 4.25% | 20.3 Gyr |
| 8 | 4 | 0% (no repulsive regime) | — |
| 16 | 0 | 11.77% | 44.8 Gyr |

**Verdict: `GEOMETRIC SCREENING ONLY`, not a likelihood constraint.** At
most 4.25% of pairs sit in the repulsive window at the kSZ bound, and their
dispersal time (~20 Gyr) exceeds the age of the universe — no overt
contradiction, but this is not a statistical fit and should never be
described as one. Certificate:
`experiments/20260803-bridge/FINDING_cluster_pair_sign_constraint.md`.

## 6. Observational status of the later curve on real CC data — not a certified comparison

Evaluated at the 27-point Moresco et al. (2022) cosmic-chronometer
compilation (`data/hz_cc.csv`):

```
chi2(curve, 0 free params)          = 14.40
chi2(flat LCDM, 2 free params,
     H0=68.77, Om=0.317)            = 12.81
raw delta_chi2                      = +1.59   (naive read: favors LCDM)

AIC(curve)  = 14.40      AIC(LCDM) = 16.81     delta_AIC = -2.41 (favors curve)
BIC(curve)  = 14.40      BIC(LCDM) = 19.40     delta_BIC = -5.00 (favors curve, more)
```

**The sign is not stable across conventions**, and neither reading should
be asserted: `AIC`/`BIC` assign the curve zero effective parameters, but
its generative operator is unidentified (§4) — its true degrees of freedom
are unknown, not zero by default. Assigning `k=0` to compute "AIC favours
the curve" would repeat the same class of error as the naive "χ² favours
ΛCDM" reading, in the opposite direction.

Leave-one-out (27 single-point removals, our own dataset/curve): 0 sign
flips. This is **not** presented as refuting any other party's LOO claim —
different curve extraction, different dataset (this project's 27-point
Moresco compilation, not the 31 points drawn on the source figure itself),
different method. It stands only on its own terms.

**Verdict: curve-level distinct; no observational preference established
either way until a protocol fixes what is being compared on both sides.**

## 7. Registered negative results

| ID | claim tested | verdict |
|---|---|---|
| NR-018 | positive-density pair-fluid mapping of pure inverse-power potential produces dark energy | REJECT — `w=n/3`, structural, scope-limited to §2 |
| C4 | pair-interaction energy density reaches `Ω~10⁻⁴` | FAIL as implemented; direction survives at `~10⁻⁷` |

## 8. Reproduction

```bash
# Section 2 — pair-fluid w=n/3
# (symbolic derivation, no script; see CERT_C2_C3.md for the analyst transcript)

# Section 4 — digitiser + positive control + Table A1 divergence
python scripts/a1_digitize_tjb_figure.py
python scripts/plot_audit_summary_for_tjb.py

# Section 5 — MCXC geometric screening
# derivation inline in FINDING_cluster_pair_sign_constraint.md; data/mcxc.csv,
# flat LCDM H0=67.36 Om=0.3153, halo exclusion 1.9*(R500_i+R500_j)

# Section 6 — CC chi2/AIC/BIC
# real data: data/hz_cc.csv (27 pts, Moresco et al. 2022)
# curve: orange-curve extraction from scripts/a1_digitize_tjb_figure.py
```

## 9. Explicitly out of scope

The following exist only as a parked, unverified handoff and must not be
cited alongside the material above without first passing the same gates:
cascade auxiliary-field EFT, shift-symmetric `P(X)`+worldline multipoles,
the dipole-polarization thawing model, `NR-019`, `NR-020`, the decorrelation
rescue hypothesis, and the disputed `fσ8` growth claim. See
`experiments/20260803-bridge/HANDOFF_multing_plus_next_session.md` for the
full content and its own stated caveats.
