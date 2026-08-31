# v14K — Self-Revising Understanding Experiment Report

## Question
Can a connection-memory reasoning fabric revise its internal explanatory structure when a new lesson changes what the system should believe, rather than merely memorizing a new answer or altering only relations that already existed?

## v14K0 — Structural revision
2,100 synthetic cases across six relation domains began with a strong simplified/wrong path and a genuinely absent three-relation explanatory chain.

Controls:
- static;
- strengthen-only;
- v14J existing-link-only;
- v14K structural revision without effort weighting;
- v14K structural revision with effort weighting.

Clean-model post-learning correctness:
- static: 0%;
- strengthen-only: 0% on the original decision because the old shortcut remains dominant;
- v14J existing-only: 0% because missing intermediate relations cannot be allocated;
- v14K no-effort: ~77.3%;
- v14K effort: ~97.0%.

Selected v14K touched roughly four logical links per lesson: about three new explanatory links plus one contradicted shortcut. Unrelated stable links remained unchanged in this synthetic graph.

## v14K0b — Effort after struggle
A deliberately missing formula/relation was taught only after 1..4 failed attempts. Model one-shot retest success was approximately:
- 1 failed attempt: 33.2%;
- 2: 64.5%;
- 3: 87.1%;
- 4: 95.5%.

Interpretation: unresolved effort can raise local eligibility/plasticity so a relevant later lesson is imprinted more strongly. Effort does not determine whether the lesson is correct.

## v14K1 — Structural coverage
A three-link explanatory chain was queried in five related ways. It covered 5/5. A single direct cue->answer edge covered 1/5. This is a simple graph-transfer screen, not a general-understanding benchmark.

## v14K2 — Sparse candidate-link capacity
At 2,852 cells and 5,312 existing logical links, a proxy with eight dormant connection slots per cell gives 22,816 candidate slots. Under a simple +2 net links per explanatory revision assumption, 5,000 revisions reach ~67% occupancy and 8,000 reach ~93%. Four slots/cell saturate much earlier.

## v14K3 — Hardware redundancy
Parallel connection copies help read/write-device faults but give limited benefit when the learning signal itself is semantically wrong. Under one stressed condition, increasing one logical link to three physical copies only modestly improved immediate correctness. This demonstrates a common-mode semantic error that replication cannot solve.

## v14K4 — Provisional understanding
A new explanation was first written weak/provisional and was strongly consolidated only after 3 or 5 corroborating evidence events supported the same semantic direction.

At 15% independently wrong evidence, 5% program failure, 20% read variation:
- immediate commit: 75.2%;
- majority-3: 89.3%;
- majority-5: 92.1%.

At 20% wrong evidence:
- immediate: 69.2%;
- majority-3: 84.1%;
- majority-5: 88.1%.

Tradeoff: provisional consolidation costs roughly twice the program events of immediate commit in this model. It does not protect against fully correlated/systematic misinformation.

## Main conclusion
The useful v14K mechanism is not `remember the new sentence strongly`. It is:

`unresolved goal -> local effort eligibility -> lesson recruits/rewrites sparse connection structure -> obsolete explanation weakens -> teacher signal removed -> original problem replays -> transfer/self-test decides consolidation`.

This lets the internal explanatory graph change while ordinary semantic nodes retain no persistent voltage.

## Evidence boundary
All v14K0-v14K4 results are synthetic graph/control models. No v14K dormant programmable connection or effort-field device has been fabricated or PEX-closed. The v14J fixed-MIM inference links remain the nearest physical cost floor; programmable reversible memcapacitive links are future-process candidates.
