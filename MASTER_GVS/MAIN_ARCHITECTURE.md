# GVS / Neural Glyph — MAIN ARCHITECTURE

**Status:** authoritative integration document. Update this file after every experiment that changes what the system keeps, rejects, or how the pieces connect. Old experiment reports remain evidence; this file states the current combined architecture.

## 0. Primary objective

Build the cheapest practical hardware + software AI system that can become highly capable while reducing unnecessary data movement, memory reads, repeated routing, duplicated support hardware and unnecessary conversions between representations.

The architecture is not required to be purely analog, brain-like, digital, optical or computer-like. Experiments decide which physical representation belongs at which scale.

Core rules:

`stable/reused/local structure -> physical when it wins`

`changing/rare/exact state -> exact computer hardware when it wins`

`ambiguity/failure -> exact fallback`

`weak analog state -> local/short`

`long-distance communication -> robust meaning/results, not fragile raw state`

`live charge -> information; controlled leak -> adaptation; expired charge -> recovery when worthwhile`

## 1. Current whole-system flow

```text
external / sensory / exact input
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
local intelligent Glyph region
  - Tri-Wall / capacitive evidence
  - static templates
  - Grammar motif cells
  - short Passive Myelin
  - local competition / inhibition
  - familiarity / context / fatigue / homeostasis charge
  - direct fourth-face links
  - segmented analog taps
  - Autonomic Event Spine taps
        |
        +---- confident local physical winner ----> robust event
        |
        +---- ambiguous / new / invalid ---------> exact fallback
        |
        v
carrier compiler chooses cheapest valid route
  - dedicated electrical/Myelin chord
  - robust electrical regional/global fabric
  - future Optical Void Chord for long hot relation
        |
        v
next local region / exact computer / result
```

The exact computer is a precision/fallback/consolidation boundary, not the per-event central router.

## 2. Existing physical front end

### Active-Low Coordinate Release
Four-transistor CMOS NOR releases a local selection only when row and column selection agree. It replaced the larger wake-boundary implementation.

### Regional Event Lease
One validated long coordinate selection may remain useful for a local burst. Only validated local winners/successes may refresh the charge state. Raw/noisy activity cannot refresh it. DONE/CLEAN may hard-clear it.

Current selected physical group: **8 isolated local paths per lease**.

Measured 8-way physical result from v13A4:
- 14 NFET + 2 PFET + 1 MIM in the shared interface;
- TT/FF/SS + 12 mismatch launches passed;
- lease/interface write + eleven refreshes ~106.8 fJ TT proxy;
- one selection + lease activity ~0.787 pJ versus ~5.44 pJ for eight separate long selections in the communication proxy.

## 3. Local stable computation primitives

### Capacitive ternary synapses — v12K
Stable synaptic values may be represented by physical MIM coupling when the physical connection is cheaper than repeated memory reads. Exact fallback handles exceptions.

### Shared templates — v12L/v12M
Repeated templates use physical/shared capacitive structure and static selector configuration. Per-event template-ID SRAM reads, one-hot selection and naive binary decoders are not default.

### Grammar Cells — v12N -> v13A5/A6
Grammar detects repeated local motifs. The old fixed 0.500 V threshold is rejected. Current physical Grammar uses same-family MIM ratios and a robust mirrored/dual-pair reader when a robust decision is required.

Current closed physical Grammar readout:
- 10 legal MIM ratio array;
- 10-MOS dual-input-pair self-check reader, replacing the asymmetric 13-MOS analog swap reader;
- fresh motif replay for the two phases when conservative mode is required;
- selected closure timing 6 ns/phase;
- nominal TT/FF/SS exact + partial pass;
- small combined MIM+MOS mismatch closure screen with zero wrong accepts;
- full co-placed readout energy approximately 76–97 fJ in the closure battery.

Use Grammar only when motif recognition removes larger downstream/routing work; do not put Grammar everywhere.

### Direct analog steering
If the next local structure already has a membrane/competition/inhibition node, weak electrical state may steer it directly instead of first paying for a robust reader. This reuses the old v12G principle. The robust Grammar reader remains available when a full-swing boundary is required.

