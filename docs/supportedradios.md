
Below is a list of EdgeTX-compatible radios and their level of support.

###Officially Supported Radios

The development and support for EdgeTX is conducted by the EdgeTX core development team with the support of developers from the community. Firmware for these radios is included in the main EdgeTX codebase.

* Flysky EL18 (since v2.8)
* Flysky NB4+[^1] (limited support since v2.11) 
* Flysky NV14[^2] (since v2.5)
* Flysky PA01 (since v2.11.3)
* Flysky PL18/PL18EV[^3] (limited support since v2.10)
* Flysky PL18U (since v2.11.2)
* Flysky ST16[^4] (limited support since v2.11)
* Jumper Bumblebee (since v2.10.5)
* Jumper T-Lite / T-Lite v2 (since v2.4, v2.11 will be the last version to support this radio)
* Jumper T-Pro (since v2.6, v2.11 will be the last version to support this radio)
* Jumper T-Pro v2 (since v2.10)
* Jumper T-Pro S (since v2.10.3)
* Jumper T12 / T12 Plus / T12 Pro Hall (since v2.4, v2.11 will be the last version to support this radio)
* Jumper T12 Max (since v2.10.3)
* Jumper T14 (since v2.10)
* Jumper T15 (since v2.10.1)
* Jumper T15 Pro (will be supported from EdgeTX v2.12)
* Jumper T16 / T16 Plus / T16 Pro Hall (since v2.4)
* Jumper T18 / T18 Lite / T18 Pro (since v2.4)
* Jumper T20 (since v2.10)
* Jumper T20 V2 (since v2.10)
* RadioMaster Boxer (since v2.8.1)
* RadioMaster GX12 (since v2.11)
* RadioMaster MT12 (since v2.10, Companion to follow)
* RadioMaster Pocket (since v2.10)
* RadioMaster T8 Pro (since v2.4, v2.11 will be the last version to support this radio)
* RadioMaster TX12 (since v2.4, v2.11 will be the last version to support this radio)
* RadioMaster TX12 Mark II (since v2.8)
* RadioMaster TX15 (will be supported from EdgeTX v2.12, until then, use [RadioMaster factory downloads](https://radiomasterrc.com/pages/tx15-downloads))
* RadioMaster TX16S / RadioMaster TX16S MAX / RadioMaster TX16S Mark II (since v2.4)
* RadioMaster TX16S MK3 / RadioMaster TX16S MK3 MAX (will be supported from EdgeTX v2.12)
* RadioMaster Zorro (since v2.6)

[^1]: Hardware modifications are required to support EdgeTX on Flysky NB4+, see [NB4+ hw mods](https://github.com/EdgeTX/edgetx/wiki/Flysky-NB4--Hardware-Mod-for-Complete-EdgeTX-Support) for more info. Internal RF module is not supported by EdgeTX.  
[^2]: Some external RF modules might not work correctly due to radio hardware not able to provide enough power to the module.  
[^3]: Hardware modifications are required to support EdgeTX on Flysky PL18/PL18EV, see [PL18/PL18EV hw mods](https://github.com/EdgeTX/edgetx/wiki/Flysky-PL18-%26-PL18EV-Hardware-Mod-for-Complete-EdgeTX-Support) for more info.  
[^4]: Internal RF module and magnetometer are not supported.

---

###Manufacturer Supported
 
The development and support for EdgeTX is conducted by the hardware manufacturers themselves. All changes made by the manufacturer are then submitted for review and inclusion into the main EdgeTX codebase.

* iFlight Commando8 (since v2.8)
* BetaFPV LiteRadio3 Pro (since v2.8, v2.11 will be the last version to support this radio)
* FatFish F16 (since v2.11)
* HelloRadioSky V12 (TBD on release)
* HelloRadioSky V14 (since v2.11)
* HelloRadioSky V16 (since v2.11)

---

###Not supported by the EdgeTX Team - Community supported only

The development and support for EdgeTX is conducted by other interested 3rd parties from the community. Changes can be proposed as pull-requests to be considered for inclusion into the main EdgeTX codebase.

* Eachine TX16S (since v2.4)  
* FrSky QX7 / QX7S (since v2.4, v2.11 will be the last version to support this radio)  
* FrSky QX7 ACCESS / QX7S ACCESS (since v2.4)  
* FrSky X9 Lite / X9 Lite S (since v2.4, v2.11 will be the last version to support this radio)
* FrSky X9D / X9D+ / X9D+ SE (since v2.4, v2.11 will be the last version to support this radio)
* FrSky X9D+ 2019 / X9D+ SE 2019  (since v2.4)
* Frsky X9E / Frsky X9E Hall (since v2.4)
* FrSky X10 / X10S / X10 Express / X10S Express (since v2.4)
* FrSky X12S / X12S-IRSM (since v2.4)
* FrSky X-Lite / X-Lite S / X-Lite Pro (since v2.4, v2.11 will be the last version to support this radio)

---
***Note**: To better support the manufacturers' release timelines, the manufacturers' can release an EdgeTX-supported radio with a "ready for manufacture" version of EdgeTX that has been developed in collaboration with the EdgeTX team that has not yet been merged into the main codebase. As a result, this firmware will not be available in EdgeTX Buddy or EdgeTX Companion until the next minor EdgeTX release. 
