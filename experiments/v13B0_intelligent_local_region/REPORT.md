# Neural Glyph v13B0 — Intelligent Local Region / Passive-Chain Depth

**Verdict: PARTIAL PASS — the eight-way Regional Lease remains strongly useful for a heterogeneous local region, but deep passive-Myelin chains without local regeneration are rejected. The next physical region should mix Grammar/template/Myelin work behind one lease and regenerate weak analog evidence locally before it becomes too small.**

## Why v13B starts here

The repository already contains the v13A5/v13A6 Grammar-reader work, including a physical 10-MOS dual-input-pair reader that passed full reader PEX plus local event gates and a physical-ratio Grammar model in 48/48 combined mismatch cases at the selected 3.5 ns/phase timing.

Therefore v13B does **not** redo the old v13A5 reader problem. The next system question is whether several real local structures can share one eight-way Regional Lease without either:

1. paying a long coordinate selection for every small operation; or
2. chaining weak analog evidence so deeply that the evidence becomes unreliable.

The first v13B experiment attacks the second problem directly.

## Terms

- **Passive Myelin** — a MIM-capacitor physical edge that transfers local analog evidence without a runtime memory lookup or full-swing conversion.
- **Regeneration checkpoint** — a local analog reader that converts weakening analog evidence back into a robust event before more processing continues.
- **Symmetric decision margin** — half the exact-vs-partial voltage separation; it is the largest equal safety margin an ideal reference placed between the two classes could provide.

## Circuit experiment

A new eight-hop passive-Myelin chain was generated from the preserved v12R Grammar/Myelin circuit rather than invented from a new architecture.

The source uses the existing v12R exact and partial Grammar evidence pair. Each branch then passes through eight consecutive MIM Myelin edges. Every new stage starts from the same 0.44 V analog baseline used by the historical circuits.

Tested TT configurations:

- 2x2 um MIM edge + 3 fF target node (historical selected edge scale)
- 2x2 um MIM + 2 fF target
- 3x3 um MIM + 2 fF target
- 4x4 um MIM + 2 fF target
- 5x5 um MIM + 2 fF target

Simulation used the supplied SKY130 ngspice model deck and ngspice revision 26. This new multi-hop chain screen is TT only; the old v12R single-edge circuit already showed capacitor-dominated nominal TT/FF/SS agreement, but that old result is not treated as multi-hop PVT signoff.

## Main result — weak analog evidence cannot be chained arbitrarily deeply

### Historical-scale 2x2 MIM / 3 fF target

Exact-vs-partial separation:

- source: 45.82 mV
- hop 1: 26.17 mV
- hop 2: 14.94 mV
- hop 3: 8.54 mV
- hop 4: 4.90 mV

Best possible symmetric margin is therefore only:

- hop 1: 13.08 mV
- hop 2: 7.47 mV
- hop 3: 4.27 mV

This is below the v13A6 one-phase reader's empirically tested >=18 mV high-margin region after only one passive hop.

The old two-phase self-check tolerated the ~11 mV stress region by converting some difficult cases into fallback instead of wrong accepts. On that empirical boundary, the historical 2x2/3 fF edge supports about one passive hop before a local confidence check becomes appropriate.

### Lower 2 fF target node

2x2 MIM / 2 fF improves transfer:

- hop 1 separation: 29.16 mV
- hop 2: 18.44 mV
- hop 3: 11.69 mV

but the corresponding symmetric margins are only 14.58, 9.22 and 5.85 mV. It still does not justify an unbroken high-confidence analog chain.

## Larger Myelin capacitors were tested rather than assumed

Increasing edge capacitance preserves separation longer:

| Myelin edge | area proxy / edge | hop-1 separation | hop-1 best symmetric margin | consecutive hops with >=11 mV symmetric margin |
|---|---:|---:|---:|---:|
| 2x2 + 2 fF target | 4 um^2 | 29.16 mV | 14.58 mV | 1 |
| 3x3 + 2 fF | 9 um^2 | 33.02 mV | 16.51 mV | 2 |
| 4x4 + 2 fF | 16 um^2 | 35.08 mV | 17.54 mV | 3 |
| 5x5 + 2 fF | 25 um^2 | 36.33 mV | 18.17 mV | 4 |

