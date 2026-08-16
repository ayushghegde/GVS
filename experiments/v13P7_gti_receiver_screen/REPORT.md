# v13P7 — GTI receiver / false-event screen

**Status: PARTIAL PASS — receiver choice narrowed; transistor-level PVT still pending**

## What happened

v13P6 showed that v12S `run`/`capture` should remain tile-local and that sparse inter-tile events are a better scaling target. The next question was whether long event wires can create false tile selections and what receiver is cheapest.

## False-event risk from extracted parallel coupling

Using the physical 1 mm M4 pair extraction and a simple high-impedance charge-sharing upper-bound estimate,

`Vvictim ~= VDD * Ccouple / (Cvictim_to_substrate + Ccouple)` at VDD=1.8 V,

we obtain:

- 0.4 um gap: ~0.977 V victim kick
- 0.6 um gap: ~0.884 V
- 1.0 um gap: ~0.738 V
- 5.0 um gap: ~0.237 V

The supplied SKY130 combined-test baseline reports `sky130_fd_pr__nfet_01v8` threshold around 0.731 V nominal. Therefore a tightly packed 1 mm parallel event pair could, in the worst high-impedance case, raise an inactive line near or above a transistor threshold. This is a real physical false-event risk.

For the orthogonal 1 mm M4/M5 crossing, the same estimate gives only about 4.5-5.2 mV, using the extracted 0.221205 fF crossing coupling. This strongly favors orthogonal long trunks.

## Receiver candidates

### Candidate A — capacitive coincidence receiver

Row and column events each inject charge into a small local wake node. With a suitable capacitance ratio, one event can stay below threshold while two coincident events rise above threshold. This matches GVS's existing coincidence/evidence philosophy.

However, a robust intentional-MIM implementation consumes appreciable capacitor area per tile and still needs PVT/mismatch validation. It is not the default choice yet.

### Candidate B — two-key MOS receiver

Use one small row-controlled NFET in series with one small column-controlled NFET, plus a weak local restore for the wake node. Both row and column must be active to assert local wake.

Advantages:

- ordinary SKY130 MOS only;
- no ADC or global buffer tree;
- preserves v12S tile-local analog behavior;
- low trunk loading because the row/column network sees only transistor gates;
- cheaper area than adding multiple intentional MIM capacitors per tile.

The prior physical gate-attachment experiment measured ~0.7065 fF extra layout capacitance for a representative W=0.84 um NFET gate attachment. Using that value conservatively as an upper-bound proxy, four receiver gates add ~2.826 fF to each trunk of a 4x4 GTI cluster. This is small relative to the extracted 75.908 fF M4 and 87.877 fF M5 1 mm trunk capacitances.

## 4x4 grid context

The extracted 4x4 grid has:

- 0 DRC errors;
- 16 orthogonal crossings;
- 0.221205 fF per crossing;
- 0.88482 fF total crossing coupling accumulated per trunk.

With the conservative receiver gate-load proxy, one active row plus one active column remains roughly 0.55 pJ for a 0->1 charge at 1.8 V, before receiver internal-node energy. This is still small relative to the historical ~28.28 pJ nominal v12S physical-query VDD window.

## Decision

- Keep orthogonal GTI event trunks.
- Do **not** globalize v12S run/capture.
- Reject tightly packed long parallel event wires.
- Prefer the two-key MOS receiver for the next physical/transient prototype.
- Keep capacitive coincidence as an optional later experiment, not as a required architecture feature.

## Problem still open

The two-key MOS receiver has not yet passed SKY130 transient TT/FF/SS/mismatch simulation. Weak-restore sizing, event pulse width, receiver delay and static current during selection must be measured before adoption.

## What is next

Build and simulate the smallest row+column receiver attached to one unchanged v12S tile input. Verify:

1. row only -> no wake;
2. column only -> no wake;
3. row+column -> deterministic wake;
4. neighboring orthogonal event -> no false wake;
5. TT/FF/SS and mismatch;
6. energy/delay;
7. receiver does not disturb local lease/run/capture/Myelin behavior.
