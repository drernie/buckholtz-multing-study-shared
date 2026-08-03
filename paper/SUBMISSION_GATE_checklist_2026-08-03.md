# Submission Gate — pre-send checklist

**Package:** `letter_to_TJB_consolidated_audit_2026-08-03_EN.md` +
`onepager_for_TJB_2026-08-03_EN.md` + `reports/audit_summary_for_tjb.png`
**Gate:** `~/.claude/rules/integrity.md` § Submission Gate
**Status: 3 of 4 gate items closed. Cooling-off is NOT closed — see bottom.**

---

## 1. Adversarial review — CLOSED

Context-asymmetric skeptic run against letter + one-pager, given only the
documents and the source certificates, no session history. 6 findings
returned; each independently re-verified by this session before any edit
(not taken on the skeptic's word — `audit-verification-gate.md`):

| # | finding | this session's own verification | outcome |
|---|---|---|---|
| P1 | "naive" tone inconsistency | grep, both files | fixed |
| P2 | heading omits `C(z)` qualifier | grep, both files | fixed |
| P3 | 25.1% vs cert's 25.2% | recomputed 130.4/104.2−1 by hand | dismissed — sent value is correct, cert has internal rounding artifact recipient never sees |
| P4 | closing paragraph reads backhanded | re-read, agreed on independent judgment | fixed |
| P5 | "the later curve" referent ambiguity | grep | noted, not fixed (recipient sent the file himself) |
| P6 | sign-crossing description | recomputed the actual sign sequence | dismissed — letter's z=0.4 boundary claim is accurate |

A second human review round then caught a methodology issue the skeptic
missed (χ²/AIC parameter-count asymmetry) — verified and found to be
**worse** than flagged (sign reverses under AIC/BIC); the directional claim
was withdrawn entirely rather than patched. See item 9 below.

## 2. Explicit verification checklist — CLOSED (12 items, ≥9 required)

| # | claim | source | how verified |
|---|---|---|---|
| 1 | `U(r,z) = -A2/r + A3/2r² - A4/3r³ + C(z)` follows from `F(r,z)` | direct calculus | `[VERIFIED]` — one-line derivative, reproducible by inspection |
| 2 | `U∝r⁻ⁿ` under standard pair-fluid mapping gives `w=n/3` | `CERT_C2_C3.md` | `[VERIFIED-CERT]` — symbolic + 360 configs to 7×10⁻¹⁶ |
| 3 | Table A1: β_d, β_q chosen by fit to H-data; H0-anchored at z=0 | `CERT_C5A_supplementary.md` | `[VERIFIED-CERT]` — independent reader, corroborated by C1 |
| 4 | Preprint contains 0 figures | `CERT_C5B/C5C` | `[VERIFIED-GREP]` — `grep -c -i figure` = 0 on both preprint and supplementary |
| 5 | Orange curve vs Table A1: up to 44%, rms 21% | `CERT_C5B_figure3.md` | `[VERIFIED-EXTRACTION]` — re-run this session, `plot_audit_summary_for_tjb.py` output matches to the digit |
| 6 | Positive control: blue curve → flat ΛCDM, `H0=67.37`, `Ωm=0.3152`, rms 0.002% | script output | `[VERIFIED]` — recomputed twice this session, both runs agree |
| 7 | `z=1.965` is the source figure's own marked CC-calibration boundary | `CERT_C5C_orange_curve_provenance.md` | `[VERIFIED-EXTRACTION]` — legend text extracted directly from the PDF |
| 8 | `ℓ_q ≥ ℓ_d/2` is exact for attractive-everywhere | algebra | `[VERIFIED]` — discriminant of the force-law's bracket, checked by hand |
| 9 | MCXC screening: ≤4.25% of 4051 pairs in repulsive window at `ℓ_d=8` Mpc | `FINDING_cluster_pair_sign_constraint.md` | `[VERIFIED]` — computed this session against 1742 real clusters, projected separation |
| 10 | CC χ²: curve 14.4 vs ΛCDM 12.8; AIC/BIC reverses the sign | this session's computation | `[VERIFIED]` — raw chi2 + AIC + BIC all computed and cross-checked by hand |
| 11 | Signature carries ORCID + Ronin Institute | direct file read | `[VERIFIED]` — confirmed present, `tail` of the actual sent file |
| 12 | "not necessarily trustworthy or directly useful" is a verbatim quote | `CERT_C1_provenance.md` | `[VERIFIED-SOURCE]` — matched against the preprint's own text layer |

No claim in the sent package rests on the parked `HANDOFF_multing_plus_next_session.md` content — checked explicitly (`git grep` for its unique numbers found no matches in letter/onepager/figure).

## 3. Text ↔ figure consistency — CLOSED

Cross-checked letter, one-pager, and figure against each other line by
line this session: control residual, rms, the four annotated percentages
(+11/+25/+36/+44%), the calibration-boundary note, and all terminology
(curve naming, Table A1 phrasing) agree across all three documents. One
inconsistency found and fixed (one-pager had drifted from the letter's 6
precision corrections after a mid-session edit) — see git log
`bc14280`..`1c5beaa`.

## 4. Cooling-off — **NOT CLOSED**

> *"The moment right after declaring 'READY' is the least reliable moment
> to judge readiness; re-check after a pause, not in the same breath as
> finishing."* — `integrity.md`

This item cannot be satisfied by the assistant — it requires real elapsed
time and a human re-read with fresh eyes, not another same-session pass.
**Recommendation:** read the package once more tomorrow, or after a
different task, before sending. If you choose to send today anyway, that
is a deliberate override of this gate, not a technical blocker — the
content itself has passed 1–3.

---

**Verdict: content-ready. Time-gate open.** Nothing here should be read as
"do not send" — only as "the fastest-possible send skips a check this
project's own rules call mandatory, and the check costs one day, not
more work."
