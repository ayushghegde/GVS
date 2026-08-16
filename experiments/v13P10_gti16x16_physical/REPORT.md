# v13P10 — Physical 16x16 GTI fabric with extracted CMR loading

**Verdict: PARTIAL PASS — physical fabric scaling passed; full tile lifecycle integration remains**

## What happened

A real ~1 mm x 1 mm 16x16 inter-tile event grid was drawn and extracted using the supplied SKY130A Magic technology.

Geometry:

- 16 horizontal M4 trunks
- M4 width: 0.30 um (technology minimum)
- 16 vertical M5 trunks
- M5 width: 1.60 um (technology minimum)
- ~60 um same-layer trunk pitch
- 256 M4/M5 orthogonal crossings

Result:

- DRC errors: **0**
- named row/column nets: 32
- each M4 row substrate capacitance: **75.908 fF**
- each M5 column substrate capacitance: **~87.7 fF**
- each M4/M5 crossing coupling: **0.221205 fF**
- crossings per row/column: 16
- accumulated crossing coupling per row/column: **3.53928 fF**

The 256-crossing grid therefore remains linear: no new collective coupling mode appeared compared with the earlier 4x4 experiment.

## Receiver loading

v13P8 physically extracted the CMR proof layout. Approximate full input loading from its substrate/coupling terms is:

- ROW input: **~1.24525 fF per receiver**
- COL input: **~1.19779 fF per receiver**

Adding 16 receiver inputs and 16 crossing couplings to one selected axis gives approximately:

- selected M4 row: **99.37 fF**
- selected M5 column: **110.60 fF**

At 1.8 V, one 0->1 charge of the selected row + selected column costs roughly:

**0.68 pJ** (`(Crow+Ccol)*V^2`).

This remains small relative to the historical ~28.28 pJ nominal v12S physical-query window and, importantly, the event capacitance is not placed on v12S local run/capture/dendrite nodes.

## What is solved by this experiment

The earlier long-parallel-event-wire crosstalk problem has a physically validated scaling path:

- use orthogonal M4/M5 event geometry;
- keep tile-local analog competition local;
- use CMR at intersections;
- use the v13P9 local PRE boundary to wake only the selected tile.

A 16x16 physical event fabric does not show unexpected crosstalk accumulation.

## What is not solved

- receiver and PRE-gate full supplied-SKY130 transient signoff is still blocked by the local ngspice parser/library compatibility issue;
- the complete v12S tile has not yet been physically instantiated 256 times;
- inter-cluster hierarchy above one 16x16 island is not yet physically tested.

## What is next

The next useful step is not a larger flat grid. It is to connect one selected GTI coordinate through CMR + PRE_LOCAL into the unchanged v12S lifecycle, then test a hierarchy of 16x16 islands only after that chain is verified.
