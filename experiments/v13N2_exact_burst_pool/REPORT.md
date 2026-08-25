# Neural Glyph v13N2 — Ambiguity-Burst Exact-Pool Sizing

**Verdict: MODEL PASS.** A shared exact backbone can preserve computer-grade fallback availability without one exact core per octet, but the pool must be sized from the measured ambiguity rate rather than minimized blindly.

## Why this experiment
v13N0 showed that sharing exact cores saves large duplication with tiny route energy. The remaining danger is burst contention: many octets may become uncertain at once.

v13N2 models 32 intelligent octets. Each octet independently requests exact service with probability `p` in one normalized service epoch. One exact service slot can accept one request during that epoch. If more requests arrive than slots, excess requests wait; they are **not** converted into wrong local accepts.

The model asks how many slots are needed so immediate-service overflow occurs less than 1%, 0.1% or 0.01% of epochs.

This is a capacity model, not a claim about a particular processor clock. A real pipelined core that serves multiple requests per epoch would need fewer physical cores than these one-slot equivalents.

## Key 99.9%-fit result
For overflow probability <=0.1%:

| Ambiguity Budget | exact service slots | reduction vs 32 per-octet slots | actual overflow |
|---:|---:|---:|---:|
| 1% | **3** | **90.6% fewer** | 0.0287% |
| 2% | **4** | **87.5% fewer** | 0.0411% |
| 5% | **6** | **81.25% fewer** | 0.0868% |
| 10% | **9** | **71.875% fewer** | 0.0809% |
| 20% | **14** | **56.25% fewer** | 0.0561% |
| 25% | **16** | **50% fewer** | 0.0600% |
| 50% | **25** | **21.875% fewer** | 0.0268% |

## What happened
At the low ambiguity rates v13N is trying to create, the exact-computer capability can be heavily pooled without making immediate exact service rare.

Example: if only 5% of 32 octets request exact service in a given epoch, six one-request service slots cover >99.9% of independent-demand epochs. That is **26 fewer exact slots** than one-per-octet duplication.

## Important limitation
Fallback requests in real AI workloads are not guaranteed independent. A novel global event may make many regions uncertain together. Therefore this model is a lower-bound planning tool, not final queue signoff.

A burst-correlated workload must be replayed before choosing silicon counts. Overflow means queue/delay or escalation, never silent local acceptance.

## v13N consequence
The hollow interior should not be filled uniformly. Exact Service Core / memory capacity should scale with observed ambiguity and burst correlation. Empty volume is cheaper than unused exact hardware.

## Decision
- SIZE exact capacity from workload ambiguity/throughput.
- KEEP queue/exact fallback behavior safe under overflow.
- DO NOT duplicate exact cores merely to eliminate femtojoule-scale access routes.
- DO NOT under-provision so aggressively that exact fallback becomes unavailable when novelty arrives.

## Next
Measure Ambiguity Budget and correlation on a real multi-region trace. Then map the required exact slots into actual Component Bays with memory bandwidth and thermal constraints.

## Reproduce
`python3 experiments/v13N2_exact_burst_pool/source/run_v13n2.py`

Evidence class: deterministic binomial capacity model. No processor throughput or AI-accuracy claim.
