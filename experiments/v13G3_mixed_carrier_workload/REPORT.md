# Neural Glyph v13G3 — Mixed-Carrier Workload Screen

**Verdict: KEEP the carrier compiler and proceed to a physical/system mixed region. This model shows that optical promotion is most valuable for communication-sensitive code/reasoning and repeated sound routes, but it should apply only to long/hot selections that genuinely cross the optical distance threshold.**

## Basis

Reuse v13A workload/core numbers and locality rules:
- image: 16 motif events, 4x-stress local burst >=3 -> 6 long selections;
- sound Grammar: 160 local 3-step motifs, burst 1 -> 160 long selections in the conservative screen;
- code: ~47 active AST motifs, burst >=2 -> 24 long selections;
- reasoning: 12 hops, burst >=4 -> 3 long selections.

Core proxies from v13A:
- image hybrid core ~26.1714 pJ; exact ~47.5556 pJ;
- sound Grammar core ~506.7003 pJ; exact ~1183.2 pJ;
- code hybrid core ~0.04086 pJ; exact ~99.2 pJ;
- reasoning hybrid core ~1.0606 pJ; exact ~10.8 pJ.

Communication comparison in this screen:
- electrical long selection: 0.68 pJ/event base v13A proxy;
- promoted optical event: 0.01923 pJ/event moderate direct-photocharge scenario.

This intentionally assumes the optical relation is long/hot enough to qualify. It does not claim every long selection can be optical.

## Sensitivity to fraction of long selections that earn optical promotion

### 0% optical (all surviving long selections electrical)
- image total ~30.25 pJ -> ~36.4% below exact;
- sound ~615.50 pJ -> ~48.0% below exact;
- code ~16.36 pJ -> ~83.5% below exact;
- reasoning ~3.10 pJ -> ~71.3% below exact.

### 50% of long selections promoted optically
- image total ~28.27 pJ -> ~40.6% below exact;
- sound ~562.64 pJ -> ~52.4% below exact;
- code ~8.43 pJ -> ~91.5% below exact;
- reasoning ~2.11 pJ -> ~80.5% below exact.

### 100% optical sensitivity bound
- image ~26.29 pJ -> ~44.7% below exact;
- sound ~509.78 pJ -> ~56.9% below exact;
- code ~0.50 pJ -> ~99.5% below exact;
- reasoning ~1.12 pJ -> ~89.6% below exact.

The 100% row is not realistic for arbitrary workloads; it is an upper-bound sensitivity showing how strongly communication dominates code/reasoning proxies when the local core is already tiny.

## Interpretation by domain

### Image
Local visual evidence already consumes substantial core energy, so long-link optimization helps but does not dominate. Keep local electrical/capacitive processing; optical only for genuinely repeated cross-region features/results.

### Sound
The Grammar representation remains valuable because it compresses local patterns. If a subset of resulting long motif/sequence relations is stable and distant, optical promotion can further reduce communication without moving local acoustic/Grammar evidence into photonics.

### Code
Code's local motif/dispatch core is extremely cheap; communication dominates the physical proxy. Therefore code benefits strongly from keeping hot algorithm/module dispatch relations physically local or promoting long stable dispatch routes. Exact program state/arithmetic remains digital.

### Reasoning
Reasoning remains the most route-sensitive. Hot multi-hop relations should first become local electrical/Myelin paths. If a stable relation still spans several millimeters/regions, a promoted optical chord becomes a plausible second level. Cold/drifting semantics remain exact.

## Compiler rule refined

For each candidate long relation:

1. verify semantic stability and reuse;
2. determine physical distance and cheapest dedicated electrical route;
3. determine whether existing Regional Lease/Myelin can localize it instead;
4. only if it still remains long, compare direct electrical versus optical endpoint/path energy;
5. include aperture, source sharing, cooling, alignment, route-write and fallback cost;
6. promote only if lifetime traffic repays those costs.

The optical route is never chosen simply because the relation is logically distant.

## Architectural consequence

v13G now has two compilers operating together:

### Representation compiler
Chooses Grammar/template/Myelin/exact representation.

### Carrier/volume compiler
Chooses fourth face, electrical tap/spine, dedicated electrical chord, Optical Void Chord, component bay and thermal/optical corridor resources.

These decisions interact: a good representation can eliminate a long communication before the carrier compiler needs to solve it.

## Decision

The next experiment should stop adding isolated carriers and build one mixed eight-way region with real local structures plus both electrical and modeled optical long routes, then replay image/sound/code/reasoning traces through the same promotion/fallback policy.
