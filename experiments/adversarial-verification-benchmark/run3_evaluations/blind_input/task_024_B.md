# Task 024 — treatment arm output (FL protocol)

## FL Standard-Ladder Review — Task 024

### 1. Falsifiable claim
The RMS-based drift detector (threshold=0.15) is well-calibrated and deployment-ready because only 0.02% of windows over 6 months were flagged. Bundles a specificity claim (weakly addressed) and a calibration/deployment-readiness claim (zero evidence).

### 2. Controls
**Positive control absent.** Nothing demonstrates the detector flags a known-bad window. **Negative control implicit and unverified** — the 6-month dataset is used as its own negative-control population without confirming it's actually mostly drift-free.

### 3. Red flags
- Silently-fixed threshold=0.15, no derivation.
- Circular reasoning: "low flag rate => well calibrated" only follows if the data is already known mostly drift-free — the thing being established.
- Masking bug verified real: nanmean of all-NaN window (known, logged dropout event class per report's own context) returns NaN, NaN>threshold=False — every dropped window silently joins "not drifting."

### 4. Executed checks
- Confirmed the NaN-masking bug directly: `flag_drift(all-NaN window) = False`, RuntimeWarning "Mean of empty slice."
- Positive/negative control the report never ran: synthetic normal window (RMS=0.049, not flagged) vs synthetic drift window (RMS=0.307, flagged) — confirms detection logic isn't dead code, ruling out the most catastrophic failure, but this is exactly the check the original report skipped.
- Could not quantify the real dropout rate's effect on the actual 0.02% figure (marked UNKNOWN, not asserted) — but the bias direction (toward looking safer than it is) is confirmed structural.

### 5. Verdict
**Not supported — REPEAT, not REJECT.** Detection logic isn't fundamentally broken, but the "well-calibrated, ready for deployment" conclusion isn't backed: no positive control distinguishes "rarely fires" from "silently never fires correctly," and dropout windows are counted as confirmed-normal rather than unmeasured.

---

### DRAFT CLAIM
A signal-processing pipeline flags a window as "drifting" if sqrt(nanmean(window^2)) exceeds a hardcoded threshold of 0.15. Applied to 6 months of turbine data, 0.02% of windows were flagged, concluded well-calibrated and deployment-ready. Independent execution confirms: known network-hiccup dropouts arrive as all-NaN windows; nanmean of an all-NaN array returns NaN, and NaN>threshold evaluates False in NumPy — so every dropped window is silently scored "not drifting," mixing "confirmed normal" with "unmeasured." Separately, no positive control was run anywhere — nothing demonstrates the detector fires on genuine drift, so a miscalibrated threshold would produce an identical low flag rate. A synthetic check (executed for this review) confirms the comparison logic can fire given large enough input, ruling out total dead-code failure, but the calibration/deployment-readiness claim remains unsupported pending a positive control, explicit dropout handling, and a justified threshold.
