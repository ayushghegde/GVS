# Neural Glyph v13N0 — Shared Exact-Core Pool

**Verdict: MODEL PASS.** Computer-grade exact/fallback capability should be pooled in a small number of interior Component Bays rather than duplicated inside every intelligent octet, unless measured traffic/latency proves that sharing is too slow.

## New term
**Frugal Exact Backbone (FEB):** a small pool of shared Exact Service Cores and exact memory/control resources serving many locally intelligent Glyph octets.

FEB is not a new processor architecture. It is a placement/resource-sharing rule for the exact hardware GVS already retains for ambiguity, boot/repair/configuration, memory and precise computation.

## Why v13N starts here
The objective is not to make the hollow package visually complicated. It is to make support hardware cheap enough that most silicon/energy is spent on useful local intelligence rather than duplicated control, repeated memory movement and repeated long selections.

Earlier v13K already selected interior Component Bays for frequently accessed exact/memory hardware and rejected one microcontroller per cell. v13N0 asks how aggressively that exact hardware can be shared geometrically.

## Geometry
Reuse the preserved 10 x 10 x 2 mm / 32-region class as 4 x 4 x 2 intelligent octet centers.

Compare 1, 2, 4, 8, 16 and 32 Exact Service Core copies. Shared cores are placed on the interior midplane; candidate placements are searched to minimize average Manhattan distance. The one-core case uses the preserved central position (5,5,1) mm and reproduces the earlier 5.5 mm average distance.

Existing dedicated electrical-route proxy: ~3.74 fJ/mm. Round-trip route cost is modeled as request + return.

No exact-core area or compute-energy number is invented here. Core-copy reduction and access-route cost are reported separately.

## Results
| Exact cores | copies removed vs 32 | reduction | avg one-way distance | avg round-trip route |
|---:|---:|---:|---:|---:|
| 1 | 31 | **96.875%** | 5.50 mm | **41.14 fJ** |
| 2 | 30 | **93.75%** | 3.94 mm | **29.45 fJ** |
| 4 | 28 | **87.5%** | 2.38 mm | **17.77 fJ** |
| 8 | 24 | **75.0%** | 1.75 mm | **13.09 fJ** |
| 16 | 16 | **50.0%** | 0.50 mm | **3.74 fJ** |
| 32 | 0 | 0% | 0 | 0 |

## What happened
The route penalty for sharing exact hardware is only tens of femtojoules per exact access in this preserved geometry proxy, while copy count falls by 75-97% over the useful shared-core range.

This strongly supports using the hollow interior for a few shared exact/memory Component Bays rather than filling every cell/octet with duplicated computer-like control.

## Problem still open
One central core may be geometrically cheap but become a throughput bottleneck during bursts of ambiguous work. Geometry alone cannot choose the core count.

## Decision
- KEEP shared interior Exact Service Cores.
- REJECT one exact/microcontroller-like core per cell as the default.
- Do not force one global core either; size the pool from measured ambiguity/throughput.
- Keep exact fallback logically available even when physically shared.

## Next
v13N1 measures the energy break-even between local-first physical intelligence and exact-every-episode execution without assuming an exact-compute energy.

## Reproduce
`python3 experiments/v13N0_exact_core_pool/source/run_v13n0.py`

Evidence class: deterministic geometry/energy proxy using preserved GVS route constants. No PDK/PEX/manufacturing-cost claim.
