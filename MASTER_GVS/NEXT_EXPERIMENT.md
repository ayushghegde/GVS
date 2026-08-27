# Current Next Experiment — v13U4 Consolidation Interface Closure

## Goal
Close the smallest persistent-memory interface that can help adaptive tissue without putting slow/high-voltage NVM into every cell.

## Required path
`fast MIM/MOS state -> familiarity/stability -> deep promotion -> shared NVM interface -> persistent prior -> power-up seed -> live RPF allowed to override`.

## Battery
1. reproduce v13U endurance/staleness frontier;
2. load SKY130 SONOS programmed/erased BOL/EOL model corners with a compatible simulator if available;
3. verify low-voltage read separation and read disturbance;
4. model/measure shared high-voltage programming infrastructure and amortization;
5. program/erase latency must stay off the critical reasoning path;
6. power-cut restart: compare random boot, SONOS prior, and live re-adaptation;
7. stale persistent prior may delay adaptation but must never force a wrong robust result;
8. test sparse relation/morphology consolidation, not per-event context;
9. compare lifetime writes against 100k guaranteed cycles;
10. keep MRAM as a future parameter envelope only unless a real process model is available.

## Acceptance
Keep persistent quantum-effect memory only if total lifetime cost improves after high-voltage/process/area/endurance costs. Otherwise keep purely volatile MIM/MOS tissue and external/ordinary persistent configuration.
