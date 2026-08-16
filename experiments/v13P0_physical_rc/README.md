# v13P0 — first measured physical RC experiment

Status: **experiment only; no v12S architecture change**.

## Why this exists

v12S passed schematic-level lifecycle and synthetic parasitic stress. The next required evidence is physical SKY130 layout/extraction. This experiment measures the passive interconnect scale and verifies that two exact v12S primitives can be represented DRC-cleanly and extracted by Magic.

## Tool/provenance

- Magic source: 8.3.681; supplied archive SHA256 `34cd9b5b9ce7d224b5bade44ecedf2271d3b0abdf2e4a064c87abe5e11f24aaf`
- Netgen source: 1.5.323; supplied archive SHA256 `cfa15f0622a6ca9a80319b6f99f4f8f2636648fec3973916744815bc2604d3a3`
- Supplied Spice64/ngspice-47 Windows package SHA256 `a568918b09570e62970dad2192e9d29a8c0539d434ec5256e06d8835006fb260`
- SKY130 common archive SHA256 `6200955c9c81f6add434b2711cc77388138ed3c7c8d3944f6cc2d76a71802618`
- SKY130 primitive archive SHA256 `a6f5e6c8f31334d10c3b31d81bb5aa604e8523ed2384783dc1ccf852155569f9`
- SKY130 Magic tech SHA256 `1e9bc77f8e76f76f7ad6f00501a0495562bd625db84d51b1728cccec84d30d65`
- SKY130 combined SPICE library SHA256 `48de7c677e2c6e7d09b2559279de9f818be71010a4aa933d728eb4db3b133c84`
- recovered v12S archive SHA256 `0ab940fa5cfe1ef850e2b1ea482c142203acd52be140df621f1a60b568a63878`

Magic was built headlessly (`--disable-readline`) because this execution environment does not expose the Tcl development configuration. This does not alter extraction rules.

## Critical scaling correction

When `sky130A.tech` is loaded directly, Magic reports `scale 1000 1 1e+06` in `.ext`; geometry coordinates used here are therefore interpreted at 10 nm per coordinate unit. An earlier exploratory sweep used coordinates 10x too large. Those exploratory numbers are discarded. All numbers below are from the corrected sweep.

## Corrected DRC-clean interconnect extraction

Minimum-width M1 = 0.14 um. M3 test width = 0.30 um.

| Layer | Length (um) | R estimate (ohm) | C to ground (fF) | DRC |
|---|---:|---:|---:|---:|
| M1 | 1 | 1 | 0.096109 | 0 |
| M1 | 2 | 2 | 0.180858 | 0 |
| M1 | 3 | 3 | 0.265607 | 0 |
| M1 | 5 | 4 | 0.435106 | 0 |
| M1 | 10 | 9 | 0.858852 | 0 |
| M1 | 20 | 18 | 1.706340 | 0 |
| M3 | 1 | <1 (rounded in lumped .ext) | 0.110285 | 0 |
| M3 | 2 | <1 (rounded) | 0.195976 | 0 |
| M3 | 3 | <1 (rounded) | 0.281667 | 0 |
| M3 | 5 | 1 | 0.453049 | 0 |
| M3 | 10 | 2 | 0.881504 | 0 |
| M3 | 20 | 3 | 1.738410 | 0 |

Adjacent minimum-spacing wires also show coupling. For 10 um parallel runs: M1 coupling is about 0.564 fF and M3 about 0.529 fF in this geometry.

### Interpretation

The corrected passive-route result is encouraging. Even a 20 um minimum-width M1 run is about 1.71 fF to ground, below the existing v12S +3 fF moderate dendrite stress case. A 10 um run is about 0.86 fF. This does **not** prove the full tile passes PEX, because device diffusion/gate parasitics, contacts, vias, fanout, coupling, and complete routing remain to be extracted.

## Exact v12S primitive layout checks

### MIM Myelin/template capacitor

A true 2.0 x 2.0 um `sky130_fd_pr__cap_mim_m3_1` geometry was created with M3 bottom plate, `mimcap`/`mimcc`, and M4 top plate.

- DRC errors: 0
- extracted device: `sky130_fd_pr__cap_mim_m3_1`
- extracted dimensions: `w=2`, `l=2`
- extracted plate-to-plate parasitic entry: about 0.387 fF
- top plate substrate C: about 0.0167 fF
- bottom plate substrate C: about 0.1215 fF

The device's intended MIM capacitance remains represented by the PDK model; the values above are extraction parasitics around it.

### Myelin NFET switch primitive

A 0.42/0.15 um NFET geometry was created from ndiff + poly.

- DRC errors: 0
- extracted device: `sky130_fd_pr__nfet_01v8`
- extracted `w=0.42`, `l=0.15`
- extracted source area/perimeter: `as=0.1764`, `ps=1.68`
- extracted drain area/perimeter: `ad=0.1806`, `pd=1.70`
- extracted gate-to-substrate parasitic: about 0.0672 fF

This verifies that the exact v12S NFET dimensions are representable and recover correctly through SKY130 extraction.

## Decision

**Do not redesign v12S yet.** The first measured physical evidence does not expose a passive-RC failure. The earlier synthetic +3 fF dendrite stress appears conservative relative to the bare routes measured here.

## Next experiment

Build one complete physical Myelin edge from the unchanged v12S schematic: 2x2 um MIM template capacitor + 0.42/0.15 NFET switch + contacts/vias + DEND/TPL/SW routing. Run DRC, extraction, LVS against the recovered v12S subcircuit, then use the extracted RC/device parasitics in the lifecycle battery. Only an observed failure should trigger a local architecture change.
