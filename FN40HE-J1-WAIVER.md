# J1 mounting-relief DRC waiver

Date: 2026-08-28  
Scope: J1 only — Molex 781710004 unified-daughterboard connector mounting
reliefs.

## Waived findings

The eight annular-width and eight hole-to-hole findings associated with J1's
mounting-relief geometry are waived for this placement-stage revision. They
are intentional features of the project-local
`J1_MOLEX_781710004_MountingReliefs` footprint and do not represent a changed
electrical connection or a routing defect.

The `MP` mounting/relief pad is tied to GND in both the board and schematic.
The J1 position and footprint geometry match the working MX FN40 reference
board used by this project. The electrical pins remain VBUS, D-, D+, and GND.

## Conditions of this waiver

- Use only the specified Molex 781710004 connector and the current local
  footprint geometry.
- Confirm the relief/drill drawing against the selected PCB fabricator's
  capabilities before release.
- Inspect the connector on the first assembled prototype for fit, retention,
  and daughterboard alignment.
- Verify the unified daughterboard cable orientation before applying power.
- This waiver does not cover clearance, shorts, unconnected nets, USB,
  analog, power, mechanical, or any other DRC category.

The imported 4060 DRC policy globally ignores some hole-related categories;
this record preserves the intended, limited engineering rationale for J1.
