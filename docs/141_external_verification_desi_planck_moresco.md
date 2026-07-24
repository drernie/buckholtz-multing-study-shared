# docs/141 — External Verification Pass: DESI/Planck/Moresco + correction of "retracted" framing

**Date:** 2026-07-24
**Origin:** user pasted an external synthesis document (26-item P0/P1/P2 status writeup, not
authored by us) proposing several new, specific claims about TJB's v25 paper, with 4 supporting
arXiv links, and asked to (a) fix a factual error in that document's description of our own
docs/140 finding, and (b) verify the 4 links. This doc records both.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · NO_AUTHOR_ERROR · OUR_RECONSTRUCTION

---

## 1. Correction: "первая независимая кривая — отозвана из-за нашего бага"

**This line does not appear in anything we authored.** Grepped `docs/140` and `activeContext.md`
— neither uses the word "отозвана"/"retracted" about the clean-room H(z) finding. The line
originates in the external pasted document, not in our own files.

**What actually happened, per docs/140 §3.2–3.3 (unchanged, already correct):** `Agent(reviewer)`
found a real P1 bug (H(z) pinned to the constant H0,anchor instead of solved self-consistently).
We fixed it and **re-ran** — the non-monotonic shape (peak≈152 km/s/Mpc at z≈0.7, falling to ≈68
by z=2.5) came back **unchanged**. docs/140 states this explicitly: *"confirms the earlier
shape-mismatch finding was NOT an artifact of the bug, strengthening rather than undermining
docs/140 §3.3's conclusion."* The finding was **re-confirmed on corrected code**, not retracted.

If the external document (or any future derivative of it) is used again, that line needs to read
"re-confirmed after fixing a reviewer-caught bug" — not "retracted."

---

## 2. WebFetch verification of the 4 cited sources (2026-07-24, all fetched directly, not from memory)

| # | URL | Claim being checked | Result |
|---|---|---|---|
| 1 | arxiv.org/abs/2404.03001 | Is this DESI DR1 or DR2? What H(z=2.33) does it report? | **DR1** ("first year of observations," 2024 series). Abstract states verbatim: **"H(z_eff) = (239.2 ± 4.8)(147.09 Mpc/r_d) km/s/Mpc"** at z_eff=2.33 — exact match, to the decimal, of what TJB's paper cites and labels "DESI DR2." |
| 2 | arxiv.org/abs/2503.14739 | Is this the real DESI DR2? What does it report at z=2.33? | **Yes, DR2** ("DESI DR2 Results I: Baryon Acoustic Oscillations from the Lyman Alpha Forest," 2025). Abstract: **D_H(z_eff)/r_d = 8.632 ± 0.098 (stat) ± 0.026 (sys)** — a different native quantity, converting to H(2.33)≈236.1±2.8 at standard r_d, not 239.2±4.8. |
| 3 | arxiv.org/abs/1807.06209 | Planck 2018 flat-ΛCDM H0 and Ωm | Confirmed: **H0=67.4±0.5 km/s/Mpc, Ωm=0.315±0.007** (final full-mission, TT,TE,EE+lowE+lensing). Matches docs/137 item 2's already-independently-computed correction exactly. |
| 4 | arxiv.org/abs/2003.07362 | Does SPS choice dominate the CC H(z) error budget? | Confirmed: abstract states **"the choice of the stellar population synthesis model dominates the total error budget on H(z), with contributions at a level of ~4.5%"** (range 2.3%–5.4% depending on z, with modern stellar libraries). Supports docs/137 item 5's covariance question with a concrete number: a 4.5%-level systematic dwarfs the reported Δχ²=0.935 gap between MULTING and ΛCDM on the 31-point CC fit — worth stating explicitly when that item is eventually raised. |

**Headline result: finding #1 is new and upgrades docs/137 item 3** from "ambiguous r_d
convention" to a precise, source-located mismatch — see the updated docs/137 §3 for the
TJB-facing wording. Findings #3 and #4 are independent confirmations of numbers we had already
derived ourselves (docs/137 items 2 and 5) — good convergent validation, not new information.

---

## 3. What this does NOT establish

- Does not imply the DR1-vs-DR2 label is anything other than an honest citation/release slip —
  explicitly NOT presented as evidence of carelessness in the paper's actual physics or fitting.
- Does not by itself change whether MULTING's DESI-extrapolation failure (Table VI, −4.55σ to
  −5.03σ) gets better or worse under the corrected DR2 number — that requires re-running the
  σ calculation with 236.1±2.8 in place of 239.2±4.8, not done here (cheap follow-up, not yet
  executed).
- Does not resolve the much larger external synthesis document's other 25 items, most of which
  either (a) duplicate findings we already have in docs/133-140 (parameter degeneracy, r_X
  circularity, T0 tension, AIC/BIC caution — all independently convergent, good signal) or (b) are
  reasonable physics questions with no fact to "verify" (equivalence-principle risk, local-to-
  global bridge gap) — those were addressed narratively in the chat response, not reproduced here.
