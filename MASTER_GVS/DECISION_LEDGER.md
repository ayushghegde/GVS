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
- **margin-tiered readout**: spend one comparison on a physically characterized high-margin representation; spend two-phase self-check or exact fallback only when the margin is low/unknown
- **same-die vertical GVS placement**: place MIM evidence/storage above transistor logic in the BEOL when DRC/PEX proves it safe; v13A7 demonstrated one legal 2x2 um MIM directly above a real NFET with only ~0.059 fF worst plate-to-transistor parasitic in that test
- reserve long/vertical interfaces for **robust meaning** (winner/event/config/result), not tiny high-impedance analog evidence

## Regional Event Lease correctness invariants
- only a **validated local success/winner** may refresh the lease
- raw sensory/event activity, noise, partial coordinates and unselected regions must never refresh it
- DONE/CLEAN may hard-clear the lease
- exact fallback must remain independent of lease state
- do not make solved v12S run/capture/dendrite correctness depend on the regional lease

## Grammar/readout invariants from v13A5/v13A6
- do not directly trust an absolute Grammar voltage threshold across real MIM corners
- candidate/reference total capacitance should be physically symmetric before attaching a comparator; unequal total capacitance can move the decision boundary when reader gate capacitance is added
- tiny analog evidence must not silently become a digital/full-swing answer when comparator offset dominates; ambiguity must escalate
- robust readout energy must be included in compiler decisions, not only sub-fJ MIM coupling energy
- a Grammar Cell is not preferred over a warm static selector solely on local event energy; it must save larger downstream or communication work
- the old two-phase polarity-swap reader remains the **safe low-margin mode**, not the normal high-margin 3-step sound-Grammar path
- current empirical boundary: single-phase produced no errors in the tested >=18 mV stress classes and in the ~25-30 mV final Grammar class, but errors appeared at the artificial ~11 mV stress class
- do not generalize that boundary into a fabrication-yield guarantee; physical PEX and larger mismatch sampling are still required

## 3D architecture invariants from v13A7
- first exploit **vertical structure already available inside one CMOS die** before paying for die stacking
- MIM capacitors may overlap transistor XY area when DRC/PEX confirms no unwanted connection/coupling
- keep weak Grammar/dendrite/candidate/reference/latch-internal analog state within one physical tier
- hybrid-bond interfaces, if later used, should carry full-swing events, region coordinates, slow static configuration, or exact-compute requests/results
- true hybrid-bond 3D is a **future cost/performance option**, not required for the SKY130 prototype
- monolithic/CFET stacked active devices are research/future options, not current baseline requirements
- do not stack hot exact-compute logic underneath sensitive analog/event tiers without thermal analysis
- backside power delivery is a future advanced-node option; it is not available in the current SKY130 baseline

## Keep selectively / mode-dependent
- visual Grammar first-look, not universal vision
- 2-bin sound temporal pooling as low-power mode when accuracy trade is acceptable
- physical relation edges for stable/reused reasoning, with exact fallback
- dynamic shared selector banks only for severe area constraints
- extra intentional receiver membrane capacitor only if a real glitch problem later requires it
- old regional PVT/leak adaptation if a future measured PVT/leak problem reappears in the current small-dendrite architecture
- v11U-style slow calibration/offset memory for genuinely low-margin comparators if it later proves cheaper than repeated self-check
- two-phase polarity-swap/self-check for low-margin/unknown analog evidence or periodic health checking
- **hybrid-bonded memory/event tier** when measured communication/area savings justify bonding, thermal, yield and test cost
- backside power delivery when moving to an advanced process that supports it and system power/routing data justify it

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
- unconditional two-phase swap for the final high-margin 3-step sound Grammar primitive; v13A6 shows the current data does not justify paying that cost on every normal event
- making the first GVS prototype depend on exotic monolithic 3D/CFET fabrication
- sending tiny analog evidence directly across a die-to-die vertical interface
- using 3D merely because it is advanced if 2D/BEOL overlap is cheaper

## Open, worth testing
- physical layout/PEX of the v13A6 **7-MOS direct one-phase Grammar reader** attached to the extracted equal-total MIM ratio
- **verticalized v13A6 layout**: place the 10-MIM candidate/reference array directly above the reader/local logic and compare area + GC/GR parasitics against side-by-side placement
- measured one-phase readout energy; do not estimate by simply halving the old two-phase number
- pack one shared Grammar reference/direct reader beside/under the selected eight-way Regional Lease and measure real area/coupling
- retain/characterize the two-phase reader as a low-margin safety mode rather than the default
- local template/Myelin evidence behind the eight-way lease after Grammar readout layout
- physical 4x4 / 16x16 grid loaded with the final selected coordinate-release/lease interfaces
- full physical tile layout/extraction beyond slices
- stacked MIM recovery storage if real DRC/PEX proves legal and worthwhile
- inter-island hierarchy above one 16x16 physical island
- **hybrid-bonded event/config/memory tier** after the same-die vertical cell is physically signed off; use measured/technology-specific bond parasitics rather than literature proxies for final decisions
- thermal model for any real 3D stack before stacking high-power exact compute with analog/event tiers
- compiler using real measured area + wire + fallback + driver + robust-readout + 3D-interface cost instead of proxies
- full multimodal system test with image, sound, code and reasoning using the same physical-cost-aware promotion/demotion policy
- compatible simulator/model route for re-running the historical v12S continuous-model signoff without modifying v12S
