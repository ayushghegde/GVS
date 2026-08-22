# GVS / Neural Glyph — MAIN ARCHITECTURE

**Status:** authoritative integration document. Update this file after every experiment that changes what the system keeps, rejects, or how the pieces connect. Old experiment reports remain evidence; this file states the current combined architecture.

## 0. Primary objective

Build the cheapest practical hardware + software AI system that can become highly capable while reducing unnecessary data movement, memory reads, repeated routing, and duplicated support hardware. The architecture is not required to be purely analog, brain-like, digital, or computer-like. Experiments decide which representation belongs where.

Core rule:

`stable/reused/local structure -> physical/electrical when it wins`

`changing/rare/exact state -> exact computer hardware when it wins`

`ambiguity/failure -> exact fallback`

`long-distance communication -> robust meaning/results, not weak raw state`

## 1. Current whole-system flow

```text
external/sensory/event input
        |
        v
physical coordinate release / local-region selection
        |
        v
Regional Event Lease
        |
        +---- 8 isolated nearby event paths
        |
        v
local intelligent region
  - Tri-Wall / capacitive evidence
  - static templates
  - Grammar motif cells
  - short Passive Myelin
  - local competition / inhibition
  - familiarity / context / fatigue / homeostasis charge
  - direct fourth-face or autonomic tap routing
        |
        +---- confident local physical winner ----> robust event
        |
        +---- ambiguous / new / invalid ---------> exact fallback
        |
        v
regional robust routing / promoted Myelin chord / exact computer
        |
        v
result, action, or next local region
```

## 2. Existing physical front end

### Active-Low Coordinate Release
Four-transistor CMOS NOR releases a local selection only when row and column selection agree. It replaced the larger wake-boundary implementation.

### Regional Event Lease
One validated long coordinate selection can remain useful for a local burst. Only validated local winners/successes may refresh the charge state. Raw/noisy activity cannot refresh it. DONE/CLEAN may hard-clear it.

Current selected physical group: **8 isolated local paths per lease**.

Measured 8-way physical result from v13A4:
- 14 NFET + 2 PFET + 1 MIM in the shared interface;
- same bounding-box proxy as the earlier one-way interface in that layout;
- TT/FF/SS + 12 mismatch launches passed;
- lease/interface write + eleven refreshes ~106.8 fJ TT proxy;
- one selection + lease activity ~0.787 pJ versus ~5.44 pJ for eight separate long selections in the communication proxy.

## 3. Local stable computation primitives

### Capacitive ternary synapses — v12K
Stable synaptic values may be represented by physical MIM coupling when the physical connection is cheaper than repeated memory reads. Exact fallback handles exceptions.

### Shared templates — v12L/v12M
Repeated templates use physical/shared capacitive structure and static selector configuration. Per-event template-ID SRAM reads, one-hot selection, and naive binary decoders are not default.

### Grammar Cells — v12N -> v13A5/A6
Grammar detects repeated local motifs. The old fixed 0.500 V threshold is rejected. Current physical Grammar uses same-family MIM ratios and a robust mirrored/dual-pair reader when a robust decision is required.

Current closed physical Grammar readout:
- 10 legal MIM ratio array;
- 10-MOS dual-input-pair self-check reader, replacing the asymmetric 13-MOS analog swap reader;
- fresh motif replay for the two phases when conservative mode is required;
- current closure timing 6 ns/phase;
- nominal TT/FF/SS exact + partial pass;
- small combined MIM+MOS mismatch closure screen recorded with zero wrong accepts;
- full co-placed readout energy roughly tens of fJ, approximately 76–97 fJ in the current closure battery.

Use Grammar only when motif recognition removes larger downstream/routing work; do not put Grammar everywhere.

### Myelin
Passive Myelin is a short physical capacitive structural edge for repeated local paths. Full-swing Myelin carries robust meaning across stronger boundaries.

Deep passive analog Myelin chains are rejected: margin decays rapidly over hops. Regenerate locally or promote a direct chord when distance/reuse justifies it.

## 4. Tri-Wall / framework cell direction

### Tri-Wall Glyph Cell
Three capacitor faces supply local evidence; a fourth connection face exports to a neighboring/receptor path. In SKY130 this is emulated with legal planar MIMs because literal vertical sidewall MIM is not available in the present PDK.

Three ~2x2 um MIM-equivalent walls with the historical local state reproduce approximately the old three-input Grammar exact/partial voltage separation (~27 mV class first-order screen).

### Fourth-face link
A minimum NFET can connect local evidence to a small Contact Receptor. For ~0.5 V analog evidence, the gate must be strongly enabled; ~1.0 V gate compressed the signal badly while ~1.2 V preserved ~25 mV class separation in the physical/PDK screen.

