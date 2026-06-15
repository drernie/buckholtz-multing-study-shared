# Author Questions — k_A Closure Test (Q15–Q18)

**Status:** PENDING — awaiting author response  
**Labels:** NOT_VALIDATION | INTERNAL_CLOSURE_TEST | AUTHOR_CONFIRMATION_REQUIRED  
**Reference:** docs/99_k_a_closure_report.md

---

## Q15: What physical quantity is k_A?

The supplementary lists `k_a_c2_msun_range` (≈1e11–1e13 M☉ at z=0).

- Is k_A the cluster kinetic energy divided by c²: K/c² = (3/2) m_A σ_v² / c²?
- Or a different quantity (sub-component kinetic energy, quadrupole moment, etc.)?
- What observational proxy determines k_A?

**Why it matters:** The 100× k_A range drives the 94.7× β_q spread (Section K). An independent physical definition constrains β_q directly.

---

## Q16: Is k_A fixed by theory or a free parameter?

We test k_A_indep from Press-Schechter + virial with α fixed only at z=0 to the CSV value (not fit to H(z)).

- Should k_A be fixed from cluster observations before fitting β?
- Or is it a free parameter like β_d, β_q?
- If fixed: which formula and priors?

---

## Q17: D(z) schedule origin

D_required(z) / D_csv(z) ≠ 1 at high z at fixed β=4.5, β_q=18.0.

- Are D(z) values from a physical scaling relation or chosen to match H_obs(z)?
- At z=8.5, is the large D_required/D_csv ratio expected?

---

## Q18: k_A independence and quadrupole dominance

When ε_q ≫ 1, Φ(z)/Φ(0) ≈ [D(0)/D(z)]⁴ — weakly dependent on k_A and β.

- Is quadrupole dominance intended?
- Is there a regime where dipole and monopole matter?

---

## Email block (English, soft framing)

Subject: Constructive question on k_A(z) in Table A1 workflow

> Dear Dr. Buckholtz,
>
> In our internal audit of the Table A1 H_MULT implementation, we found that the bridge retrodiction depends strongly on how k_A(z) and D(z) are specified, while β values appear largely degenerate in the quadrupole-dominated regime.
>
> The most constructive next step may be to make k_A(z) an independently specified physical input rather than a fitted schedule. Does IDM/MULTING provide an independent rule for k_A(z), or would you be open to testing one using simulations or virial/ICM scaling?
>
> Does k_A represent a physical kinetic-energy parameter that can be estimated independently of H(z), or is it an effective fit coordinate in the current Table A1 workflow?
>
> This is an implementation reproducibility question — not a claim about the full theory.

**Do not send without review.**
