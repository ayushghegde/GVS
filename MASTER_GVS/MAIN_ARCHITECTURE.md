# GVS / Neural Glyph — MAIN ARCHITECTURE

**Status:** authoritative integration document. Update after every architecture-changing experiment. Old experiment folders remain evidence; this file states the combined current system.

## 0. Objective and rules
Build the cheapest practical hardware + software AI that can still become highly capable. Do not choose analog, digital, optical or brain-like hardware in advance; use the representation/physics that wins after real communication, area, energy, latency, correctness and support costs.

Core rules:
- stable/reused/local structure -> physical/electrical when it wins;
- changing/rare/exact state -> exact computer hardware;
- ambiguity/failure -> exact fallback;
- weak analog state stays local/short;
- robust meaning/results may travel farther;
- live charge = information; controlled leak = adaptation/time; expired charge may be recovered;
- raw/noisy activity may not train leases/promoted routes;
- DRC alone is insufficient: extraction/connectivity determines physical correctness;
- keep failed experiments and tag whether the principle or only the implementation failed.

## 1. Whole-system flow
```text
input / sensor / exact data
        -> physical coordinate release
        -> Regional Event Lease
        -> eight isolated local paths
        -> local intelligent Glyph region
             Tri-Wall capacitive evidence
             static templates
             Grammar motifs
             short Passive Myelin
             local competition/inhibition
             familiarity/context/fatigue/homeostasis
             direct fourth-face / tap routing
        -> confident physical winner -> robust event
        -> ambiguous/new/invalid -> exact fallback
        -> carrier+volume compiler chooses next route
             electrical/Myelin
             event spine
             future thin TIR optical chord
        -> next region / exact computer / output
```
The exact computer is a precision/fallback/consolidation boundary, not the per-event router.

## 2. Closed physical front end
### Active-Low Coordinate Release
4-transistor CMOS NOR releases a local selection only when row+column agree.

### Regional Event Lease
Validated long selection can be reused locally; only validated success/winners refresh it. DONE/CLEAN hard-clear remains available.

Selected 8-way physical interface from v13A4:
- 14 NFET + 2 PFET + 1 MIM;
- TT/FF/SS + 12 mismatch launches passed;
- write + 11 refreshes ~106.8 fJ TT proxy;
- one selection + lease ~0.787 pJ versus ~5.44 pJ for eight independent long selections in the earlier communication proxy.

## 3. Local stable computation
### Capacitive ternary synapses — v12K
Physical MIM coupling represents stable local synaptic structure when cheaper than repeated memory reads. Exact residual handles exceptions.

### Shared templates — v12L/v12M
Repeated templates use shared capacitive structure + static configuration; avoid per-event template SRAM reads/one-hot/naive decoders when they are more expensive.

### Grammar — v12N -> v13A5/A6
Fixed 0.5 V Grammar threshold is rejected. Current physical Grammar uses a legal 10-MIM ratio array plus a 10-MOS dual-input-pair self-check reader when a robust decision is needed.

Closed readout state:
- fresh replay for conservative two-phase check;
- 6 ns/phase selected;
- TT/FF/SS exact+partial pass;
- combined MIM+MOS small mismatch screen closed with zero wrong accepts;
- co-placed readout energy ~76–97 fJ in that battery.

### Direct analog steering
If the destination already has a membrane/competition node, local evidence may directly steer it instead of paying a separate robust reader. Keep the robust reader for true boundaries.

### Myelin
- Passive Myelin = short local capacitive structural edge;
- Full-Swing Myelin = robust boundary link;
- deep passive analog chains are rejected because margin decays;
- stable distant relations may earn a direct electrical or future optical chord.

## 4. Tri-Wall / framework cell
### Tri-Wall Glyph Cell
Three capacitor faces provide local evidence; a fourth connection face exports to a neighbor/receptor. SKY130 emulates literal sidewalls with legal planar MIMs.

Three ~2x2 um MIM-equivalent walls reproduce ~27 mV-class historical exact/partial separation in the present first-order cell model.

### Fourth-face link
Minimum NFET + small Contact Receptor.
- ~0.5 V analog evidence needed ~1.1–1.2 V gate class to preserve ~25 mV separation in the tested physical/PDK screen;
- robust ~0.2 V regional events are easier to transfer.

### Contact Receptor
Small landing capacitance prevents one large cell membrane from charge-sharing directly into another large membrane.

## 5. Autonomic Tap Spine — v13D/v13E
Shared protected trunk with local subwires/taps; each tap owns local state instead of a central per-event router.

Closed four-tap result:
- shielded ~180 um spine, four isolated branches;
- selected promoted-tap gate = **0.9 V**;
- nominal TT/FF/SS pass;
- **12/12 TT/FF/SS independent mismatch launches pass**;
- selected outputs essentially retain full ~0.2 V event;
- inactive taps microvolt-class;
- protected analog disturbance ~0.344 mV in current coupling proxy.

Event-source proxies:
- direct neighbor fourth face ~0.15 fJ/event;
- ~180 um event spine one tap ~0.67 fJ;
- four taps ~1.34 fJ.

