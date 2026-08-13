# P29 — Archidiacono's own DM-only model has an absolute-growth mechanism via gravitational feedback; their coupling topology differs from MULTING's universal g

**Date:** 2026-08-13
**Origin:** direct continuation of `FINDING_P28`'s own corrected §4 point 1
— flagged, but not checked there, whether Archidiacono et al.'s actual
CMB+BAO pipeline (beyond the toy differential-growth model P28 used) has
independent sensitivity to absolute matter-growth amplitude. This finding
goes to their own field equations (via WebFetch, not general
modified-gravity-literature reasoning) to check directly.
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P29_archidiacono_own_equations_absolute_growth.py`

**[CORRECTED after skeptic review, same day.]** The title originally
claimed this finding "confirms an absolute growth channel exists" in a way
that "directly strengthens" `FINDING_P28`'s corrected retraction. The
skeptic's most consequential catch (below, sub-verdict C1): this is a
**non-sequitur**. §2(b)'s real result — baryons in Archidiacono's own
*DM-only* model respond gravitationally to enhanced `δ_χ` — is a different
mechanism from what P28's retraction was actually about (a *universal*
coupling enhancing *both* species' growth *directly*, via the fifth force
itself, not via secondary gravitational feedback). Demonstrating the first
does not confirm the second. §3 is corrected below to withdraw that
linkage. A second real issue: §1's "two independent WebFetch queries,
cross-checked" language is **exactly** the framing `FINDING_P22` itself
already retracted in its own Skeptic Verdict section (*"multiple WebFetch
calls to the same URL are not independent verification of each other"*) —
this finding repeated an error already caught and fixed elsewhere in this
same session. See the Skeptic Verdict section for the full breakdown (13
sub-verdicts).

## 0. Honest scope, stated before anything else

**Evidence-quality caveat, stated up front:** the quoted equations below
come from two WebFetch calls against `arxiv.org/html/2204.08484`, mediated
by a summarization model — not a direct read of the paper's raw LaTeX
source. This is a real, structural limitation of the tool available in
this session (the `WebFetch` tool converts and summarizes; it does not
return verbatim source). Two independent, differently-worded queries
against the same page returned **consistent** equation text both times
(cross-checked below), which raises confidence above a single query, but
this is still `[VERIFIED-WEBFETCH]`, one tier below directly reading a
source file — not `[VERIFIED-BASH]`. If a future finding can access the
paper's raw source (e.g. the arXiv LaTeX source download), it should
re-verify these equations directly and upgrade the marker.

This finding does **not** derive any new numeric bound, does not
reconstruct Archidiacono et al.'s actual MCMC likelihood, and does not
resolve whether their `β<0.01` bound, reinterpreted for a universal
coupling, would be tighter or looser than the DM-only case. **[Corrected
after skeptic review — point (1) below originally claimed this
"strengthens FINDING_P28's corrected retraction"; that linkage was a
non-sequitur, see §3.]** It establishes two narrower, more concrete points:
(1) their own *DM-only* model has a mechanism for absolute (not merely
differential) growth enhancement via ordinary gravitational feedback on
baryons — a real observation about their model on its own terms, but one
that does *not* by itself say anything about how a *universal* coupling
would behave in their pipeline; and (2) their fifth force has a different
source-receiver topology than MULTING's own universal `g` — equation-level
specificity added to a caveat P23 already established, not a structurally
new one.

## 1. Source verification (two WebFetch queries against the same page)

**[Corrected after skeptic review]** ~~Two independent WebFetch queries,
cross-checked~~ — **[corrected]** same URL, same session, same
summarization model. `FINDING_P22`'s own Skeptic Verdict section already
retracted exactly this framing: *"multiple WebFetch calls to the same URL
are not independent verification of each other — language implying
otherwise ('confirmed twice/three times independently') has been avoided."*
This finding repeated that error. What the two queries below *do* show:
the summarizer returned the *same* text for eq. 4.4 on two differently-worded
prompts, which is evidence the summarization is not wildly unstable on this
input — but if the summarization silently drops or misplaces a term on
*every* pass (a systematic error, not a random one), two queries would
reproduce that error identically, not catch it. Treat both quotes below as
`[VERIFIED-WEBFETCH]` from a **single underlying source read**, not as two
independent checks.

Query 1 (broad: "does the paper discuss σ8/S8, and universal coupling
degeneracies?") returned, among other content, their Poisson-type equation
(their eq. 4.4):

> "k²δs = −a² 4πGₙβ(∂log mχ(s)/∂s) ρ̄χδχ"

and quoted their own text characterizing eq. 4.16 as containing "a new
contribution to the potential... as well as a suppression of Ωₘ below unity
due to the fraction of the total energy density" — i.e., a term that
affects the **DM density equation directly**, not only a relative quantity.

Query 2 (targeted: "confirm precisely whether the Poisson-type source
includes a baryon term, and whether baryons feel the fifth force directly")
returned the **same** equation 4.4 (verbatim match against query 1),
their DM Euler equation (eq. 4.2):

> "θ'χ + (ℋ + ∂log mχ(s)/∂s · s̄') θχ − k²(Ψ + ∂log mχ(s)/∂s · δs) = 0"

and a baryon growth equation from the coupled system around eq. 4.16:

> "δ''b + ℋδ'b − (3/2)Ωm ℋ²(fχδχ + (1−fχ)δb) = 0"

**[Corrected after skeptic review]** ~~The two queries' quotes of eq. 4.4
match verbatim — the strongest cross-check available without raw-source
access.~~ The two queries' quotes of eq. 4.4 match verbatim — consistent
with a stable (not obviously hallucinating-differently-each-time)
summarization on this specific equation, but **not** an independent
cross-check per the correction above; a systematic misreading would
reproduce identically across both queries.

## 2. Method and result

**(a) Structural comparison — is Archidiacono's coupling the same
functional form as a universal coupling, just rescaled?** No. Their eq.
4.4's source term, as transcribed from the WebFetch quote, contains only
`ρ̄_χδ_χ` (dark matter density perturbation) — no `δ_b` term appears in
that transcription. **[Corrected after skeptic review]** ~~verified: `delta_b
not in dm_only.free_symbols`, sympy~~ — that sympy check only confirms the
symbols *typed into the script* match the *quote as transcribed*; it is
not independent verification of the quote itself (the real evidence is
§1's WebFetch text, with the caveats stated there). A genuinely universal
coupling (P23's reading of MULTING's `g` — proportional to inertial mass
for *every* species, exactly as gravity itself is) would source its
Poisson-type equation from the **total** matter perturbation `δ_tot =
f_χδ_χ + (1−f_χ)δ_b`, which structurally requires a baryon contribution.
If the transcribed eq. 4.4 is accurate, these are not the same functional
form under a relabeling of the coupling strength — one is DM-self-sourced,
the other is source-democratic across species. A future re-mapping of
Archidiacono's `β` bound onto MULTING's universal `g` (as `FINDING_P22`
originally did) needs to account for this topology difference, not just
rescale the coupling magnitude.

**(b) Does Archidiacono's own DM-only model still produce an absolute
growth effect, even though the fifth-force term itself only appears in the
DM equation?** As transcribed, yes. Their own quoted baryon growth equation
is sourced by `(3/2)Ω_mH²(f_χδ_χ + (1−f_χ)δ_b)` — a term with nonzero
derivative with respect to `δ_χ`. **[Corrected after skeptic review]**
~~verified symbolically: `∂/∂δ_χ = (3/2)Ω_mH²f_χ ≠ 0`~~ — this derivative
is trivially forced by the linear form as transcribed; sympy adds nothing
beyond confirming arithmetic on what was typed in, not an independent check
on whether the transcription is right. Baryons carry no direct fifth-force
term, but they **do**, on this transcription, respond to enhanced DM
clustering through ordinary gravity, since baryon growth is sourced by the
*total* matter perturbation, which includes the (fifth-force-enhanced)
`δ_χ`. Combined with the paper's own characterization of eq. 4.16 as
containing "a new contribution to the potential" affecting the DM equation
directly, this is consistent with: **even in their own DM-only model, an
absolute (not merely differential) growth-of-structure channel exists** —
the fifth force boosts DM's own growth, which then, via standard gravity,
also boosts baryon growth, alongside the differential DM-baryon lag their
abstract highlights as the paper's headline novel signature. **This
existence claim says nothing about magnitude** — whether this channel is
large enough to be *observationally* significant (e.g. detectable in `σ8`)
is not addressed here; per `β<0.01`, the effect is small by construction,
and "exists" is not the same claim as "is significant."

## 3. Consequence for `FINDING_P28`'s correction

**[CORRECTED after skeptic review — a non-sequitur, the single most
consequential catch on this finding.]** ~~This directly strengthens
FINDING_P28's corrected retraction with concrete textual evidence,
replacing what was previously argued only from general
modified-gravity-literature plausibility.~~ **It does not.** `FINDING_P28`'s
corrected retraction was specifically about a **universal** coupling —
enhancing *both* `δ_χ` and `δ_b` *directly*, through the fifth force
itself, which is what would show up in standard `σ8`/growth-of-structure
channels. §2(b) above demonstrates something different: in Archidiacono's
own **DM-only** model, baryons respond to `δ_χ` *indirectly*, through
ordinary gravity — the same generic mechanism by which baryons would follow
enhanced clustering in *any* scenario where dark matter clusters more
than baryons (warm dark matter, mixed dark matter, etc.), not something
specific to a fifth force being universal. Demonstrating gravitational
feedback in the DM-only case does not license a conclusion about the
visibility of a *universal* coupling — those are different mechanisms. If
anything, this observation cuts the other way: it suggests Archidiacono's
own `β<0.01` bound might *already* carry some sensitivity to absolute
growth even in the DM-only case they actually studied, which complicates
rather than confirms the "universal case would be dramatically more
constrained" intuition P28's retraction leaned on.

**Corrected, narrower consequence, matching the scope this finding can
actually support:** Archidiacono's own field equations show their DM-only
model is not purely differential in its effects — an absolute growth
channel exists via gravitational feedback (§2(b)) — but this finding does
**not** establish anything about how a *universal* MULTING-style coupling
would behave in their pipeline. That would require deriving the universal-
coupling analogue of their eq. 4.4 and eq. 4.16 from scratch (baryons
sourcing and receiving the fifth force too, not just gravity), which this
finding does not attempt — see `FINDING_P30` (planned) for that next step.

~~It does not resolve what P28 §4 point 2 (corrected) left open... If
anything, this adds a third, independent reason...~~ **[Corrected]** §2(a)'s
topology observation (DM-sourced-only vs. universal) is real, but on
reflection it is **substantially the same fact** P23 already established
(MULTING's `g` couples to total cluster mass, not a DM-only component),
now expressed at the level of the mediator's own source term rather than
the target population. Calling it a "third, independent reason" alongside
P23 and P28 double-counted P23 — more accurately, this finding adds
**equation-level specificity** to P23's already-recorded caveat, not a new,
independent one. `FINDING_P22`'s mapping still needs re-examination for
exactly the reason P23 already gave; this finding sharpens *how* that
mismatch shows up mathematically, without adding a structurally distinct
objection.

## 4. What this does NOT establish

1. **A numeric bound of any kind.** No MCMC, no likelihood, no re-derived
   `β` value. Purely a structural/equation-level comparison.
2. **That Archidiacono's `σ8`/`S8` is explicitly varied or reported as a
   derived parameter in their fit.** The two WebFetch queries could not
   confirm this from the available (summarized) text — flagged as
   genuinely `[UNKNOWN]`, not assumed either way.
3. **A resolution of whether a universal-coupling reinterpretation of their
   bound would be tighter or looser than the DM-only case.** Only that the
   two cases are structurally different couplings, not a rescaling of one
   into the other — a prerequisite question for that comparison, not the
   comparison itself.
4. **A revision of `FINDING_P22`'s numeric `A·g²` figure.** Not attempted
   here (`FINDING_P22` was independently corrected the same day, on an
   unrelated `4π`-normalization issue, to `A·g²≲8.39×10⁻¹²` — this finding
   only adds a further caveat on the mapping's *applicability*, joining
   P23's and P28's already-recorded caveats, and is orthogonal to that
   numeric correction).
5. **Verbatim-source confidence.** Per §0, these equations are
   WebFetch-mediated (summarized), not directly read from source — treat
   as `[VERIFIED-WEBFETCH]`, one tier below a direct file read, pending
   future re-verification against raw LaTeX if available.
6. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction of
   the coupling structure and a published external paper's own equations —
   not a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P29_archidiacono_own_equations_absolute_growth.py
```

