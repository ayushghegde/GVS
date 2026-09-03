# Neural Glyph v14T — Hollow Polarity Tile

## New terms

**HPT — Hollow Polarity Tile:** a regional chip structure where ordinary v14S polarity cells remain on the active outer/top surface while a small cavity below them provides inner-wall passive electrical storage and optional thermal-fluidic volume.

**CRS — Charge Return Skin:** passive capacitor material on part of the inner cavity walls, split into shared intermediate-voltage reservoirs used only when charge recovery saves more energy than its switching/control cost.

**Adaptive Recovery:** enable charge recycling only for rails whose recoverable energy exceeds the measured/estimated recovery-control overhead; short local rails may bypass it while long regional rails use it.

## Architecture

The semantic cell is unchanged from v14S: zero MOS in the ordinary cell, six passive branch mouths, HZO polarity route memory, guided volatile gap, passive ballast, aperture shield, and two repair spares.

v14T adds a regional structure below/around many cells:

```text
active/top surface: v14S cells + program metal
---------------------------------------------
hollow cavity: passive 0.4-V / 0.8-V reservoir skins
               optional coolant-compatible channel
---------------------------------------------
backside: power / thermal / package interface
```

The cavity is not used to make every cell three-dimensional. That would add process complexity. It is used as shared infrastructure where extra inner surface area is actually valuable.

## Selected geometry target

- region: 200 x 200 um
- cavity: 60 x 40 x 40 um
- projected void fraction: 6%
- inner surface excluding top: 10,400 um2
- modeled usable capacitor surface: 50%
- conservative dielectric proxy: er=9, 20 nm
- modeled total reservoir: ~20.72 pF, ~10.36 pF per tank

## Energy-recovery rule

Do not harvest the tiny Choice-node charge; its energy is negligible compared with a full guided-gap event. Recover only programming-distribution charge already being moved on shared metal rails.

The physical 16-line SKY130 proxy shows compact local program metal around 0.115 fF/um mean effective single-line loading in this geometry. Therefore local recovery is conditional on control overhead. Regional rails are the preferred target because their capacitance is much larger while the same reservoir can be shared.
