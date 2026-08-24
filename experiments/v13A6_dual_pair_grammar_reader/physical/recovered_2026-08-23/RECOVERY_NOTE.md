# v13A6 Reader Physical Recovery Kit

## Status

This package exists because the repository preserved the v13A6 top-level Magic generator but did not preserve its four child `.mag` cells.

The four child cells in this directory are **reconstructed from preserved v13A6 evidence**, not claimed to be byte-for-byte copies of the lost original files.

Preserved evidence used:

- `gen_reader_bodytied.py` pin/instance coordinates and top-level routing;
- selected v13A6 transistor dimensions from the committed report;
- selected 10-MOS topology from the committed report.

## Recovered primitives

| cell | device | selected W/L | preserved top-level pin centers |
|---|---|---|---|
| `nf_cross.mag` | NFET cross-coupled | 0.42 / 0.30 um | S=(25,21), D=(105,21), G=(65,119) |
| `nf_reset.mag` | NFET reset | 0.42 / 0.15 um | S=(25,21), D=(90,21), G=(57,119) |
| `pf_input.mag` | PFET evidence input | 2.75 / 0.55 um | S=(25,137), D=(130,137), G=(77,352) |
| `pf_tail.mag` | PFET phase tail | 1.00 / 0.30 um | S=(25,50), D=(105,50), G=(65,177) |

Magic/SKY130A validation on 2026-08-23:

- each primitive: 0 DRC;
- extraction returns exactly one intended SKY130 MOS per cell with exact W/L;
- preserved top generator + recovered primitives: 0 DRC hierarchical top;
- flattened reader: 0 DRC;
- flattened reader: exactly 10 intended MOS;
- extracted topology matches the selected dual-input-pair reader mapping.

## Reader regeneration

The original committed `../gen_reader_bodytied.py` remains untouched and is the provenance source for placement/top-level routing. A local recovery run regenerated `reader10_top_v3`, flattened it, and extracted the intended ten-device topology.

## 10-MIM array

`grammar10_mim_reconstructed.mag` is a **new reconstruction**, not the missing original co-placed file.

It implements the preserved physical-ratio topology with exactly ten legal 2x2 um MIMs:

Candidate (5 devices):
- three full driven couplers C0/C1/C2 -> GC;
- one GC-to-GND physical series pair with floating midpoint MIDC.

Reference (5 devices):
- two full REF_EVT -> GR couplers;
- one REF_EVT-to-GR physical series pair with floating midpoint MIDR;
- one full GR-to-GND MIM.

Validation:
- 0 DRC;
- exactly 10 extracted `sky130_fd_pr__cap_mim_m3_1` devices;
- each extracts w=2 um, l=2 um.

Do not call this MIM geometry the historical original. Use it only as a recovery starting point and rerun combined PEX/mismatch before promoting it.

## Important limitation

Because the lost primitive geometry itself was not in Git, parasitics of these recovered cells cannot be assumed identical to the historical v13A6 PEX numbers. The recovered cells preserve transistor dimensions, pin coordinates, topology, legal layout, and the original top-level routing interface. Rerun PEX and acceptance tests before using new energy/timing numbers.
