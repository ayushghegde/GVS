# Neural Glyph v12S — Autonomous Complete Tile + Hierarchical Local Rebuild

**Verdict: PARTIAL PASS**

## What v12S was required to solve

Two previously open problems were attacked together:

1. The software-heavy rebuild loop still scanned too much of the model and decided replacement structures globally.
2. The physical hardware pieces had not all been exercised in one integrated transistor-level tile.

v12S now has a single SKY130/ngspice lifecycle netlist containing:

- physical reuse lease;
- physical hot-region rebuild request;
- one exact low-leak `VALID` SRAM bit;
- Grammar Cell inputs;
- pre-placed programmable passive Myelin edge slots;
- capacitive template evidence;
- local dendrites;
- robust soma nodes;
- shared competition/inhibition;
- one-hot full-swing Myelin route capture;
- new-data exact kernel;
- exact timeout fallback;
- recovery reservoir;
- error-triggered invalidation/demotion.

This is **one schematic-level transistor/capacitor netlist**. It is not yet an extracted physical layout.

## Important architecture correction: rebuilding means enabling local edge slots

A fabricated chip cannot grow a new MIM capacitor after manufacturing.

The practical self-reorganizing mechanism is therefore a small local pool of pre-placed structural slots.

A rebuild writes local configuration/trust state that enables an appropriate slot.

The programmable passive Myelin experiment used:

`Grammar dendrite -> MIM capacitor -> minimum-size static pass NFET -> local dendrite`

With the selected 10 fF target, the programmed route retained a useful exact/partial separation across TT/FF/SS and mismatch screens. With the config bit off, the target returned to its baseline.

Thus "rebuild" in this silicon proposal means **local re-binding of a pre-placed structural resource**, not dynamic fabrication.

## Hierarchical rebuild: stop scanning the whole model

The rebuild compiler was replayed against the actual 28,000-query v12Q trace containing 349 distinct execution-plan regions and 12 initial structural archetypes.

A stress sequence invalidated regions at two workload shifts and also injected novel structural changes.

### Whole-model periodic baseline

- sleep epochs: 194
- regions: 349
- region inspections: 67,706
- four-way representation-check proxy: 270,824
- continuous metadata proxy: 8,376 exact bits

### Physical-lease hierarchical rebuild

- consolidator region inspections: **12**
- rebuild requests: **12**
- exact fingerprint lookups: **12**
- deeper exact candidate evaluations: **27**
- actual local rebuilds: **12**
- reused existing archetypes: **5**
- new local structures: **7**
- exact continuous metadata: **349 VALID bits**

Reductions:

- region inspection: **99.982%**
- representation/candidate checking: **99.986%**
- continuous exact metadata: **95.83%**

Final answers stayed exact because an invalid region remains on the exact path until its local rebuild is verified.

Not every invalidated region was rebuilt. That is intentional. Cold invalid regions stayed exact/digital rather than spending hardware/configuration effort on a representation that had stopped paying for itself.

## New rebuild idea: exact fallback is the teacher

v12S removes another unnecessary search.

When a physical representation is invalid, the first exact fallback already executes the correct structure.

That exact fallback produces a small structural fingerprint.

During sleep:

1. physical lease says which invalid region is hot;
2. exact fallback trace supplies the desired structure;
3. fingerprint checks whether an existing archetype already implements it;
4. if yes, locally re-bind that archetype;
5. only a fingerprint miss enters rule/template/Grammar/physical-edge search;
6. verify;
7. write local config + VALID.

This is why only 27 deeper candidate evaluations were needed in the stress test.

The exact computer is therefore used as a **shadow teacher** only after the physical system asks for help.

## Final complete tile — nominal PVT

### TT / 25 C

- lease after two reuse packets: **0.663 V**
- physical rebuild request: **16.030 us**
- VALID after rebuild: **1.800000 V**
- exact vs partial local dendrite: **0.5431 / 0.5005 V**
- dendritic margin: **42.61 mV**
- correct route latch: **1.800000 V**
- wrong route latch: **-3.292e-06 V**
- max wrong route during decision/cleanup: **0.0016 V**
- physical-query exact output: **1.800000 V**
- VALID after error: **4.507e-09 V**
- invalid-query physical route: **1.098e-09 V**
- exact-fallback output: **1.800000 V**

FF and SS produced the same logical behavior.