The direct fourth face remains the preferred nearest-neighbor weak-analog connection because it presents the smallest load.

### Contact Receptor
Use a small landing capacitance instead of connecting one large cell state directly to another large membrane. This preserves more analog separation and prevents raw equal-capacitance charge dilution.

## 5. Hollow / volumetric framework architecture

Long-term physical interpretation:

- silicon/semiconductor exists where active devices require it;
- cell walls/ribs act as active structural framework rather than filling all volume with inactive silicon;
- inner/outer surfaces may host computation/capacitors;
- cavity/interior volume may hold whatever is useful at that scale: routing, memory, exact logic, power conversion/distribution, recovery storage, thermal structures, sensors/I/O, or package-scale chiplets;
- do not fill the interior with one continuous conductor because it destroys independent state/selectivity.

This is a future/custom-process/package direction. Present experiments emulate its electrical rules in ordinary SKY130.

## 6. Shared walls and protected service infrastructure

### Janus / Service Spine Wall
A neighboring pair of cells may share one structural wall instead of duplicating two shells. The weak analog capacitor surfaces remain separate. The protected middle carries robust/slow infrastructure behind shields.

Selected cross-section:

```text
cell A weak capacitor face
  dielectric
  shield/reference
  protected service lanes
  shield/reference
  dielectric
cell B weak capacitor face
```

Do not leave the shared middle floating. Earlier physical-capacitor behavior shows that a floating midpoint can couple a disturbance large enough to consume a significant fraction of the ~25 mV useful local signal.

v13C physical wall proxy:
- unshielded 100 um service line produced ~1.184 fF coupling to each weak face, enough for ~29 mV worst simple kick on the current ~72 fF evidence proxy -> rejected;
- shielded service spine removed direct service-to-evidence capacitance terms at extractor resolution in the tested geometry -> kept;
- two service lanes can coexist but couple to one another, so robust/slow lanes or extra shielding/orthogonal routing are preferred.

Service-wall lanes may carry:
- VDD/GND/reference;
- shared PVT/environment pilots;
- slow promotion/demotion/configuration;
- expired-charge recovery;
- robust winner/event traffic;
- Myelin-chord landing/control;
- exact-computer request/result when appropriate.

Do not carry tiny GC/GR/dendrite/latch-internal high-impedance signals in the service spine by default.

## 7. Routing hierarchy

Current routing is not one mechanism.

1. **Direct fourth face** — nearest-neighbor private weak analog relation.
2. **Segmented analog tap spine** — short local non-neighbor weak analog relation; unused segments/taps isolated.
3. **Protected event spine + local tap/receptor** — regional shared event/control; local capacitor walls recreate analog evidence at the destination.
4. **Myelin chord** — promoted stable/hot long-range direct relation through the local/framework routing volume.
5. **Exact/global fabric** — cold, changing, precise, or semantically uncertain relation.

Do not broadcast weak analog state to many permanently attached receivers. Load destroys margin.

## 8. Autonomic Tap Spine — v13D

A protected shared trunk may have small local subwires/taps into cells. Each tap owns local state; a central per-event router is not required.

Current architecture model showed:
- direct fourth face with 3 fF receptor preserves ~24 mV from a 25 mV source differential;
- one selected full shared-spine branch preserves ~20.9 mV first-order;
- all eight analog taps simultaneously attached to the full spine drops to ~16.8 mV -> reject;
- short segmented analog branches preserve ~23 mV class margin;
- regional event fanout is better carried as a ~0.2 V event and converted back into local analog evidence than by carrying the fragile ~25 mV analog difference across the whole trunk.

## 9. Decentralized physical state / Autonomic State Ladder

Use different physical mechanisms at the time scale each naturally handles best.

### Fast electricity
- events and evidence;
- local competition;
- repetition/familiarity;
- immediate context;
- temporary tap selection;
- inhibition.

### Medium stored charge
- Regional Lease;
- Use Reservoir / connection hotness;
- fatigue/homeostasis;
- short routing context;
- promotion probation.

### Slow environment physics
Use v11U/v12A-style replica leak/PVT sensors, not raw route activity, to modify promotion difficulty, retention and inhibition as temperature/process conditions change.

### Rare consolidation
Only after repeated local electrical evidence and conservative/exact validation may a relation become static/promoted Myelin/configuration.

### Future nonvolatile anchor
Magnetic/nonvolatile state is a future-process option for very stable verified configuration, not a per-event carrier and not required by SKY130.

## 10. Repetition, homeostasis and local learning

### v12E repetition
Old self-referenced firing charge naturally increased familiarity:
- first validated use ~1–2 mV class difference;
- second ~17 mV;
- third ~28 mV across the preserved screens.

