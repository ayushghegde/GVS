# Neural Glyph v14U — Sparse Active Spine

**Status: PARTIAL PASS.** Physical SKY130 regional-grid extraction passed; FIC/HZO, passive rectifier and final active-spine PEX remain device-level work.

## What happened
The repeated 40-MOS/8-cell Program Porch was removed from the architecture. v14U shares active voltage restoration across a region while semantic cells and inference remain 0 MOS. Two physical program-grid proxies were completed previously: 8x8 and 16x16 both had 0 Magic DRC errors. Recorded mean 16x16 loads were ~16.346 fF/row and ~17.771 fF/column, with ~2.93 ps/~0.55 ps lumped RC. Raw 16x16 extraction files were lost during a prior tool-session interruption, so these are preserved summarized measurements, not regenerated evidence.

The old 100 ns write target was rejected. A broad RC/inhibit Monte Carlo shows that long pulses let half-selected HZO charge too far. Short pulses exploit selected/inhibited time-constant separation without a branch MOS selector.

## Selected architecture
- **SAS — Sparse Active Spine:** one regional active block supplies power gain, rail restoration and external control.
- **DPD — Dynamic Precharge Decode:** rails are precharged, then fixed two-terminal mismatch devices return wrong rails toward the hollow 0.4/0.8-V reservoirs. No static pull fight.
- **FIC — Field-Isolated Collar:** 4-nm-class HZO route memory sits behind a dielectric stand-off and aperture; electric field reaches the guided gap but HZO and Ag do not need direct chemical contact.
- **HRM — Hollow Rib Matrix:** dry ribbed cavities provide internal reservoir surface and mechanical support. Liquid cooling is separate from the electrical cavity.

## Problem
Three items remain unclosed: (1) fabricated/calibrated 4-nm FIC switching near the low-voltage short-pulse target; (2) a simple directional two-terminal mismatch device with enough forward/reverse separation; (3) real layout/PEX of the <=52-MOS/256-cell active spine. These are not reasons to add MOS inside the semantic cell.

## What is next
v14V reduces the active-spine job itself. Instead of statically generating every program level, the hollow reservoir becomes a regional pulse-energy store and a much smaller active launcher injects one energy packet; passive timing/polarity structures steer that packet. Passive elements are not claimed to create net power gain.
