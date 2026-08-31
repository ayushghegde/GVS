# Neural Glyph v14J — Self-Plastic Capacitive Connection Memory

**Status:** model-level plastic-link architecture plus real SKY130 fixed-capacitor inference floor. No programmable v14J memcapacitor has been fabricated or closed in the current SKY130 process.

## Central change
v14H moved long-term semantic memory out of persistent node voltage and into sparse connection strength. v14J makes the connection itself plastic.

A semantic cell keeps only temporary excitation for the current thought. Long-term knowledge is the physical transfer strength of the connection.

`temporary node charge -> decays after thought`

`connection capacitance/state -> persists across thoughts`

## New primitive — Self-Polarizing Capacitive Link (SPCL)

**Self-Polarizing Capacitive Link (SPCL):** a two-terminal connection whose nonvolatile capacitance is changed by the polarity/history of electrical learning pulses, so future inference excitation is transferred more strongly through useful relations and more weakly through disproven relations.

Intended behavior:

- low-amplitude read excitation transfers charge but is below the programming threshold;
- useful pre/post activity plus a local confirmation echo generates one programming polarity and increases coupling;
- contradiction/error feedback generates the opposite differential polarity and decreases coupling;
- later evidence can reverse the state again;
- no semantic value is stored as persistent voltage in the connected cells.

The correctness/contradiction echo is not optional. Electricity alone cannot know that a semantic relation is true. v14J reuses Goal Echo, local contradiction evidence, and Population Confidence as the source of local learning polarity; there is no per-link digital address or weight-update controller in the candidate core.

## Why bidirectional plasticity is required
A strengthen-only Hebbian link accumulates obsolete strong paths after knowledge changes. v14J0 therefore compares strengthen-only learning against reversible strengthen + weaken learning, with one/two/three parallel link copies under read variation, programming failure, and false feedback.

The reversible rule wins decisively in the current model.

## Hardware anatomy
The cheapest inference floor is ordinary fixed MIM geometry:

`weak relation -> ~1x1 um MIM-like coupling`

`strong relation -> ~2x2 um MIM-like coupling`

Magic/SKY130 extraction confirms both geometries are legal and gives a strong/weak effective coupling proxy of about 3.41x after direct TOP-BOT parasitic capacitance is included.

That fixed geometry cannot learn. It is only the cost/physics floor that a programmable connection must beat.

The trainable candidate is a future-process ferroelectric/memcapacitive link. HZO ferroelectric-capacitor literature demonstrates reversible nonvolatile capacitance states and non-destructive low-voltage read, but v14J does not assume those reported devices are automatically cheaper than CMOS or directly portable to SKY130.

## v14J0 learning evidence
Continual-learning screen:

- 1000 source relations;
- 500 possible targets;
- 12 rounds;
- 5% of relations changed per round;
- three local learning pulse-pairs per changed relation;
- 20% inference-read variation;
- 5% independent programming-failure probability;
- false learning feedback swept from 0 to 10%.

Selected reversible results:

- 1 link copy, clean feedback: 99.5% final accuracy;
- 2 copies: 99.9%;
- 3 copies: 100%;
- with 5% false feedback: 97.2%, 99.3%, 99.7% for 1/2/3 copies;
- with 10% false feedback: 93.6%, 97.9%, 98.0%.

Never-changed knowledge remains essentially intact because only active local links receive programming pulses.

Strengthen-only control falls to roughly 60-69% final accuracy after repeated relation changes even with multiple copies. Old strong paths are never removed.

## Six-hop relearning
A six-hop relation fabric was locally modified in 25% of chains. Only the changed edge was reprogrammed.

With 5% programming failures and 10% false feedback:

- one link copy: ~96.1% exact six-hop paths;
- two copies: ~99.4%;
- three copies: ~99.4%.

This is a synthetic graph test, not arbitrary natural-language reasoning.

## Read/program separation
The device-state model uses a 0.2 V inference pulse, a nominal 1.5 V plasticity threshold, and a 3 V learning pulse envelope. With 20% threshold variation in 200,000 samples:

- modeled read-disturb events: 0;
- modeled programming pulses above threshold: 100%.

These voltages are screening parameters, not a selected physical process. The v14J device must ultimately reduce programming overhead enough that learning circuitry does not destroy the cost advantage.

## Physical fixed-link floor
Magic 8.3.681 / SKY130A:

- 1x1 um MIM weak link: 0 DRC, real `sky130_fd_pr__cap_mim_m3_1`;
- 2x2 um MIM strong link: 0 DRC, real `sky130_fd_pr__cap_mim_m3_1`;
- current-PDK nominal MIM model plus direct extracted TOP-BOT parasitic gives ~2.737 fF weak and ~9.345 fF strong;
- effective strong/weak ratio ~3.415x.

For a 5 fF receiving-node proxy and four co-firing links at 0.2 V, the modeled target rises from ~137 mV with four weak links to ~176 mV with four strong links. This establishes a physical inference mechanism but not programmable learning.

## KEEP
- semantic memory primarily in sparse connection state rather than persistent node voltage;
- ordinary cells ephemeral between questions;
- reversible electrical plasticity: useful path strengthens, disproven path weakens;
- local programming only on recently active connections;
- Goal Echo / contradiction / Population Confidence as the learning-polarity source;
- weak/strong or small-number-of-level states before high-precision analog weights;
- two or three parallel copies only where learning/read faults justify them;
- fixed MIM connection plane as the cheapest inference-only control.

## REJECT / CONDITIONAL
- strengthen-only Hebbian learning as the main rule: REJECT;
- preserving semantic memory as node voltage: REJECT;
- high-precision per-link analog weights by default: REJECT until needed;
- claiming ordinary SKY130 MIM learns: REJECT;
- claiming HZO memcapacitor is cheaper than CMOS before process/programming/yield accounting: REJECT;
- high-voltage per-link programming circuitry: REJECT unless shared/amortized cost proves acceptable;
- autonomous learning with no truth/goal/contradiction signal: REJECT; correlation alone cannot distinguish a useful association from a repeatedly wrong one.

## Meaning of intelligence in v14J
v14J is not a math architecture. The same plastic connection rule is intended to support language context, episode recall, causal chains, code relations, planning, analogies, transformation selection, and other learned structures. Specialized exact operators such as CRRO remain reusable structures recruited only when the connection fabric creates a Need Potential for them.
