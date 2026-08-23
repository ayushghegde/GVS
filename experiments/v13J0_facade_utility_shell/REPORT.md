# Neural Glyph v13J0 — Facade Utility Shell / All-Surface Utilization

**Verdict: KEEP selectively. Use outside/backside/sidewall surfaces for robust shared utilities, distributed recovery/decoupling banks, thermal plumbing, optional optical source/endpoints and fault bypass. Do not duplicate the entire local nervous/data network on the exterior. Weak analog computation remains on protected inner/framework surfaces.**

## New terms
- **Facade Utility Shell (FUS):** protected robust service wiring and support devices placed on the outer/top/back/side surfaces of the hollow framework, analogous to pipes/tanks/balconies on a building.
- **Roof Reservoir Array (RRA):** distributed recovery/decoupling capacitor bank on top/backside/exterior surfaces; local live reservoirs drain to it only after their information has expired.
- **Facade Bypass Ring:** sparse outside robust wiring retained mainly for power/configuration/recovery and as a fault bypass, not as a second copy of every local data link.
- **Service Pod:** an outside/backside support block such as decoupling/recovery capacitance, regulator, ESD/test, optical source bank or thermal interface. Local per-event analog computation is not a default Service Pod.

## 1. Building interpretation
The hollow-framework chip now uses three classes of physical space:
1. **rooms / inner surfaces:** local Glyph computation, Tri-Wall evidence, Grammar/template/Myelin, fourth faces, weak analog state;
2. **walls / ribs:** shielded service lanes, local electrical event spines, power/reference/recovery connections;
3. **facade / roof / outside:** robust shared utilities, distributed reservoir banks, large support devices, thermal exhaust/manifold, optional photonic endpoints and emergency bypass routes.

The design goal is not to fill every surface. The goal is to place each function where its communication, noise, thermal and manufacturing cost is lowest.

## 2. Thin-package geometry screen
Model only: 10 mm x 10 mm x 2 mm slab, 4 x 4 x 2 = 32 regions. This is an illustrative geometry, not a proposed physical GVS dimension.

- total exterior surface = 280 mm^2;
- sidewall-only surface = 80 mm^2;
- region center to a single internal central collector: average Manhattan distance ~5.5 mm, total 176 mm if every region had its own dedicated drain;
- each of the two region layers sits only ~0.5 mm from its nearest top/bottom exterior face, total local drop length 16 mm.

This gives a **~90.9% reduction in the local last-mile drain length** versus a naive single central collector (176 mm -> 16 mm) when the recovery/decoupling bank is distributed across the exterior. This is not a claim versus an optimally distributed internal rail; it shows why an exterior distributed bank is attractive on a thin package.

## 3. Does outside wiring shorten ordinary data routes?
No, not automatically.

A 32-region 4x4x2 internal grid was compared with the same grid plus a perimeter facade ring, surface drops and four corner risers.

Weighted cell-to-cell shortest-path distance:
- internal-only average ~6.968 mm;
- internal + perimeter facade average ~6.968 mm;
- p95 and worst path were also unchanged in this simple geometry.

Therefore exterior wiring is **not selected as the normal local data path merely to use the outside surface**.

## 4. Fault-bypass result
The facade ring adds an independent physical route class. In 1000 random-edge-failure trials:

At 40% random edge removal:
- internal-only mean largest connected cell fraction ~94.5%, 5th-percentile ~84.4%;
- internal + perimeter facade mean ~97.7%, 5th-percentile ~93.8%.

At 30% failure:
- internal-only mean ~98.6%;
- with facade ~99.5%.

This is a graph-resilience model, not a manufacturing-yield prediction. It justifies the outside network as a **robust service/fallback domain**.

## 5. Cost of duplicating everything
The model edge count rises:
- internal grid: 64 edges;
- internal + sparse perimeter facade: 116 edges (~81% more);
- a full top+bottom exterior mesh would be still larger.

Because normal route length did not improve, a full duplicated exterior nervous network is rejected. The selected facade is sparse and utility-oriented.

## 6. What belongs outside
### Good outside/backside candidates
- VDD/GND/reference distribution;
- distributed recovery/decoupling capacitors (Roof Reservoir Array);
- slow configuration/promotion/test/repair;
- ESD/I/O support;
- large chip-level recovery converter/bank;
- thermal exhaust/condenser interface;
- optional regional optical source bank / photonic coupling layer;
- spare robust bypass links.

### Keep inside/on protected framework
- GC/GR Grammar evidence;
- dendrite/membrane/latch internal nodes;
- live lease/use/familiarity charge;
- local competition/inhibition;
- per-event short fourth-face and event-spine links;
- local exact logic/memory when moving it outside would add more communication than it saves.

## 7. External feasibility reference
Backside-power research already supports the physical principle of separating utilities from signal routing. Imec reports that backside power delivery can reduce frontside routing congestion and that backside connectivity can also host I/O/ESD functions and dense MIM decoupling capacitance. This does not prove the literal GVS hollow facade, but it strongly supports using otherwise free outer surfaces for robust utility functions rather than forcing everything through the same signal metal stack.

## 8. Decision
### KEEP
- facade/backside robust utilities;
- distributed exterior recovery/decoupling bank;
- sparse exterior bypass ring;
- outside support pods when shared/large/hot/slow;
- compiler choice of inside versus outside placement.

### REJECT as default
- moving weak analog state to long outside routes;
- duplicating every data link on the facade;
- adding outside components only to maximize surface utilization.

## 9. Architectural rule
`weak/local/frequent -> inside/protected framework`

`robust/shared/slow/large/hot/support -> wall/facade/outside if total cost wins`

`faulted internal utility -> facade bypass when available`
