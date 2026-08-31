# Neural Glyph v14H — Need-Triggered Structural Reasoning

**Status:** model-level reasoning architecture. v14G remains the transistor-free associative-semantic candidate; v14H adds a reusable exact addition operator and a need-triggered transformation-control hypothesis. No v14H two-terminal device has yet been physically closed.

## What happened

v14G found an important limit: associative recall can follow learned relations, but it does not automatically invent an exact operation that was never stored as a value-to-value link. v14H attacks that problem in two layers.

First, v14H0 compares three exact-operation candidates: residue/phase rings, a reusable wave-displacement track, and sparse value-to-value lookup. The residue operator wins the current model screen.

Second, v14H1 tests the user's observation that multi-step reasoning does not need a stored instruction sequence. A learned transformation is recruited only when the current state creates a need for it. In the rectangle example, assigning x, forming x+5, applying area, moving 84 to the left, factorizing, and choosing the physically valid root are separate transformations that become relevant at different states.

## New primitive — Coprime Residue Ring Operator (CRRO)

**Coprime Residue Ring Operator (CRRO):** a structural arithmetic operator that represents one value simultaneously by its phase/position on several coprime residue rings, so addition is performed by the same physical displacement geometry for every operand pair.

The current screen uses moduli 3, 4, 5, and 7. Their least common multiple is 420, so the residue tuple uniquely identifies one value in `Z_420`.

For a value `n`, the local state is:

`(n mod 3, n mod 4, n mod 5, n mod 7)`

Addition is local on every ring:

`r_m(out) = (r_m(a) + r_m(b)) mod m`

No learned edge for the specific pair `(a,b)` is required. The result can remain residue-coded for the next operation; a global value decode is needed only at a boundary that requires ordinary numeric representation.

### Variation protection

The selected model uses five local copies of each residue ring and majority restoration within each modulus. That is 95 residue-state sites total: `5 × (3+4+5+7)`.

Variation is modeled as combined static fabrication offset plus event noise, with total RMS expressed as a fraction of one residue-state spacing. This is a model coordinate, not a measured device distribution.

## v14H0 model evidence

Domain: exact modular addition in `Z_420`.

- total operand pairs: 176,400;
- sparse lookup stores 25% = 44,100 pairs;
- held-out pairs: 132,300;
- CRRO nominal exact rate on all held-out pairs: 100%;
- three-track wave-displacement nominal exact rate on all held-out pairs: 100%;
- sparse lookup direct exact rate on held-out pairs: 0%;
- nearest memorized-pair interpolation control: 6.8% on 1,000 held-out samples.

At variation sigma = 0.20 of one state pitch, with 5,000 eight-operation chains:

- CRRO-5 exact chains: 99.98%;
- three-track wave operator exact chains: 99.54%.

At the same stress for 32-operation chains:

- CRRO-5 exact chains: 99.76%;
- wave-3 exact chains: 98.92%.

### Structural hardware proxy

This is not an area, energy, yield, or dollar comparison.

- CRRO-5: 95 residue state sites, 0 programmable operand-pair links;
- wave-3: 1,260 displacement state sites, 0 programmable operand-pair links;
- 25% lookup: 44,100 programmable operand-pair links and incomplete coverage;
- full lookup: 176,400 programmable operand-pair links.

The CRRO therefore wins the present screen because it generalizes to unseen pairs, composes under modeled variation, and has much lower state-site count than the reusable wave track while eliminating value-pair memory.

## Important limitation — this is not general arithmetic yet

The current CRRO proves only reusable **addition modulo 420**. It does not yet provide unbounded integers, multiplication, division, factorization, floating point, symbolic algebra, or arbitrary code execution.

The user example `x(x+5)=84 -> x^2+5x-84=0 -> factor` still requires structural multiplication/factorization hardware. v14H does not hide those operations behind a CPU.

## Confidence problem found

