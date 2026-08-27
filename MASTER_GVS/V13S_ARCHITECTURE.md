# GVS v13S — Adaptive Differentiated Venous Tissue

**Status: architecture/model pass + real SKY130 venule geometry pass; transistor slow-egress/PVT closure open.**

v13S keeps the accepted v13A Grammar/reader hardware, v13Q cell-as-local-wire and population confidence, and v13R differentiated cells + reservoir hierarchy. It makes differentiation more adaptive without returning to universal cells, changes recovery into a two-stage venous hierarchy, and reduces cell-library manufacturing complexity with a common base + role-specific patches.

## 1. Whole-system idea
The chip behaves less like identical processors connected to routers and more like tissue:
- most cells are physically differentiated and cheap;
- a small General Reserve population can change logical role when nearby functional populations stay overloaded;
- short information events continue through Embodied Conduction Cells themselves where that wins;
- expired charge leaves stateful cells into small local venules, then slowly reaches the Charge Artery;
- the regional reservoir remains between cell-scale recovery and the larger battery/collector;
- all differentiated cells share one common ECC base geometry and add only the role patches they need.

## 2. Role Pressure Field
**Role Pressure Field (RPF):** a persistent local need signal emitted when a role population cannot drain its work; General Reserve Cells integrate the signal and temporarily adopt the most under-supplied role.

This is the hardware analogue of developmental recruitment, not runtime transistor creation. Fixed Grammar/template/binding/constraint/exact cells remain physically fixed. Only the four broad General Reserve Cells in the current 64-cell model have the optional hardware needed to re-role.

### v13S0 evidence
Seven 120-epoch workload phases shift demand between mixed, Grammar-heavy, template-heavy, binding-heavy, constraint-heavy, exact-heavy and mixed-return operation.

Compared with fixed reserve roles:
- accumulated queue/backlog: 374,590 -> **102,786** (**72.56% lower**);
- max queue: 812 -> **335** (**58.74% lower**);
- ending queue: 553 -> **18**;
- only **40 reserve role changes over 840 epochs**.

An ideal instantaneous central oracle reaches backlog 88,218, so local RPF is only ~16.51% above the oracle in this model.

After a deterministic 10% specialized-cell loss at the midpoint, RPF reduces backlog **58.06%** versus fixed reserves.

A conservative carrier-support screen counts 1,769 role-pressure pulses. Charging four 0.67 fJ event-spine tap proxies per pulse gives only ~**0.156 fJ per completed modeled operation**. This is not a physical RPF energy measurement; it bounds the present model away from a high-energy hidden scheduler.

## 3. Two-Stage Venous Egress
**Local Venule:** a small shared post-expiry charge buffer serving several nearby stateful cells before the regional Charge Artery.

**Two-Stage Venous Egress:** `expired cell -> moderate cell/venule RC -> slower shared venule outlet -> Charge Artery -> regional reservoir -> battery/collector`.

The change solves a v13R tradeoff: one very slow direct drain is quiet but leaves dead charge inside the cell longer. v13S lets charge leave the cell sooner while the shared venule performs most of the smoothing.

### v13S1 selected model point
- cell -> venule tau ~2 local event intervals;
- venule -> artery tau ~8;
- one slow venule outlet per 8 cells.

Relative to direct tau=8 cell-to-artery egress on the same traces:
- spent charge remaining in the first-stage cell after 8 intervals: **~1.83%**;
- artery peak: uniform **2.57% lower**, bursty **19.30% lower**, aligned **28.29% lower**;
- regional-reservoir peak: **3.12-9.43% lower** across the three tests;
- modeled transfer fraction remains ~100% after drain time;
- slow venule outlets: 32 for 256 cells, **87.5% fewer** than one slow outlet/cell.

The eight-cell local venule reaches ~6.33 normalized cell-charge units in the aligned stress. Larger groups are allowed only if physical capacitance/area still wins.

## 4. Reservoir and battery hierarchy
The regional reservoir is retained because the Local Venule does not replace its functions.

Recovery hierarchy:
1. useful information/state;
2. normal expiry/isolation;
3. cell-to-venule transfer;
4. Local Venule smoothing;
5. Charge Artery;
6. regional shared reservoir;
7. slower battery/larger collector transfer.

The reservoir still supplies electrical buffering/decoupling, correlated-expiry surge absorption, isolation from the larger storage element, fault containment, slow battery-side transfer and optional low-voltage regional reuse where physically justified.

Correctness rule remains hard: live information state never drains merely to recover energy. Recovery failure loses energy only.

## 5. Common ECC Base + Expression Patches
**Expression Patch:** a small role-specific physical add-on attached to a common Embodied Conduction Cell base. Ordinary cells carry only the needed Grammar/template/binding/constraint/exact patch; General Reserve Cells carry a broader set.

This avoids both bad extremes: every cell containing every component, or every role requiring a completely unrelated full-cell layout.

