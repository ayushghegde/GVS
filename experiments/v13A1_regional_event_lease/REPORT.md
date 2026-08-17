# Neural Glyph v13A1 — Regional Event Lease

**Verdict: PARTIAL PASS — physical lease layout/PEX, PVT, mismatch and disturbance screens pass; complete historical-v12S signoff is still blocked by simulator/model compatibility.**

## What problem this solves

v13A showed that cheap physical/event computation can lose its advantage if every local motif or reasoning hop repeatedly pays the millimeter-scale inter-island selection cost. The extracted 16x16 GTI row+column selection is about 0.68 pJ per long selection.

The Regional Event Lease remembers **this region is already selected** for a short useful burst, so related Grammar/template/Myelin/reasoning work can remain local rather than recharging the long fabric each time.

This is not a replacement for v12S run/capture, soma competition or exact fallback. It is a local communication-state primitive around those mechanisms.

## Design lineage

The circuit deliberately reuses older Glyph mechanisms:

- v12D: firing charge as short-lived electrical memory;
- v12J: stop inactive/wrong evidence at the source;
- v12P: physical lease/hotness rather than continuous bookkeeping.

Only **validated local success** may refresh the lease. Raw/noisy activity must never refresh it. DONE/CLEAN hard-clears it, and exact fallback remains independent.

## Selected circuit

- coordinate-write NFET: W=0.42 um, L=0.15 um;
- validated-success refresh NFET: W=0.42 um, L=0.15 um;
- weak inactivity leak NFET: W=1 um, L=8 um, gate biased near 0.40 V;
- DONE/CLEAN clear NFET: W=0.42 um, L=0.15 um;
- local low-voltage event-gate NFET: W=0.42 um, L=0.15 um;
- one physical 2x2 um `sky130_fd_pr__cap_mim_m3_1` on WAKE.

The original schematic target was about 20 fF of wake storage. The selected physical layout reaches approximately that class **without a dedicated 20 fF ideal capacitor**: at the typical linear-cap corner the 2x2 MIM is about 9.5 fF intrinsic (area + perimeter), while the compact extracted WAKE network contributes about 9.605 fF of explicit WAKE-to-ground parasitic capacitance, plus smaller cross-couplings. The storage is distributed, so this is an engineering interpretation rather than an exact single-C value.

This is a useful case where unavoidable physical capacitance performs useful state storage instead of being treated only as waste.

## Physical layout and compaction

The first correct physical lease (`v3`) was DRC-clean and extracted as exactly five intended NFETs plus one 2x2 MIM, but it was unnecessarily loose.

A compaction experiment then reduced empty vertical spacing without changing topology.

- original bounding box: ~15.52 um x 27.0 um = ~419.04 um^2;
- selected compact bounding box: ~15.52 um x 22.0 um = ~341.44 um^2;
- bounding-box reduction: **~18.5%**.

The first compact attempt is explicitly rejected: it had zero DRC errors but extraction showed WAKE/OK and capacitor connectivity were wrong because routing was moved without moving referenced transistor subcells. This is preserved as evidence that DRC-clean does not prove topology correctness.

The corrected compact layout:

- DRC errors: **0**;
- extracted devices: **5 intended NFETs + 1 intended MIM**;
- PRE, OK, DONE, EVT, OUT, WAKE, LEAKG and GND remain separate;
- full RC extraction completed.

## Compact full-RC PVT result

12-hop local burst, with validated-success refresh and DONE clear:

- TT: WAKE at hop 12 ~1.12027 V; minimum local event ~0.200221 V; post-DONE output ~-10.73 mV;
- FF: WAKE ~1.20161 V; minimum local event ~0.200060 V; post-DONE ~-12.73 mV;
- SS: WAKE ~1.02962 V; minimum local event ~0.200132 V; post-DONE ~-14.94 mV.

All nominal corners pass.

## Compact mismatch result

Four mismatch launches per corner: **12/12 PASS**.

Weakest hop-12 WAKE in the verified battery:

- TT mismatch minimum ~1.11369 V;
- FF mismatch minimum ~1.16441 V;
- SS mismatch minimum **~0.98405 V**.

All twelve local events remained essentially full 0.2 V. Cleanup remained within the existing +/-30 mV acceptance screen.

## Compact disturbance result

The compact PEX retains the useful partial-coordinate filtering:

### 5 mV orthogonal-fabric disturbance
Across TT/FF/SS:
- WAKE peak ~14-17 uV;
- local event output only ~0.341-0.350 mV.

### Deliberately bad 0.74 V partial coordinate
Across TT/FF/SS:
- WAKE peak ~0.207-0.275 V;
- local event output only ~2.07-3.83 mV.

### True 1.8 V coordinate
Across TT/FF/SS:
- WAKE peak ~1.136-1.234 V;
- local event output ~0.200 V.

## Energy result retained from transistor-level selection

For the selected 20-fF-class circuit, coordinate write was about 38-40 fJ and eleven validated refreshes about 7-47 fJ depending on corner. One long 16x16 selection plus the TT lease overhead is roughly 0.736 pJ versus ~8.16 pJ for twelve repeated long selections, approximately a 91% reduction in that **communication-only proxy**. This is not a whole-system energy claim.

## What is now solved

- one global coordinate can be amortized over at least a 12-event local burst without a digital counter;
- real SKY130 devices passed TT/FF/SS and mismatch;
- the physical lease is DRC-clean and full-RC extracted;
- the physical implementation uses parasitic capacitance productively;
- compacting the cell reduced its bounding-box area by ~18.5% without losing function;
- safe and deliberately bad partial-coordinate disturbances do not become full local events;
- DONE/CLEAN clears the region;
- exact fallback does not depend on the lease.

## Remaining problem

The next problem is **integration above this physical cell**, not the lease itself.

1. co-place/extract the physical 4T active-low coordinate-release cell with the compact lease;
2. verify the direct physical coordinate -> lease handoff, including combined mismatch and incomplete-coordinate cases;
3. connect the selected regional event to local Grammar/template/Myelin evidence without touching solved v12S run/capture nodes;
4. repeat complete historical-v12S signoff only with a simulator/model route compatible with the continuous SKY130 deck used by the historical baseline.

The current Linux ngspice build can run the device-specific SKY130 models used for these physical sub-block tests, but it cannot parse the newer continuous model deck used by the historical combined v12S library. The unchanged v12S control fails the same way under the stripped legacy model route, so that simulator limitation must not be misclassified as a Regional Lease failure.
