# Neural Glyph v13B1 — Hollow Contact Region + Analog Reader Screen

**Verdict: KEEP AS A TARGETED ARCHITECTURE OPTION, NOT AS A BLANKET REPLACEMENT FOR NORMAL METAL ROUTING.**

This experiment tests three related ideas:

1. a chip-sized hollow/shell-like 3D organization with active structures on outer/inner surfaces;
2. local touching/contact-style electrical propagation instead of a separate long wire for every logical edge;
3. a readerless / fully analog Grammar-consumption path that directly steers an existing local competition node.

It does not replace the closed v13A5 10-MIM + dual-pair robust reader. That reader remains the safe boundary for destinations that require a robust event.

## 1. Important correction about planar routing

In normal CMOS, cell A does not literally need to pass through B/C/D to reach E. Upper metal can already cross over intermediate cells. The physical cost comes from distance, capacitance, coupling, repeaters, and routing congestion.

Therefore a hollow 3D geometry is useful only when it reduces those physical costs or adds genuinely useful extra surfaces/shortcuts. It is not useful merely because intermediate cells no longer block the route.

## 2. Hollow shell graph screen

A simple equal-scale topology model compared ~150-node networks.

Baseline 12x12 planar nearest-neighbor grid:
- 144 nodes
- average path = 8 hops
- p95 = 15 hops

6x6x6 hollow cube boundary, local face/edge touching only:
- 152 nodes
- average path = 6.65 hops
- ~16.9% fewer hops
- ~16.9% shorter normalized geometric path
- only ~1.14x the total local connection inventory of the planar nearest-neighbor grid

Hollow shell with local surface diagonals:
- average path = 4.22 hops
- ~47.3% fewer hops
- ~33.9% shorter normalized geometric path
- but ~3x the total connection inventory

Hollow local-touch shell + sparse cross-cavity chords:
- 6 chords: 5.49 average hops (~31.4% fewer than planar), ~1.33x connection inventory
- 12 chords: 5.26 average hops (~34.3% fewer), ~1.50x inventory
- 24 chords: 5.01 average hops (~37.3% fewer), ~1.83x inventory

For one extreme opposite-corner route in the model:
- surface nearest-neighbor route = 15 local hops / normalized length 15
- surface diagonal route = 9 hops / length ~11.49
- one direct cross-cavity chord = 1 hop / length ~8.66

This supports sparse long shortcuts for hot/reused paths rather than wiring every possible diagonal.

## 3. Contact Nervous Mesh — new architecture concept

**Contact Nervous Mesh (CNM): a local GVS fabric where neighboring cells exchange charge through short controlled junctions at their physical boundaries instead of requiring a separately routed long wire for every neighbor relation.**

The key word is **controlled**.

Raw conductive touching of many cells would simply short states together, spread charge everywhere, and destroy selectivity. A useful contact mesh requires one of:
- a pass MOS junction;
- a weak context/inhibition transistor;
- a capacitive contact;
- a stable programmable/memristive junction in a future process.

Current research on self-organized nanowire and nanoparticle networks shows that physically touching junction networks can conduct through many parallel paths and exhibit brain-like / reservoir dynamics. That validates the physical principle, but those systems are not precise replacements for CMOS routing.

### Selected use in GVS

Use CNM only for very local neighborhood interaction:
- competition;
- inhibition;
- context;
- short Grammar-to-next-stage transfer;
- local recurrent reasoning;
- lease/fatigue/homeostasis sharing.

Do not use an uncontrolled contact mesh for exact state or long global routing.

## 4. Myelin Chord — new architecture concept

**Myelin Chord: a sparse direct conductor across the hollow interior that connects two repeatedly communicating regions without forcing the event through every local surface hop.**

This is the hollow-chip form of the existing Myelin idea.

A chord is created/promoted only when reuse justifies it. Cold or changing relations remain ordinary routed/exact state.

This gives the hollow geometry an actual purpose:
- local contacts handle dense nearby interactions;
- sparse chords handle hot long-range associations;
- robust events travel across chords;
- weak analog state normally remains local unless the chord itself is an intentionally short analog Myelin edge.

## 5. Fully analog / readerless Grammar screen

The closed v13A5 reader is already an analog comparator internally, but it regenerates to a robust event. This experiment tests a more analog path: use the Grammar candidate/reference voltages directly to steer the next local physical competition.

**Analog steering reader: a readerless path where candidate/reference voltages directly gate weak inhibitory transistors in the destination competition instead of first creating a separate full-swing readout.**

The current co-placed Grammar levels were used approximately as:
- exact: GC=0.5748 V, GR=0.5527 V
- partial: GC=0.5301 V, GR=0.5517 V

A compact 100 fF destination competition was tested using weak W=0.42 um / L=12 um direct shunts.

### TT
Exact:
- intended C max ~0.424 V
- wrong E max ~0.219 V

Partial:
- C max ~0.334 V
- intended E max ~0.581 V

Correct polarity in both directions.

### FF
Exact:
- C max ~0.458 V
- E max ~0.203 V

Partial:
- C max ~0.330 V
- E max ~0.640 V

Correct polarity.

### SS
Exact:
- C max ~0.338 V
- E max ~0.194 V

Partial:
- C max ~0.316 V
- E max ~0.460 V

Correct polarity.

The readerless path therefore preserves the current Grammar sign through TT/FF/SS in this screen.

The test used the same asymmetric rule already validated in v12G: new evidence excites; analog context/evidence steers inhibition. It does not add a powered analog reader.

### Mismatch status

A first `tt_mm` rerun did not produce independent seeds in the current ngspice invocation, so no new mismatch claim is made here. Do not replace the v13A5 robust reader until an actual independent-mismatch screen passes.

## 6. Energy/area interpretation

The readerless analog path is attractive only when the destination already contains a local membrane/competition node.

If a new membrane is added solely to avoid the ~80-100 fJ robust Grammar readout, the extra capacitance/current can erase the benefit.

Selected rule:

- destination already analog/local competition -> try direct analog steering first;
- destination requires robust/full-swing state or exact boundary -> use the closed dual-pair reader;
- long/hot repeated route -> consider Myelin chord;
- cold/changeable/exact relation -> keep routed/exact computer representation.

## 7. Hollow chip practicality

The hollow shell is not selected as the first fabricated GVS package.

Potential benefits:
- more usable inner+outer surface area;
- shorter 3D paths for some region pairs;
- sparse direct cross-cavity chords;
- natural separation of local analog surface regions and robust long-range links;
- possible thermal benefit only if the internal surface is actually connected to a heat-transfer path.

Problems:
- inner-surface fabrication/alignment;
- power delivery;
- testing/yield;
- mechanical packaging;
- uncontrolled contact networks create crosstalk;
- an empty sealed cavity gives little thermal benefit by itself.

Therefore the selected near-term implementation is to emulate the hollow architecture in ordinary silicon first: multiple local regions, short local contact-like interfaces, and sparse direct chords/bridges. Only move to a real hollow package if the measured routing/thermal gains justify the manufacturing cost.

## 8. Decision for v13B

Keep three routing classes:

1. **Local contact** — very short controlled neighbor interaction.
2. **Myelin chord** — sparse direct long-range path for hot/reused associations.
3. **Exact/global fabric** — robust route for changing, cold, or exact state.

Keep two Grammar consumption classes:

1. **Readerless analog steering** when the destination already has a physical competition node.
2. **Closed v13A5/v13A6 dual-pair reader** when a robust event is actually needed.

The next v13B region should measure how many reader blocks and long-coordinate events disappear when these choices are made by physical locality/reuse instead of using one interface everywhere.
