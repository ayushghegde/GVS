# v15FG Architecture

## FSS — Fragment Scratch Screen
A shared optical scratch surface. It carries only the intermediate fragment needed to continue reasoning; it is not a destination-routing display.

- each dot has a fixed electrical emitter domain (modeled at 5 V)
- fragment value is encoded by dot pattern / pulse timing, not by making device voltage equal the number
- screen remains visible for >=1 us
- all participating chips can observe the same surface
- common chip power distribution is separate from content transport

Example: the intermediate value 10 may be represented as a fixed-voltage spatial code rather than a literal 10 V node.

## Same-AI Dialogue Mode
Optional high-compute mode:
1. give the same prompt to two instances of the same AI/model family
2. each produces an independent candidate
3. if they agree strongly, stop
4. if they disagree, exchange compact claims/checks
5. reconcile to one answer

This is an inference policy, not a new neuron device.

## Local semantic fabric
Unchanged from accepted v15D:
- guided volatile gap for event firing
- dendritic positive/negative free charge for short-lived preference
- natural leakage for forgetting
- HZO polarization for slow consolidated preference
- four active routes + two repair branches
- zero MOS in ordinary semantic cells

No FITA tunnel. No SEEP delayed tag. No extra learning capacitor.

## Functional global modulation
Optional low-dimensional global bias charge can alter gain/thresholds for functions analogous to caution, urgency, and curiosity. This is not a claim of emotion or consciousness.

## Maker revision request
Persistent physical fault evidence can create a hardware-doubt signal that asks the maker to revise the next chip. Unknown knowledge does not trigger this path.