### Myelin
Passive Myelin is a short physical capacitive structural edge for repeated local paths. Full-swing Myelin carries robust meaning across stronger boundaries.

Deep passive analog Myelin chains are rejected because margin decays rapidly over hops. Regenerate locally or promote a direct chord when distance/reuse justifies it.

## 4. Tri-Wall / framework cell

### Tri-Wall Glyph Cell
Three capacitor faces supply local evidence; a fourth connection face exports to a neighboring/receptor path. In SKY130 this is emulated with legal planar MIMs because literal vertical sidewall MIM is not available in the current PDK.

Three ~2x2 um MIM-equivalent walls reproduce approximately the historical three-input Grammar exact/partial voltage separation (~27 mV class first-order screen).

### Fourth-face link
A minimum NFET can connect local evidence/event to a small Contact Receptor.

Two different operating classes are now distinguished:
- ~0.5 V analog evidence required a strongly enabled gate (~1.1–1.2 V class in the tested screen) to preserve ~25 mV separation;
- a ~0.2 V robust regional event is much easier to pass and under v13E the promoted tap is selected at **0.9 V** after full mismatch closure.

The direct fourth face remains the preferred nearest-neighbor weak-analog/event connection because it presents the smallest load.

### Contact Receptor
Use a small landing capacitance rather than connecting one large cell state directly to another large membrane. This preserves analog separation and prevents raw equal-capacitance charge dilution.

## 5. Autonomic Tap Spine / v13E physical closure

A protected shared trunk may have small local subwires/taps into cells. Each tap owns local state; a central router does not decide every event.

Selected v13E physical/electrical result:
- shielded ~180 um spine with four physically isolated branches;
- DRC clean and extracted branch/spine parasitics used in the PDK bench;
- 0.9 V promoted tap gate selected after gate sweep;
- one-active + four-active nominal TT/FF/SS pass;
- **12/12 TT/FF/SS independent mismatch launches pass** at 0.9 V;
- selected outputs remain essentially the full ~0.2 V event;
- inactive taps remain microvolt-class;
- protected analog disturbance ~0.344 mV class in the current extracted coupling proxy.

Event-source energy proxies:
- direct neighboring fourth face ~0.15 fJ/event;
- protected ~180 um event spine one tap ~0.67 fJ/event;
- same spine four taps ~1.34 fJ/event.

Therefore the spine does not replace the direct fourth face. It is the next routing scale.

### Familiarity-driven tap control
Reuse v12E electrical repetition rather than a digital reuse counter in every cell:
- first validated use ~1–2 mV familiarity class;
- second ~17 mV;
- third ~28 mV across preserved screens.

Selected policy:
- one/two uses = probation;
- third closely repeated validated use may create temporary promotion if local margin/cost rules allow;
- continued success writes slower Use/Lease state;
- inactivity naturally demotes.

### Homeostatic loading control
Reuse v12F pooled electrical homeostasis when too many weak-analog taps try to load one segment. Excess participation raises inhibition/selection pressure locally instead of requiring a software scheduler.

### Tap charge recovery
After event capture, expired promoted-gate charge may be connected one-way into a low-voltage recovery reservoir. The v13E screen recovered roughly ~53% of removed tap-gate energy in that specific simple bench while leaving the live event untouched. This is not a universal recovery fraction.

## 6. Shared walls and protected service infrastructure

### Janus / Service Spine Wall
Neighboring cells may share one structural wall instead of duplicating two shells. Weak analog capacitor surfaces remain separate. The protected middle carries robust/slow infrastructure behind shields.

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

Do not leave the shared middle floating.

v13C physical proxy:
- unshielded 100 um service line produced ~1.184 fF coupling to each weak face, enough for ~29 mV simple worst kick on the ~72 fF evidence proxy -> rejected;
- shielded spine removed direct service-to-evidence capacitance terms at extractor resolution in the tested geometry -> kept;
- two service lanes can coexist but couple to one another, so robust/slow lanes, extra shielding or orthogonal routing are preferred.

Service-wall lanes may carry:
- VDD/GND/reference;
- shared PVT/environment pilots;
- slow promotion/demotion/configuration;
- expired-charge recovery;
- robust winner/event traffic;
- Myelin-chord landing/control;
- exact-computer request/result when appropriate.

