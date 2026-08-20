# Current Next Experiment — Verticalized Direct Grammar Cell

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

v13A5/v13A6 established the PVT-tracking equal-total Grammar MIM ratio and the **margin-tiered** reader policy:

- high-margin/stable representation -> one-phase direct reader
- low/unknown margin -> two-phase self-check
- ambiguity/failure -> exact computer path

The current normal high-margin 3-step sound Grammar reader target is the 7-MOS direct reader, not the old unconditional 13-MOS two-phase reader.

## New v13A7 result

A real SKY130 physical experiment placed one legal 2x2 um MIM **directly above** a W=0.42/L=0.15 NFET in XY.

- DRC errors: 0
- exactly one NFET + one MIM extracted
- no accidental short
- largest measured MIM-plate-to-transistor parasitic in this test: ~0.059 fF

Therefore the next reader should not be laid out as a flat side-by-side block by default. The MIM evidence layer should be deliberately placed above the local transistor logic where routing allows.

See:
- `experiments/v13A7_3d_vertical_architecture/`
- `MASTER_GVS/3D_ARCHITECTURE.md`

## Next physical experiment

Build the first **vertical Glyph compute cell** by merging v13A6 and v13A7:

1. lay out the 7-MOS direct one-phase Grammar reader in FEOL/M1/M2;
2. place the 10-MIM candidate/reference ratio array directly above as much of the reader as legal using M3/M4;
3. keep GC/GR routes very short and symmetric;
4. keep robust output nodes O0/O1 physically short and away from weak evidence wiring;
5. reserve the highest available metal for robust/global event routing where practical;
6. DRC + extraction; reject DRC-clean layouts with wrong connectivity;
7. measure:
   - total XY footprint
   - GC/GR ground/cross coupling
   - O0/O1 parasitic capacitance
   - unwanted MIM-to-transistor vertical coupling
8. compare against a side-by-side reference placement;
9. run TT/FF/SS + combined MIM/MOS mismatch;
10. measure actual one-phase readout energy;
11. connect the verticalized Grammar cell behind one path of the selected 8-way Regional Lease.

## Acceptance rules

Keep the verticalized cell only if:

- exact/partial Grammar sign remains correct across the characterized physical class;
- there are zero wrong accepted high-margin decisions in the signoff screen;
- weak analog evidence remains local and is not exported vertically/long-distance;
- XY area or evidence-wire parasitics improve materially versus side-by-side placement;
- robust output parasitics stay within the measured reader timing budget;
- exact fallback remains independent.

## True die-stacked 3D after this

Do **not** make hybrid bonding a prerequisite for the first GVS chip.

After the same-die vertical cell passes, screen a regional hybrid-bond partition where a memory/config/event tier sits directly over local Glyph groups. Only robust events and static/slow configuration should cross the die interface.

The v13A7 architecture model suggests substantial communication-energy headroom versus the ~0.68 pJ planar long-selection proxy, but those hybrid-bond numbers are literature-based modeling, not GVS-extracted silicon.

## Separate tooling issue

Complete historical-v12S continuous-model signoff remains a separate simulator/model compatibility task. Do not modify solved v12S behavior around that tooling mismatch.
