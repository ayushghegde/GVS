# Neural Glyph v13A6 — 10-MOS Dual-Input-Pair Grammar Reader

**Verdict: PARTIAL PASS — the selected reader is now a real 0-DRC, body-tied SKY130 layout with full RC PEX. The full reader PEX + local event gates + physical-ratio Grammar model passes 48/48 combined mismatch cases at a 3.5 ns/phase safe timing. Co-placement with the actual 10-MIM array remains.**

## Analysis target
v13A5 solved the old fixed 0.5 V Grammar threshold with a legal-MIM PVT-tracking candidate/reference ratio, but the sequential analog-swap reader became physically asymmetric. v13A6 removes the analog crossbar and keeps weak evidence fixed locally.

## Selected topology
One regenerative core is reused for two mirrored input pairs:

- 2 cross-coupled NFETs: W=.42 um / L=.30 um
- 2 output-reset NFETs: W=.42 um / L=.15 um
- 2 phase-tail PFETs: W=1 um / L=.30 um
- 4 evidence-input PFETs
- total: **10 MOS**

Phase 0 uses the normal candidate/reference orientation. After reset and a fresh local evidence replay, phase 1 uses the mirrored orientation. A valid answer must reverse physical latch side while preserving the same logical result. Same-side preference or weak resolution is fallback, never an accepted answer.

## Electrical input-pair optimization
The physically useful parameter was input-pair **aspect ratio**, not larger tail current.

The selected electrical geometry is:

**W=2.75 um / L=.55 um**

It has ~1.51 um^2 gate area, preserving useful mismatch averaging while giving much higher W/L than the old W=1/L=1 pair.

Fully integrated electrical comparison:

- W=2.0/L=.5: good energy but rare fallback
- W=2.5/L=.6: lower energy but fallback remained
- **W=2.75/L=.55: 96/96 integrated mismatch cases correct, 0 fallback, 0 wrong — selected**
- W=3/L=.5: also robust but higher energy

## Local reference/event tracking
The reference line is heavier than one motif line, so an identical pass device is not sufficient at nanosecond timing.

Selected local interface:
- motif event gate: W=.42/L=.15 NFET
- shared reference gate: ~W=.945/L=.15 NFET (~2.25x motif width)
- reference and motif come from the same local ~0.2 V event domain
- allow ~1 ns local settle before comparison

This avoids precision analog calibration while keeping reference/motif amplitude reasonably tracking across PVT/mismatch.

## Physical reader layout
The selected reader was manually laid out in Magic/SKY130A from verified transistor primitives.

Verified primitives:
- PMOS input W=2.75/L=.55
- PMOS tail W=1/L=.30
- NFET cross W=.42/L=.30
- NFET reset W=.42/L=.15

All primitive dimensions extract exactly.

### First topology error caught by extraction
The first full reader was 0-DRC but tail control `N0/N1` crossed the `SP0/SP1` drain routes on M2, shorting control and source nodes. That layout was rejected. Moving N0/N1 control routes to M3 fixed the topology without changing devices.

### Physical body infrastructure
The first electrically correct reader still relied on a testbench tie for NFET substrate/body.

A real local p-substrate contact was then added below the NFET row:
- `psc` substrate contact
- local interconnect + mcon + M1
- physical via stack into the existing GND M3 rail

Final extraction now shows all NFET body terminals physically on **GND**. No floating body/testbench body assumption remains.

### Final reader physical checks
- DRC: **0 errors**
- extracted devices: exactly **10 intended MOS**
- PMOS input geometry: exact W=2.75 um / L=.55 um
- GC/GR, SP0/SP1, N0/N1, O0/O1, RST, VDD and GND remain separate
- no unintended net equivalences
- full resistance extraction completed
- ext2spice regenerated with `scale off`, so physical W/L are explicit in the PEX netlist

## What physical PEX changed
The original electrical reader used very small output-node load assumptions. Extraction shows substantially larger real loading.

Approximate extracted boundary capacitance:
- O0: ~6.8 fF after physical substrate tie
- O1: ~7.0 fF
- SP0: ~4.5 fF
- SP1: ~4.0 fF
- GC: ~1.87 fF reader-side parasitic
- GR: ~1.90 fF reader-side parasitic
- direct GC-GR reader coupling: only ~0.017 fF

The earlier reader had assumed ~2 fF output storage. Physical diffusion/junction/routing capacitance is therefore the main reason regeneration slows.

Detailed extresist also shows hundreds-of-ohms local contact/terminal paths. Reducing those resistances helps, but resistance is **not** the main limit: even with reader resistances numerically removed, the 1.5 ns schematic timing remains too short. Real distributed capacitance dominates.

## Physical timing screen
With full reader PEX and ideal +/-25 mV evidence:
- 1.5 ns/phase: correct polarity but not robust
- 2.5 ns: close to threshold at FF
- ~2.7 ns: first nominal ideal-evidence point above 0.9 V

With the full local event gate + MIM-ratio network attached, FF is again the limiting corner:
- 3.0 ns: FF exact phase 0 ~0.886 V, not accepted
- 3.1 ns: ~0.905 V, technically passes but too little margin
- 3.2 ns: ~0.924 V
- **3.5 ns: selected physical signoff point**

The extra few hundred picoseconds are preferable to enlarging devices or adding a new analog stage.

## Full physical-reader PEX + combined mismatch
The 3.5 ns/phase battery includes simultaneously:
- extracted reader R/C
- physical body tie
- event-gate mismatch
- independent MIM mismatch in the ratio model
- reader MOS mismatch
- fresh local evidence replay for phase 2
- ~1 ns local source/reference settle

Two batches, seeds 101..808, TT/FF/SS, exact and partial:

**48/48 correct accepts**

- fallback: **0**
- wrong accepts: **0**

Examples of hard points:
- weakest FF exact winner in the second batch: ~0.953 V
- SS partial exact-fallback-side losers remain below the 0.9 V robust threshold
- evidence sign remains correct in both phases

Physical-reader VDD work over the two-phase decision is roughly:
- FF: ~105-121 fJ in the current screen
- TT: ~114-128 fJ
- SS: ~117-134 fJ

This is about 2x the schematic readout estimate, but still around 0.1 pJ — much smaller than the ~0.68 pJ long coordinate-selection proxy that Grammar/locality is intended to avoid.

## Analysis conclusion
The important result is not that the reader stayed at the original 1.5 ns timing — it did not.

The result is that the **same 10-MOS analog self-check architecture survives real layout/extracted parasitics** after accepting a longer local 3.5 ns evaluation window. No ADC, digital threshold, analog swap crossbar, or larger comparator architecture was required.

The current physical bottleneck is capacitance on robust latch nodes, not loss of the candidate/reference evidence ratio.

## Still not complete
The reader PEX is physical, but the 10-MIM candidate/reference array is still represented using physically measured MIM/series-pair values rather than co-placed in the same extracted layout as this reader.

### Next
1. reconstruct/place the accepted 10-MIM Grammar candidate/reference array;
2. place it directly beside the body-tied 10-MOS reader;
3. route GC/GR physically with matched short paths;
4. DRC + full combined extraction;
5. verify actual array-reader cross-coupling and floating series midpoint behavior;
6. rerun 3.5 ns TT/FF/SS + combined mismatch;
7. measure combined area and full event energy;
8. if it passes, connect the robust Grammar result behind the selected eight-way Regional Event Lease.

Do not shrink the phase window or change input transistor geometry merely to recover schematic energy unless the physical layout proves a material system-level benefit.