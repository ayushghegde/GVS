# GVS v13N — Frugal Intelligent Hollow Fabric

**Status:** architecture/model pass; real trace + physical system closure open. v13N does not replace the accepted v13A local-compute hardware, v13K neurovascular anatomy, or v13L physical isolation rule. It changes how the full chip spends hardware: common/reused intelligence stays local and cheap; exact computer-grade resources are pooled and used only when needed.

## New architecture name
**Frugal Intelligent Hollow Fabric (FIHF):** a hollow/all-surface GVS organization in which locally intelligent Glyph regions occupy useful surfaces, while shared exact/memory/recovery/thermal resources occupy interior or exterior Component Bays only when their measured system benefit repays their area, energy, thermal and manufacturing cost.

FIHF is not one new transistor primitive. It is the resource-allocation architecture around the already selected Glyph primitives.

## 1. Objective
Drive support overhead toward a second-order cost while retaining computer-grade exact capability.

The target is not literally zero-cost hardware. The engineering translation of “cheap enough to ignore” is:
- eliminate duplicated hardware before optimizing tiny energy terms;
- keep repeated memory/routing/conversion out of the fast local path;
- make shared-service transport a small fraction of useful local work;
- use expensive exact computation only for ambiguity/new/exact state;
- keep exact fallback available so local physical intelligence is never forced to guess;
- leave space empty when filling it would cost more than it saves.

## 2. Flexibility principle
v13N treats almost every placement/routing rule as a **compiler tendency, not a rigid law**.

Hard correctness/physics constraints remain:
- zero wrong robust accepts in a signed-off battery;
- weak analog evidence must stay within measured physical margin or fall back;
- live information state may not be loaded merely to recover energy;
- exact fallback must remain available;
- extracted connectivity/parasitics outrank DRC-only confidence;
- model/future-process results may not be mislabeled as physical SKY130 closure.

Everything else is chosen by measured total cost:
- inside vs outside placement;
- surface vs interior route;
- direct fourth-face vs subwire/spine/chord;
- electrical vs optical;
- number of exact cores;
- amount of reservoir/decoupling capacity;
- shield use;
- whether a surface/volume is populated at all.

v13M1's surface-only experiment is retained as a stress test of a possible bad implementation, **not** as a claim that the user's hollow idea required signals to travel around the shell.

## 3. Local intelligent layer
The first concrete local unit remains the heterogeneous eight-cell intelligent octet behind one Regional Event Lease.

Local roles may include:
- Grammar motif recognition;
- shared/static templates;
- short Passive Myelin relations;
- local competition/inhibition;
- context/familiarity/homeostasis;
- local regeneration/confidence;
- robust boundary/exact handoff.

The role mix is workload/compiler dependent rather than a rigid cell taxonomy.

Local physical intelligence exists to remove repeated long selection, memory access, routing and exact work for stable/reused structure. It is not required to implement every possible computation by itself.

## 4. Cell anatomy retained from v13K
Each ordinary cell/cluster keeps the useful neurovascular organization:
- **Nerve:** low-swing firing/event path;
- **Charge Artery:** low-voltage collection path for charge after its information role is finished;
- **Thermal Capillary:** passive heat path toward shared thermal structures;
- **Light Nerve:** optional optical path only when the real distance/reuse/source/manufacturing break-even wins.

Touching paired cells prefer the direct fourth-face relation because it is already cheaper than paying a shared-spine tap for the same private neighboring event.

No per-cell microcontroller, ADC, calibration loop, pump or recovery scheduler is added by v13N.

## 5. Frugal Exact Backbone
**Frugal Exact Backbone (FEB):** a small pool of shared Exact Service Cores and exact memory/control resources serving many locally intelligent Glyph octets.

Exact Service Cores may provide:
- arbitrary precise arithmetic/logic;
- exact fallback;
- boot/configuration;
- repair/test;
- exact state machines;
- I/O/DMA support;
- access to larger exact memory/compute chiplets when needed.

They are not duplicated into every cell or octet merely to avoid a short access route.

### v13N0 placement result — 32 octets
Using the preserved 10 x 10 x 2 mm geometry and ~3.74 fJ/mm route proxy:
- 1 central exact core removes **96.875%** of per-octet core copies; avg request+return route ~**41.14 fJ**;
- 2 remove **93.75%**; ~**29.45 fJ**;
- 4 remove **87.5%**; ~**17.77 fJ**;
- 8 remove **75%**; ~**13.09 fJ**;
- 16 remove **50%**; ~**3.74 fJ**.