Winner latency after soma release:

- TT: **2.049 us**
- FF: **2.428 us**
- SS: **1.324 us**

## Mismatch screen

The final chosen lifecycle netlist was independently launched four times at each mismatch corner:

- 4 x `tt_mm`
- 4 x `ff_mm`
- 4 x `ss_mm`

Result:

**12/12 passed** the route/output/invalidation criteria.

The largest wrong-route excursion in these final launches was **0.0028 V**, far below a valid route's ~1.8 V.

This is still a small mismatch sample, not a production-yield Monte Carlo.

## Why template evidence was strengthened

An earlier integrated version failed one FF mismatch launch: the partial candidate won the analog soma race.

That version was rejected.

Instead of adding a digital comparator, v12S increased the already-present stable capacitive template evidence using a 2x2 um MIM branch and a clearer context event.

This raised the local exact-vs-partial dendritic separation to roughly **42.6-42.6 mV** nominally and removed the observed mismatch flip in the chosen screen.

The extra capacitor area/event load is accepted because it protects correctness.

## Self-locking and self-clearing Myelin

Another failed version froze the winning soma near a CMOS switching point so a later data operand could still see the route.

That burned hundreds of pJ in the query window.

The chosen design instead:

1. winner spike regeneratively sets one full-swing one-hot route latch;
2. route latch immediately closes the shared capture window;
3. only after capture is closed does `NOT(capture)` enable soma recovery;
4. both analog somas discharge into the recovery reservoir;
5. the full-swing route latch remains available for later new data;
6. cleanup-created loser spikes cannot create a second route because capture is already closed.

The TT physical-query VDD window is now **28.28 pJ** in this integrated test, compared with roughly 315 pJ in the rejected half-on-soma version.

The exact-fallback number in this netlist is only a tiny kernel stub and is **not** a fair full-digital-model energy comparison.

## Automatic recovery

The recovery reservoir is 10 pF.

During the TT accepted physical query it rose from:

- 0.199754 V
- to 0.224034 V

Stored reservoir-state gain:

**~51.4 fJ**

FF/SS are approximately 52.0/51.5 fJ.

This is stored capacitor energy only, not usable battery energy and not converter efficiency.

## Component count

Chosen schematic tile:

- SKY130 NFETs: 47
- SKY130 PFETs: 23
- total MOS: **70**
- PDK MIM capacitor instances: **14**
- explicit lumped capacitors: 21
- resistors: 4

This is a small demonstrator, not a final optimized layout.

## Parasitic stress

Real extraction could not be performed because the runtime contains the SKY130 technology files but no installed Magic/KLayout/OpenRCX extraction executable.

Rather than label a schematic as extracted, v12S added explicit parasitic stress.

Moderate profile added, among other loads:

- +3 fF to each 10 fF local dendrite;
- +20 fF to the shared run node;
- +20 fF to capture;
- extra SRAM/route-latch capacitance.

That profile passed TT/FF/SS and one mismatch launch at each corner.

At TT, even the deliberately extreme stress profile (+12 fF on each local dendrite, +100 fF on run and capture) still selected route 0 and produced the exact output, though latency/energy increased.

This is encouraging, but **not a substitute for extracted layout**.

## What is actually solved

**Solved at schematic transistor level:**

- all major fast-path components are in one netlist;
- physical lease identifies a hot region;
- sleep request is generated physically;
- exact VALID can locally install a pre-placed Myelin/template structure;
- Grammar + template evidence drives robust local competition;
- winner route becomes one-hot full-swing state;
- later new data uses that route in an exact kernel;
- route invalidation blocks the physical path;
- exact fallback still works;
- analog state is reclaimed automatically;
- hierarchical rebuild avoids whole-model scanning.

## What is not yet solved

**Actual extracted-layout validation is still missing.**

The next physical step is not another architecture invention. It is to place this chosen tile, route it, extract the real interconnect RC, and rerun the same lifecycle.

The acceptance battery is now fixed, so an extracted tile should be judged against:

1. lease request;
2. local VALID write;
3. programmed Myelin/template route;
4. one correct winner / zero wrong route;
5. new-data exact execution;
6. recovery;
7. error invalidation;
8. second-query physical block;
9. exact fallback.

If real extraction breaks a node, only that local structure should be redesigned; the architecture does not need to change pre-emptively.
