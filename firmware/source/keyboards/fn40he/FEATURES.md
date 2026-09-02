# FN40HE analog and gaming features

The FN40HE firmware uses libhmk's analog input and advanced-key engine. The
settings are stored in the emulated EEPROM on the AT32F405, so the configurator
does not need to stay open after saving a profile.

Use [hmkconf](https://hmkconf.com/) to configure the features below after the
firmware has been flashed and the keyboard has completed its initial
calibration.

## Onboard profiles

The keyboard provides four onboard profiles. Each profile stores its own
keymap, per-key actuation and Rapid Trigger settings, advanced keys, macros,
gamepad bindings, analog curve, and tick rate.

- `Fn + F9`: swap between the default profile and the last non-default profile.
- `Fn + F10`: advance to the next profile.

The default profile starts with Rapid Trigger and SOCD disabled. This avoids
surprising key behavior before the Hall sensors have been tested and calibrated.

The first boot of this feature build resets settings written by the earlier
32-advanced-key FN40 firmware because the persistent profile layout is larger.
Subsequent updates using the same layout preserve the onboard settings normally.

## Adjustable actuation

Every Hall-effect key has an independent actuation point represented internally
as a normalized value from 0 to 255 over its calibrated travel. The default is
128, or approximately the middle of the measured travel. Use the live analog
view in hmkconf to tune actuation after the switches have been installed.

## Rapid Trigger

Rapid Trigger can be enabled per key. Press and release sensitivity can share
one value or use separate values. Continuous mode keeps Rapid Trigger active
until the key returns to its calibrated rest position.

For a first hardware test, begin with a conservative sensitivity and enable it
only on movement keys. Extremely small values can amplify sensor noise or
mechanical wobble, especially before every key has reached bottom-out at least
once and established its travel range.

## SOCD and distance priority

Null Bind pairs provide the following simultaneous-key resolution modes:

- last input wins;
- first/primary key wins;
- second/secondary key wins;
- neutral, where both keys are released;
- distance priority, where the more deeply pressed key wins.

Distance priority is the libhmk equivalent of Wooting's Rappy Snappy behavior.
An optional bottom-out threshold can allow both keys once both have passed that
depth. Typical pairs are `A`/`D` and `W`/`S`.

SOCD rules differ between games and tournaments. Configure the behavior that is
permitted for the intended game rather than assuming last-input or distance
priority is universally allowed.

## Dynamic Keystroke and advanced keys

The firmware reserves 57 advanced-key slots per profile, enough for every
physical Hall-effect key. Supported advanced behaviors include:

- Dynamic Keystroke with up to four bindings and actions at press, bottom-out,
  release from bottom-out, and release;
- tap-hold;
- toggle;
- macros;
- Null Bind/SOCD pairs.

Dynamic Keystroke temporarily controls the affected key's press stages itself,
so the firmware suppresses Rapid Trigger for that key while a DKS stroke is in
progress.

## Analog gamepad

Profiles can map keys to XInput buttons, triggers, or joystick directions. The
analog curve, circular or square joystick output, and snappy opposite-axis
behavior are configurable. XInput is disabled by default so the keyboard starts
as a conventional USB keyboard.

## Calibration and polling

The keyboard automatically calibrates the resting sensor values at startup and
learns each key's bottom-out range during use. A full recalibration is also
available through hmkconf.

High-speed polling is enabled by default for the AT32F405 USB high-speed
interface. The firmware can fall back to the lower polling mode through its
global options if compatibility testing requires it.

## Scope compared with Wooting

These features provide comparable input concepts, but this is not Wooting
firmware and does not use Wootility. Physical travel accuracy depends on the
MT9102ET sensors, magnet/switch geometry, calibration, filtering, and noise of
the assembled FN40HE. RGB lighting is not supported by libhmk.
