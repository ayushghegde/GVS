# v14V Architecture — Self-Addressed Polarity Fabric

## One-line architecture
A Glyph branch that wins inference temporarily marks itself, allowing one global confirmation/contradiction pulse to update that branch's HZO polarity without row/column addressing.

## Core structure

```text
                         REGIONAL PULSE LAUNCHER
                              (shared gain)
                                  |
                    +-------------+-------------+
                    |      one TEACH mesh       |
                    +-------------+-------------+
                                  |
          ---------------------------------------------------
          |                 |                 |             |
       Glyph cell        Glyph cell        Glyph cell     ...
          |
       CHOICE
      / / | \ \
   branch branch ... spare
      |
      +-- guided volatile gap      <- inference event
      +-- passive ballast
      +-- FIC/HZO polarity collar  <- durable route memory
      +-- ETG passive inhibit      <- short-lived self-address tag
```

## State separation

- **Durable state:** HZO electric polarization; stores learned route preference.
- **Fast event state:** guided volatile bridge; performs inference/competition.
- **Eligibility state:** ETG volatile conductance; says only “this branch was recently used.”
- **Energy state:** hollow regional charge reservoir; stores/recycles program-line charge, not semantics.

Keeping these jobs separate is deliberate. No one material is forced to be nanosecond firing event, long-retention memory, and regional power source simultaneously.

## Inference
1. Incoming activity excites the shared Choice node.
2. HZO polarity changes local guided-gap barrier/firing preference.
3. One branch bridges first.
4. Winner collapses the Choice node and quenches competitors.
5. The winner event also sets its ETG temporary tag.
6. The volatile conductive bridge relaxes.

No learning address and no MOS are used in this path.

## Learning
1. A recent winner has an active ETG tag.
2. Confirmation/contradiction is corroborated if needed.
3. The regional launcher sends one polarity-coded TEACH pulse over a single mesh.
4. Tagged ETG passes enough pulse to its FIC/HZO collar.
5. Untagged or stale ETGs block the pulse.
6. HZO polarity changes durably; ETG relaxes and disappears.

The teaching mesh carries **what happened** (confirm/contradict). The physical tag carries **where it happened**.

## Why this is simpler than v14U
v14U still needed a regional address decoder and independently controlled program rails. v14V removes normal explicit learning addresses. The only repeated per-branch elements are already useful physical branch elements; ETG reuses the passive program-inhibit layer instead of adding a standalone selector.

## Retained GVS ideas
- electric polarity learning
- guided-gap competition
- field-isolated HZO/Ag chemistry
- hollow dry charge reservoir
- charge recovery
- spare/repair branches
- usage eligibility, but only as volatile nonsemantic state
- confirmation/contradiction and corroboration
- regional active gain only

## Hard failure rule
If ETG requires a per-branch transistor, or if fresh and stale tags cannot be separated well enough, v14V self-addressing is rejected and v14U remains the fallback. No MOS rescue inside semantic cells.
