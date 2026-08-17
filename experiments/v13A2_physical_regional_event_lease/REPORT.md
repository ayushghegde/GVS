# v13A2 — Physical Regional Event Lease

**Verdict: PARTIAL PASS — full physical cell + RC PEX passed; full tile-chain integration remains**

## What happened

v13A showed that a hybrid Glyph fabric can lose its energy advantage if every low-level motif/hop repeatedly pays the long-distance coordinate-selection cost. v13A1 therefore introduced a short-lived regional event lease: one true coordinate writes a local charge state, validated local work refreshes it, inactivity leaks it, and DONE/CLEAN hard-clears it.

v13A2 physically laid out that lease in the supplied SKY130A technology and reduced the intentional storage after PEX showed that unavoidable physical parasitic capacitance can usefully provide part of the state.

Selected physical cell:

- 1 x minimum 0.42/0.15 um NFET coordinate/write device
- 1 x minimum 0.42/0.15 um validated-success refresh NFET
- 1 x W=1 um / L=8 um weak-leak NFET
- 1 x minimum 0.42/0.15 um DONE/CLEAN clear NFET
- 1 x minimum 0.42/0.15 um local-event gate NFET
- 1 x `sky130_fd_pr__cap_mim_m3_1`, W=2 um, L=2 um

No architecture or transistor dimensions were changed to make layout easier.

## Physical result

Magic 8.3.681 with the supplied SKY130A technology:

- final hierarchical layout DRC errors: **0**
- flattened layout DRC errors: **0**
- extracted active devices: **5 NFET + 1 M3 MIM**
- MIM dimensions: **2 x 2 um**
- no unintended topology change was accepted

The first combined physical attempt produced 134 DRC violations and was rejected. The problem was contact/metal enclosure and overly packed routing, not the lease circuit. The cell was rebuilt as clean transistor sub-blocks with separated metal distribution until DRC reached zero.

## Why 2x2 MIM was selected

The first clean full layout used a 3x3 um MIM. Full extraction showed that the WAKE network already contributes substantial unavoidable capacitance through wiring, contacts, diffusion and device terminals.

The 2x2 um MIM version therefore deliberately uses **physical parasitic capacitance as part of the short-lived lease state** rather than treating every parasitic as waste.

The extracted RC network includes approximately:

- direct top-level WAKE-to-ground parasitic terms of several fF;
- distributed WAKE node capacitance across routed subnodes;
- hundreds-of-ohms contact/local-interconnect branches on some terminals;
- the intrinsic 2x2 um MIM device separately modeled by the PDK.

The full resistance PEX still passes, so those access resistances are not a functional bottleneck for the low-current ~0.2 V local event path.

Compared with the original 3x3 MIM plate, 2x2 reduces intentional MIM plate area by about **56%**.

## Full-RC PVT result

Using the actual extracted resistance/capacitance network and supplied SKY130 models:

| corner | WAKE at hop 12 | minimum local event | maximum local event | post-DONE event |
|---|---:|---:|---:|---:|
| TT | 1.12262 V | 0.2002415 V | 0.2002979 V | -9.90 mV |
| FF | 1.205059 V | 0.2000629 V | 0.2000675 V | -8.19 mV |
| SS | 1.028607 V | 0.2001198 V | 0.2001648 V | -14.57 mV |

All three corners passed the 12-hop stretch target.

## Full-RC mismatch battery

Four launches each at `tt_mm`, `ff_mm`, and `ss_mm`: **12/12 pass**.

Worst observed values:

- minimum hop-12 WAKE: **0.9899827 V** (SS mismatch)
- minimum local-event amplitude: **0.200005 V**
- largest negative post-DONE cleanup excursion: **-18.67872 mV**

Because the cleanup excursion is now close to the existing ~20 mV blocking/noise comfort criterion, the intentional MIM is **not reduced below 2x2 um**. Saving a little more plate area is not worth consuming more cleanup/noise margin.

## Disturbance result

Worst-corner SS full-RC screen:

- safe orthogonal-wire disturbance, 5 mV input -> WAKE peak **13.7 uV**, event output **0.341 mV**
- deliberately bad partial coordinate, 0.74 V -> WAKE peak **0.206 V**, event output **2.02 mV**
- true 1.8 V coordinate -> WAKE peak **1.136 V**, event output **0.20013 V**

So the lease also acts as a physical incomplete-coordinate filter: partial/crosstalk activity does not become a full local event.

## What is solved

The v13A regional-wake problem is now solved through real physical layout and full RC extraction for one lease primitive:

`one global coordinate selection -> local regional lease -> 12 validated local events -> DONE clear`

The unavoidable capacitance of the physical cell is now intentionally part of the computation/state.

## Current problem

The lease has not yet been inserted behind the final selected 4T coordinate-release cell and in front of the complete unchanged v12S lifecycle in one supplied-SKY130 run.

That is now the next experiment. Do not redesign the lease unless that integrated chain produces a measured failure.

## Next

Build and run:

`ROWB/COLB -> 4T active-low coordinate release -> physical v13A2 lease PEX -> local event/pre boundary -> unchanged v12S Grammar/Myelin/soma/route/recovery/error/fallback lifecycle`

Acceptance requires preservation of the existing v12S decision margin, one-hot route, invalidation, second-query block and exact fallback, while a single long coordinate selection can amortize several local operations.