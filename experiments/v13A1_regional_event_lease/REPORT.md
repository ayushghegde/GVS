# Neural Glyph v13A1 — Regional Event Lease

**Verdict: PARTIAL PASS — real SKY130 transistor-level PVT/mismatch passed; physical layout/PEX remains**

## What problem this solves

v13A showed that a cheap physical/event representation can lose its advantage if every local motif or reasoning hop repeatedly pays a millimeter-scale inter-island selection cost. The physically extracted 16x16 GTI row+column selection is about 0.68 pJ per long selection.

The missing primitive was a cheap local state that remembers: **this region is already selected; keep several useful local events here before paying the long fabric again.**

This is not a new AI architecture. It wraps the existing Grammar/template/Myelin/v12S mechanisms with a short-lived physical locality state.

## Design lineage

The selected circuit deliberately reuses older Glyph mechanisms:

- v12D: firing charge as short-lived electrical memory
- v12J: gate wrong/inactive evidence at the source
- v12P: physical lease/hotness rather than continuous bookkeeping

A slow trace is **not** continuously read by a CMOS inverter, avoiding static current near inverter threshold.

## Selected circuit

- coordinate-write NFET: W=0.42 um, L=0.15 um, diode-connected
- validated-success refresh NFET: W=0.42 um, L=0.15 um, diode-connected
- weak inactivity leak NFET: W=1 um, L=8 um, gate biased at 0.40 V
- DONE/CLEAN clear NFET: W=0.42 um, L=0.15 um
- local low-voltage event-gate NFET: W=0.42 um, L=0.15 um
- wake/lease storage capacitor: **20 fF**

Only a validated local success refreshes the lease. Raw/noisy local activity does not.
Existing DONE/CLEAN hard-clears the trace.
Exact fallback does not depend on the lease.

## Real SKY130 model route

The run used the supplied SKY130 device-specific 1.8 V NFET BSIM files rather than a compact stand-in:

- `parameters/lod.spice`
- `parameters/invariant.spice`
- `sky130_fd_pr__nfet_01v8__{corner}.corner.spice`
- `sky130_fd_pr__nfet_01v8__mismatch.corner.spice`
- `sky130_fd_pr__nfet_01v8__{corner}.pm3.spice`

with `.option scale=1u` and `mc_mm_switch` for the mismatch launches.

## 12-hop stretch result

One true coordinate writes the regional lease. Twelve local 0.2 V events then execute; the first eleven validated successes refresh the lease. DONE clears it afterward and a later event must remain blocked.

Nominal + 4 mismatch launches per corner = **15/15 PASS**.

Key nominal values:
- TT wake at hop 12: ~1.1253 V
- FF wake at hop 12: ~1.2083 V
- SS wake at hop 12: ~1.0293 V

Weakest mismatch case:
- SS mismatch wake at hop 12: **~0.9833 V**

Every one of the twelve local event outputs remained essentially the full 0.2 V; minimum measured across the screen was ~0.199997 V.

After DONE, the post-burst output stayed blocked. With the minimum clear device, the cleanup kick was limited to roughly -7 to -11 mV across the screen instead of the ~-20 mV class seen with an unnecessarily large clear transistor.

## Disturbance filtering

The lease also acts as a useful physical partial-coordinate filter.

### Safe orthogonal-fabric disturbance: 5 mV
Across TT/FF/SS:
- wake trace peak: ~10-13 uV
- gated event output: only microvolts

### Deliberately bad partial coordinate: 0.74 V
Across TT/FF/SS:
- wake trace peak: ~0.207-0.275 V
- gated 0.2 V event output: only ~1.5-3.1 mV

### True coordinate: 1.8 V
Across TT/FF/SS:
- wake trace peak: ~1.137-1.235 V
- local event passes at ~0.200 V

So the regional lease does not turn the previously measured long-wire partial-crosstalk case into a full local event.

## Energy

Selected 20 fF circuit, actual SKY130 corner models:

Coordinate write:
- TT: ~38.37 fJ
- FF: ~37.70 fJ
- SS: ~40.29 fJ

Eleven validated refreshes for a 12-hop burst:
- TT: ~18.10 fJ
- FF: ~7.00 fJ
- SS: ~46.61 fJ

Total lease write+refresh:
- TT: ~56.46 fJ
- FF: ~44.70 fJ
- SS: ~86.89 fJ

For comparison, twelve repeated long 16x16 coordinate selections at ~0.68 pJ each would be ~8.16 pJ of communication charge. With the regional lease, only one long selection is required plus the tens-of-fJ lease overhead. This is a communication-energy comparison, not whole-system energy.

At TT, one long selection + lease write/refresh is roughly 0.736 pJ versus 8.16 pJ for twelve long selections, about a 91% reduction in that communication-only proxy.

## Why 20 fF was selected

40 fF passed comfortably but cost more storage/write charge.
20 fF also passed the complete 12-hop PVT/mismatch screen after shrinking the clear device to minimum size.
A 10 fF version was not fully signed off and is not selected.

The correct lesson was not "make the capacitor as small as possible". The clear-device charge injection had to be reduced as well.

## What is solved

- one global coordinate can amortize several local operations without a digital counter/scheduler;
- the v13A 4-event locality target is exceeded: the same lease passed a 12-hop stretch case;
- successful local work can refresh locality state;
- inactivity has a real weak-leak path;
- DONE/CLEAN clears the region;
- partial coordinate/crosstalk does not become a full local event;
- TT/FF/SS and 12 mismatch launches passed at transistor level.

## Remaining problem

This is not yet a physical-layout pass.

Still required:
1. draw the 5-NFET + 20 fF lease in Magic;
2. DRC and PEX;
3. measure actual wake-node parasitics and clear-device injection;
4. connect PEX lease to the selected physical coordinate-release cell and local event path;
5. rerun TT/FF/SS/mismatch with extracted parasitics;
6. integrate one leased region into the complete v12S lifecycle and verify that invalidation/exact fallback remain independent.

If physical parasitics consume too much of the 20 fF design margin, increase to 30-40 fF rather than redesigning the architecture.
