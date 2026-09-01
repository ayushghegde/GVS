# Neural Glyph v14P — Electrostatic Trail Selection Fabric

**Status:** model-level path-selection and reversible-learning candidate. No fabricated v14P trapped-charge branch tip exists yet.

## Central idea

Long-term route preference is stored as local electrostatic field at the mouth/tip of a sparse candidate branch, not as persistent voltage in the semantic cell and not necessarily as a stable conducting filament in the link.

A confirmed route accumulates a trapped-charge/polarization bias that lowers its effective branch barrier. A contradicted route is neutralized or oppositely biased so its barrier rises again.

## Primitive — Electrostatic Trail Tip (ETT)

An ETT is a small trap-rich or polarizable dielectric pocket placed beside the field-focus tip of a v14O-style guided-gap branch.

- positive/forward trail state: lowers local switching barrier and makes the branch easier to activate;
- neutral state: baseline branch;
- reverse trail state: raises the local barrier and suppresses the branch.

The trapped state is persistent; ordinary semantic-cell excitation is temporary.

The first implementation target uses the same two-terminal branch pulse for read/reasoning and larger differential coincidence pulses for trail programming. A third terminal is not part of the preferred design.

## Learning rule

REJECT: every use strengthens the path.

KEEP:
1. activity creates eligibility only;
2. confirmation/self-test deposits the favorable trail on the active/correct branch;
3. contradiction removes or reverses trail on the active wrong branch;
4. later evidence can reverse the state again.

This preserves v14K provisional learning and teacher-free self-test.

## Model result

A 6-way relation-learning model compared:
- ungated use-only deposition;
- confirm-only strengthening with no active erasure;
- reversible confirmation/contradiction trail.

After changing 25% of relations:
- use-only remained near chance and did not relearn;
- confirm-only retained too much attraction to the old route;
- reversible trails reached full relearning in the selected deterministic screen and old-route selection fell to zero.

## Branch-tip screen

Selected five-branch screen:
- read pulse proxy: 0.22 V;
- baseline branch threshold proxy: 0.25 V;
- favorable trail: +5 effective charge units;
- contradicted branch: -1 effective unit;
- branch-threshold sigma: 16 mV;
- trap/coupling variation: 25%;
- electrostatic cross-coupling: 15%.

120,000-trial result:
- correct branch wins ~98.06%;
- target above threshold ~89.68%;
- any wrong branch above threshold ~2.78%;
- target-only clean firing ~87.17%.

Wide fanout remains weaker: the hardest 16-way / 20-mV-sigma stress point fell to ~89.5% winner accuracy. v14P therefore keeps sparse branch fanout rather than dense local branching.

## Electrostatic sanity boundary

A point-charge calculation in a high-k dielectric gives order-10-mV potential shifts for an elementary charge a few nanometres away. This only establishes scale; real screening, trap distribution, electrodes, geometry, and tunnelling must replace the point-charge approximation before physical promotion.

## Relationship to v14O

v14O still provides:
- guided short dynamic gap;
- field-focus inert tip;
- passive current ballast;
- sparse physical regeneration.

v14P changes the learned route memory:
- instead of requiring the branch filament itself to hold the whole long-term weight,
- a nearby electrostatic trail biases which volatile branch is easiest to fire.

This deliberately decouples fast firing physics from long-term route memory.

## Keep / reject

KEEP:
- sparse candidate branches;
- transient electrical activity in cells;
- persistent knowledge in local connection state;
- reversible electrostatic trail;
- positive confirmation and negative/neutralizing contradiction;
- v14O guided-gap firing and sparse regeneration.

REJECT:
- ungated 'more traffic = more permanent attraction';
- free charge sitting indefinitely on bare metal;
- dense all-to-all branch tips;
- claiming trapped-charge retention/programming energy before physical testing.
