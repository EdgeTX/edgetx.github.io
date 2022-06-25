 
## Developer Competition: 
<p align="center">
<a><img src="https://raw.githubusercontent.com/EdgeTX/edgetx.github.io/master/images/Doomport.jpg" align="center" height="318" width="366"></a>
</P>

<h2>sponsored by:</h2>
<p align="center">
<a href="https://www.radiomasterrc.com/" target="_blank"><img src="https://github.com/EdgeTX/edgetx.github.io/blob/master/images/RadioMasterLogo.png?raw=true" align="center" width="497"></a>
</p>

**Task:** 

Port the DOOM video game so that it can be played on the Radiomaster TX16S.
 
 **Contest Details:**
 
The game must be playable by the user interfaces available on stock TX16S (touchscreen, buttons, roller, gimbals, pots, sliders, switches or any combination of them. Whatever works intuitively and does not require additional hardware or mods to TX16S, will be accepted).
 
Must use microSD card for the WAD resource file (unlike the [current STM32F429 implementation](https://github.com/floppes/stm32doom) that uses a USB drive).

Submissions shall be posted into the [EdgeTX Discord](https://discord.gg/wF9wUKnZ6H) **#doom-dev-competition** channel with links to the GitHub repo of the working code and a YouTube video presenting/showing the result.

The first person to post working code with an accompanying video, will win the prize: **1 set of Radiomaster AG01 gimbals** - including free shipping world-wide.

<p align="center">
<a href="https://www.youtube.com/watch?v=82-fAHKRMVE" target="_blank"><img src="https://raw.githubusercontent.com/EdgeTX/edgetx.github.io/master/images/RM_AG01_video.jpg" align="center" width="500"></a>
</p>

*Note: winner is responsible for any VAT or customs fees applicable in their country.*

### ***Deadline for submissions: September 9th, 2022***

**Helpful links to get you started:**

STM32F429 Discovery board Doom implementation: [https://github.com/floppes/stm32doom](https://github.com/floppes/stm32doom)

*Note: the TX16S has slightly different display resolution (320x240 vs. 480x272) and different touch controller chip (STMPE811 vs. GT911), but same STM32F429 type microcontroller.*

EdgeTX TX16S firmware code as reference for interacting with TX16S power circuitry, display, microSD, touchscreen and buttons: [https://github.com/EdgeTX/edgetx/](https://github.com/EdgeTX/edgetx/)

TX16S schematics with detailed explanation of functionality: [RCGroups Blog post: TX16S schematic diagram](https://www.rcgroups.com/forums/showthread.php?3869543-Blog-17-RadioMaster-TX16S-schematic-diagram)

### Bonus

A solution that can be flashed via EdgeTX bootloader without having to resort to DFU flashing (e.g. `doom_tx16s_fw.bin` under SD card `\FIRMWARE` and Doom shareware WAD file under `\DOOM\doom1.wad`) will receive a bonus prize - [RadioMaster Sticky360 Gimbal Stick Ends for TX16S](https://www.radiomasterrc.com/collections/tx16s-accessories/products/sticky360-gimbal-stick-ends-for-tx16s) (the winner can pick the color).

<p align="center">
<a href="https://www.youtube.com/watch?v=W80j61uyR6g" target="_blank"><img src="https://cdn.shopify.com/s/files/1/0609/8324/7079/files/STICKY360-1200X900_1024x1024.gif" align="center" width="500"></a>
</p>
