# GVS v13P4 — Real Terminal Loading on Shared M4 Segment

**Status: PARTIAL PASS; conservative fan-in boundary tightened.**

## What happened

v13P3 showed that wire length is the first shared-node physical scaling pressure: a 200 um M4 spine plus 16 empty taps crossed the historical +20 fF v12S shared-node stress envelope, while a 100 um spine remained below it even with many empty taps.

v13P4 replaces an empty tap with a real transistor terminal so that contact/poly layout parasitic is included rather than guessed.

The test structure used:

- 100 um minimum-width M4 shared spine;
- legal M4 -> M3 -> M2 -> M1 via stack;
- local M1 branch;
- physically contacted gate of a `sky130_fd_pr__nfet_01v8`, W=0.84 um, L=0.15 um.

Magic reported **0 DRC errors** and extracted the intended NFET with the correct dimensions.

## Measured capacitance

- bare 100 um M4 spine: 7.610610 fF
- spine + one empty legal tap: 7.963000 fF
- spine + one real W=.84/L=.15 NFET gate tap: 8.317110 fF

Therefore:

- empty routing/tap overhead: +0.352390 fF
- additional real gate/contact layout overhead beyond that empty tap: +0.354110 fF
- total real attachment overhead relative to the bare spine: **+0.706500 fF**

The intrinsic MOS gate capacitance remains in the PDK transistor model used by the original schematic. The number above represents the extra physical layout/contact/interconnect parasitic that schematic-only simulation does not contain.

## Fan-in implication

A simple linear projection using this representative terminal gives:

- 8 similar real attachments on 100 um: about 13.26 fF routing/layout parasitic
- 12: about 16.09 fF
- 16: about **18.91 fF**
- 18: about **20.33 fF**

This is only a first-order projection. Dense taps show some electrostatic shielding/nonlinearity, and capture/run attach to a mix of gate and diffusion terminals of several transistor sizes. Therefore the data does **not** establish 16 as a final universal fan-in limit.

It does establish a useful conservative design direction: **100 um local shared-control segments should stay around the low-to-mid teens of representative real terminals until the larger terminal types are measured.**

## Current problem

The largest capture/run devices have not been characterized physically. In particular, larger PFET gates and W=4/W=12 diffusion terminals could contribute different layout parasitics. The complete run/capture block also has not been placed as one physical structure.

## What is next

1. Measure representative larger gate and diffusion-terminal attachment costs used by capture/run.
2. Build the actual small run/capture local block using the measured mix of terminals.
3. Extract total shared-node parasitic and choose a fan-in that stays below the v12S +20 fF stress envelope with margin.
4. Feed the shared-node PEX plus v13P0 Myelin-edge PEX into the unchanged v12S transient lifecycle.
5. Add hierarchy/buffering only if extracted transient evidence requires it.

No computational architecture change is justified. Short physical shared-control segmentation remains the evidence-supported implementation rule.
