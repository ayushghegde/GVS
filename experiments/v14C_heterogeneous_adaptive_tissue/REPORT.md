# v14C — Heterogeneous Adaptive Reasoning Tissue

**Verdict: SYSTEM MODEL PASS / PHYSICAL ADAPTIVE-SUPPORT PVT PASS / FULL PEX-MISMATCH CONDITIONAL.**

## What changed
The earlier architecture used four fully general reserve cells. A reserve-count sweep found six full reserves improve latency but do not always maximize hardware efficiency. v14C differentiates the reserve itself: four full General Reserve Cells plus two Critical Reserve Cells carrying only Constraint+Exact Expression Patches.

## Complete-question benchmark
The benchmark is not an isolated role counter. Each arriving question requires a sequential set of physical roles:
- association: Grammar -> Template;
- relation: Grammar -> Binding -> Grammar;
- constraint: Grammar -> Binding -> Constraint -> Constraint;
- exact: Grammar -> Binding -> Exact;
- mixed: Grammar -> Template -> Binding -> Constraint -> Exact.

Seven 120-epoch workload phases include balanced, relation-heavy, template-heavy, binding-heavy, constraint-heavy, exact-heavy and mixed demand, plus burst noise and 10% specialized-cell loss at midpoint. Delayed work queues; it never becomes a wrong answer.

### Three-organization control
At 100 seeds, the baseline 4-reserve adaptive organization gives ~71.7% on-time completion versus ~52.0% fixed differentiated and ~100% universal. Universal uses 320 optional module copies; fixed/adaptive use 60.

### Reserve differentiation
The 4 General + 2 Constraint/Exact CRC organization gives at 10% cell loss:
- eventual completion: 100%;
- within-20-epoch completion: ~90.11%;
- p95 latency: ~22.36 epochs;
- optional module copies: 64.

The two CRCs replace two relay-only positions, so region cell count stays 64. Because all ECCs participate in cell-as-wire conduction, this does not remove two conduction sites.

Under 0/10/20/30% specialized-cell loss, the CRC design remains complete in the modeled drain window. Heavier failure still increases latency; no claim of fault immunity is made.

## Adaptive support cost
Selected FAST/SLOW Role Pressure per full reserve uses about 61.88 fF total pressure+bucket capacitance. Charging that whole amount to 1 V once per role switch gives a deliberately conservative ~30.94 fJ/switch capacitor-energy proxy. Together with the preserved 0.156 fJ/completed-operation support-event proxy and ~0.15 fJ local transition proxy, modeled adaptive/communication support remains around the fJ/question scale, far below the preserved ~pJ local intelligent-region proxy. This is a proxy, not PEX energy.

## Physical adaptive-support evidence
Selected physical timing:
- FAST: 2 MIM, injector 1.26/0.50 um;
- SLOW: 4 MIM, injector 1.38/0.50 um;
- 27/27 matched PVT points preserve SLOW-after-FAST;
- minimum gap ~10.023 ns, mean ~24.855 ns.

Earlier 8-MIM SLOW storage is rejected: PEX/PVT showed low-supply non-recruitment. The 4-MIM SLOW bank halves that storage and passes the selected 27-point PVT table.

Preliminary independent TT mismatch evidence: FAST ~150.3–160.4 ns, SLOW ~170.6–180.3 ns for 12+12 runs. A 2x empirical half-span screen still leaves ~0.30 ns timing-order margin; 2.1x can cross. Ordering crossover is therefore treated as an adaptation-speed degradation, not a correctness fault. Full 48+48 PDK Monte Carlo remains open and is not claimed here.

## Hard reasoning
A high-load hard-query screen reuses v13U's measured stochastic-search probabilities (96-variable per-attempt success ~0.50; 128-variable ~1/6). At four attempts, v14C adaptive tissue answers about 70% within 20 epochs while fixed differentiation falls below 30% and universal is about 79%. Eventual resolution remains about 79% because the reasoning dynamics, not capacity, dominate.

Allowing 12 attempts increases eventual resolution to about 96% but lowers on-time throughput. Confidence–Pressure Effort with a low pressure threshold improves both eventual resolution and on-time completion slightly relative to a fixed four-attempt rule. This keeps difficult questions from consuming unlimited local tissue during congestion.

## Decision
KEEP:
- differentiated ordinary cells;
- 4 full General Reserve Cells;
- 2 Constraint/Exact Critical Reserve Cells;
- selected 2-MIM FAST / 4-MIM SLOW Role Pressure;
- CHL, hysteresis, developmental-wave re-role and break-before-make;
- cell-as-wire, Population Confidence and neurovascular recovery;
- low-pressure conditional extra settling.

REJECT:
- universal full-feature cells as default;
- 8-MIM SLOW pressure store;
- six or eight fully general reserve cells as default;
- unlimited hard-query settling under congestion;
- interpreting unresolved states as answers.

## Limitation
v14C is a system-model promotion candidate, not a fully fabricated chip or foundation-model demonstration. Exact integrated Magic source for the newly selected full Role-Pressure+CRC cell and a completed 48+48 PDK Monte-Carlo/PEX battery still need to be preserved. The next experiment is aimed at that physical freeze plus a larger multi-region reasoning trace.
