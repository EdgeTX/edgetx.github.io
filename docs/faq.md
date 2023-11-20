---
hide:
  - toc
---

## Frequently Asked Questions

###My computer does not detect my radio when I plug it in via USB. What should I do?###

Ensure that your USB cable is not defective or only charging capable – if not sure, try another one. Also, if your radio has more than one USB port, ensure you are plugging it into the DATA port, not the CHARGING port. This is usually the port at the top of the radio. Lastly, It may be an issue with the drivers on your computer. You can install the **ImpulseRC Driver Fixer** by downloading it from here:  [**https://impulserc.blob.core.windows.net/utilities/ImpulseRC_Driver_Fixer.exe**](https://impulserc.blob.core.windows.net/utilities/ImpulseRC_Driver_Fixer.exe)

###My computer does not see my radio’s SD card. How can I fix that?###

See the steps mentioned above. Ensure your radio is powered on when plugging it in via USB. Also, check that your SD card is installed correctly.

###My radio will not connect to my computer in DFU mode even though I plug it in with it powered off. Why is that?###

Some radios require you to press a button when plugging the radio into the computer to connect in DFU mode. The Jumper T-Pro has the DFU button at the top near the USB port. The Flysky NV18/EL18 have the DFU button concealed down the innermost lanyard holder screw-hole.

###My radio goes into Emergency mode when I power it on or at random times. Why is that?###

The most common cause for your radio to go into Emergency mode is when it cannot properly access the SD card or its contents. This can be caused by a defective SD card, missing SD card files, or a defective SD card port on the radio (rare). In many cases, installing a new, high-quality SD card with fresh SD card contents will fix this issue.

###After flashing EdgeTX on my radio, it has a "No SD Card" error even though the same working SD card is installed. What could be the problem?###

When this error is displayed, the SD card cannot be read. Most of the time, this is due to something physical (slot/contacts). Sometimes the card needs to be correctly re-formatted.

The RadioKing TX18S and early models of the Jumper T18 have a design flaw with the SD card sensor, which results in the radio displaying this error even though an SD card was installed. The manufacturer worked around this issue by creating a custom version of OpenTX that disabled the SD card check in the software. For those radios with this issue, users must use the manufacturer's custom firmware, as EdgeTX will not work.

###I updated to EdgeTX from OpenTX, but my radio still says “Welcome to OpenTX” when I turn it on. How do I fix that?

Ensure that you update your sound pack as described in the [Update Instructions.](https://edgetx.gitbook.io/edgetx-user-manual/edgetx-user-manual/installing-and-updating-edgetx) Make sure that the language folder (**EN** for English language) is in the **Sounds** folder on the SD Card (**SOUNDS**/(**language**)/). Also, ensure that your **voice language** setting in the **Radio Settings** matches the installed sound pack folder. (example: English selected for EN sound pack folder, German selected for DE sound pack folder).

###I do not see any sound files when I create a global/special function for Play Track/BGMusic Why is that?

The sound files must be in the SD card's **SOUNDS**/(**language**)/ folder.

###Why don’t I see my model image files that I put on the SD Card?

Ensure that the images are placed in the **IMAGES** folder on the SD Card. The image file type shall be .png format, and the file name must not exceed nine characters.

###Why is my radio so slow when navigating on the Select Model screen?

This is usually caused when the model image files are too large. The ideal model image size is 192x114 pixels and the ideal file format is .png

###Where can I find image files of different RC models to use with my radio?

A large repository of EdgeTX-compatible RC model image files can be found here: [https://www.air-rc.com/](https://www.air-rc.com/)

###How can I change the background image on my radio?

To change the background image, replace the **background** file in the THEMES -> EdgeTX folder on your SD card with the desired background image file (must have the name **background**). The ideal image size for background and _splash screen images_ is the actual radio screen size (480x272 pixels for most color screen radios). The picture format should be .png. Screen dimensions for the supported color screen radios can be found [here](https://github.com/EdgeTX/edgetx-sdcard).

###How do I change the splash screen image on my color screen radio?

Place the desired splash screen image file (named splash.png) in the /IMAGE/ folder on your SD Card, and EdgeTX will use that image for the splash screen.

###How do I update to EdgeTX from OpenTX?

A detailed update guide can be found here:

[Update from OpenTX to EdgeTX - EdgeTX User Manual (gitbook.io)](https://edgetx.gitbook.io/edgetx-user-manual/edgetx-user-manual/installing-and-updating-edgetx)

###Do I need to re-bind my models after updating to EdgeTX?

No, you should not need to re-bind your models. Your receivers are bound to your RF module, not to the radio firmware. Updating the radio firmware does not affect your RF module.

###Where is the frequency fine-tune feature. It had it in OpenTX?

The frequency fine-tune option is only available in EdgeTX for protocols that support that feature. It will not be shown in the options if it is not supported.

###Does the Yaapu LUA script work with EdgeTX?

Yes, an EdgeTX version of the Horus Mapping Widget from Yaapu exists and can be found here: https://github.com/yaapu/HorusMappingWidget

###Does the Betaflight LUA script work with EdgeTX?

Yes, the Betaflight LUA script does work with EdgeTX. However, it will need to be installed again from scratch after updating from OpenTX to EdgeTX,

###Where can I get LUA Scripts for EdgeTX?

A collection of LUA Scripts compatible with EdgetX can be found here: [https://github.com/EdgeTX/lua-scripts](https://github.com/EdgeTX/lua-scripts)

###When will EdgeTX work on the TBS Mambo and Tango2?

Team Blacksheep is developing a version of EdgeTX that will be compatible with the TBS Mambo and Tango2. The EdgeTX team does not know when it will be complete. Please get in touch with Team Black Sheep for more information. [https://team-blacksheep.freshdesk.com/support/home](https://team-blacksheep.freshdesk.com/support/home)

###Does EdgeTX still have the model wizards?

Yes, the model wizards are still included included in EdgeTX. However, they no longer start automatically and must be started manually. The location of the wizards has been changed to SD Card -> Scripts->Wizard.
