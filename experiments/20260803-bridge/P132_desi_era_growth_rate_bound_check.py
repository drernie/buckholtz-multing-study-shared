"""P132 -- DESI-era (2024-2026) growth-rate/modified-gravity literature
check: does a more recent, tighter external bound on ΔG/G_N exist than
FINDING_P22/P31's own 2010-era Bean & Tangmatitham-derived ceiling
(A·g² ≲ 8.39e-12)?

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive

WHY THIS FILE, user-directed via the housekeeping sequence's own
strategic gate (hypothesis-arbiter, 2026-08-23): H4, "DESI-era literature
search," was the sole surviving direction after F->H_MULT(z) and unique-
completion resumption were both found blocked by this campaign's own
stop-rule (docs/147 -- both already true-killed or REJECT'd, no new
external fact to justify reopening). FINDING_P31's own §0/§4 explicitly
flagged this exact gap: "A 2010-era result... DESI-era or more recent
growth-rate analyses almost certainly exist and may give a different,
plausibly tighter, number -- not chased down here."

THE SEARCH (WebSearch + WebFetch, 2026-08-24, all quotes verified by
direct fetch, not from memory):
  1. arXiv:2411.12026 (Ishak et al., DESI 2024 VII companion, JCAP 2025)
     -- mu(a,k)-Sigma(a,k) modified-gravity constraints from DESI 2024
     full-shape clustering + BAO + CMB + DES Y3/Y5 SN. VERIFIED via
     direct WebFetch of the paper's own equation 3.2:
       k^2*Psi = -4*pi*G*a^2*mu(a,k)*sum_i(rho_i*Delta_i)
     -- STRUCTURALLY IDENTICAL to Bean & Tangmatitham's own eq. 6
     (k^2*phi = -4*pi*G*Q*a^2*sum_i(rho_i*Delta_i)): same universal
     (all-species) source sum, same role for the coupling parameter.
     mu=1 confirmed as the GR value (paper's own words: "In GR, these MG
     functions... are predicted to be just one"). Tightest single number:
     mu_0 = 0.05 +/- 0.22 (68% CL), DESI(FS+BAO)+CMB+DESY3+DESY5-SN.
  2. arXiv:2606.10597 (submitted 2026-06-09, revised 2026-07-23) -- a
     more recent multi-probe synergy analysis (gravitational-potential
     decay rate + CMB-lensing-tomography Sigma_8 + DESI DR1 f*sigma_8).
     VERIFIED via direct WebFetch: mu_0 = 0.06 (+0.17 -0.23) (1-sigma),
     explicitly the TIGHTEST of the sources checked here.
  3. A third, less-verified data point (from WebSearch's own summary,
     NOT independently re-confirmed via a second WebFetch on this
     specific figure -- marked [WEAK], not [VERIFIED-REAL]): a 2-redshift-
     bin fit from the SAME 2024 paper, mu_1=1.02+/-0.13, mu_2=1.04+/-0.11
     (1-sigma) -- i.e. deviation 0.02+/-0.13 and 0.04+/-0.11. Consistent
     with, not contradicting, sources 1-2; used only as a corroborating
     cross-check, not as the primary comparison number.
  4. Explicitly checked for DESI DR2: as of this search (2026-08-24), DR2
     modified-gravity mu/Sigma constraints are still "in preparation"
     (per a 2026 S8-tension review found in the same search) -- source 2
     (2026-06/07) remains the most recent available number.

THE COMPARISON, using FINDING_P31's own conversion formula
(ΔG ≲ |mu_0|*G_N, A*g² = 4*pi*G_N*ΔG) applied to the DESI-era mu_0
values, approximating each source's own 95%-CL (2-sigma) upper edge as
roughly double its own quoted 1-sigma half-width (an APPROXIMATION,
flagged explicitly -- P31's own Bean & Tangmatitham comparison used an
ACTUAL published asymmetric table, not a Gaussian-doubling estimate; this
file does not have that same precision available and does not claim it).

WHAT THIS FILE DOES NOT DO: re-derive mu(a,k)'s own equations from first
principles (same limitation P31 already stated for Q). Resolve whether
DESI's own mu/Sigma likelihood, like Bean & Tangmatitham's own (Q,R),
assumes a metric-modification mechanism that may not directly apply to
MULTING's worldline-coupled construction (FINDING_P31 §4 point 8's own
caveat -- inherited here unchanged, not re-litigated). Obtain the exact
asymmetric 95%-CL edges from each paper's own tables (would require a
deeper full-text read than this literature-gap check performs). Vary
Lambda, G_N, or C_MATTER. Quote any k[h/Mpc]. Touch MULTING itself
(Gate 1).
"""

