# Current Next Experiment — Physical Direct One-Phase Grammar Reader

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

v13A5 solved the old fixed 0.500 V Grammar-threshold problem with a PVT-tracking equal-total legal-MIM candidate/reference ratio. The physical series-pair extraction and real readout/mismatch data remain preserved under `experiments/v13A5_pvt_tracking_grammar_readout/`.

The final 3-step sound Grammar physical ratio produces roughly 25-30 mV candidate/reference evidence in the real combined mismatch screen, not the artificial ~11 mV low-margin stress that originally motivated unconditional two-phase checking.

## v13A6 simplification

Re-analysis of the preserved latch data shows:

- +/-31 mV single-phase phase-0 decisions: 24/24 correct
- +/-18 mV: 24/24 correct
- +/-11 mV: 22/24 correct -> low-margin one-phase is not universally safe
- final real Grammar ratio (~25-30 mV), combined MIM+MOS mismatch: **24/24 phase-0 decisions correct**

In the final real-swap screen, both full-readout fallbacks occurred in phase 1; phase 0 was already correct.

Therefore the **normal high-margin 3-step Grammar path no longer uses an unconditional two-phase swap reader**.

Selected normal reader concept:
- PFET tail W=1/L=0.3 um
- two PFET differential inputs W=1/L=1 um
- two cross-coupled NFETs W=0.42/L=0.3 um
- two output-reset NFETs
- direct short/symmetric GC/GR routes into the PFET gates

Conceptual reader count: **7 MOS** instead of the 13-MOS two-phase/swap implementation.

Removed from the normal path:
- four input-swap NFETs
- two input-reset NFETs
- X0/X1 sample routing
- PH1 routing
- second local motif replay
- second regenerative comparison

Two-phase self-check is retained as a **margin-tiered safety mode**, not deleted.

## Critical rule

Use one phase only for a representation whose physical evidence class is characterized with adequate margin.

Use two-phase self-check or exact fallback for:
- low/unknown evidence margin;
- drifted/uncharacterized physical structures;
- health/calibration checks;
- analog representations whose margin can approach the known ~11 mV unsafe band.

This makes readout precision adaptive like the rest of the hybrid compiler.

## Next physical experiment

1. lay out the 7-MOS direct reader in Magic;
2. keep GC/GR routes extremely short, symmetric and away from output/control wiring;
3. DRC and extraction; reject DRC-clean layouts with wrong connectivity;
4. connect it to the extracted 10-MIM candidate/reference network;
5. measure direct GC/GR loading and GC<->GR coupling;
6. run TT/FF/SS and combined MIM+MOS mismatch;
7. require zero wrong accepted decisions in the characterized high-margin 3-step Grammar class;
8. measure the **actual one-phase readout energy** rather than dividing the old two-phase number by two;
9. compare reader transistor count, area, evidence-node capacitance and energy against the 13-MOS reader attempt;
10. place the shared reference/direct reader behind the selected eight-way Regional Lease.

## After direct-reader signoff

Test the compiler policy itself:
- high-margin/stable motif -> one-phase local readout
- low-margin/unknown motif -> two-phase self-check
- detected ambiguity/failure -> exact computer path

Then repeat the same idea for image first-look Grammar and local Myelin/reasoning evidence instead of assuming one confidence circuit fits every representation.

## Separate tooling issue

Complete historical-v12S continuous-model signoff remains a separate simulator/model compatibility task. Do not modify solved v12S behavior around that tooling mismatch.
