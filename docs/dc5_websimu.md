---
hide:
  - navigation
  - toc
---

<p></p> 
<p align="center">
<a><img src="/assets/dc5_poster.jpg?raw=true" align="center" width="497"></a>
</P>

## **Contest Details**

**Task:**

Be the first developer to make a mergeable pull-request (PR) against EdgeTX main GitHub repository with a fully working web based EdgeTX radio firmware simulator.

See an existing pull-request (PR) at [EdgeTX GitHub PR#5940](https://github.com/EdgeTX/edgetx/pull/5940) as a proof-of-concept (PoC) rewrite of `simu` that relies on SDL2, [ImGui](https://github.com/ocornut/imgui) and [emscripten](https://emscripten.org/) to provide a very simple simulation that runs in a browser. The developer competition entry should minimally improve upon the basic PoC as stated below.

The existing PoC does not really make use of any specific JavaScript (JS) code apart from the code injected by `emscripten`. This means that basically everything is drawn via SDL code in the C/C++ code base (mainly `targets/simu/sdl_simu.cpp`).

Because of the way web browsers handle file systems, the PoC does not have any support for using existing any SD card image or even model files. It should be however possible to use [browser-fs-access](https://github.com/GoogleChromeLabs/browser-fs-access) to offer that feature in a browser independent way.

The current layout of the application is controlled solely from C/C++ code via ImGui layout. Ideally, this code would be moved to JS in the web page, thus opening a way to use simple CSS to customize the visual appearance. It would also allow to have a much nicer and more flexible layout using today's browser capabilities.

In general, exporting the functions allowing for generic handling of controls (switches, pots, etc.) should allow the simulator libraries to become more generic and remove dependencies on things like ImGui and SDL altogether.

The same applies to the simulator libraries used by Companion. As of now, these libraries are based on Qt code embedded in the libraries, which make it difficult to use in other context, and requires Qt to be included in Docker images used to build firmwares and simulator libraries.

Ideally, the WASM simulator component should be only responsible for running the firmware as such, and write into a simple byte buffer when refreshing the screen, triggered directly by the JS code.

**Prize:**

[Flysky Elysium EL18 radio](https://www.flysky-cn.com/el18description) with a [Flysky FRM303 Module (Carefree edition)](https://www.flysky-cn.com/frm303description) (sponsored by Flysky). The combo set will be shipped world-wide (see next sentence for limitations!) free of charge directly from the Flysky factory to the winner. Due to current geo-political situation, the prizes cannot be shipped to regions affected by war or other objective circumstances where logistics cannot deliver them. For detailed information about the limitations, please contact [Flysky](mailto:flyskyrc@flysky-cn.net). EdgeTX would cover any possible local import fees (the winner of this competition can hand in the possible import fee bill via our [OpenCollective page](https://opencollective.com/edgetx/expenses/new)).


**Rules**

To be eligible to win the radio, an address of a 18+ years old person is required. Entries from anyone, who has previously won an EdgeTX developer contest, will be accepted earliest on April 1st, 2025. Members of the <a href="https://edgetx.org/bylaws/#edgetx-development-team">EdgeTX development team</a> cannot participate in the competition.

The contests ends after first successful submission, or on midnight of April 30th, 2025 GMT.

The EdgeTX PSC reserves the right not to accept submissions that work incorrectly and / or may negatively impact other parts of the EdgeTX system. The decision of the winner by EdgeTX PSC is final and legal recourse is excluded.


**If you have questions about the contest, feel free to contact the EdgeTX team on our discord at the [#dc5_websimu](https://discord.com/channels/839849772864503828/1343989454464876604) channel**


## **Special thanks to our contest sponsor for their prize donation and helping to make this contest possible:**

<p></p> 
<p align="center">
<a href="https://www.flysky-cn.com/" target="_blank"><img src="/assets/FlySkyGold.png?raw=true" align="center" width="344"></a>
</p>
