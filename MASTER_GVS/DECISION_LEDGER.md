# Decision Ledger

## Strongly keep
- hybrid analog/event + exact computer architecture
- capacitive stable synapses and templates
- static selector configuration, not per-event template-ID SRAM reads
- Grammar Cells **only where motif recognition also removes larger recognition/routing/downstream work**
- local ambiguity detection + exact escalation
- upstream source gating
- passive/full-swing Myelin for repeated local paths
- physical lease / demand-driven rebuild
- exact shadow-teacher fallback for invalid/cold/new structure
- pre-placed programmable physical slots rather than imaginary post-fabrication new capacitors
- self-locking route capture before analog cleanup
- automatic recovery after decision
- orthogonal long event routing (M4/M5 direction)
- locality-aware representation compiler
- regional sharing of large support resources when proven safe
- **Regional Event Lease**: one long coordinate may remain locally useful for a validated burst instead of recharging the long fabric every local event
- selected physical local group: **8 nearby isolated event paths per Regional Lease** until workload/layout data justifies another size
- use unavoidable physical capacitance as useful state when extraction proves it is stable enough; do not automatically fight every parasitic
- validate physical topology by extraction, not DRC alone
- for Grammar confidence, compare capacitor **ratios** made from the same MIM family rather than using an absolute 0.5 V threshold
- selected safe Grammar readout baseline: short regenerative latch with **two-phase polarity swap/self-check**; same-side preference or weak resolution becomes fallback

## Regional Event Lease correctness invariants
- only a **validated local success/winner** may refresh the lease
- raw sensory/event activity, noise, partial coordinates and unselected regions must never refresh it
- DONE/CLEAN may hard-clear the lease
- exact fallback must remain independent of lease state
- do not make solved v12S run/capture/dendrite correctness depend on the regional lease

## Grammar/readout invariants from v13A5
- do not directly trust an absolute Grammar voltage threshold across real MIM corners
- candidate/reference total capacitance should be physically symmetric before attaching a comparator; unequal total capacitance can move the decision boundary when reader gate capacitance is added
- tiny analog evidence must not silently become a digital/full-swing answer when comparator offset dominates; ambiguity must escalate
- robust readout energy must be included in compiler decisions, not only sub-fJ MIM coupling energy
- a Grammar Cell is not preferred over a warm static selector solely on local event energy; it must save larger downstream or communication work

## Keep selectively / mode-dependent
- visual Grammar first-look, not universal vision
- 2-bin sound temporal pooling as low-power mode when accuracy trade is acceptable
- physical relation edges for stable/reused reasoning, with exact fallback
- dynamic shared selector banks only for severe area constraints
- extra intentional receiver membrane capacitor only if a real glitch problem later requires it
- old regional PVT/leak adaptation if a future measured PVT/leak problem reappears in the current small-dendrite architecture
- v11U-style slow calibration/offset memory for the shared Grammar comparator **only if** it proves zero wrong accepts and materially reduces average two-phase readout energy

## Rejected / not default
- analog exact ALU
- brain-only long reasoning with no fallback
- Grammar Cells everywhere
- global broadcast of every low-level event
- per-event SRAM template-ID lookup
- one-hot template configuration
- naive binary-decoder selector
- unisolated shared sensory source lines
- fixed weak-leak bias across PVT
- nonlinear HVT-varactor recovery bank for selected implementation
- DRC-only acceptance of compact layouts without checking extracted connectivity
- letting raw/noisy local events refresh a Regional Event Lease
- old fixed **0.500 V Grammar threshold** as a physical signoff rule
- unsupported/aggressive 1x1 MIM as the selected fractional Grammar reference
- unequal-total Grammar candidate/reference networks that become reader-load sensitive
- long-lived v12S-sized soma race as Grammar readout: electrically correctable but pJ-class waste
- over-shrunk regenerative latch/input pair that produced wrong accepted decisions at ~11 mV evidence
- adding charge-recovery hardware to the ~50 fJ Grammar readout before proving recovery saves more than its own devices/wiring

## Open, worth testing
- full physical layout/PEX of the v13A5 **5-MIM candidate + 5-MIM shared reference + real swap/self-check latch**
- pack one shared Grammar reference/readout beside the selected eight-way Regional Lease and measure real area/coupling
- v11U-inspired slow comparator offset calibration, after the safe two-phase baseline is physically validated
- local template/Myelin evidence behind the eight-way lease after Grammar readout layout
- physical 4x4 / 16x16 grid loaded with the final selected coordinate-release/lease interfaces
- full physical tile layout/extraction beyond slices
- stacked MIM recovery storage if real DRC/PEX proves legal and worthwhile
- inter-island hierarchy above one 16x16 physical island
- compiler using real measured area + wire + fallback + driver + robust-readout cost instead of proxies
- full multimodal system test with image, sound, code and reasoning using the same physical-cost-aware promotion/demotion policy
- compatible simulator/model route for re-running the historical v12S continuous-model signoff without modifying v12S
