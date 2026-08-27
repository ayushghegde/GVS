# GVS v13T — Adaptive Tissue Homeostasis

**Status: architecture/model pass + real SKY130 adaptive-patch geometry pass; transistor/PVT role-switch closure open.**

v13T keeps v13S differentiated ECCs, Role Pressure, Expression Patches, cell-as-wire communication, Local Venule -> Charge Artery -> reservoir recovery, and the proven Grammar/reader baseline. It solves the main failure mode of adaptive tissue: reserve cells must change role without thrashing, without making every cell universal, and without mixing old patch state into new patch state.

## 1. Dual-Time-Scale Role Pressure
**Dual-Time-Scale Role Pressure (DTRP):** two reserve cells respond relatively quickly to persistent shortages while two respond more slowly, so the tissue can follow both short demand changes and long structural changes.

Most cells remain physically specialized. Only the small General Reserve population may change active Expression Patch. Role pressure is integrated locally. Hysteresis, minimum dwell, and role fatigue prevent reserves from chasing every noisy fluctuation.

### v13T0 held-out dynamic result
100 deterministic workload traces, seven changing workload phases, burst noise, and a 10% specialized-cell loss after the midpoint.

Mean accumulated backlog:
- fixed reserves: 205,548
- instant queue chasing: 27,041
- one-timescale homeostasis: 27,804
- **dual-timescale homeostasis: 23,900**

Dual-time-scale pressure reduces backlog ~88.37% versus fixed reserves and ~11.62% versus instant queue chasing while using ~121.5 role changes instead of ~1,009 (~87.96% fewer changes).

## 2. Adaptation-speed boundary
v13T1 sweeps workload phase durations from 4 to 120 epochs.

Instant chasing is best for extremely fast changes but pays very high switching activity. The dual system stays close on fast phases and becomes better on slower phases:
- duration 4: dual backlog 1,716 vs instant 1,398, but 27.6 vs 156.5 switches;
- duration 32: dual 26,228 vs instant 25,134, with 114.8 vs 875.8 switches;
- duration 64: dual 66,059 vs instant 72,621, with 203.8 vs 1,604.4 switches;
- duration 120: dual 184,090 vs instant 203,781, with 369.3 vs 2,888.6 switches.

**Decision:** retain two adaptation timescales. The fast reserve absorbs short local imbalance; the slow reserve captures stable workload changes. Do not make the entire tissue reconfigure at the fast timescale.

## 3. Break-Before-Make Patch Handoff
**Break-Before-Make Patch Handoff (BBMPH):** before a General Reserve cell changes role, the old Expression Patch is isolated from shared cell state; its small local patch-state island is allowed to drain into the Local Venule while the new patch is enabled after the normal one-step handoff.

**Developmental Wave:** at most one reserve cell in a local region begins a role change per local interval.

### v13T2 result
Across 100 dynamic/failure traces:
- unstaggered dual homeostasis: mean backlog 23,899.62; 121.5 role changes; up to 4 simultaneous role changes;
- BBMPH developmental wave: mean backlog **24,055.38**; **99.78** role changes; **1** simultaneous role change.

The backlog penalty is only ~0.65% while role changes fall ~17.88% and correlated role-change/recovery starts are reduced from four at once to one.

With the v13S first-stage venule model tau~2, an isolated old patch retains only ~1.83% of its initial residual after eight local intervals even though the new patch may already be active.

## 4. Physical adaptive patch-gate anatomy
v13T3 uses Magic 8.3.681, SKY130A tech `1.0.602-0-gf3c505b`, and two real recovered `nf_reset` SKY130 NFET geometries as patch-selection devices.

The two patch selectors and both Role Pressure control lines are placed at the cell boundary, far from the weak GC/GR evidence pair.

Result:
- 0 DRC;
- two real NFET instances;
- distinct STATE_A/PATCH_A/ROLE_PRESSURE_A and STATE_B/PATCH_B/ROLE_PRESSURE_B nodes;
- GC-GR remains 0.040625 fF;
- no direct Role Pressure / state / patch -> GC or GR capacitance term is reported at Magic extraction precision.

Local boundary coupling remains small but nonzero and must be counted in later patch implementation:
- state->own patch ~0.03109 fF;
- role-pressure->own patch ~0.002175 fF;
- state->role-pressure ~0.002600 fF.

**Decision:** adaptive patch-selection hardware belongs at the boundary/service skin, not over the weak analog core.

## 5. Relation to recovery
Role adaptation and energy recovery are coordinated by physics, not a recovery controller:
1. old patch stops participating in information;
2. break-before-make isolation disconnects its state;
3. residual patch charge enters the Local Venule;
4. new patch may become active after handoff;
5. Local Venule smooths old-state charge into the Charge Artery;
6. regional reservoir buffers the larger recovery system.

Recovery failure may lose energy, but must not create a wrong computation.

## 6. What v13T rejects
- instant queue chasing as the normal adaptation rule;
- letting every ordinary specialized cell re-role;
- changing several local reserve cells simultaneously when a wave costs almost no throughput;
- waiting for an entire reserve cell to become electrically empty before activating a separate new patch;
- mixing role-control lines into GC/GR merely to save local routing;
- adding a digital role scheduler.

## 7. Evidence boundary
v13T0-v13T2 are deterministic system models, not transistor-level AI benchmarks. v13T3 is real SKY130 Magic geometry/extraction but does not close ON current, OFF leakage, role-pressure storage behavior, PVT or mismatch.

The supplied ngspice 47 archive is the official 64-bit Windows binary package. It was successfully unpacked in this runtime, but this Linux environment has no Windows compatibility layer. The old Linux ngspice 26 source remains incompatible with the current SKY130 combined model deck. No toy MOS model is accepted for signoff.

## 8. Current decision
### KEEP
- fixed differentiation for ordinary cells;
- a small General Reserve population;
- dual-time-scale Role Pressure;
- hysteresis/dwell/fatigue;
- Break-Before-Make Patch Handoff;
- one-at-a-time local Developmental Wave;
- Local Venule -> Charge Artery -> reservoir hierarchy;
- boundary placement of adaptive patch-control hardware.

### CONDITIONAL
- exactly two fast + two slow reserve cells;
- exact hysteresis/dwell constants;
- one role change per interval;
- tau~2 patch-to-venule and tau~8 venule-to-artery model points;
- exact number of patch options in a General Reserve cell.

## 9. Next
Build v13T4: one physically integrated General Reserve + Grammar/state + Relay mini-tissue with a real role-pressure storage element, two patch selectors, break-before-make isolation, Local Venule, Charge Artery and reservoir equivalent. Close with a SKY130-compatible Linux simulator when available.

If adaptive tissue remains stable and cheap after transistor/PVT closure, promote v13S/v13T adaptive differentiation into `MAIN_ARCHITECTURE.md`. If role-control state or patch interfaces become expensive, reduce reserve flexibility rather than making ordinary cells universal.
