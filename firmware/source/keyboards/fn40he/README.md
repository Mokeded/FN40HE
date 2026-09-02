# FN40HE

FN40HE is a 57-position Hall-effect conversion of the Mokeded FN40 PCB. It uses
the HE60 v2 AT32F405 analog architecture and the libhmk firmware stack.

- MCU: AT32F405RCT7
- Oscillator: 12 MHz HSE
- USB: high-speed (`hs`) through the unified daughterboard connector
- Sensors: 57 x MT9102ET
- Multiplexers: 8 x SN74LV4051A
- PCB: 2 layers, 1.2 mm finished thickness

The default key numbering follows `sensor-map.csv`: firmware key 0 is HE1 and
firmware key 56 is HE57. The unused mux slots are encoded as zero, matching
libhmk's convention.

The firmware includes per-key adjustable actuation, split and continuous Rapid
Trigger, Null Bind/SOCD and distance priority, Dynamic Keystroke, tap-hold,
toggle, macros, four onboard profiles, automatic calibration, analog XInput,
and high-speed polling. See [FEATURES.md](FEATURES.md) for configuration details
and safe initial settings. `Fn + F9` swaps profiles and `Fn + F10` selects the
next profile.

Enter the factory AT32 DFU bootloader by holding the physical BOOT button while
connecting USB, or by using the `SP_BOOT` binding on layer 1.

Run `python setup.py -k fn40he`, then `pio run` to build.