Use this principle for fast physical probation/temporary tap promotion instead of inventing a digital reuse counter in every cell.

### v12F homeostasis
Pooled electrical activity may automatically increase inhibition when too many cells/taps participate. Reuse this to protect shared analog segments from excess simultaneous loading.

### v12G context
Short-lived electrical traces may directly steer future local inhibition/competition. Do not convert them into digital state unless a robust boundary requires it.

## 11. Self-setting fourth face / tap promotion

Only validated successful outcomes may train persistent/temporary connection state.

Selected lifecycle:

```text
raw event -> no training
validated repeated use -> local familiarity rises
familiarity sufficient -> temporary/probation tap
continued useful reuse -> slower Use/Lease state rises
stable validated relation -> promoted/static tap or Myelin
inactivity -> natural decay/demotion
```

The exact restored gate voltage needed depends on what is being transferred:
- ~0.5 V weak analog evidence needed roughly >=1.1–1.2 V in the tested fourth-face NFET;
- a ~0.2 V event requires much less gate overdrive and is the selected regional-spine transfer mode under v13E testing.

## 12. Energy lifecycle

Do not treat all discharge as waste, but do not disturb live information to harvest it.

Selected rule from v11S/U/V/W and v12I:

`live charge = information`

`controlled leak = adaptation / time / threshold`

`expired/reset charge = one-way recovery when worthwhile`

Older v12I expired-trace experiment recovered about 68.9% of removed trace energy into a low-voltage rail in that specific bench. This does not imply all energy is recoverable. Resistance, leakage, conversion, drivers and parasitics still dissipate energy.

The current framework should route cleanup/recovery only after the decision is captured.

## 13. Heat and magnetic roles

### Heat
Use temperature/leak physics as a slow **Thermal Brake**:
- hot/leaky region -> harder promotion, shorter retention, stronger inhibition;
- cooler region -> normal state returns.

Do not use heat to encode exact fast route identity. Do not count thermoelectric recovery unless a real thermal gradient and recovery device are measured.

### Magnetism
Future-process persistent verified configuration only. Electrical runtime remains primary. Current SKY130 does not include MRAM devices.

## 14. Exact computer boundary

Exact hardware remains necessary and is deliberately kept.

Use exact computation for:
- arithmetic/carry/index/pointer/code state;
- rapidly changing or rare knowledge;
- low-margin ambiguity;
- semantic invalidation/correction;
- verifying a relation before durable consolidation;
- cold/new cases where physical structure has not earned promotion.

The exact computer is not a central router for every local event. It is a precision/fallback/consolidation boundary.

## 15. Current physical correctness rules

- extraction, not DRC alone, determines electrical correctness;
- weak analog state remains local/short;
- robust meaning may travel farther/vertically;
- do not use fixed absolute Grammar thresholds across real MIM corners;
- raw/noisy activity cannot refresh leases or train persistent taps;
- do not place weak analog state in long series stacks or deep passive chains;
- capture decision before cleanup/recovery;
- inactive shared sources must remain electrically isolated;
- sharing is allowed only when it does not corrupt local decisions;
- physical cost includes communication, robust readout, fallback, driver, wire and support circuitry, not only the sub-fJ primitive.

## 16. Rejection handling

Every rejected result must be tagged:
- `PRINCIPLE_REJECTED`;
- `IMPLEMENTATION_REJECTED`;
- `MODE_ONLY`;
- `FUTURE_PROCESS`.

This prevents useful principles such as stored-leak adaptation, recovery, analog context, selective Grammar, and targeted 3D from being lost because one topology failed.

## 17. Current v13E integration target

v13E must finish the four-tap Autonomic Tap Spine physical/electrical closure and then build the first mixed local region.

Immediate closure battery:
1. shielded protected spine extraction;
2. four isolated local taps/subwires;
3. promoted event transfer at the lowest robust gate point;
4. one-active and multi-active fanout TT/FF/SS;
5. independent mismatch;
6. inactive-tap leakage/isolation;
7. familiarity/promotion policy from validated repetition;
8. homeostatic limit on weak analog simultaneous loading;
9. cleanup/recovery only after capture;
10. energy comparison against separate fourth-face/control routes.

After closure, populate one eight-way Regional-Lease region with multiple real Grammar/template/Myelin structures and measure useful local intelligent work rather than isolated primitives.

## 18. Maintenance rule

**After every experiment:**
1. keep the experiment report/results;
2. update this `MAIN_ARCHITECTURE.md` with every accepted/rejected architectural change;
3. update `NEXT_EXPERIMENT.md`;
4. update Decision Ledger / Do-Not-Reinvent if a principle or implementation changes status;
5. never leave the active architecture distributed only across version folders.
