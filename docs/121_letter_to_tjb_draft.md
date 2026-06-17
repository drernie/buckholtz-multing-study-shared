# docs/121 — Letter to TJB (SENT 2026-06-17, single question)
# Status: SENT · single-question version · supersedes the 3-question draft
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

This is the version actually sent. The earlier 3-question draft ("Dear Thomas",
6.8σ, +7.2%) was REPLACED: salutation corrected to "Dear Dr. Buckholtz" (Sergey's
consistent style), numbers re-verified, thermal + sign questions dropped, kept only β_d.

---

## Subject
Follow-up on the reconstruction — one result and one question

## Body (as sent)

Dear Dr. Buckholtz,

Thank you again for the June 14 call and for sharing your procedure document. Following your Step 1 approach, I have been running the reconstruction with real cluster catalogs (MCXC + XMM) and the Moresco cosmic-chronometer H(z) data. Before my question, I want to share one result that I find genuinely striking.

Equation 32 holds cleanly under independent verification. Using PDG 2024 constants, the relation (4/3)(m_τ/m_e)¹² = α_EM/α_G agrees to within 0.17σ — about one part in 7000. This is independent of the cosmological framework, and I consider it the strongest numerical asset in the work; I wanted you to know it survives an independent check. The 7:9:17 boson-mass relation (Eq. 31) also holds for the Higgs, to within about 0.4σ.

With that established, there is one point where your perspective would substantially help. I raise it as a question from a reconstruction, not as a critique.

Computing k_A = E_ICM/c² from cluster X-ray temperatures (kT ≈ 3–8 keV, f_gas ≈ 0.15), I obtain k_A/M ≈ 1.3×10⁻⁶ for a median MCXC cluster. With β_d = 4.5 (Table A1) and near-contact geometry (D ≈ r_A), the dipole force fraction ε = β_d·(k_A/M)·(r_A/D) ≈ 6×10⁻⁶. At the cosmological separations where H(z) is actually probed (D ≫ r_A), ε shrinks by a further factor r_A/D, placing the dipole far below detectability. The Gemini value β_d ≈ 2×10⁴ in your appendix reaches ~3%, but only at the cluster boundary; reaching a 1% signal at cosmological D would require β_d of order 10⁵–10⁶.

My question: is there a physical argument for a large β_d — for example, does it encode a ratio of sub-structure scales not captured by the bulk E_ICM/c² definition — or is β_d intended as a free parameter to be fixed by data? (Relatedly: an unconstrained fit to the 27 cosmic-chronometer points prefers all-positive (1+z) coefficients, which I currently read as the dipole being negligible at β_d = 4.5 rather than as a sign problem — but I would value your view.)

Knowing this would let me either complete a clean reproducibility report or pinpoint the precise next step for the framework. I remain happy to share the full code and the complete reconstruction whenever useful.

With best regards,
Sergey Boyko
Ronin Institute for Independent Scholarship
ORCID: 0009-0009-2178-5701

---

## Number provenance (each figure has an executable source)
- 0.17σ (Eq.32): PDG 2024, LHS/RHS=1.000135 [VERIFIED-inline]
- 0.4σ (Higgs 7:9:17): PDG 2024 [VERIFIED-inline]
- k_A/M ≈ 1.3×10⁻⁶; ε ≈ 6×10⁻⁶ at D≈r_A; β_d ~10⁵–10⁶ for 1% at cosmological D
- Gemini β_d ≈ 2×10⁴ → ~2.6% ("~3%")
- DROPPED (unverifiable/wrong): "6.8σ" (real ~5.7σ), "+7.2% Jeans" (real ~0), thermal & sign Qs

*SENT · docs/121 · 2026-06-17 · awaiting TJB reply on β*
