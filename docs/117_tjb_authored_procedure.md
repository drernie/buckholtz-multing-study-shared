# docs/117 — TJB-Authored Procedure (Q1–Q3 source)

**Date received:** 2026-06-14 23:30 (email from [private email redacted])
**Context:** Sent after the Zoom call (2026-06-14). Author's own AI-prompt ("outtakes" material).
**Status:** AUTHOR_CONFIRMED — this supersedes our reconstructions of Q1/Q2/Q3 intent.

```
SAFETY LABELS (HARD):
  AUTHOR_MODEL · AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION
  INTERNAL_DIAGNOSTIC_ONLY · NO_PUBLIC_CLAIMS
  Procedure is the AUTHOR'S; any fit we run remains OUR_RECONSTRUCTION of the data step.
```

---

## 1. Why this document exists

For weeks the project's top blocker was **Q1**: there is no closed analytic bridge
F_oP → H(z) in the preprint — Appendix A.1 is an AI prompt. On 2026-06-14 TJB sent his
**actual procedure prompt** directly. This is the authoritative answer to Q1, Q2, Q3.
It is preserved here verbatim so it survives context loss and is version-controlled.

---

## 2. Author's procedure — VERBATIM

> **\*\* outtakes — for now**
>
> Trying to appropriately separate evidence (as in data) from authority (as in outputs from
> models and theories) can be important and can be difficult. (We note, as an aside, the notion
> that data usually associates with some aspects of authority.) If you have a choice between
> relying on data and relying on outputs from models or theories, try, as much as is practical,
> to emphasize using data.
>
> For each one of the following, provide URLs to (and titles or names for) papers and/or data
> sets via which a person can determine (for redshifts z ranging from zero to as large a z for
> which there is useful data) data ranges and distributions within the ranges.
>
> **Step 0 — Perspective and guidelines**
> Assume that the two-word term *galaxy cluster* includes notions of protoclusters and galaxy
> clusters. Assume that *galaxy cluster* does **not** include so-called galaxy groups that (like
> the Milky Way / Andromeda) involve just two or few galaxies. Assume that *galaxy cluster* does
> **not** include objects that have emerged from collisions of galaxy clusters.
>
> **Step 1 — Scope (regarding redshift) and basic data**
> For each of the following, determine (for z from zero to as large a z for which there is useful
> data) a maximal value of z for which there is useful data and useful information about
> distributions within the relevant ranges:
> - (A) masses {in units of solar mass} of galaxy clusters.
> - (B) ICM thermal energy divided by the square of the speed of light {in units of solar mass}
>   for galaxy clusters. {ICM = intracluster medium.}
> - (C) radii {in units of Mpc} of galaxy clusters.
> - (D) distances {in units of Mpc} between neighboring non-colliding galaxy clusters.
> - (E) values {km/s/Mpc} of the Hubble parameter H(z).
> - (F) values {km/s/Mpc}, as estimated by the FLRW metric, of the Hubble parameter H(z).
>
> Use the term **z_+** to denote a maximal z for which: there is useful data for all six of
> (A)–(F); and one can remove data about galaxy clusters about to collide or that previously
> collided. Estimate and report z_+. From here on, report results spanning (but not outside)
> the range 0 < z < z_+.
>
> Produce tables {as a function of z} for pairs (A,B), (C,D), (E,F). For (E,F), also give time
> {Gyr} after the Big Bang per row. If (F) assumes an H0, report H0, list data sources, and
> discuss reasoning for the H0 choice.
> - **H-data** ≡ the H(z) associated with (E).
> - **H-FLRW** ≡ the H(z) associated with (F).
>
> **Step 2 — Possible standardization regarding z_+**
> Continue to use the value of z_+ that you calculated.
>
> **Step 3 — Some formulas to use below**
> object_1 and object_2 are galaxy clusters. G = gravitational constant.
> Gravitational interaction: **F = F_2 − F_3_1 − F_3_2 + F_4**
> (F_2 = monopole attraction; F_3_1, F_3_2 = dipole repulsion; F_4 = quadrupole attraction;
> *distance* = distance between object_1 and object_2; beta_d, beta_q = positive dimensionless
> parameters to be estimated later.)
> - F_1 = G · mass_1 · mass_2 / distance²
> - F_3_1 = beta_d · G · mass_1 · ('ICM thermal energy'_2 / c²) · radius_2 / distance³
> - F_3_2 = beta_d · G · ('ICM thermal energy'_1 / c²) · mass_2 · radius_1 / distance³
> - F_4 = beta_q · G · ('ICM thermal energy'_1 / c²) · ('ICM thermal energy'_2 / c²) · radius_1 · radius_2 / distance⁴
> Solar systems and objects within them have no ICM → F_3_1 = F_3_2 = F_4 = 0 there.
>
> **Step 3 (sic) — Calculate H-MULT**
> Assume protoclusters/clusters can increase mass by accreting nearby stuff or change over time.
> Try to remove data about clusters about to collide / that previously collided.
> *To the extent you want to, please feel free to construct a phenomenological mapping from the
> force-law terms into an effective acceleration equation.*
> Over 0 < z < z_+, how well can you fit (using F) the function H-data? Constrain beta_d, beta_q
> ≥ 0. **Do NOT constrain beta_d·radius_1, beta_d·radius_2, or beta_q·radius_1·radius_2 based on
> any physical distances or lengths.** Choose positive beta_d, beta_q minimizing the standard
> deviations away from the nominal H-data values.
> - **H-MULT** ≡ the H(z) associated with your results. Report beta_d and beta_q.
>
> **Step 4 — Pearson correlation coefficient r**
> Give a range of r for each statement:
> - (a) "For z < z_+, H-data correlates with H-MULT." Identify biggest sources of scatter.
> - (b) "For z < z_+, H-data correlates with galaxy-cluster-pair separation velocities for
>   comoving Hubble-flow pairs." Identify biggest sources of scatter.
>
> **\*\* STOP HERE \*\***
>
> — Tom (Thomas J. Buckholtz, tjb@alumni.caltech.edu)

