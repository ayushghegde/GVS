# Neural Glyph v13L1a — Physical Differential-Service Geometry

**Verdict: PHYSICAL GEOMETRY PASS.** Real SKY130 Magic layout/extraction confirms that service routing geometry strongly controls differential coupling into the weak Grammar pair. Orthogonal routing makes the extracted Nerve/Artery coupling equal on GC and GR in this test; an intervening shield removes direct service-to-weak capacitance terms at extractor resolution. A deliberately one-sided parallel layout is 0-DRC but badly asymmetric and is rejected.

## Evidence class
- real SKY130A Magic technology: `sky130A.tech` version reported by Magic as `1.0.602-0-gf3c505b`;
- Magic 8.3.681 source built locally in batch/non-Tcl mode;
- real Magic DRC and `.ext` parasitic extraction;
- metal-geometry experiment only: no MOS/MIM reader attached yet;
- no ngspice transient/PVT claim in this stage.

Magic `.ext` capacitance values are in attofarads; results below are converted to femtofarads.

## Why this experiment was run
v13L0 introduced **Differential Service Coupling (DSC)**: the dangerous service disturbance for Grammar is the mismatch between coupling into candidate `GC` and reference `GR`, not common-mode coupling alone.

v13L1a asks whether that metric appears in real SKY130 extraction and whether geometry can suppress it without adding control logic.

## Common weak-pair geometry
All variants use:
- `GC`: metal2, 100 um x 0.5 um;
- `GR`: metal2, 100 um x 0.5 um;
- 2.0 um edge-to-edge separation between the weak rails;
- separate `NERVE` and `ARTERY` service nets;
- no vias connecting services to weak rails.

The test is intentionally long enough to make coupling measurable. It is a geometry screen, not the final cell dimensions.

## Variant A — one-sided parallel service routing
Geometry:
- `NERVE` on metal3 directly above `GC` for 100 um;
- `ARTERY` on metal3 parallel and closer to the GC side than GR.

DRC: **0 errors**.

Extracted direct coupling:
- NERVE -> GC: **4.3095 fF**;
- NERVE -> GR: no direct term reported -> normalized asymmetry treated as **1.000** for this screen;
- ARTERY -> GC: **0.944026 fF**;
- ARTERY -> GR: **1.139590 fF**;
- ARTERY normalized asymmetry: **-0.093858** (~9.39%).

### Result
**REJECT.** DRC-clean does not mean electrically safe. A one-sided parallel service route can create multi-fF coupling and strong physical-side preference.

This directly validates the repository's rule that extracted topology/parasitics, not DRC alone, are authoritative.

## Variant B — orthogonal service routing
Geometry:
- GC/GR remain horizontal on metal2;
- NERVE and ARTERY cross them vertically on metal3 at separate x positions.

DRC: **0 errors**.

Extracted coupling:
- NERVE -> GC: **0.127589 fF**;
- NERVE -> GR: **0.127589 fF**;
- ARTERY -> GC: **0.127589 fF**;
- ARTERY -> GR: **0.127589 fF**.

Normalized asymmetry for both services: **0.000000** at reported extraction precision.

Relative to the rejected NERVE parallel case, direct NERVE coupling to GC drops from 4.3095 fF to 0.127589 fF, about **97.0% lower**, while also becoming matched between GC and GR.

### Result
**KEEP.** Orthogonal crossing is a strong default when a service must pass near a weak differential pair.

## Variant C — shielded service routing
Geometry:
- GC/GR on metal2;
- continuous `SHIELD` on metal3 covering the weak-pair region;
- NERVE and ARTERY on metal4 above the shield.

DRC: **0 errors**.

Extraction reports:
- GC <-> SHIELD: 9.9659 fF;
- GR <-> SHIELD: 9.9659 fF;
- NERVE <-> SHIELD: 10.4761 fF;
- ARTERY <-> SHIELD: 13.0924 fF;
- no direct NERVE->GC, NERVE->GR, ARTERY->GC or ARTERY->GR capacitance terms at extractor resolution.

### Result
**KEEP selectively.** The shield converts the service interaction into shield coupling instead of direct weak-node coupling in this extraction. It is stronger than orthogonal routing but consumes a metal layer/area and heavily couples the shield itself, so it should be used where the weak-margin value justifies the routing cost.

## Physical decision
v13L now has a concrete service-routing hierarchy near weak differential evidence:

1. **avoid long parallel one-sided service routes** beside GC/GR;
2. prefer **orthogonal crossing** for ordinary low-swing Nerve/Charge-Artery transit;
3. use an **intervening shield** when service density, parallel run length or extracted asymmetry is too high;
4. sign off candidate-side and reference-side coupling separately;
5. use normalized DSC asymmetry together with the actual Grammar margin;
6. do not add a scheduler/ADC/calibration controller merely to compensate for bad geometry.

This is the same design philosophy as v13K: solve ordinary interference with voltage-domain and geometry separation before adding timing/control rules.

## Relationship to the hollow / inside-out architecture
This result improves the hollow interpretation:
- weak Grammar/Tri-Wall evidence should occupy a protected computation skin;
- Nerve and Charge Artery should cross weak regions orthogonally or travel behind a shield/service face;
- high-swing VDD/config/test should remain farther away in the robust facade/backside domain;
- framework ribs can carry services, but they may not run arbitrarily parallel to weak evidence just because the structure is hollow.

The result supports the *physical organization* of inside/outside surfaces; it does not prove literal active inner-wall fabrication.

## What is still missing
v13L1a is not the full Neurovascular Cell Slice. It does not yet include:
- the legal 10-MIM Grammar array;
- the selected body-tied 10-MOS two-phase reader;
- recovery contact/lifecycle signal;
- combined MIM+MOS mismatch;
- TT/FF/SS transient operation;
- event/recovery energy.

## Next — v13L1b integrated physical slice
Use the **orthogonal layout as the low-cost baseline** and the **shielded layout as the high-protection variant**. Attach the real 10-MIM Grammar candidate/reference network and selected 10-MOS reader, then rerun extraction and the full electrical battery.

Acceptance remains zero wrong robust accepts. If added MIM/reader loading turns the currently matched orthogonal coupling into material differential asymmetry, inspect placement first; do not redesign Grammar merely to tolerate a poor layout.
