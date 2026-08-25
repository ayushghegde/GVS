# Neural Glyph v13M2 — Two-Octet Locality and Cross-Surface Routing

**Verdict: MODEL PASS.** The eight-cell intelligent region remains economically useful even when a large fraction of episodes cross into a second octet. The dominant saving is still long-selection reuse. Cross-octet carrier choice matters, but it is a second-order term until routing dominates the workload.

## Why this experiment
v13M0 showed that one mixed eight-cell region can avoid repeated long selections. v13M1 showed that forcing opposite-surface communication around the shell can create a 5x path-length penalty.

v13M2 asks whether the local-region advantage survives once work must leave one octet and enter another.

## Model
One base episode performs eight primitive operations in octet A. With probability/fraction `p_cross`, it hands off once to octet B, which performs four additional primitive operations.

Compare:
- **independent selection baseline:** every primitive operation pays the preserved 680 fJ long-selection proxy;
- **v13M:** each octet entered pays one 680 fJ long selection plus one 106.8 fJ lease, then does its local work.

Preserved octet local-core proxy: 537.3144 fJ for the eight-role v13M0 mix. The remote half-octet uses half that core cost only as a deterministic composition proxy.

Cross-route variants:
- near regional spine: 0.67 fJ;
- short 2 mm opposite-surface electrical chord: ~7.63 fJ;
- rejected 10 mm surface detour: ~37.55 fJ;
- 10 mm optical route amortized over 64 uses: ~26.581 fJ.

No new circuit/PEX result is claimed.

## Locality result
Using the short 2 mm chord when a cross-octet handoff is needed:

| cross-octet fraction | independent baseline | v13M | saving | long selections baseline -> v13M |
|---:|---:|---:|---:|---:|
| 0% | 5.977 pJ | 1.324 pJ | **77.85%** | 8.0 -> 1.0 |
| 10% | 6.277 pJ | 1.430 pJ | **77.21%** | 8.4 -> 1.1 |
| 25% | 6.726 pJ | 1.590 pJ | **76.36%** | 9.0 -> 1.25 |
| 50% | 7.475 pJ | 1.856 pJ | **75.18%** | 10.0 -> 1.5 |
| 75% | 8.225 pJ | 2.121 pJ | **74.21%** | 11.0 -> 1.75 |
| 100% | 8.974 pJ | 2.387 pJ | **73.40%** | 12.0 -> 2.0 |

Even when every episode crosses to the second octet, the selection+local-core proxy remains about 73% lower than independently selecting every primitive.

This means v13M does **not** require perfect locality. Locality improves the result, but the regional lease structure remains useful under substantial cross-region traffic.

## Cross-surface route result
At 100% cross-octet traffic:
- forced 10 mm surface detour: ~2.417 pJ/episode;
- short 2 mm protected electrical chord: ~2.387 pJ/episode;
- difference: ~29.92 fJ, ~1.24% of total episode energy.

The percentage looks small because long selection/core energy dominates this current proxy. But the route penalty compounds when:
- many cross events occur per episode;
- the local cores become cheaper;
- long selection cost is further reduced;
- route distance grows.

Therefore the v13M1 route rule remains important even though it is not yet the dominant total-energy term.

## Optical interpretation
A 10 mm optical route at 64 uses (~26.581 fJ/use including route-write amortization) is cheaper than a 10 mm electrical route (~37.55 fJ/use), but **it is still much more expensive than a physically available 2 mm electrical chord (~7.63 fJ/use).**

So the carrier compiler must compare against the *best actual electrical geometry*, not against an artificially long surface-only electrical path.

**Decision:** do not promote optics simply because two cells are on different hollow surfaces. First check whether a short protected electrical bridge exists.

## Intelligence consequence
The octet is now a useful unit of local intelligence rather than an isolated primitive container:
- one validated selection activates a neighborhood of different physical functions;
- Grammar/template/Myelin/context interactions remain local;
- crossing into another neighborhood costs another lease, not four or eight new long selections;
- exact fallback remains available at the boundary;
- Nerve/Artery/Thermal anatomy remains separate from the meaning graph.

## What happened / problem / next
### What happened
The two-octet model retained a 73-78% selection+local-core advantage over the tested locality range.

### Problem found
Carrier comparisons can be misleading if the electrical baseline is artificially forced around the hollow shell. A short interior chord beats the otherwise attractive 10 mm optical route.

### Next
Move from model composition to the first **two-octet physical/system slice**:
1. one physically closed/recovered Grammar cell inside each octet;
2. one template and one short Myelin relation per octet represented with preserved physical/schematic blocks;
3. direct fourth-face/local links inside each octet;
4. shared low-swing Nerve between octets;
5. shared Charge-Artery branch physically separated from weak evidence;
6. one short protected opposite-surface electrical chord;
7. replay local-only, 25%, 50% and 100% cross-octet traffic;
8. measure service coupling, lease stability, robust decisions, cross-event energy and fallbacks;
9. keep optical unpopulated unless the real route length/reuse passes break-even.

## Reproduce
From repository root:
`python3 experiments/v13M2_two_octet_locality/source/run_v13m2.py`

Tool class: deterministic Python 3 model using preserved GVS energy proxies. No PDK/PEX claim is made.
