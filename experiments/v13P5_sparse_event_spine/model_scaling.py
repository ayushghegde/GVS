#!/usr/bin/env python3
"""v13P5 Sparse Event Spine scaling screen.

Uses measured v13P physical parasitics. This is a modeled scaling experiment,
not extracted-layout or transistor-level validation.
"""
import math

VDD = 1.8
M4_FF_PER_UM = 7.6106 / 100.0
REAL_GATE_ATTACH_FF = 0.7065
GROUP = 4
LOCAL_LEN_UM = 25.0
PARENT_LEN_UM = 100.0

def flat_cap_ff(n):
    length_um = 6.25 * n
    return M4_FF_PER_UM * length_um + REAL_GATE_ATTACH_FF * n

def local_cap_ff():
    return M4_FF_PER_UM * LOCAL_LEN_UM + REAL_GATE_ATTACH_FF * GROUP

def parent_cap_ff():
    return M4_FF_PER_UM * PARENT_LEN_UM + REAL_GATE_ATTACH_FF * GROUP

def ses_active_path_ff(n):
    levels = math.ceil(math.log(n, GROUP))
    return local_cap_ff() + max(0, levels - 1) * parent_cap_ff()

def cycle_energy_fj(c_ff):
    return c_ff * VDD * VDD

print('edges,flat_fF,ses_active_path_fF,reduction_pct,flat_cycle_fJ,ses_cycle_fJ')
for n in (16, 64, 256, 1024):
    f = flat_cap_ff(n)
    s = ses_active_path_ff(n)
    print(f'{n},{f:.5f},{s:.5f},{100*(1-s/f):.3f},{cycle_energy_fj(f):.5f},{cycle_energy_fj(s):.5f}')
