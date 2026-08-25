# Current Next Experiment — v13N4 Trace-Driven Frugality Closure

## Why v13N4 is next
v13N has reduced the cheapness/smartness question to measurable workload quantities instead of adding more hardware rules.

### v13N0 — shared Exact Service Core geometry
For 32 intelligent octets in the preserved 10 x 10 x 2 mm geometry:
- 1 central exact core removes 96.875% of per-octet core copies with ~41.14 fJ average request+return route;
- 4 shared cores remove 87.5% with ~17.765 fJ round-trip route;
- 8 remove 75% with ~13.09 fJ.

**Decision:** the hollow interior should contain a sparse exact/memory backbone, not one computer-like controller per cell/octet.

### v13N1 — local-first/exact-fallback break-even
Using the preserved ~1.324 pJ local intelligent-octet episode and four-core access route, local-first becomes lower energy than exact-every-episode when exact computation exceeds approximately:
- 1.45 pJ at 90% local resolution;
- 1.75 pJ at 75% local resolution;
- 2.63 pJ at 50% local resolution.

**Decision:** local physical intelligence is useful as a cheap filter in front of exact computation, but it is not automatically cheaper if exact work is tiny or local resolution is poor.

### v13N2 — burst sizing
For 32 octets and independent exact requests, <=0.1% immediate-service overflow requires:
- 3 exact slots at 1% ambiguity;
- 6 at 5%;
- 9 at 10%;
- 16 at 25%.

**Decision:** exact capacity should be sized from ambiguity/throughput, not minimized blindly and not duplicated blindly.

### v13N3 — shared-service transport tax
With four shared exact cores, exact request/return transport contributes only:
- ~0.067% of a local-octet episode at 5% ambiguity;
- ~0.134% at 10%;
- ~0.335% at 25%;
- ~0.671% at 50%.

**Decision:** the access wire is already a second-order energy term in the current model. The unresolved costs are exact compute/memory, ambiguity rate/correlation, packaging/yield and thermal capacity.

## v13N4 goal
Measure the **real Ambiguity Budget** and exact-service burst structure from representative multi-region work before choosing physical Exact Service Core count or filling more Component Bay volume.

### Ambiguity Budget
The fraction of intelligent-octet episodes that cannot be robustly resolved locally and therefore request exact fallback.

The experiment must distinguish:
- local robust accept;
- safe local fallback;
- exact request;
- exact completion;
- wrong robust accept (must remain zero);
- cross-octet event;
- memory/exact-state traffic.

## Trace requirement
Use representative workloads that exercise different structure classes rather than one hand-picked motif stream. At minimum preserve separate traces/classes for:
- repetitive/local motif-heavy work;
- template/reuse-heavy work;
- context/reasoning-like mixed work;
- code/control/exact-heavy work;
- novelty/change burst stress.

If a full model trace is not yet available, build an adapter around the nearest preserved v12S/v13 workload generator and clearly label it as a proxy. Do not invent a favorable fallback percentage and call it measured.

## Canonical trace fields
Each completed octet episode should record at least:
- epoch/time index;
- octet/region id;
- workload class;
- local primitive operations;
- lease acquisition/refresh count;
- local robust accept or fallback;
- exact request yes/no;
- exact service completion epoch;
- exact service slot/core id if modeled;
- cross-octet handoff count;
- robust Nerve/chord/spine events;
- memory bytes/words moved where available;
- wrong robust accept count;
- optional local energy components when directly measurable.

## Measurements
### Intelligence/locality
- local-resolution fraction;
- Ambiguity Budget;
- local operations completed per lease;
- cross-octet rate;
- exact-heavy versus structure-heavy workload split;
- wrong accepts and safe fallbacks.

### Exact-backbone demand
- exact requests per epoch distribution;
- mean/p95/p99/p99.9/max concurrency;
- burst correlation / over-dispersion relative to independent demand;
- queue depth and wait if a proposed pool is smaller than the burst;
- exact-core utilization;
- memory/exact-state traffic per completed episode.

### Cost
Feed the measured trace back into v13N0-v13N3 to compute:
- minimum practical Exact Service Core/service-slot count;
- candidate Component Bay locations;
- exact transport tax;
- local-first versus exact-every-episode energy frontier using measured exact energy when available;
- duplicated exact/memory hardware avoided;
- whether shared-memory traffic becomes the new dominant cost.

## Acceptance
v13N4 passes only if:
- wrong robust accepts remain zero in the tested trace/replay;
- local-resolution/fallback classification is reproducible;
- exact overflow is handled by queue/delay/escalation, never by guessing;
- a shared exact pool materially reduces duplicated capacity versus one-per-octet for at least the structure-heavy target workloads;
- measured exact-service transport remains a second-order cost or the architecture is adjusted;
- no new per-cell controller/recovery scheduler is added to hide poor local resolution;
- exact-heavy workloads are allowed to remain exact-heavy rather than being forced through unsuitable local analog structures.

## After v13N4
Choose a concrete physical v13N5 configuration from the measured workload distribution:
- number and size of Exact Service Core Component Bays;
- exact-memory placement;
- which cell surfaces actually need local intelligent octets;
- which interior/exterior locations stay empty;
- shared recovery/thermal capacity;
- promoted electrical chords;
- optional optical routes only if real traffic crosses their break-even.

Then build the physical multi-octet slice. Do not physically lock an arbitrary exact-core count before this trace-driven sizing step.

## If v13N4 shows poor local resolution
Do not automatically add more local hardware. First classify why:
- missing reusable motif/template -> local structure may help;
- insufficient analog margin -> inspect physical implementation;
- genuinely novel/exact computation -> keep it on the Frugal Exact Backbone;
- memory-dominated work -> improve placement/state reuse rather than comparator count.

The target is minimum total cost, not maximum analogization.
