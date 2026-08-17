# Neural Glyph v13A4 — Eight-Way Shared Local Group

**Verdict: PARTIAL PASS — one physical coordinate/Regional-Lease interface successfully serves eight isolated local event paths in the same bounding box. Real Grammar/template/Myelin loads remain the next step.**

## Problem

v13A3 solved one physical coordinate -> Regional Event Lease -> one local event path. Duplicating that complete interface for every nearby operation would bring back area and long-wire duplication.

v13A4 asks whether one selected physical region can serve several nearby Glyph operations while:

- keeping each event source isolated;
- preserving lease PVT/mismatch margin;
- blocking incomplete coordinates;
- avoiding a larger interface footprint;
- retaining exact fallback independence.

A "local group" here is simply a few nearby Glyph event paths that reuse one long-distance selection. It is not a new compute architecture.

## 4-way intermediate experiment

The selected v13A3 interface was given three additional minimum-size W=0.42/L=0.15 event-gate NFETs. All four gates share WAKE, but every path has its own EVT and OUT node. Inactive sensory/event sources are never shorted together.

This explicitly avoids the previously rejected shared-sound-selector mistake where inactive 0 V sources fought an active source.

### Physical result

- DRC: 0;
- expected devices: 10 NFET + 2 PFET + 1 MIM = v13A3 core (7 NFET + 2 PFET + 1 MIM) + 3 extra event gates;
- bounding box: still ~30.02 um x 22.0 um = **660.44 um^2**;
- no bounding-box growth relative to the one-path v13A3 interface.

Ground-referenced extracted WAKE capacitance proxy rises from ~9.625 fF for the one-path interface to ~12.220 fF for the 4-way physical group, an increase of ~2.60 fF (~27%).

Full physical PEX passes TT/FF/SS, row-only/column-only/none/partial-coordinate negatives, and 12/12 mismatch launches.

Weakest SS-mismatch WAKE at event 12 in the recorded 4-way battery: ~0.999 V. Active selected events remain essentially 0.2 V; inactive outputs remain microvolt-class.

## 8-way selected experiment

Seven extra minimum event gates were packed into unused space around the existing interface using two local gate columns. The shared WAKE route controls only transistor gates. Every EVT/OUT path stays separate.

### Physical layout

- DRC: 0;
- extracted device count: **14 NFET + 2 PFET + 1 MIM** = 7-NFET/2-PFET v13A3 core + 7 additional event gates;
- bounding box: **30.02 um x 22.0 um = 660.44 um^2**;
- therefore the 8-way group still has the same bounding box as the original one-way interface.

A naive eight-interface duplication proxy would be 8 x 660.44 = ~5283.5 um^2. One shared interface with eight paths is therefore an **87.5% reduction in duplicated interface bounding-box area per eight paths** in this placement. This is a bounding-box proxy, not final routed-chip area.

### Extracted WAKE loading

Ground-referenced WAKE-network capacitance proxy:

- one path: ~9.625 fF;
- four paths: ~12.220 fF;
- eight paths: ~13.961 fF.

So eight-way physical routing adds ~4.34 fF versus the one-path interface (~45%), but only ~1.74 fF versus four-way (~14%). The extra capacitance is not purely harmful: with validated refresh it also slows WAKE decay and contributes useful lease storage.

## 8-way PVT result

Twelve sequential local events are distributed across the eight isolated paths while validated local-success pulses refresh the common lease.

- TT: WAKE event 12 ~1.1271 V; minimum active event ~0.200214 V; PASS.
- FF: WAKE event 12 ~1.2065 V; minimum active event ~0.200060 V; PASS.
- SS: WAKE event 12 ~1.0434 V; minimum active event ~0.200017 V; PASS.

Inactive-path outputs remain microvolt-class during a selected event. DONE clears the shared lease.

## False-coordinate result

At SS with **no validated refresh**:

- row-only: WAKE peak ~0.611 mV;
- column-only: ~1.127 mV;
- none: ~0.485 mV;
- deliberately partial coordinate: ~0.855 mV.

Intended event-path outputs remain only ~0.34 mV class, not ~0.2 V.

## 8-way mismatch result

Four launches per corner: **12/12 PASS**.

Event-12 WAKE:

TT mismatch:
- 1.17805, 1.13704, 1.08084, 1.14394 V

FF mismatch:
- 1.18797, 1.16132, 1.23844, 1.15245 V

SS mismatch:
- 1.04640, **1.01660**, 1.02662, 1.07661 V

Every active local event remains essentially full 0.2 V. Inactive outputs remain microvolt-class and cleanup remains inside the existing +/-30 mV screen.

## Energy comparison

Using the same full-PEX TT integration window:

- 4-way coordinate-write + eleven validated refreshes: **~99.7 fJ**;
- 8-way: **~106.8 fJ**.

Doubling the physical local paths from four to eight therefore increases this local lease/interface energy by only **~7.2%** in the measured bench.

If eight nearby operations would otherwise each pay the ~0.68 pJ long 16x16 coordinate-selection proxy, eight long selections are ~5.44 pJ. One long selection plus the ~0.107 pJ local 8-way lease activity is ~0.787 pJ, an **~85.5% reduction in this communication/locality-overhead proxy**. This is not a whole-system energy claim.

## 16-way electrical boundary screen

A 16-gate electrical loading screen, without a new physical 16-way layout, was also run to determine whether the next limit is electrical or geometric.

At SS:
- nominal event-12 WAKE ~1.0435 V;
- four SS-mismatch launches: ~0.9982, 1.0326, 1.0381, 1.0750 V;
- selected events remain ~0.2 V.

Therefore 16-way fanout is still electrically plausible. It is **not selected**, because the current physical advantage of eight-way is that seven extra event gates fit in existing whitespace with no bounding-box growth. A 16-way physical layout would require more aggressive packing/routing and should only be pursued if real local workloads need it.

## Decision

**Select eight local paths per physical Regional Lease as the current default physical group size.**

Why:

- 8-way is physically extracted and DRC-clean;
- same bounding box as one-way and four-way implementations;
- 12/12 mismatch pass;
- false coordinates remain blocked;
- only ~7% more local lease energy than the 4-way implementation;
- 16-way has electrical headroom but no demonstrated zero-area physical implementation yet.

This is a physical granularity decision, not a fixed architectural law. The representation compiler may later choose a smaller or larger local group when measured workload reuse/area/communication cost justifies it.

## What is next

The event gates used here are deliberately simple load/isolation paths. The next experiment must replace some of them with **real local work** from the existing Glyph architecture rather than continuing to add empty fanout:

1. attach a small Grammar/template/Myelin evidence structure behind several of the eight paths;
2. keep evidence and competition local;
3. allow only validated local winners to refresh the shared lease;
4. verify that inactive local structures stay physically quiet;
5. extract local evidence-wire coupling and area;
6. compare one shared 8-way group against eight separately selected structures;
7. do not modify solved v12S run/capture or exact fallback.

The historical full-v12S continuous-model simulator incompatibility remains a separate tooling problem and must not be mistaken for a failure of this physical local-group result.