## Skeptic verdict (context-blind, Step 8a, 2026-08-13)

Given only this file, the script, `FINDING_P28_archidiacono_differential_blindness.md`
(corrected), `FINDING_P23_target_population_confirmed_universal.md`
(corrected), and `FINDING_P22_archidiacono_beta_mapping.md` — no session
history. 13 sub-verdicts, per Step 8a (not merged):

- **A1–A3** (physical plausibility of the quoted eq. 4.4, eq. 4.2, and the
  baryon growth equation): **CONFIRMED-REAL** — the quoted forms are
  textbook Damour–Polyakov-style scalar-source equations, internally
  consistent with the paper's own stated setup (a scalar coupled only to
  DM). No error found in the physics plausibility of the transcriptions
  themselves.
- **A4** (redundant symbol `β` and `∂log mχ/∂s` carried as independent):
  **WEAKENED** — schematized more than "verbatim" implies; does not affect
  the structural argument.
- **B1/B2** (sympy checks as "verification"): **WEAKENED — tautological**.
  `delta_b not in dm_only.free_symbols` and the nonzero-derivative check
  each only restate what was typed into the script; the real evidentiary
  weight is the WebFetch quote, not the sympy arithmetic. *Applied: FIXED —
  §2 and the script's print statements corrected to say "consistent with
  transcription," not "verified"/"confirmed."*
