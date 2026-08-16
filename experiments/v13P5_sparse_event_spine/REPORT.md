# v13P5 Sparse Event Spine — MODELED CANDIDATE

## What happened

Physical extraction from v13P showed that local Myelin edges and compact multi-edge clusters have very small parasitics, while long shared run/capture wiring grows much faster. The original v12S stress data also shows that added shared-node capacitance does not immediately break correctness, but increases query energy materially.

The exact v12S netlist was re-read before proposing a change. `run` and `capture` are dynamic analog control/storage nodes, each with intentional 50 fF storage and weak restore paths. Because of that, a conventional always-active CMOS clock/buffer tree would add unnecessary switching and gates.

v13P5 therefore proposes a **Sparse Event Spine (SES)** as a candidate physical organization:

1. retain v12S local run/capture behavior inside small clusters;
2. use the existing physical lease/hot-region selection to wake only the relevant cluster;
3. export only a small summary event upward;
4. keep upper levels short and low fan-in;
5. do not toggle inactive cluster control wiring.

This is intended as physical hierarchy, not a change to the exact computational semantics.

## Problem being attacked

Flat shared run/capture wiring scales linearly in both wire length and attached terminal parasitic. v13P measurements used for this screen are:

- M4 wire capacitance: 7.6106 fF per 100 um;
- one representative real W=0.84 um / L=0.15 um gate attachment including legal branch/via/contact geometry: 0.7065 fF extra physical capacitance.

The historical v12S TT physical-query energy was about 28.28 pJ nominal. Recorded parasitic stress increased it to about 34.19 pJ at +20 fF run/capture, 41.75 pJ at +50 fF, and 50.48 pJ at +100 fF while still preserving logical correctness. Therefore capacitance is an efficiency/scaling problem before it is a correctness problem.

## Scaling screen

Assumptions for this first-order model:

- four Myelin edges per local cluster;
- 25 um M4 local control segment;
- 100 um M4 parent segments;
- one active cluster/path per query, consistent with lease-driven sparse activation;
- parent attachment parasitic initially approximated using the measured representative real-gate attachment;
- only extracted physical interconnect/terminal parasitics are counted here; intentional 50 fF v12S storage, intrinsic MOS capacitance, summary logic delay and summary-device intrinsic capacitance are not claimed to be eliminated.

Results:

| Edges | Flat physical C | SES active-path physical C | Reduction |
|---:|---:|---:|---:|
| 16 | 18.91 fF | 15.17 fF | 19.8% |
| 64 | 75.66 fF | 25.60 fF | 66.2% |
| 256 | 302.63 fF | 36.04 fF | 88.1% |
| 1024 | 1210.53 fF | 46.48 fF | 96.2% |

The scaling trend is the important result: flat physical control loading grows approximately O(N), while a sparse active path grows approximately O(log_4 N) under the stated assumptions.

## Verdict

**MODELED CANDIDATE — worth physical prototyping, not yet accepted.**

The idea is kept because the measured parasitics show a strong scaling advantage and because it reuses GVS's existing lease/locality mechanism. It is not yet promoted into the architecture because the following are still unknown:

- exact summary-device topology;
- summary-device intrinsic + layout capacitance;
- arbitration latency through multiple hierarchy levels;
- whether local `capture` closure and cleanup ordering remain exact across levels;
- energy of the added summary devices;
- PVT and mismatch robustness.

## What is next

Build one physical **4-local-to-1-parent SES cell** using SKY130 devices. The cell should preserve the v12S capture rule: the first valid local winner closes only its local window and sends one full-swing summary event upward. Extract the layout, measure all parasitics, then simulate the cell before attempting deeper hierarchy. If the summary cell costs too much energy/latency, reject SES and keep segmented flat M4 wiring instead.
