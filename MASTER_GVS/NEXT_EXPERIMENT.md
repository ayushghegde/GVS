# Current Next Experiment — Co-placed Physical Coordinate + Regional Lease

## What is already solved

The Regional Event Lease is no longer only a transistor-level concept.

`experiments/v13A1_regional_event_lease/` now has a preferred compact physical implementation:

- exactly 5 intended SKY130 NFETs + one 2x2 um M3 MIM;
- DRC errors: 0;
- full RC extraction completed;
- compact bounding box ~15.52 um x 22.0 um (~341.44 um^2), about 18.5% smaller than the first correct layout;
- TT/FF/SS full-RC 12-hop burst: pass;
- 12/12 mismatch launches: pass;
- 5 mV orthogonal disturbance: blocked;
- deliberately bad 0.74 V partial-coordinate case: only millivolt-class local output;
- true coordinate: full ~0.2 V event passes.

The physical WAKE storage is approximately the intended 20-fF class without a giant ideal capacitor: the 2x2 MIM contributes roughly 9.5 fF intrinsic at the typical cap corner and the extracted WAKE-to-ground network contributes about 9.605 fF of unavoidable routing/device capacitance, plus smaller cross-couplings.

`experiments/v13A2_coordinate_lease_chain/` also shows that a real-SKY130 4T active-low coordinate release can drive the physical lease through a 12-hop burst at TT/FF/SS and 12/12 combined mismatch launches.

## Critical invariant

**Only validated local success may refresh the Regional Event Lease.**

Raw/noisy events, partial coordinates, row-only/column-only activity and unselected regions may not refresh it. DONE/CLEAN may clear it. Exact fallback remains independent.

## What remains

The coordinate release and compact lease have been validated as a chained circuit/PEX pair, but they are not yet one co-placed physical extraction.

### Next physical experiment

1. draw/recover the selected 4T active-low coordinate-release layout;
2. place it directly beside the compact Regional Event Lease;
3. route its PRE output physically into the lease write input;
4. run DRC;
5. extract the **combined** coordinate + lease RC network;
6. confirm all expected devices/nets and no accidental shorts;
7. run true coordinate, row-only, column-only, none and partial-coordinate stress;
8. run TT/FF/SS and combined mismatch;
9. run the 12-hop validated-refresh burst;
10. measure area and compare against separate-cell routing.

If the co-placed cell passes, use it as the local interface between the 16x16 orthogonal event fabric and a small Glyph region/island.

## After that

Connect the selected event output only to **local Grammar/template/Myelin evidence**, not to solved v12S run/capture/dendrite control. One long coordinate should select a local region; related image motifs, sound Grammar events, code motifs or reasoning hops then execute locally before another long selection is paid.

The complete historical v12S lifecycle should be re-signed only when a simulator/model path is available that can parse the continuous SKY130 deck used by the historical baseline. The current Linux ngspice build can run device-specific models for physical sub-block experiments but cannot parse that newer continuous deck. The unchanged v12S control fails the same way under the stripped legacy route, so do not redesign v12S around this tooling mismatch.