---

## 3. Mapping to our blockers — what this resolves

| Our blocker | Author's answer | New status |
|---|---|---|
| **Q1 / Row 11 / G1** — bridge F_oP→H(z) | *"construct a phenomenological mapping from the force-law terms into an effective acceleration equation"* | **ANSWERED** — phenomenological → effective acceleration; NOT a closed GR formula. Our M8-A finding confirmed by author. |
| **Q2 / Row 35 / G8** — T_i normalization | (B) *"ICM thermal energy / c² {in units of solar mass}"* | **ANSWERED** — T_i = E_ICM/c² in M_sun (Sergey's letter guess confirmed). |
| **β_d magnitude "7-order gap"** | *"Do NOT constrain beta_d·radius … by any physical distances or lengths"* | **RESOLVED** — beta·radius is a free fitted combination; beta and radius are degenerate. The "×10⁷ vs 4.5" was a misread of a deliberately-free parameter, NOT an error. |
| **Q3 / Row 36 / G9** — Newton vs GR route | *"effective acceleration equation"* | **ANSWERED** — kinematic/phenomenological, not GR stress-energy. (Our GR-route w=+2/3 result is off the author's path — do NOT present it as refutation.) |
| **z=5, z=8.5 leverage outliers** | z_+ = max z with useful (A)–(F) cluster data (realistically z≈1.5–2) | **OUT OF SCOPE by author** — work only 0 < z < z_+; high-z upticks excluded by construction. |
| **SC-6 / F5 Local Group** | Step 0: groups (MW/Andromeda) explicitly excluded; so are collision remnants | **OUT OF SCOPE by author** — Local Group is a group, not a cluster. |
| **Our correlation/LOO approach** | Step 4 asks for Pearson r on H-data vs H-MULT and vs separation velocities | **VINDICATED** — author institutionalizes the correlation method we used. |

---

## 4. What remains (now mechanical, was blocked)

1. **Step 1 — assemble real cluster data A–F** with cited URLs, in 0 < z < z_+ (real catalogs:
   CHEX-MATE, Planck PSZ2, Chandra/XMM mass-T; CC/BAO for H-data). NOT synthetic.
2. **Determine z_+** from where all six (A)–(F) have usable data + collision removal.
3. **Fit** beta_d, beta_q (≥0, beta·radius unconstrained) minimizing σ vs H-data → H-MULT.
4. **Step 4** — report Pearson r ranges + scatter sources.

Boundaries unchanged: the PROCEDURE is the author's; any number we produce is OUR_RECONSTRUCTION
of the data-assembly + fit step, labeled NOT_VALIDATION, NO_PUBLIC_CLAIMS. No new email to TJB
needed now — the next deliverable is data + fit, not correspondence.

---

## 5. Provenance

- Source: email TJB → Sergey, 2026-06-14 23:30, subject thread "script".
- Sergey's 36-row structured-reading table (RU+EN) + 3 questions (Row 11/35/36) + Prompt Hacker
  link sent 2026-06-15 12:25 (xlsx in `C:\Users\serge\Downloads\buckholtz_36_starting_reading_{RU,EN}_v2.xlsx`).
- Call occurred 2026-06-14 (multiple Zoom segments due to Basic time limit).

---

*AUTHOR_CONFIRMED · NOT_VALIDATION · NOT_REFUTATION · INTERNAL_DIAGNOSTIC_ONLY*
*docs/117 issued 2026-06-15 — supersedes Q1/Q2/Q3 OPEN status in docs/116*
