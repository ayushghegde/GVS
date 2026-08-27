# Current Next Experiment — v13T4 Integrated Adaptive Tissue Physical Closure

## Goal
Physically close the first adaptive General Reserve Cell together with a real stateful Grammar neighbor, Relay neighbor and the v13S venous recovery hierarchy.

## Required slice
- preserved weak GC/GR Grammar evidence pair;
- one Relay ECC;
- one Grammar/state ECC;
- one General Reserve ECC with two Expression Patch selectors;
- one fast and one slow Role Pressure storage path or equivalent physically measurable two-timescale implementation;
- hysteresis/dwell/fatigue implemented with the minimum local analog/state hardware justified by measurement;
- break-before-make patch isolation;
- Local Venule -> Charge Artery -> regional reservoir -> battery/collector equivalent;
- boundary communication and role-control placement.

## Battery
1. Magic DRC and extracted connectivity/RC.
2. Role Pressure accumulation/leak on fast and slow paths.
3. Verify noisy pressure cannot cause rapid patch thrashing.
4. Patch A -> isolated -> Patch B handoff with zero make-before-break overlap.
5. Old patch residual state -> Local Venule while new patch operates.
6. Neighboring Grammar/Relay computation during role change.
7. Live-state recovery remains blocked.
8. Venule/Artery/reservoir ripple during role-change bursts.
9. TT/FF/SS.
10. Independent mismatch.
11. stuck patch-select, stuck pressure, stuck venule outlet faults.
12. total area/capacitance/energy versus fixed differentiated and universal-cell controls.
13. zero wrong robust accepts; uncertainty may remain unresolved.

## Tooling
Use a Linux simulator demonstrably compatible with the current SKY130 model deck. The uploaded ngspice 47 archive is the official Windows binary package and is preserved as tool provenance, but this Linux runtime cannot execute it without a Windows compatibility layer. Do not substitute a toy MOS model for signoff.

## Acceptance
- adaptive reserve materially reduces overload without high re-role rate;
- no noisy role-pressure oscillation;
- break-before-make prevents state mixing;
- old-patch recovery does not block new-patch work long enough to erase the adaptation benefit;
- role controls/venules do not materially disturb GC/GR;
- recovery failure changes energy only, not correctness;
- adaptive reserve remains cheaper than making ordinary cells universal.

## After pass
Promote v13S/v13T adaptive differentiation into MAIN_ARCHITECTURE, then test a multi-region reasoning trace where reserve cells, cell-as-wire transport, population confidence, relation/constraint reasoning and venous recovery operate together.