Do not carry tiny GC/GR/dendrite/latch-internal high-impedance signals in the service spine by default.

## 7. Hollow / volumetric framework

The long-term physical interpretation is now **Heterogeneous Void Fabric**, not simply an empty cavity and not a uniformly filled core.

- semiconductor exists where active devices require it;
- cell walls/ribs form active structural framework;
- inner/outer surfaces may host computation/capacitors;
- shared walls carry protected utilities;
- interior volume is allocated by function;
- do not fill the interior with one continuous conductor because it destroys independent state/selectivity.

This remains a future/custom-process/package direction. Current electrical rules are emulated in ordinary SKY130.

### Functional interior zones

#### A. Active framework / wall zone
Tri-Wall cells, direct links, shields, power, recovery and local service routing.

#### B. Optical Corridor
Intentionally clear line-of-sight volume for promoted long Optical Void Chords. Do not block a committed corridor with later components unless the route is first demoted/rerouted.

#### C. Thermal Artery
Dedicated coolant/heat-removal channel near hot exact-compute, memory, optical-source or power-conversion modules.

#### D. Component Bay
Interior mounting volume for memory, exact compute, recovery storage, sensor interfaces or support hardware when placing it there reduces total cost/communication.

#### E. Structural/alignment rib
Mechanical support and optical alignment reference; may also carry robust shielded services.

#### F. Reserve/bypass corridor
Uncommitted routing volume kept for redundancy, faults and future promotions.

The compiler must assign **volume** as well as representation and route.

## 8. Routing hierarchy

Current routing is multi-scale:

1. **Direct fourth face** — nearest-neighbor private weak analog/event.
2. **Segmented analog tap spine** — short local non-neighbor weak analog relation; unused segments/taps isolated.
3. **Protected electrical event spine + local tap/receptor** — regional shared event/control; local capacitors recreate analog evidence.
4. **Dedicated electrical / Myelin chord** — stable short/medium relation when wire remains cheapest.
5. **Optical Void Chord** — future long hot line-of-sight relation when endpoint/path energy + aperture/cooling cost beats electrical alternatives.
6. **Contactless capacitive/inductive coupling** — only across tiny assembly gaps when eliminating a galvanic bond solves a packaging/yield problem.
7. **RF/mmWave** — rare broadcast/discovery/backup if wired/optical paths are impractical; not normal local routing.
8. **Exact/global fabric** — cold, changing, precise or semantically uncertain relation.

Do not broadcast fragile analog state to many permanently attached electrical receivers.

## 9. Optical Void Chord — v13F/v13G

### Conventional photonic baseline
Published 2025 3D photonic transceivers demonstrate ~50 fJ TX-front-end + ~70 fJ RX-front-end = ~120 fJ/bit; an optimistic source screen raises this to ~150 fJ/bit before some tuning scenarios.

This is far too expensive for local GVS links but can be numerically below the old ~680 fJ long-coordinate/fabric proxy.

### Direct Photocharge Receptor
Future-process candidate:

`light -> photodiode -> local receptor charge -> local physical competition`

rather than:

`light -> receiver amplifier -> full-swing digital -> analog cell`.

Ideal v13F photon/charge model for a 3 fF receptor at 1550 nm and 80% detector QE:
- 20 mV local charge contribution -> ~0.060 fJ incident optical energy;
- 200 mV robust local event -> ~0.600 fJ incident optical energy.

Simple kT/C noise for 3 fF at 300 K is ~1.18 mV RMS, so 20 mV is not immediately ruled out by the simplest thermal-noise screen. Real detector noise/reset/alignment still require physical photonic testing.

### First-order direct-photocharge crossover
Combine the ~0.600 fJ detector-incident event with a published ~5.9 fJ modulator and source/path scenarios:
- good source/path -> ~8.8 fJ/event;
- moderate -> ~19.2 fJ;
- poor -> ~65.9 fJ.

Against current ~3.0–3.7 fJ/mm electrical robust-event wire slopes, first-order crossover is roughly:
- good ~2–3 mm;
- moderate ~5–6 mm;
- poor ~18 mm.

This is a scenario model, not measured GVS optics. It explains why optics belongs at hollow/package distances rather than local cell distances.

