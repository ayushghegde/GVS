# Neural Glyph v13J3 — Facade Quiet Window + Regional Reservoir Integration

**Verdict: PARTIAL PASS.** The Facade Utility Shell remains useful, but robust exterior utilities must obey a quiet-window rule around weak analog decisions. The strongest recovery hierarchy is no longer `tiny reservoir -> chip converter`; it is `local state -> proven regional shared reservoir -> batched facade/chip collector`. The older v13P12 10 pF / 4-tile shared reservoir materially improves the recovery scaling argument.

## New terms
- **Facade Quiet Window (FQW):** during a weak high-impedance analog decision, large facade/recovery/configuration transitions are frozen or staggered; after capture, utility activity may resume.
- **Regional Recovery Landing (RRL):** a facade/backside landing bank placed near a small group of cells/tiles, so short branches feed a regional reservoir before any chip-level conversion.
- **Recovery Capillary:** short isolated branch from a local expired state to the nearest regional recovery landing; it is closed only after the local state has expired.

## 1. Old experiment rescue changes the recovery hierarchy
v13J1 initially used the v13E tap-gate recovery result as its scale reference: ~2.85 fJ removed and ~1.51 fJ reaching a local low-voltage rail per expired state.

The older v13P12 result is stronger for the next level:
- one **10 pF shared recovery reservoir across four tiles**;
- nominal TT/FF/SS pass;
- 12/12 mismatch launches, 48 tile instances pass;
- weakest post-error second-request minimum remained above the 0.9 V request boundary;
- about **220 fJ** capacitor-energy increase in one four-tile recovery interval;
- shared capacitance target reduced 40 pF -> 10 pF versus one 10 pF reservoir per tile.

Therefore v13J should not attach a chip-level converter to every tiny state. The selected hierarchy is:

`live local state -> local function -> expiry -> regional 10 pF-class shared reservoir -> batch threshold -> facade/chip collector`.

The 10 pF value is still a lumped physical candidate from v13P12, not a closed extracted exterior implementation.

## 2. Exterior placement loading screen
Use the v13C shielded service-line capacitance proxy ~6.231 fF / 100 um only as a first-order branch-load estimate.

For a thin-package region ~0.5 mm from its nearest exterior face:
- one 0.5 mm recovery branch -> ~31.2 fF;
- four such branches -> ~124.6 fF total;
- versus a 10 pF regional reservoir, branch capacitance is only **~1.25%** of the reservoir target.

Using the v13P12 TT recovery rise 0.1990 V -> 0.2893 V as a charge proxy, adding ~124.6 fF parallel branch capacitance would reduce the idealized final rise only to roughly ~0.288 V class. This is small enough to justify a physical PEX test; it is **not** a new PVT signoff.

## 3. Facade Quiet Window crosstalk screen
Weak local evidence reference:
- protected evidence node ~72 fF;
- useful differential ~25 mV;
- current high-margin screen ~18 mV.

Use the existing ~0.124 fF protected-branch coupling as a deliberately conservative facade-to-weak-node proxy.

One utility transition produces approximately:
- 0.9 V step -> **1.55 mV** kick;
- 1.2 V -> **2.06 mV**;
- 1.8 V -> **3.09 mV**.

A single transition does not erase the current margin.

But simultaneous aligned switching accumulates:
- at 0.9 V: 4 lines leave ~18.81 mV; 5 fall below 18 mV;
- at 1.2 V: 3 lines leave ~18.81 mV; 4 fail the high-margin screen;
- at 1.8 V: 2 lines leave ~18.81 mV; 3 fail.

Therefore shielding alone is not permission for unlimited facade activity.

### Selected timing rule
1. configure slow facade utilities before weak analog accumulation when possible;
2. freeze high-swing facade transitions during Grammar/dendrite/latch-sensitive windows;
3. capture the local winner/result;
4. open Recovery Valves and perform facade/recovery transfers afterward;
5. if a robust emergency service must switch during the analog window, exact/fallback confidence handles the disturbed case rather than silently accepting it.

