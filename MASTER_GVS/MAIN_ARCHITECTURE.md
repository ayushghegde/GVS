# GVS / Neural Glyph — MAIN ARCHITECTURE

**Status:** authoritative combined architecture through v13J4. Update after every architecture-changing experiment. Version folders keep evidence and failures; this file states the current system.

## 0. Design objective and non-negotiable rules
Build the cheapest practical hardware + software AI system that can remain highly capable while minimizing unnecessary memory reads, conversions, data movement, routing and duplicated support hardware.

Rules:
- stable/reused/local structure -> physical implementation when total cost wins;
- changing/rare/exact state -> exact computer hardware;
- ambiguity/failure -> exact fallback;
- weak analog state stays local/short;
- robust meaning/results may travel farther;
- locality is part of computation;
- raw/noisy activity may not refresh leases or train persistent routes;
- live charge = information; controlled leak = time/adaptation; expired charge may be recovered;
- capture/validate before cleanup/recovery;
- sharing is accepted only when it does not corrupt local decisions;
- DRC alone is insufficient; extraction/connectivity is authoritative;
- a failed implementation does not automatically reject the principle.

## 1. Whole-system flow
```text
input / sensor / exact data
        -> Active-Low Coordinate Release
        -> 8-way Regional Event Lease
        -> local intelligent Glyph region
             Tri-Wall capacitive evidence
             static templates
             Grammar motifs
             short Passive Myelin
             direct analog steering when destination already has a membrane
             local competition / inhibition
             familiarity / context / fatigue / homeostasis
             direct fourth-face links
             segmented taps / Autonomic Event Spine
        -> confident local winner -> robust event
        -> ambiguous/new/invalid -> exact fallback
        -> representation + carrier + volume compiler
             local electrical / Myelin
             regional event spine
             dedicated electrical chord
             optional thin TIR optical chord only after break-even
        -> next region / exact computer / output
```

The exact computer is a precision/fallback/consolidation boundary, not the per-event central router.

## 2. Physically/electrically closed front end
### Active-Low Coordinate Release
4-transistor CMOS NOR; selected row+column agreement releases the local region.

### 8-way Regional Event Lease
Validated long selection is reused for a local burst. Raw activity cannot refresh it.

Selected v13A4 interface:
- 14 NFET + 2 PFET + 1 MIM;
- TT/FF/SS + 12 mismatch launches pass;
- write + 11 refreshes ~106.8 fJ TT proxy;
- one selection + lease ~0.787 pJ versus ~5.44 pJ for eight independent long selections in the earlier proxy.

## 3. Local computation primitives
### Capacitive ternary synapses — v12K
Stable local weights may be physical MIM coupling; exact residual handles exceptions.

### Shared templates — v12L/v12M
Repeated templates use shared capacitive structure/static configuration rather than repeated per-event memory/decoder work when cheaper.

### Grammar — v12N -> v13A5/A6
Fixed 0.5 V threshold is rejected. Selected robust Grammar uses:
- legal 10-MIM physical ratio array;
- 10-MOS dual-input-pair self-check reader;
- fresh replay for conservative two-phase checking;
- 6 ns/phase selected closure;
- nominal TT/FF/SS exact+partial pass;
- combined MIM+MOS mismatch screen with zero wrong accepts;
- co-placed readout energy roughly 76–97 fJ in the closure battery.

Use Grammar selectively when motif recognition removes larger work/routing.

### Direct analog steering — v12G/v13B
If the destination already has a local membrane/competition node, weak state may directly steer it instead of paying a separate reader. Robust reader remains for true boundaries.

### Myelin
- Passive Myelin: short local capacitive structural edge;
- Full-Swing Myelin: robust boundary/event link;
- deep passive analog chains are rejected because signal margin and absolute level decay;
- stable distant relations may earn a direct electrical or future optical chord.

## 4. Tri-Wall / framework cell
### Tri-Wall Glyph Cell
Three capacitor faces supply evidence; fourth side is controlled connection/output. SKY130 currently emulates literal walls with legal planar MIMs.

Three ~2x2 um MIM-equivalent walls reproduce ~27 mV-class historical exact/partial separation in the current first-order model.

### Fourth-face link
Minimum NFET + small Contact Receptor.
- ~0.5 V analog evidence needed ~1.1–1.2 V gate class in tested screens to preserve ~25 mV separation;
- ~0.2 V robust regional events pass much more easily.

Direct fourth face remains the preferred nearest-neighbor route.

### Contact Receptor
Small landing capacitance prevents large membrane-to-membrane charge dilution.

