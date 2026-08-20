import csv

VDD = 1.8
PLANAR_SELECTION_FJ = 680.0
LEASE_BURST_FJ = 106.8
M4_FF_PER_UM = 0.076106
LOCAL_WIRE_UM_EACH = 50.0

# Architecture-screen inputs from published hybrid-bond literature.
# These are not GVS-measured foundry guarantees.
BONDS = [
    (10.0, 3.0),
    (5.0, 0.1),
    (1.0, 0.07),
]


def cv2_fj(c_ff):
    return c_ff * VDD * VDD


def main():
    local_wire_c_ff = 2.0 * LOCAL_WIRE_UM_EACH * M4_FF_PER_UM
    local_wire_e_fj = cv2_fj(local_wire_c_ff)

    rows = []
    for pitch_um, bond_c_ff in BONDS:
        for overhead_x in (1, 4, 8, 16):
            vertical_links_fj = cv2_fj(2.0 * bond_c_ff) * overhead_x
            selection_fj = vertical_links_fj + local_wire_e_fj
            rows.append({
                "architecture": f"hybrid_bond_{pitch_um:g}um",
                "bond_pitch_um": pitch_um,
                "bond_cap_fF_each": bond_c_ff,
                "vertical_link_overhead_x": overhead_x,
                "assumed_local_wire_um_each": LOCAL_WIRE_UM_EACH,
                "selection_energy_fJ": selection_fj,
                "selection_saving_vs_planar_pct": 100.0 * (1.0 - selection_fj / PLANAR_SELECTION_FJ),
                "selection_plus_12event_lease_fJ": selection_fj + LEASE_BURST_FJ,
                "region_saving_vs_planar_pct": 100.0 * (1.0 - (selection_fj + LEASE_BURST_FJ) / (PLANAR_SELECTION_FJ + LEASE_BURST_FJ)),
            })

    # Deliberately conservative interface-capacitance stress.
    bond_c_ff = 3.0 + 20.0
    selection_fj = cv2_fj(2.0 * bond_c_ff) + local_wire_e_fj
    rows.append({
        "architecture": "10um_plus_20fF_interface_each",
        "bond_pitch_um": 10.0,
        "bond_cap_fF_each": bond_c_ff,
        "vertical_link_overhead_x": 1,
        "assumed_local_wire_um_each": LOCAL_WIRE_UM_EACH,
        "selection_energy_fJ": selection_fj,
        "selection_saving_vs_planar_pct": 100.0 * (1.0 - selection_fj / PLANAR_SELECTION_FJ),
        "selection_plus_12event_lease_fJ": selection_fj + LEASE_BURST_FJ,
        "region_saving_vs_planar_pct": 100.0 * (1.0 - (selection_fj + LEASE_BURST_FJ) / (PLANAR_SELECTION_FJ + LEASE_BURST_FJ)),
    })

    fields = list(rows[0].keys())
    with open("3d_selection_energy_screen.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
