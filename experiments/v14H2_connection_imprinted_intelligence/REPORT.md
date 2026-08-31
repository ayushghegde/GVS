# v14H2 — Connection-Imprinted Excitation Fabric

## Problem
Earlier v14H work focused too narrowly on reusable arithmetic transformations. The larger architectural question is whether persistent semantic memory needs to live inside every cell at all.

The new hypothesis is that long-term meaning is mostly **connection memory**: which cells are connected and how strongly. Cell voltage/charge is temporary excitation for the current query and should decay between queries.

## New primitives

### Connection-Imprinted Excitation Fabric (CIEF)
A sparse network in which semantic memory is encoded in connection strength. Nodes begin each query with no persistent semantic charge.

### Capacitive Synapse Link (CSL)
A passive weighted connection whose coupling strength controls how much transient charge a receiving cell gets. The cheapest inference-only implementation can use fixed capacitor geometry; a trainable two-terminal implementation remains open.

### Ephemeral Relay Cell (ERC)
A semantic node that carries temporary activation but has no dedicated nonvolatile voltage/state memory. It may use unavoidable/parasitic node capacitance as the transient carrier.

### Connection Bundle Population (CBP)
A small number of parallel weak/strong links for important relations. Redundancy is spent on connections rather than persistent memory in every cell.

## Broad shared-fabric experiment
One fabric was used for seven synthetic reasoning families:

1. ambiguous context/meaning selection;
2. causal two-hop relations;
3. code-like diagnosis -> repair;
4. planning/prerequisite chains;
5. factual multi-hop relations;
6. analogy/relation matching;
7. selection of a reusable structural operation.

The experiment is intentionally not a foundation-model benchmark. It tests whether one connection-based physical rule can serve multiple reasoning types without separate persistent node memories.

### Fabric size
- semantic/goal cells: 2,852;
- learned sparse directed connections: 5,312;
- dedicated persistent node-memory sites: 0;
- connection density: about 0.0653% of a dense directed fabric.

### Connection-strength variation
Overall accuracy:
- nominal: 100%;
- 10% independent link-strength sigma: ~99.95%;
- 20%: ~99.48%;
- 30%: ~98.31%.

At 20% variation, analogy is the weakest family because its competing learned paths are deliberately close; the other tested families remain near-perfect in this synthetic graph.

## Capacitive co-firing screen
For a simple ambiguous-context junction, a 0.2-V input step drives a 5-fF receiving node through passive coupling capacitors.

Correct context target couplings: `0.65 + 0.9 + 0.9 + 0.9 fF`.
Weak competing target: `0.65 + 0.18 + 0.18 fF`.

Nominal charge-sharing estimate:
- correct target: ~80 mV;
- weak/ambiguous target: ~34 mV.

At 40% independent capacitor variation, the correct target still received the larger voltage in the 5,000-trial screen.

This supports the physical principle that **co-firing through stronger/more numerous connections naturally produces larger received excitation** without storing semantic voltage in the target cell.

## Weight precision screen
The learned connection weights were quantized to physical levels.

A two-level weak/strong fabric remained ~99.81% correct at 20% link variation and ~97.04% at 40% variation in this synthetic benchmark.

Therefore the present evidence does not justify expensive high-precision analog connection weights. The first physical candidate should use very few connection-strength levels.

## Long-chain connection redundancy
A separate 12-hop screen used one correct strong connection and three weak distractors at every hop.

At 30% link variation:
- one link per relation: ~77.1% exact 12-hop chains;
- two parallel copies: ~98.65%;
- three copies: ~99.85%;
- five copies: 100% in this 2,000-chain run.

Tripling all 5,312 links would still be only ~0.196% of a dense 2,852-cell directed fabric. This is a structural proxy only, not an area/yield measurement.

## Persistent-node-charge control
Retaining activation from the previous query did not improve the mixed-domain benchmark. Small residuals were mostly harmless; larger residuals caused cross-query interference. At 20% connection variation, retaining 50% of previous-query activation reduced accuracy from ~99.67% to ~98.26% in the selected run.

This does not prove biological neurons never use persistent local state. It supports the narrower hardware choice: **persistent semantic memory does not need to be stored as voltage in every GVS semantic cell.**

## Keep / reject

KEEP:
- persistent semantic memory in sparse connection strengths;
- temporary charge as the current-query carrier only;
- Goal Echo and Need Potential as connection biases;
- two/few-level connection strengths before precision-heavy analog weights;
- sparse connection bundles where variation requires redundancy;
- CRRO/other structural operators as reusable specialized transformations selected by the same connection fabric;
- sparse CFN/Role-Pressure tissue only where its measured benefit repays its extra state.

REJECT:
- a nonvolatile electrical state element in every semantic cell;
- dense all-to-all connection matrices by default;
- high-precision analog weight storage without measured benefit;
- treating modular arithmetic as the center of intelligence;
- claiming the synthetic seven-domain benchmark means all human questions are solved.

## Hardware interpretation
Two hardware paths remain distinct:

1. **Fixed compiled connection plane** — train the model before fabrication and encode weak/strong weights as passive capacitor/interconnect geometry. This is the cheapest inference candidate but cannot learn new weights on-chip.
2. **Trainable two-terminal connection plane** — use a nonvolatile two-terminal device whose conductance/capacitance state changes with training. This retains learning flexibility but must beat CMOS on process complexity, area, programming energy, retention, endurance and variation.

The architecture must not call a memcapacitor/memristor cheaper merely because it has two terminals.

## What is next
v14H3 should test **Connection Plasticity Without Node Memory**:
- fixed two-level MIM geometry control;
- a compact two-terminal programmable-capacitance model;
- a compact two-terminal conductance-memory model;
- CMOS/SRAM weight storage as cost reference only.

The test must add new facts/relations after deployment, measure interference with old knowledge, quantify the minimum number of programmable links required, and preserve the same broad reasoning mechanism. Multiplication/factorization becomes one structural-operator subproblem inside this larger experiment rather than the canonical goal.
