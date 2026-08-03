# Letter to Dr. Buckholtz — 2026-08-03 (FINAL, short, no attachments)

**Status: DRAFT. The user sends, not the assistant.**

## Product separation (the thing that went wrong earlier)

Two different products got merged into one line. They are now separate:

| artifact | purpose | status |
|---|---|---|
| `letter_to_TJB_consolidated_audit_2026-08-03_EN.md` | full consolidated audit | **HOLD until after the preprint** — he asked for exactly this |
| `technical_memorandum_MULTING_Hz_audit_2026-08-03.md` | derivations, full tables | HOLD, ours |
| `reports/audit_summary_for_tjb.*` | proof that the curve ≠ Table A1 | memorandum only; the *result* is reported in one sentence below, the figure is not sent |
| `reports/hz_with_errorbars_for_tjb.*` | error bars + minimum | **WITHHELD** — see provenance note |
| **this file** | brief reply to his 2026-08-03 email | **SEND** |
| MULTING+, P(X), LLM tournament | new theory | separate track entirely |

## Why the error-bar figure is withheld

Extracted his plotted CC markers and matched them against our 27-point
Moresco+2022 set: **26 of 32 matched** (|Δz|<0.02 and |ΔH|<4 km/s/Mpc). So ~6
of his points come from a source we do not hold. The qualitative point (the
bars are missing, and CC uncertainties are large) is robust, but quoting
"median σ = 17, max 62" as if it characterised *his* set would be an overclaim.
Withholding also respects his request not to be sent material now.

## Precision decisions, both tested rather than assumed

- **`z ≈ 0.10`, not `z = 0.098`.** The minimum is shallow: H stays within
  0.2 km/s/Mpc of it across z ∈ [0.062, 0.136]. Three significant figures are
  not justified by the digitisation.
- **`q(z)=0 at z≈0.378` omitted — but it is NOT unstable.** Tested under
  smoothing windows from 1 to 201 points: the crossing moves only 0.378 →
  0.382. The number is sound; it is left out for economy, because it is one
  more claim he would have to check, not because it fails. Available if wanted.

---

**Subject:** Re: current MULTING figure and Zenodo materials

Dear Dr. Buckholtz,

Thank you for the update. I would be honoured to be included in the
acknowledgements.

One feature of the current figure seems especially worth having in explicit
form: the orange curve has a shallow minimum near z ≈ 0.10, while the flat
ΛCDM curve is monotonic across the plotted interval. That is a difference in
the shape of the function rather than an offset between two similar curves,
and it appears to be the clearest difference in shape visible on the current
figure in the low-redshift region — which is where you said the interesting
behaviour lies.

One provenance note may also be useful before the Zenodo package is frozen.
The later orange curve and the H_MULT column of Table A1 do not agree
numerically, and appear to represent different versions or stages of the
construction. Their difference is small and changes sign below z ≈ 0.4, but
then grows to roughly 11% at z = 0.65, 25% at z = 1.0, and 36% at z = 1.5,
reaching about 44% at z = 2.1 — beyond the CC-calibration boundary your figure
marks. If both are included in the Zenodo materials, it may be worth labelling
that distinction explicitly, so a reader does not have to work it out.

I will hold the rest of what I have been working through until after the
preprint, as you suggested. No
response is needed at this stage.

With thanks and respect,

Sergey Boyko
ORCID 0009-0009-2178-5701
Ronin Institute
