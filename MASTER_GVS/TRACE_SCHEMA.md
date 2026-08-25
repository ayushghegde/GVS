# GVS Canonical Multi-Region Trace Schema

This schema is the required interchange format for v13N4 and later workload-driven architecture sizing. It exists so different chats/agents do not invent different meanings for “fallback rate”, “local resolution” or “exact demand”.

## One row = one completed/intended intelligent-octet episode
Required CSV columns:

- `epoch` — discrete workload/service time bucket used for exact-demand concurrency measurement.
- `octet` — local intelligent-region identifier.
- `workload` — workload/trace class label such as motif, template-heavy, reasoning-like, code/exact-heavy, novelty-stress.
- `local_result` — `accept` when local robust hardware accepted; `fallback` when it safely refused; other values must be documented.
- `exact_request` — 1/0 indicating whether the episode requested shared exact service.
- `cross_handoffs` — number of handoffs to another intelligent octet/region.
- `memory_units` — exact-memory traffic quantity in the native trace unit; the unit must be stated beside the trace (bytes/words/cache-lines/etc.).
- `wrong_accept` — count of wrong robust local accepts; architecture acceptance requires zero in signed-off workloads.

Recommended columns:

- `exact_complete_epoch` — epoch in which exact service completed.
- `exact_service_slot` — selected Exact Service Core/slot identifier when modeled or measured.
- `local_ops` — number of local primitive operations completed in the episode.
- `lease_count` — Regional Event Lease acquisitions/active leases attributable to the episode.
- `lease_refreshes` — validated refresh count.
- `robust_events` — Nerve/spine/chord robust event count.
- `energy_fj` and component energy columns when directly measured or consistently modeled.
- `memory_unit_name` or sidecar metadata defining `memory_units`.

## Canonical meanings

**Local resolution fraction:** episodes with `local_result=accept` and no `exact_request`, divided by all episodes.

**Ambiguity Budget:** episodes with `exact_request=1`, divided by all episodes.

**Exact concurrency:** number of `exact_request=1` rows sharing one `epoch`.

**Wrong robust accept:** a local robust acceptance whose logical result is incorrect. It is not the same as a safe fallback or an exact request.

**Overflow:** exact demand in an epoch exceeds the selected service-slot capacity. Overflow must queue/delay/escalate; it may never authorize a local guess.

## Required provenance beside every trace
Every trace directory/report must state:
- workload/generator source;
- whether the trace is measured, simulated or synthetic proxy;
- epoch definition;
- memory-unit definition;
- architecture/commit used;
- random seeds if any;
- whether local decision correctness is known or only event counts are modeled.

A synthetic trace may validate tooling but may not be used as evidence for v13N Ambiguity Budget unless explicitly labeled proxy.

## Analyzer
Run:
`python3 scripts/gvs_trace_analyze.py <trace.csv> [--slots N] [--out summary.json]`

The analyzer reports local resolution, Ambiguity Budget, wrong accepts, cross traffic, memory traffic, exact-demand percentiles, empirical exact-slot requirements, workload split and optional queue pressure.
