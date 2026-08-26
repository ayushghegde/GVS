# Neural Glyph v13R3 — Physical Differentiated Communication + Recovery Pair

**Verdict: PHYSICAL GEOMETRY PASS / TRANSIENT OPEN.**

This is the first real SKY130 Magic geometry combining a wall communication aperture and a separate post-expiry recovery aperture around a weak differential core proxy.

## Physical structure
Two instances of the recovered real `sky130_fd_pr__nfet_01v8` geometry are used:
1. communication aperture: `NEIGHBOR <-> CELL`, gate `AP_GATE`;
2. recovery egress candidate: `CELL <-> ARTERY`, gate `EXPIRE`.

Weak rails are `GC` and `GR`. The two boundary devices are placed on opposite sides of the cell state bus.

## Magic result
- Magic 8.3.681;
- real SKY130A technology file;
- **0 DRC errors**;
- exactly two NFET child instances;
- intended connectivity preserved.

Extracted direct geometry terms:
- `NEIGHBOR -> CELL`: ~0.016098 fF;
- `ARTERY -> CELL`: ~0.016098 fF;
- `NEIGHBOR -> GC`: ~0.00403226 fF;
- `ARTERY -> GR`: ~0.00403226 fF;
- `GC <-> GR`: ~0.0175439 fF in this proxy geometry.

No corresponding direct `NEIGHBOR -> GR` or `ARTERY -> GC` term was reported at extraction precision.

## Disturbance interpretation
Using the preserved 72 fF screening node only as a simple coupling proxy:
- 0.2 V neighbour event -> ~0.0112 mV one-sided kick;
- 0.0903 V Charge-Artery swing -> ~0.00506 mV one-sided kick.

These are tiny relative to the earlier ~18 mV high-margin evidence screen, but this is not a full Grammar co-layout and does not replace real GC/GR signoff.

## What happened
Putting communication and recovery switches at opposite cell boundaries keeps their individual weak-core couplings extremely small. The geometry is naturally differentiated: a relay-only neighbour does not need its own recovery device merely because the stateful cell has one.

## Problem still open
The NFET used here is not yet sized as a **slow** egress device. The supplied ngspice revision 26 cannot parse the current SKY130 combined model deck even on the PDK's own parser test, so ON resistance, OFF leakage, slow-egress time constant, backflow, TT/FF/SS, mismatch and energy remain open.

No ideal switch or toy MOS model is substituted.

## Decision
- KEEP boundary placement for information and recovery apertures;
- KEEP mirrored service placement around weak differential cores where possible;
- KEEP recovery hardware only on cell roles that justify it;
- DO NOT claim transistor-level SCE closure yet.

## Reproduce
Run `raw/build_sym.cmd` through Magic 8.3.681 with the preserved SKY130A tech file and the existing recovered `nf_cross.mag` primitive.

Evidence class: real Magic DRC/extraction geometry using a real recovered SKY130 NFET layout; not transient PVT closure.