Therefore fourth face remains the nearest-neighbor winner; the event spine is the next scale.

### Familiarity / promotion
Reuse v12E self-referenced repetition rather than a digital counter in every cell:
- first use ~1–2 mV familiarity class;
- second ~17 mV;
- third ~28 mV across preserved screens.

Lifecycle:
`validated repetition -> probation -> temporary tap -> slower Use/Lease state -> promoted route`; inactivity leaks it away.

### Homeostasis
Reuse v12F pooled electrical homeostasis to suppress too many simultaneous weak-analog participants before loading destroys margin.

### Electrical context
Reuse v12G short electrical traces to steer future local inhibition/competition directly when safe.

### Recovery
After capture, expired tap/configuration charge may be recovered one-way. Current simple v13E tap-gate bench recovered ~53% of removed gate energy; older v12I trace bench recovered ~68.9% in its own geometry. Neither is a universal fraction.

## 6. Shared silicon/framework walls
### Janus / Service Spine Wall
Two cells may share one structural wall. Weak capacitor faces remain isolated; shielded robust/slow services run through the middle.

Selected stack:
`cell A weak face -> dielectric -> shield -> service lanes -> shield -> dielectric -> cell B weak face`.

v13C physical proxy:
- unshielded 100 um service line ~1.184 fF coupling to each weak face, enough for ~29 mV simple kick -> rejected;
- shielding removed direct service-to-evidence terms at extractor resolution in the tested geometry -> kept;
- multiple service lanes may coexist but require robust signaling/extra shielding/orthogonal routing.

Wall services may carry VDD/GND/reference, PVT pilots, configuration, recovery, robust events, Myelin control and exact requests/results. Do not place tiny GC/GR/dendrite/latch-internal nodes on the service spine.

## 7. Hollow / Heterogeneous Void Fabric
The interior is neither completely empty nor maximally filled.

Functional zones:
- **Active framework/wall zone:** cells, capacitors, fourth faces, service wiring;
- **Thin optical-lightpipe lanes:** long/hot routes only;
- **Thermal Exhaust/Artery:** component-free heat transport path to a shared external manifold;
- **Component Bay:** memory, exact logic, recovery support, sensors/I/O when communication savings repay area/heat;
- **Structural/alignment ribs:** mechanics + protected services;
- **Reserve/bypass volume:** fault rerouting and future promotion.

Do not fill the interior with one conductor/network: it destroys independent state/selectivity.

## 8. Routing hierarchy
1. Direct fourth face — adjacent private weak analog/event.
2. Segmented analog tap — short non-neighbor weak analog.
3. Shielded event spine — regional shared robust event/fanout.
4. Dedicated electrical/Myelin chord — stable short/medium route while wire is cheapest.
5. **Thin TIR Optical Chord** — future long/hot relation only after distance+reuse break-even.
6. Capacitive/inductive contactless bridge — only tiny assembly gaps where eliminating galvanic bonds solves packaging/yield.
7. RF/mmWave — rare broadcast/discovery/backup, not normal local reasoning.
8. Exact/global fabric — cold/changing/precise/semantic uncertainty.

## 9. Thin TIR Optical Chord — v13F/v13G/v13H
### Why thin TIR instead of a large empty corridor
Ordinary total internal reflection requires a higher-index guiding core; therefore the selected near-term hollow route is a skinny transparent glass/polymer lightpipe through the cavity, not a large air corridor. True hollow/air-core anti-resonant guidance is future research only.

Literature-backed v13H proxy:
- ~0.08 dB/cm propagation;
- ~0.47 dB/facet coupling;
- direct-photocharge target ~0.600 fJ detector-incident energy for a 3 fF receptor at 0.2 V and 80% detector QE;
- laser wall-plug scenario 15%;
- modulator proxy 5.9 fJ/event.

Runtime optical event work is ~10.9–11.1 fJ over 3–20 mm because endpoint energy dominates propagation.

Fair electrical comparison uses improved dedicated-route proxy:
`E_electrical ~= 0.15 + 3.74*d_mm fJ/event`.

Including a 1 pJ rare route-write cost, approximate reuse break-even:
- 3 mm ~2102 uses;
- 5 mm ~126;
- 10 mm ~38;
- 15 mm ~23;
- 20 mm ~16.

So optics is **not** selected for ordinary local traffic. Distance and reuse must both justify it.

### Optical route volume
A demonstrated ~9x9 um guide core is ~0.00081 mm^3 over 10 mm; even a conservative 50x50 um reserved lane is ~0.025 mm^3 over 10 mm. Optical routing therefore need not reserve component-sized empty volume.

### Direct Photocharge Receptor
Future photonic-process candidate:
`light -> photodiode -> local charge -> local physical competition`, avoiding a conventional receiver amplifier when margin permits.

Weak optical analog use must be differential/self-referenced, never one absolute intensity threshold.

