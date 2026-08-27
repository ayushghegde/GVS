# v13T1 — Adaptation Timescale Sweep

**Verdict: MODEL PASS / BOUNDARY FOUND.** One adaptation speed is not sufficient.

50 seeds are tested at phase durations 4, 8, 16, 32, 64 and 120 epochs using instant chase, one-timescale homeostasis and dual-timescale homeostasis.

At very fast phase changes, instant chasing has the lowest queue but switches many times more often. The dual system stays close while cutting switching. At phase durations 64 and 120, dual-timescale homeostasis also has lower backlog than instant chasing.

Decision: keep a small fast reserve plus a small slow reserve. Do not let all reserve cells adapt at the fastest timescale.