The current five-replica majority signal is not a sufficiently selective correctness detector. At sigma = 0.20 it flags many correct-but-noisy operations and catches only part of the very rare wrong states. Extra mod-6, mod-10, mod-140 and mod-210 coherence rings were screened; their detection improvement did not justify their added state cost in the current model.

Therefore:

- CRRO is accepted as the arithmetic **operator candidate**;
- its current confidence detector is **not physically closed**;
- Population Confidence must be improved before exact-answer signoff.

## New mechanism — Need Potential

**Need Potential:** a local mismatch signal produced when the current active state lacks a relation or transformation required by the active goal.

A Need Potential does not contain an instruction address. It biases only transformation cells compatible with the unresolved state.

Example:

`unknown width + goal(width)` -> need symbolic binding

`width=x + length is five greater` -> need relation expression

`dimensions known + area=84` -> need area relation

`x(x+5)=84 + factorable goal` -> need zero-form equation

`x^2+5x-84=0` -> need factor/root transformation

The sequence emerges because solving one need changes the physical state and therefore changes which Need Potential exists next.

## New primitive — Need-Triggered Transformation Cell (NTTC)

**Need-Triggered Transformation Cell (NTTC):** a reusable learned transformation site that becomes active only when the present state and Goal Echo match its preconditions; it is not a stored step number in a program.

The intended local competition is:

`current state + Goal Echo + unresolved relation -> Need Potential -> compatible NTTC population -> structural transform -> new state`

Then the old need disappears and another may appear.

## v14H1 selection experiment

A control-level screen generated every unique combination of:

- width 1..50;
- length offset 1..20;
- six possible starting transformation stages.

That gives 6,000 unique problem states. Only 25% were placed in a full-state lookup control; 4,500 exact numeric states were held out.

Results:

- need-gated reusable transformation traces on held-out numeric states: 100% nominal;
- exact full-state lookup first-action success on held-out states: 0%;
- blind fixed six-step sequence trace success: about 16.58%, because it only works when the problem happens to begin at stage zero.

The experiment also stressed corrupted need-state features with replicated local populations. With nine copies per feature population:

- 5% independent feature-flip probability: 99.99% trace success;
- 10%: 99.71%;
- 15%: 97.64%;
- 20%: 90.48%.

These are abstract control-model results, not measured hardware reliability.

## The 84-area example

The v14H reasoning interpretation is:

1. need an unknown representation -> width becomes `x`;
2. need the dependent dimension -> length becomes `x+5`;
3. need the geometry relation -> `x(x+5)=84`;
4. need zero-form for the available factor relation -> `x^2+5x-84=0`;
5. need roots -> `(x+12)(x-7)=0`;
6. need a physically valid dimension -> choose `x=7`.

The key point is not the specific school method. The key point is that no cell needs to store “step 1, then step 2, then step 3.” Each transformation is reusable and becomes active only because the current state needs it.

## Keep / reject

KEEP:
- v14G Goal Echo and sparse associative fabric;
- reusable structural operations instead of value-pair memorization;
- CRRO-5 as the current exact-addition candidate;
- residue-coded chaining so decoding is not required after every operation;
- Need Potential as the local reason a transformation becomes relevant;
- NTTCs as reusable transformations selected by state, not program position;
- Population Confidence as answer authority.

REJECT:
- sparse lookup as a substitute for unseen arithmetic;
- a fixed instruction sequence for all problem presentations;
- claiming modular addition solves general arithmetic;
- adding large coherence rings that do not repay their state cost;
- reintroducing a hidden transistor CPU to perform multiplication/factorization.

## What is next

The next canonical experiment is a **structural multiplication/factor relation operator** that composes with CRRO and NTTC selection.

It must:

1. solve unseen products/factor relations rather than memorize pairs;
2. remain transistor-free in the v14G/v14H reasoning core candidate;
3. compose with residue-coded addition without global binary conversion;
4. provide a stronger confidence/error boundary than the current CRRO majority flag;
5. beat a lookup-table implementation in state/link cost;
6. reproduce the `x(x+5)=84` trace without handing multiplication or factorization to a conventional processor.
