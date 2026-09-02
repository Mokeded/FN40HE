# Assembly variants

The PCB contains 57 independent Hall-sensor channels. The overlapping bottom
row switch positions are mechanical alternatives; do not install switches or a
plate that attempts to use overlapping options simultaneously.

HE48/HE48A and HE53/HE53A are close alternate-layout pairs. Each pair retains
both switch outlines and both alignment-hole pairs but uses one midpoint Hall
sensor and one capacitor pair, as on HE60. Do not add a second sensor at the
mechanical-only HE48A or HE53A position.

## Universal57 — selected release variant

Populate all PCB components, including all 57 MT9102ET sensors and their local
filter capacitors. Select the physical switch layout with the plate. Unused
sensors remain available for a later layout change. This is the default BOM and
the supplied 57-key firmware configuration. The 2026-08-28 prototype release
package uses this variant; SplitSpace and SevenUnit remain documented future
assembly alternatives and are not the released population set.

## SplitSpace

Use the primary split-space bottom row. Do not populate:

- HE55 / C109 / C110 — alternate SW50 position
- HE56 / C111 / C112 — alternate 7U SW53 position

All other components are populated. Firmware for a permanently assembled
SplitSpace board should replace the two omitted mux entries with zero or ignore
firmware keys 54 and 55.

## SevenUnit

Use the original KLE alternative positions SW50 and SW53. Do not populate the
sensors and filter pairs under primary keys that conflict with the 7U keycap:

- HE49 / C97 / C98 — SW51
- HE50 / C99 / C100 — SW52
- HE51 / C101 / C102 — SW54
- HE52 / C103 / C104 — SW55
- HE54 / C107 / C108 — SW49

Populate HE55 (SW50), HE56 (SW53), and HE57 (SW56). The plate, stabilizer
locations, and keycap clearances must be checked against the original FN40 KLE
before ordering. Firmware for a permanently assembled SevenUnit board should
replace the five omitted mux entries with zero or ignore their firmware keys.

`BOM.csv` contains quantities and DNP reference columns for all three variants.
