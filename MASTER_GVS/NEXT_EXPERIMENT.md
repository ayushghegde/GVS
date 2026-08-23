# Current Next Experiment — v13J5 Physical Facade/Recovery Quiet-Window Closure

## What v13J has now established

### v13J0 — Facade Utility Shell
- use outside/backside/sidewall surfaces selectively for robust/shared utilities;
- do not duplicate the whole nervous/data network externally;
- facade is valuable for recovery/decoupling, power/reference, test/repair, thermal interface, optional photonics and fault bypass;
- graph model showed no ordinary cell-to-cell shortest-path improvement from duplicating the facade, but better resilience under heavy random link loss.

### v13J1 — Hierarchical Reservoir Collector
- local reservoirs remain part of computation;
- only expired state drains one-way;
- tiny packets should first pool regionally before any chip-level conversion;
- large batching belongs at the chip/facade collector, not one converter per cell.

### v13J2 — Integrated system screen
- facade + tiny recovery credit alone changed the 64-episode dynamic proxy by only ~0.043%;
- its primary value is congestion/isolation/serviceability/fault bypass, not a giant energy credit;
- optional photonics remains conditional and was the larger route-energy lever in the long/hot stress case.

### v13J3 — Facade Quiet Window
Using the conservative existing ~0.124 fF coupling proxy against a ~72 fF weak node:
- one 0.9 V utility step -> ~1.55 mV kick;
- 1.2 V -> ~2.06 mV;
- 1.8 V -> ~3.09 mV.

From a ~25 mV useful differential and 18 mV high-margin target:
- four aligned 0.9 V transitions still leave ~18.81 mV;
- three at 1.2 V;
- two at 1.8 V;
- beyond those simple aligned stress points the high-margin target fails.

Selected rule: freeze/stagger high-swing facade activity during weak analog integration; resume after capture.

v13J3 also reuses v13P12 rather than only the tiny tap-gate recovery proxy:
- 10 pF shared reservoir across four tiles;
- nominal TT/FF/SS pass;
- 12/12 mismatch launches / 48 tile instances pass;
- ~220 fJ energy increase in one four-tile recovery interval;
- 40 pF separate target -> 10 pF shared target.

### v13J4 — Autonomous Recovery Backpressure
The 10 pF regional reservoir is a short-term buffer, not a long-term battery. First-order accumulation from 0.199 V with ~220 fJ packets gives:
- 1 packet ~0.289 V;
- 2 ~0.357 V;
- 4 ~0.464 V;
- 8 ~0.626 V;
- 16 ~0.862 V;
- 18 ~0.912 V.

Therefore drain the regional bank every one/few recovery episodes when a safe window appears, and batch conversion only in a larger downstream facade/chip collector.

Conceptual local control:
`RECOVERY_PRESENT & CAPTURED_OR_DONE & !WEAK_ANALOG_ACTIVE -> allow facade drain`.

No central per-event recovery scheduler is required.

## v13J5 physical goal
Close the facade/recovery interface electrically before adding more package ideas.

### Required circuit/physical slice
1. one real Grammar/evidence node from the closed ratio/readout family;
2. robust `VALID/CAPTURED/DONE` state;
3. one weak local membrane/evidence node exposed to extracted coupling;
4. one shielded facade-equivalent utility/recovery line;
5. one Recovery Valve / Autonomic Recovery Gate;
6. one regional shared-reservoir branch, starting with the v13P12 10 pF-class behavior or a scaled same-die proxy;
7. exact fallback independent.

### Timing battery
8. switch one facade utility at 0.9/1.2/1.8 V while weak analog evidence is live;
9. repeat with 2/3/4 simultaneous aligned utilities until the actual high-margin/fallback boundary is observed;
10. repeat the same switching only after `CAPTURED/DONE` and verify accepted result does not change;
11. inject recovery while analog is active and verify ARG keeps the drain closed;
12. inject after capture and verify reservoir drains.

### Robustness
13. TT/FF/SS nominal;
14. independent mismatch launches;
15. false-capture / stuck-open recovery-path stress;
16. stuck-closed recovery path must degrade energy only, not correctness;
17. facade bypass failure must leave normal local electrical/exact path functional.

### Measurements
- exact/partial or winner margin before facade switching;
- margin after forced utility switching;
- fallback count versus wrong-accept count;
- regional reservoir voltage before/after safe drain;
- live-node disturbance from recovery branch;
- energy removed/recovered;
- extra facade/service parasitic load;
- latency added by the quiet window.

## Acceptance
v13J facade/recovery interface is physically closed only if:
- normal scheduled facade recovery causes no accepted-result corruption across PVT + mismatch;
- forced unsafe simultaneous switching produces fallback before wrong acceptance;
- recovery never loads live information state;
- stuck-closed recovery does not affect correctness;
- shared regional reservoir still performs its original recovery/lease-support role;
- exact fallback remains independent.

After that closure, return to the full eight-region mixed intelligent block and compare the physical electrical base with optional package layers rather than adding more isolated primitives.
