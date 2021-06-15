# EdgeTX 2.4 Release Notes
# -Draft-

We are happy to bring you the first release of EdgeTX – the cutting edge open source firmware for your R/C radio. EdgeTX is a fork of OpenTX 2.3.11, so it contains all the current features of OTX2.3.11 as well and some additional features that were slated for OTX 2.3.12 including:
* Add support for RadioMaster T8
* Multirotor Wizard for Color LCD radios
* Add ETX1 and EXT1 to calibration screen
* Add support for Jumper T-Lite
* Fix multi per channel failsafe
* Add telemetry sources for inputs
* Add GHST GPS Telemetry Sensors
* M-Link telemetry
* Multi module config support
* New Lua function getAvailableMemory
* Improved sync for CRSF Shot
* R9M Flex support broken 2.3.12N495
* Stop mixer scheduler when stopping module
* Set correct channel count for Ghost modules
* Several other small fixes

Additionally, EdgeTX adds the several other enhancements and new features:
* Added touchscreen support for touchscreen equipped radios
* Overhauled user interface to better support touchscreen use
* Fix mixer scheduler 33Hz only issue
* Remove legacy ZCHAR
* Added support for MAVLink -**_(TBD)_**
* Radios with internal GPS will display GPS icon and sat number in top bar
* Added OneBit mode to HARDWARE menu in order fix inverter bug in x9D+ and X7
* Raised maximum mixer scheduler period to 50ms (20Hz)
* Added key handling for lua scripts
* Added additional graphics plotting functions
* Make timers conditional on switch (if set)
* Added auto-switch / auto-source for color lcd radios
* Added automated model conversion for models from OpenTX on startup.
* Added many small “under the hood” enhancements and fixes.

### Supported radios
* X9Lite
* QX7
* T12
* TX12
* T8
* Tlite
* XLite
* X9DP
* X9DP2019
* X10
* T16
* TX16S
* X12S
* T18

### Limitations:
Please note the following limitations. At the time of release:
* Users are not able to import model files from OpenTX Companion into to EdgeTX (Firmware flashing with OpenTC Companion is still possible).
* Support for FlySky Nirvana NV14 is not available.
* Users are not able to select a theme or modify the default theme color scheme.

### Download Links:
EdgeTX Flasher: [https://github.com/EdgeTX/flasher/releases](https://github.com/EdgeTX/flasher/releases)

EdgeTX SD Card: [https://github.com/EdgeTX/edgetx-sdcard/releases](https://github.com/EdgeTX/edgetx-sdcard/releases)

### Installation:

Installation Guide - https://github.com/EdgeTX/edgetx.github.io/wiki/How-to-install-EdgeTX--(pre-release)-for-the-first-time (_will update with new installation page link)_

### Thanks:
Special thanks to all those that contributed to making this release possible! Without the support and commitment from the development team and the community, this release would not have been possible.  We are looking forward to bringing you more of the things that you want in our next release on the 21st of September, 2021.

### Keep in touch!
Discord - https://discord.gg/wF9wUKnZ6H

Facebook - https://www.facebook.com/groups/edgetx
