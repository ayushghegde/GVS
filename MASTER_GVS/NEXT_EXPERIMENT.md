# Current Next Experiment — Physical PVT-Tracking Grammar Block Behind the Eight-Way Lease

## What is already solved

The selected physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

v13A4 physically proved the eight-way group at TT/FF/SS, false-coordinate cases and 12/12 mismatch launches.

v13A5 then placed the old v12N 3-step sound Grammar computation behind that locality path and found a real old-design problem:

- TT exact motif ~0.52219 V; partial ~0.49479 V
- SS exact ~0.53044 V; partial ~0.50030 V

Therefore the historical fixed 0.500 V Grammar threshold is not a safe physical decision boundary under the real MIM corner spread.

## Selected v13A5 electrical solution

### Equal-total legal-MIM ratio

Candidate:
- 3 full driven 2x2 um MIMs
- one physical 2x2 + 2x2 MIM series pair to ground
- 5 physical MIM devices total

Shared reference:
- 2 full driven 2x2 um MIMs
- one physical driven 2x2 + 2x2 series pair
- 1 full 2x2 um MIM to ground
- 5 physical MIM devices total

A real Magic extraction of the two-MIM series pair is preserved in `experiments/v13A5_pvt_tracking_grammar_readout/physical/`.

With real comparator input devices attached, nominal evidence margins remain roughly:
- exact: +26.9 to +27.4 mV
- partial: -24.3 to -25.7 mV

Independent MIM mismatch plus SKY130 transistor mismatch did not collapse the ratio in the current screen.

### Self-checking readout

Selected latch core:
- PFET tail W=1/L=0.3 um
- PFET differential pair W=1/L=1 um
- cross NFETs W=0.42/L=0.3 um
- 2 fF output storage

Real minimum-NFET input swapping performs two phases:
1. candidate/reference normal
2. reset
3. candidate/reference swapped

A valid decision must reverse physical latch polarity. Same-side preference or weak resolution is fallback.

Real-swap 7 ns/phase combined mismatch screen:
- 24 exact/partial cases across TT/FF/SS
- correct accepts: 22
- fallbacks: 2
- wrong accepts: **0**

## Honest readout energy

The robust readout is tens of femtojoules, not sub-fJ:

- TT: ~46.7 fJ exact / ~52.7 fJ partial
- FF: ~33.4 / ~39.5 fJ
- SS: ~58.5 / ~63.6 fJ

The Grammar/reference capacitor-event work itself remains only a few tenths of a femtojoule. Regenerative readout dominates.

Therefore Grammar must not replace the warm static selector merely because its capacitive motif core is cheap. It is worthwhile when the motif event also avoids larger downstream work or one/more long physical selections (~0.68 pJ each in the measured 16x16 fabric).

## Next physical experiment

The current unknown is **layout interaction**, not the electrical ratio concept.

1. physically lay out one 5-MIM candidate using only legal 2x2 um MIMs;
2. physically lay out the 5-MIM shared reference beside it;
3. compact them while keeping series-pair midpoint parasitics controlled;
4. DRC and extract the combined candidate/reference network;
5. measure unwanted candidate-reference and neighboring-MIM coupling;
6. replace the proxy capacitor matrix with the full extracted network and verify the exact/partial differential margins;
7. physically place the selected latch-D plus real swap/reset NFETs beside the MIM block;
8. run combined PEX PVT + mismatch + two-phase self-check;
9. place the resulting shared reference/readout beside the selected eight-way Regional Lease;
10. measure area and full event energy per useful motif.

## After physical two-phase signoff

Only then test the optional old-v11U-inspired optimization:

- self-check/calibrate comparator offset slowly or during idle;
- remember the slow offset state regionally;
- use one phase on normal events when calibration is trustworthy;
- periodically re-run the two-phase check and fall back immediately on drift/uncertainty.

Do **not** replace the safe two-phase baseline with calibration until calibration shows zero wrong accepted decisions across mismatch and PVT drift.

## Separate tooling issue

Complete historical-v12S continuous-model signoff remains a separate simulator/model compatibility task. Do not modify v12S around that tooling mismatch.
