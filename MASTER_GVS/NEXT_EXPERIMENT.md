# Current Next Experiment — v14S1 Physical 64-Cell Tile Closure

Do not invent another semantic-cell topology unless v14S fails.

## Goal
Close one complete 64-cell Shared-Threshold Polarized-Link Cell (STPLC) tile against a physically specified MOS reference.

## Required work
1. Build/calibrate a two-terminal HZO/FTJ polarized-link compact model with OFF/WEAK/STRONG states and real read/program I-V behavior.
2. Build/calibrate one Ag/HfO2-class volatile threshold-switch model including threshold/hold distribution, delay, leakage, recovery and stress.
3. Keep the v14R extracted small-node geometry and add realistic device/contact/interconnect capacitance.
4. Simulate 64 cells with sparse degree-5 links and real transient pulse propagation, not only score-based Monte Carlo.
5. Sweep process/device envelopes plus local mismatch/variation.
6. Run read-disturb and cumulative half-select programming stress.
7. Implement one shared programming rail/driver group and count area/energy amortized per cell.
8. Build a physically laid-out MOS comparison implementing the same receive/integrate/fire function and degree-5 programmable relation interface.
9. Compare complete tile: area, event energy, propagation delay, programming energy, static leakage, device count, wire load and yield sensitivity.

## Acceptance
Promote only if all are met together:
- >=99% single-stage decision accuracy at the selected practical variation envelope;
- >=99% eight-stage route success after calibrated transient modeling or a correction mechanism that costs less than the lost margin;
- no meaningful distractor firing under background/weak inputs;
- read disturb acceptable for expected inference count;
- half-select cumulative disturb acceptable for expected training count;
- shared periphery does not erase the device-count/area advantage;
- total tile energy-delay product beats the physically laid-out MOS reference;
- common semantic cell remains MOS-free.

## Failure rule
If the polarized link cannot provide enough low-voltage conductance contrast, test a simpler two-terminal polarized resistive link before adding selectors. If the shared threshold switch is the problem, improve only that single switch using seed/guided-gap/cation-limiter geometry. Do not return to one active switch per branch unless a full tile comparison proves it cheaper.
