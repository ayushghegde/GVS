# Current Next Experiment — v13S4 Adaptive Tissue Physical Closure

## Goal
Physically close the first small v13S tissue using a simulator that correctly supports the current SKY130 model deck.

## Required slice
- common ECC base geometry;
- one Relay ECC;
- one Grammar/state ECC;
- one General Reserve ECC carrying two switchable Expression Patch functions;
- boundary communication aperture;
- normal post-expiry isolation;
- shared Local Venule;
- one deliberately weak venule -> Charge-Artery outlet;
- regional reservoir equivalent and battery/collector load;
- preserved weak GC/GR evidence pair.

## Required battery
1. Magic DRC + extracted connectivity/RC.
2. Contact aperture OFF leakage / ON low-swing event delay and energy.
3. Verify live information cannot enter the venule.
4. After expiry, measure cell -> venule emptying and residual charge versus time.
5. Measure venule -> Charge-Artery flow, regional-reservoir ripple and backflow.
6. Uniform, bursty and aligned expiry stress.
7. Simultaneous information event + neighboring recovery.
8. RPF/General-Reserve role-change disturbance.
9. TT / FF / SS.
10. Independent mismatch screen.
11. Area/device/capacitance comparison against:
    - fixed differentiated v13R cells with direct slow egress;
    - universal-cell control;
    - v13S common-base + patch + venule tissue.

## Acceptance
- zero wrong robust accepts;
- uncertain population may remain unresolved rather than guess;
- live-state recovery remains blocked;
- recovery failure changes energy only, not correctness;
- boundary venule does not materially reduce GC/GR margin;
- two-stage recovery empties the cell sooner while not increasing artery/reservoir stress versus direct tau=8 after real device sizing;
- General Reserve adaptation materially reduces overload without high switching/support cost;
- Expression Patches and shared venule reduce total physical cost after their interfaces are counted;
- no per-cell microcontroller, ADC or recovery scheduler is added.

## Tooling
Prefer current ngspice (official release 47 as of August 2026) or another simulator demonstrably compatible with the same SKY130 model deck. Tool substitution must be validated on the PDK's own test deck before GVS results are accepted.

## If it passes
Promote v13S adaptive differentiation + two-stage venous hierarchy into `MAIN_ARCHITECTURE.md`, then scale to a multi-region intelligent trace rather than another isolated primitive.

## If it fails
Keep the failure local: coarsen patch roles, reduce reserve adaptability, change venule group size/time constants, or revert affected cell types to v13R direct SCE. Do not undo proven Grammar, cell-as-wire, population confidence or neurovascular isolation merely to rescue a bad support layout.
