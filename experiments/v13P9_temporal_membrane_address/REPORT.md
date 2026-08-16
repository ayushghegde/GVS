# v13P9 — Temporal Membrane Address Integration

**Status: PARTIAL PASS — physically grounded RC/charge model; transistor sensing still pending**

## What problem this attacks

v13P8 physically proved that an M2/M3/M4 metal membrane can accumulate ROW and COLUMN evidence with sub-fF couplings. The remaining comparison with a two-key MOS receiver is not only transistor count: a direct MOS AND requires ROW and COLUMN pulses to overlap in time, or else extra pulse stretching/latching is required.

The membrane can retain the first coordinate event and add the second later. This reuses the older GVS membrane idea as temporal integration rather than only voltage summation.

## Physical basis

Use the compact v13P8 extracted geometry:

- Cmem = 0.648568 fF
- Crow = 0.372559 fF
- Ccol = 0.380659 fF
- nominal ROW-only membrane contribution = ~0.478 V at 1.8 V
- nominal COLUMN-only contribution = ~0.489 V
- nominal coincident total = ~0.967 V
- DRC = 0

## Leaky-membrane timing screen

For a first-order membrane decay `V(t)=V0*exp(-t/(Rleak*Cmem))` and a nominal sensing point of 0.73 V, the first coordinate can decay before the second arrives and the sum can still fire.

| effective leak | tau | conservative nominal ROW/COLUMN skew |
|---:|---:|---:|
| 25 Mohm | 16.2 ns | ~10.8 ns |
| 50 Mohm | 32.4 ns | ~21.5 ns |
| 100 Mohm | 64.9 ns | ~43.1 ns |
| 200 Mohm | 129.7 ns | ~86.1 ns |
| 500 Mohm | 324.3 ns | ~215 ns |
| 1 Gohm | 648.6 ns | ~431 ns |

This is a nominal timing screen, not a transistor-level guarantee.

## Better implementation: epoch reset instead of a precision gigaohm resistor

A very high-value physical resistor is area-expensive and poorly controlled. The better candidate is a dynamic membrane epoch:

1. one small RESET NFET discharges the M3 membrane at the start of an address epoch;
2. RESET turns off;
3. ROW and COLUMN events may arrive with skew and deposit charge;
4. one local sense/evaluate event is taken near the end of the epoch;
5. membrane is reset again.

This removes the need for a precise leak resistor. The membrane itself stores the first coordinate until evaluation. The address epoch prevents stale charge from combining with a later unrelated query.

## Relation to earlier GVS concepts

This is not a new model representation. It combines older ideas already present in the GVS direction:

- coordinate/grid selection: ROW + COLUMN identify local structure;
- membrane: evidence persists and sums over a short time window;
- synaptic weight: physical capacitance controls how much each coordinate contributes;
- exact fallback/teacher: an ambiguous or uncalibrated cluster can use the conventional MOS/exact selector;
- local lifecycle: reset/evaluate is local to a tile cluster, not a global analog bus.

## Why this can be more valuable than a MOS AND even if area is similar

A two-key MOS stack is likely smaller in raw device area. However it requires simultaneous ROW/COLUMN assertion. The temporal membrane can accept non-overlapping coordinate events in the same address epoch without separate per-line pulse stretchers or latches.

So the possible saving is system-level:

- less clock/pulse-stretch hardware;
- no requirement to keep two long event trunks high simultaneously;
- natural tolerance to row/column arrival skew;
- capacitance performs storage + coincidence computation in the same structure.

## Correctness restriction

The membrane only chooses/wakes a tile island. It does not replace v12S VALID, Grammar/template evidence, Myelin competition, route capture, invalidation or exact fallback.

If sensing PVT/mismatch cannot be made reliable, keep the two-key MOS receiver. The capacitance idea is not mandatory.

## Next

1. Attach a reset NFET and minimal sensing device to the compact 2 um-pad physical membrane.
2. Measure the added membrane capacitance from those devices.
3. Run ROW-only, COLUMN-only, ROW-then-COLUMN and COLUMN-then-ROW transient tests with skew sweep.
4. Repeat TT/FF/SS and mismatch.
5. Compare total layout area and energy to a custom two-key MOS receiver including any pulse-stretch/latch hardware needed for the same skew tolerance.
