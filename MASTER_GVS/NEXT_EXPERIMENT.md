# Current Next Experiment — v13M3 Two-Octet Physical/System Slice

## Why v13M3 is next
v13M has now answered the system-model questions that were blocking a physical composition.

### v13M0 — mixed intelligent octet
A heterogeneous eight-cell region behind one existing Regional Event Lease retained about **77.8% lower selection + local-core proxy** than eight independent long selections in the tested workloads. Hollow 2x2x2 placement reduced local communication by about 10-15% for some interaction graphs but not all.

**Decision:** intelligence/locality comes from several real primitives cooperating behind one lease. Hollow geometry helps placement, service separation and adjacency; it is not itself the compute mechanism.

### v13M1 — surface routing
Forcing all communication to stay on the 10 x 10 x 2 mm shell is rejected. Across 4,186 boundary-location pairs the mean surface-routing penalty was only ~3%, but directly opposite cells can pay a **5x path-length penalty** (2 mm direct vs 10 mm around the shell).

**Decision:** use surfaces as a placement/service fabric, not a mandatory data manifold. Keep protected direct/interior chords legal when they materially reduce cost.

### v13M2 — two-octet locality
The two-octet model retained about **73-78% selection + local-core savings** from 0% through 100% cross-octet episodes. At 100% crossing, a short 2 mm electrical chord remains much cheaper per crossing than either a 10 mm electrical surface route or a 10 mm optical route amortized over 64 uses.

**Decision:** v13M does not require perfect locality. Crossing another intelligent region should cost another lease/handoff, not repeated long selection of every primitive. Optical promotion must compare against the best real electrical geometry, not an artificially long surface-only route.

## v13M3 goal
Build the first physically grounded **two-octet Hollow Surface Intelligent Region** using the accepted GVS hardware rather than creating new cell logic.

Each octet should contain/represent the existing functional classes:
1. Grammar;
2. static template;
3. short Passive Myelin;
4. local competition/context/regeneration;
5. robust boundary/exact handoff;
6. direct fourth-face/local neighbor relations;
7. one Regional Event Lease shared by the local structures.

Do not invent a new comparator, ADC, microcontroller or recovery scheduler merely to make the composition easier.

## Required neurovascular/service anatomy
Across the two-octet physical/system slice include:
- one low-swing Nerve link between octets;
- one separate low-voltage Charge-Artery branch toward a shared regional recovery node;
- protected weak-evidence placement using the v13L orthogonal-or-shield rule;
- one deliberately opposite-surface **short protected electrical chord** so v13M1 is tested physically rather than only modeled;
- a passive Thermal-Capillary geometry/attachment representation sufficient to estimate area/path feasibility without pretending it is a full thermal-fluid signoff;
- optical conduit/route may be represented, but do not populate/promote an optical runtime path unless real route length and expected reuse pass the preserved break-even.

## Physical baseline rule
Use the repository's accepted historical hardware as architectural truth.

Where the recovered/reconstructed Grammar implementation is used, keep its provenance explicit. Before calling the Grammar instance physically closed inside v13M3, the recovered block must demonstrate the required two-phase robust behavior under the relevant PVT/mismatch battery. If that closure is still incomplete, v13M3 may proceed with geometry/service extraction around it, but the final v13M3 verdict must remain PARTIAL rather than silently inheriting a PASS.

## Workload replay
Replay at least four traffic classes:
- local-only: 0% cross-octet handoff;
- mostly local: 25%;
- mixed: 50%;
- cross-heavy: 100%.

For each class, preserve the same logical work while changing only placement/routing/locality.

## Measurements
### Computation/locality
- long selections per completed episode;
- lease acquisitions and refreshes;
- local primitive operations completed per lease;
- cross-octet handoffs;
- exact fallbacks;
- wrong robust accepts (must remain zero).

### Physical electrical
- DRC and extracted connectivity;
- GC/GR total loading around the physical Grammar instance;
- Nerve->GC and Nerve->GR coupling separately;
- Artery->GC and Artery->GR coupling separately;
- normalized Differential Service Coupling;
- cross-octet chord coupling into weak evidence;
- two-phase physical-side preference;
- Nerve event energy;
- Charge-Artery branch/recovery energy;
- cross-octet chord energy;
- total selection + local-core + communication energy.

### Hollow cost
- active/computation surface used;
- service surface reserved;
- whether total service/support reservation remains below the v13M0 ~46.74% geometric break-even for the chosen shell model;
- area cost of shields/chords/component bays;
- thermal-capillary area/path estimate.

## Acceptance
v13M3 passes only if:
- zero wrong robust accepts in the tested battery;
- ordinary low-swing Nerve/Artery activity does not require a new global quiet scheduler;
- recovery never alters correctness of a live information state;
- direct fourth-face/local routes remain preferred for touching cells;
- the short opposite-surface chord materially beats the forced surface detour without creating unacceptable DSC;
- crossing into another octet uses another lease/handoff rather than reselecting every primitive;
- the hollow service reservation does not erase the useful-surface advantage;
- no optical route is selected when a shorter electrical route wins;
- no new per-cell controller is introduced.

## If v13M3 passes
Promote the following into `MAIN_ARCHITECTURE.md`:
1. Hollow Surface Intelligent Octet as the first concrete local-region composition;
2. surfaces = placement/service fabric, not surface-only routing;
3. protected short interior/opposite-surface chord rule;
4. optical comparison against best actual electrical path;
5. service-reservation break-even as a hollow-cost compiler constraint;
6. canonical `scripts/gvs_sim.py` workflow as the experiment entry point.

Then scale from two octets to a real multi-region trace replay rather than studying isolated primitives again.

## If v13M3 fails
Inspect physical placement/coupling and service-area pressure first. Do not discard the v13K neurovascular anatomy or v13A computation merely because a particular two-octet layout is poor. If the service reservation exceeds the hollow-area break-even, simplify/shared-route the service anatomy before adding more control logic.
