# v13Q1c Aperture Transient Status

**Status: TOOL-BLOCKED / NOT A CIRCUIT FAIL.**

The physical wall-aperture geometry and real SKY130 NFET placement from v13Q1a/v13Q1b remain valid evidence. The next requested transient battery is not signed off because the locally supplied ngspice source builds revision 26, while the current SKY130 combined model library does not parse successfully even on its own distributed `continuous/test.spice` under that simulator.

Observed control check:
- supplied ngspice: revision 26;
- SKY130 distributed parser test: fails before evaluating the aperture circuit, with undefined model-parameter symbols in the current combined deck;
- therefore no TT/FF/SS aperture result from this binary is accepted.

A newer simulator is required before claiming ON resistance, OFF leakage, low-swing delay, switching energy, PVT or mismatch.

This does **not** demote the v13Q physical geometry results:
- remote wall NFET layout is 0 DRC;
- connectivity is `NEIGHBOR <-> NFET <-> CELL` controlled by `AP_GATE`;
- moving the NFET to the cell boundary removed reported direct switch coupling into GC/GR at Magic extraction precision.

No toy MOS model is substituted and no fake transient PASS is recorded.
