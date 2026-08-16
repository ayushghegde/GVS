# v13P6 — Glyph Tile Islands (GTI)

**Status: PARTIAL PASS — physical inter-tile routing evidence only**

## What happened

The previous SES exploration assumed that v12S `run`/`capture` might need to scale as long shared analog buses. Re-reading the exact v12S tile showed that this was the wrong scaling premise: `run` and `capture` are solved **tile-local** dynamic analog control nodes used by the local soma competition and route capture. v12S already passed self-locking capture, cleanup ordering and very heavy parasitic stress on those local nodes.

Therefore GTI keeps the proven v12S tile electrically local and experiments only on **inter-tile communication**.

Candidate scaling rule:

- preserve each tile's lease/run/capture/Myelin behavior unchanged;
- never extend tile-local analog competition nodes globally;
- communicate between tiles with sparse event signals only;
- use horizontal M4 and vertical M5 trunks so long wires cross orthogonally instead of running parallel;
- keep unavoidable long same-layer parallel trunks widely separated.

This is a physical composition experiment, not a replacement for the v12S computation.

## Physical extraction

Magic 8.3.681 was rebuilt locally and loaded with the supplied SKY130A technology.

Minimum-width M4 single-event links were drawn and extracted:

- 100 um: 7.61061 fF, DRC 0
- 250 um: 18.9935 fF, DRC 0
- 500 um: 37.9650 fF, DRC 0
- 1000 um: 75.9080 fF, DRC 0

A 1 mm M4 wire therefore costs about 0.246 pJ for one 0->1 charge at 1.8 V (`C*V^2`). This is below 1% of the historical ~28.28 pJ nominal v12S physical-query VDD window.

## Crosstalk discovery

Two 1 mm parallel M4 event wires were physically extracted. Legal DRC spacing did not imply low coupling:

- 0.4 um gap: 48.4536 fF coupling, DRC 0
- 0.6 um gap: 40.1709 fF coupling, DRC 0
- 1.0 um gap: 29.9363 fF coupling, DRC 0
- 5.0 um gap: 8.43806 fF coupling, DRC 0
- 10 um gap: coupling fell below the extractor's reported coupling threshold in this setup, DRC 0

This is a real inter-tile physical risk: tightly packed long parallel event wires could capacitively disturb one another.

## Orthogonal hierarchy experiment

A 1 mm horizontal minimum-width M4 event trunk crossed a 1 mm vertical minimum-width M5 trunk once.

Extracted result:

- M4 trunk substrate capacitance: 75.908 fF
- M5 trunk substrate capacitance: 87.9215 fF
- M4<->M5 crossing coupling: **0.221205 fF**
- DRC errors: **0**

The orthogonal crossing therefore reduced coupling by roughly 135x relative to the 1 um-gap parallel M4 case.

Charging both 1 mm trunks once at 1.8 V costs about 0.531 pJ total. This remains small compared with one nominal v12S physical query and, importantly, does not place that capacitance directly on the tile-local analog `run`/`capture` nodes.

## Interpretation

The earlier v12S local control problem was already solved. The new problem is **cheap, low-crosstalk composition of many solved tiles**.

GTI is currently a better direction than replacing local run/capture with SES. SES may remain as an exploratory sparse-event concept, but only **between tiles**, not inside the solved tile.

## What is next

1. Physically instantiate a small 2x2 or 4x4 tile-island event fabric.
2. Use M4 horizontal / M5 vertical trunks and local event receivers.
3. Measure cumulative crossing capacitance, same-layer coupling, event delay and energy.
4. Add the smallest possible receiver/summary devices and test TT/FF/SS in ngspice.
5. Keep v12S tile-local analog behavior unchanged.
6. Reject GTI if receiver/device overhead or false-event susceptibility erases the physical advantage.
