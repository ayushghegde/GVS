# v13P8 — Coincidence Membrane Receiver (CMR)

**Verdict: PARTIAL PASS / preferred GTI receiver candidate**

## What happened

Before designing another receiver, the v12S source/report and the current physical experiments were re-read. The earlier tile already solved local run/capture, winner locking, cleanup, fallback, Grammar/template evidence and local membrane/soma behavior. The unresolved problem is inter-tile addressing, not the tile-local analog competition.

A pure two-capacitor threshold receiver was screened first. It was rejected as the default because one-event and two-event amplitudes are only 2:1; making that robust against transistor threshold/mismatch requires extra reference/competition circuitry or significant intentional capacitor area.

A long-channel 5-transistor leaky-membrane receiver was also screened. It worked electrically in a conservative model, but weakening the restore PFET with a long channel costs more silicon than the transistor it saves and creates static current while selected, so it was rejected as the default.

The selected candidate is a compact **4-transistor CMOS coincidence cell** (active-low `WAKEN`): two PFETs in parallel and two NFETs in series. ROW and COL are already robust full-swing GTI event lines. The unavoidable output diffusion/interconnect capacitance is treated as the local membrane; no explicit MIM is added unless later noise evidence requires one.

## Exact SKY130 physical result

A proof layout was generated with the supplied SKY130A Magic technology using:

- 2 x `sky130_fd_pr__nfet_01v8`, W=0.42 um, L=0.15 um
- 2 x `sky130_fd_pr__pfet_01v8`, W=0.84 um, L=0.15 um
- M2 power/output routing
- M3 ROW/COL gate trunks to avoid crossing the M2 buses
- well/substrate contacts

Final result:

- DRC errors: **0**
- unintended net equivalences/shorts: **0**
- extracted devices: **2 NFET + 2 PFET**, correct W/L
- ROW and COL remain distinct
- WAKEN, VDD and GND remain distinct

The first physical attempts were intentionally rejected because legal M2 landing pads touched or crossed gate routes and extraction exposed net shorts. The final layout fixes these by shrinking via landings and doglegging power/output paths.

## Free membrane / input loading

Magic extraction (cap values converted from aF to fF) gives approximately:

- WAKEN-to-substrate: **0.555 fF**
- WAKEN-to-VDD coupling: **0.375 fF**
- WAKEN-to-ROW coupling: **0.259 fF**
- WAKEN-to-COL coupling: **0.165 fF**
- WAKEN-to-mid coupling: **0.0866 fF**

So the active-low receiver already has roughly ~1.4 fF of local electrical storage/coupling without an intentional MIM capacitor.

Each input in this unoptimized proof layout loads the local fabric by roughly ~1.1-1.2 fF including substrate and extracted couplings. This is small relative to the previously extracted 1 mm M4/M5 GTI trunk capacitance.

## Conservative transistor pre-screen

Because the locally built ngspice executable currently rejects syntax in the supplied full SKY130 library (parser/build issue), a deliberately wide Level-1 transistor screen was used only as a **pre-screen**, not as historical SKY130 PVT data.

Five deliberately broad cases were tested (fast, typical, slow and two N/P skew cases), using the actual Magic-extracted receiver parasitics.

For all five cases:

- no input -> WAKEN stays ~1.8 V
- ROW only -> WAKEN stays ~1.8 V
- COL only -> WAKEN stays ~1.8 V
- ROW + COL -> WAKEN falls essentially to 0 V
- ROW + ~5 mV orthogonal-wire disturbance -> WAKEN stays ~1.8 V

The deliberately bad old parallel-wire disturbance (~0.74 V on the inactive input) can create a false select in one skewed case. This confirms that the receiver and the orthogonal GTI wiring are a coupled solution: the receiver does not justify returning to tightly packed long parallel event wires.

Estimated receiver switching energy in this pre-screen is only a few fJ for the actual coincidence cell itself; long-wire charging remains the larger addressing cost.

## Capacitor decision

An explicit 10 fF membrane was tested in the conservative screen. It can reject short simultaneous full-swing glitches, but increases valid-event energy and consumes MIM area. Since the actual orthogonal GTI wiring reduces induced disturbance to only a few millivolts, the explicit capacitor is **not accepted by default**.

If later extracted/system tests reveal real full-swing glitch hazards, the 2x2 um ~10 fF MIM already proven in v12S remains an available optional membrane filter.

## Current problem

The inter-tile coincidence/address problem is now solved at topology + exact physical-layout/extraction level. What is still missing is a full transient run using the supplied SKY130 transistor model library because the locally compiled ngspice parser is incompatible with part of that library syntax.

That is a tool-validation blocker, not evidence that the CMR circuit failed.

## What is next

1. Use the measured ~1.1-1.2 fF per ROW/COL input load to re-extract/screen a larger GTI grid (16x16 or hierarchical 4x4 clusters).
2. Connect active-low `WAKEN` into the existing v12S tile boundary without changing tile-local run/capture/Myelin semantics.
3. Run the complete chain: GTI row/column -> CMR -> unchanged v12S local lifecycle.
4. Repair/rebuild ngspice with a parser compatible with the supplied SKY130 library and rerun the receiver under actual TT/FF/SS/mismatch models.

No v12S tile-local behavior is replaced by this experiment.