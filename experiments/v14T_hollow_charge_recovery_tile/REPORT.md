# Neural Glyph v14T — Hollow Polarity Tile / Adaptive Charge Recovery

**Status: PHYSICAL PROGRAM-METAL PROXY PASS; HOLLOW/RECOVERY SYSTEM MODEL PARTIAL PASS.**

## What happened

v14T tested the two chip-level ideas that should not burden every semantic cell: the hollow-chip structure and electricity harvesting. The polarity idea remains untouched as v14S HZO route memory.

The useful hollow architecture is regional, not per-cell. A small cavity beneath a 200 x 200 um active region provides inner wall area for passive reservoir capacitors and can remain compatible with a future coolant channel. The selected model point is a 60 x 40 x 40 um cavity, only 6% projected void.

A real 16-line SKY130 metal program-grid proxy was then built with two crossing tank rails. Magic reports **0 DRC errors** and produced a real `.ext` parasitic extraction. The compact 20-um program lines have mean conservative switched-node loading of about **2.296 fF**, or **~0.115 fF/um**. Interior lines are similar; end-line fringe/self terms are higher.

That physical result corrected the recovery policy. Mandatory recovery on every tiny rail is rejected. Short local rails are only worth recovering if the control/isolation overhead is low enough; long regional rails clearly contain enough switched energy to justify shared recovery.

## Current selected architecture

**HPT — Hollow Polarity Tile:** top/outer active surface contains the v14S zero-MOS semantic cells; hollow inner walls contain shared passive Charge Return Skin reservoirs; backside carries package power/thermal interfaces.

**CRS — Charge Return Skin:** passive inner-wall capacitor structure used as shared charge tanks for rare HZO programming, not as semantic memory and not as an inference power source.

The modeled 60 x 40 x 40 um cavity has 10,400 um2 inner surface excluding its open top. Using only 50% of that surface with a simple er=9, 20-nm dielectric proxy gives ~20.72 pF total reservoir, ~10.36 pF/tank. This is a geometry model, not fabricated capacitance.

## Physical program-grid result

Proxy:
- 16 metal2 program conductors, ~20 um long;
- two metal3 tank rails crossing the bank;
- Magic/SKY130A technology 1.0.602-0-gf3c505b;
- DRC = 0;
- mean effective conservative line load ~2.296 fF;
- mean normalized loading ~0.115 fF/um.

The effective load calculation counts the node self/substrate term and all explicit couplings as if the other conductors are stationary during a single-line transition. It is therefore a useful conservative switching-energy proxy, not a full activity-factor timing model.

## Charge recovery result

The model uses two selected program-distribution conductors and a conservative three-step recovery envelope bounded around 55% saving at tank/load ratio 1 and 66.7% as the reservoir becomes very large.

At the physical-proxy scaling and 1.2 V:
- 20 um pair: direct distribution energy ~6.61 fJ; gross recovery envelope ~4.41 fJ;
- 100 um pair: ~33.06 fJ direct; ~22.04 fJ gross recoverable;
- 200 um pair: ~66.11 fJ direct; ~44.08 fJ gross recoverable;
- 400 um pair: ~132.23 fJ direct; ~88.15 fJ gross recoverable.

This exposes the correct rule. With ~2 fJ recovery-control overhead, even the compact rail can win modestly. With ~5 fJ overhead, the 20-um rail loses while regional rails still win strongly. Therefore v14T selects **Adaptive Recovery**: use recovery only where the rail's recoverable charge exceeds real control overhead.

## Why the hollow idea survives

The modeled cavity supplies orders of magnitude more tank capacitance than the current program-line load requires while consuming only 6% projected region area. This makes the inner-wall reservoir plausible as shared infrastructure. However, no fabricated cavity, stress/yield analysis, or real capacitor process has been demonstrated.

The optional simple hydraulic screen is also favorable in the model, but it is not CFD and does not justify adding liquid cooling unless later thermal density requires it.

## What was rejected

- per-cell energy harvester;
- harvesting the ~attofarad Choice node;
- mandatory recovery on every local line;
- putting semantic cells on all cavity walls merely to claim 3-D density;
- claiming the earlier 36-MOS/8-cell porch target is physically closed;
- treating the cavity capacitor model as extracted silicon capacitance.

## Current problem

v14T improves energy infrastructure but does not remove the remaining transistor requirement. The inherited v14S Program Porch still uses a conservative ~40-MOS/8-cell structural proxy because the chip needs active jobs somewhere: generate/restore programming voltage, connect selected row/column rails, isolate unselected rails, drive RC load, and interface with external digital control.

The semantic cell itself remains 0 MOS. The remaining question is whether those active jobs can be shared over a much larger region or replaced by passive nonlinear coincidence so the MOS cost collapses rather than being repeated per 8 cells.

## What is next

v14U should directly test a **Sparse Active Spine**: one regional set of active edge drivers serving many zero-MOS cells through passive nonlinear ferroelectric coincidence selection and the v14T hollow reservoir. It must compare 8-cell porch, 64-cell regional spine, and larger sharing factors on MOS count per semantic cell, extracted regional rail capacitance and RC delay, write energy including recovery, selected vs half-selected HZO voltage, sneak/disturb risk, level restoration and drive-current requirement, and whether sharing creates a throughput bottleneck.

If the regional spine still needs dense per-cell active isolation, the passive-addressing idea fails. Do not add hidden branch MOS.
