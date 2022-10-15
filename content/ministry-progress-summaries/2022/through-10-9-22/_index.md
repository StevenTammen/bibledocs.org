---
title: Through 10/9/22
weight: 30
layout: content-page
---

{{< subjects >}}

{{< /subjects >}}

{{% section-navigation %}}

## Video {#video}

{{% video
src="https://www.youtube.com/embed/HpKO1ZHIzPQ"

playlist="https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb"

video=""

audio=""

slides="https://www.bibledocs.org/slides/ministry-progress-summaries/2022/through-10-9-22/"
%}}

## Summary {#summary}

This cycle was dominated by two primary areas: tech research and setup, and coding support for discussion pages.

On the tech side of things, I did research, bought, and started setting up several different things. A stenomask and voice recognition software to be able to dictate prose at high speeds, a separate wireless lapel mic system to use for content recordings and live presentations, and a portable monitor setup for working on-the-go, so that I can perhaps work in a local public library on the weekends, as sometimes I find that working in a public place can help me focus better.

Aside from all that, the biggest task knocked out this cycle was coding support for discussion pages in the Python preprocessor application for static sites that I've been developing over the last few months. This was a large coding effort, taking me many days. But I'm very glad to have it behind me now, so that it will no longer be hanging over my head.

## Timestamps {#timestamps}

[00:00](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=0s) - Introduction  
[04:54](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=294s) - Outline  
[06:34](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=394s) - Did lots, lots more computer setup stuff, including things related to the video recording workflow  
[08:10](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=490s) - Researched, ordered, and started to set up things related to voice recognition  
[13:45](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=825s) - Researched and ordered a better mic setup for making content videos  
[16:33](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=993s) - Researched, ordered, and planned out a portable computer setup to work at a local public library on weekends  
[18:40](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1120s) - Pondered the multi-website future that is coming  
[21:44](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1304s) - Misc. discussions from the ministry community  
[26:34](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1594s) - Modified the preprocessor Python application to support discussion pages  
[32:42](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1962s) - Upcoming work  
[35:40](https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2140s) - Outro  

{{% content %}}

## Content {#content}

<!-- --- -->

### Did lots, lots more computer setup stuff, including things related to the video recording workflow {#did-lots-lots-more-computer-setup-stuff-including-things-related-to-the-video-recording-workflow}