### v13S3 cost sensitivity
For the current 64-cell differentiated composition:
- optional role-module copies: universal 320 vs patch fabric 60 -> **81.25% fewer**;
- 20,000 random module-weight trials: median total normalized hardware reduction **73.92%**; 5th percentile **65.72%**;
- in the 5th-percentile trial, saved hardware tolerates ~**3.75 base-cell cost units** of extra implementation/interface cost per installed patch before losing to the universal-cell baseline.

This is an abstract cost frontier, not a silicon-area or manufacturing-dollar measurement.

## 6. Physical venule placement
v13S2 uses Magic 8.3.681 and SKY130A tech `1.0.602-0-gf3c505b`, with a real recovered SKY130 NFET slow outlet and the preserved v13A reader GC/GR terminal geometry.

Both near-core and boundary layouts are **0 DRC** with correct `VENULE -> source`, `ARTERY -> drain`, `SLOW_GATE -> gate` connectivity.

Near-core routing gives matched direct coupling:
- VENULE -> GC: **0.00604839 fF**;
- VENULE -> GR: **0.00604839 fF**.

Using the preserved 72 fF screening node and 0.0903 V recovery swing gives ~0.0076 mV simple common-mode kick per side.

Moving the venule/outlet to the cell boundary removes any direct VENULE/ARTERY -> GC/GR capacitance term from the extracted file at Magic's reporting precision.

**Decision:** put venules at the cell/service boundary. Symmetry is helpful but not a reason to route recovery through weak evidence.

## 7. Differentiated cell anatomy
A practical v13S region contains a compact mix such as Relay ECC base only, ECC + Grammar patch, ECC + template patch, ECC + binding/context patch, ECC + constraint/competition patch, ECC + exact spatial patch, and a small General Reserve population with multiple patches.

Recovery is also differentiated. Tiny relay cells may omit a recovery tap entirely. Stateful/high-capacitance cells may connect to a Local Venule after expiry. One slow venule outlet is shared by a local group if physical sizing closes.

## 8. Information, charge and heat remain separate
Information routing remains flexible: face/edge/vertex aperture if economical, regenerative ECC chain, Nerve/subwire, event spine, promoted electrical/Myelin chord, then optional optical Light Nerve after real break-even.

Recovery uses Local Venule -> Charge Artery -> reservoir. Thermal Capillary/Artery remains passive and separate. The same contact is not reused for all three merely to reduce wire count.

## 9. What v13S rejects
- making every cell universal so it can adapt;
- a digital scheduler assigning cell roles every cycle;
- one slow recovery limiter per cell when a shared venule can do the smoothing;
- deleting the reservoir because a venule exists;
- unique full custom cell layout for every role/concept;
- routing venules through weak evidence because matched common-mode coupling looks small;
- pretending the current physical geometry result is transistor/PVT closure.

## 10. Evidence boundary / open problems
Still open: real slow-outlet ON current, OFF leakage/backflow, TT/FF/SS and mismatch, absolute Local Venule capacitance sizing, actual Expression Patch area/interface capacitance, physical RPF implementation/coupling, large multi-cell AI-quality workloads, and literal active all-surface 3-D manufacturing.

The supplied ngspice source is revision 26 and is too old for the current SKY130 combined model deck. The official current ngspice release is substantially newer; this runtime could verify its availability but could not transfer the external archive into the local sandbox. No simplified MOS model is substituted for signoff.

## 11. Current v13S decision
### KEEP
- v13Q cell-as-local-wire + population confidence;
- v13R fixed differentiation for ordinary cells;
- four-ish General Reserve Cells as a tunable local reserve, not a law;
- Role Pressure Field for slow reserve recruitment;
- two-stage cell -> Local Venule -> Charge Artery recovery;
- regional reservoir before battery/collector;
- common ECC base + Expression Patch library;
- wall/boundary placement of communication and recovery devices.

### PHYSICALLY CONDITIONAL
- eight-cell venule grouping;
- tau 2 / tau 8 model point;
- exact role counts;
- patch granularity;
- any diagonal contact or optical path.

## 12. Next — v13S4 Adaptive Tissue Physical Closure
Use a current SKY130-compatible simulator and build one physical differentiated mini-tissue containing common ECC bases, one Relay cell, one Grammar/state cell, one General Reserve cell with two Expression Patch options, wall communication aperture, per-state post-expiry isolation, one shared Local Venule/slow outlet, Charge Artery + regional reservoir equivalent, and the preserved weak GC/GR pair.

Close DRC/extraction, aperture ON/OFF, cell->venule emptying, venule->artery smoothing, backflow, simultaneous communication+recovery, TT/FF/SS, mismatch, RPF switching disturbance, and total area/energy versus v13R one-tap-per-cell + fixed-role baseline.

If the expression patch interface or adaptive reserve costs more than it saves, coarsen/remove it. If the venule does not improve cell reuse + reservoir stress together after real device sizing, return to direct SCE for the affected cell type.
