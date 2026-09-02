# FN40HE release project

This folder is the compact, portable FN40 Hall-effect keyboard project. Open
`FN40HE.kicad_pro` in KiCad 10.

## Release checks completed on 2026-09-01

- PCB DRC: 0 violations, 0 unconnected pads, 0 footprint errors.
- Schematic ERC: 0 errors and 0 warnings.
- Firmware mapping: all 64 mux channels agree across the PCB, schematic,
  `FN40HE-mux-map.csv`, and the firmware configuration.
- ADC order: A3, A4, A5, A6, A7, C4, C5, B0.
- Firmware clean build: successful with compiler warnings treated as errors.
- Firmware size: 33,452 bytes flash (12.8%) and 14,724 bytes RAM (14.1%).
- JLCPCB Gerber ZIP: archive integrity passed.

The firmware is source/build/mapping ready, but it has not yet been proven on
an assembled FN40HE PCB. The first prototype still needs DFU flashing, USB
enumeration, every-key analog verification, calibration, and functional tests
for Rapid Trigger, SOCD, actuation settings, profiles, and alternate layouts.

## Main files

- `FN40HE.kicad_pro`, `FN40HE.kicad_sch`, `FN40HE.kicad_pcb`: KiCad project.
- `FN40_Project.pretty`, `lib`, `fp-lib-table`, `sym-lib-table`: portable local
  footprint and symbol libraries required by the KiCad project.
- `FN40HE-BOM.csv`: assembly bill of materials.
- `FN40HE-ASSEMBLY.md`: mutually exclusive layout/population guidance.
- `FN40HE-sensor-map.csv`, `FN40HE-mux-map.csv`: physical and firmware maps.
- `FN40HE-J1-WAIVER.md`: inherited connector drilling rationale and first-unit
  inspection requirement.
- `FN40HE-DRC.rpt`, `FN40HE-ERC.rpt`: final electrical check reports.
- `FN40HE-plate.step`: plate/mechanical reference.
- `manufacturing/FN40HE-Gerbers-JLCPCB.zip`: current bare-board upload archive.
- `firmware/build/FN40HE.bin`: normal DFU flashing artifact.
- `firmware/build/FN40HE.hex` and `FN40HE.elf`: alternate/debug artifacts.
- `firmware/source`: complete libhmk-derived source for rebuilding.

## Firmware build and flashing

From `firmware/source`, install PlatformIO, then run:

```sh
python setup.py -k fn40he
pio run
```

The checked-in `platformio.ini` is already configured for `fn40he`. Enter the
AT32 factory DFU bootloader by holding BOOT while connecting USB, then flash
`firmware/build/FN40HE.bin` with a compatible AT32/DFU tool. Do not flash the
first production batch before one assembled prototype has passed the hardware
tests listed above.

## Firmware features and configuration

The firmware includes four profiles, per-key adjustable actuation, split and
continuous Rapid Trigger, Null Bind/SOCD and distance priority, Dynamic
Keystroke, macros, analog gamepad mappings, calibration, and high-speed USB
polling. Use hmkconf after flashing and calibration. The default profile starts
with Rapid Trigger and SOCD disabled.

## Manufacturing notes

The intended board is two-layer FR-4, 1.2 mm finished thickness, and 1 oz outer
copper. Review the J1 reliefs and routed NPTH slots in JLCPCB's CAM viewer. The
J1 geometry is inherited from the working MX FN40 and remains a documented
prototype inspection item.

The design and firmware include GPLv3-derived work. Retain `LICENSE`, source,
and attribution when redistributing modifications.
