# External physical evidence used to define v14S targets

These papers support candidate material/device *ranges*. They do not prove the GVS compound branch.

1. Jintai Liu et al., **Ultra-low-voltage operation, large ferroelectric polarization, fast switching speed, and high endurance of 450 °C processed HZO thin films by starting-layer engineering**, Journal of Materials Science & Technology, 2026. Reported 5-nm HZO with Pr ≈ 15.8 µC/cm² at 1.2 V, and low-voltage/endurance data. This is the reason v14S uses `P≈0.16 C/m²` and a 1.2-V selected-program target as a screening point.
2. Zhiyuan Fu et al., **Hafnia-Based High-Disturbance-Immune and Selector-Free Cross-Point FeRAM**, IEEE Transactions on Electron Devices, 2024, DOI 10.1109/TED.2024.3369569. Demonstrated a selector-free 1-kbit HZO cross-point FeRAM and quantified disturb behavior; supports treating array disturb as an engineering problem rather than assuming per-cell MOS selection is mandatory.
3. Shan Deng et al., **Vertical 2T-nC FeRAM Demonstration: BEOL Read Transistor for 4F² Memory Strings and Two-Terminal Selector Design for Polarization Disturb Mitigation**, VLSI Technology and Circuits 2025, DOI 10.23919/VLSITechnologyandCir65189.2025.11074964. Demonstrated experimentally that inserting passive nonlinearity into a ferroelectric capacitor stack can reduce polarization disturb; supports the v14S nonlinear-inhibit research direction.

The v14S model deliberately does not copy any reported device stack as if it were already compatible with the guided-gap branch. Physical integration remains the next experiment.