The 5x5 edge is the first tested point that barely crosses the previous ~18 mV high-margin boundary after one hop.

But it consumes **6.25x the MIM area of a 2x2 edge** just to gain a small first-hop confidence improvement. It also loads the source more strongly and does not make a long chain robust; the symmetric margin is already ~15.34 mV at hop 2.

**Decision: reject 5x5 Myelin as the default solution to chain depth.** The architecture should regenerate locally instead of buying confidence mainly with large capacitors.

## Another important physical failure mode

Long passive chains do more than lose class separation. Their absolute node voltages drift far outside the useful local evidence range because each stage participates in capacitive charge redistribution.

For example, in the historical 2x2/3 fF chain, the exact branch falls from ~0.513 V at hop 1 to ~0.394 V by hop 4 and eventually negative by hop 8 in this isolated chain bench.

That is a strong reason not to treat Passive Myelin as an arbitrary analog wire replacement.

**Passive Myelin is a short structural edge, not an unlimited analog transmission line.**

## v13B region consequence

The first intelligent local region should therefore be segmented:

`long coordinate -> Regional Lease -> local Grammar/template/Myelin work -> local regeneration when analog margin is weakening -> continue locally -> robust region result`

The regeneration checkpoint is not a new digital conversion requirement. It reuses the already-developed local analog Grammar/confidence reader or an existing robust event boundary.

## Does frequent local regeneration destroy the locality energy advantage?

No, in the current measured proxy.

For a deliberately conservative screen, v13B used:

- long planar coordinate-selection proxy: **680 fJ**
- measured eight-way lease activity: **106.8 fJ**
- conservative physical v13A6 two-phase reader: **134 fJ** per robust decision (top end of the reported ~105-134 fJ screen)
- 32-way static template event: **0.644 fJ**
- passive Myelin extra source work: **~0.0132 fJ/edge**

### Eight local operations

If all eight operations were Grammar/readout-heavy:

- eight separately selected structures: ~6512 fJ
- one shared Regional Lease + all eight local readers: ~1859 fJ
- reduction in this communication + local-core proxy: **~71.5%**

For a heterogeneous example with:

- 3 Grammar readouts
- 3 static-template events
- 2 passive-Myelin edges
- 2 additional robust checkpoints after those Myelin edges

results are:

- independent long selections: ~6112 fJ
- one shared eight-way region: ~1459 fJ
- reduction: **~76.1%**

For eight selector-like local events, the proxy reduction is ~85.5%.

These are **not whole-chip energy claims**. They show that even conservative local confidence checkpoints do not erase the measured benefit of avoiding repeated millimeter-scale selection.

## What happened / problem / result

### What happened

v13B moved from isolated-block thinking to an actual local-region question. The first new circuit experiment chained real old-Glyph Passive Myelin repeatedly and measured how fast useful analog separation decays.

### Problem found

A pure deep analog chain is unsafe. Weak evidence separation collapses quickly, and absolute analog levels drift because of charge sharing.

### What was tried

The experiment reduced target capacitance and enlarged MIM edges from 2x2 through 5x5 um.

### Result

Larger MIM improves chain depth, but the area cost grows much faster than the confidence benefit. A 5x5 MIM barely earns one high-margin passive hop while using 6.25x the area of the 2x2 edge.

### Conclusion

**Do not build v13B as one long analog chain. Build it as a locally segmented intelligent region.** Keep weak analog work local, use Passive Myelin for short structural edges, and regenerate only when the measured margin requires it.

## Next v13B experiment

Build the first mixed eight-way local region using the already-proven physical eight-way lease PEX:

1. at least two real Grammar structures;
2. at least two static template-selector paths;
3. at least two Passive Myelin structural edges;
4. one robust Myelin/exact-computer boundary;
5. one or more local confidence/regeneration checkpoints only where the chain-depth result says they are needed;
6. only validated local winners may refresh the Regional Lease;
7. inactive structures must stay electrically quiet;
8. measure full local event energy, evidence coupling, lease stability and final robust result;
9. compare against the same operations with separate long selections.

The hollow/inside-out 3D chip idea is not needed to solve this v13B0 problem and is therefore not added here. It remains optional for a later physical packaging/layout experiment only if it produces a measured advantage.
