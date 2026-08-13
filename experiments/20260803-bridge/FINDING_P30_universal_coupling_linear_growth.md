# P30 — universal-coupling linear-growth equations, replacing Archidiacono's DM-only topology with a source-democratic one

**Date:** 2026-08-13
**Origin:** user-specified, following the P22 `4π` correction and the P29
skeptic correction. P29's own withdrawn linkage to P28 left a genuine gap:
this project has never derived what a truly *universal* coupling (P23's
reading of MULTING's `g`) actually does to the linear growth equations —
only a schematic toy (P28) and Archidiacono's own *DM-only* equations
(P29). This finding closes that gap directly, before asking what real
growth-of-structure bounds constrain `ΔG/G_N` (the next, separate step).
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Script:** `P30_universal_coupling_linear_growth.py`

## 0. Honest scope, stated before anything else

This finding derives equations, not bounds. It does **not** search for or
apply any real CMB/BAO/growth-rate observational constraint on `ΔG/G_N` —
that is explicitly the next step this finding sets up, not something it
attempts. It also does **not** re-derive the friction (Hubble-drag) term
of the growth equation from first principles — that term is carried
through unmodified from the standard sub-horizon form, by convention, not
verified symbolically here (only the *source* term, which is what actually
changes between the DM-only and universal cases, is derived and checked).

## 1. Method

Starts from `FINDING_P29`'s own quoted baryon growth equation (the one
concrete, WebFetch-verified piece of Archidiacono's actual perturbation
system this project has), rewritten via the standard Friedmann-equation
identity `(3/2)Ω_mH²=4πG_N·ρ_m` to make the `G_N`-dependence explicit:

```
S_baryon (Archidiacono, DM-only model, UNMODIFIED) = 4π·G_N·ρ_m·(f_χδ_χ+(1−f_χ)δ_b)
```

**Replaces the DM-only topology with a universal one**, per the user's
explicit instruction: instead of only baryons receiving this unmodified
term while DM alone receives an *extra*, DM-sourced fifth-force term (per
P29's own eq. 4.4/4.2 findings), **both** species receive the *same*
enhanced source term, with `G_N→G_eff=G_N+ΔG`, sourced by the *same*
total-matter combination — matching P23's own established reading of
MULTING's `g` as proportional to inertial mass for every species, exactly
as gravity itself is (not DM-restricted, per `MODEL_SPEC_AUDIT.md`'s own
`M500` row).

## 2. Result (sympy-verified)

**(a) Under universal coupling, the two species' source terms are
identical:**

```
S_χ = S_b = 4π·(G_N+ΔG)·ρ_m·(f_χδ_χ+(1−f_χ)δ_b)
S_χ − S_b = 0   (verified, not assumed)
```

Given matched (adiabatic) initial conditions, identical linear ODEs with
identical sources have identical solutions: `δ_χ(t)=δ_b(t)` for all time.
**This re-confirms P28's earlier result — a universal coupling produces no
relative/differential DM-baryon signature — now derived within a fuller
equation structure** (Archidiacono's own quoted baryon-equation template,
not P28's simplified toy source-term comparison).

**(b) The combined single-species equation for total matter reduces
exactly to the user-specified target form.** Defining `δ_m:=f_χδ_χ+
(1−f_χ)δ_b` and substituting `δ_χ=δ_b=δ_m` (licensed by (a)):

```
δ_m'' + Hδ_m' = 4π·G_eff·ρ_m·δ_m,   G_eff = G_N + ΔG
```

Verified symbolically that the derived source term matches this target
exactly (`sp.simplify` confirms zero difference). **This is the standard,
textbook single-species linear growth equation with an enhanced effective
Newton's constant** — the same functional form any standard
modified-gravity growth-rate analysis (`fσ8`, redshift-space distortions,
`σ8`/`S8` constraints) is already built to constrain.

## 3. Why this matters

This closes the gap `FINDING_P29`'s own corrected §3 flagged explicitly:
deriving the universal-coupling analogue of Archidiacono's equations "from
scratch (baryons sourcing and receiving the fifth force too, not just
gravity)" — done here. The result is a **standard**, recognizable equation
form, which means the honest next question this project can now ask is:
*what real growth-of-structure observational bounds exist on `ΔG/G_N`
(equivalently, on a `G_eff/G_N−1` deviation)?* — a well-posed, literature-
searchable question, in contrast to trying to force-fit Archidiacono's own
DM-only-specific `β` bound onto a structurally different coupling (P23,
P28, P29's now-three-times-recorded caveat on `FINDING_P22`'s original
mapping).

## 4. What this does NOT establish

1. **Any numeric bound on `ΔG/G_N`.** No literature search performed, no
   CMB/BAO/growth-rate data consulted. This is a **derivation-only**
   finding — the natural next step (a real bound search) is explicitly
   deferred, not attempted.
2. **A re-derivation of the friction/Hubble-drag term.** Carried through
   unmodified from the standard sub-horizon growth-equation form, by
   convention; only the *source* term (what changes between DM-only and
   universal coupling) was derived and verified here.
3. **That this fully replaces Archidiacono's own eq. 4.2/4.4 mechanism.**
   Those equations describe a specific, screened/mediator-field
   construction (a genuine field `s` with its own dynamics, Compton
   wavelength, etc.). This finding uses their *net effect on the growth
   equations* (a `G_N→G_eff` shift) as the target form, which is the
   standard leading-order behavior expected for `r≪m_φ⁻¹` (per the same
   short-distance regime Archidiacono's own text — quoted in `FINDING_P22`
   — states directly), but does not re-derive the full field-theoretic
   machinery behind it.
4. **A resolution of what value `ΔG` actually takes.** Only its
   *functional role* in the growth equation — connecting it to a number
   still requires either (a) the direct-`G`-measurement route flagged as
   open in P28, or (b) the growth-of-structure bound route this finding
   sets up, neither pursued to a number here.
5. Per NO_AUTHOR_ERROR: entirely about this project's own reconstruction,
   built by generalizing a published external paper's own equations — not
   a claim about TJB's own unpublished theory.

## Reproduction

```bash
python experiments/20260803-bridge/P30_universal_coupling_linear_growth.py
```
