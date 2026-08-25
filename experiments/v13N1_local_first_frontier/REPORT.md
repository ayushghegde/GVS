# Neural Glyph v13N1 — Local-First Intelligence / Exact-Fallback Frontier

**Verdict: MODEL PASS with a quantitative break-even.** Local physical intelligence does not need to replace computer-grade exact computation. It is economically useful whenever it resolves enough common work that the avoided exact computation repays the ~1.324 pJ preserved octet cost.

## New term
**Ambiguity Budget:** the fraction of local intelligent-region episodes that cannot be accepted locally and therefore request exact fallback.

## Question
Can GVS retain the smartness/correctness boundary of an exact computer while making exact execution rare enough that the expensive exact hardware becomes a shared exception path?

This experiment deliberately does not assume a favorable exact-compute energy. It sweeps exact work from 0.5 to 100 pJ.

## Preserved values
- v13M two-octet/local octet episode proxy: **1324.1144 fJ** for one selected intelligent octet episode;
- v13N0 four-core shared interior placement: **17.765 fJ** average request+return route per exact fallback.

The exact-core internal compute energy is the swept unknown.

## Comparison
**Exact-every-episode:** every episode executes on exact hardware.

**Local-first:** pay the local intelligent-octet episode; only the Ambiguity Budget fraction also pays exact access + exact computation.

Common sensor/input costs are outside this comparison.

## Break-even exact-compute energy
Local-first becomes lower-energy than exact-every-episode when exact computation exceeds:

| exact fallback fraction | local resolution | exact-compute break-even |
|---:|---:|---:|
| 1% | 99% | **~1.320 pJ** |
| 5% | 95% | **~1.376 pJ** |
| 10% | 90% | **~1.453 pJ** |
| 25% | 75% | **~1.748 pJ** |
| 50% | 50% | **~2.630 pJ** |
| 75% | 25% | **~5.279 pJ** |

This is a useful result because the required break-even is not extreme. The architecture can still win even when local intelligence resolves only half the episodes, provided an exact episode costs more than ~2.63 pJ in this proxy.

## Example points
At a hypothetical 5 pJ exact episode:
- 5% fallback -> local-first ~1.575 pJ vs ~5.018 pJ exact-every-episode: **~68.6% lower**;
- 10% fallback -> ~1.826 pJ: **~63.6% lower**;
- 25% fallback -> ~2.579 pJ: **~48.6% lower**.

At a hypothetical 10 pJ exact episode:
- 10% fallback -> ~2.326 pJ vs ~10.018 pJ: **~76.8% lower**.

These are sensitivity-model results, not measurements of a real CPU/NPU energy.

## What happened
v13N turns the local analog/physical mechanisms into a cost filter in front of exact computation rather than asking them to imitate an entire digital computer.

The smartness boundary stays hybrid:
`common/reused/local structure -> physical intelligence`
`ambiguous/new/exact state -> shared exact service`

## Important limitation
This does **not** prove foundation-model intelligence or software-equivalent accuracy. The experiment only proves the system-energy break-even for a hybrid exact-fallback architecture given a measured future local-resolution rate and exact-compute cost.

## Decision
- KEEP exact fallback always available.
- Do not send every easy/repeated local operation to exact hardware.
- Measure the real Ambiguity Budget on representative workloads before choosing final core count.
- If local resolution is poor, improve useful local primitives/placement rather than hiding the problem with more recovery/control rules.

## Next
v13N2 sizes the shared exact pool against bursty ambiguity so pooling does not create a computer bottleneck.

## Reproduce
`python3 experiments/v13N1_local_first_frontier/source/run_v13n1.py`

Evidence class: deterministic sensitivity model using preserved GVS local/route proxies. Exact-compute energy is explicitly swept, not claimed measured.
