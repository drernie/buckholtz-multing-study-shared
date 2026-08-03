# Letter to Dr. Buckholtz — 2026-08-03

**Status: DRAFT. The user sends, not the assistant.**

Written per `feedback_tjb_no_questions_share_results.md`:
- zero questions — unresolved items framed as *my* limits, not requests
- continuous prose, no numbered report sections
- goal is a useful contribution to his work, not an audit verdict
- technical memorandum stays on our side, not announced as incoming
- ~600 words, matching the format of the successful 2026-06-01 reply

---

**Subject:** MULTING H(z) — a small reproducibility note

Dear Dr. Buckholtz,

Over the past several days I worked through the MULTING H(z) material —
Appendix A, Table A1, and the supplementary transcripts — building a small
private reproducibility scaffold around it. A few things came out of that
which I thought might be worth passing along.

The most useful result, to my mind, concerns the local force law itself. It
reconstructs very cleanly: from F(r,z) = -A2/r² + A3/r³ - A4/r⁴ the potential
follows uniquely, up to the usual additive constant. What I had not expected
is that it also yields an exact structural relation. Writing the force in
normalised form, an intermediate repulsive interval exists only when
ℓ_d > 2ℓ_q — equivalently, ℓ_q ≥ ℓ_d/2 is precisely the condition for the
force to remain attractive at every separation. This is a relation between
the two length scales rather than a fitted quantity, and it is the kind of
thing that can be confronted with data. I ran a first pass against a real
catalogue of 1742 X-ray clusters and found nothing that contradicts it. That
is only a geometric screening, not yet a statistical constraint, but it is a
genuinely checkable feature of the framework, and it belongs to the local
theory rather than to any reconstruction of mine.

On Table A1 — your own caveat about the AI-service responses turned out to be
well placed. Working through the supplementary transcripts, the β_d and β_q
values appear to have been chosen by each service fitting against the H-data
it was supplied, with the curve normalised to the observed H₀ at z=0. This
seems to me a property of how the table was produced rather than anything
about the underlying physics, and it matches your note that you left the
services considerable discretion.

The figure you sent me on 2 August looks like a separate object from Table A1
— digitising both, the two diverge as redshift increases, most of that beyond
the calibration boundary your figure itself marks at z = 1.965. I should say
that I validated my own extraction first: fitting the ΛCDM reference curve on
the same figure recovers flat Planck parameters to about 0.002%, so the
difference is a property of the curves rather than of my digitiser. Where I
ran out of what I could establish is the origin of that curve — I was not able
to work out what produced it, and I have left it unclassified rather than
guess.

I also spent time on the most direct route from the local interaction to a
cosmological background — treating the pair-interaction energy as an effective
fluid. That particular route does not close: for a pure inverse-power
potential the configurational mapping gives w = n/3 for each term, all
positive. I want to be careful about the scope of that, because it is narrow:
it says nothing against a covariant medium, a polarisation sector, or an
explicit averaging prescription. If anything it suggests those are the more
promising directions, and that is where I would like to look next if it would
be of any use to you.

The one thing I could not do at all is find a computation of H_MULT(z) that
does not pass through the AI-service transcripts. That is where my own
reconstruction stops rather than a gap in your work, and I mention it only so
you know the boundary of what I was able to check.

I am glad to write up any of this properly if it would be useful — the local
structural condition seems to me the most immediately valuable piece, and I
would be happy to develop it further. Please treat all of it as entirely
optional and yours to use or set aside.

With respect,

Sergey Boyko
ORCID 0009-0009-2178-5701
Ronin Institute
