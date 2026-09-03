# Neural Glyph v14S — Chip-Level Architecture

**Status:** selected chip-level candidate; physical compound-device closure pending.

## Core primitive

**SP-PGCC — Self-Protected Polarity-Guided Choice Cell:** a zero-MOS semantic cell with one extracted-class tiny shared choice node and six competing passive compound branches; four branches carry learned relations and two are repair spares.

## Branch

**Compound Polar Branch:** two co-located but electrically separated functions.

### 1. Inference path

`CHOICE -> guided dynamic gap -> intrinsic ballast -> next local node`

- ~0.25-V event regime;
- volatile bridge only;
- first branch to bridge collapses the shared CHOICE node and quenches losers;
- no membrane capacitor, Schmitt trigger, selector MOS, SRAM bit, or per-branch compliance MOS.

### 2. Memory/program path

`program row -> passive nonlinear inhibit -> HZO polarity collar -> program column`

- separate terminals from inference path;
- HZO polarization changes the electric field at the adjacent guided gap through a shield aperture;
- selected learning uses a V/3-like regional program scheme;
- half-selected collars remain below the strong-write condition;
- confirmation/contradiction chooses programming polarity;
- recent-use eligibility is the natural volatile residue of the guided gap.

## Polarization Aperture Shield

**Polarization Aperture Shield:** grounded metal surrounding the HZO collar except for a nanoscale opening aimed at the guided gap. It is passive geometry whose job is to keep most of the useful local fringe field while suppressing neighboring-field crosstalk.

Current engineering target: 10-nm HZO patch, ~16-nm aperture, >=20-nm neighboring sensitive-gap spacing. Physical dimensions are device targets, not SKY130 design rules.

## Program Porch

**Program Porch:** one slow shared driver bank per eight semantic cells. It generates/steers the programming levels for 16 local row/column lines. It is outside the inference path and is amortized across all branch collars in the bank.

Current conservative count target: <=40 MOS-equivalent devices per eight cells (<=5/cell). This is a count proxy until layout/PEX.

## Why six branches

Four branches are normal local learned relations. Two are empty reserve mouths. Training can assign a relation to a spare if a branch is defective. This gives fault repair with passive spare geometry rather than duplicating every stored connection or adding repair logic to each cell.

## Selected performance targets from v14S model

- ordinary core MOS: 0;
- amortized shared program-periphery proxy: 5 MOS/cell;
- correct + quenched six-way selection at nominal P=0.16 C/m² with four-neighbor aperture crosstalk: ~99.9937%;
- winner mean delay: ~7.96 ns;
- model event energy: ~1.906 fJ;
- material floor for >99.98% current modeled route selection: around P>=0.14 C/m²;
- choice + six estimated HZO collars: ~0.179 fF;
- 20% winner quench: ~0.092 ns.

## What v14S intentionally does not do

- no high-voltage learning current through the diffusive signal gap;
- no per-branch transistor;
- no standalone eligibility device;
- no dense all-to-all crossbar;
- no one-device-does-everything requirement;
- no claim that HZO or a selector material is already integrated with the GVS diffusive branch.

## Direction check

v14S stays aligned with the original transistor-replacement goal because complexity is moved *out* of the repeated semantic cell. The repeated structure is passive/thin-film/metal geometry; the slow difficult programming circuitry is shared at eight-cell granularity. The architecture is accepted only if physical closure preserves that asymmetry.
