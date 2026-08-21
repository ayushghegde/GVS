# Current Next Experiment — v13B1 Mixed Intelligent Local Region

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

The repository already contains:

- v13A5: PVT-tracking legal-MIM Grammar ratio + conservative self-check readout work;
- v13A6 dual-pair reader: physical 10-MOS reader PEX, 48/48 combined mismatch pass at the selected 3.5 ns/phase point;
- v13A6 margin-tiered policy: high-margin characterized representations may use a cheaper one-phase reader, while low/unknown margin keeps the conservative self-check/fallback path;
- v13A7: same-die MIM-over-transistor vertical placement is physically legal in the tested SKY130 slice;
- v13B0: deep Passive-Myelin analog chains are **not** safe as unlimited local transmission lines.

## New v13B0 result

An eight-hop passive-Myelin chain was simulated from the preserved v12R Grammar/Myelin circuit.

For the historical-scale 2x2 um MIM / 3 fF target edge:

- source exact-vs-partial separation: ~45.82 mV
- hop 1: ~26.17 mV
- hop 2: ~14.94 mV
- hop 3: ~8.54 mV

The best possible symmetric reference margin therefore falls to ~13.08 mV after one hop and ~7.47 mV after two hops.

Larger MIM edges were tested rather than assumed. A 5x5 um edge barely reaches ~18.17 mV best symmetric margin after one hop, but uses 6.25x the MIM area of a 2x2 edge and still loses margin on later hops.

**Decision:** do not solve local chain depth by making every Myelin capacitor large. Passive Myelin remains a short structural edge. Regenerate weak analog evidence locally when margin requires it.

Even with a conservative ~134 fJ physical reader checkpoint, one shared eight-way region still saves roughly 71-85% of the measured communication + local-core proxy versus eight separate long selections, depending on workload mix. This is not a whole-chip claim.

See:
- `experiments/v13B0_intelligent_local_region/REPORT.md`
- `experiments/v13B0_intelligent_local_region/results/`

## Next physical experiment — v13B1

Build the first **heterogeneous intelligent local region** behind the already-extracted eight-way Regional Lease.

Required local contents:

1. at least two real Grammar structures;
2. at least two static template-selector paths;
3. at least two Passive-Myelin structural edges;
4. one robust Myelin/exact-computer boundary;
5. local confidence/regeneration checkpoints only where analog margin needs them;
6. unused paths remain electrically quiet;
7. only validated local winners may refresh the lease.

## Measurements required

- local-event amplitude after the physical eight-way lease PEX;
- Grammar exact/partial margin with neighboring template/Myelin activity present;
- Passive-Myelin margin after one short edge;
- inactive-path leakage/crosstalk;
- lease WAKE voltage through the mixed event sequence;
- robust final event correctness;
- total local energy versus repeating long coordinate selection for each operation;
- area/capacitance cost of shared checkpoints and shared reference structures.

## Acceptance rule

The mixed region is accepted only if:

- no inactive local structure creates a false robust result;
- analog evidence never continues through an uncharacterized deep passive chain;
- final robust events remain correct across the tested PVT/mismatch screen;
- exact fallback remains independent;
- shared locality still provides a material measured advantage after robust-readout cost is included.

## 3D / hollow-chip idea

Do **not** force the hollow/inside-out 3D chip concept into v13B1. Same-die vertical MIM-over-transistor placement may be used where it reduces real area/wiring, because v13A7 physically demonstrated that technique. More exotic hollow-volume/stacked packaging remains parked until a measured local-region bottleneck justifies it.

## Separate tooling issue

Historical full-v12S continuous-model signoff remains separate. Do not alter solved v12S behavior to work around simulator/model compatibility.
