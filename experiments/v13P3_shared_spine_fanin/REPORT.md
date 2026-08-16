# GVS v13P3 — Shared Run/Capture Spine Fan-In

**Status: PARTIAL PASS with a measured physical scaling limit.**

## What happened

The next physical risk after single-edge and neighbor-coupling validation was shared-node fan-in. The v12S schematic uses shared `run` and `capture` nodes, and its historical moderate parasitic profile added +20 fF to each of those nodes.

To isolate the routing contribution before adding transistor terminal capacitance, DRC-clean minimum-width shared spines were extracted on M2/M3/M4/M5 at 25, 50, 100 and 200 um. A second sweep added legal M4 -> M3 -> M2 -> M1 tap stacks with 1 um local M1 branches to M4 spines.

All recorded structures have **0 DRC errors**.

## Wire-only layer sweep

Extracted capacitance at 200 um:

- M2: 15.6046 fF
- M3: 17.1628 fF
- M4: 15.1992 fF
- M5: 17.6867 fF

M4 was selected for the fan-in sweep because it had the lowest extracted capacitance in this geometry while also having much lower sheet resistance than M2. The SKY130 Magic extraction deck lists approximately 125 milliohm/square for M2 and 47 milliohm/square for M3/M4 in the active extraction corner.

A minimum-width 200 um M4 line is therefore roughly 667 squares, or about 31 ohms of distributed metal resistance. Its lumped RC product with 15.2 fF is well below a picosecond, far below the microsecond-scale v12S lifecycle timing; capacitance/fan-in is the more relevant constraint here.

## 200 um M4 fan-in sweep

- 0 taps: 15.1992 fF
- 2 taps: 15.9040 fF
- 4 taps: 16.6088 fF
- 8 taps: 18.0183 fF
- 16 taps: **20.8375 fF**

The 16-tap case crosses the historical +20 fF shared-node stress envelope **before attached transistor terminal capacitance is included**. This is the first v13 physical experiment that exposes a real scaling boundary rather than simply remaining far below the previous stress margin.

## 100 um M4 fan-in sweep

- 0 taps: 7.61061 fF
- 8 taps: 10.4297 fF
- 16 taps: 12.2799 fF
- 24 taps: 14.0189 fF
- 32 taps: **15.4993 fF**

A 100 um local segment with 32 legal tap stacks remains below 20 fF in the routing-only extraction. Device terminal capacitance still has to be added before assigning a production fan-in limit.

## Interpretation

The evidence does **not** support changing the GVS computation or Myelin mechanism. It supports a physical implementation rule:

**Do not implement run/capture as one long flat shared wire. Keep shared-control networks short and local, then connect local segments hierarchically.**

This is consistent with the existing GVS local/hierarchical direction and follows directly from physical extraction:

- single Myelin edges are comfortably inside the old local-dendrite stress envelope;
- four adjacent edges still have tiny accumulated coupling;
- long shared control wiring is the first structure to approach the old stress limit.

## Current problem

The sweep models legal routing/tap structures but not the actual run/capture transistor terminals. The complete physical shared-control block must include representative attached devices, and the v12S transient lifecycle must be rerun with the extracted network.

## What is next

1. Build a representative 100 um M4 local run/capture segment with real attached SKY130 transistor terminals rather than empty M1 tap branches.
2. Extract total node capacitance and resistance at 8/16/24 or similar fan-in.
3. Choose a conservative physical fan-in below the +20 fF historical stress level.
4. Use repeated local segments to form the shared network; only add buffering/repeaters if extracted transient simulation shows a failure.
5. Combine this shared-network extraction with the v13P0 Myelin-edge PEX overlay and rerun the unchanged v12S lifecycle.

No architecture change is justified yet; **physical segmentation is justified**.
