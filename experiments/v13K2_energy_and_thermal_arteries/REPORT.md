# Neural Glyph v13K2 — Charge-Artery + Thermal-Capillary Scaling

**Verdict: KEEP both as dedicated per-cell service paths, but make them capillaries into shared regional trunks rather than one large pipe/converter per cell.**

## A. Charge Artery
Reuse the v13C shielded-line capacitance proxy ~6.231 fF / 100 um and the v13J thin-package ~0.5 mm average local drop to a nearby exterior/inner-surface landing.

One 0.5 mm recovery capillary:
- capacitance proxy ~31.16 fF.

Four cells feeding one v13P12-style 10 pF regional reservoir:
- four branch capacitances ~124.62 fF;
- branch capacitance is only ~1.25% of the 10 pF reservoir.

Use the preserved v13P12 quoted recovery interval 0.1990 V -> 0.2893 V. The added electrostatic energy stored in all four branch capacitances over that voltage rise is only about **2.75 fJ**.

The v13P12 regional reservoir itself gained about **220 fJ** in the same referenced interval, so the four branch-capacitance energy is only about **1.25% of that recovered-energy scale**.

This does not prove a complete converter. It shows that a short dedicated low-voltage artery is not obviously too expensive relative to the regional recovered packet.

### Reservoir hierarchy simplified
Selected v13K lifecycle:

`live state -> local computation`

`state expires / normal cleanup opens one-way recovery contact`

`short Charge Artery -> shared 4-cell-class regional reservoir`

`regional reservoir -> larger chip/package collector when convenient`

No per-cell DC/DC converter. No per-cell backpressure controller. If chip-level recovery is unavailable, correctness is preserved and the energy may simply be dissipated.

For a 32-cell illustrative region:
- eight 4-cell regional reservoirs -> 8 x 10 pF = 80 pF target;
- one 10 pF reservoir per cell would be 320 pF;
- this retains the older **75% shared-capacitance reduction** principle from v13P12.

## B. Thermal Capillary
Giving every tiny cell its own fluid pump/channel is rejected. Give every cell or small cluster a **passive thermal capillary** into a larger shared thermal artery/vapor/microfluidic structure.

First-order conductive screen only, using a 100 um long copper-like path with k=400 W/m/K:

| square capillary | Rth | rise at 100 uW | rise at 1 mW |
|---|---:|---:|---:|
| 2 x 2 um | 62,500 K/W | 6.25 K | 62.5 K |
| 5 x 5 um | 10,000 K/W | 1.0 K | 10 K |
| 10 x 10 um | 2,500 K/W | 0.25 K | 2.5 K |
| 20 x 20 um | 625 K/W | 0.063 K | 0.625 K |

These are geometry/material calculations, not a fabricated GVS thermal measurement.

### Consequence
- tiny low-power cells can use small passive thermal contacts;
- hotter Component Bays / Exact Service Cores / optical source banks need much larger thermal attachment areas;
- the shared hollow Thermal Artery handles bulk transport to the chip/package heat collector;
- the thermal network has no per-event controller and therefore cannot electrically disturb the analog network.

Recent 3D-IC microfluidic research has reported ~15 K maximum-temperature reduction in a modeled cavity/microchannel/TSV system, supporting the general use of dedicated 3D cooling paths, not this exact GVS geometry.

## C. Three-network cell rule
Every ordinary cell may expose:
1. **Nerve:** fast low-swing firing/event communication;
2. **Charge Artery:** low-voltage expired-charge collection;
3. **Thermal Capillary:** passive heat path.

Only selected cells/regions additionally get:
4. **Light Nerve:** thin optical route for long/hot relationships.

The three basic services are physically different networks. Do not multiplex firing, energy recovery and heat transport merely to save one route.

## Decision
KEEP the biological-style separation because each physics naturally performs a different job and the first-order loading/thermal numbers are compatible with the existing regional architecture.

Next physical requirement: co-layout one weak evidence cell with a low-swing nerve, low-swing recovery artery and shielding/thermal anchor, then extract actual parasitic coupling before treating v13K as physical closure.
