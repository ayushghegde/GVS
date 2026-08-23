# Neural Glyph v13L pre-integration — Reader-Terminal Differential Service Coupling

**Verdict: PHYSICAL PRECHECK PASS for orthogonal service routing; REJECT one-sided parallel routing. Full v13L1b remains open.**

## What happened
v13L1a proved the Differential Service Coupling (DSC) rule on long generic weak rails. This experiment asks a narrower question before the full MIM+MOS integration: does the rule still hold when the weak-pair geometry is changed to the **actual GC/GR metal2 terminal dimensions used by the selected body-tied 10-MOS reader generator**?

The selected reader generator defines the two weak input terminals as metal2 bars:
- GC: x=62..92, y=930..1580;
- GR: x=462..492, y=930..1580.

Those dimensions were copied exactly into three new SKY130A Magic layouts. No transistor or MIM device was invented or altered in this precheck.

## Evidence class
- Magic 8.3.681 built from the uploaded source archive;
- SKY130A `sky130A.tech` from the uploaded PDK files;
- real Magic DRC and parasitic extraction;
- all variants: 0 DRC errors;
- reader-terminal geometry is real from the selected repository generator;
- **not** yet the complete 10-MOS+10-MIM circuit, so no new TT/FF/SS or mismatch claim is made here.

Magic `.ext` coupling values are converted from attofarads to femtofarads in `summary.csv`.

## Variant 1 — orthogonal baseline
Nerve and Charge Artery cross both GC and GR on metal3.

Extracted direct coupling:
- NERVE->GC: 0.0662631 fF
- NERVE->GR: 0.0663032 fF
- normalized DSC magnitude: ~0.0303%
- ARTERY->GC: 0.0646362 fF
- ARTERY->GR: 0.0646763 fF
- normalized DSC magnitude: ~0.0310%

**KEEP.** The actual reader-terminal geometry remains extremely well matched under orthogonal crossing.

## Variant 2 — deliberately one-sided parallel Nerve
The Nerve runs parallel directly above the GC side. The layout is still DRC-clean.

Extracted direct coupling:
- NERVE->GC: 0.199795 fF
- NERVE->GR: 0.000621399 fF
- normalized DSC magnitude: ~99.38%

The Artery in the same deliberately bad variant is less severe (~5.28% DSC), showing that distance/placement rather than net name controls the result.

Using the existing conservative 72 fF weak-node reference and the preserved 0.2 V Nerve / 90.3 mV Artery swings, 32 aligned Nerve + 32 aligned Artery transitions give an estimated differential kick of ~17.76 mV. That would reduce a 25 mV useful differential to only ~7.24 mV, well below the 18 mV high-margin target.

**REJECT.** DRC-clean parallel placement can destroy the differential margin.

## Variant 3 — shielded compact terminal region
A metal3 shield covers the compact GC/GR terminal region and Nerve/Artery cross on metal4.

Extracted direct service coupling:
- NERVE->GC: 0.00243105 fF
- NERVE->GR: 0.00238195 fF
- ARTERY->GC: 0.00243105 fF
- ARTERY->GR: 0.00238195 fF
- normalized DSC magnitude: ~1.02% for both services.

Absolute direct service coupling is about 27x lower than the orthogonal compact baseline, although the tiny residual terms are not perfectly matched. Under the same 32+32 aligned-transition stress, the estimated differential kick is only ~0.0063 mV.

**KEEP selectively.** Shielding buys much lower absolute coupling but consumes routing resources; orthogonal crossing remains the normal low-cost baseline.

## Problem solved
The main uncertainty after v13L1a was whether its geometry result depended on the artificial 100 um weak rails. It does not. With the selected reader's compact GC/GR terminal geometry:
- orthogonal crossing is still essentially common-mode;
- one-sided parallel routing is still electrically dangerous despite 0 DRC;
- shielding still sharply reduces absolute direct coupling.

So the next full integrated slice can keep the existing Grammar architecture and focus on placement/loading, exactly as v13K requires.

## What is still open
This precheck does **not** close v13L1b because it does not yet instantiate:
- legal physical 10-MIM Grammar array;
- the ten MOS devices themselves;
- recovery contact/lifecycle control;
- full RC of the integrated circuit;
- TT/FF/SS transient operation;
- combined MIM+MOS mismatch;
- readout/event/recovery energy.

## Next
Proceed with the repository's existing `v13L1b Integrated Grammar + Neurovascular Slice` plan using:
1. orthogonal service crossing as the baseline;
2. shielded service routing only as the high-protection comparison;
3. the unchanged selected 10-MIM Grammar + body-tied 10-MOS two-phase reader;
4. extracted GC/GR total loading and DSC as the first failure checks.

If full integration fails, inspect physical asymmetry and added GC/GR capacitance before changing Grammar. Do not add a scheduler, ADC, calibration loop or fixed digital threshold to compensate for a bad layout.