This is copy-count + route energy, not an absolute silicon-area claim because real Exact Service Core area is not yet measured.

## 6. Ambiguity Budget
**Ambiguity Budget:** fraction of local intelligent-region episodes that cannot be robustly resolved locally and therefore request exact fallback.

The Ambiguity Budget becomes a first-class chip-sizing measurement. Low ambiguity means more exact hardware can be shared; high ambiguity means the exact backbone needs more capacity or the local physical intelligence is not helping enough.

### v13N1 local-first energy break-even
Using the preserved ~1.324 pJ intelligent-octet episode and four-core ~17.765 fJ exact-access route, local-first becomes lower energy than exact-every-episode when the exact computation itself costs more than approximately:
- 99% local resolution -> **1.320 pJ**;
- 95% -> **1.376 pJ**;
- 90% -> **1.453 pJ**;
- 75% -> **1.748 pJ**;
- 50% -> **2.630 pJ**;
- 25% -> **5.279 pJ**.

Therefore v13N does not assume local physical intelligence always wins. If exact execution is extremely cheap or local resolution is poor, the compiler may send more work to exact hardware.

## 7. Exact throughput sizing
v13N0 proves geometry/copy-count sharing; it does not justify one exact core for all workloads.

v13N2 sizes a 32-octet exact pool with one normalized exact-service slot/request/epoch and independent fallback demand.

For <=0.1% immediate-service overflow:
- 1% ambiguity -> **3 slots** (90.6% fewer than 32);
- 2% -> **4** (87.5% fewer);
- 5% -> **6** (81.25% fewer);
- 10% -> **9** (71.875% fewer);
- 20% -> **14** (56.25% fewer);
- 25% -> **16** (50% fewer).

Real requests may be correlated; real exact cores may service multiple requests per epoch. Therefore final core count must come from trace + throughput replay, not this binomial model alone.

Overflow queues/delays/escalates. It never authorizes a wrong local accept.

## 8. Transport Support Tax
**Transport Support Tax:** exact-fallback request/result transport energy divided by the preserved local intelligent-octet episode energy.

v13N3 shows that sharing exact hardware does not currently lose its benefit through access-wire energy.

With four shared exact cores:
- 5% ambiguity -> ~**0.067%** transport tax;
- 10% -> ~**0.134%**;
- 25% -> ~**0.335%**;
- 50% -> ~**0.671%**.

Even one central core stays below 1% through 25% ambiguity in the current route proxy.

**Interpretation:** the access wire is already close to the “ignorable” target. The remaining big costs are exact compute/memory, duplicated hardware, memory traffic, packaging/yield and thermal capacity.

## 9. How the hollow space is filled
The hollow volume/surfaces are not required to be full. They are a resource pool.

### Put on computation skins when locality wins
- Tri-Wall / Grammar / template / Myelin structures;
- competition/context/familiarity/homeostasis;
- local lease interfaces;
- direct fourth-face contacts;
- short Nerve/subwire structures.

### Put in interior Component Bays when frequent shared access wins
- Frugal Exact Backbone cores;
- frequently accessed exact memory/controller blocks;
- shared SRAM/cache/equivalent exact state where locality repays it;
- short promoted electrical/Myelin chords;
- regional event-spine junctions;
- selected reservoir/decoupling structures when physical routing/thermal cost wins.

### Put outside/backside/side/top when heat/service/manufacturing wins
- large power regulation;
- large recovery/decoupling banks;
- test/ESD/I/O;
- large/hot/slow support;
- thermal condenser/manifold/heat spreader;
- optional shared optical source/coupling bank;
- package-facing memory/compute chiplets when their access cost remains acceptable.

### Use hollow volume for shared infrastructure
- Thermal Arteries / vapor or future microfluidic paths;
- protected short chords/bridges;
- optional thin optical lanes;
- structural support;
- empty spacing/shielding where separation is cheaper than active hardware.

**Empty space is a valid winning result.** A block is installed only when measured lifetime/system benefit exceeds its area, routing, thermal and manufacturing cost.