- Set up SSH keypair on new computer, added it to GitHub, SourceTree, DigitalOcean
- Installed Snagit. Set TV monitor to run at 4K (but upscale text so that text size doesn't change much). So that Snagit recordings will be at much higher resolution, and hopefully webcam footage will be much clearer/sharper than it has been. Toggle off reduce-to-1080p Snagit setting
- Made new GoPro video profiles to shoot in 4K, linear mode, without video stabilization. Hopefully better color balance too.
- Set up Python 3 on new computer, built new local virtual environments
- Set up properly ignoring .git/, .venv/ folders in project repos on new computer. There's a specific DropBox command to run
- Installed Auto-Editor in the global Python environment via `pip`
- Removed OneDrive-related folders on Windows 11, cleaning up after its sloppy uninstaller. Boo.
- Debugged framerate matters (converting variable framerate to constant framerate, and how it impacts editing/video concatenation). Also some audio bugs in concatenating video fragments.
- Moved all ~440 GB of videos that were being stored on a backup hard drive onto the new desktop computer, and started backing up with DropBox too. Will try to upload much of the backlog to YouTube in the near-ish future to reclaim the space. It took a while for Dropbox to sync all this, given my relatively slow ~10 Mbps internet upload speed
- Set up Cold Turkey on the new computer, and adjusted automated lockout times across both the new computer and the old computer.
- Imported phrase express phrase list to match the old computer's list. Computer access restrictions are now set up completely. Helps me better stay on-task and better maintain a consistent sleep schedule.

<!-- --- -->

### Researched, ordered, and started to set up things related to voice recognition {#researched-ordered-and-started-to-set-up-things-related-to-voice-recognition}

- I bought a stenomask, specifically a wireless model called the [Privo](https://talktech.com/shop/stenomask-store/privo-wireless/). This is the microphone I will be using when interacting with my computer via voice recognition.
- Once the mic came (and I had tested it out and gotten comfortable using it), I bought voice recognition software called [Dragon](https://www.nuance.com/dragon/business-solutions/dragon-professional-individual.html), downloaded and installed it, and followed a couple [excellent tutorial videos](https://www.youtube.com/playlist?list=PLOJQA3XA9IBsygttlHqROgk1ZGSRFLrY3) to get the initial setup completed (user profiles, etc.)
- Spent time playing around with Dragon, and testing out dictation. Right out of the box, I can already dictate quite quickly, with good accuracy.
- Verified it will play nice with AutoHotkey. It seems to! Hurray!
- Tested out what things are and are not supported in dictation mode alone. Punctuation, new line, and new paragraph all are, which is mainly what I wanted to verify.
- Spent a long time figuring out some final aspects of my keyboard layout design (on one of the custom movement layers), now that I have a better feel for how the voice recognition works, and where its functional holes are.
- After getting the hang of adding vocabulary entries to Dragon, added some initial entries for making things bold, making things italic, making things both bold and italic, and then some core punctuation (period, comma, question mark, exclamation mark). I'll be adding more custom stuff over time, to increase the speed at which I can dictate by eliminating ambiguity for the recognition engine.
- I still have plenty more punctuation and stuff to figure out, but this was a good start.

<!-- --- -->

### Researched and ordered a better mic setup for making content videos {#researched-and-ordered-a-better-mic-setup-for-making-content-videos}

After some research, I also bought a different mic system, both for when I'm recording content videos, and presenting live. It's called the Rode Wireless Go II.

* Dual-channel wireless mic receiver, two transmitters
* High quality lapel mic
* An accessory that lets you turn the wireless transmitter (that has a built-in omnidirectional microphone) into a hand-held mic. I'll use this for questions when presenting live.
* [Amazon.com: Rode Wireless GO II Dual Channel Wireless Microphone System](https://www.amazon.com/gp/product/B08XFQ6KP9/)
* [Amazon.com: Rode Lavalier GO Professional Wearable Microphone](https://www.amazon.com/gp/product/B07WM65GTF/?th=1)
* [Amazon.com: Rode Interview GO Handheld Adaptor for Wireless GO](https://www.amazon.com/gp/product/B086YXCDYC/)

I've been busy so I haven't set up and tested these things yet, but I will soon.

<!-- --- -->

### Researched, ordered, and planned out a portable computer setup to work at a local public library on weekends {#researched-ordered-and-planned-out-a-portable-computer-setup-to-work-at-a-local-public-library-on-weekends}

Well, first off, I went to my local library, got a library card, and walked around to get myself familiar with it. I also got my devices connected to the wifi there, and so on.

I know from my experiences in college that it is sometimes easier for me to stay on-task when I work in public places, and with that in mind, I set out to be able to bring a multi-monitor setup with me when I go to work in the library (which will probably primarily be on Saturdays and Sundays).

The setup I decided on (to be used in addition to, at the time being, my tablet, Bluetooth mechanical keyboard, wireless trackball, and Bluetooth noise-cancelling headphones):

* [2x Folding monitor stands](https://www.amazon.com/Wearson-WS-03A-Adjustable-Folding-100x100mm/dp/B00XUF2GBI)
* [2x Quick-release Vesa adapter plates](https://www.amazon.com/VIVO-Attachment-Removable-Mounting-STAND-VAD2/dp/B01BTAAUV8/)
* [2x 24" Monitors](https://www.amazon.com/gp/product/B092XF3W9T/)
* [A padded monitor carrying case than can haul two 24" monitors](https://www.amazon.com/Trunab-Carrying-Compatible-Computer-Accessories/dp/B096V6H4GC)
* [A USB docking station to get additional HDMI connections to support the monitors](https://www.amazon.com/Docking-Station-Adapter-Monitors-Compatible/dp/B08R9WZKFN/)

All this was pretty expensive when taken together, but I have high hopes for this setup. I think it is rather clever, and ought to work very well.

<!-- --- -->

### Pondered the multi-website future that is coming {#pondered-the-multi-website-future-that-is-coming}

I helped my roommate come up with ideas for his ministry website's domain name. I sent him a list of suggestions from my past research, and he used one of those. I also helped him register it with a domain name registrar.

This got me thinking a bit about the next steps I will need to take to get my website theme in the state it needs to be in to be shared across multiple websites. Both this one I'm helping my roommate set up, and my own other planned websites (personal, and business-focused). I probably ought to make this theme organization stuff happen sooner rather than later. Some of the things I was thinking about here were related to combining all of the CSS into one file, and then making it SCSS to be able to use variables for accent colors and so on.

<!-- --- -->

### Misc. discussions from the ministry community {#misc-discussions-from-the-ministry-community}

Several of us in the community had a long discussion about cryptocurrencies, investing, and what our attitudes towards these things ought to be as Christians.

One of the Bible studies on Saturday afternoons turned into a discussion of apologetics approaches. One of the folks in our community has an atheist friend he is trying to send good reading materials to, and the question was how to best do all this. The atheist friend is very much on the scientific/philosophical side of things, a super-logical sort of person. It is my opinion that most apologetics resources end up being too lightweight and airy-fairy to be convincing for very smart people (my friend had initially asked for book suggestions to have his intellectually-inclined friend read), so we talked a bunch about what then, if not actual book suggestions.

After much discussion on the call, I scrounged up a bunch of links for this friend who is involved with this other guy. I went with links regarding the mind body problem, critiques of logical positivism and prevailing oversimplistic views regarding philosophy of science (at least from a strict materialist perspective), and so on. I did a lot of research myself since I found the topics and arguments here interesting.

<!-- --- -->

### Modified the preprocessor Python application to support discussion pages {#modified-the-preprocessor-python-application-to-support-discussion-pages}

Knocking out this coding got me a good bit of the way towards finishing Phase II in my plan of attack, which I'm happy about.

- The first thing I did was take stock of all I needed to do, and then I came up with with a plan of attack -- getting the tasks written down in a list and roughly sequencing them.
- After that, I powered through it. It was probably a solid 20 hours of coding (lots of debugging during the refactor), so I wasn't wrong to have been dreading it some. Hopefully, this will be one of the last big functional coding efforts I'll have to drag myself through, at least for a while. Although this preprocessor app is in need of better error handling, general refactoring to make the codebase cleaner and more organized, documentation... etc. Sigh. Some day.
- After validating that everything worked properly with some fake test content, I organized everything for the first discussion video in the SR4 series, and then replaced the test content with that. You can have a look at it [here](https://www.bibledocs.org/longer-topical-studies/ichthys-sr4-satans-world-system/introduction-to-sr4-satans-world-system/level-of-depth-calling-many-deceived-too-harsh-why-god-allows-satan-control/). Note that it also shows up on the related [content page](https://www.bibledocs.org/longer-topical-studies/ichthys-sr4-satans-world-system/introduction-to-sr4-satans-world-system/), and [aggregation page](https://www.bibledocs.org/longer-topical-studies/ichthys-sr4-satans-world-system/) too. The UX is slightly different in each case, according to what I think makes the most sense.
- Then I checked over everything and pushed it all live on the site.

Just to get a sense of the scale here, [this](https://github.com/StevenTammen/bibledocs.org/commit/ef31f39ab0ecb49811050ff86800772f77b840ac) is the big-bang commit for the website-related changes related to this effort to refactoring to support discussion pages.

I've been lazy and haven't been committing as consistently in the preprocessor repo (among other reasons, just because I know it's not really ready for public use anyway, so it doesn't matter too much at the moment), so I can't presently show the changes there in the same way. But it was a really big changeset spanning across many files.

<!-- --- -->

### Upcoming work {#upcoming-work}

- Write up documentation on the content organization page about discussion pages
- Get all videos/audio recordings uploaded to Archive.org for all the relevant recent videos
  - Shorter ministry intro video
  - Longer ministry intro video
  - BB6A first focused video
  - SR4 video 1 Introduction
  - SR4 video 2 Adam and Eve
  - All ministry progress summary videos
  - Etc.
- Organize all the remaining videos in the SR4 series. This is the other big thing I need to finish before I'll be done with Phase II in my plan.
- Set up the Rode Wireless Go II microphone system, and test it thoroughly
- Continue making progress on the voice recognition front

{{% /content %}}

{{% transcript %}}

## Video/audio transcript {#video-audio-transcript}


{{% /transcript %}}

{{% section-navigation %}}