# v14H3 — Local Binary Connection Plasticity

## Goal
Test whether new knowledge can be learned by changing only connection strengths while ordinary semantic cells keep no persistent voltage memory.

## Model
- 1,000 source populations and 500 target populations;
- each source initially has one strong correct link plus three weak distractor links;
- weights are binary weak/strong;
- 10 learning rounds change 5% of source relations per round;
- learning a changed relation performs only two local operations per connection copy: weaken old link, strengthen new link;
- read variation sigma = 20%;
- programming failure probability screened at 0%, 1%, 5%, 10%;
- 1, 2, or 3 parallel connection copies screened.

This is an abstract connection model, not a physical memcapacitor/memristor measurement.

## Controls
A fixed-geometry connection plane cannot adapt. When 20% of relations change, overall accuracy becomes 80% and accuracy on changed relations is 0%.

## Plastic results after ten rounds
With no programming faults, one, two, and three-copy fabrics all end at 100% current-relation accuracy.

At 1% per-write failure:
- 1 copy: 99.6%;
- 2 copies: 100%;
- 3 copies: 100%.

At 5% per-write failure:
- 1 copy: 98.2%;
- 2 copies: 99.7%;
- 3 copies: 99.9%.

At 10% per-write failure:
- 1 copy: 94.3%;
- 2 copies: 98.4%;
- 3 copies: 99.2%.

Never-changed relation retention stays essentially 100% in the selected runs because updates touch only the local old/new connection pair.

## Cost proxy
Programming events per changed relation:
- 1 copy: 2;
- 2 copies: 4;
- 3 copies: 6.

This is a write-count proxy only. It is not energy or area until a physical link device is selected.

## Architectural consequence
On-chip learning does not require persistent semantic charge at a node in this model. The stored fact is the link configuration itself.

The preferred hierarchy is therefore:

1. mostly fixed weak/strong passive links for consolidated knowledge;
2. a small plastic two-terminal link population where new learning is valuable;
3. two or three connection copies only where reliability requires it;
4. ordinary semantic nodes remain ephemeral excitation sites.

## Remaining hardware problem
A connection device must now demonstrate that weak/strong programming is cheaper than transistor/SRAM weight storage after write selectors, process steps, yield, endurance, retention and programming energy are included.

A fixed MIM plane remains the inference-only cost floor. Trainable ferroelectric memcapacitors or other two-terminal devices remain candidates, not accepted hardware.
