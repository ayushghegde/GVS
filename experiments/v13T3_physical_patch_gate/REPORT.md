# v13T3 — Physical Adaptive Patch-Gate Geometry

**Verdict: PHYSICAL GEOMETRY PASS; transistor/PVT closure open.**

Magic 8.3.681 + SKY130A tech `1.0.602-0-gf3c505b` with two real recovered `nf_reset` NFET cells.

The two patch-selection devices and Role Pressure lines are placed at the cell boundary around a preserved GC/GR weak-pair geometry.

Results:
- DRC errors: **0**
- NFET instances: **2**
- GC-GR: **0.040625 fF**
- no direct STATE/PATCH/ROLE_PRESSURE -> GC or GR capacitance term reported at extraction precision
- local state->own-patch coupling: ~0.0310908 fF
- role-pressure->own-patch: ~0.00217518 fF
- state->role-pressure: ~0.00260013 fF

The geometry proves boundary placement is compatible with weak-evidence isolation. It does not prove ON/OFF patch timing, analog Role Pressure storage, PVT or mismatch.
