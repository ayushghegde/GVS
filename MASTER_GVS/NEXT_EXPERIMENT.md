# Current Next Experiment — Physical PEX of the Regional Event Lease

## Circuit-level problem now solved
v13A required a cheap local state that amortizes one long coordinate selection across several local operations.

`experiments/v13A1_regional_event_lease/` now provides a real-SKY130 transistor-level candidate:

- 20 fF regional wake/lease capacitor
- minimum 0.42/0.15 um write NFET
- minimum 0.42/0.15 um validated-success refresh NFET
- W=1/L=8 um weak inactivity-leak NFET at ~0.40 V gate bias
- minimum 0.42/0.15 um DONE/CLEAN clear NFET
- minimum 0.42/0.15 um local event-gate NFET

It passed the 12-hop stretch case at TT/FF/SS and 4 mismatch launches per corner: 15/15 runs total. It also rejected the safe 5 mV orthogonal disturbance and reduced a deliberately bad 0.74 V partial-coordinate case to only millivolt-class local event output.

The selected 20 fF circuit costs roughly 38-40 fJ for coordinate write plus ~7-47 fJ for eleven validated refreshes depending on corner. This is small relative to repeatedly paying the extracted ~0.68 pJ long 16x16 coordinate selection.

## What remains
The current unknown is **physical layout**, not circuit concept.

### Next physical experiment
1. draw the selected 5-NFET + 20 fF lease in Magic using the supplied SKY130A technology;
2. keep the 20 fF storage local and avoid long coupling into sensitive v12S nodes;
3. run DRC;
4. extract actual C/R and device dimensions;
5. inspect clear-transistor charge-injection/parasitic coupling around WAKE_TRACE;
6. replace the schematic 20 fF/lumped parasitics with extracted PEX;
7. rerun TT/FF/SS + mismatch;
8. connect one physical 4T coordinate-release cell -> regional lease -> local event gate;
9. integrate that chain with the complete v12S lifecycle;
10. verify error/invalidation/exact fallback remain independent of the lease.

## Acceptance conditions
- true coordinate opens the region;
- row-only / column-only / no coordinate cannot open it;
- 5 mV-class orthogonal-wire disturbance cannot open it;
- partial/bad coordinate cannot become a full local event;
- at least four local operations survive after one long selection;
- 12-hop repeated reasoning remains a stretch target when validated local hops refresh the lease;
- DONE/CLEAN clears the region before unrelated work;
- PVT/mismatch remain correct with extracted parasitics;
- total lease overhead remains much smaller than the long selections it avoids.

## Fallback if 20 fF is too small after PEX
Increase storage to 30-40 fF. Do not redesign the architecture merely to defend the smallest capacitor.
