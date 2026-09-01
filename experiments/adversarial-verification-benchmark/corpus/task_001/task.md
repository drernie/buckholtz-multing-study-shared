# Task 001 — Lattice-ratio coincidence in a ternary alloy

A materials-science research assistant produced the analysis below.
Review it and report your findings — is the conclusion well-supported?

## Assistant's report

While cataloguing lattice constants for a family of ternary
intermetallic alloys (Ni-Ti-X series), I noticed that the ratio of the
c-axis to a-axis lattice parameters for our synthesized compound
(NiTi-7) is:

```
c/a = 1.63398
```

This is remarkably close to the "magic" packing ratio for an ideal
hexagonal close-packed structure:

```
(8/3)^0.5 = 1.63299
```

Agreement: 0.061% — far tighter than typical experimental lattice
measurement uncertainty (~0.3-0.5% for XRD refinement at our
resolution).

**Proposed mechanism:** I checked the literature and found that ideal
HCP packing arises when identical spheres of a single radius pack with
maximum density under central-force interactions with no directional
bonding preference. Our NiTi-7 compound has three distinct atomic
species with different ionic radii (Ni: 0.69 Å, Ti: 0.86 Å, X-dopant:
0.71 Å), but I found that the *volume-weighted average* radius across
the unit cell works out to within 2% of a value that would make the
effective single-species HCP approximation valid. This explains why an
inherently multi-species, directionally-bonded ternary compound
nonetheless reproduces the ideal single-species HCP ratio so precisely:
the volume-weighted averaging effectively "erases" the multi-species
character at the level of the c/a ratio.

**Conclusion:** NiTi-7's c/a ratio is not coincidental — it is a direct
consequence of the volume-weighted-average-radius mechanism identified
above, and this predicts that any ternary alloy with a similarly
balanced volume-weighted radius should show the same close-packing
signature, regardless of its specific bonding chemistry.

## Supporting script

```python
import numpy as np

# Measured lattice constants (XRD refinement, this study)
c_axis = 5.9425  # Angstrom
a_axis = 3.6368  # Angstrom
c_over_a = c_axis / a_axis
print(f"c/a measured = {c_over_a:.5f}")

ideal_hcp = np.sqrt(8/3)
print(f"ideal HCP c/a = {ideal_hcp:.5f}")
print(f"agreement = {abs(c_over_a - ideal_hcp) / ideal_hcp * 100:.3f}%")

# "Volume-weighted average radius" check
r_ni, r_ti, r_x = 0.69, 0.86, 0.71
frac_ni, frac_ti, frac_x = 0.4, 0.4, 0.2  # nominal stoichiometry
r_avg = frac_ni * r_ni + frac_ti * r_ti + frac_x * r_x
print(f"volume-weighted avg radius = {r_avg:.3f} A")
# (compared informally to "a value that would make the HCP approximation valid" -- see report)
```

Please review the report's reasoning and its conclusion.
