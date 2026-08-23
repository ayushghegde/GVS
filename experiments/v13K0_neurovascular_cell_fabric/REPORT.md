# Neural Glyph v13K0 — Neurovascular All-Surface Cell Fabric

**Verdict: KEEP as the new structural direction; future-process geometry, not literal SKY130 fabrication.**

## Why v13K
v13J solved service placement but accumulated timing/control rules around the facade. v13K attacks the cause physically: do not let firing, expired-charge collection, heat transport and optional optics fight for one conductor or one switching domain.

## New terms
- **Neurovascular Glyph Cell (NGC):** a Tri-Wall Glyph cell with separate physical service paths for firing, expired-charge recovery and heat removal, plus an optional optical port.
- **Nerve:** the low-swing event path. Directly touching paired cells use the fourth-face contact; non-neighbors use a short subwire/event spine.
- **Charge Artery:** a dedicated low-voltage path that accepts charge only after the local state is no longer information and carries it to a shared regional recovery reservoir.
- **Thermal Capillary:** a passive high-thermal-conductivity path from a cell/support block into a shared Thermal Artery/Exhaust. It is not an electrical signal wire.
- **Light Nerve:** an optional thin optical/lightpipe route for long, repeatedly reused relations that pass the existing optical break-even compiler.
- **Inside-Out Cell Skin:** cells/support devices may occupy outer, inner, underside and side surfaces when fabrication and total communication/thermal cost justify it.
- **Exact Service Core:** a shared digital/controller-like block for boot, exact fallback, repair/configuration and exact state. It is not duplicated in every cell.

## Cell anatomy
The existing three capacitor walls remain the local evidence surfaces. The fourth side becomes the preferred connection/service face.

```text
                 capacitor wall
                      |
        capacitor -- CELL -- capacitor
                      |
             FOURTH CONNECTION FACE
             [ direct NERVE pad ]
             [ charge-artery edge ]
             [ thermal anchor ]
             [ optional optical dock ]
```

Directly paired neighboring cells use the shortest direct electrical connection through the fourth face. The previous measured/model proxies remain the reason:
- direct fourth-face event ~0.15 fJ;
- ~180 um shared event-spine one-tap event ~0.67 fJ;
- four-tap spine ~1.34 fJ total.

Thus direct neighbor is about **77.6% lower event-source work than using the one-tap regional spine** in the current proxies. The shared spine remains useful for fanout and non-neighbors.

## All-surface geometry screen
Illustrative only: 10 x 10 x 2 mm hollow slab, 0.2 mm framework thickness.

- outer surface area: 280 mm^2;
- inner cavity dimensions: 9.6 x 9.6 x 1.6 mm;
- inner surface area: 245.76 mm^2;
- total inner+outer active surface: **525.76 mm^2 = 1.878x the outer surface alone**.

Even after reserving surface for nerves/arteries/thermal/optical/support:
- 20% service reserve -> 420.61 mm^2 usable = **1.50x outer-only area**;
- 30% reserve -> 368.03 mm^2 = **1.31x**;
- 40% reserve -> 315.46 mm^2 = **1.13x**.

This does not mean 1.5x transistor density in a real product. It shows why inner/outer/underside/side surfaces can remain useful after substantial service-area reservation.

## Where larger components go
Do not place a microcontroller in every cell. If controller-like functionality is useful, place one or a few Exact Service Cores / memory / power-management / I/O blocks in Component Bays on inner or outer surfaces according to locality and cooling.

Near-term manufacturable analogues may use chiplets/dies and backside wiring. Literal active cells on every inner cavity wall are a custom/future process. Current backside research already demonstrates double-sided connectivity/backside power and explores active functional backside devices; this supports the direction but does not prove the literal GVS cavity.

## Structural rule replacing many timing rules
Separate the services physically:

```text
weak analog / capacitors -> protected cell surface
0.2 V firing nerve       -> low-swing nerve layer
expired charge           -> low-voltage charge artery
heat                     -> passive thermal capillary
long/hot selected route  -> optical/lightpipe layer
high-swing power/config  -> robust outer/backside service layer
```

The goal is that normal nerve/artery/thermal activity can coexist without needing a central scheduler. Only the fundamental lifecycle rule remains: **do not drain a node while it still carries useful information.**

## Decision
KEEP:
- cells on useful inner+outer+underside+side surfaces where cost wins;
- direct fourth-face connection for paired neighbors;
- separate per-cell Nerve, Charge Artery and Thermal Capillary;
- optional Light Nerve only after break-even;
- shared Exact Service Cores/Component Bays instead of per-cell microcontrollers.

REJECT:
- one combined conductor carrying firing + recovery + power;
- duplicating controllers in every cell;
- filling every surface merely because it exists;
- claiming literal all-surface active-silicon fabrication is already available in SKY130.
