"""Exclude macOS AppleDouble sidecars from every PlatformIO source scan."""

Import("env")

from platformio.builder.tools import piobuild


APPLEDOUBLE_FILTER = "-<**/._*>"
if APPLEDOUBLE_FILTER not in piobuild.SRC_FILTER_DEFAULT:
    piobuild.SRC_FILTER_DEFAULT.append(APPLEDOUBLE_FILTER)
