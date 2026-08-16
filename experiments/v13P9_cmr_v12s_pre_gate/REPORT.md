# v13P9 — CMR -> existing v12S pre boundary

**Verdict: PARTIAL PASS / integration direction accepted**

## What happened

The exact v12S netlist was re-read before adding selection logic. v12S already has a `pre` node driving the two soma precharge PFETs. When local `pre=0`, those PFETs hold the somas high and competition cannot fire; when `pre` rises, the proven v12S competition is released.

Instead of adding new clamps to each soma or modifying run/capture/Myelin, the GTI receiver is attached at this existing boundary.

## Circuit

The selected physical receiver from v13P8 provides active-low `WAKEN_B`.

Two extra devices make a local pre gate:

1. PFET pass device from global/query `PRE` to tile `PRE_LOCAL`, gate=`WAKEN_B`.
2. NFET clamp from `PRE_LOCAL` to ground, gate=`WAKEN_B`.

Unselected (`WAKEN_B=1`): PFET pass off, NFET clamp on -> `PRE_LOCAL=0` -> existing v12S somas remain precharged/high.

Selected (`WAKEN_B=0`): PFET pass on, clamp off -> rising `PRE` is passed strongly to `PRE_LOCAL` -> the original v12S soma competition is released.

No run/capture/Myelin/VALID behavior is replaced.

## Timing observation

A PFET pass device passes the rising PRE edge strongly but does not actively pass a falling edge while the tile remains selected. Therefore the cheap two-device interface uses a synchronized selection window: ROW/COL selection ends at the same time as the query PRE-release window ends. CMR then returns `WAKEN_B` high and the NFET clamp resets `PRE_LOCAL` low.

In the conservative wide transistor screen (fast, typical, slow, N/P skew):

- unselected / ROW-only / COL-only / orthogonal-crosstalk -> PRE_LOCAL remains essentially 0 V
- ROW+COL -> PRE_LOCAL reaches 1.8 V during the selected window
- with synchronized end -> PRE_LOCAL is essentially 0 V by 6.5 ns in every tested case

This is a pre-screen, not actual SKY130 PVT signoff; full supplied-model transient remains blocked by the local ngspice parser issue.

## Hardware cost

Per addressed tile-island boundary:

- v13P8 CMR: 4 MOS
- local PRE interface: 2 MOS
- intentional MIM capacitors: 0

Total new selection hardware: **6 MOS** before any later optional buffering.

The receiver uses its unavoidable physical node capacitance as local membrane/storage rather than adding a 2x2 um MIM by default.

## Why this direction is preferred

It preserves the solved v12S local analog circuit and moves selection to an existing robust boundary. It is cheaper than adding duplicate soma clamps, cheaper/smaller than a long-channel leaky restore receiver, and more PVT-robust than a pure two-capacitor threshold detector.

## What is next

1. Use the physically extracted v13P8 ROW/COL input loading to estimate and then physically check a larger GTI cluster (target 16x16 first).
2. Keep the tile-local v12S circuit unchanged behind PRE_LOCAL.
3. Once a compatible ngspice/SKY130 parser is available, rerun CMR + PRE gate under actual TT/FF/SS/mismatch and then insert it into the complete v12S lifecycle.
