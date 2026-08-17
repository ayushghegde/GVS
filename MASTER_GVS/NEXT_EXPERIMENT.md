# Current Next Experiment — One Physical Lease Serving a Small Local Group

## What is already solved

The physical locality interface is now one co-placed and extracted layout:

`ROWB/COLB -> 4T coordinate release -> physical M4 PRE handoff -> 5T Regional Event Lease + 2x2 MIM -> local event`

Selected compact interface (`experiments/v13A3_physical_locality_interface/`):

- 0 DRC errors;
- expected 9 NFET + 2 PFET + 1 MIM extracted;
- compact bounding box ~30.02 um x 22.0 um = ~660.44 um^2;
- ~21% smaller than the first roomy co-placement;
- TT/FF/SS pass;
- row-only / column-only / none / partial coordinate blocked;
- 12/12 simultaneous coordinate+lease mismatch launches pass;
- weakest SS-mismatch WAKE at event 12 ~0.9905 V;
- local events remain ~0.2 V;
- DONE/CLEAN clears the lease.

## Critical invariant

Only **validated local success/winner state** may refresh the lease. Raw/noisy events never refresh it. Exact fallback remains independent.

## Next problem

A single Regional Lease is useful only if it can serve several nearby local operations. If every Grammar/template/Myelin path needs its own coordinate+lease interface, area and wiring duplication return.

The next experiment therefore asks:

> How many nearby local event gates can one physical WAKE node drive before added gate/wire capacitance consumes the lease margin or costs more area/energy than it saves?

This is the first real "local group" test. A local group simply means a few nearby Glyph structures that share one long-distance selection but still perform their own local computation.

## Next experiment

1. use the selected compact v13A3 interface unchanged;
2. add 4 local minimum-size event gates whose gates share WAKE;
3. give each path its own low-voltage EVT input and OUT node;
4. run DRC and full RC extraction;
5. measure added WAKE capacitance and local-path coupling;
6. run TT/FF/SS and mismatch;
7. verify all four paths can pass ~0.2 V events while selected;
8. verify inactive paths do not fight active sources;
9. verify incomplete coordinates keep every local path blocked;
10. verify DONE clears all paths;
11. if 4-way passes comfortably, test 8-way fanout;
12. compare interface area/energy per local path against duplicating four coordinate+lease interfaces.

## Acceptance rule

Keep shared local fanout only if:

- it preserves the v13A1/v13A3 lease margin;
- it does not create source contention like the rejected early shared-sound selector;
- inactive local sources are isolated;
- per-path area and long-wire energy fall materially;
- no correctness dependency is added to exact fallback.

## Separate tooling issue

A complete historical-v12S lifecycle rerun remains blocked by the current Linux ngspice build's inability to parse the continuous SKY130 deck used by the historical baseline. Do not redesign v12S around that simulator mismatch. Physical sub-block work continues with the device-specific SKY130 models that are working correctly.