## 5. Autonomic Tap Spine — v13D/v13E
Protected shared trunk with isolated local subwires/taps. Each tap owns local physical state.

Closed v13E four-tap result:
- shielded ~180 um spine with four isolated branches;
- promoted-tap gate selected at **0.9 V**;
- nominal TT/FF/SS pass;
- **12/12 independent TT/FF/SS mismatch launches pass**;
- selected outputs retain essentially full ~0.2 V event;
- inactive taps remain microvolt-class;
- protected analog disturbance ~0.344 mV in the current coupling proxy.

Event-source proxies:
- direct fourth-face neighbor ~0.15 fJ;
- ~180 um spine one tap ~0.67 fJ;
- four taps ~1.34 fJ.

### Familiarity / promotion — v12E
Electrical repetition replaces a digital counter in the fast path:
- first validated use ~1–2 mV familiarity class;
- second ~17 mV;
- third ~28 mV in preserved screens.

Lifecycle:
`validated repetition -> probation -> temporary tap -> slower Use/Lease state -> promoted route`; inactivity demotes it.

### Homeostasis — v12F
Pooled activity increases inhibition/selection pressure when too many weak analog participants load one segment.

### Short electrical context — v12G
Recent charge directly steers future local competition/inhibition when margin is adequate.

## 6. Shared silicon/framework walls
### Janus / Service Spine Wall
Two neighboring cells may share one structural wall. Weak capacitor faces remain isolated; robust/slow services run through the middle behind shields.

Selected stack:
`weak face A -> dielectric -> shield -> service lanes -> shield -> dielectric -> weak face B`.

v13C physical proxy:
- unshielded 100 um service line ~1.184 fF coupling to each weak face -> ~29 mV simple kick -> rejected;
- shielded geometry removed direct service-to-evidence capacitance terms at extractor resolution -> kept;
- multiple service lanes require robust signaling/extra shielding/orthogonal routing.

Service lanes may carry VDD/GND/reference, PVT pilots, configuration, recovery, robust events, Myelin control and exact requests/results. Do not carry tiny GC/GR/dendrite/latch-internal nodes there by default.

## 7. Hollow / volumetric architecture
### Hollow-Electrical Base — default product architecture
The default package/chip concept is a hollow/framework electrical system:
- active semiconductor only where devices need it;
- inner/outer framework surfaces used for cells/capacitors;
- fourth faces + subwires + event spines + electrical Myelin;
- component bays for exact memory/logic/support where locality wins;
- shared thermal exhaust;
- facade/backside utilities if packaging cost is acceptable;
- exact fallback independent.

This is the **lowest-manufacturing-complexity selected architecture today**.

### Heterogeneous Void Fabric
Interior space is assigned by function rather than maximally filled or maximally empty:
- active framework/wall zone;
- component bays;
- thermal exhaust/arteries;
- narrow optional optical/lightpipe lanes;
- structural/alignment ribs;
- reserve/bypass volume.

Do not fill the interior with one continuous conductor/network.

## 8. Facade Utility Shell — v13J
Outside/backside/sidewall surfaces may host robust shared utilities analogous to pipes/tanks/services on a building.

### Facade Utility Shell
Good facade candidates:
- power/reference;
- recovery/decoupling banks;
- configuration/test/repair;
- ESD/I/O support;
- large regulators/support devices;
- thermal manifold/condenser interface;
- optional optical source/coupling bank;
- sparse fault bypass.

Keep weak/local/frequent analog computation inside/protected framework.

Illustrative 10x10x2 mm, 32-region geometry:
- exterior area ~280 mm^2;
- sidewalls ~80 mm^2;
- naive dedicated central-collector routes total ~176 mm;
- distributed top/bottom quadrant-bank facade routes total ~96 mm in the refined model -> ~45.5% shorter than that naive central arrangement.

Outside wiring did **not** shorten ordinary cell-to-cell shortest paths in the tested graph, so duplicating the full nervous network on the facade is rejected.

Sparse facade bypass improved graph resilience under heavy random edge loss and is retained as robust utility/fault infrastructure.

This direction is consistent with backside-power research: moving robust power/services to the backside can reduce frontside signal congestion and can support backside I/O/ESD and dense decoupling structures. This is supporting precedent, not proof of literal GVS facade fabrication.

## 9. Facade Quiet Window — v13J3
Shielding does not allow unlimited simultaneous high-swing facade activity near weak analog nodes.

