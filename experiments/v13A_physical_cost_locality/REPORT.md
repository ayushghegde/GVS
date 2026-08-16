# Neural Glyph v13A — Physical-Cost-Aware Hybrid Locality Compiler

## Verdict
PARTIAL PASS.

v13A continues the v12K -> v12M -> v12N -> v12O/P/Q/R -> v12S hybrid architecture. It does not move exact arithmetic/state back into analog hardware, and it does not make the fabric digital-only.

The experiment attacks the physical problem left by v12O/Q/R: primitive analog/event costs were measured, but long-wire communication and layout overhead were not part of the representation compiler's decision.

v13A feeds a real extracted inter-island communication cost back into the compiler and asks whether image, sound, code, and 12-hop reasoning should still use physical/event representations.

## Inputs preserved from earlier experiments

### Hybrid core costs
Normal-domain core/proxy values are taken from the preserved v12O task-value experiment:

- image exact: 47.556 pJ; hybrid core: 26.171 pJ
- sound exact: 1183.2 pJ; hybrid core: 506.700 pJ
- code dispatch exact: 99.2 pJ; Grammar/event core: 0.0409 pJ
- 12-hop reasoning exact table proxy: 10.8 pJ; physical/event hybrid core: 1.061 pJ

These are not whole-chip power numbers.

### Real physical communication cost
v13P10 physically drew and extracted a ~1 mm x 1 mm 16x16 orthogonal M4/M5 event grid.

The selected row + column charge was ~0.68 pJ at 1.8 V including the receiver input-loading estimate used in that experiment.

v13A intentionally keeps 0.68 pJ as the base long-fabric event cost and then stresses it by 2x, 4x, and 8x to represent missing driver/via/layout overhead.

## Failure mode tested

Bad implementation:

`every low-level motif/hop -> long GTI fabric -> destination`

This can erase the hybrid advantage even though the local analog primitive itself is extremely cheap.

The important result is that communication locality has to be part of the representation decision.

## Event counts used for the stress screen

- image: 16 local 2x2 Grammar/motif events from the v12N first-look representation
- sound raw stress: 480 original features
- sound Grammar case: 160 local 3-step groups (480/3)
- code: ~47 active sparse AST motifs
- reasoning: 12 relation hops

The sound 160-event case is a locality model, not a claim that every sound workload always has exactly 160 emitted spikes.

## Compiler acceptance rule

A physical/event representation is retained only if, after communication cost, it still keeps at least a 10% energy reserve versus the exact-core proxy.

The compiler can satisfy the rule by increasing local burst size: several local events execute inside one island before another long-fabric selection is paid.

No accuracy approximation is introduced by this locality rule. If physical cost cannot be repaid, the exact path remains available.

## Main result

### Measured 1x fabric cost
Even the deliberately bad per-event global implementation remains cheaper in the four normal domains, but the savings are smaller than the old primitive-only estimate.

Equal-domain average:
- all exact: ~335.19 pJ
- naive global hybrid: ~173.44 pJ
- reduction: ~48.3%

The old v12O core-only autonomous comparison was ~56.2% lower than all-exact. Real wire cost therefore removes part of the apparent advantage, but does not erase it.

### 2x communication-cost stress
Minimum local burst for >=10% reserve:
- image: 2 motif events
- raw sound: 2 events
- 3-step sound Grammar: 1 motif event
- code: 1 AST motif
- reasoning: 2 hops

### 4x communication-cost stress
Minimum local burst:
- image: 3 motif events
- raw sound: 3 events
- 3-step sound Grammar: 1 motif event
- code: 2 AST motifs
- reasoning: 4 hops

Equal-domain locality-aware reduction versus exact: ~21.0%.

A naive global implementation at the same 4x cost has only ~12.5% average reduction and individually makes image/code/reasoning much less attractive.

### 8x communication-cost stress
Minimum local burst:
- image: 6 motif events
- raw sound: 5 events
- 3-step sound Grammar: 2 motif events
- code: 3 AST motifs
- reasoning: all 12 hops in one local path/island

The locality-aware equal-domain average is still ~19.6% below all-exact, while the naive per-event global implementation is ~35% WORSE than all-exact.

This is the strongest v13A result.

## Architecture decision

The long event fabric must not behave like a conventional bus carrying every synapse/event.

Selected rule:

`raw/local evidence -> local Grammar/capacitive/Myelin island -> high-level event or exception -> long fabric`

not:

`every feature/hop -> long fabric`.

### Image
Keep 2x2/local visual Grammar and capacitive evidence local. At high communication overhead, several motif events should be evaluated within one island before a global event is emitted. Ambiguous/detail-rich images still escalate to the exact/detailed path.

### Sound
The existing 3-step Grammar structure is physically valuable for communication as well as recognition. It reduces the number of long-distance events enough that sound remains strongly favorable even under large routing-overhead stress.

### Code
AST motifs should be recognized locally. The long fabric should carry a kernel/algorithm dispatch event, while exact program semantics, arithmetic, indexes, and state remain digital.

### Reasoning
This is the most communication-sensitive domain. A 12-hop chain should not pay a millimeter-scale coordinate selection on every hop. Hot/repeated multi-hop paths should stay inside one local event region/Myelin execution path. Drift, cold relations, and exceptions still use exact rules/tables.

This independently supports the v12Q/v12R Myelin direction using real extracted wire cost.

## What v13A solves

- It closes part of the v12O "unknown analog overhead" problem with an actual extracted communication number.
- It explains why v12N Grammar and v12Q/R Myelin are not just recognition tricks: they are communication-compression mechanisms.
- It prevents the compiler from promoting a physical representation whose wire movement costs more than the memory movement it was meant to avoid.
- It keeps analog/event computation local and exact computation available without forcing either representation everywhere.

## What it does NOT solve

- The 0.68 pJ figure is one extracted 16x16 island, not a complete-chip route hierarchy.
- Driver energy and inter-island hierarchy above one 16x16 island are still not fully extracted; 2x/4x/8x factors are stress tests, not measurements.
- Selector transistor area is not fully solved. v13A reduces long selector/template wiring by keeping selectors/Grammar local, but the remaining local selector layout area still needs physical compaction.
- A local "burst/region hold" circuit that amortizes one coordinate selection across several events is not yet transistor/layout validated.

## Next physical experiment

The best next hardware step is a regional wake/communication trace:

1. one long row/column coordinate selects a local island;
2. a small local charge/lease state remembers that selection for a short event burst;
3. local Grammar/capacitive/Myelin events run without repeatedly recharging the long row/column wires;
4. inactivity leaks/reset clears the regional wake;
5. exact fallback remains independent.

This reuses the old Glyph principle of charge as short-lived state rather than adding a large digital routing controller.

The first target should be the 4x-stress requirements from this experiment:
- >=3 image motifs per wake
- >=3 raw sound events (or one 3-step Grammar motif)
- >=2 code motifs
- >=4 reasoning hops

If a tiny physical wake trace can hold those burst lengths without false selection, the long-wire problem is substantially reduced.
