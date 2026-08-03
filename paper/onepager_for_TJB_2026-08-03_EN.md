# MULTING → H(z): consolidated audit

**One page. 2026-08-03. Our reconstruction — errors are ours.**
The local force law is **not** rejected by this work. What follows separates the
reproducible parts of the framework from the one part that still needs a bridge.

---

### 1 · The local interaction's radial dependence reconstructs uniquely, up to $C(z)$

$$F(r,z)=-\frac{A_2}{r^{2}}+\frac{A_3}{r^{3}}-\frac{A_4}{r^{4}}
\qquad\Longrightarrow\qquad
U(r,z)=-\frac{A_2}{r}+\frac{A_3}{2r^{2}}-\frac{A_4}{3r^{3}}+C(z)$$

$C(z)$ is the ordinary additive freedom that leaves the local force unchanged.
The force law stands as a testable physical hypothesis.

### 2 · The simplest pair-fluid bridge is closed — as an identity, not an estimate

For $U\propto r^{-n}$, Euler's identity applied **pair by pair, before averaging**:

$$s\,\frac{dU}{ds}=-n\,U \quad\Longrightarrow\quad p=\frac{n}{3}\,\rho
\quad\Longrightarrow\quad w=\tfrac13,\ \tfrac23,\ 1 \ \text{ for the three terms.}$$

None is negative. Verified symbolically and across 360 configurations to
$7\times10^{-16}$.

> **Scope — this is narrow on purpose.** It closes the configurational
> pair-fluid mapping **only**. It says nothing against a covariant medium, a
> polarisation sector, a nonlocal completion, or explicit cosmological averaging.

### 3 · Table A1 and the later H(z) curve are two different objects

Table A1's status you flagged yourself. We took the caveat seriously and worked
out the consequence: $\beta_d,\beta_q$ were selected by minimising deviation from
the H-data, with the curve normalised to the observed $H_0$ at $z=0$. Read it as
an exploratory, data-conditioned calibration — a statement about procedure, not
about the model.

The later curve is a **separate object with its own provenance**, and it is not a
plot of Table A1:

| $z$ | 0.00 | 0.06 | 0.14 | 0.25 | 0.40 | 0.65 | 1.00 | 1.50 | 2.10 |
|---|---|---|---|---|---|---|---|---|---|
| curve | 73.9 | 72.6 | 72.6 | 75.4 | 83.0 | 101.2 | 130.4 | 172.1 | 218.6 |
| Table A1 $H_{\rm MULT}$ | 73.0 | 70.2 | 73.5 | 78.8 | 83.1 | 91.4 | 104.2 | 126.5 | 151.8 |
| deviation | +1.2% | +3.4% | −1.2% | −4.3% | −0.1% | **+10.7%** | **+25.1%** | **+36.1%** | **+44.0%** |

**rms 21 %.** All nine rows in range shown, none omitted. Below $z=0.4$ they
scatter by a few per cent in both directions; above it the difference is
one-sided and monotone. Nor is the curve flat ΛCDM re-anchored: the ratio between
the two plotted curves varies 10 % and crosses unity.

**The 44 % point is past the source figure's own calibration boundary.** Your
figure marks $z=1.965$ as where "calibrated data ends, extrapolation begins."
The $z=2.10$ comparison above sits just beyond that line; within it, the
largest divergence is $36\%$ at $z=1.50$.

**Positive control on our own extraction.** The blue curve on the same figure
recovers as flat Planck ΛCDM at $H_0=67.37$, $\Omega_m=0.3152$, **rms 0.002 %** —
two parts in $10^5$. The distinct shape is therefore a property of the curve, not
of our digitiser. *(See the attached figure: control and result on one panel.)*

**Observational status on real data — not yet a certified comparison.**
Evaluated at the 27 real cosmic-chronometer points (Moresco et al. 2022), the
curve gives $\chi^2=14.4$ against a flat-ΛCDM best fit's $\chi^2=12.8$ (2
parameters, $H_0=68.8$, $\Omega_m=0.32$). Read naively this favours ΛCDM; but
penalise ΛCDM's two fitted parameters (AIC or BIC) and the sign reverses in the
curve's favour. Neither reading should be asserted: the curve's own effective
degrees of freedom are unknown, since its generating operator is unidentified
(§3), so no parameter count can honestly be assigned to it yet. **Status:
curve-level distinct; no observational preference is established either way
until a protocol fixes what is being compared on both sides.**

### 4 · What the audit leaves — the main result

$$\text{local MULTING force}\;\longrightarrow\;
\boxed{\;\text{unidentified physical bridge}\;}\;\longrightarrow\;H(z)$$

The first stage is explicit. The last stage is a numerical target curve whose
generating procedure is not identified in the material available to us. The
open problem sits entirely in the box, and it is now considerably narrower
than it was.

### 5 · One exact local structural condition survives, and remains testable

$$F(r)\propto-\frac{1}{r^{2}}+\frac{\ell_d}{r^{3}}-\frac{\ell_q^{2}}{r^{4}}$$

An intermediate **repulsive** interval exists only when $\ell_d>2\ell_q$, so

$$\boxed{\ \ell_q\ \ge\ \ell_d/2\ }$$

is the exact condition for the force to stay attractive at every separation. A
relation between the two length scales, not a fit. Confrontable with cluster
dynamics, pairwise velocities, lensing and kSZ-conditioned samples. A
preliminary pass against 1742 X-ray clusters found no overt contradiction,
though this is a geometric screening, not yet a statistical constraint on the
parameters.

---

### What we will state in the memorandum, absent further information

1. **the later H(z) curve** — a separate, code-generated artifact whose
   generating procedure is not identified in the material available to us; not classified as an independent
   forward prediction without further basis.
2. **the effective energy behind it** — carried by an unspecified sector,
   since the standard pair-fluid mapping of pair-interaction energy (§2) is
   not sufficient on its own.

A line from you on either point would be welcome, whenever convenient; nothing
here depends on a reply.

---

*Curves digitised by colour from the supplied figure; Table A1 values from the
published table. Full certificates, negative results and reproduction commands
are in the technical memorandum in preparation.*

*The parts of this we could audit cleanly — the caveat you attached to Table A1,
the calibration boundaries marked explicitly on the later figure — were
auditable because they were documented, not smoothed over. That made this a
constructive audit rather than an adversarial one.*