## 10. Recovery remains secondary
The Charge Artery is kept because it also physically separates recovery switching from weak evidence and because shared recovery capacitance already showed a 75% target-capacitance reduction versus separate 10 pF banks in the preserved regional model.

But v13N does not treat recovered charge as the main chip-energy win. Reducing duplicated compute/memory/routing is more important.

Recovery stays simple:
`state performs useful job -> state expires normally -> one-way collection may occur`.

If recovery fails, energy is lost; correctness remains intact.

## 11. Thermal architecture
Every cell does not get a pump.

`cell/cluster -> passive Thermal Capillary -> shared Thermal Artery/Exhaust -> exterior collector`.

Exact/memory/optical Component Bays receive larger thermal attachments proportional to real heat. Cooling wins over harvesting. Heat-recovery electricity cannot rescue a bad compute architecture.

## 12. Optical architecture
Optics is not installed merely because hollow space exists.

Before promotion, compare against the **best actual electrical route**, including direct interior chords. Only long/hot/reused relations that still repay source, alignment, idle and manufacturing cost receive Light Nerves.

## 13. What “smartness of a computer” means in v13N
v13N does not claim that the local physical cells alone equal a general-purpose computer or a foundation model.

The architecture preserves computer-grade functional capability by keeping shared exact hardware able to execute precise/novel/arbitrary operations while local physical structures remove the common/reused work that does not need that expense.

Conceptually:
`local physical intelligence = cheap structural accelerator + associative/local decision layer`
`Frugal Exact Backbone = precise general/exact capability`

A full AI-capability claim still requires sufficient model state/memory, software/compiler support and representative workload accuracy tests.

## 14. v13N whole-system picture
```text
 OUTER / INNER / SIDE / UNDERSIDE COMPUTATION SKINS
 -------------------------------------------------
 intelligent octets
 Grammar + templates + short Myelin + context
 direct fourth-face neighbors
 local Nerve / lease interfaces
        |                  |
        +---- robust result/fallback request ----+
                                                   \
                  HOLLOW FUNCTIONAL INTERIOR       \
        +--------------------------------------------+
        | Frugal Exact Backbone / exact memory bays |
        | shared event-spine junctions              |
        | short promoted electrical/Myelin chords   |
        | shared recovery/decoupling where useful   |
        | thermal arteries / structural voids       |
        | optional thin optical lanes               |
        | EMPTY SPACE where nothing repays its cost |
        +--------------------------------------------+
                |                    |
          Charge Arteries       Thermal Capillaries
                |                    |
        shared reservoirs       exterior heat system
                |
       larger collector if useful

 OUTSIDE/BACKSIDE SERVICE PODS
 power / I/O / test / large recovery / hot support / optional optical source
```

Signals are free to use whatever physical path has the lowest measured total cost. They are not required to follow the shell.

## 15. Current v13N decision
### KEEP
- v13A local computational primitives;
- v13K neurovascular cell anatomy;
- v13L geometry/isolation rule near weak evidence;
- heterogeneous intelligent octets;
- shared Frugal Exact Backbone;
- ambiguity-rate-driven exact-core sizing;
- inside/outside Component Bay compiler;
- short direct/interior chords when useful;
- optional optics only after real break-even;
- empty hollow volume when filling it is not worthwhile;
- canonical repository simulator as the shared experiment source of truth.

### REJECT as defaults
- microcontroller/exact core in every cell/octet;
- filling all hollow volume merely because it exists;
- universal optical hardware;
- per-cell recovery controller/pump;
- sending every episode to exact hardware;
- forcing all data around the chip surfaces;
- hardware duplication merely to save femtojoule-scale access routes.

## 16. What remains unresolved
- real Ambiguity Budget on representative AI traces;
- fallback correlation during novelty/global events;
- exact-core/memory real area, power, latency and bandwidth;
- whole-chip manufacturing/yield cost for practical stacked vs full inside-out implementations;
- full multi-octet physical extraction with real Grammar/template/Myelin/service coexistence;
- full AI quality/accuracy versus software baseline;
- thermal closure for populated Component Bays.

## Next — v13N4 Trace-Driven Frugality Closure
Stop adding abstract hardware rules. Replay representative multi-region workloads through the canonical GVS simulator and measure actual local-resolution/fallback behavior, exact-service concurrency, memory movement and route utilization. Use those measured distributions to choose Exact Service Core count, Component Bay placement and memory topology. Then physically compose the selected configuration.
