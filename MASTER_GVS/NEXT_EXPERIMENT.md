# Current Next Experiment — Real Glyph Work Behind the Eight-Way Local Lease

## What is already solved

The selected compact physical locality interface (`experiments/v13A3_physical_locality_interface/`) is:

`ROWB/COLB -> 4T coordinate release -> physical PRE handoff -> 5T Regional Event Lease + 2x2 MIM`

Corrected physical core device count:
- **7 NFET + 2 PFET + 1 MIM**;
- 0 DRC errors;
- ~30.02 um x 22.0 um = ~660.44 um^2;
- TT/FF/SS and 12/12 combined mismatch pass.

`experiments/v13A4_shared_local_group/` now proves that the same interface can serve **eight isolated local event paths**:

- eight-way physical layout remains in the same ~30.02 um x 22.0 um bounding box;
- 14 NFET + 2 PFET + 1 MIM extracted total;
- DRC = 0;
- TT/FF/SS pass;
- row-only / column-only / none / partial-coordinate cases blocked;
- 12/12 mismatch launches pass;
- weakest SS-mismatch WAKE at event 12 ~1.0166 V;
- active local events remain ~0.2 V;
- inactive outputs remain microvolt-class;
- DONE/CLEAN clears the shared lease.

Ground-referenced WAKE-network capacitance proxy grows from ~9.625 fF for one path to ~13.961 fF for eight paths. The extra capacitance remains acceptable and partly contributes useful lease storage when validated refresh is present.

At TT, moving from four physical paths to eight raises coordinate-write + eleven-refresh energy only from ~99.7 fJ to ~106.8 fJ (~7.2%) while doubling path count.

A 16-gate electrical loading screen also passes SS and four SS-mismatch launches, so the current limit is physical packing/routing rather than WAKE electrical drive. Sixteen-way is not selected yet because eight-way already fits in existing whitespace with no bounding-box growth.

## Current selected local-group size

**Eight nearby event paths per physical Regional Lease** is the current default physical granularity.

This is not a rigid architectural constant. The future physical-cost-aware compiler may choose smaller/larger groups when measured workload reuse, area, communication and fallback cost justify them.

## Critical invariant

Only **validated local success/winner state** may refresh the Regional Lease. Raw sensory activity, noise, incomplete coordinates and unselected regions may not refresh it. Exact fallback remains independent.

## Next problem

The eight paths used in v13A4 are deliberately simple pass/isolation loads. The next question is whether the same locality advantage survives **real Glyph computation**.

### Next experiment

Use the old proven hybrid mechanisms rather than inventing a new compute block:

1. recover the v12N Grammar Cell and/or v12M static-template/Myelin evidence primitive from the preserved archives;
2. place a small number of these real evidence structures behind several of the eight leased paths;
3. keep each evidence source isolated;
4. keep analog evidence/competition local to the group;
5. allow only a robust validated local winner to refresh WAKE;
6. DRC/extract the local evidence wiring where practical;
7. compare exact/partial motif separation with and without locality-interface loading;
8. measure whether inactive local structures remain quiet;
9. compare area/event energy against selecting each structure independently;
10. retain exact escalation for ambiguous/low-margin cases.

### First preferred workload

Start with the **v12N sound Grammar primitive**, because sound already showed strong local 3-step motif repetition and v13A showed Grammar grouping is valuable as communication compression as well as recognition. After that, test image first-look Grammar and local Myelin/reasoning reuse.

## Separate tooling issue

Complete historical-v12S continuous-model signoff remains blocked by the current Linux ngspice parser/model compatibility. Do not redesign the solved v12S tile around that tooling issue. Physical sub-block experiments continue with the device-specific SKY130 models that are working correctly.