### Optical route consolidation
Nonvolatile photonic MEMS and phase-change switches are future-process options for rare route writes with zero static hold power. A 2025 nonvolatile MEMS switch reported ~1 pJ theoretical switch energy and zero-static retention. This is not per-event hardware; it is a candidate route-consolidation mechanism after familiarity and validation.

## 10. Optical Dendrite / long fan-in-fanout

Future-process candidate for sparse long-range physical computation.

### Optical Fanout Tree
One modulated source may split/steer photons to several direct-photocharge receptors. Photon energy scales with receiver count, but the modulator/router may be shared.

Moderate v13G model at 10 mm:
- 1 receiver ~19.2 fJ optical vs ~37.5 fJ one dedicated electrical route;
- 4 receivers ~59.2 fJ vs ~150.1 fJ four electrical routes;
- 8 receivers ~112.6 fJ vs ~300.2 fJ eight electrical routes.

This excludes real splitter/switch/alignment loss.

### Optical Dendrite
Several promoted long-range sources may deposit charge onto one local photodiode/receptor and sum physically.

Ideal 3 fF moderate-path model:
- one 20 mV long contribution ~7.23 fJ source/modulator work;
- four contributions -> ~80 mV nominal local sum, ~28.9 fJ source work;
- four dedicated 10 mm electrical routes -> ~150 fJ first-order;
- four old long-coordinate events -> ~2720 fJ proxy.

This is only valid when pooled evidence is semantically acceptable. A pooled photodiode loses source identity after summation.

### Optical analog safety
Never use one absolute optical voltage/intensity threshold as the signoff rule. If weak optical analog evidence is used, prefer:
- Differential Photocharge Pair (signal vs matched reference);
- two-phase physical self-check for low margin;
- known reference pulse on the same source/path family;
- coarse pulse/ternary weights rather than precision optical attenuation.

Exact fallback remains independent.

## 11. Multi-physics roles inside the framework

### Electricity / charge — KEEP primary
Fast local information, evidence, competition, familiarity, lease, context, fatigue and tap selection.

### Capacitive contactless coupling — MODE_ONLY
Published older links achieved ~41–80 fJ/bit over face-to-face few-micrometer gaps. Useful only when packaging/assembly benefits justify eliminating a galvanic connection.

### Inductive near-field coupling — MODE_ONLY
Published older inter-chip links reached ~65 fJ/bit; useful across tens-of-micrometer tier gaps or isolated modules, not as a replacement for local GVS wiring.

### RF/mmWave — MODE_ONLY
Hundreds-of-fJ-to-pJ class full transceivers make it poor for normal GVS. Possible rare broadcast/clock/discovery/backup role.

### Acoustic/phononic — MODE_ONLY processing, REJECT routing
Useful future filters, frequency processing, sensing or delays. Too slow for normal cavity routing; ~1 mm acoustic flight is ~0.1 us class versus picoseconds for light.

### Heat — KEEP slow environment physics
Temperature/leak controls Thermal Brake thresholds, promotion and decay. Do not encode fast route identity in heat.

### Microfluidics — KEEP thermal infrastructure
Use Thermal Arteries close to hot internal modules. Do not share moving coolant with precision free-space optical corridors by default.

### Mechanical MEMS — FUTURE_PROCESS route configuration
Useful for rare nonvolatile optical switching, not as normal data carrier.

### Magnetism — FUTURE_PROCESS persistent anchor
Verified long-lived configuration only; current SKY130 has no MRAM device module.

## 12. Decentralized physical state / Autonomic State Ladder

Use physical mechanisms at natural time scales:

### Fast electricity
- events/evidence;
- local competition;
- familiarity;
- context;
- temporary tap selection;
- inhibition.

### Medium stored charge
- Regional Lease;
- Use Reservoir / connection hotness;
- fatigue/homeostasis;
- short routing context;
- promotion probation.

### Slow environment physics
v11U/v12A-style replica leak/PVT sensors modify promotion difficulty, retention and inhibition as temperature/process conditions change.

### Rare consolidation
Exact/conservative validation may convert a repeatedly useful relation into static electrical Myelin, a promoted tap, or future nonvolatile optical/magnetic configuration.

