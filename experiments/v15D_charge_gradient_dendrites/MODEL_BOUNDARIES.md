# v15D Model Boundaries

Actual ngspice verifies the compact electrical charge accumulation/decay and deterministic charge-biased branch-current split.

Python models:
- stochastic guided-gap nucleation/selection;
- coupled free electrode charge, HZO polarization charge, seven-domain NLS/Merz-like switching and leakage;
- need-based replay / unknown / redefinition behavior.

Not yet measured in a GVS physical device:
- signed residual charge captured per guided-gap firing event;
- actual retention time of that residual;
- exact electrostatic coupling from residual charge/HZO polarization to guided-gap nucleation;
- multi-level HZO polarization retention under this nanoscale geometry;
- irreversible Ag deep-trap statistics.

Therefore v15D is a partial physics pass, not a fabricated-device claim.
