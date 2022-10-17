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

<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=0">0:00</a> - hey guys so right now I'm going to be recording the ministry progress summary video here uh through October 9th 2022<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=7">0:07</a> - and so as you may have noticed I have a little bit of a change in location here so it's kind of funny I actually decided<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=14">0:14</a> - to try recording uh most of the videos here in the bathroom here in the master uh just because I've had issues with the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=20">0:20</a> - lighting in the office that I've been working in now I could uh you know use the GoPro in a room that's better lit by<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=27">0:27</a> - outside light but then I can only record videos when it's bright outside and you know if I'm at work a lot of the work<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=34">0:34</a> - day then I'd use some stuff in the early evening like working out eating dinner well by the time I'm ready to maybe<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=39">0:39</a> - record videos and evenings already dark outside and you know if I get up in the morning to work sometimes it's not<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=45">0:45</a> - always completely light and so I like this idea of being kind of independent from outside light and to do that that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=50">0:50</a> - means that I have to have good inside light now there is a pretty well lit spot in the kitchen in the house but the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=56">0:56</a> - problem with that is that I do have a roommate and so if I I'm recording a video I you know it kind of means my<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=63">1:03</a> - roommate can't you know he can't be moving around the house as much and it kind of interferes with other people's stuff and you know especially later on<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=70">1:10</a> - maybe if we get another person that's living in the house that's not really sustainable and so I kind of need a room where I can<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=76">1:16</a> - close off the door and uh you know have a nice quiet environment for me to record that also has really good<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=82">1:22</a> - lighting because lighting is one of the main drivers here of the video quality and so I spent some time today trying to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=88">1:28</a> - figure out where I was going to do this and it's a little bit funny you know you can see the bathtub in the background<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=93">1:33</a> - here but this is actually probably one of the best split spots in the house you know I have two overhead panels of the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=101">1:41</a> - lights in front of the mirrors here and so I have nice good light in front of me which means that you know I'm not like<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=107">1:47</a> - cast out or anything and you know I have uh the video settings uh dialed quite a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=113">1:53</a> - bit more in here I spent some time earlier this evening fiddling around just because I haven't been very happy with the quality of the videos I mean I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=119">1:59</a> - know it's not been like a huge deal for me because you know most of the time it's just me recording the screen anyway but I wanted to increase video quality<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=126">2:06</a> - especially as I start getting into more Production videos and so this was uh kind of the compromise I came up with<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=131">2:11</a> - now if I wanted to spend extra money I could probably get like a diffuse light thing you know people who who do stuff<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=138">2:18</a> - at like photo studios and stuff they'll have these like oh what's the right thing I mean it's kind of like this uh reflective silver<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=145">2:25</a> - material that they'll use for like uh diffuse lighting for uh photos and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=151">2:31</a> - videos and that sort of thing would definitely help uh with the uh the lighting in the office and I have been<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=157">2:37</a> - shooting stuff and then I could keep recording the office but you know it costs a lot of money and it's kind of a hassle and you know I don't if I don't<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=164">2:44</a> - need to buy the extra stuff I want to buy the extra stuff you know and it's not like my bathroom is ugly or anything so you'll just get to probably see here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=171">2:51</a> - for the foreseeable future you'll see the the blackout curtain there in the bathtub and everything and uh nothing so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=176">2:56</a> - wrong with this really um this is just kind of what I've decided on here in the interim because the lighting is much better and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=183">3:03</a> - hopefully that means that the video is a lot clearer we don't have any graininess from uh kind of the iso being set too<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=189">3:09</a> - high or a low light you know GoPros do not uh have a very big image sensor and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=194">3:14</a> - so that's been one of the reasons why it's been struggling in the light conditions here but now I have the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=199">3:19</a> - shutter speed set reasonably low the iso cap out at 400 and I'm in a much better lit room and so I really think that this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=206">3:26</a> - should help the video quality a lot so I'll stop rambling about that anyone who's interested in video stuff maybe can feel my pain a little bit but this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=212">3:32</a> - is kind of what I've decided upon as the better late room in my house and so that's why I'm here recording a video in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=217">3:37</a> - the bathroom um all right so with that out of the way we'll go ahead and get started for uh<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=222">3:42</a> - the stuff for this couple weeks uh progress while grammar uh for the things<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=228">3:48</a> - that I've gotten done the last couple weeks um so this ministry progress summary is through October 9th and so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=233">3:53</a> - that was actually a couple days back um I'll hop into the summary here oops I actually cut off the recording<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=239">3:59</a> - there um I will hop into the slides now uh rather than pausing the recording<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=246">4:06</a> - um and so I was actually going to record this a bit earlier but I had to Edge my yard I was not very interesting<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=251">4:11</a> - ministry-wise but I hadn't edged it before since I moved into the house and I finally got an edger and it took me a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=258">4:18</a> - lot longer than I thought it would and so I was very tired after that and didn't particularly feel like recording<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=263">4:23</a> - a video and so that's why this is a a couple days light here um and so we are going to be going stuff<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=269">4:29</a> - through October 9th and you see it's the 12th so all a little bit behind here so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=274">4:34</a> - this particular cycle here was dominated by a couple primary areas uh mainly<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=280">4:40</a> - setting up some additional Tech stuff so uh microphones and things like that and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=285">4:45</a> - uh that will come for future content recording as well as voice recognition stuff we'll get to that and then as well<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=292">4:52</a> - as me coding support for discussion pages in the preprocessor application so we'll go through all of this the tech<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=298">4:58</a> - related setup stuff here I had a bunch more stuff that I had to do getting my new computer the new desktop computer I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=304">5:04</a> - have set up with everything and uh and I'll kind of go through that real rapid fire and then these are the other Tech<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=310">5:10</a> - things that I set up a steno mask here for voice recognition and the voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=315">5:15</a> - recognition software itself some configuration there initially just testing it out getting used to it a bit<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=322">5:22</a> - and then another microphone here so I'm still recording with my wired lapel mic here but I did get a wireless system<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=328">5:28</a> - that I will set up for a kind of better content recording when I'm making these content videos as well as when I'm<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=335">5:35</a> - presenting live I'll go over that and then kind of a portable computer setup<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=340">5:40</a> - to work when I'm at a local public library on weekends and so part of the idea here is getting out of the house in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=347">5:47</a> - a public place sometimes help me helps me focus a bit better and so one of the problems with that though is if I'm on<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=353">5:53</a> - my on my puny little tablet screen I don't have as much screen real estate to work with and so I tried to figure out a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=359">5:59</a> - way to get around this and my solution was I bought two 24-inch monitors as well as like folding monitor stands and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=365">6:05</a> - quick release mounts for the monitors and uh I have yet to test this out but I did a lot of research and I'm pretty<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=371">6:11</a> - psyched about how it might work and then we'll go over the other stuff uh the big primary thing here being<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=377">6:17</a> - modifying the python application on the code side of things so not a terribly interesting a couple set of weeks here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=384">6:24</a> - for like forward progress content wise uh but we're still getting everything set up here so that I can kind of play<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=391">6:31</a> - the long game and hopefully increase the throughput quite a bit in a sustainable way in the long term so uh I'm not even<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=398">6:38</a> - sure if I'm going to read through all of this anyone who's really interested can certainly take a look at this slide here for all of the computer stuff that I had<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=405">6:45</a> - to do I had to set up SSH keys on the new computer this is video configuration stuff video configuration stuff I just<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=412">6:52</a> - mentioned some of the stuff that I've done there um you know this is setting up the new video modes I had to set up python on the new computer properly<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=419">6:59</a> - ignore stuff in Dropbox so it's not syncing like the Version Control files and the virtual environment that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=425">7:05</a> - contains python packages installing the video editing software on the new computer<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=430">7:10</a> - um uh this frame rate stuff this was kind of interesting uh the screen recording<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=436">7:16</a> - software that I'm using right now actually records in variable frame rate but the automatic editing program that I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=441">7:21</a> - use is kind of depends on constant frame rate and so I had to figure out how to convert between the two video editing in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=447">7:27</a> - general typically uses constant frame rate I backed up a bunch of uh The Daily Progress summary videos that I've been<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=453">7:33</a> - recording for about a year now um I have a big backlog that I need to upload eventually but I got those on the new<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=458">7:38</a> - computer since I have a much bigger SSD backing up the Dropbox in the cloud as well just that's a lot more secure in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=464">7:44</a> - case you know something were to happen to the backup hard drive and then set up the computer filtering stuff to kind of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=471">7:51</a> - lock myself out late at night so that I will actually go to bed at a reasonable time this is something that I've been doing for a few years now just helps me<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=478">7:58</a> - focus better if I kind of control and get my access to the computers that I use that way I can you know work when I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=485">8:05</a> - want to be working and then be off the computer when I want to be off the computer all right so I'm not going to spend too much time here you know if<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=490">8:10</a> - you're really interested in the stuff you can go read a bit more and then I did a bunch of stuff related<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=496">8:16</a> - to voice recognition so I actually have a Steno mask and it says that I ordered so I'll actually open up the link here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=503">8:23</a> - um this is a company that makes these products for voice recognition now<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=508">8:28</a> - there's nothing so unique about how the microphone in this works the thing that's really cool about it is I mean it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=514">8:34</a> - looks really dorky let me see if I can find a picture of someone using it somewhere um yeah this is what it looks like so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=520">8:40</a> - you hold it up to your face like this it kind of looks almost like the plague mask from the Black Death in history but<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=526">8:46</a> - it has this foam inside of it that blocks all of the sound that comes into it basically and so you can actually<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=534">8:54</a> - talk into this microphone if you're in a public place and someone can tell that you're making noise but it's very muffled and so it protects your privacy<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=541">9:01</a> - it also just lets you not bother other people so much um if you are using this for voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=546">9:06</a> - recognition and that's like dictating dictating Pros is primarily what I'm going to be using this and so it's expensive of course but um<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=553">9:13</a> - this is actually Wireless as well so this is the microphone that I got now the reason why it really matters which microphone you use is because the voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=560">9:20</a> - recognition algorithms uh kind of depend on becoming accustomed to your voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=565">9:25</a> - patterns and if you use a different microphone it sounds different and so I wanted to be training the voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=572">9:32</a> - recognition software and AI to be recognizing my voice when I'm talking into this because I'll be able to use<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=577">9:37</a> - this in all circumstances versus the lapel mic that I'm using right now you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=583">9:43</a> - know just talking in the privacy of my own home well it sounds a bit different I mean not super different but enough so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=589">9:49</a> - that it might throw off the accuracy of the software some so that's why I waited until this mic came then I got the voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=595">9:55</a> - recognition software itself another very expensive thing here it's called Dragon so it's made by a company called Nuance<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=601">10:01</a> - here the individual like the home license here is less expensive oh actually this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=607">10:07</a> - is this is the professional version but I wanted to edit the vocabulary and stuff related to that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=612">10:12</a> - um I would consider myself somewhat of a power user like I'm going to go script uh certain things with their scripting<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=618">10:18</a> - language I think you can use Visual Basic uh the syntax is kind of gross but if I want to be able to send key presses<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=624">10:24</a> - in a specific order or do macros and things like that you have to have the professional version to be able to do that so again maybe not going to read<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=631">10:31</a> - through all of this I did a bunch of initial setup here the short of it is that even right out of the box without a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=638">10:38</a> - lot of customization on my part it works very well I can already dictate quite quickly with good accuracy I mean it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=645">10:45</a> - misses a word every uh every once in a while now I am going to be working in coming weeks and months to integrate<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=652">10:52</a> - this with the keyboard layout design that I've been working on for years not going to spend a lot of time talking<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=657">10:57</a> - about that because it's not terribly Ministry related but it's been a personal hobby project of mine for<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=662">11:02</a> - probably about four or five years now and voice recognition has been something I've been meaning to pick up for a long time as well going to be trying to kind<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=669">11:09</a> - of integrate the two in a hybrid approach and I just haven't seen very many other people try it many people who use voice recognition full-time do it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=676">11:16</a> - because of carpal tunnel or other RSI repetitive strain injuries so they can't<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=681">11:21</a> - type so they're forced to use voice recognition many people who type just don't use voice recognition because it's kind of a hassle to set things up even<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=688">11:28</a> - though I think it has lots of advantages and it's obviously why I'm doing it so a lot of people just haven't mixed the two so most people that use voice writing<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=694">11:34</a> - only use voice writing most people who type only type and there hasn't seemed to be a lot of like cross-pollination<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=699">11:39</a> - between the two and so I'm going to try to set up a system that uses both playing to the advantages of both um so I'll get to that eventually here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=706">11:46</a> - but this was the first part I can already do a good bit of dedication I'm going to start hopefully dictating out<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=713">11:53</a> - some of like the stuff here where I'm dictating out stuff that I do every day um just to get myself accustomed to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=719">11:59</a> - using the voice recognition in place of typing because it is much much faster as I say even though the accuracy I'm still<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=725">12:05</a> - working on some stuff to a better increase the usability of this long term you're removing some of the ambiguity<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=731">12:11</a> - for the voice recognition engine here just by making my own briefs for things like punctuation because if you say the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=739">12:19</a> - word period period is a valid word in English like the period of a pendulum swing or a period period of time so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=745">12:25</a> - that's ambiguous between whether you want those words or the punctuation mark So if I make my own uh text brief for<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=752">12:32</a> - the punctuation mark I say something different that like a nonsense word that signifies period then I won't have<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=757">12:37</a> - ambiguity anymore um so things like that will help increase the speed in which I can dictate without ambiguity so I have a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=766">12:46</a> - lot more setup ahead of me here at least to make it work the way that I think will be ideal but I'm getting the hang<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=771">12:51</a> - of it and this is exciting because you know this is part of phase three technically in that plan that I've gone<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=776">12:56</a> - over in the last Ministry progress summary but being able to start dictating things at this high speed you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=783">13:03</a> - know ballpark 200 words per minute rather than my typing speed which is even if I'm touch typing on my custom<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=789">13:09</a> - layout it's only about 75 which is not that slow there are people who can touch type closer to 100 120 even those are<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=796">13:16</a> - the very exceptional people but 200 is still a lot faster and so being able to do that will just mean that I can get<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=803">13:23</a> - more or things generated on the content side here so that's the voice recognition this was<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=808">13:28</a> - one piece of technology that I was working on setting up here so the Steno mask getting that mic specific for the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=814">13:34</a> - voice recognition so that I can start creating the audio profile and the voice recognition software that will recognize<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=820">13:40</a> - my voice coming through this mic specifically and then getting the software set up and familiaromizing<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=826">13:46</a> - myself with all of its features and stuff I ordered a separate microphone this one's different um so the microphone that I'm using<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=832">13:52</a> - right now is a wired lapel mic that I have plugged into the GoPro I wanted a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=837">13:57</a> - wireless version um so it's not such a big deal when I'm just sitting here recording stuff but um I would like to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=843">14:03</a> - make product reviews and things a separate personal YouTube channel not the ministry stuff so much but being<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=848">14:08</a> - able to have a microphone that doesn't tether me so much to the camera itself will give me a lot more flexibility when I'm shooting video if I'm outside and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=855">14:15</a> - you know on a bike or things like that it just give me a lot more power as well as the wireless just being more<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=861">14:21</a> - convenient generally and so I did a bunch of research I found this cool wire this microphone system is made by a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=868">14:28</a> - company called rode so this is the mic itself you have a receiver and then two<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=873">14:33</a> - transmitters here and then I bought a lapel mic from the same company that plugs into one of the transmitters and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=879">14:39</a> - then also an adapter thing this is pretty cool this is for once we start having the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=885">14:45</a> - live Bible studies this is not a terribly interesting picture of it let me see if there's any pictures down in the reviews<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=891">14:51</a> - um so yeah this is what it looks like I mean it's got the uh the sibilant and the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=897">14:57</a> - plosive filter there um it just looks like a kind of a studio mic thing here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=902">15:02</a> - um but this is handheld wireless and so people can pass this around if they have questions once we do the live<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=908">15:08</a> - presentations we won't be recording those because it kind of disincentivizes people from talking but we will be doing<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=914">15:14</a> - those live uh like integrated with a zoom call and so having the mic that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=919">15:19</a> - people can use to ask questions because this is a dual Channel wireless system uh means that I'll have the lapel mic<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=925">15:25</a> - that I can use for when I am talking you know like through the study content and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=931">15:31</a> - then if people have questions they can pass around that other mic and that way you know people will ask questions one at a time of course it's not so much of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=938">15:38</a> - a conversation as it is uh the question and answer part of that and so that's the system here for generating content<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=944">15:44</a> - like I am right now as well as the live presentations I have not actually set all this up yet it's still in the boxes well it came earlier last week but once<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=952">15:52</a> - I get some time I'm going to be be experimenting with all of this there's no reason why it shouldn't work on this one actually plugs into 3.5 millimeter<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=958">15:58</a> - rather than USB which is why it can be used on the GoPro but pretty excited about the audio here it's got very good<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=964">16:04</a> - audio quality and I did my research again kind of expensive so I'm uh spending some funds here hopefully to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=970">16:10</a> - set up the audio in the video uh much better and more sustainably for the long term here but to do that got you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=976">16:16</a> - research you do have to spend you do kind of get what you pay for and I have come to that conclusion after reading a lot of reviews and stuff that uh if I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=984">16:24</a> - want to kind of uh have the highest quality that I can you do kind of need<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=990">16:30</a> - to spend some money to get quality gear for that purpose and so it's kind of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=995">16:35</a> - what I was here so that's another microphone thing and then this is the portable computer setup I'm not going to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1000">16:40</a> - spend too much time talking about this because it really is basically just like having two 24-inch monitors and uh the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1008">16:48</a> - catch here is that the setup is completely portable I mean this is like the bad thing that I'm going to transport the monitors in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1014">16:54</a> - um so it you know you can see like this is the size of a person it is not tiny but this is something that I can just<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1020">17:00</a> - toss in my car and then carry in with me if I go somewhere like working at a coffee shop or the library or something<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1026">17:06</a> - um and so uh the basically the thing that lets all of this work is that there<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1031">17:11</a> - are folding monitor stands and those look like this and so you know they fold flat more or less which means you can<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1038">17:18</a> - just toss them in a backpack and then there are these uh Visa Mount adapters here these are like quick release or<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1045">17:25</a> - there's like a tab thing at the bottom and you just press the tab and then you can slide the monitors in and out more<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1051">17:31</a> - or less instantly like this and so with this thing coupled I should be able to set up both of the 24 inch monitors in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1058">17:38</a> - under a couple minutes and so that makes it more or less truly portable and then of course having two 24-inch monitors<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1064">17:44</a> - plus my tablet screen gives me a lot more real estate to work with when I'm on the go and so this is not portable in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1071">17:51</a> - the sense that people think of like I don't know MacBook airs as being portable you know this will be very heavy not like terribly heavy but you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1077">17:57</a> - know certainly more than 10 pounds probably all said and done and uh you know I've got to carry my I mean I am<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1083">18:03</a> - kind of a nerdy person and so I have a mechanical keyboard and a trackball that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1088">18:08</a> - I use and the noise canceling headphones and the holes I already had all that so this was specifically setting up the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1094">18:14</a> - portable monitor so and also not rambling about the technology I'm guessing most people aren't super interested in all this but all of these<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1100">18:20</a> - things are with that goal of me being able this is me being able to be more productive work in public places you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1105">18:25</a> - know switch it up a bit so that I'm not always just sitting at my house when I'm doing work on the ministry stuff and then the microphone stuff this is for<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1112">18:32</a> - voice recognition and this is for Content Generation all of this is very useful uh you know stuff that I'll be<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1117">18:37</a> - using a lot and so again that's why even though it costs money I think it will be money well spent in the long term here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1124">18:44</a> - so uh here's something a little bit more interesting perhaps on the ministry side I have my roommate come up with ideas<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1130">18:50</a> - for his ministry website's domain name and so mine is Bible docs right and so<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1136">18:56</a> - it's kind of a tricky process choosing a name not that we're super interested in the marketing branding side of things<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1141">19:01</a> - but you want it to be something memorable and something reasonably short so that it's easy to remember and share and so uh he picked out one of the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1149">19:09</a> - domain names that I had kind of had on my list you know we talked about how you generate them and things like that but<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1156">19:16</a> - he ended up liking one of the ones that was on the list that I had come up with earlier when I was doing the same process a few months back and I helped<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1162">19:22</a> - him register it with the domain name registrar and in the process of this I got thinking a bit here about the next<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1168">19:28</a> - steps and so I will need to work on some stuff with the website theme to get in a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1174">19:34</a> - state that is ready for basically being used in more than one place so right now it's just more or less being used on the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1180">19:40</a> - ministry website I have an older version of it that's also being used on my personal blog that has been up you know<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1185">19:45</a> - for a few years now that I haven't really updated that consistently I did for a while in college but I I have<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1190">19:50</a> - grand plans to make that more active as well as launch a separate kind of like uh business type website that's a little<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1198">19:58</a> - bit more formal me writing up video content and stuff like that but if I want to use it in these multiple places<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1205">20:05</a> - as well as this ministry site for my friend and maybe help another couple contacts in my Ministry circles also set<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1210">20:10</a> - up Bible study websites well I need to kind of get it in a place that is<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1217">20:17</a> - kind of better set up for uh sharing across multiple people like that and so one of the things I'm going to do for<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1223">20:23</a> - example is try to refactor the CSS to use scss instead so that we can make<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1228">20:28</a> - some of the color styling in the user interface uh basically variables so that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1234">20:34</a> - people can say hey I want this caller for the text this color for the backgrounds of like the table of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1239">20:39</a> - contents in the sidebar menu and then you just change it one place rather than having to change it all across the styling file so that's just one example<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1246">20:46</a> - but there's a lot more stuff I need to do more or less just to clean it up because most of what I have works but<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1252">20:52</a> - I've been building it for several years now and so the code base is is not quite<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1257">20:57</a> - zip ties and duct tape I've tried to follow better practices than that but it is not been something that I had taken<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1263">21:03</a> - the time to sit down and clean up a lot and so that's something that I want to do before I start you know duplicating<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1268">21:08</a> - it everywhere I want to make sure that I've kind of polished things better than I have because so far like I said if<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1274">21:14</a> - it's just me it doesn't matter if it's a bit messy because I know my own code but if I'm going to be deploying this kind<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1281">21:21</a> - of more in a production sense across maybe four or five even 10 websites depending on how many people I end up helping eventually it'd be much better<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1287">21:27</a> - for it to be more cleaned up and of course it is a public GitHub repository so other people anyone in the world<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1292">21:32</a> - who's interested in the theme can of course use it um and so if I if it ever gains a bit more traction I will want it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1297">21:37</a> - to be a kind of better maintained than it is at the moment and so I just got thinking about all this this is<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1303">21:43</a> - something else uh probably a little bit down the road here but I did spend some time on this after I helped my roommate with the domain name stuff<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1309">21:49</a> - um probably not going to spend too much time talking about this and some of those video is already going to be long but we had several conversations on the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1316">21:56</a> - ministry group so one of them we were actually talking about cryptocurrencies and crypto investing as well as just<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1322">22:02</a> - investing generally you know our relationship to money as Christians the purpose that we have for using money in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1327">22:07</a> - this world you know it's a tool it's kind of neither good nor evil although the love of money and greed is of course<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1334">22:14</a> - not a good thing for us um but you know crypto specifically has a higher risk than many other assets and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1340">22:20</a> - we were talking about does that send a good witness for us as Christians you know gambling for example certainly doesn't send a great witness especially<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1347">22:27</a> - if taken to addictive lengths and so is investing in cryptocurrencies the same as gambling I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1353">22:33</a> - mean kinda uh depends on which ones you do and how much research you do and certainly we don't want to be legalistic<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1359">22:39</a> - about it and say you can never do it but you know we just need to be responsible stewards of the resources that God has<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1364">22:44</a> - given us and things like that so we're talking about that we also had this conversation about kind of like<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1369">22:49</a> - apologetics approaches one of our friends in the community has an atheist friend who he's trying to kind of send<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1374">22:54</a> - good materials to something that would be worthy of dialogue and the friend he<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1380">23:00</a> - has is uh kind of very inclined towards the scientific and philosophical side of things a very formal very intellectual<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1387">23:07</a> - which is a good thing you know this is certainly not like a bad thing you know wanting to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1392">23:12</a> - talk about things in a very formal and rigorous way well the problem is is that there are a number of apologetics<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1397">23:17</a> - resources that kind of claim to be along those lines but even as a Christian as someone who already believes things in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1404">23:24</a> - terms of formulating arguments that I think unbelievers would actually find convincing towards you know for example<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1409">23:29</a> - actually interacting in dialogue with some of the questions they might have and things like that I've just always<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1415">23:35</a> - found these resources even the ones that style themselves as being very formal to just kind of be too lightweight and kind<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1421">23:41</a> - of hand wavy is not a very kind term but Airy fairy um you know just kind of not<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1428">23:48</a> - tackling the issues not tackling them head on or really listening and so I just don't have a lot that I feel<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1434">23:54</a> - comfortable recommending in the sphere and so we're talking about things uh you know not so much formal<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1440">24:00</a> - apologetics like proving the existence of God because there's always going to be a component of Faith involved in this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1445">24:05</a> - uh but more uh formally handling objections towards for example the existence of a spiritual realm uh the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1453">24:13</a> - Mind Body problem in neuroscience and philosophy of mine here so you know the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1458">24:18</a> - the issue of Consciousness and how strict materialists have a hard time defending that and philosophy of science<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1465">24:25</a> - in terms of people thinking science can explain everything except it certainly can't because there are certain things<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1470">24:30</a> - certain questions the science just isn't capable of answering and then logical positivism as that relates to philosophy<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1477">24:37</a> - of science and uh you know basically a refutation of strict materialism a writ large all of this sort of thing uh you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1484">24:44</a> - know I don't know how much of that is followable by most people but it is kind of an important area of apologetic<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1491">24:51</a> - discourse that I just don't have very good resource suggestions on because I've never been Terribly Happy with many<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1497">24:57</a> - of the Christian resources that I've written not because I disagree with the people writing these things at least not<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1502">25:02</a> - in large part but just because I don't think many of the things that I write along these lines have done a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1508">25:08</a> - particularly good job kind of writing them in a way that will be convincing to their target audiences and so it's a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1516">25:16</a> - very difficult thing to be formal kind of all the way through through and through without presupposing all of the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1521">25:21</a> - things that we believe as Christians and so one of the tricky things about apologetics is to a certain degree you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1527">25:27</a> - have to be arguing without presupposing some of the things that we commonly take for granted so for example that God<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1532">25:32</a> - exists and that his word is inerrant and that we can build our Doctrine off of that because the people don't buy the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1539">25:39</a> - inerrancy of scripture and they don't believe the Bible is a valid like epistemological base then you have a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1544">25:44</a> - hard time discussing things with them and so instead you have to talk about the idea of axioms and presuppositions<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1550">25:50</a> - and kind of why people believe what they believe and all of this other stuff just to kind of be able to talk<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1556">25:56</a> - in a way that doesn't presuppose the thing that you're arguing for um and so it's a shift that can be<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1561">26:01</a> - difficult to do especially do well um and this isn't like a blanket condemnation of all things apologetics<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1567">26:07</a> - out there as if I could just do it so much better it's a tricky it's a tricky tricky subject um it's a tricky thing to handle the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1574">26:14</a> - point in this was I couldn't just think of something off the shelf that I was like oh yes this is definitely what my friend should share so we talked about<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1579">26:19</a> - all of this and kind of the best way to go about it and some of the things in there I was actually pretty interested after the conversations I went did some<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1585">26:25</a> - research tried to find some links that might be helpful here from uh you know kind of blogs that I followed or just<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1592">26:32</a> - videos about these topics and stuff that might be a good start so those were discussions we had<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1599">26:39</a> - um you know in as much as people probably haven't been all that interested in a lot of the stuff I've already been rambling about here I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1604">26:44</a> - really don't want to talk too too much about the actual coding part of this um so I am going to go show you what the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1610">26:50</a> - discussion pages are that will probably be more interesting here um so discussion pages are uh uh pages<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1616">26:56</a> - and videos here supporting kind of tangentially related content to the studies uh that I have here and so uh<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1623">27:03</a> - here in the sr4 studies so this is the first lesson here to the sr4 series<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1629">27:09</a> - which is just the introductory video here right and so this has all the content for the introductory video now<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1634">27:14</a> - what the discussion page are is on the content page here if we show the table of contents you'll see down at the bottom oh we have this other section<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1641">27:21</a> - which is where the discussion page is now by default on the content Pages um we minimize the content in the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1647">27:27</a> - transcript of the discussion page so that the only stuff that shows up is the summary in the time stamps which is like the the brief version that will I'll let<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1654">27:34</a> - people get an idea of the topic so the discussion page itself looks like a normal page here so it has its own<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1660">27:40</a> - content and transcripts right it the content is very similar to all of the other pages on the website it's how it's<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1665">27:45</a> - organized so this is the discussion page kind of the low level here now content Pages can have one or more discussion<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1671">27:51</a> - pages and uh they they show up again here at the bottom of the content page so if I have a second discussion page it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1677">27:57</a> - would show up you know second after this one um and then uh they actually show up on<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1683">28:03</a> - the aggregation Pages here as well so note in the sidebar menu here I added uh links here to show and hide discussion<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1690">28:10</a> - pages so right now I only have one but they function just like the content transcript sections you can expand and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1696">28:16</a> - collapse the discussion Pages for any given content page and by default they'll start out collapsed on the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1702">28:22</a> - aggregation pages and this is just the same content that was in the other places as well and um so if you if you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1708">28:28</a> - show like the content uh and the transcripts then they will show the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1713">28:33</a> - content in the transcripts within that discussion page section as well and then you can actually search across uh all of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1719">28:39</a> - the content on this page all at once and again that's the main purpose of the aggregation Pages as used on this site<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1725">28:45</a> - is primarily for uh so here we are in the discussion page section here right this is the discussion page showing up<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1731">28:51</a> - on this uh website as well uh being able to search and skim through absolutely everything here and then you can uh you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1738">28:58</a> - know if we hide the content and hide the transcripts you know you can search and skim just through the summaries and the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1743">29:03</a> - time stamps uh this is the purpose of the aggregation Pages for that searching and the skimming being able to view the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1749">29:09</a> - study content all together doing those two things which are very helpful for finding information<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1754">29:14</a> - this is how a discussion Pages show up in all these voices now to actually make it so that all of this happens in a more<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1760">29:20</a> - or less automatic automated way so that I just write a page like this and stick<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1766">29:26</a> - it in the folder and then have my python application do absolutely everything else so it copies it onto the content<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1773">29:33</a> - page it copies it onto the aggregation page after it's already shown up on the content page it sets it so that it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1778">29:38</a> - displays correctly by default in both of those places and it gets handled if you<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1783">29:43</a> - have more than one of these things and they show up in the right order and all of that stuff I'm not going to bore you with the messy implementation details<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1790">29:50</a> - but long story short took me quite a long time to figure out how to do all of this you know I would say ballpark 20<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1796">29:56</a> - hours of coding lots of debugging in that because this is kind of a bug prone process I had to change the way that I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1803">30:03</a> - organized some of the information in the file structure on the website so something called page bundles in Hugo<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1810">30:10</a> - started using Branch bundles rather than Leaf bundles probably doesn't mean very much most people but there's kind of a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1817">30:17</a> - lot of debugging in trial and error involved in figuring out how I needed to order everything to make this be the new<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1823">30:23</a> - default Behavior but now that I've gotten this set up and the reason why I'm spending so much time on the uh the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1829">30:29</a> - python application I've written up front here is moving forward in the future all I'll have to do is write new studies in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1835">30:35</a> - markdown which is kind of what I draft the web pages in and then I will press<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1840">30:40</a> - play on my application and let it spin for 10 or 15 seconds and then boom it will make the slides for me it will<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1846">30:46</a> - organize all of the content on the pages um it will actually also it will also build a subject index so the discussion<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1853">30:53</a> - Pages show up in the subject index as well I know that I added uh something here on Satan so if we go find Satan<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1860">31:00</a> - here in the subject Index this is actually a discussion page here you can see because discussion shows up<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1866">31:06</a> - in the page title here so Satan is already positionally defeated that's something that we had here so we will go<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1874">31:14</a> - you know click on this and you can see that it actually already shows up on the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1880">31:20</a> - discussion page and so uh in this way you know discussion pages are fully integrated content on the website<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1886">31:26</a> - um but they won't get in the way on the content Pages unless you want to see them so not I can't talk too much I mean this was hundreds of lines of code<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1892">31:32</a> - probably that I had to change and you know just for a sense of scale this isn't even the python application self<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1898">31:38</a> - this is the GitHub repository for the website I had to change some short codes and stuff but I mean this is the number<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1905">31:45</a> - of files I had to change on just the website and so um I don't actually have a lot of the stuff in Version Control<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1910">31:50</a> - this is a CSS file I mean this was a what's this one uh this is like the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1915">31:55</a> - section navigation stuff um yeah I mean I won't bore everyone with the details it was pretty gross and it took me quite<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1921">32:01</a> - a long time to get it um I haven't actually been pushing most of the commits to the preprocessor it's just not something that is quite ready for<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1928">32:08</a> - public use yet I mean the repo is public it's just out of date at this point because I've been working on this for a<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1933">32:13</a> - few months past what I pushed more recently I think um just keeping it all local here as I continue to polish stuff so can't show<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1940">32:20</a> - you the actual diff there but it was probably on the magnitude of 15 files and hundreds of lines change so it took<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1945">32:25</a> - me a nice long time here to do all this but I'm kind of hopeful now that I've done this that I won't have to do things<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1951">32:31</a> - like this again for a while uh that I will have knocked out a lot of the uh kind of the grosser coding side of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1958">32:38</a> - things here because now the preposter application should properly be doing everything you know I shouldn't have to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1963">32:43</a> - do more at least that's what I'm hoping um all right so with that that is all of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1968">32:48</a> - the stuff that I got done here again maybe not the most interesting cycle uh you know in these two weeks here I done<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1974">32:54</a> - a lot of kind of setup stuff now content will be coming more shortly here<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1979">32:59</a> - hopefully so stuff that I still need to do this is kind of my short-term goals I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1984">33:04</a> - need to write up documentation now that I've got the discussion Pages pushed live on the side I need to write up some<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1989">33:09</a> - documentation on the content organization page kind of explaining what they are and how they work similar to as I've done with the content pages<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=1995">33:15</a> - and aggregation Pages already I've been a bit lazy there's a lot of like boring<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2001">33:21</a> - busy work that I have to do when I upload the videos and the audio to archive.org I do that so that people can<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2007">33:27</a> - download them for offline use you know so that way you don't have to have an internet connection to watch the videos because by default YouTube doesn't let<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2013">33:33</a> - you download videos it's actually against YouTube's terms of service so I upload them to this platform so that<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2019">33:39</a> - anyone who does want to download the videos so that they're not tied without internet connection can do so they don't<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2024">33:44</a> - have to violate YouTube's terms of service to do it I just provide the links in the video descriptions but um I have to go like find the files and<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2031">33:51</a> - download them and then upload them to archive.org and make sure the metadata data is correct and it just takes a while and is a bit of annoying busy work<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2037">33:57</a> - and so I have a backlog of videos here that I need to do that for and I should try to keep up with it more consistently I'm actually thinking uh as I catch up<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2044">34:04</a> - here um the other big part of like phase two in the ministry plan here that I<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2049">34:09</a> - went over in the last Ministry progress summary uh so uh the things in phase two were knocking out the discussion page<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2055">34:15</a> - stuff that I mostly just did I have to write the documentation for it and then go through all of the remaining stuff in<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2062">34:22</a> - the sr4 series and completely organize the videos there so post all the stuff on the website I'll make sure all the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2068">34:28</a> - links work build out all the descriptions on YouTube get all of that content completely polished and then<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2073">34:33</a> - I'll keep going after that that will finish off phase two that's when I'll start making content videos again in the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2078">34:38</a> - sr4 series and so hopefully this won't take me as long as coding the discussion page stuff did you know because it's not<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2084">34:44</a> - code this time it's just this is more or less just going to be a lot of busy work I'm going to try to do like maybe one<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2089">34:49</a> - study a day I think I have about 18 17 left something like that um and then I've just got to knock it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2096">34:56</a> - out um and so I'm thinking of doing like all all of this archive.org stuff all at once I'm kind of just like block myself<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2103">35:03</a> - uh you know several hours there and just go do it for all the videos all at the same time that way I won't have to like keep coming back to it<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2109">35:09</a> - um and then I'll knock out organizing all the transcripts and the time stamps and all the video descriptions and stuff<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2114">35:14</a> - I may do it like piece by piece um because I have quite a bit to do there but that's the main other thing<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2120">35:20</a> - that I have to do in phase two and then I'll be ready to start making new content again and then hopefully this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2125">35:25</a> - will be more interesting on the content side not so much setup stuff um and then also more on the tech stuff I need to actually test out the wireless<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2132">35:32</a> - microphone that I mentioned that I got for the content recordings as well as continuing to set up more on the voice<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2139">35:39</a> - recognition stuff so that I can start using that more full time here all right well to finish off here uh<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2145">35:45</a> - back on the webcam um I'm just going to say real briefly that I'm glad that I got a good bit of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2151">35:51</a> - work done here on the discussion Pages as well as starting to get some of the sr4 videos you know I did the one sr4<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2158">35:58</a> - video with the discussion page uh got that kind of fully organized so these<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2163">36:03</a> - are some of the steps in that uh second phase of the ministry rollout plan here and so once I have finished all this<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2170">36:10</a> - like I've said before I'll be able to actually start making more content videos again and that's something I'm<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2176">36:16</a> - excited about just because it's something that I you know just am more interested in than some of the busy work<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2182">36:22</a> - here that I'm having to do up front to get the setup done and once I start doing that again I'm going to try to get<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2187">36:27</a> - more involved locally I think I've mentioned as well that that's something else I'm looking forward to so I'm<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2193">36:33</a> - hoping here that uh you know next coming cycle as I move forward on the<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2198">36:38</a> - organization stuff that I'll only have maybe several more weeks of this before I'll be done uh with that initial push<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2205">36:45</a> - and then that will let me kind of diversify some of the things I work on and hopefully it'll mean that uh some of<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2210">36:50</a> - the stuff's more exciting both for me to do and for people to keep up with here so I hope that uh this summary here has<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2217">36:57</a> - been informative for all the people keeping up with what's going on in this ministry and with that I will talk to<br/>
<a href="https://www.youtube.com/watch?v=HpKO1ZHIzPQ&t=2223">37:03</a> - everyone again next time<br/>

{{% /transcript %}}

{{% section-navigation %}}