This extends the old rule `capture before cleanup/recovery` to all exterior utilities.

## 4. Regional -> chip-level batching screen
Use the v13P12 ~220 fJ stored regional packet only as a scaling input. Assume a hypothetical second-stage transfer efficiency of 90%; fixed transfer overhead is varied.

### 100 fJ fixed chip-transfer overhead
- 1 regional packet -> ~98 fJ net at chip level (~44.5% of the regional stored energy);
- 2 packets -> ~296 fJ (~67.3%);
- 4 packets -> ~692 fJ (~78.6%);
- 8 packets -> ~1484 fJ (~84.3%).

### 200 fJ overhead
- 1 packet -> no positive net;
- 2 packets -> ~196 fJ (~44.5%);
- 4 packets -> ~592 fJ (~67.3%);
- 8 packets -> ~1384 fJ (~78.6%).

The important result is not the exact 90% number—it is hypothetical. The result is that **regional pooling makes the second-stage converter operate on hundreds of femtojoules rather than one-femtojoule packets**, so fixed activation cost becomes much easier to amortize.

No energy is created; each stage can only retain a fraction of charge/energy that would otherwise be dissipated.

## 5. Facade routing screen refined
The previous 10 x 10 x 2 mm, 32-region illustrative slab gave:
- 176 mm total if every region had a dedicated Manhattan route to one central internal collector;
- 16 mm total vertical distance to the nearest top/bottom exterior surfaces.

A new distributed facade model uses four quadrant banks on each of the top and bottom surfaces. For the same 4x4x2 region placement:
- vertical drops total ~16 mm;
- surface routing to the nearest quadrant bank totals ~80 mm;
- combined ~96 mm;
- **~45.5% less route length** than the deliberately naive 176 mm one-central-collector layout.

This is a more conservative result than v13J0's 90.9% `last-mile only` number because it includes surface routing after reaching the facade. An optimized internal distributed collector could be competitive; the facade is selected for congestion/isolation/serviceability in addition to length.

## 6. Why the facade still earns its place
Even when dynamic-energy recovery is small relative to the whole intelligent workload, the facade can:
- separate power/recovery/test from weak analog routing;
- host large shared decoupling/recovery banks;
- provide an independent robust bypass network;
- move large/hot support devices away from local analog surfaces;
- give optional photonic source/coupling hardware an external attachment plane;
- give thermal exhaust a natural package boundary.

This direction is consistent with real backside-power research: backside power delivery is used specifically to decouple power from signal routing, reduce BEOL congestion, and can extend the otherwise free backside to I/O/ESD and dense MIM decoupling functions. It does not prove the literal GVS facade geometry.

## 7. What failed / was rejected
- **REJECT** `all exterior utilities may switch whenever they want because they are shielded`.
- **REJECT** one chip-level converter per tiny local reservoir.
- **REJECT** direct chip collector connection while a reservoir still carries lease/context/familiarity information.
- **REJECT** claiming exterior placement automatically shortens every route.

## 8. Selected architecture after v13J3

```text
weak local cell / Grammar / context
        |
        | live state isolated from recovery
        v
local / regional work
        |
    result captured
        |
        v
Recovery Capillary opens
        |
        v
4-tile-class Regional Recovery Landing (~10 pF candidate)
        |
        | accumulate / batch
        v
Facade / Roof Reservoir Array
        |
        v
chip/package recovery converter or low-voltage support
```

Facade utilities obey a quiet window around weak analog decisions.

## 9. Next physical test
Build one **same-die electrical proxy** before trying literal sidewall/backside fabrication:
1. weak 72 fF-class evidence node / real Grammar-side node;
2. shielded facade-equivalent service line;
3. one recovery branch and one regional reservoir branch;
4. switch facade service at 0.9/1.2/1.8 V both during and after the analog decision;
5. verify that post-capture recovery does not change accepted result;
6. sweep simultaneous utility activity until fallback/high-margin boundary is observed;
7. TT/FF/SS + independent mismatch;
8. only after this passes, map the protected service line to a backside/facade package process.
