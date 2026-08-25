# Neural Glyph v13N3 — Shared Exact-Service Transport Tax

**Verdict: MODEL PASS.** In the preserved 32-octet geometry, the *transport-only* cost of sharing exact computer hardware is already sub-percent relative to one local intelligent-octet episode over the tested core counts and ambiguity rates. The exact computation itself is not included and is not claimed negligible.

## New term
**Transport Support Tax:** average energy spent only moving an exact-fallback request/result between a local octet and the shared Exact Service Core pool, divided by the preserved local-octet episode energy.

This metric answers a narrow question: does pooling exact hardware create so much communication that the saved duplication is defeated?

## Preserved values
- local intelligent octet episode: 1324.1144 fJ;
- v13N0 average exact request+return route:
  - 1 core: 41.14 fJ;
  - 2 cores: 29.4525 fJ;
  - 4 cores: 17.765 fJ;
  - 8 cores: 13.09 fJ;
  - 16 cores: 3.74 fJ.

Average transport per episode is `fallback_fraction * route_cost`.

## Key results
For four shared exact cores:
- 1% fallback -> **0.178 fJ/episode**, tax ~**0.013%**;
- 5% -> **0.888 fJ**, ~**0.067%**;
- 10% -> **1.777 fJ**, ~**0.134%**;
- 25% -> **4.441 fJ**, ~**0.335%**;
- 50% -> **8.883 fJ**, ~**0.671%**.

Even the single-central-core geometry stays below 1% transport tax through the tested 25% fallback point (~0.777%).

## What happened
The cost of *reaching* shared exact capability is not the main problem in this geometry. Core compute energy, memory traffic, throughput, thermal load and manufacturing area are much more important unknowns.

This is useful because it means v13N can aggressively pool exact hardware without immediately paying back the saved duplication through long-wire energy.

## What this does not prove
- whole-chip cost is not negligible;
- exact compute energy is not negligible;
- memory bandwidth/latency is not closed;
- correlated novelty bursts are not closed;
- manufacturing cost of hollow packaging is not closed.

## Decision
Treat exact-service transport as a second-order energy term in the current v13N model, but keep measuring it after physical placement. Focus future cost reduction on duplicated exact/memory hardware, memory movement, ambiguity rate, packaging/yield and thermal support.

## Next
Stop adding abstract frugality rules. Run a representative multi-region trace through the canonical simulator to measure real local-resolution rate, exact-fallback correlation, memory/exact-service traffic and utilization. Then choose the physical number/size of Component Bays.

## Reproduce
`python3 experiments/v13N3_shared_service_tax/source/run_v13n3.py`

Evidence class: deterministic model using preserved GVS energy proxies. No physical exact-core or package claim.