Using the conservative existing ~0.124 fF protected-branch coupling proxy with a ~72 fF weak node and ~25 mV useful differential:
- one 0.9 V utility step -> ~1.55 mV kick;
- one 1.2 V step -> ~2.06 mV;
- one 1.8 V step -> ~3.09 mV.

Against the current 18 mV high-margin screen:
- up to 4 aligned 0.9 V transitions remain above ~18.8 mV;
- up to 3 at 1.2 V;
- up to 2 at 1.8 V.

Normal policy is stricter: **freeze/stagger high-swing facade transitions during weak analog accumulation; resume after result capture.** Emergency robust activity may force fallback rather than silently accept a disturbed analog result.

## 10. Reservoir and energy lifecycle
### Core rule from v11/v12
`LIVE charge = information / lease / context / familiarity / adaptation`

`controlled leak = time/environment/self-regulation`

`EXPIRED charge = recover one-way if worthwhile`

Do not harvest from live high-impedance state.

### v13E tiny recovery reference
Simple expired tap-gate bench recovered ~53% of removed gate energy into a low-voltage rail; old v12I trace bench recovered ~68.9% in its own geometry. These are not universal fractions.

### v13P12 regional shared reservoir — reused in v13J
One 10 pF reservoir shared across four tiles:
- replaced 40 pF total separate recovery capacitance with 10 pF target -> 75% reduction;
- nominal TT/FF/SS pass;
- 12/12 mismatch launches, 48 tile instances pass;
- weakest post-error second-request minimum remained above 0.9 V;
- ~220 fJ capacitor-energy increase in one four-tile recovery interval.

The 10 pF reservoir is still a lumped physical candidate, not a completed exterior bank PEX.

### Hierarchical Reservoir Collector
Selected hierarchy:
`local reservoir computes -> expires -> regional shared reservoir -> safe-window drain -> larger facade/chip collector -> infrequent converter/low-voltage reuse`.

Do not put one active converter on every tiny reservoir.

The old tiny-packet screen showed chip conversion overhead only amortizes at large batch sizes. Reusing the larger ~220 fJ regional packet makes the second stage much more plausible.

## 11. Autonomous Recovery Backpressure — v13J4
The regional reservoir is a buffer, not a permanent battery.

First-order 10 pF energy-accumulation screen starting near 0.199 V with ~220 fJ packets:
- 1 packet -> ~0.289 V;
- 2 -> ~0.357 V;
- 4 -> ~0.464 V;
- 5 -> ~0.510 V;
- 8 -> ~0.626 V;
- 16 -> ~0.862 V;
- 18 -> ~0.912 V.

Therefore do not hold hundreds of packets in a small regional capacitor. Drain the regional bank every one/few recovery episodes when safe; perform large batching only in the bigger downstream chip/facade collector.

### Autonomic Recovery Gate
Conceptual local control:
`RECOVERY_PRESENT & CAPTURED_OR_DONE & !WEAK_ANALOG_ACTIVE -> allow facade drain`.

The reservoir voltage itself can represent recovery urgency/backpressure; no digital event counter is required in the fast path. Exact threshold/device still needs PVT/self-referenced physical closure.

Failure policy:
- stuck-open recovery path must not be allowed to load live state;
- stuck-closed path may lose recovery efficiency but must not break inference correctness;
- overfull bank triggers conservative drain/fallback, never threshold corruption.

## 12. Routing hierarchy
1. direct fourth face — nearest neighbor private analog/event;
2. segmented analog tap — short non-neighbor weak analog;
3. shielded electrical event spine — regional robust event/fanout;
4. dedicated electrical/Myelin chord — stable short/medium relation;
5. optional thin TIR optical chord — long/hot route only after lifetime break-even;
6. contactless capacitive/inductive bridge — tiny assembly gaps only when packaging needs it;
7. RF/mmWave — rare broadcast/discovery/backup;
8. exact/global fabric — cold/changing/precise/semantically uncertain.

## 13. Optional Photonic Layer — not default
Thin TIR/direct-photocharge photonics is an optional package/region upgrade only when route distance, reuse and source-idle behavior repay manufacturing and running cost.

Selected v13I conservative eight-region expected-lifetime screen:
- 16 uses/relation -> no optical-economic routes;
- 32 uses, 50% hot -> ~8.17% expected communication saving;
- 64 uses, 50% hot -> ~22.34%;
- 128 uses, 50% hot -> ~30.46%;
- 256 uses, 50% hot -> ~34.52%.

At 10 mm / 64 uses / 50% eligibility, preserved workload total improvement:
- image ~0.125%;
- sound ~0.171%;
- code ~13.97%;
- reasoning ~1.40%.

