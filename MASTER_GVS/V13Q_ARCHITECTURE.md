# GVS v13Q — Cellular Conduction Confidence Fabric

**Status:** architecture/model pass; physical contact aperture and population-confidence closure open.

v13Q keeps the accepted v13A computational primitives, v13K neurovascular anatomy, v13L isolation rule, and v13O/v13P physical-reasoning direction. It changes the local communication substrate and the treatment of uncertainty.

## 1. Central invention — cell becomes part of the wire

### Embodied Conduction Cell (ECC)
An ECC is a repeated Glyph cell whose boundary contains selectable communication contacts, local evidence/state storage, and regeneration. For short local paths the event is handed from cell to neighbouring cell; the computing fabric itself therefore forms the communication path.

This removes the architectural separation `compute cell -> router -> local wire -> router -> compute cell` where that separation provides no benefit.

It does **not** claim conductor-free electronics. Short metal/contact structures still exist inside and between cells.

## 2. Cell geometry
A conceptual cubical ECC has candidate contacts on:
- 6 faces;
- 12 edges;
- 8 vertices.

These are **candidate** contacts, not permanently conductive junctions.

### Contact Aperture
A Contact Aperture is a normally closed/off local electrical interface that opens only when a stored/promoted relation or active local event needs that neighbour.

The default preference is:
1. face contact;
2. edge diagonal if it materially reduces path cost;
3. vertex diagonal only if its measured coupling/energy still wins;
4. dedicated Nerve/subwire/spine/chord for communication that is not economical as a regenerative cell chain.

v13Q0 model result: in a 16 x 16 x 4 packed-cell lattice, face+edge+vertex reachability reduced mean relay count from ~11.877 to ~7.476 hops (~37.05%). With edge=1.5x and vertex=2x face-contact energy, the relay proxy was ~18.53% lower than face-only. At edge=2x/vertex=3x the energy win vanished. Therefore diagonal contacts are optional compiler choices.

## 3. Outer protective skin and hollow interior
The chip/package remains inside-out/hollow in the architectural sense established earlier.

### Practical implementation
- active local cells live on conventional or stacked silicon layers;
- backside/outer package surfaces may carry additional cell/service layers, support chiplets, reservoirs, thermal structures and I/O;
- the protective/passivation material itself is not assumed to magically contain normal CMOS devices;
- inner component bays and stacked active skins fill the hollow volume only where they repay cost;
- unused hollow volume may remain structural/thermal/empty.

### Future implementation
If manufacturing supports true active inner/outer/side surfaces, ECCs may form a genuinely three-dimensional packed fabric with independent face/edge/vertex apertures.

## 4. Unsureness is represented physically
v13Q does not store `UNSURE=1` in a controller.

### Population Confidence Field (PCF)
Several local cells represent each competing hypothesis. The network's confidence is the activity/evidence separation between the strongest population and its competitors.

`large separation -> robust event`

`small separation -> keep settling / recruit more evidence / do not fire`

The uncertain state is therefore a **distributed physical condition**, not a computer instruction.

v13Q0 evidence accumulation model with four candidate populations and sixteen cells/population:
- moderate drift 0.18: 99.8% correct robust decisions, 0.01% wrong robust, 0.19% still uncertain;
- stronger drift 0.25: 100% correct, zero wrong, zero unresolved in 20,000 trials.

Very weak evidence intentionally remains unresolved more often rather than being forced into a wrong categorical answer.

## 5. Local inhibition and recurrence
The physical analogy retained from neural circuits is:
- recurrent excitation preserves/accumulates evidence for a hypothesis;
- lateral inhibition makes incompatible populations compete;
- fatigue/homeostasis prevents one stale population from owning the region indefinitely;
- constraint pressure from v13O destabilizes states that continue violating relations;
- population margin determines whether a robust event may leave the local fabric.

There is no central variable-selection/search processor in this rule.

## 6. Quorum Relay
A Quorum Relay is a local ECC regeneration rule in which several selected neighbour contacts must agree before the cell repeats a robust event.

In the v13Q0 stress model, every selected contact has a 10% independent event error and the path is 16 cell relays long:
- one contact/hop becomes unreliable;
- five supporters with a confidence margin reduce end-to-end wrong events to ~0.785%;
- seven to ~0.325%;
- nine to ~0.085% with ~1.008 local attempts/planned hop and no measured stalls in 20,000 trials.

