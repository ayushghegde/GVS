# Neural Glyph v13O1 — Typed Relation Wavefront

**Verdict: MODEL PASS.**

## New term
**Relation Wavefront:** a query event propagates only through physical/local connections carrying the requested relation type, so graph reasoning traverses stored connectivity rather than scanning a memory table with a processor.

## Experiment
Sparse directed typed graphs with 128–512 entities, average degree 4 or 8, and 8–16 relation types were generated deterministically. Each test used 500 grounded multi-hop queries, ensuring at least one valid target existed.

For every requested relation in sequence, only currently active frontier nodes inspect/activate matching local relation edges.

## Result
All tested configurations retained the grounded target in **100%** of 500 queries at 2, 4 and 8 hops.

For 512 nodes, degree 4, 16 relation types:
- 2 hops: mean 2.334 matching edge events, ~0.057% of full-scan edge inspections;
- 4 hops: 4.84 events, ~0.059%;
- 8 hops: 9.872 events, ~0.060%.

Using the preserved 0.67 fJ selected event-spine proxy only as a conservative carrier comparison, the 8-hop case is ~6.61 fJ of event-carrier proxy. This is not whole-query physical energy.

## Problem
The graph is already compiled into connectivity. v13O1 does not yet solve cheap learning/storage of millions of changing relations or natural-language binding.

## Reproduce
`python3 experiments/v13O1_relation_wavefront/source/run_v13o1.py`
