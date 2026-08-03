# Certificate C5A — the supplementary transcripts

**Verdict: `DATA_CONDITIONED_CONSTRUCTION`**
**Labels:** NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION · L0 descriptive
**Scope: Table A1 and the supplementary service transcripts only. Figure 3 is a
separate object and is not addressed here.**

**Handling note.** The per-service tables are gitignored by the maintainer's
publication-hygiene policy (`data/supplementary_extracted/README.md`). That policy
permits reporting aggregate, non-redistributive observations. No table is
reproduced here; only structural facts and the services' own annotations.

---

## The question C5A had to settle

> Were the observed `H(z)` values available to the service when it produced the
> H-MULT column — that is, is H-MULT a prediction or a fit?

**Answered, unambiguously: a fit.** All three services state it themselves in the
supplementary material's own recap tables.

## The evidence, in the services' own words

| service | `β_d` | `β_q` | the annotation attached to those values |
|---|---|---|---|
| ChatGPT | 0.78 | 0.19 | **"Best-fit value minimizing RMS deviation from H-data"** |
| Claude | 4.5 | 18.0 | **"Best-fit value (from page 21 optimization section)"** |
| Gemini | 4.25 | 8.10 | **"Determined value from fitting"** |

And the normalisation, stated in two independent services' recaps:

> `h0_anchor = 73.0 km/s/Mpc` — **"H_MULT normalized to this value at z=0"**

73.0 is the observed `H₀`. So at `z = 0`, `H_MULT = H_data = 73.0` and
`σ_MULT = 0` **by construction**, not by agreement.

ChatGPT additionally supplies an analytic `w_eff`:

> `w_eff = −1 + 0.28 tanh[(z − 0.9)/0.9]` — **"Effective equation of state
> fitting MULTING H(z)"**

## Dependency graph

```
published observations (SH0ES 2022, Moresco 2022/2014, BOSS BAO)
        │
        ├──────────────► each service selects its own H-data values
        │                (they disagree — see below)
        │
        ├──────────────► beta_d, beta_q FITTED to minimise deviation from those
        │                                values
        │
        ├──────────────► H0 anchor set to the observed 73.0
        │
        ▼
   H-MULT column  ──────► sigma_MULT computed against the same H-data
        │
        ▼
   Table A1  =  the Claude service's row of this graph
                (beta_d = 4.5, beta_q = 18.0 identifies it uniquely)
```

There is no branch in this graph that runs from the force law to `H(z)` without
passing through the observations.

## What this explains

Every numerical anomaly found earlier now has a mechanism:

| observation (found before the transcripts were read) | explained by |
|---|---|
| `H_w_eff` reproduces `H_data` to 0.29 % rms | `w_eff` was fitted to `H-data` |
| `H_MULT(0) = H_obs(0) = 73.0`, `σ_MULT = 0` | explicit `h0_anchor` normalisation |
| three services differ by 5.8× in `β_d`, 94.7× in `β_q` | each fitted independently, to different H-data |
| `H_FLRW` matches no standard cosmology | each service generated its own |
| `(z, t)` pairs inconsistent with ΛCDM | each service assigned its own redshifts |

## The services disagreed on the observations themselves

Same cosmic time, different redshift and different "observed" `H`:

| `t` [Gyr] | `z` (Claude) | `z` (Gemini) | `H_data` (Claude) | `H_data` (Gemini) |
|---|---|---|---|---|
| 13.5 | 0.00 | 0.02 | 73.0 | 70.2 |
| 10.0 | 0.40 | 0.38 | 82.0 | 90.5 |
| 9.0 | 0.65 | 0.54 | 92.0 | 101.2 |

At `t = 9` Gyr the two services differ by 10 % in the quantity they both call an
observation. This is the source-level counterpart of the paper's own statement
that "the services disagreed somewhat regarding observed values of `H(z)`".

## A finding that reframes the project's standing request

**The missing bridge inputs exist in the supplementary material.**

For eight months this project has been asking for `k_A(z)`, `r_A(z)` and the
separation `D(z)` — recorded as open question Q2, and identified as the reason
the bridge could not be built. They are present:

- Claude, p. 20: `m_A`, `r_A`, `D_CAB`, `k_A/c²` — as **ranges**, twelve rows
- Gemini, pp. 26–27: the same four quantities — as **single values**, eleven rows

**But they are service output, not author-supplied physics.** Two services
produced different values for the same quantities at the same cosmic times, and
neither derived them — they were chosen alongside the fitted `β`.

So the correct next request to the author is not "please supply `k_A`, `r_A`,
`D`". Those exist and are not the obstacle. The question is whether **any**
calculation of `H(z)` from MULTING exists that does not pass through a service
fitting two coefficients to the data it is meant to predict.

## Verdict against the frozen options

```
REPRODUCIBLE_OPERATOR              no
DATA_CONDITIONED_CONSTRUCTION      YES  <-- Table A1's H-MULT column
GRAPHICAL_INTERPOLATION            not applicable at this level
NON_IDENTIFIABLE                   no — the construction IS identifiable,
                                   and it is a two-parameter fit plus an anchor
```

The construction is identifiable. That is a stronger and more useful result than
"non-identifiable": we now know what was done, and it was a fit of `β_d`, `β_q`
to `H-data`, normalised to the observed `H₀`.

## Scope — what this certificate does not establish

- **Nothing about Figure 3.** Whether it is a plot of Table A1, of a separate
  computation, or of something else, is C5B and requires its own evidence. The
  standing instruction not to transfer C1 or C5A to Figure 3 is observed.
- Nothing about whether the MULTING force law is correct. A model whose free
  parameters are fitted to data is not thereby wrong; it is thereby not tested by
  those data.
- Nothing about the author's intent. He states the provenance plainly, flags the
  services' unreliability, and reports the disagreements himself.
- The `β` values are fitted **within the supplementary's own framing**; we have
  not verified that the fits are correct fits, only that they are described as
  fits.

## The one number this changes

Any statement of the form "MULTING reproduces `H(z)` better than ΛCDM" drawn from
Table A1 compares a **two-parameter fit anchored to the data** against a
**zero-free-parameter Planck cosmology**. That is not a like-for-like comparison,
and the σ columns in Table A1 do not carry a parameter penalty. The repository
already holds `scripts/aic_model_comparison.py` for exactly this correction; it
should now be pointed at this framing.
