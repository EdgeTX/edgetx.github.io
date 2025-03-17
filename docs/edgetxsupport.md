---
hide:
  - toc
---


##How radio manufacturers can get a version of EdgeTX for their new radio hardware.

If you are a radio manufacturer and are interested in using EdgeTX as the firmware for your radio, there are several ways to achieve this. Under the open-source GPL, anyone can use EdgeTX or create a modified version of EdgeTX to use. The only stipulation is that the source code for the ***modified version*** of EdgeTX ***must*** be ***made available*** for everyone to see and use.

**There are several ways to can get a version of EdgeTX that supports your new radio hardware:**

1. **Develop and Maintain your own fork of EdgeTX**
   
   - Create your own fork of EdgeTX and make the needed changes to support your hardware yourself and publish it yourself (keeping in mind that your new fork must be made available for others to use.).
   
   - ***In this case, you are responsible for the maintenance and bug fixing of your firmware.*** 
   
   - ***Note**: in order to prevent confusion by the users, you **must not** refer to the software as EdgeTX, but rather “a custom branch of EdgeTX v2.4.x”.  Additionally, you **must not** use the EdgeTX logo for product marketing or packaging.*

2. **Develop the support of your hardware yourself and get it merged to EdgeTX code base**
   
   - Make the needed changes to support your hardware yourself, submit a pull request to the EdgeTX team for review.  If approved, your changes will be merged into the main branch of EdgeTX where it will be published and distributed as part of the normal release schedule.
   
   - The new radio will be added to our list of supported radios after the merge.
   
   - Future development of new features and bug fixes will include all the supported radios for consideration.
   
   - Manufacturers are highly encouraged to participate in testing, and bugs fixing to ensure our continuous development will not break the firmware of your radios.
   
   - If you do not have the know-how or resources to make the needed changes to support your hardware yourself, then you can contact the EdgeTX Team to get some assistance to give you some references, or try to outsource the development to third party who understand the EdgeTX code base. 

3. **Co-develop the hardware and firmware with EdgeTX Team**
   
   - If your new radio is interesting enough (e.g. new hardware platform, new hardware features, etc.), and you can find one or more EdgeTX teamates who feel interested to closely work with you for the new development, this maybe a good choice, try reach out to us either on [Discord](https://discord.gg/wF9wUKnZ6H) or via email at psc@edgetx.org
   
   - ***Note**: The EdgeTX Team develops the EdgeTX firmware as a hobby, and usually new hardware with interesting features can easily draws our attention, but because we do the development with our spare time, we cannot promise when the development can be finished.  If manufacturer concerns about the progress of the development, it is highly recommended to put in your own effort to speed up the pace.*

We highly encourage all manufactures that are planning to produce a radio transmitter that will use EdgeTX to contact the EdgeTX PSC for collabaration early on. This will allow our experts to give you advice to ensure that your product will perform as expected with EdgeTX.

All manufacturers that are using EdgeTX are encouraged to participate in the EdgeTX partnership program.  Under this program, hardware-specific features and bug fixes will be completed on a priority basis by the EdgeTX Team. More information about the benefits and requirements of the partnership program can be seen here: [EdgeTX partnership program.](partnershipprogram.md)