This is not final fault tolerance; it establishes a cost/reliability knob that remains local to the fabric.

## 7. Wall computation
An ECC boundary is not only a switch matrix.

Each face/edge/vertex contact group can feed a small local integration compartment before the cell body/state changes. This follows the useful biological principle that dendritic compartments perform local nonlinear integration instead of sending every input to a central processor.

In GVS terms, a wall may contain/reuse:
- a short capacitive evidence input;
- a template/Grammar relation;
- a local inhibitory input;
- a familiarity/promote state;
- a Contact Aperture gate.

The exact transistor/MIM implementation remains to be physically selected; v13Q does not invent a large crossbar per cell.

## 8. Knowledge and reasoning
v13Q composes the previous physical-reasoning mechanisms:

`input -> local Grammar/templates -> temporary binding/context -> relation propagation through ECC fabric -> constraint/population settling -> optional exact spatial patch -> robust output`

Long-term stable knowledge should preferentially become sparse morphology/relations in the cell fabric rather than fetched weights.

Temporary/novel context remains distributed state and does not require permanently rewiring every contact.

## 9. Communication hierarchy after v13Q
1. direct active face aperture;
2. selected edge/vertex aperture if cheaper;
3. short regenerative ECC chain;
4. dedicated low-swing Nerve/subwire;
5. regional event spine for fanout;
6. promoted electrical/Myelin chord for stable longer relation;
7. optional optical Light Nerve for genuinely long/hot/reused traffic after real break-even.

The compiler is free to choose; none of these is a universal routing law.

## 10. Neurovascular services retained
### Nerve
Nerve remains a low-swing event carrier for routes where a dedicated path beats cell-by-cell regeneration. v13Q reduces its local use; it does not delete it.

### Charge Artery
Expired charge still uses a separate one-way low-voltage recovery path. Information contacts do not double as recovery collectors.

### Thermal Capillary
Heat remains on passive thermal structures. Computation/contact walls do not become heat-routing switches.

### Light Nerve
Optical routes remain optional and must beat the best real electrical/cellular path.

## 11. Why not open every contact?
A permanently open 26-neighbour cell would create excessive capacitance, crosstalk and unclear ownership. v13Q therefore selects **potential connectivity + sparse active conductivity**.

A cell may be geometrically adjacent to many cells while electrically participating with only a few at a given time.

## 12. Current decision
### KEEP
- cell-as-regenerative-local-wire concept;
- possible face/edge/vertex neighbour geometry;
- normally closed Contact Apertures;
- population-coded uncertainty;
- local recurrent accumulation + inhibition;
- quorum regeneration;
- earlier Grammar/template/Myelin/context/fatigue/homeostasis;
- separate charge and thermal anatomy;
- flexible hollow inside/outside placement.

### REJECT
- one router/controller per cell;
- all 26 contacts permanently open;
- forcing every signal through the cell fabric when a dedicated route is cheaper;
- treating uncertainty as permission to guess;
- automatic computer fallback for every low-confidence state;
- merging recovery/thermal current with weak information contacts.

## 13. Evidence boundary
v13Q0 is a deterministic system/model experiment using preserved GVS event-energy proxies. It is not SKY130 PEX of a 3-D ECC.

The next physical question is the off-capacitance and disturbance cost of selectable neighbour apertures around a real weak evidence pair.

## 14. Next — v13Q1 Physical Contact-Aperture Slice
Construct a planar physical proxy with:
- one recovered/closed Grammar weak pair;
- one repeated ECC body/state element;
- four face-like neighbour apertures;
- two diagonal shortcut variants;
- local population/quorum integration represented by the smallest MOS+MIM implementation that preserves the model rule;
- nearby Nerve and Charge Artery retained for comparison.

Measure DRC, connectivity, off/on contact capacitance, GC/GR differential coupling, event energy, PVT/mismatch and whether uncertain input remains non-robust before wrong acceptance.

If diagonal contacts are expensive, delete them. If contact-off loading destroys Grammar margin, isolate the apertures physically before changing the proven Grammar reader.
