# GVS 3D Architecture — Current Direction

## Status

3D is **selected as a direction, not as a requirement for the first prototype**.

The experiment record is `experiments/v13A7_3d_vertical_architecture/`.

## Stage 1 — use the third dimension inside an ordinary die

This is the selected near-term implementation.

- transistors in FEOL
- local M1/M2 reader/control routing
- M3/M4 MIM evidence and charge state directly above local logic when DRC/PEX allows
- highest metals reserved for robust/global event routing

A real SKY130 test placed a legal 2x2 um MIM directly above a W=0.42/L=0.15 NFET in XY:

- DRC = 0
- exactly one NFET + one MIM extracted
- largest measured plate-to-transistor parasitic in the test ~0.059 fF

Therefore vertical MIM-over-logic placement is a real physical option in the current process.

## Stage 2 — hybrid-bonded functional tiers

Use only after the local 2D/verticalized blocks are physically signed off and communication is still a dominant cost.

Preferred partition:

### Glyph/event tier
- Regional Lease
- Grammar/template/Myelin
- local capacitive evidence
- robust local winner generation

### Memory/config tier
- static template assignment bits
- residual/exact metadata
- slow compiler state
- dense memory that benefits from vertical local connection

### Exact compute tier or adjacent chiplet
- ALU
- exact state/arithmetic
- fallback computer
- unusual/new/low-margin work

## Vertical-interface rule

**Cross tiers with robust meaning, not weak analog state.**

Good vertical signals:
- full-swing winner/event
- region/coordinate event
- slow static configuration
- exact-computer request/result

Keep local to one tier:
- dendrite/Grammar evidence voltage
- candidate/reference ratio nodes
- latch internal nodes
- other tiny high-impedance analog state

## Why this fits GVS

GVS is already local/event-driven. A vertical tier can sit directly over the local region it serves, replacing millimeter-class horizontal transport with very short vertical interconnects. The Regional Lease then amortizes even that vertical selection across multiple local operations.

## Cost rule

Do not adopt advanced 3D merely because it exists.

Near-term cheapest path:
1. mature/open process;
2. aggressive same-die vertical MIM/logic overlap;
3. compact local groups;
4. measured wire/energy reduction.

Hybrid bonding becomes attractive when its saved communication/area is larger than:
- bond/process cost
- yield loss
- thermal penalty
- power-delivery complexity
- test/assembly overhead

## Thermal rule

Do not automatically stack the high-power exact-compute block underneath sensitive analog/event hardware. Tier ordering must be chosen with thermal modeling and package cooling.

## Power rule

Backside power delivery is a promising future advanced-node option because it separates power from signal routing and is relevant to 3D stacks, but it is not part of the SKY130 baseline.

## Current next physical use of 3D

Merge v13A6 and v13A7:

- direct one-phase Grammar reader below
- 10-MIM candidate/reference array above it
- shortest possible GC/GR connection
- robust outputs kept below the measured parasitic budget
- DRC/PEX and compare against side-by-side placement

This is the first selected **vertical Glyph compute cell**.