- **B3** (the "universal" comparison case): **FALSIFIED as an external
  comparison** — `universal_poisson_source` is a hand-built stipulation,
  never itself sourced from any paper or from MULTING's own action; framing
  it as "verified symbolically, not asserted" oversold an internal
  counterfactual structure as a fetched-vs-fetched comparison. *Applied:
  noted explicitly in the script's own output.*
- **C1** (§2(b)→§3 inferential leap — **the single most consequential
  issue**): **FALSIFIED as a non-sequitur.** P28's retraction concerned a
  *universal* coupling's direct enhancement of both species, showing up in
  `σ8`; P29's §2(b) demonstrates a *different* mechanism (DM-only fifth
  force → gravitational feedback onto baryons) in a genuinely DM-only
  model. The first does not license conclusions about the second. If
  anything, this observation suggests Archidiacono's own DM-only bound may
  already carry some absolute-growth sensitivity, complicating rather than
  confirming the "universal case is dramatically tighter" intuition.
  *Applied: FIXED — §3 rewritten, the "directly strengthens" claim
  withdrawn and replaced with a narrower, correctly-scoped consequence;
  title changed.*
- **D1** ("third independent caveat" on `FINDING_P22`'s mapping):
  **WEAKENED** — largely restates P23's target-population caveat
  (MULTING's `g` couples to total mass, not DM-only) from the mediator/
  source side rather than the mass/receiver side; the two are two views of
  the same mismatch, not independent caveats. *Applied: FIXED — §3
  corrected to describe this as equation-level specificity added to P23's
  caveat, not a new, independent one.*
- **E1** ("two independent WebFetch queries, cross-checked"): **FALSIFIED**
  — this is exactly the methodology framing `FINDING_P22`'s own Skeptic
  Verdict section already retracted (*"multiple WebFetch calls to the same
  URL are not independent verification of each other"*), repeated here
  despite being available to check against. *Applied: FIXED — §1 corrected
  throughout, title-level banner added.*
- **E2** (script's `CONFIRMED:` print statements): **WEAKENED** — evidence-
  marker inflation; the honest chain is WebFetch summarization → hand-typed
  sympy expression → sympy verifies its own typing, which does not license
  "CONFIRMED." *Applied: FIXED — script corrected to "CONSISTENT WITH
  TRANSCRIPTION."*
- **F1** (§0 vs. §3 internal contradiction — §0 disclaimed resolving
  directionality, §3 claimed to strengthen a directional retraction):
  **WEAKENED** — real contradiction. *Applied: FIXED — §0 corrected to
  match §3's corrected, narrower scope.*
- **F2** ("absolute growth channel exists" vs. observational significance):
  **WEAKENED** — existence is not the same claim as magnitude/detectability;
  not addressed in the original. *Applied: FIXED — explicit caveat added to
  §2(b) and the script's output.*

**Not a core-predicate-false kill of the finding's narrow structural
observations** — §2(a) (topology mismatch, as transcribed) and §2(b)
(gravitational-feedback mechanism, as transcribed) survive as textual/
schematic observations. **This is a framing/scope issue with a genuine
inferential error baked in** — specifically C1, which required withdrawing
the finding's central interpretive claim (that it strengthens P28), not
merely softening it. The skeptic's own one-line summary: *"P29's narrow
structural observations survive, but its interpretive claim that this
strengthens P28's retraction is a non-sequitur, its 'third caveat' claim
largely restates P23, and its 'two-independent-WebFetch cross-check'
language repeats exactly the methodology error P22 itself already
retracted."*
