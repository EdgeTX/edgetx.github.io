---
hide:
  - toc
---


##How radio manufacturers can get a version of EdgeTX for their new radio hardware.

If you are a radio manufacturer and are interested in using EdgeTX as the firmware for your radio, there are several ways to achieve this. Under the open-source GPL, anyone can use EdgeTX or create a modified version of EdgeTX to use. The only stipulation is that the source code for the ***modified version*** of EdgeTX ***must*** be ***made available*** for everyone to see and use.

**There are several ways to can get a version of EdgeTX that supports your new radio hardware:**

1. **Develop the support of your hardware yourself and get it merged to EdgeTX code base**
   
   - Make the needed changes to support your hardware yourself, submit a pull request to the EdgeTX team for review.  If approved, your changes will be merged into the main branch of EdgeTX where it will be published and distributed as part of the normal release schedule.
   
   - The new radio will be added to our list of supported radios after the merge.
   
   - Future development of new features and bug fixes will include all the supported radios for consideration.
   
   - Manufacturers are highly encouraged to participate in testing, and bugs fixing to ensure our continuous development will not break the firmware of your radios.
   
   - If you do not have the know-how or resources to make the needed changes to support your hardware yourself, then you can contact the EdgeTX Team to get some assistance to give you some references, or try to outsource the development to third party who understand the EdgeTX code base. 

2. **Co-develop the hardware and firmware with EdgeTX Team**

   - If your radio introduces novel features (e.g., a new hardware platform and/or new hardware capabilities) and you managed to draw the interest from one or more EdgeTX team members, co-development may be viable. Try reach out via [Discord](https://discord.gg/wF9wUKnZ6H) or via email at psc@edgetx.org for your proposal.
   
   - ***Note**: EdgeTX is developed by volunteers, and while innovative hardware often attracts attention, progress depends on contributors’ availability. Manufacturers concerned about timelines should allocate internal resources to accelerate development.*

3. **Develop and Maintain your own fork of EdgeTX**
   
   - Create your own fork of EdgeTX and implement hardware-specific modifications independently. (Please ensure the fork remains publicly available)
   
   - ***In this case, your team assumes full responsibility for long-term maintenance and bug fixes.*** 
   
   - ***Note**: To avoid user confusion, **always label** your software as a "custom branch of EdgeTX vx.x.x" (**never** "EdgeTX"). Commercial use of the EdgeTX logo is strictly prohibited.*

We strongly encourage all manufacturers planning to produce EdgeTX-compatible radio transmitters to contact the EdgeTX Project Steering Committee (PSC) early for collaboration. This allows our experts to advise on optimizing your product for EdgeTX compatibility.  

All manufacturers that are using EdgeTX are encouraged to participate in the EdgeTX partnership program.  Under this program, hardware-specific features and bug fixes will be completed on a priority basis by the EdgeTX Team. More information about the benefits and requirements of the partnership program can be seen here: [EdgeTX partnership program.](partnershipprogram.md)