### Optical Dendrite / Fanout
Future sparse long-range option:
- multiple distant sources may deposit charge into one local receptor when pooled evidence is semantically acceptable;
- one source may fan out to several direct-photocharge receptors;
- source identity is lost in pooled fan-in, so exact/code identity-sensitive signals stay separate/electrical.

## 10. v13H fair hollow-versus-all-electrical qualification
Eight regions were modeled at corners of an illustrative 10 mm cube. Pair distances: 12 at 10 mm, 12 at 14.14 mm, 4 at 17.32 mm. Every relation is allowed the improved dedicated electrical route; optics is selected only when lifetime total including 1 pJ write is lower.

Communication-lifetime results:
- 16 uses/relation -> no optical promotion wins;
- 32 uses, 50% hot -> ~14.7% communication saving;
- 64 uses, 50% hot -> **~31.0%**;
- 64 uses, all hot -> **~44.7%**;
- 128 uses, all hot -> ~60.9%;
- 256 uses, all hot -> ~69.0%.

This is the first fair qualification against the improved electrical route rather than only the old 0.68 pJ global-coordinate proxy.

Using preserved v13A image/sound/code/reasoning cores with 10 mm long relations, 50% optical eligibility and 64 lifetime uses:
- image whole-workload improvement vs improved all-electrical ~0.12%;
- sound ~0.17%;
- code **~14.0%**;
- reasoning ~1.4%.

Therefore hollow optics is most valuable where communication is a large fraction of useful work; local image/sound computation remains predominantly electrical/capacitive.

## 11. Thermal architecture
### Thermal Brake
Local replica-leak/PVT state changes promotion/retention/inhibition when a region becomes hot. Heat is slow environment physics, not fast route identity.

### Shared Thermal Exhaust / Artery
User-selected scale rule: do **not** harvest every tiny heat source locally. Many chips/regions dump heat into component-free hollow exhaust paths that lead to one larger top/package/rack collection system.

A literal evacuated empty channel is not a high-power heat conveyor by itself; radiation at modest chip temperatures is too weak. Selected physical direction is hollow vapor-chamber / heat-pipe / microfluidic exhaust with conducting walls/wicks/working fluid, while remaining empty of computing components.

Sequence:
`hot framework -> spreader/wick -> hollow vapor/exhaust route -> top condenser/heat exchanger -> optional TEG -> outside/facility heat sink or useful heat loop`.

Place the thermoelectric stage at the external collection boundary so it does not add thermal resistance to every cell.

A 2025 external rack model reported 125 W TEG output from 25 kW heat (~0.5%), 219 W in a dual-stage variant (~0.876%), and ~20.1 kW useful hot-water output. GVS uses those only as scale scenarios, not measurements. Primary goal is cooling + useful heat export; electrical heat harvesting is secondary.

## 12. Other physics
- capacitive contactless coupling: MODE_ONLY for micrometer assembly gaps;
- inductive coupling: MODE_ONLY for isolated/vertical gap links;
- RF/mmWave: MODE_ONLY broadcast/backup;
- phononic/acoustic: MODE_ONLY filters/sensors/delay, reject normal routing;
- magnetism/MRAM: FUTURE_PROCESS persistent verified state only;
- MEMS/PCM optical switches: FUTURE_PROCESS rare route consolidation, not per-event switching;
- wireless power: reject as default because protected service-wall power is cheaper/controlled.

## 13. Exact computer boundary
Keep exact hardware for arithmetic/carry/index/pointer/code state, rapidly changing/cold knowledge, low-margin ambiguity, semantic invalidation, correction, and route consolidation verification. Do not force these functions into analog/optical physics merely for purity.

## 14. Compilers
### Representation compiler
Chooses Grammar/template/Myelin/exact representation.

### Carrier + volume compiler
Chooses fourth face, segmented tap, event spine, electrical chord, thin TIR optical chord, component bay, thermal path and fallback route.

A representation is optimized first: if local Grammar/Myelin removes a communication entirely, the carrier compiler does not route it.

## 15. Current acceptance status
### Physically/electrically closed in current SKY130 flow
- Active-Low Coordinate Release;
- 8-way Regional Lease/interface;
- 10-MIM + 10-MOS robust Grammar readout;
- physical Tri-Wall emulation / fourth-face screens;
- shielded service-wall proxy;
- four-tap Autonomic Event Spine at 0.9 V with 12/12 mismatch closure.

### Model/literature-backed future-process architecture
- literal hollow/vertical framework fabrication;
- thin TIR photonic lightpipes and direct photocharge endpoints;
- Optical Dendrites/fanout;
- vapor/microfluidic thermal exhaust integrated into hollow volume;
- MEMS/PCM/magnetic persistent route anchors.

Never label future-process models as physical GVS measurements.

## 16. Maintenance rule
After every experiment:
1. keep raw results/report, including failures;
2. update this MAIN_ARCHITECTURE.md;
3. update NEXT_EXPERIMENT.md;
4. update decision/do-not-reinvent records when status changes;
5. distinguish measured PDK/layout, circuit model, system proxy and outside-literature numbers;
6. never leave the active architecture only inside version folders.
