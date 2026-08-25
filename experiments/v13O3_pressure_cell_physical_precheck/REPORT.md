# Neural Glyph v13O3 — Pressure-Cell Physical Precheck

**Verdict: PARTIAL / PHYSICAL CLOSURE OPEN.**

## Goal
Check whether the new Constraint-Pressure idea can begin from ordinary legal SKY130 structures rather than requiring exotic memory devices.

## What happened
A standalone 2x2 um MIM pressure-capacitor geometry was created and run through Magic 8.3.681 with the local SKY130A technology deck.

Magic reported:
- 0 DRC errors;
- technology `sky130A`, version `1.0.602-0-gf3c505b`;
- an extracted `sky130_fd_pr__cap_mim_m3_1` device.

This supports using a normal MIM capacitor as a local analog persistence/pressure state.

## Problem found
The first standalone top-terminal metal4 route was not actually connected to the extracted MIM top node. Extraction therefore shows `PRESSURE` as a separate node while the MIM top terminal is unnamed (`c1_0_0#`). This is a real layout/connectivity failure even though DRC is clean.

A transistor-level feedback test was also attempted with the supplied ngspice source, but ngspice revision 26 rejected constructs in the current SKY130 combined model deck before the candidate pressure circuit itself was evaluated. No generic MOS model was substituted and no SKY130 electrical PASS is claimed.

## Decision
- KEEP ordinary MIM storage as the preferred pressure-state primitive.
- Treat extracted connectivity, not DRC alone, as the gate.
- Do not redesign the architecture around this routing mistake.
- Do not claim physical pressure-cell closure until a connected terminal geometry and compatible preserved SKY130 simulation flow are rerun.

## Next
Use the known-good MIM terminal/contact pattern from the accepted/recovered Grammar layouts, then build the smallest local violation-charge/leak/feedback slice and run TT/FF/SS plus mismatch if the physical mechanism proves stable.
