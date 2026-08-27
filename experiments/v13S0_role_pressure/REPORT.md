# Neural Glyph v13S0 — Role-Pressure Reserve Differentiation

**Verdict: MODEL PASS.** Keep most cells physically differentiated as in v13R, but allow only the small General Reserve population to re-role itself from persistent local demand. This improves workload adaptation without returning to a universal cell.

**Role Pressure Field (RPF):** a local low-swing/familiarity-like need signal produced by persistent backlog in a functional population; General Reserve Cells integrate the pressure and temporarily adopt the most under-supplied role.

64-cell region: Grammar 12, template 10, binding 8, constraint 8, exact 2, plus four General Reserve Cells. Seven 120-epoch phases deliberately shift demand between mixed, Grammar-heavy, template-heavy, binding-heavy, constraint-heavy, exact-heavy and mixed-return operation.

Results on identical arrivals:
- fixed reserve roles: backlog 374,590; max queue 812; ending queue 553;
- RPF: **102,786**; max queue **335**; ending queue **18**; 40 role changes/840 epochs;
- ideal instantaneous oracle: backlog 88,218; max queue 300; ending queue 4.

RPF therefore cuts accumulated backlog **72.56%** and max queue **58.74%** versus fixed reserves, while remaining only **16.51% above the oracle**.

A conservative support proxy counts 1,769 pressure pulses. Even charging four separate 0.67 fJ event-spine taps per pulse is only ~**0.156 fJ per completed modeled operation**. This is a carrier proxy, not a physical RPF circuit measurement.

At epoch 420, a deterministic 10% specialized-cell failure removes one template, two binding and one constraint cell. RPF reduces backlog from 559,680 to 234,709 (**58.06% lower**) versus fixed reserves.

KEEP differentiated ordinary cells, a small General Reserve population, persistent pressure/hysteresis and switching cost/fatigue. REJECT making all cells universal again, a central role allocator, and zero-hysteresis fast switching.

Evidence boundary: deterministic queue/capacity model. General Reserve Cells logically re-role; fixed specialized cells do not change transistor inventory at runtime.

Reproduce: `python3 experiments/v13S0_role_pressure/source/run_v13s0.py`
