# FN40HE

FN40HE is a 40%, Hall-effect mechanical keyboard PCB and firmware project. It
adapts the FN40 layout to magnetic (Hall-effect) switches, giving every key
analog actuation — per-key adjustable actuation points, Rapid Trigger,
SOCD/Null Bind, Dynamic Keystroke, and analog gamepad output — instead of a
fixed mechanical trip point.

## What's in this repository

- **KiCad hardware design** — `FN40HE.kicad_pro`/`.kicad_sch`/`.kicad_pcb`,
  a two-layer PCB with 57 independent Hall-sensor channels multiplexed down
  to an 8-channel ADC scan order, plus `FN40HE-plate.step` for the
  mechanical plate reference. `FN40_Project.pretty`, `lib`, `fp-lib-table`,
  and `sym-lib-table` are the local footprint/symbol libraries needed to
  open the project without external dependencies.
- **Firmware** (`firmware/`) — a [libhmk](https://github.com/libhmk/libhmk)-derived
  build configured for the `fn40he` board target, with prebuilt DFU
  artifacts in `firmware/build/` and full source under `firmware/source/`
  for rebuilding.
- **Manufacturing and assembly data** — `FN40HE-BOM.csv` (bill of
  materials for all assembly variants), `FN40HE-ASSEMBLY.md` (which
  mutually-exclusive switch/sensor positions to populate per variant),
  `FN40HE-sensor-map.csv` and `FN40HE-mux-map.csv` (physical-to-firmware
  key mapping), and `manufacturing/FN40HE-Gerbers-JLCPCB.zip` (bare-board
  fab archive).
- **Verification records** — `FN40HE-DRC.rpt` and `FN40HE-ERC.rpt` (PCB/
  schematic check reports) and `FN40HE-J1-WAIVER.md` (documented DRC
  waiver and inspection requirement for the J1 connector footprint).

See `FN40HE-README.md` for release status, build/flash instructions, and
firmware feature details.

## Assembly variants

The board supports three populate/DNP variants sharing one PCB:
**Universal57** (all 57 sensors populated — the released default),
**SplitSpace**, and **SevenUnit** (alternate bottom-row layouts). See
`FN40HE-ASSEMBLY.md` and the DNP columns in `FN40HE-BOM.csv` before
ordering assembly.

## License

This project incorporates GPLv3-derived hardware design and firmware work.
See `LICENSE`. Retain source, license, and attribution when redistributing
modifications.
