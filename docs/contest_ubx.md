---
hide:
  - navigation
  - toc
---

<p></p> 
<p align="center">
<a><img src="/assets/UBXContestPoster.jpg?raw=true" align="center" width="497"></a>
</P>


## **Contest Details**

**Task:**

Be the first developer to make a pull-request (PR) against EdgeTX main GitHub repository with fully working radio side GPS uBlox UBX protocol implementation, including a link to a short video demonstrating the functionality in the GitHub pull-request post.

The solution should minimally parse from UBX all in EdgeTX currently supported fields that are parsed from NMEA, such as: 

* latitude  
* longitude  
* altitude  
* HDOP  
* number of satellites  
* lock status  
* speed  
* heading  
* date  
* time  

See for reference

[https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/gps.h#L27-L39](https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/gps.h#L27-L39)


[https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/gps.cpp](https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/gps.cpp)


[https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/lua/api_general.cpp#L1372-L1408](https://github.com/EdgeTX/edgetx/blob/3807d7759b58746ab54e230b7cd147c9eecda98c/radio/src/lua/api_general.cpp#L1372-L1408)
(doc here: [https://luadoc.edgetx.org/part_iii_-_opentx_lua_api_reference/general-functions-less-than-greater-than-luadoc-begin-general/gettxgps](https://luadoc.edgetx.org/part_iii_-_opentx_lua_api_reference/general-functions-less-than-greater-than-luadoc-begin-general/gettxgps) )


On color radios, following widget should continue to work: [https://github.com/EdgeTX/edgetx-sdcard/tree/master/sdcard/c480x272/WIDGETS/TxGPStest](https://github.com/EdgeTX/edgetx-sdcard/tree/master/sdcard/c480x272/WIDGETS/TxGPStest) and RTC clock sync should also continue to work with UBX GPS communication protocol.


***--Hints--***

Check out: [https://github.com/betaflight/betaflight/blob/master/src/main/io/gps.c](https://github.com/betaflight/betaflight/blob/master/src/main/io/gps.c) for tips how this could be solved. 

The following doc could also be interesting from page 63: [https://www.yumpu.com/en/document/read/5138505/ubx-protocol](https://www.yumpu.com/en/document/read/5138505/ubx-protocol)


**Prize:**

[RadioMaster TX16S Mark II MAX](https://www.radiomasterrc.com/products/tx16s-mark-ii-max-radio-controller) radio (sponsored by RadioMaster). The radio will be shipped world-wide free of charge directly from the RadioMaster factory to the winner.

***Note:*** the contest winner will need to cover all import/customs fees for the prize. However, those fees will be re-imbursed by the EdgeTX via expense submission to the [EdgeTX Open Collective](https://opencollective.com/edgetx/expenses/new).


**Contest ends after first successful submission or on 30 September 2024**


**If you have questions about the contest, feel free to contact the EdgeTX team on our discord at the [#ubx-contest channel](https://discord.com/channels/839849772864503828/1210916167976361984)**



## **Special thanks to our contest sponsor for their prize donation and helping to make this contest possible:**

<p></p> 
<p align="center">
<a href="https://www.radiomasterrc.com/" target="_blank"><img src="/assets/RadioMasterLogo.png?raw=true" align="center" width="270"></a>
</P>


***The EdgeTX PSC team reserves the right not to accept submissions that work incorrectly and / or may negatively impact other parts of the EdgeTX system.***

 








