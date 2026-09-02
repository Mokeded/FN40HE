#pragma once

// Persistent-profile layout signature for the FN40-HE60 configuration with
// four profiles and 57 advanced-key slots. The earlier FN40 build used the
// generic signature with 32 slots; using a keyboard-specific signature makes
// that incompatible layout reset safely instead of being read at wrong offsets.
#define EECONFIG_MAGIC_START 0x46353701
