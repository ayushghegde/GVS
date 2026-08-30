# Neural Glyph v14G — Goal-Echo Associative Reasoning Fabric

**Status:** transistor-free semantic-core candidate at model level. The v14E CMOS tissue remains the physically closed reference, but MOS transistors are not allowed inside the v14G semantic/reasoning fabric.

## What changed

v14G takes the user's intended mechanism literally at the architectural level: a question first excites the physical pattern representing **what must be found**, contextual and factual cells co-fire, and learned physical connections determine which cell becomes active next. A value or concept found at one step can therefore activate another learned relation and continue the reasoning chain without a program counter choosing the next address.

The important correction from v14EG is economic. v14G does not replace every transistor with a potentially more expensive exotic device. Most semantic cells are passive. Active restoration is sparse and is accepted only if a two-terminal device can beat the transistor baseline in density, energy and process cost.

## New primitive — Associative Relay Cell (ARC)

**Associative Relay Cell (ARC):** a transistor-free passive semantic site whose temporary activation propagates through physically weighted learned connections; semantic memory remains in the connection state rather than the transient firing energy.

An ARC may contain a small state capacitance/resonant state and several sparse learned links. It does not require one active threshold device per cell.

## New mechanism — Goal Echo

**Goal Echo:** the physical pattern for the requested answer type sends reciprocal compatibility bias backward through learned connections while prompt evidence propagates forward.

The intended computation is:

`prompt/context -> learned firing history -> forward evidence`

plus

`what must be found -> reciprocal goal echo`

and the next cell is the one where compatible forward and backward evidence reinforce each other most strongly.

This makes the goal part of the physical computation rather than a software instruction.

## Context

Context is not attached to a word by a parser. During training, cells that repeatedly co-fire develop strong links. Thus BANK may co-fire with RIVER/WATER/SHORE in one learned neighborhood and MONEY/LOAN/ACCOUNT in another. When the same contextual cells fire again, the corresponding sense path receives more physical evidence.

## Training memory

v14G currently assumes sparse two-terminal programmable links for learned connection strength. Only links that actually co-fired are retained; no dense all-to-all crossbar is required.

This is a future-process candidate, not a claim that current GVS SKY130 already contains the required programmable link. Recent passive memristive crossbar work supports the plausibility of transistor-free two-terminal weight layers, but yield, tuning, write energy, endurance and material compatibility remain acceptance conditions.

## Sparse restoration

A purely passive chain attenuates. v14G therefore rejects both extremes:

- one exotic firing device per semantic cell; and
- no active restoration anywhere.

The current candidate uses mostly passive ARCs plus sparse **Two-Terminal Restoration Junctions (TRJs)**.

**TRJ:** a volatile two-terminal threshold device at selected junctions that converts shared bias energy into a fresh wave only after sufficiently strong local evidence arrives.

TRJs are not yet selected devices. Ovonic/metal-oxide threshold switches are research candidates only. v14G requires the chosen TRJ to be simpler and cheaper at system level than the transistors it removes.

## Model evidence

Deterministic v14G screens currently show:

- contextual BANK disambiguation: 97.3% at 20% learned-link variation and 82.9% at 40%;
- learned goal recognition: 99.4% at 20% link variation and 95.2% at 40%;
- similar-episode recall: 98.43% at 20% variation and 89.4% at 40%;
- toy code diagnosis/retrieval: 96.73% at 20% variation;
- an ambiguous 8-hop learned path falls to 3.94% at 20% link variation with forward-only strongest-link propagation, but Goal Echo raises it to 87.24%;
- 12-hop / 20% variation: 0.78% forward-only versus 74.98% with Goal Echo;
- passive 64-hop propagation with one sparse restorer every eight cells succeeds 100% at 6% nominal per-hop loss and about 98.85% at 8% loss in the current event-level screen;
- a 4096-cell, degree-6 sparse fabric with restoration every eight cells uses 512 active restoration junctions rather than 4096 one-per-cell devices.

## Important failure — pure association is not general arithmetic

The arithmetic chain test is exact when every required operation/value transition has been physically learned. When 216 specific arithmetic transitions were deliberately removed, pure associative routing recovered **0%** of them.

Therefore v14G does not claim that associative recall alone performs arbitrary mathematics or novel code execution. A scalable structural operator is still required for relationships that cannot be stored economically as individual learned edges.

This is now the central intelligence/hardware problem, not a reason to reintroduce a transistor computer.

## Structural cost screen

For a sparse undirected degree-6 graph, the model stores only three learned edges per cell on average. At 4096 semantic cells with a restorer every eight cells:

- learned two-terminal links: 12,288;
- restoration junctions: 512;
- small state MIMs: 4,096;
- crude reference using one 6T SRAM weight per edge plus a 6-MOS firing block per cell: 98,304 MOS.

That corresponds to about 7.7 reference MOS devices per v14G two-terminal device in this deliberately simple structural comparison. It is **not a dollar-cost, area, or measured-energy claim**. Passive crossbar periphery, selectors, programming infrastructure and yield can erase this advantage and must be counted later.

## Selected v14G direction

`input pattern -> learned goal cell -> context/fact co-firing -> sparse learned links -> forward evidence + reciprocal Goal Echo -> passive associative chain -> sparse TRJ restoration only where required -> answer population -> output transducer`

No MOS transistor is permitted in the semantic/reasoning core candidate.

## Keep / reject

KEEP:
- semantic context as co-firing history;
- question goal as a physical source of backward/reciprocal evidence;
- sparse learned connections;
- passive cells for most of the fabric;
- sparse restoration rather than one active device per cell;
- partial energy reciprocity and the existing reservoir hierarchy for unrecovered energy.

REJECT:
- one expensive exotic device replacing every MOS transistor;
- dense all-to-all connection memory by default;
- pure strongest-link forward propagation for deep ambiguous reasoning;
- claiming associative lookup can solve an operation that has never been learned or physically represented;
- claiming OTS/memristor hardware is already cheaper than mature CMOS before process/energy/yield closure.

## Next physical problem

The next experiment must create a transistor-free **structural operator** that can generalize a learned relation without storing one link for every possible value. Arithmetic is the cleanest test. Candidate directions include residue/phase-coded value cells, wave displacement operators, or another regular physical transform. It must be cheaper than a lookup table and must compose with Goal Echo.
