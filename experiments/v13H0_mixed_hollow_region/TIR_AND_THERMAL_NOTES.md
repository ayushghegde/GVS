# v13H TIR + Thermal Notes

## Thin optical route
A literal air/hollow core is not selected for ordinary total internal reflection (TIR), because standard TIR requires a higher-index guiding core surrounded by lower-index material. The selected near-term architecture proxy is therefore a very thin transparent glass/polymer lightpipe through the hollow volume, not a component-sized empty corridor. Hollow/air-core anti-resonant guidance remains future research only.

Reference model uses published glass-waveguide values around 0.08 dB/cm propagation loss and ~0.47 dB/facet coupling. Combined with the existing direct-photocharge receiver model, 15% laser wall-plug efficiency and 5.9 fJ modulator proxy, runtime optical event energy is ~10.9-11.1 fJ across 3-20 mm.

Electrical comparison uses current GVS dedicated-route proxy `0.15 + 3.74*d_mm` fJ/event. Including a 1 pJ rare route-write cost, optical promotion requires about 2102 reuses at 3 mm, 126 at 5 mm, 38 at 10 mm, 23 at 15 mm and 16 at 20 mm. Therefore thin TIR lightpipes are kept only for long/hot routes.

A ~9x9 um demonstrated waveguide core occupies only ~0.00081 mm^3 over 10 mm length; even a conservative 50x50 um reserved lane is ~0.025 mm^3. The optical route therefore need not reserve component-sized empty volume.

## Large shared thermal exhaust/harvester
The user's preferred thermal architecture is interpreted as a component-free hollow thermal route shared by many chips/regions, carrying heat outward to one large top/package/rack harvester rather than putting a TEG on every small cell.

A literally evacuated empty channel is not a good high-power heat carrier by itself; at chip-like temperatures radiation across 1 cm^2 is only tens of milliwatts for modest temperature differences. The closest useful physical implementation is a hollow vapor chamber / heat-pipe-like exhaust, or a fluid/air manifold, with conductive walls/wicks that collect heat and transport it to the external condenser/harvester.

Selected sequence:
`hot framework -> thermal spreader/wick -> hollow vapor/exhaust artery -> shared top condenser/heat exchanger -> optional thermoelectric harvester -> facility/environment heat rejection or useful hot-water loop`.

The thermoelectric stage is placed at the external collection boundary so it does not add thermal resistance at every cell.

A 2025 rack-scale TEG+heat-pipe+PCM model reported 125 W electrical output from a 25 kW rack (0.5%) and 219 W in a dual-stage variant (~0.876%), while ~20.1 kW of useful heat was delivered as hot water. Linear scaling is used only as a scenario screen: 64 chips at 200 W each (~12.8 kW heat) correspond to ~64-112 W electrical recovery and ~10.3 kW useful heat under those same ratios. This is not a GVS measurement.

Decision: harvest heat at large scale, but prioritize low thermal resistance and useful heat export; never sacrifice chip cooling to chase a small thermoelectric percentage.