### Expired charge
One-way recovery only after information is captured/expired.

## 13. Heat, cooling and optical co-design

Heat is not a fast information carrier, but the hollow architecture makes thermal management a structural advantage.

Rules:
- place hot exact-compute/memory/laser/source modules close to Thermal Arteries;
- keep sensitive analog states away from strong thermal gradients;
- let Thermal Brake reduce promotion/activity in hot regions;
- prefer zero-static optical route storage when it reduces continuous heater/tuning power;
- do not count thermoelectric recovery without a measured temperature gradient and device.

## 14. Internal exact/memory modules

The cavity may host exact hardware only when it reduces total communication/cost.

Good candidates:
- local residual/exception memory;
- exact arithmetic/code engine near frequently escalating regions;
- recovery storage;
- sensor/I/O conversion;
- optical source/switch block near cooling.

Bad default:
- one hot central controller that every local event must visit merely because there is cavity space.

## 15. Fault tolerance / self-healing

The Heterogeneous Void Fabric reserves alternate routing resources.

Selected decentralized policy:

`route success -> familiarity/lease maintained`

`repeated timeout/failure -> route state decays or invalidates`

`alternative path succeeds -> alternative familiarity rises`

`stable replacement -> promote`

Electrical and optical routes remain fallbacks for one another where physically available. Exact fallback verifies correctness during transitions but does not schedule every event.

## 16. Exact computer boundary

Use exact computation for:
- arithmetic/carry/index/pointer/code state;
- rapidly changing/rare knowledge;
- low-margin ambiguity;
- semantic invalidation/correction;
- verifying a relation before durable consolidation;
- cold/new cases where physical structure has not earned promotion.

## 17. Current physical correctness rules

- extraction, not DRC alone, determines electrical correctness;
- weak analog state remains local/short;
- robust meaning may travel farther/vertically/optically;
- do not use fixed absolute Grammar thresholds across real MIM corners;
- raw/noisy activity cannot refresh leases or train persistent taps/routes;
- do not place weak analog state in long series stacks or deep passive chains;
- capture decision before cleanup/recovery;
- inactive shared sources must remain electrically isolated;
- sharing is allowed only when it does not corrupt local decisions;
- physical cost includes communication, readout, fallback, drivers, wire, aperture, route configuration, cooling and support circuitry;
- future optical analog evidence must be self-referenced/differential when absolute drift can consume margin;
- optics is not selected merely because it is faster; it must beat the cheapest valid electrical route including endpoint cost.

## 18. Rejection handling

Every rejected result must be tagged:
- `PRINCIPLE_REJECTED`;
- `IMPLEMENTATION_REJECTED`;
- `MODE_ONLY`;
- `FUTURE_PROCESS`.

This prevents useful principles such as stored-leak adaptation, recovery, analog context, selective Grammar and targeted 3D/optical structure from being lost because one topology failed.

## 19. Current forward experiment — v13G3

Build the first **heterogeneous regional system**, not another isolated carrier:

1. one existing eight-way Regional Lease;
2. multiple real local Grammar/template/Myelin paths;
3. one/few direct fourth-face neighbors;
4. one four-tap v13E electrical event spine;
5. model/placeholder endpoints for two promoted long Optical Void Chords;
6. one Optical Dendrite fan-in case and one optical fanout case in the system model;
7. one internal exact/residual-memory bay;
8. Thermal Artery / thermal-budget model near the hot exact/optical source block;
9. exact fallback independent of every promoted route;
10. workload traces from sound/image/code/reasoning to measure which relations actually earn electrical vs optical promotion.

Measure:
- useful decisions per energy;
- long events removed;
- readers/conversions removed;
- occupied wall/routing/aperture volume;
- thermal load;
- fallback rate;
- route lifetime/payback;
- failure recovery.

Only after this system-level comparison should literal hollow-package fabrication details be promoted further.

## 20. Maintenance rule

**After every experiment:**
1. keep the experiment report/results;
2. update this `MAIN_ARCHITECTURE.md` with every accepted/rejected architectural change;
3. update `NEXT_EXPERIMENT.md`;
4. update Decision Ledger / Do-Not-Reinvent if a principle or implementation changes status;
5. never leave the active architecture distributed only across version folders.
