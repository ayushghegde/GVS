# Neural Glyph v13K4 — Inside/Outside Component-Bay Placement Screen

**Verdict: USE BOTH. Frequently accessed exact/memory support tends to belong near the geometric center/interior; large/hot/slow/test-facing support tends to belong on outer/backside surfaces. Do not force every component inside or outside.**

## Why this test
v13K allows cells on inner, outer, underside and side surfaces and also allows larger controller/memory/support blocks in Component Bays. The question is whether outside placement is always better because it is easier to cool/service, or inside placement is always better because it is closer to the cells.

## Geometry
Illustrative 10 x 10 x 2 mm slab with 4 x 4 x 2 = 32 region centers.

Candidate shared Exact Service Core / memory locations:
- center inside: (5,5,1) mm;
- top center: (5,5,2);
- bottom center: (5,5,0);
- side center: (0,5,1);
- top corner: (0,0,2).

This is a placement model, not a fabricated package.

## Route result
Average Manhattan distance from the 32 cells:
- center inside: **5.5 mm**;
- top/bottom center: **6.0 mm**;
- side center: **8.0 mm**;
- top corner: **11.0 mm**.

Using the existing improved dedicated electrical-route proxy ~3.74 fJ/mm only as a communication comparison:
- center inside: ~20.57 fJ average route energy proxy;
- top/bottom center: ~22.44 fJ;
- side center: ~29.92 fJ;
- top corner: ~41.14 fJ.

So a heavily accessed exact/memory block placed centrally inside is about **8.3% lower route proxy than a top-center placement**, ~31% below a side-center placement, and ~50% below a corner placement in this simple geometry.

## Placement rule
### Put inside / central when
- access is frequent from many cells;
- exact memory/controller traffic would otherwise dominate communication;
- the block can be cooled adequately by its Thermal Artery;
- moving it outside does not simplify manufacturing enough to repay the route cost.

### Put outside/backside/side when
- block is large/hot/slow/shared;
- it benefits strongly from direct cooling, package I/O, test or replacement;
- traffic is infrequent or originates mostly from nearby surface cells;
- it is power regulation, large recovery storage, optical source/coupling, ESD/test or thermal equipment.

## Microcontroller interpretation
If GVS needs a microcontroller-like element, treat it as an **Exact Service Core**, not as part of every Glyph cell. It may contain boot/configuration state machines, exact fallback control, repair/test, I/O and small exact compute. Large exact AI arithmetic/memory can be separate blocks/chiplets.

## Important consequence
The user suggestion 'components both inside and outside' is better than choosing one side globally. It becomes another compiler decision:

`frequent communication -> place near the cells`

`large/hot/service-facing -> place near exterior/thermal boundary`

## Next
The next experiment should now be the physical v13K5 Neurovascular Cell Slice. The architecture questions have been reduced enough: physically co-lay out one weak evidence node, one 0.2 V Nerve and one low-voltage Charge Artery and measure their actual extracted coupling under TT/FF/SS/mismatch.