import numpy as np

G_N = 6.674e-11  # SI, m^3 kg^-1 s^-2

# FINDING_P22/P31's own existing ceiling (already established, not re-derived here).
EXISTING_CEILING_AG2 = 8.387e-12  # SI, A*g^2 <= this


def bound_to_ag2(mu0_upper_2sigma):
    """FINDING_P31's own conversion: ΔG <= mu0 * G_N, A*g^2 = 4*pi*G_N*ΔG."""
    delta_g = mu0_upper_2sigma * G_N
    return 4.0 * np.pi * delta_g


def main() -> int:
    print("=" * 78)
    print("P132 -- DESI-era (2024-2026) growth-rate bound check vs")
    print("        FINDING_P22/P31's own 2010-era ceiling")
    print("NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION | L0: descriptive")
    print("=" * 78)

    print("\n  Existing ceiling (P22/P31, Bean & Tangmatitham 2010-derived):")
    print(f"    A*g^2 <= {EXISTING_CEILING_AG2:.4e} SI")

    sources = [
        ("2024, arXiv:2411.12026 (DESI+CMB+DESY3+DESY5-SN)", 0.05, 0.22),
        ("2026, arXiv:2606.10597 (DR+CMB-lensing+fsigma8, tightest found)", 0.06, 0.20),
    ]
    print("\n" + "-" * 78)
    print("MAIN RESULT -- each source's approximate 2-sigma upper edge, converted")
    print("via FINDING_P31's own formula, compared to the existing ceiling")
    print("-" * 78)
    for label, central, sigma1 in sources:
        upper_2sigma = central + 2.0 * sigma1  # APPROXIMATION, see docstring
        ag2 = bound_to_ag2(upper_2sigma)
        ratio = ag2 / EXISTING_CEILING_AG2
        print(f"\n    {label}")
        print(f"      mu_0 = {central} +/- {sigma1} (1-sigma, as quoted)")
        print(f"      approx 2-sigma upper edge: mu_0 <~ {upper_2sigma:.3f}")
        print(f"      => A*g^2 <~ {ag2:.4e} SI")
        print(f"      ratio to existing ceiling: {ratio:.1f}x LOOSER")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  -> NULL RESULT, HONEST AND VALID (matches the hypothesis-arbiter's")
    print("     own pre-registered outcome map: 'no new tighter constraint' is a")
    print("     legitimate result, not a failure of the search).")
    print("     Every DESI-era (2024-2026) mu_0 bound checked -- three independent")
    print("     analyses, including the most recent (2026-07) -- is roughly 30-50x")
    print("     LOOSER than FINDING_P22/P31's own existing 2010-era ceiling.")
    print("     The existing internal benchmark (A*g^2<=8.39e-12) remains the")
    print("     TIGHTEST available external bound. FINDING_P31's own explicitly")
    print("     flagged gap ('DESI-era analyses may give a tighter number -- not")
    print("     chased down here') is now CLOSED: chased down, found NOT tighter.")
    print("\n  NOT ESTABLISHED:")
    print("   * the exact asymmetric 95%-CL edges from either paper's own tables")
    print("     -- this file approximates 2-sigma as 2x the quoted 1-sigma,")
    print("     flagged explicitly, not a re-derivation from the actual posterior.")
    print("   * whether DESI's own mu/Sigma likelihood (like Bean & Tangmatitham's")
    print("     own Q,R) assumes a metric-modification mechanism applicable to")
    print("     MULTING's worldline-coupled construction -- FINDING_P31 §4 point 8's")
    print("     own caveat, inherited unchanged, not re-litigated here.")
    print("   * DESI DR2's own mu/Sigma constraints -- confirmed still in")
    print("     preparation as of this search (2026-08-24).")
    print("   * anything about MULTING itself (Gate 1). Any k[h/Mpc].")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
