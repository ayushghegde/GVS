# Neural Glyph v14K — Self-Revising Understanding Fabric

**Status:** model-level architecture built on the v14J self-plastic connection-memory fabric. The semantic/reasoning core remains transistor-free by requirement. v14K does not claim fabricated self-rewiring hardware; it defines and tests how connection structure should revise when new teaching changes an explanation.

## Central change from v14J

v14J proved that a learned connection must be electrically reversible: useful routes strengthen and contradicted routes weaken. v14K adds a harder requirement: learning must also be able to create a previously absent explanatory relation and retire an obsolete shortcut.

Long-term understanding is therefore not a stored voltage and not a single answer edge. It is a sparse explanatory graph embodied in connection state.

- semantic node charge is temporary;
- connection state is persistent;
- dormant candidate crosspoints provide finite structural-plasticity capacity;
- new teaching may activate dormant links;
- contradiction may drive obsolete links toward OFF;
- the original unresolved question is immediately replayed after revision;
- a revision is consolidated only when self-test / later evidence supports it.

## New primitive — Effort Eligibility Field (EEF)

**Effort Eligibility Field (EEF):** a short-lived local plasticity bias that grows when a reasoning neighborhood repeatedly fails to satisfy the active Goal / Population Confidence condition.

EEF is not semantic memory and does not contain an answer. It only says: `this unresolved neighborhood has spent repeated activity trying to resolve the goal, so a relevant lesson should be allowed to modify it more strongly.`

The intended cheap implementation is a shared local transient field/capacitive bias, not one persistent effort-memory device per connection.

Repeated failure without teaching does not permanently rewrite knowledge.

## New primitive — Dormant Structural Plasticity Slot (DSPS)

**Dormant Structural Plasticity Slot (DSPS):** a physically pre-existing but nearly-OFF candidate connection that can be electrically moved OFF <-> WEAK <-> STRONG when a newly taught relation recruits that pair of local concepts.

A chip cannot grow a wire across arbitrary distance after fabrication. Structural learning therefore means activating/deactivating sparse pre-laid candidate crosspoints, not creating literal new metal routes.

At the v14H model scale (2,852 semantic cells), eight logical candidate slots per cell provide 22,816 slots, versus more than eight million directed pairs in a dense fabric. This is a logical capacity proxy, not silicon area.

## New mechanism — Self-Test Consolidation Cycle (STCC)

1. Attempt the question from the current connection structure.
2. If no robust answer is reached, EEF rises locally and the unresolved cue/goal trace remains briefly available.
3. A lesson co-activates new concepts/relations.
4. Dormant compatible DSPS links receive provisional SET pulses.
5. Contradiction feedback gives the obsolete explanation a depression/RESET pulse.
6. Remove the teacher signal and replay the original question through the revised fabric.
7. If Population Confidence resolves the question and related transfer probes remain coherent, consolidate the new links.
8. If the self-test fails or later evidence contradicts the lesson, leave the revision weak/provisional or reverse it.

The hardware therefore tries to use what it just learned instead of merely storing the teacher's sentence.

## Understanding versus memorization

v14K defines a learned explanation as useful only if it supports queries implied by the structure, not only the exact training question.

A three-link explanatory chain in the v14K structure screen answered five related query forms: intermediate state, mechanism, final result, and transfer from intermediate states. A single direct cue->answer memory covered only one of those five forms.

This is still a small synthetic graph test; it is not proof of human-level understanding.

## Broad revision model

The v14K model applies the same revision rule to synthetic cases labelled:
- biology concept revision;
- newly taught mathematical formula;
- code rule / repair revision;
- causal explanation;
- planning prerequisite;
- language-context relation.

The labels do not imply full real-world competency. They test whether one physical structural-learning rule can revise different relation graphs without domain-specific instruction machinery.

### Selected result

In the broad synthetic revision screen:
- static old understanding: 0% post-lesson solution of the deliberately missing explanation;
- strengthen-only: formed the taught chain but left the old strong route, so the old answer continued to dominate;
- v14J existing-link-only: could alter old weights but could not create missing explanatory intermediates;
- v14K structural revision without effort weighting: about 77.3% immediate post-learning correctness;
- v14K with EEF: about 97.0% in the clean model while touching about four logical links/lesson and preserving unrelated knowledge in the tested graph.

For the explicit formula-after-struggle screen, increasing unresolved attempts from one to four increased one-shot post-teaching success from about 33% to about 95% under the model's effort-gated plasticity rule. This is a synthetic model result, not a claim about human learning.

## Provisional understanding

Hardware replication protects device faults but cannot repair a semantically wrong lesson delivered to every copy. v14K therefore adds provisional consolidation.

New explanations begin weak. When lesson confidence is uncertain, three or five partially independent corroborating observations vote on the semantic direction before strong consolidation.

At 15% false evidence with 5% program failure and 20% read variation:
- immediate single-evidence commit: ~75.2% post-learning correctness;
- provisional majority of 3: ~89.3%;
- provisional majority of 5: ~92.1%.

At 20% false evidence:
- immediate: ~69.2%;
- majority-3: ~84.1%;
- majority-5: ~88.1%.

Five-evidence consolidation roughly doubles local programming events in this model, so it is not the default for high-confidence lessons. Correlated/systematic misinformation remains an unsolved common-mode failure; majority evidence only helps when evidence errors are at least partly independent.

## Finite structural capacity

Structural plasticity is not free. With eight candidate slots/cell in the current logical proxy:
- 5,000 explanation revisions occupy about 67% of available slots;
- 8,000 reach about 93%.

Four slots/cell nearly saturate around 3,000 revisions in the same proxy. Future physical work must therefore include pruning/reuse, local reserve connection banks, or hierarchical concept allocation.

## Hardware direction

v14J already established the inference cost floor: fixed weak/strong SKY130 MIM geometries can provide a useful capacitance ratio without a transistor in each semantic link. Ordinary MIM is not electrically plastic.

v14K therefore requires a future programmable connection element with at least:
- OFF / WEAK / STRONG effective coupling;
- reversible SET and depression;
- low-voltage nondestructive inference;
- local program selectivity / low half-select disturbance;
- enough endurance for continual revision;
- total write/selection infrastructure cheaper than the transistor baseline.

Ferroelectric memcapacitors are a physically relevant research candidate, not yet a selected GVS process device.

## Keep / reject

KEEP:
- persistent meaning in sparse connection structure, not semantic node voltage;
- temporary excitation charge during a thought;
- reversible connection plasticity from v14J;
- sparse dormant connection slots for new explanatory relations;
- local EEF after unresolved effort;
- immediate teacher-free self-test after learning;
- provisional learning under uncertain evidence;
- transfer/implied-query coverage as an understanding test;
- Goal Echo and Population Confidence.

REJECT:
- strengthening a new route without weakening the disproven old route;
- assuming v14J can learn a relation whose physical connection slot does not exist;
- a dense all-to-all rewiring matrix;
- making high effort itself evidence that a lesson is true;
- fully consolidating every one-shot uncertain lesson;
- copying the same semantically wrong update across many redundant links and calling it robust;
- claiming that the current synthetic graph is general intelligence.