Thus photonics is a route-dominated optimization, not a universal whole-chip win.

Optical source idle/start/tuning energy is a hard acceptance term. At 10 mm / 64 uses only ~10.97 fJ/event advantage remains after the modeled route-write amortization; if the source cannot stay below the corresponding utilization budget through sharing/power-gating, keep the route electrical.

Weak optical analog evidence must be differential/self-referenced, never one absolute light threshold.

## 14. Thermal architecture
### Thermal Brake
Replica-leak/PVT state changes promotion/retention/inhibition as temperature/process conditions change. Heat is slow environment physics, not fast route identity.

### Shared Thermal Exhaust
Do not harvest every tiny heat source locally. Many regions/chips send heat through component-free vapor/heat-pipe/microfluidic exhaust to a common top/package/rack collector.

Sequence:
`hot framework -> spreader/wick -> hollow thermal route -> condenser/heat exchanger -> optional large TEG -> external heat sink/useful heat loop`.

Cooling has priority over harvesting. Low-grade electrical heat conversion is secondary; useful heat export may be much larger.

## 15. Other physics status
- capacitive contactless coupling: MODE_ONLY for tiny assembly gaps;
- inductive coupling: MODE_ONLY for isolated/vertical gaps;
- RF/mmWave: MODE_ONLY broadcast/backup;
- phononic/acoustic: MODE_ONLY filters/sensors/delay, reject normal routing;
- magnetism/MRAM: FUTURE_PROCESS persistent verified state only;
- MEMS/PCM optical switches: FUTURE_PROCESS rare route consolidation, not per-event switching;
- alpha particles: REJECT runtime carrier; KEEP only as radiation-fault model;
- wireless power: reject as default because protected service-wall power is cheaper/controllable.

### Radiation Quarantine Rule
One isolated high-amplitude transient may not train a persistent route or refresh the lease. Promotion still requires repeated validated success; suspicious uncorrelated spikes are invalid/noise unless normal timing/context validation confirms them.

## 16. Compilers
### Representation compiler
Chooses Grammar/template/Myelin/exact representation.

### Carrier + volume + placement compiler
Chooses:
- fourth face;
- segmented tap;
- event spine;
- electrical chord;
- optional TIR optical chord;
- wall/facade service lane;
- component bay;
- thermal path;
- recovery collector;
- fallback route.

Placement tendency:
`weak + frequent + local -> inside/protected framework`

`robust + shared + slow/large/hot -> wall/facade/exterior if total cost wins`.

A good representation may eliminate a communication before the carrier compiler routes it.

## 17. Current evidence status
### Physically/electrically closed in current SKY130 flow
- Active-Low Coordinate Release;
- 8-way Regional Lease/interface;
- 10-MIM + 10-MOS robust Grammar readout;
- physical Tri-Wall/fourth-face screens;
- shielded service-wall proxy;
- four-tap Autonomic Event Spine at 0.9 V with 12/12 mismatch closure;
- v13P12 10 pF / four-tile regional shared-recovery circuit result (lumped reservoir, not exterior layout).

### Architecture/circuit/system model or outside-process future target
- literal hollow/vertical framework;
- Facade Utility Shell physical package;
- regional-to-facade recovery converter;
- Autonomic Recovery Gate physical implementation;
- thin TIR photonics/direct photocharge;
- Optical Dendrites/fanout;
- integrated vapor/microfluidic thermal exhaust;
- MEMS/PCM/magnetic route anchors.

Never label future-process/model values as fabricated GVS measurements.

## 18. Current next physical closure target
Build one same-die electrical proxy that combines:
- real Grammar/evidence node;
- robust VALID/CAPTURED/DONE;
- one facade-equivalent shielded utility/recovery line;
- one Recovery Valve / Autonomic Recovery Gate;
- one regional shared reservoir branch;
- facade transitions at 0.9/1.2/1.8 V during and after weak analog windows;
- post-capture recovery;
- TT/FF/SS + independent mismatch;
- deliberately forced simultaneous utility switching to measure the true fallback boundary.

Only after this electrical interface closes should the literal facade/backside package be promoted as a physical implementation target.

## 19. Maintenance rule
After every experiment:
1. preserve raw results and failures;
2. update this MAIN_ARCHITECTURE.md;
3. update NEXT_EXPERIMENT.md;
4. update decision/do-not-reinvent records when status changes;
5. label evidence type: measured PDK/layout, circuit model, system proxy, or external literature;
6. never leave the active architecture distributed only across version folders.
