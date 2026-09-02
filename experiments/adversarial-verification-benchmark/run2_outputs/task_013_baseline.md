# Task 013 — baseline arm output

## Findings

**Verdict: the conclusion is not well-supported.** The report's central argument — that agreement between the two methods rules out a calibration error because "an error... would have to coincidentally affect both methods identically" — is backwards. The two methods do share the calibration identically, by explicit construction (same `ZP = 25.340` applied to both), so agreement between them is not evidence against a zero-point error. It is guaranteed regardless of whether the zero-point is right or wrong.

### Verification performed

I extracted the script and ran it, then added a probe: I varied a hypothetical zero-point error `delta_ZP` from -0.5 to +1.0 mag (a shared additive shift applied to both apparent magnitudes, exactly as the pipeline does) and recomputed both distances.

Result [VERIFIED-BASH]:
```
delta_ZP=-0.50: d_ms=2013.7 pc, d_rrl=2015.5 pc, ratio=0.999113
delta_ZP=+0.00: d_ms=2535.1 pc, d_rrl=2537.4 pc, ratio=0.999113
delta_ZP=+1.00: d_ms=4017.9 pc, d_rrl=4021.5 pc, ratio=0.999113
```

The ratio `d_ms/d_rrl` is exactly invariant to `delta_ZP` — not approximately, exactly, to the last printed digit. This is provable analytically: distance modulus is `mu = m - M`, and since the same `ZP`-derived shift `delta` enters `m_ms` and `m_rrl` additively and identically, it cancels in `mu_ms - mu_rrl`, which is independent of `delta`. A 1-magnitude zero-point bust (a ~150% distance error, taking the cluster from ~2000 pc to ~4000 pc) would leave the two methods in the exact same mutual "agreement" as a perfect calibration.

### What the agreement actually demonstrates vs. what it's being claimed to demonstrate

- **What it shows:** the raw photometry of the main-sequence stars and the raw photometry of the RR Lyrae variables are mutually consistent, given the assumed absolute-magnitude calibrations. That is real, non-trivial information.
- **What it does NOT show:** that the absolute distance scale (i.e., the zero-point itself) is correct. Because both methods route through the identical `ZP`, this specific test has zero statistical power against a shared zero-point error.

This is a textbook non-independence fallacy: "two different physical methods" is not the same as "two methods independent with respect to the error being tested."

### Secondary, lower-priority concerns
- Only 3 RR Lyrae variables — small-N systematic/statistical uncertainty in the P-L fit isn't discussed.
- Neither method's magnitude appears extinction/reddening-corrected.

### What would actually constitute independent confirmation
Calibrate the two methods with genuinely separate zero-points — e.g., anchor one method to an independent absolute scale such as Gaia parallaxes of local calibrator stars, while the RR Lyrae P-L zero point comes from its own independently-calibrated absolute-magnitude relation.

---

**DRAFT CLAIM:** The report's conclusion — that agreement between main-sequence-fitting and RR Lyrae distances constitutes independent confirmation of the cluster distance — is not well-supported, because both methods used the identical photometric zero-point (`ZP = 25.340`) to convert instrumental to apparent magnitudes. Since this zero-point enters both methods' apparent magnitudes additively and identically, it cancels exactly out of the comparison between the two derived distances; a numerical check varying a hypothetical zero-point error from -0.5 to +1.0 mag confirmed the ratio of the two distances stays fixed at 0.999113 regardless of the error size, meaning a 1-magnitude zero-point error (roughly a 150% distance error) would produce the exact same "agreement" as a perfect calibration. The report's claim that "an error... would have to coincidentally affect both methods identically" inverts the actual situation — the shared zero-point makes identical contamination a certainty by construction, not an implausible coincidence. The agreement is real evidence that the two methods' relative photometry and assumed absolute-magnitude calibrations are mutually consistent, but it carries no information about whether the shared zero-point itself, and hence the absolute distance scale, is correct.
