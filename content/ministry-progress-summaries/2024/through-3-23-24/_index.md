---
title: Through 3/23/24
weight: 10
layout: content-page
video: https://www.youtube.com/watch?v=UjHR0HJJbyw
playlist: https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb
---

{{< subjects >}}

{{< /subjects >}}

{{% section-navigation %}}

## Video {#video}

{{% video
videoId="C_RCnuxTSHo"

videoPlaylist="https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb"

slides="https://www.bibledocs.org/slides/ministry-progress-summaries/2023/through-1-1-23/"
%}}

## Summary {#summary}

This cycle I mostly focused on completing a large chunk of the development effort to automate video content processing. With the progress I've now made on my Python application, I should be able to post the backlog of BB1: Theology videos I have recorded and ready (probably ~20 videos) in a much shorter timeframe than if I had to manually process them one-by-one. I also recorded a short series of videos on some matters relating to death, resuscitation, and the afterlife that I will be posting in the near future, alongide the aforementioned BB1 videos.

## Timestamps {#timestamps}



{{% content %}}

## Content {#content}

<!-- --- -->

### Foreword: things I did not do, despite some of my prior plans {#foreword-things-i-did-not-do-despite-some-of-my-prior-plans}

Well, time flew by, and it has been a while again. I should say upfront I did rather poorly at spending my time according to my plans in the last ministry progress summary. Not that I wasn't productive, but I just didn't do the things I had thought I might. For example:

- I said I'd try to release more frequently, yet here we are some 4+ months later, with this being the first new update.
- I said I'd try to fill in discussion questions from a local Bible study covering the book of Romans, yet I didn't really make any progress there.
- I said I'd try to finish off my verse-by-verse study of 1 Thessalonians 5 (the remaining verses I hadn't got to yet in that chapter), but I didn't make any progress there.
- I said I'd try to finish some of my other in-progress studies (on the concept of judging others, and the lukewarmness of the modern church), but I didn't make any progress there.
- And finally, I said I might think about a couple other possibilities (perhaps starting another series on CT with mid-week meetings, and perhaps getting more involved with online Christian communities), but I didn't really spend much time further considering these things, even though I had wanted to think over these matters more.

So that's a list of things I didn't do, even though I had been thinking these things were where I was going to turn next, as of a few months ago.

<!-- --- -->

### So what *did* I actually do? {#so-what-did-i-actually-do}

Here's a high-level overview of some of the tasks I focused on:

- We kept having our weekly Zoom meetings going through the Ichthys study BB1: Theology. We are almost done with this study now.
- When I got a series of questions (about sleep as a metaphor for death, resuscitation, the afterlife, etc.) from a friend, I made a series of in-depth videos to answer the questions. This turned into a four-part series, with ballpark four hours of pretty dense recorded content.
- Since MailChimp deprecated TinyLetter (the mailing list service I'd been using on [BibleDocs](https://www.bibledocs.org/), and also had set up for Jordan's ministry site [BibleDriven](https://www.bibledriven.org/)), I had to switch both of us over to a different mailing list service. I decided to go with [Buttondown](https://buttondown.email/). This took some work.

<!-- --- -->

I also coded. *A lot*.

- I built out [a command-line video processing application](https://github.com/StevenTammen/command-line-video-and-audio), and formalized an entire video processing workflow, with hundreds of lines of code to completely automate large chunks of the video generation process.
- I set up [a better command-line Python development workflow](https://github.com/StevenTammen/dotfiles) as part of setting up the video processing scripts. I decided to use the [xonsh shell](https://xon.sh/) on the [Windows subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about#what-is-wsl-2) (Ubuntu), with a package called [vox](https://github.com/xonsh/xontrib-vox) to seamlessly manage Python virtual environments.
- I cleaned up the codebase for [my keyboard layout project](https://github.com/StevenTammen/taser). I'm still not quite done, but I'm now a good bit closer to being ready to use it full-time, since the codebase is much more understandable and maintainable. I have been trying to start using this full-time before I *really* ramp up content production, so that I am more efficient when I am typing out large volumes of text. It has been a long-standing goal of mine.
- I figured out [how to support page-internal timestamps for embedded YouTube videos](https://github.com/StevenTammen/youtube-iframe-api-multiple-videos-example), and fully implemented them on the site. All this is JavaScript, interacting with the [YouTube Iframe API](https://developers.google.com/youtube/iframe_api_reference).
- I figured out how to use different fonts for Greek and Hebrew Unicode character ranges on webpages via CSS, and set things up to use better Greek and Hebrew fonts (e.g., Cardo, Gentium, SIL Ezra, SBL Hebrew, etc.) in recording slides specifically.

I'm not going to go over absolutely all of these coding-relating things in further depth in this video, but I will talk somewhat more about the general video processing steps, as well as page-internal timestamps, since I can sort of demo those visually, and they are probably the most important things of the lot.

<!-- --- -->

### Why did things turn out delayed this way? Mostly because I wanted to finish the bulk of the video processing automation before I processed all the videos {#why-did-things-turn-out-delayed-this-way-mostly-because-i-wanted-to-finish-the-bulk-of-the-video-processing-automation-before-i-processed-all-the-videos}

I wanted to mostly finish the Python application to automate all the video processing stuff before I processed all the BB1 videos, so I'd avoid a lot of time opportunity cost. Long story short, wiring it all up just proved to be harder than might be first apparent.

Even as it is now, it is not perfect. I'll talk more about a couple planned improvements in the section going over my upcoming plans. However, even where things are right now, it completely automates:

- Combining recording segments, with clean title-slide transitions between them
- Generating accurate timestamps completely automatically

And across the many, many hours of video content we've recorded for BB1, having these things automated will save me a massive amount of time. That's why I chose to wait until I had all the automation more in place before doing the BB1 videos.

<!-- --- -->

### A brief overview of the video processing workflow {#a-brief-overview-of-the-video-processing-workflow}

I will be going over a few concepts:

- Markdown content files
- The recording directory structure. (Right now I store all my recordings in Dropbox).
  - segments.xlsx
  - The `recording/raw/` and `recording/processed/`and `recording/topic-transitions/` subdirectories
  - metadata.txt, and mp4 video chapters (as can be used for navigation in the [VLC video player](https://www.videolan.org/vlc/), among others)
  - youtube-description.txt

The short version is that all of this together automates a lot of the video processing steps that would otherwise be tedious and time-consuming (not to mention more error-prone) to do by hand.

<!-- --- -->

### What the output videos look like on YouTube/the website {#what-the-output-videos-look-like-on-youtube-the-website}

The big things to note are the clean title-slide transitions between topics, and the accurate timestamps for every single section/topic.

Seeing it all in action will help make it a lot more obvious what I am talking about, so I'll just demo the main functionality in the ministry progress video here.

<!-- --- -->

### Page-internal timestamps and the YouTube Iframe API {#page-internal-timestamps-and-the-youtube-iframe-api}

I added a site setting cookie on the site that lets you pick whether you want timestamps to open the videos in a new tab, or change the time of the page-embedded video (the default behavior now). I also set up a couple other things with the YouTube Iframe API, like making it so that only one embedded video can be played at a time, and implementing a menu navigation link that automatically scrolls to you to whatever video is currently playing.

One thing that is very useful that is now better supported is being able to full-text-search video transcripts, and then immediately play videos at whatever times correspond to search matches.

Seeing it all in action will help make it a lot more obvious what I am talking about, so I'll just demo the main functionality in the ministry progress video here.

<!-- --- -->

### So now that all of that is set up, releases will be more consistent. I promise {#so-now-that-all-of-that-is-set-up-releases-will-be-more-consistent-i-promise}

I just very recently finished getting everything just discussed set up, and decided to make this ministry progress update even before actually putting up more of the content I have in in my ready backlog. I released [the first BB1 video]() before putting up this ministry progress summary (so that I could use it as an example in demoing all the new functionality), but all the other videos aren't actually up yet.

I'm planning to release at least a couple videos a week for the next few weeks, until I run out of ready content. If you aren't already subscribed to [the YouTube channel](https://www.youtube.com/channel/UCFk7khraAKf68DZ5GeYEFIw), you might consider doing that, since from here on out, there ought to be more consistent new video content.

<!-- --- -->

### Upcoming plans {#upcoming-plans}

First of all, I'm going to be working on getting the full backlog of ready videos posted (as just discussed), so that will be my top priority.

In our BB1 study, we are still talking about the Trinity, but are now in the last section of the study, going over Christophanies in the Old Testament. We will probably finish this study in several more weeks. I'm planning to have us start either Christology or Soteriology next (parts 4A and 4B, respectively, of the Bible Basics series on Ichthys), but I haven't picked which yet.

<!-- --- -->

In the immediate short term, I have three other primary goals:

- Setting up completely automatic silence removal in the video editing process (to further save me time---right now it is still a bit tedious, since I have to process segment by segment using a GUI tool). This will entail switching us away from Zoom, since Zoom recordings don't seem to play nice with the scriptable command-line tool I'd like to use, for some strange reason. I'm going have us try Microsoft Teams next, I think.
- Setting up further automation with the topic transitions in videos. I would like to automatically generate the top transition video segments in a hands-off (completely automated) way. Right now I have to manually record the short segments one by one.
- Setting up a BibleDocs podcast on the podcasting platform [PodBean](https://www.podbean.com/), to include all the content from our Ichthys group Bible studies (at least that is the content stream I'll start with for podcasting---I will probably expand to others too, later). I need to support ripping mp3 audio off of the mp4 videos, and generating proper mp3 metadata/episode descriptions so that podcast episode timestamps will work properly on Apple Podcasts and Spotify (the two most dominant podcast apps, at present).

<!-- --- -->

After all of that, I want to turn my full focus back to launching an in-person Bible study at my house. There are a ton of TODOs left there, but I'll leave all those aside for now, until we get a bit closer.

This will definitely be my next longer-term goal. I've been meaning to make this happen now for literally years, but now that all the content production automation is coming together, I think I'm finally about ready to get it going in a fully sustainable fashion.

{{% /content %}}

{{% transcript %}}

## Video/audio transcript {#video-audio-transcript}

{{% timestamp videoId="UjHR0HJJbyw" time="0" display="0:00" %}} - hey guys right now I'm going to be making the ministry progress summary here through March 23rd  
{{% timestamp videoId="UjHR0HJJbyw" time="7" display="0:07" %}} - 2024 so it's been several months here um I ended up getting really busy with some  
{{% timestamp videoId="UjHR0HJJbyw" time="13" display="0:13" %}} - of the coding projects I had for automating some of the video processing  
{{% timestamp videoId="UjHR0HJJbyw" time="18" display="0:18" %}} - for all of the content that we'll be having moving forward so I didn't quite finish all of the things that I thought  
{{% timestamp videoId="UjHR0HJJbyw" time="24" display="0:24" %}} - I was going to focus on at the end of the last Ministry progress summary which was oh I guess back in October or so um  
{{% timestamp videoId="UjHR0HJJbyw" time="31" display="0:31" %}} - but we're going to be going over kind of all of the things that I did instead so um I really wanted to finish a lot of  
{{% timestamp videoId="UjHR0HJJbyw" time="39" display="0:39" %}} - the uh kind of automation for processing videos before I processed all of the  
{{% timestamp videoId="UjHR0HJJbyw" time="44" display="0:44" %}} - videos for the Bible basics series that we've been doing in our Zoom Bible  
{{% timestamp videoId="UjHR0HJJbyw" time="49" display="0:49" %}} - studies on the weekends here just because I had maybe a backlog of 20 videos or so and I knew that if I tried  
{{% timestamp videoId="UjHR0HJJbyw" time="57" display="0:57" %}} - to do it all manual first I'd end up wasting a lot of time relative to me just waiting a while until I finish some  
{{% timestamp videoId="UjHR0HJJbyw" time="63" display="1:03" %}} - of the automation so that's really mostly what I focused on the last several months was getting this video  
{{% timestamp videoId="UjHR0HJJbyw" time="70" display="1:10" %}} - automation uh process sort of set up I made a python application on the command  
{{% timestamp videoId="UjHR0HJJbyw" time="75" display="1:15" %}} - line that basically helps me process a lot of the videos and calculate timestamps completely automatically so  
{{% timestamp videoId="UjHR0HJJbyw" time="81" display="1:21" %}} - I'll go over some of the specifics in that a little I mean not too much technical depth here and go over some of  
{{% timestamp videoId="UjHR0HJJbyw" time="87" display="1:27" %}} - the other things we did um and then as per normal I will also be going over uh  
{{% timestamp videoId="UjHR0HJJbyw" time="93" display="1:33" %}} - kind of what I'm planning on focusing on for the next little bit in the future kind of what my my next stretch goals  
{{% timestamp videoId="UjHR0HJJbyw" time="99" display="1:39" %}} - are uh just as we've been doing for all of the ministry progress summaries since I started doing  
{{% timestamp videoId="UjHR0HJJbyw" time="107" display="1:47" %}} - these all right well to kick us off I just wanted to go over uh some of the  
{{% timestamp videoId="UjHR0HJJbyw" time="113" display="1:53" %}} - things that I had thought that I might be focusing on at the end of the last Ministry progress summary so this was  
{{% timestamp videoId="UjHR0HJJbyw" time="118" display="1:58" %}} - kind of what had in the upcoming plan section from that last progress update I  
{{% timestamp videoId="UjHR0HJJbyw" time="124" display="2:04" %}} - had from last October and I just wanted to go over some of these things and well basically say that I didn't get to them  
{{% timestamp videoId="UjHR0HJJbyw" time="131" display="2:11" %}} - and so it's not that I won't get to these things ever um I am planning on doing all of this eventually uh you know  
{{% timestamp videoId="UjHR0HJJbyw" time="138" display="2:18" %}} - kind of time permitting and depending on uh you know what else i' deem a higher priority and things like that but um I  
{{% timestamp videoId="UjHR0HJJbyw" time="145" display="2:25" %}} - thought that I was going to be releasing more frequently here you know first of all just because I thought I was going  
{{% timestamp videoId="UjHR0HJJbyw" time="150" display="2:30" %}} - to be releasing some of the Bible basics content that we've been doing from our video series but I ended up kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="156" display="2:36" %}} - bottlenecking all of that behind uh finishing the content automation process  
{{% timestamp videoId="UjHR0HJJbyw" time="162" display="2:42" %}} - that I mentioned just before um and so I actually didn't end up making any  
{{% timestamp videoId="UjHR0HJJbyw" time="167" display="2:47" %}} - releases in between then and now and the reason why I'm doing it now is because I finally finished the initial steps in  
{{% timestamp videoId="UjHR0HJJbyw" time="175" display="2:55" %}} - that process that lets me much more rapidly make new video content  
{{% timestamp videoId="UjHR0HJJbyw" time="180" display="3:00" %}} - kind of with the structure in the format that I want and so that's kind of why it ended up being longer here than I  
{{% timestamp videoId="UjHR0HJJbyw" time="186" display="3:06" %}} - thought it might and um you know this time for for real I really do think that I will be keeping a more consistent  
{{% timestamp videoId="UjHR0HJJbyw" time="193" display="3:13" %}} - schedule um I I may not release every couple weeks you know I'll still probably follow kind of Milestones with  
{{% timestamp videoId="UjHR0HJJbyw" time="200" display="3:20" %}} - the ministry progress uh so for example the next progress summary after this current one that I'm making will  
{{% timestamp videoId="UjHR0HJJbyw" time="206" display="3:26" %}} - probably kind of be once I posted a lot of the videos for uh the Bible basics part one series that we've been doing uh  
{{% timestamp videoId="UjHR0HJJbyw" time="213" display="3:33" %}} - so getting that theology proper series up on YouTube and you know once I've at least made a lot more progress there and  
{{% timestamp videoId="UjHR0HJJbyw" time="219" display="3:39" %}} - maybe achieved some of my other milestones in uh that project that lets me automate things maybe I'll make  
{{% timestamp videoId="UjHR0HJJbyw" time="225" display="3:45" %}} - another one but um you know so despite my best intentions haven't been as consistent here in providing updates  
{{% timestamp videoId="UjHR0HJJbyw" time="232" display="3:52" %}} - although I have been busy as we will see here um and then some of the other content things I just ended up not  
{{% timestamp videoId="UjHR0HJJbyw" time="238" display="3:58" %}} - focusing on those because I I put most of my effort and my focus on getting the new video content up and to be able to  
{{% timestamp videoId="UjHR0HJJbyw" time="246" display="4:06" %}} - do that uh largely focusing on trying to automate some of the tasks that are involved in that so some of the other  
{{% timestamp videoId="UjHR0HJJbyw" time="252" display="4:12" %}} - things that I may come back to in the future uh doing some of those discussion  
{{% timestamp videoId="UjHR0HJJbyw" time="257" display="4:17" %}} - based questions from that Bible study of Romans that we had with one of the local groups I've been involved with uh  
{{% timestamp videoId="UjHR0HJJbyw" time="264" display="4:24" %}} - finishing the verse by verse uh series that I started on 1 Thessalonians chapter 5 five I got through I don't  
{{% timestamp videoId="UjHR0HJJbyw" time="271" display="4:31" %}} - know like maybe verse 16 verse 20 I can't quite remember there were a few verses at the end of the chapter that I  
{{% timestamp videoId="UjHR0HJJbyw" time="277" display="4:37" %}} - I still hadn't gotten to yet and just kind of for completeness sake may as well finish off that chapter um I have a  
{{% timestamp videoId="UjHR0HJJbyw" time="283" display="4:43" %}} - couple larger studies still in progress here uh one on the concept of how we ought to view judging others as  
{{% timestamp videoId="UjHR0HJJbyw" time="289" display="4:49" %}} - Believers and then one on the lukewarmness of the modern church but I haven't managed to make a lot of  
{{% timestamp videoId="UjHR0HJJbyw" time="295" display="4:55" %}} - progress there either again just because my focus has been elsewhere and then some of the future matters or stretch  
{{% timestamp videoId="UjHR0HJJbyw" time="302" display="5:02" %}} - goals still thinking about them didn't really make a lot of progress here in terms of I don't know weighing pros and  
{{% timestamp videoId="UjHR0HJJbyw" time="308" display="5:08" %}} - cons or uh kind of looking at what my options are here so thinking about  
{{% timestamp videoId="UjHR0HJJbyw" time="313" display="5:13" %}} - starting another Series in the middle of the week uh you know where my friend and co-host and I might kind of bounce ideas  
{{% timestamp videoId="UjHR0HJJbyw" time="319" display="5:19" %}} - off each other in a less uh I guess I would say consistently structured uh way  
{{% timestamp videoId="UjHR0HJJbyw" time="327" display="5:27" %}} - so our normal group Bible studies are right now they're happening on Sundays but they've been either on Saturdays or  
{{% timestamp videoId="UjHR0HJJbyw" time="333" display="5:33" %}} - Sundays for several years now but if we could do one in the middle of the week you know that might help increase the  
{{% timestamp videoId="UjHR0HJJbyw" time="339" display="5:39" %}} - amount of content we can put out so that was one of the ideas and then the other one was just getting more involved with  
{{% timestamp videoId="UjHR0HJJbyw" time="344" display="5:44" %}} - some online Christian Community so like forums sub subreddits Facebook groups  
{{% timestamp videoId="UjHR0HJJbyw" time="349" display="5:49" %}} - that sort of thing um but I just didn't make a lot of progress there either so I won't belabor this overly just this was  
{{% timestamp videoId="UjHR0HJJbyw" time="356" display="5:56" %}} - a list of things that I thought I was GNA kind of focus on and then honestly most of my focus ended up getting kind  
{{% timestamp videoId="UjHR0HJJbyw" time="362" display="6:02" %}} - of tied up in the other matters that uh I'll talk about in just a minute here and so I don't really view this as like  
{{% timestamp videoId="UjHR0HJJbyw" time="368" display="6:08" %}} - a a failure really it's just kind of updating people on well well I didn't actually do these things and I'm going  
{{% timestamp videoId="UjHR0HJJbyw" time="374" display="6:14" %}} - to you know tell you about what the things I did do instead but you know not all of these things are never going to  
{{% timestamp videoId="UjHR0HJJbyw" time="380" display="6:20" %}} - be done like I said before just maybe I'll get to them in a while once I finished the set of other things that I  
{{% timestamp videoId="UjHR0HJJbyw" time="386" display="6:26" %}} - chose to focus on this cycle instead  
{{% timestamp videoId="UjHR0HJJbyw" time="392" display="6:32" %}} - all right well going through that last section kind of should obviously bring up the question of well if I didn't do  
{{% timestamp videoId="UjHR0HJJbyw" time="398" display="6:38" %}} - all of the things that I thought maybe I was going to do what did I do instead and so I'm going to kind of go over a  
{{% timestamp videoId="UjHR0HJJbyw" time="404" display="6:44" %}} - couple slides here some of the highlevel uh things that I focused on in the last few months here and so you know one of  
{{% timestamp videoId="UjHR0HJJbyw" time="411" display="6:51" %}} - the high priorities has been continuing to record those Bible study meetings we've been having from our Zoom bible  
{{% timestamp videoId="UjHR0HJJbyw" time="417" display="6:57" %}} - study on the weekends here and so we are actually almost done now with this first  
{{% timestamp videoId="UjHR0HJJbyw" time="423" display="7:03" %}} - part of the Bible basic series on ichus which is theology proper so we started out that study talking about the the  
{{% timestamp videoId="UjHR0HJJbyw" time="430" display="7:10" %}} - essence of God and uh we've been talking about the Trinity now for several months uh we are getting close to the end here  
{{% timestamp videoId="UjHR0HJJbyw" time="437" display="7:17" %}} - uh almost done in the section now talking about christophanies in the Old Testament which is the last main section  
{{% timestamp videoId="UjHR0HJJbyw" time="443" display="7:23" %}} - of the study so I think we'll be done in several weeks here but you know over the last few months we have continued to do  
{{% timestamp videoId="UjHR0HJJbyw" time="449" display="7:29" %}} - do this every week um I actually got a series of questions from a friend uh  
{{% timestamp videoId="UjHR0HJJbyw" time="454" display="7:34" %}} - kind of talking about death and resuscitation in the afterlife and sleep as a metaphor for death and kind of a a  
{{% timestamp videoId="UjHR0HJJbyw" time="461" display="7:41" %}} - long series of pretty detailed questions about some of these things and so I actually made a video series on this uh  
{{% timestamp videoId="UjHR0HJJbyw" time="468" display="7:48" %}} - pretty in depth ended up I think being four videos and maybe four four and a half hours of content across all of  
{{% timestamp videoId="UjHR0HJJbyw" time="475" display="7:55" %}} - these topics here and so I will be releasing these videos uh kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="480" display="8:00" %}} - alongside the Bible basics videos uh that I've been talking about uh over the next several weeks here uh you know  
{{% timestamp videoId="UjHR0HJJbyw" time="487" display="8:07" %}} - maybe even a couple months you know we'll see how many I get to every week um but you know this was another uh kind  
{{% timestamp videoId="UjHR0HJJbyw" time="493" display="8:13" %}} - of thing that I hadn't really anticipated although I'm I'm glad that I did it I think it turned out well I'm pretty happy with uh some of the content  
{{% timestamp videoId="UjHR0HJJbyw" time="500" display="8:20" %}} - that I wrote kind of to answer some of these questions here and so that was another content Focus thing that I spent  
{{% timestamp videoId="UjHR0HJJbyw" time="506" display="8:26" %}} - time on and then this is not really interesting but um the uh mailing list  
{{% timestamp videoId="UjHR0HJJbyw" time="512" display="8:32" %}} - provider that I was using for my Ministry website as well as the ministry website of my friend Jordan that I  
{{% timestamp videoId="UjHR0HJJbyw" time="518" display="8:38" %}} - helped him set up um so you know I'll just plug his site again uh this is his  
{{% timestamp videoId="UjHR0HJJbyw" time="524" display="8:44" %}} - ministry site and uh you can kind of tell it uses the same theme and stuff because I helped him set it up but uh  
{{% timestamp videoId="UjHR0HJJbyw" time="529" display="8:49" %}} - this new thing here this mailing list comes from a platform called buttondown  
{{% timestamp videoId="UjHR0HJJbyw" time="536" display="8:56" %}} - and this isn't the one that we used to use we used to use one called tiny letter but then the company that uh  
{{% timestamp videoId="UjHR0HJJbyw" time="542" display="9:02" %}} - owned or bought tiny letter MailChimp they actually shut it down and so I had to update uh the mailing list providers  
{{% timestamp videoId="UjHR0HJJbyw" time="549" display="9:09" %}} - that we were using in our websites because well the company that used to run it just decided to close it which  
{{% timestamp videoId="UjHR0HJJbyw" time="556" display="9:16" %}} - was kind of unfortunate so uh this wasn't horribly complicated but we had to kind of export the mailing list like  
{{% timestamp videoId="UjHR0HJJbyw" time="563" display="9:23" %}} - the people on our list that we had import them into the new thing set up all the code to make you know make these  
{{% timestamp videoId="UjHR0HJJbyw" time="568" display="9:28" %}} - new sign up forms work and uh you know that sort of thing so this took a a couple days a couple weekends in here as  
{{% timestamp videoId="UjHR0HJJbyw" time="576" display="9:36" %}} - well I work with Jordan I did it from my own site as well kind of getting the mailing list updated so that's you know  
{{% timestamp videoId="UjHR0HJJbyw" time="582" display="9:42" %}} - kind of boring stuff but it is something that I spent a lot of time on and then as I've kind of already been talking  
{{% timestamp videoId="UjHR0HJJbyw" time="588" display="9:48" %}} - about before here I spent an awful lot of time coding in the last few months trying to automate some of the video  
{{% timestamp videoId="UjHR0HJJbyw" time="594" display="9:54" %}} - processing stuff so I'm not going to really spend too much time going over all this in great detail because most  
{{% timestamp videoId="UjHR0HJJbyw" time="600" display="10:00" %}} - people probably don't care that much but uh I mean the read me on the GitHub repository is still kind of a work in  
{{% timestamp videoId="UjHR0HJJbyw" time="607" display="10:07" %}} - progress um but this is the project I made for processing video stuff on the  
{{% timestamp videoId="UjHR0HJJbyw" time="613" display="10:13" %}} - command line so it it uses Python and wrap some FFM Peg commands and I also  
{{% timestamp videoId="UjHR0HJJbyw" time="619" display="10:19" %}} - use pandas and open pix Open PI XL for uh kind of you know Reading Writing and  
{{% timestamp videoId="UjHR0HJJbyw" time="627" display="10:27" %}} - reading stuff from Excel file to keep track of State between all of the recording segments I have and so uh I  
{{% timestamp videoId="UjHR0HJJbyw" time="634" display="10:34" %}} - really won't get into any of the nitty-gritty specifics but you can see I I had a lot of wrapper scripts here for doing various things like comining video  
{{% timestamp videoId="UjHR0HJJbyw" time="642" display="10:42" %}} - segments into the video and uh generating transition slides from the markdown files I have organizing the raw  
{{% timestamp videoId="UjHR0HJJbyw" time="649" display="10:49" %}} - recordings and the processed recordings and you know I won't bore you with all the details but uh I actually ran this  
{{% timestamp videoId="UjHR0HJJbyw" time="655" display="10:55" %}} - through an online like I don't know lines of code count for all the python files and it's not quite a thousand  
{{% timestamp videoId="UjHR0HJJbyw" time="662" display="11:02" %}} - lines but we're talking maybe 7 800 lines of code here and all the logic that goes into that and you know a lot  
{{% timestamp videoId="UjHR0HJJbyw" time="667" display="11:07" %}} - of research involved as well and so I kind of started this um before I released the last Ministry progress  
{{% timestamp videoId="UjHR0HJJbyw" time="674" display="11:14" %}} - summary video but it had some bugs like some of the timestamp alignment wasn't quite right and uh things like that and  
{{% timestamp videoId="UjHR0HJJbyw" time="681" display="11:21" %}} - so not only did I I finish that I added a lot of extra functionality to help automate a lot of things here so this  
{{% timestamp videoId="UjHR0HJJbyw" time="687" display="11:27" %}} - was probably the in task that took up by far the most amount of time here and I  
{{% timestamp videoId="UjHR0HJJbyw" time="693" display="11:33" %}} - mean it was kind of in fits and starts I didn't just sit there and do like two hours a day for I don't know like a very  
{{% timestamp videoId="UjHR0HJJbyw" time="699" display="11:39" %}} - long time it was you know maybe I would sit down and do like four or five hours on a Saturday at some point or you know  
{{% timestamp videoId="UjHR0HJJbyw" time="705" display="11:45" %}} - get up early in the morning and do an hour or two here and there um but you know it took me a nice long time and I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="712" display="11:52" %}} - not GNA Pretend This is perfect I think it's helping me automate a lot of the stuff in my process but you know I don't  
{{% timestamp videoId="UjHR0HJJbyw" time="719" display="11:59" %}} - know how useful it is to the World At Large because not everyone maybe structures their content the same way as me and stuff but uh not going to overly  
{{% timestamp videoId="UjHR0HJJbyw" time="726" display="12:06" %}} - belabor it but this is what I spend a lot of time on writing a lot of python code to automate parts of the video  
{{% timestamp videoId="UjHR0HJJbyw" time="733" display="12:13" %}} - processing steps that I take to try to make the content better so that is uh  
{{% timestamp videoId="UjHR0HJJbyw" time="738" display="12:18" %}} - you know I'll go over exactly what's involved in this a little bit later in one of the the future slides but this is probably what sucked the most of my time  
{{% timestamp videoId="UjHR0HJJbyw" time="745" display="12:25" %}} - away this last content cycle was focusing on on trying to get this done so that I could process all of the  
{{% timestamp videoId="UjHR0HJJbyw" time="753" display="12:33" %}} - backlog of videos that I have for the Bible basics part one study that theology proper that we've been going  
{{% timestamp videoId="UjHR0HJJbyw" time="758" display="12:38" %}} - through uh so that I wouldn't waste a bunch of time doing stuff by hand given that I was so close to finishing some of  
{{% timestamp videoId="UjHR0HJJbyw" time="765" display="12:45" %}} - the automation here um and then as part of this I kind of set up um my DOT files  
{{% timestamp videoId="UjHR0HJJbyw" time="771" display="12:51" %}} - repository again uh kind of set up a better command line environment for dealing with python stuff um so I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="778" display="12:58" %}} - using the windows subsystem for Linux uh well I guess the second version of that  
{{% timestamp videoId="UjHR0HJJbyw" time="783" display="13:03" %}} - that's actually a VM um and uh you know using a shell called well I don't  
{{% timestamp videoId="UjHR0HJJbyw" time="790" display="13:10" %}} - actually know how you pronounce this Exxon sh conch I guess is how they would have you pronounce it um but it's  
{{% timestamp videoId="UjHR0HJJbyw" time="796" display="13:16" %}} - basically a shell that's Python and uh you know a package that helps you manage virtual environments and things like  
{{% timestamp videoId="UjHR0HJJbyw" time="802" display="13:22" %}} - this uh really not interesting for most people I would suppose um I also uh  
{{% timestamp videoId="UjHR0HJJbyw" time="807" display="13:27" %}} - worked more on the keyboard project that I have been working on on and off for probably five years now um I do touch  
{{% timestamp videoId="UjHR0HJJbyw" time="814" display="13:34" %}} - type on a layer that's different than querty I've been trying to get this finished like actually finished fulltime  
{{% timestamp videoId="UjHR0HJJbyw" time="820" display="13:40" %}} - for like multiple years now because I want before I start really writing up  
{{% timestamp videoId="UjHR0HJJbyw" time="826" display="13:46" %}} - and really ramping up the the rate of production here um I want to have this done so that I am touch typing kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="833" display="13:53" %}} - in the most efficient way possible when I'm starting to write a lot more and I really am a lot closer I spent a lot of  
{{% timestamp videoId="UjHR0HJJbyw" time="840" display="14:00" %}} - winter break here so that happened in between uh the last release in October and this new content update I spent  
{{% timestamp videoId="UjHR0HJJbyw" time="847" display="14:07" %}} - couple weeks there really cleaning up the code base for this and uh you know I have a few more things to do it it kind  
{{% timestamp videoId="UjHR0HJJbyw" time="854" display="14:14" %}} - of is always in an in progress state but I'm a lot closer than I was to being ready to use this full-time every day  
{{% timestamp videoId="UjHR0HJJbyw" time="860" display="14:20" %}} - and that will be important as I start to make more content um this is probably  
{{% timestamp videoId="UjHR0HJJbyw" time="866" display="14:26" %}} - the other uh the other most important thing from this release the the other thing I spent a lot of time working with  
{{% timestamp videoId="UjHR0HJJbyw" time="873" display="14:33" %}} - is I uh made it so that I could actually have timestamps on the web pages on my  
{{% timestamp videoId="UjHR0HJJbyw" time="878" display="14:38" %}} - website uh that play the video on the page itself and so it used to be every  
{{% timestamp videoId="UjHR0HJJbyw" time="884" display="14:44" %}} - time you clicked on a timestamp it would open the video in a new tab but what happens if you want to change where you  
{{% timestamp videoId="UjHR0HJJbyw" time="890" display="14:50" %}} - are in the video on the page as you read the page or look at content so I will demo this as well I'm going to be  
{{% timestamp videoId="UjHR0HJJbyw" time="896" display="14:56" %}} - demoing kind of the output of my video video processing um all that all that  
{{% timestamp videoId="UjHR0HJJbyw" time="901" display="15:01" %}} - work I did for automation kind of show well why did I do all that what do I get out of it and then also be demoing this  
{{% timestamp videoId="UjHR0HJJbyw" time="907" display="15:07" %}} - uh page internal timestamps uh that I spent time doing to let you control the  
{{% timestamp videoId="UjHR0HJJbyw" time="913" display="15:13" %}} - videos that are actually embedded on the web pages on the Bible do site um and  
{{% timestamp videoId="UjHR0HJJbyw" time="919" display="15:19" %}} - then finally again probably not real interesting for a lot of people but I spent time figuring out how to use  
{{% timestamp videoId="UjHR0HJJbyw" time="924" display="15:24" %}} - better Greek and Hebrew fonts on web pages here you can actually specify  
{{% timestamp videoId="UjHR0HJJbyw" time="929" display="15:29" %}} - ranges of characters in Unicode if people know what Unicode is it's kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="934" display="15:34" %}} - like a uh you know the Latin alphabet has 26 letters you know lowercase and  
{{% timestamp videoId="UjHR0HJJbyw" time="940" display="15:40" %}} - uppercase and numbers and symbols and stuff but if you want to use a Greek letter or a letter in the Hebrew  
{{% timestamp videoId="UjHR0HJJbyw" time="946" display="15:46" %}} - alphabet well it's actually kind of better sometimes to use fonts that were  
{{% timestamp videoId="UjHR0HJJbyw" time="951" display="15:51" %}} - specifically designed for Greek and Hebrew um so there's a few uh some some good options um gentium is a good option  
{{% timestamp videoId="UjHR0HJJbyw" time="958" display="15:58" %}} - for Greek cardo is good as well um you know I some people like Greek I'm not a  
{{% timestamp videoId="UjHR0HJJbyw" time="964" display="16:04" %}} - big fan I like Gena much better and then s Ezra and Hebrew are probably the two  
{{% timestamp videoId="UjHR0HJJbyw" time="969" display="16:09" %}} - best Hebrew fonts and so I figured out how to actually use those on the web you know be able to host them myself and  
{{% timestamp videoId="UjHR0HJJbyw" time="975" display="16:15" %}} - specify that these are the fonts I want used for Greek and Hebrew uh you know that's just kind of something I've been meaning to do for a while but I finally  
{{% timestamp videoId="UjHR0HJJbyw" time="982" display="16:22" %}} - got around to it so uh I'm sorry that was a bit rambly uh this is a lot of kind of programm you know C stuff that I  
{{% timestamp videoId="UjHR0HJJbyw" time="990" display="16:30" %}} - was working on trying to get some of the content processing done more  
{{% timestamp videoId="UjHR0HJJbyw" time="995" display="16:35" %}} - automatically or kind of get you know my my keyboard project get my touch typing  
{{% timestamp videoId="UjHR0HJJbyw" time="1000" display="16:40" %}} - closer to the state where I'll be ready to pump out a lot more content in the long term and so uh I know I've been  
{{% timestamp videoId="UjHR0HJJbyw" time="1007" display="16:47" %}} - kind of doing these releases for gosh a couple years now keep saying you know I'm trying to make it better for the  
{{% timestamp videoId="UjHR0HJJbyw" time="1012" display="16:52" %}} - future I'm trying to make it better for the future and I mean I'm still am um but I really do think we're getting  
{{% timestamp videoId="UjHR0HJJbyw" time="1018" display="16:58" %}} - closer here especially now that a lot of the video processing automation has kind of uh it's least mostly done now I've  
{{% timestamp videoId="UjHR0HJJbyw" time="1025" display="17:05" %}} - gotten a lot of it in place that I really will start cranking up the content production here I think uh  
{{% timestamp videoId="UjHR0HJJbyw" time="1031" display="17:11" %}} - hopefully in the next few months so that is what I actually did here um you know  
{{% timestamp videoId="UjHR0HJJbyw" time="1036" display="17:16" %}} - again I did some new content stuff I had to fix the mailing list and I did a bunch of coding related things um and  
{{% timestamp videoId="UjHR0HJJbyw" time="1043" display="17:23" %}} - that's largely what I've been doing since last October  
{{% timestamp videoId="UjHR0HJJbyw" time="1050" display="17:30" %}} - so just to go into a little bit more detail although I know I've kind of talked about this already the main reason why I delayed kind of posting any  
{{% timestamp videoId="UjHR0HJJbyw" time="1059" display="17:39" %}} - new stuff or uh making any content releases until now was because I wanted  
{{% timestamp videoId="UjHR0HJJbyw" time="1065" display="17:45" %}} - to finish the bulk of the video processing automation before I processed all the videos so if I'm I'm doing all  
{{% timestamp videoId="UjHR0HJJbyw" time="1072" display="17:52" %}} - this work to to write a python application to do a lot of the work for me in an automated fashion well I kind  
{{% timestamp videoId="UjHR0HJJbyw" time="1078" display="17:58" %}} - kind of want to wait until I finish that automation before I go process my backlog of 20 videos right um and that's  
{{% timestamp videoId="UjHR0HJJbyw" time="1086" display="18:06" %}} - kind of why I ended up delaying here why this is coming out a bit later than maybe I had wanted um because I wanted  
{{% timestamp videoId="UjHR0HJJbyw" time="1093" display="18:13" %}} - to mostly finish the python application to automate all the video processing stuff before I processed all of the new  
{{% timestamp videoId="UjHR0HJJbyw" time="1100" display="18:20" %}} - videos um so kind of long story short just ended up being a little bit harder than I thought it would be it's not  
{{% timestamp videoId="UjHR0HJJbyw" time="1107" display="18:27" %}} - super surprising or unexpected you know it is not that trivial to kind of automate you know splicing all these  
{{% timestamp videoId="UjHR0HJJbyw" time="1114" display="18:34" %}} - video segments together on the command line and calculating time stamps dynamically based on the length of the  
{{% timestamp videoId="UjHR0HJJbyw" time="1119" display="18:39" %}} - video and so on and so forth um but um I do think this will end up saving me a  
{{% timestamp videoId="UjHR0HJJbyw" time="1126" display="18:46" %}} - lot of time in the long run here um because if IID done all of this stuff by hand it would have taken me hours and  
{{% timestamp videoId="UjHR0HJJbyw" time="1131" display="18:51" %}} - hours and hours and instead I spent I don't know probably right now about an equivalent amount of time actually you  
{{% timestamp videoId="UjHR0HJJbyw" time="1138" display="18:58" %}} - know coding something to do it but now moving forward in the future I won't have nearly as much uh time that I have  
{{% timestamp videoId="UjHR0HJJbyw" time="1144" display="19:04" %}} - to spend doing a bunch of tedious content processing steps um and so even  
{{% timestamp videoId="UjHR0HJJbyw" time="1149" display="19:09" %}} - as it is now um there are still things that I need to do to make this better  
{{% timestamp videoId="UjHR0HJJbyw" time="1156" display="19:16" %}} - really um there are a couple a couple to-dos that I have still on this uh  
{{% timestamp videoId="UjHR0HJJbyw" time="1162" display="19:22" %}} - video processing project that right now are still kind of manual and still pretty tedious and I have ideas for how  
{{% timestamp videoId="UjHR0HJJbyw" time="1169" display="19:29" %}} - to automate them as well but uh kind of decided that i' I've kind of gotten a  
{{% timestamp videoId="UjHR0HJJbyw" time="1174" display="19:34" %}} - lot of the way there and I want to start getting content up again you know so that I'm not just delaying for six  
{{% timestamp videoId="UjHR0HJJbyw" time="1180" display="19:40" %}} - months or even a year while I finish some of this so I'm gonna uh kind of bite the bullet and do a little bit of  
{{% timestamp videoId="UjHR0HJJbyw" time="1186" display="19:46" %}} - the process still pretty manual although I have ideas on how to fix it and that's going to be kind of some of the upcoming  
{{% timestamp videoId="UjHR0HJJbyw" time="1192" display="19:52" %}} - work that I'm going to plan to focus on you know alongside continuing to release all the new content here um  
{{% timestamp videoId="UjHR0HJJbyw" time="1199" display="19:59" %}} - but as terms of what the project does at the moment and I will demo this uh kind of in the next section we go over here  
{{% timestamp videoId="UjHR0HJJbyw" time="1206" display="20:06" %}} - um I automatically combine all these recording segments that I do so right now I'm recording with zoom that's the  
{{% timestamp videoId="UjHR0HJJbyw" time="1213" display="20:13" %}} - platform we've been using for uh recording our group Bible studies and uh I have been inserting these title  
{{% timestamp videoId="UjHR0HJJbyw" time="1221" display="20:21" %}} - transition slides between them so uh kind of black slides full screen with white text on them uh relaying the new  
{{% timestamp videoId="UjHR0HJJbyw" time="1228" display="20:28" %}} - topic so these are kind of topic Transitions and so I kind of add those  
{{% timestamp videoId="UjHR0HJJbyw" time="1233" display="20:33" %}} - uh splice everything together and then I generate timestamps automatically for all of the headers in the content and so  
{{% timestamp videoId="UjHR0HJJbyw" time="1240" display="20:40" %}} - that's kind of all the automation I maybe it doesn't sound so hard but actually getting all that to work  
{{% timestamp videoId="UjHR0HJJbyw" time="1246" display="20:46" %}} - properly and uh so for example when you add the title transition slides that  
{{% timestamp videoId="UjHR0HJJbyw" time="1251" display="20:51" %}} - adds time and you have to take that into account when you calculate the time stamps otherwise everything gets offset  
{{% timestamp videoId="UjHR0HJJbyw" time="1257" display="20:57" %}} - and the time stamps are wrong um so kind of getting all that set up these are the the things that I've added  
{{% timestamp videoId="UjHR0HJJbyw" time="1264" display="21:04" %}} - here uh and there will be other things like I mentioned that I'll go over that I'm still kind of kind of be working on  
{{% timestamp videoId="UjHR0HJJbyw" time="1269" display="21:09" %}} - in the meantime to completely automate even more of the process but for all of  
{{% timestamp videoId="UjHR0HJJbyw" time="1276" display="21:16" %}} - the hours and hours of video content that we've already recorded for this first part of Bible basics um having  
{{% timestamp videoId="UjHR0HJJbyw" time="1282" display="21:22" %}} - these things automated will save me a massive amount of time in getting all this content processed and kind of on  
{{% timestamp videoId="UjHR0HJJbyw" time="1288" display="21:28" %}} - the website in this final format that I think I finally kind of figured out how I want all the videos to be in the long  
{{% timestamp videoId="UjHR0HJJbyw" time="1295" display="21:35" %}} - term here and so doing it all before I had the Automation in place kind of just would have been time inefficient and so  
{{% timestamp videoId="UjHR0HJJbyw" time="1301" display="21:41" %}} - that's why things have been a little bit delayed  
{{% timestamp videoId="UjHR0HJJbyw" time="1306" display="21:46" %}} - here all right so as promised I'm gonna just go over kind of the briefest highest level overview here of some of  
{{% timestamp videoId="UjHR0HJJbyw" time="1313" display="21:53" %}} - this video processing stuff that I've been mentioned like what is it how does it work what effort am I saving in this  
{{% timestamp videoId="UjHR0HJJbyw" time="1321" display="22:01" %}} - so I'm just going to be going over a few Concepts here I I'll show you like one of the directories of the recordings  
{{% timestamp videoId="UjHR0HJJbyw" time="1328" display="22:08" %}} - that that you know kind of how it's set up and how the things fit together um so this is the directory here um for one of  
{{% timestamp videoId="UjHR0HJJbyw" time="1336" display="22:16" %}} - the recordings that I've already processed so this is the very first lesson in this Bible basics part one  
{{% timestamp videoId="UjHR0HJJbyw" time="1341" display="22:21" %}} - series that we've been going over for theology proper uh discussing the essence of God and so I have uh script  
{{% timestamp videoId="UjHR0HJJbyw" time="1348" display="22:28" %}} - that automatically generates this kind of directory structure once I say okay  
{{% timestamp videoId="UjHR0HJJbyw" time="1354" display="22:34" %}} - I'm ready to make a recording I go to the content directory and you know execute something on the command line  
{{% timestamp videoId="UjHR0HJJbyw" time="1359" display="22:39" %}} - that kind of builds out the right directories and so this file here the Excel file titled segments. xlsx that  
{{% timestamp videoId="UjHR0HJJbyw" time="1367" display="22:47" %}} - contains all of the recording segments that I'm planning to to record and so um I kind of have them in an Excel file and  
{{% timestamp videoId="UjHR0HJJbyw" time="1375" display="22:55" %}} - each row in that Excel file represents one of the recordings that I want to make for each section and so those kind  
{{% timestamp videoId="UjHR0HJJbyw" time="1382" display="23:02" %}} - of correspond to headers within the content and so once I have recorded that  
{{% timestamp videoId="UjHR0HJJbyw" time="1387" display="23:07" %}} - the recordings end up in a subdirectory here so I'm in the recording directory  
{{% timestamp videoId="UjHR0HJJbyw" time="1392" display="23:12" %}} - for this particular lesson in the study and then you go into the recording subdirectory and then I dump all of the  
{{% timestamp videoId="UjHR0HJJbyw" time="1398" display="23:18" %}} - files into the raw folder here and so these are nice and pretty you know I I  
{{% timestamp videoId="UjHR0HJJbyw" time="1404" display="23:24" %}} - numbered them in sequential order by tens but I did that automatic I that isn't how they come out of Zoom I clean  
{{% timestamp videoId="UjHR0HJJbyw" time="1410" display="23:30" %}} - them up to do this to get them in order and then I process them to remove silence in between uh kind of like  
{{% timestamp videoId="UjHR0HJJbyw" time="1417" display="23:37" %}} - awkward pauses within uh the video so if there's like a a silence while we begin  
{{% timestamp videoId="UjHR0HJJbyw" time="1423" display="23:43" %}} - or end a segment or you know if we're waiting for someone to unmute themselves when they're talking on the recording or  
{{% timestamp videoId="UjHR0HJJbyw" time="1429" display="23:49" %}} - something like that I can just cut out usually it ends up being maybe 15 or 20 seconds of Silence on some of the longer  
{{% timestamp videoId="UjHR0HJJbyw" time="1435" display="23:55" %}} - recordings or even a couple minutes depending of just kind of what ends up not being useful content you know you  
{{% timestamp videoId="UjHR0HJJbyw" time="1441" display="24:01" %}} - don't need to sit there in the video and you know watch as we wait for someone to unmute themselves to talk we can just  
{{% timestamp videoId="UjHR0HJJbyw" time="1447" display="24:07" %}} - take that out and it reduces the length of the video even if it's not by much and so that's mostly what the processing  
{{% timestamp videoId="UjHR0HJJbyw" time="1454" display="24:14" %}} - is here um I can also clean up the audio some although I haven't had to do that recently since we've had better audio  
{{% timestamp videoId="UjHR0HJJbyw" time="1459" display="24:19" %}} - but uh so that's what those two directories are and then there's another directory for containing the uh topic  
{{% timestamp videoId="UjHR0HJJbyw" time="1466" display="24:26" %}} - transition slides that I've mentioned and so uh I'll show you what these look like in a second once we actually look at the video but I record these  
{{% timestamp videoId="UjHR0HJJbyw" time="1472" display="24:32" %}} - separately and then uh the application that I've written takes the processed  
{{% timestamp videoId="UjHR0HJJbyw" time="1478" display="24:38" %}} - video files and then combines them with these topic transition video segments  
{{% timestamp videoId="UjHR0HJJbyw" time="1483" display="24:43" %}} - and splices them all together to make the video file that's in kind of like the root recording directory for this  
{{% timestamp videoId="UjHR0HJJbyw" time="1489" display="24:49" %}} - lesson and then after I've made the video uh I have to add chapters to it um  
{{% timestamp videoId="UjHR0HJJbyw" time="1495" display="24:55" %}} - and so that those correspond with all of the segment boundaries so the headers in  
{{% timestamp videoId="UjHR0HJJbyw" time="1501" display="25:01" %}} - the uh the content the timestamps basically for each section and so I do  
{{% timestamp videoId="UjHR0HJJbyw" time="1506" display="25:06" %}} - that I make a metadata file I attach that to the video and then I actually um  
{{% timestamp videoId="UjHR0HJJbyw" time="1512" display="25:12" %}} - I actually automatically generate the description that I need to paste into uh  
{{% timestamp videoId="UjHR0HJJbyw" time="1518" display="25:18" %}} - the Youtube video when I'm uploading the video to release it on YouTube so you know like the playlist link and the link  
{{% timestamp videoId="UjHR0HJJbyw" time="1524" display="25:24" %}} - to the content on Bible docs the link to the slides on Bible docs the summary and then all these timestamps well these are  
{{% timestamp videoId="UjHR0HJJbyw" time="1531" display="25:31" %}} - the things that show up as chapters in the metadata and also these are the timestamps that I'm automatically  
{{% timestamp videoId="UjHR0HJJbyw" time="1537" display="25:37" %}} - generating so that's kind of the the overall structure of how how the  
{{% timestamp videoId="UjHR0HJJbyw" time="1542" display="25:42" %}} - recording directories work um and so uh that you know maybe it's kind of just  
{{% timestamp videoId="UjHR0HJJbyw" time="1548" display="25:48" %}} - gwiz information here um there's a lot of effort that kind of goes into automating all that you know I have to  
{{% timestamp videoId="UjHR0HJJbyw" time="1554" display="25:54" %}} - have this consistent directory structure so that the application knows kind of what directories it needs to expect all  
{{% timestamp videoId="UjHR0HJJbyw" time="1561" display="26:01" %}} - these different files in and stuff but in the end you end up getting videos that I can upload to Youtube and you  
{{% timestamp videoId="UjHR0HJJbyw" time="1567" display="26:07" %}} - know just copy paste the YouTube description and then you know it has like we were just looking at in the text  
{{% timestamp videoId="UjHR0HJJbyw" time="1572" display="26:12" %}} - file version of this you know has links to the web page content the slides content the summary and then all these  
{{% timestamp videoId="UjHR0HJJbyw" time="1578" display="26:18" %}} - timestamps here and um you know again just saying oh well you're timestamping  
{{% timestamp videoId="UjHR0HJJbyw" time="1585" display="26:25" %}} - all the headers the big deal about this is that this that you see right here with all these timestamps is actually  
{{% timestamp videoId="UjHR0HJJbyw" time="1591" display="26:31" %}} - completely automatically generated so the only thing that I have to do is write my content uh as I always do in in  
{{% timestamp videoId="UjHR0HJJbyw" time="1598" display="26:38" %}} - my markdown files and and you know have my headers and subheaders for the topics that we talk about and then I just  
{{% timestamp videoId="UjHR0HJJbyw" time="1605" display="26:45" %}} - record the recording in such a way that I I kind of record each section separately and then stop the recording  
{{% timestamp videoId="UjHR0HJJbyw" time="1611" display="26:51" %}} - and restart for each new section so that I have these uh these nice separable recording segments for each of the  
{{% timestamp videoId="UjHR0HJJbyw" time="1618" display="26:58" %}} - sections and then I run my script and out pops everything that you see here completely automatically and so that's  
{{% timestamp videoId="UjHR0HJJbyw" time="1625" display="27:05" %}} - just kind of a taste of what this looks like and now to see what the uh transition slides look like um so this  
{{% timestamp videoId="UjHR0HJJbyw" time="1631" display="27:11" %}} - is 49 minutes into this recording if I click on this timestamp link you'll see that um now when I go to that timestamp  
{{% timestamp videoId="UjHR0HJJbyw" time="1639" display="27:19" %}} - in the video um there's this nice transition between the content that comes before it so I'll go back just a  
{{% timestamp videoId="UjHR0HJJbyw" time="1645" display="27:25" %}} - little bit here um I go maybe a little bit more back um you know  
{{% timestamp videoId="UjHR0HJJbyw" time="1651" display="27:31" %}} - this video is playing this video is playing you know we're talking about something looks like here we are in 2  
{{% timestamp videoId="UjHR0HJJbyw" time="1656" display="27:36" %}} - Corinthians chapter 3 and then after that um when you get to one of these  
{{% timestamp videoId="UjHR0HJJbyw" time="1662" display="27:42" %}} - topic transitions um which I guess it'll take a few more seconds here um but you kind of have this pause this ability for  
{{% timestamp videoId="UjHR0HJJbyw" time="1670" display="27:50" %}} - the video to be silent for several seconds uh as we transition topics and then we pick up with the next one and so  
{{% timestamp videoId="UjHR0HJJbyw" time="1676" display="27:56" %}} - it looks real sharp uh and and when you're kind of transitioning between things in the  
{{% timestamp videoId="UjHR0HJJbyw" time="1682" display="28:02" %}} - video so that uh people who are watching this especially on a faster playback speed won't have I don't know the the  
{{% timestamp videoId="UjHR0HJJbyw" time="1689" display="28:09" %}} - the topics bleed into each other as much it makes a lot of sense um this is something else I've wanted to do for a  
{{% timestamp videoId="UjHR0HJJbyw" time="1695" display="28:15" %}} - while but I hadn't figured out a way to kind of automate it until recently um  
{{% timestamp videoId="UjHR0HJJbyw" time="1700" display="28:20" %}} - and so if I were to try to do all this by hand in a video editor you know it would take hours and hours and hours for all the videos I have but the point of  
{{% timestamp videoId="UjHR0HJJbyw" time="1707" display="28:27" %}} - all this this kind of rambling that I'm doing here is that I set all of this stuff up to basically happen all on its  
{{% timestamp videoId="UjHR0HJJbyw" time="1714" display="28:34" %}} - own um so I run a couple commands on the command line and then it magically does everything else that is the idea and in  
{{% timestamp videoId="UjHR0HJJbyw" time="1720" display="28:40" %}} - fact now I have it so that that is actually more or less what it does so this was that thing that I mentioned  
{{% timestamp videoId="UjHR0HJJbyw" time="1727" display="28:47" %}} - that I spent most of my time on here was making all of this stuff work properly so that I can record my video segments  
{{% timestamp videoId="UjHR0HJJbyw" time="1734" display="28:54" %}} - and run a couple commands and then have everything basically come out ready for me to upload to Youtube just like  
{{% timestamp videoId="UjHR0HJJbyw" time="1743" display="29:03" %}} - that so I actually realized that I kind of combined this new section here with  
{{% timestamp videoId="UjHR0HJJbyw" time="1748" display="29:08" %}} - what I was just talking about but um I should say that everything that I just talked about for the videos on YouTube  
{{% timestamp videoId="UjHR0HJJbyw" time="1756" display="29:16" %}} - it actually holds true for all of the videos in the playlist and so it's not just like one or two it's going to be  
{{% timestamp videoId="UjHR0HJJbyw" time="1763" display="29:23" %}} - everything that I upload that will have been processed in this way and so uh you  
{{% timestamp videoId="UjHR0HJJbyw" time="1769" display="29:29" %}} - can see it on YouTube actually but you can also see it on the videos as they're embedded in the website here and so um I  
{{% timestamp videoId="UjHR0HJJbyw" time="1777" display="29:37" %}} - you know showed you what one of those uh slide transitions looks like on the YouTube video but it also holds just as  
{{% timestamp videoId="UjHR0HJJbyw" time="1783" display="29:43" %}} - much in the videos when they're embedded and so I'll get to the embedded timestamps in a second here but you know  
{{% timestamp videoId="UjHR0HJJbyw" time="1789" display="29:49" %}} - this is what we were just talking about all of that automation that helps kind  
{{% timestamp videoId="UjHR0HJJbyw" time="1795" display="29:55" %}} - of produce these these clean looking videos in the end that has has those nice transitions between topics uh and  
{{% timestamp videoId="UjHR0HJJbyw" time="1802" display="30:02" %}} - these time stamps that are actually time accurate for everything this was just the demo of kind of what it all looks  
{{% timestamp videoId="UjHR0HJJbyw" time="1809" display="30:09" %}} - like in its output form all right and so the other thing  
{{% timestamp videoId="UjHR0HJJbyw" time="1816" display="30:16" %}} - that I said I was going to demo here were the page internal timestamps and if  
{{% timestamp videoId="UjHR0HJJbyw" time="1821" display="30:21" %}} - you're a software developer uh you kind of manage these by using the API that  
{{% timestamp videoId="UjHR0HJJbyw" time="1826" display="30:26" %}} - YouTube has for embedding video iframes on your website and so it's all  
{{% timestamp videoId="UjHR0HJJbyw" time="1832" display="30:32" %}} - JavaScript here um you know I'm not writing anything else because I'm embedding these on web pages so uh it  
{{% timestamp videoId="UjHR0HJJbyw" time="1838" display="30:38" %}} - took me kind of a while to piece through the API and figure out what I needed to do here but I actually added a cookie on  
{{% timestamp videoId="UjHR0HJJbyw" time="1845" display="30:45" %}} - the website on the settings page that lets you uh basically set whether you  
{{% timestamp videoId="UjHR0HJJbyw" time="1850" display="30:50" %}} - want timestamps on the website to the internal links that change uh where the  
{{% timestamp videoId="UjHR0HJJbyw" time="1856" display="30:56" %}} - embedded video is playing or whether you want to make them external links that actually open the video in a new tab so  
{{% timestamp videoId="UjHR0HJJbyw" time="1863" display="31:03" %}} - if I go back to this page right now and I click on one of these timestamps you'll actually see that it changes the  
{{% timestamp videoId="UjHR0HJJbyw" time="1869" display="31:09" %}} - time in the video directly um and uh if I change that setting so I actually have  
{{% timestamp videoId="UjHR0HJJbyw" time="1876" display="31:16" %}} - it so that you can change the setting uh in a global sense through the settings  
{{% timestamp videoId="UjHR0HJJbyw" time="1882" display="31:22" %}} - page here um well if you do that then you can actually uh basically change  
{{% timestamp videoId="UjHR0HJJbyw" time="1889" display="31:29" %}} - whether you want the links to open in an external tab or whether you want them to control the video now if you're on a  
{{% timestamp videoId="UjHR0HJJbyw" time="1894" display="31:34" %}} - specific page just like many the other toggles I have I actually let you um control that toggle here so you know if  
{{% timestamp videoId="UjHR0HJJbyw" time="1901" display="31:41" %}} - you see here when I'm changing these These are changing the time in that embedded video at the top of the screen  
{{% timestamp videoId="UjHR0HJJbyw" time="1906" display="31:46" %}} - um well if I toggle this then actually now if I click one of these it'll open in a new tab and so you can dynamically  
{{% timestamp videoId="UjHR0HJJbyw" time="1914" display="31:54" %}} - toggle that on a per page basis as well and if I toggle it back then you'll see that now we're changing in the embedded  
{{% timestamp videoId="UjHR0HJJbyw" time="1919" display="31:59" %}} - video again um so that's pretty cool you can also toggle it for the whole site like I said on that settings page on the  
{{% timestamp videoId="UjHR0HJJbyw" time="1925" display="32:05" %}} - other cool thing that I did was I set it up so that you know even if the video is playing up here at the top so uh you  
{{% timestamp videoId="UjHR0HJJbyw" time="1932" display="32:12" %}} - know you can see the the bar is ticking stuff's happening in the video well if you scroll down and you're reading  
{{% timestamp videoId="UjHR0HJJbyw" time="1937" display="32:17" %}} - something or you're listening to the audio and you're trying to follow along in the page links if you ever want to jump back to the video I put a link in  
{{% timestamp videoId="UjHR0HJJbyw" time="1944" display="32:24" %}} - the sidebar that Scrolls you back up to the video um and so this is more useful perhaps on aggregation pages that have a  
{{% timestamp videoId="UjHR0HJJbyw" time="1952" display="32:32" %}} - a bunch of study lessons kind of all smooshed together on one page for searching and skimming well if you have  
{{% timestamp videoId="UjHR0HJJbyw" time="1959" display="32:39" %}} - one video playing and you're not exactly sure where it is on the page you can use this link in the sidebar to just always  
{{% timestamp videoId="UjHR0HJJbyw" time="1964" display="32:44" %}} - take you back up to the video and the other thing let's make sure I'm not missing anything here in what I'm going  
{{% timestamp videoId="UjHR0HJJbyw" time="1971" display="32:51" %}} - over all right the other thing that's really useful about everything that I've set up here is if you ever want to find  
{{% timestamp videoId="UjHR0HJJbyw" time="1977" display="32:57" %}} - where we talk about something in a video uh so you know all the content is on these pages in the content section in  
{{% timestamp videoId="UjHR0HJJbyw" time="1983" display="33:03" %}} - the table of contents over here but if you ever want to search through the transcript so that you can hear exactly  
{{% timestamp videoId="UjHR0HJJbyw" time="1989" display="33:09" %}} - where we are going to be talking about something you can go down to the transcript and then you can search on  
{{% timestamp videoId="UjHR0HJJbyw" time="1994" display="33:14" %}} - the page this is just normal search in browsers you know this is nothing special about this and uh in this first  
{{% timestamp videoId="UjHR0HJJbyw" time="2001" display="33:21" %}} - lesson when we're going over the essence of god let's say I want to go search for where we talked about uh so-called  
{{% timestamp videoId="UjHR0HJJbyw" time="2007" display="33:27" %}} - essential characteristics right and this is something that comes up when you talk about like what makes God God so  
{{% timestamp videoId="UjHR0HJJbyw" time="2015" display="33:35" %}} - characterist got to figure out how to spell here so you can see I actually tag um some sections here this is in the  
{{% timestamp videoId="UjHR0HJJbyw" time="2021" display="33:41" %}} - content so those are the first couple matches but now I'm down in the transcript and you know this is real far  
{{% timestamp videoId="UjHR0HJJbyw" time="2027" display="33:47" %}} - down on the page you can see in the scroll bar here and if I want to go play say 55 minutes into the video you can  
{{% timestamp videoId="UjHR0HJJbyw" time="2033" display="33:53" %}} - see we're talking about essential characteristics and um you know we're talking about what God is and what makes  
{{% timestamp videoId="UjHR0HJJbyw" time="2039" display="33:59" %}} - God God and things well if I want to go play this uh I'll scroll back up in a second but I can go ahead and just click  
{{% timestamp videoId="UjHR0HJJbyw" time="2044" display="34:04" %}} - on the timestamp now the video is playing 55 minutes in and if I jump back to the video you can see that we're 55  
{{% timestamp videoId="UjHR0HJJbyw" time="2050" display="34:10" %}} - minutes in and so what's really useful is that you can actually use a full text search on the page to search the  
{{% timestamp videoId="UjHR0HJJbyw" time="2056" display="34:16" %}} - transcripts of all the videos that we've done to figure out when we talk about stuff and then you can just click the  
{{% timestamp videoId="UjHR0HJJbyw" time="2063" display="34:23" %}} - link and then you'll have the audio immediately you know playing in your ears for exactly that text maps that you  
{{% timestamp videoId="UjHR0HJJbyw" time="2071" display="34:31" %}} - found so it basically lets you full text search the video which is something that is super super powerful and so I've  
{{% timestamp videoId="UjHR0HJJbyw" time="2078" display="34:38" %}} - already taken advantage of this myself a little bit you know trying to find where did we talk about this and you know this  
{{% timestamp videoId="UjHR0HJJbyw" time="2084" display="34:44" %}} - study or this study and eventually all of these transcripts will show up indexed on Google searches as well which  
{{% timestamp videoId="UjHR0HJJbyw" time="2090" display="34:50" %}} - will let you kind of search all of the uh content on Bible docs that much more powerfully so I'm happy with how this  
{{% timestamp videoId="UjHR0HJJbyw" time="2097" display="34:57" %}} - turned out having those timestamps on the page and then being able to jump back to the video it really lets you  
{{% timestamp videoId="UjHR0HJJbyw" time="2103" display="35:03" %}} - figure out uh or sorry really lets you use this workflow where you search for things uh just like how you normally  
{{% timestamp videoId="UjHR0HJJbyw" time="2110" display="35:10" %}} - search for things but then you can immediately go there in the video and that's that's super cool um it's something that I've wanted to support  
{{% timestamp videoId="UjHR0HJJbyw" time="2116" display="35:16" %}} - for a while but I finally got around to kind of doing all the coding in the JavaScript to to let you do that um so  
{{% timestamp videoId="UjHR0HJJbyw" time="2123" display="35:23" %}} - uh in action like I said here you know all the timestamps on pages so not on YouTube but on uh the embedded pages on  
{{% timestamp videoId="UjHR0HJJbyw" time="2130" display="35:30" %}} - my website now you can change uh where you are in the video that's on the page so that you have audio playing on the  
{{% timestamp videoId="UjHR0HJJbyw" time="2136" display="35:36" %}} - page or like I said if you prefer you can toggle it or set the global setting so that your time STP links actually  
{{% timestamp videoId="UjHR0HJJbyw" time="2143" display="35:43" %}} - still open it up on YouTube and you know that'd be if you want to see I don't know like the comments on the YouTube  
{{% timestamp videoId="UjHR0HJJbyw" time="2148" display="35:48" %}} - video or you just rather view it on YouTube um that's still an option as well so that's kind of a demo of all of  
{{% timestamp videoId="UjHR0HJJbyw" time="2155" display="35:55" %}} - the timestamp stuff that I also added to the website in this content release  
{{% timestamp videoId="UjHR0HJJbyw" time="2163" display="36:03" %}} - cycle all right so kind of last main thing we're going to talk about here is now that I have all the stuff that I  
{{% timestamp videoId="UjHR0HJJbyw" time="2170" display="36:10" %}} - kind of just demoed uh set up so that on a new video recording I kind of have all  
{{% timestamp videoId="UjHR0HJJbyw" time="2176" display="36:16" %}} - this stuff happen automatically you know I record the the sorry I splice all the video recordings together with the topic  
{{% timestamp videoId="UjHR0HJJbyw" time="2182" display="36:22" %}} - Transitions and I timestamp it and I build that YouTube description automatically and all of the time stamps  
{{% timestamp videoId="UjHR0HJJbyw" time="2187" display="36:27" %}} - now just kind of work on the website and let you full teex search the transcripts and all that all that stuff is now set  
{{% timestamp videoId="UjHR0HJJbyw" time="2194" display="36:34" %}} - up but now that I have all of that I'm kind of ready to to kind of start  
{{% timestamp videoId="UjHR0HJJbyw" time="2199" display="36:39" %}} - producing videos uh kind of more weekly or or bi-weekly depending on our schedule but being really consistent  
{{% timestamp videoId="UjHR0HJJbyw" time="2206" display="36:46" %}} - about it because I have the structure how I think I want it kind of in perpetuity now so I I can't think of a  
{{% timestamp videoId="UjHR0HJJbyw" time="2213" display="36:53" %}} - lot that I will ever want to change about this now that I've kind of done all that leg work get it all set up this  
{{% timestamp videoId="UjHR0HJJbyw" time="2218" display="36:58" %}} - is how I want the content to be uh you know for the next 10 20 years even uh  
{{% timestamp videoId="UjHR0HJJbyw" time="2223" display="37:03" %}} - you know we'll see how long this channel sticks around but um because I have it kind of in the form that I want to  
{{% timestamp videoId="UjHR0HJJbyw" time="2229" display="37:09" %}} - repeat um so I kind of have the template set up now and I have everything in place to make it repeatable in a  
{{% timestamp videoId="UjHR0HJJbyw" time="2236" display="37:16" %}} - sustainable sort of way so I really am planning on uh going through that video  
{{% timestamp videoId="UjHR0HJJbyw" time="2241" display="37:21" %}} - backlog that I have now and releasing I'm going to set a a pretty modest Target for myself of maybe two two  
{{% timestamp videoId="UjHR0HJJbyw" time="2247" display="37:27" %}} - videos a week here for the next few weeks going at least get two videos a week out from that backlog that we have  
{{% timestamp videoId="UjHR0HJJbyw" time="2253" display="37:33" %}} - making sure that they're all processed they're all fully Polished in this in this form and that they show up properly  
{{% timestamp videoId="UjHR0HJJbyw" time="2259" display="37:39" %}} - on the website that way we'll get through that backlog of 20 25 videos we have uh for this study that we've been  
{{% timestamp videoId="UjHR0HJJbyw" time="2265" display="37:45" %}} - going through and once I catch back up then as soon as we have a new lesson from our group Bible studies on the  
{{% timestamp videoId="UjHR0HJJbyw" time="2272" display="37:52" %}} - weekends I'll actually post it as soon as I'm done recording it and so as soon as we finish something I'll have it up  
{{% timestamp videoId="UjHR0HJJbyw" time="2277" display="37:57" %}} - on the YouTube channel within a day or two um that's going to be the goal moving forward here and so if you are  
{{% timestamp videoId="UjHR0HJJbyw" time="2284" display="38:04" %}} - not already subscribed to the YouTube channel you want to stay up todate with all of the new releases that are going  
{{% timestamp videoId="UjHR0HJJbyw" time="2289" display="38:09" %}} - to be rolling out over the next couple months I would recommend you do that because that way you'll be notified uh  
{{% timestamp videoId="UjHR0HJJbyw" time="2295" display="38:15" %}} - well if you tap the Bell on for the subscriptions at least you'll be notified uh whenever I post the new videos here um and so that will be  
{{% timestamp videoId="UjHR0HJJbyw" time="2302" display="38:22" %}} - something that is going to happen like I said I'm not going to do it all at once it'll probably be a couple videos a week for the next few weeks here here but I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="2308" display="38:28" %}} - going to be releasing content much more consistently now hopefully carrying this  
{{% timestamp videoId="UjHR0HJJbyw" time="2313" display="38:33" %}} - onward kind of as we go here into the future like I hopefully I won't have any more of these big pauses now because I  
{{% timestamp videoId="UjHR0HJJbyw" time="2320" display="38:40" %}} - have all of the stuff in place to let me do this sustainably you know it's not going to be a huge drain on my time  
{{% timestamp videoId="UjHR0HJJbyw" time="2325" display="38:45" %}} - since I've automated so much of this that every single week we make a new recording I can just uh pop over to the  
{{% timestamp videoId="UjHR0HJJbyw" time="2332" display="38:52" %}} - command line run a couple things and then the video's ready I don't have to sit there and do as much work as I have  
{{% timestamp videoId="UjHR0HJJbyw" time="2337" display="38:57" %}} - been doing doing in the past to get everything ready to go up and so the upshot of that is that hopefully I can  
{{% timestamp videoId="UjHR0HJJbyw" time="2342" display="39:02" %}} - do this week after week after week without it actually being a burden um and so I can do it much more sustainably  
{{% timestamp videoId="UjHR0HJJbyw" time="2348" display="39:08" %}} - which means we won't have gaps in content anymore at least that's the goal in the idea  
{{% timestamp videoId="UjHR0HJJbyw" time="2357" display="39:17" %}} - here all right finally gonna talk about my upcoming plans kind of just how I've  
{{% timestamp videoId="UjHR0HJJbyw" time="2362" display="39:22" %}} - always done in these Ministry progress summaries what are the things that I'm planning on focusing on in the near  
{{% timestamp videoId="UjHR0HJJbyw" time="2367" display="39:27" %}} - future what are my next goals kind of how am I going to be spending my time in the next few weeks here um so first of  
{{% timestamp videoId="UjHR0HJJbyw" time="2373" display="39:33" %}} - all like we were just talking about I'm going to be focusing on uh getting the full backlog of ready videos that I have  
{{% timestamp videoId="UjHR0HJJbyw" time="2379" display="39:39" %}} - up and posted to YouTube kind of in in all of the processed form you know with the the pretty transition slides and the  
{{% timestamp videoId="UjHR0HJJbyw" time="2386" display="39:46" %}} - time stamps the hyperlink to the embedded video and all that um get all of the content that I have kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="2392" display="39:52" %}} - sitting that's ready that I just need to get up on the site uh I think it's about 20 videos at present um and so uh I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="2400" display="40:00" %}} - going to be doing that that's going to be a main focus here I want to get through that backlog so that I'm kind of like not in a hole anymore so that I can  
{{% timestamp videoId="UjHR0HJJbyw" time="2408" display="40:08" %}} - kind of keep up with it week after week after that so that I don't have uh kind of this growing backlog that I have to  
{{% timestamp videoId="UjHR0HJJbyw" time="2414" display="40:14" %}} - get out from under um so that's going to be kind of priority number one uh in the next little bit now we are also going to  
{{% timestamp videoId="UjHR0HJJbyw" time="2420" display="40:20" %}} - be finishing our Bible basics part one study that I've mentioned several times here we're actually really close to the  
{{% timestamp videoId="UjHR0HJJbyw" time="2426" display="40:26" %}} - end so as I mentioned we're talking about christophanies in the Old Testament which is actually the last big section in the study and so we'll  
{{% timestamp videoId="UjHR0HJJbyw" time="2432" display="40:32" %}} - actually probably finish this study in several weeks time uh you know I don't know exactly how soon it might be three  
{{% timestamp videoId="UjHR0HJJbyw" time="2437" display="40:37" %}} - or four um but after that I think I'm going to have us start doing christology  
{{% timestamp videoId="UjHR0HJJbyw" time="2443" display="40:43" %}} - or soteriology uh these are other sections of that uh Systematic Theology on ichus uh talking about uh Jesus  
{{% timestamp videoId="UjHR0HJJbyw" time="2451" display="40:51" %}} - Christ or salvation respectively I haven't quite decided which one of these we're going to do but I think that's  
{{% timestamp videoId="UjHR0HJJbyw" time="2456" display="40:56" %}} - probably where we're going to next so I'm just going to keep making more content from that group Bible study that  
{{% timestamp videoId="UjHR0HJJbyw" time="2461" display="41:01" %}} - we've been having kind of just how we have been doing for the last year or so now as we pick back up in this Bible  
{{% timestamp videoId="UjHR0HJJbyw" time="2467" display="41:07" %}} - basic series um and then as it relates to some of my other goals here in the  
{{% timestamp videoId="UjHR0HJJbyw" time="2473" display="41:13" %}} - immediate short- term I have three other things I want to do um I want to actually set up uh complete automation  
{{% timestamp videoId="UjHR0HJJbyw" time="2480" display="41:20" %}} - for silence removal in the video processing so I mentioned right now that uh that's kind of what the processed  
{{% timestamp videoId="UjHR0HJJbyw" time="2486" display="41:26" %}} - video segments are they cut out kind of extraneous uh time in the clips where no  
{{% timestamp videoId="UjHR0HJJbyw" time="2491" display="41:31" %}} - one's saying anything it's just kind of dead content um well I am using a kind of a graphical user interface tool to do  
{{% timestamp videoId="UjHR0HJJbyw" time="2497" display="41:37" %}} - that right now um I have a command line tool that will do this but the problem I've had is that the recordings that  
{{% timestamp videoId="UjHR0HJJbyw" time="2505" display="41:45" %}} - Zoom spits out they just seem to go kind of crazy in the command line version of it and so I don't really know why um I  
{{% timestamp videoId="UjHR0HJJbyw" time="2512" display="41:52" %}} - think both tools are using FFM Peg on the back end one of them is a python rapper for it that's the one that's on  
{{% timestamp videoId="UjHR0HJJbyw" time="2518" display="41:58" %}} - the command line and I don't really know why it's causing all these bugs but I haven't been able to completely automate  
{{% timestamp videoId="UjHR0HJJbyw" time="2524" display="42:04" %}} - it because I can't use the scripal version of it because python recordings don't seem to play nice with it so um I  
{{% timestamp videoId="UjHR0HJJbyw" time="2531" display="42:11" %}} - have had on my to-do list for a while now seeing if I can switch us to a different uh kind of group video meeting  
{{% timestamp videoId="UjHR0HJJbyw" time="2537" display="42:17" %}} - application so uh either Microsoft teams or Google meet or uh you know the brave  
{{% timestamp videoId="UjHR0HJJbyw" time="2544" display="42:24" %}} - browser actually has a meeting thing built in you know I I don't know which of these I think I'm going to try to have us use Microsoft teams next um just  
{{% timestamp videoId="UjHR0HJJbyw" time="2551" display="42:31" %}} - because it's pretty feature Rich and uh it's kind of a drop in replacement for Zoom but hopefully uh the recordings  
{{% timestamp videoId="UjHR0HJJbyw" time="2558" display="42:38" %}} - from Microsoft teams won't interfere with the video processing in this way so that I can use the completely automated  
{{% timestamp videoId="UjHR0HJJbyw" time="2565" display="42:45" %}} - command line version of the tool and that will cut out one of the steps that is right now still kind of manual for me  
{{% timestamp videoId="UjHR0HJJbyw" time="2571" display="42:51" %}} - um it doesn't take super long maybe a half hour or so to go do it all but it's a half hour per video that is otherwise  
{{% timestamp videoId="UjHR0HJJbyw" time="2578" display="42:58" %}} - kind of preventable so I want to do this again before I start really cranking up  
{{% timestamp videoId="UjHR0HJJbyw" time="2583" display="43:03" %}} - the content production Pace I want to have everything completely automated and so I'm trying to knock out the stuff  
{{% timestamp videoId="UjHR0HJJbyw" time="2590" display="43:10" %}} - that right now is not completely automated even if it's a lot closer um and in that vein I'm also going to try  
{{% timestamp videoId="UjHR0HJJbyw" time="2595" display="43:15" %}} - to automate the transition uh segments a little bit more so right now I am automatically generating the transition  
{{% timestamp videoId="UjHR0HJJbyw" time="2602" display="43:22" %}} - slides from the content so those nice black slides you see that transition between segments in the video I am  
{{% timestamp videoId="UjHR0HJJbyw" time="2609" display="43:29" %}} - creating the slides that show that I'm creating those automatically but right now I have to actually manually go in  
{{% timestamp videoId="UjHR0HJJbyw" time="2615" display="43:35" %}} - and record A short segment for each one of those and you know then I run a script that actually standardizes the  
{{% timestamp videoId="UjHR0HJJbyw" time="2621" display="43:41" %}} - length of all of them to three seconds and spices them all together but you know I still have to do this extra step  
{{% timestamp videoId="UjHR0HJJbyw" time="2626" display="43:46" %}} - of manually recording all those and um I think there's a way for me to automatically generate the video  
{{% timestamp videoId="UjHR0HJJbyw" time="2633" display="43:53" %}} - segments from uh the slides if I figure out how to save each slide as an image  
{{% timestamp videoId="UjHR0HJJbyw" time="2638" display="43:58" %}} - uh you know of the right resolution 1920 x 1080 then I can use ffmpeg to turn  
{{% timestamp videoId="UjHR0HJJbyw" time="2643" display="44:03" %}} - those images into 3se second videos without audio tracks and then I can splice it all together uh hopefully  
{{% timestamp videoId="UjHR0HJJbyw" time="2649" display="44:09" %}} - without having to do anything manual at all um so those are two more uh things  
{{% timestamp videoId="UjHR0HJJbyw" time="2654" display="44:14" %}} - that I want to set up in the video processing automation that I've been working on for the last little bit and  
{{% timestamp videoId="UjHR0HJJbyw" time="2660" display="44:20" %}} - if I do those two things um I still need to automate the uh the transcript part  
{{% timestamp videoId="UjHR0HJJbyw" time="2666" display="44:26" %}} - of it a little bit more too so right now I am copy pasting the transcript off of YouTube into a spreadsheet basically  
{{% timestamp videoId="UjHR0HJJbyw" time="2674" display="44:34" %}} - like Excel and I'm using some regular Expressions to extract the timestamps and then build all the short codes and  
{{% timestamp videoId="UjHR0HJJbyw" time="2680" display="44:40" %}} - stuff but I still have to go do that every new video and uh there is a library that will let you download uh  
{{% timestamp videoId="UjHR0HJJbyw" time="2687" display="44:47" %}} - the transcript from a YouTube video Once you set up a YouTube API key in your application and I need to go look into  
{{% timestamp videoId="UjHR0HJJbyw" time="2693" display="44:53" %}} - that as well so that I can completely automate that um I'm going to start with these two things because the transcript  
{{% timestamp videoId="UjHR0HJJbyw" time="2698" display="44:58" %}} - stuff only takes me maybe five minutes it's not bad at all um these things take me a little bit longer and so I'm going  
{{% timestamp videoId="UjHR0HJJbyw" time="2704" display="45:04" %}} - to try to eliminate every single manual step from the process um I think it's possible I just need to do more uh some  
{{% timestamp videoId="UjHR0HJJbyw" time="2711" display="45:11" %}} - more software development here to get all of the remaining to-dos done um and  
{{% timestamp videoId="UjHR0HJJbyw" time="2716" display="45:16" %}} - then finally um I also want to set up a podcast for all of the content that  
{{% timestamp videoId="UjHR0HJJbyw" time="2721" display="45:21" %}} - we've been making here so I have identified the platform I want to host the podcast with it's a a platform  
{{% timestamp videoId="UjHR0HJJbyw" time="2728" display="45:28" %}} - called podbean um and it will automatically publish the podcast to  
{{% timestamp videoId="UjHR0HJJbyw" time="2733" display="45:33" %}} - both Apple podcast and Spotify those are the two most popular podcast platforms by like a wide margin you know between  
{{% timestamp videoId="UjHR0HJJbyw" time="2740" display="45:40" %}} - the two of them that's like 90% market share or something um and so I need to have all of my content up in podcast  
{{% timestamp videoId="UjHR0HJJbyw" time="2748" display="45:48" %}} - form on both of those platforms and I want the timestamps to work on both of those platforms um and the reason for  
{{% timestamp videoId="UjHR0HJJbyw" time="2754" display="45:54" %}} - that is because a lot of the content that we have here uh like this video for example is already over an hour long you  
{{% timestamp videoId="UjHR0HJJbyw" time="2761" display="46:01" %}} - really want timestamps and uh you know like the topics listed out and when the  
{{% timestamp videoId="UjHR0HJJbyw" time="2766" display="46:06" %}} - topics start if you have content uh in as much length and depth as we have in  
{{% timestamp videoId="UjHR0HJJbyw" time="2771" display="46:11" %}} - our Bible study videos here and so I need to figure out how to add metadata to MP3 files so to rip the audio off of  
{{% timestamp videoId="UjHR0HJJbyw" time="2779" display="46:19" %}} - the video files and then make sure that they have timestamps embedded in the metadata and that you know the uh Apple  
{{% timestamp videoId="UjHR0HJJbyw" time="2786" display="46:26" %}} - podcast and Spotify actually set up timestamps a little bit differently Apple podcast uses metadata on the MP3  
{{% timestamp videoId="UjHR0HJJbyw" time="2792" display="46:32" %}} - file itself and Spotify uses timestamps in the episode description but um I kind  
{{% timestamp videoId="UjHR0HJJbyw" time="2798" display="46:38" %}} - of know what I have to do here but getting all that set up to and you know I have to pay money of course it's not free um to uh host the podcast files and  
{{% timestamp videoId="UjHR0HJJbyw" time="2806" display="46:46" %}} - get the RSS feed set up for the podcasts and uh that way people can just subscribe to them on Apple podcasts or  
{{% timestamp videoId="UjHR0HJJbyw" time="2813" display="46:53" %}} - Spotify podcasts and every time we post a new lesson uh you'll have the audio  
{{% timestamp videoId="UjHR0HJJbyw" time="2819" display="46:59" %}} - version of it that you can listen to uh you know if you're commuting or doing dishes and you know things like that so I want to get the podcast form of things  
{{% timestamp videoId="UjHR0HJJbyw" time="2825" display="47:05" %}} - set up as well and that's still I haven't quite done everything I need to do there I kind of have an idea of what  
{{% timestamp videoId="UjHR0HJJbyw" time="2830" display="47:10" %}} - I have to do but even more of the kind of you know coding side of things here  
{{% timestamp videoId="UjHR0HJJbyw" time="2837" display="47:17" %}} - left to do before I I'll kind of have all the content stuff done so I guess  
{{% timestamp videoId="UjHR0HJJbyw" time="2842" display="47:22" %}} - probably kind of technical still but I will be making that effort to keep releasing content as we go now I've  
{{% timestamp videoId="UjHR0HJJbyw" time="2848" display="47:28" %}} - mentioned that I'm going to try to keep up with it so that every week at least we're going to have something new that gets posted to the channel even as I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="2855" display="47:35" %}} - working on some of these remaining content to-dos I have enough automated now that I'm going to be pressing  
{{% timestamp videoId="UjHR0HJJbyw" time="2861" display="47:41" %}} - forward with new content kind of without backlogging it as I have been in the  
{{% timestamp videoId="UjHR0HJJbyw" time="2866" display="47:46" %}} - past few months here finally um after all of that stuff that I mentioned I'm going to turn my focus back to trying to  
{{% timestamp videoId="UjHR0HJJbyw" time="2873" display="47:53" %}} - launch the in-person Bible study in my house so I have a projector setup and I've kind of been ready to do this for a  
{{% timestamp videoId="UjHR0HJJbyw" time="2879" display="47:59" %}} - couple years but I I kept wanting to get the content in a better place so that I'm can kind of do it sustainably so you  
{{% timestamp videoId="UjHR0HJJbyw" time="2885" display="48:05" %}} - know like that parable of counting the cost so not building a tower and running out of materials halfway here I kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="2892" display="48:12" %}} - want to have everything set up in a sustainable fashion before I you know invite folks over and we try to make  
{{% timestamp videoId="UjHR0HJJbyw" time="2898" display="48:18" %}} - this this uh you know this video series and podcast of of the Bible study that I  
{{% timestamp videoId="UjHR0HJJbyw" time="2903" display="48:23" %}} - host in person I want to have everything set up and ready for that to happen so that people who miss a week will kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="2909" display="48:29" %}} - seamlessly be able to view last week's stuff online uh you know in whatever format they want and have it all there  
{{% timestamp videoId="UjHR0HJJbyw" time="2915" display="48:35" %}} - but to do that I have to make it time efficient and to make it time efficient I have to automate it and so uh a lot of  
{{% timestamp videoId="UjHR0HJJbyw" time="2921" display="48:41" %}} - the in-person Bible study stuff is kind of hard dependent on me finishing the rest of the video processing stuff and  
{{% timestamp videoId="UjHR0HJJbyw" time="2928" display="48:48" %}} - the the podcast side of things as well so that I have everything in place so that when I start doing the in-person  
{{% timestamp videoId="UjHR0HJJbyw" time="2934" display="48:54" %}} - Bible studies and and recording those I'll have everything ready to kind of take that content and and automatically  
{{% timestamp videoId="UjHR0HJJbyw" time="2941" display="49:01" %}} - get it where it needs to be uh because at that point I'll be uh doing the Bible  
{{% timestamp videoId="UjHR0HJJbyw" time="2947" display="49:07" %}} - studies from our ichus group that we've been doing for the last few years so that's at least one video a week you  
{{% timestamp videoId="UjHR0HJJbyw" time="2953" display="49:13" %}} - know a couple hours of video content plus these studies plus if I ever do anything in the middle of the week you  
{{% timestamp videoId="UjHR0HJJbyw" time="2959" display="49:19" %}} - know we're talking maybe two or three videos a week of you know substantial length I have to automate it because  
{{% timestamp videoId="UjHR0HJJbyw" time="2967" display="49:27" %}} - otherwise I just would not be able to keep up and so until I get some of that stuff done this is still kind of on hold  
{{% timestamp videoId="UjHR0HJJbyw" time="2973" display="49:33" %}} - I have a lot of to-dos here you know relating to getting the house ready for it and figuring out how I'm going to  
{{% timestamp videoId="UjHR0HJJbyw" time="2979" display="49:39" %}} - have you know a a multi-channel microphone thing for people to be able to ask questions on the recordings and  
{{% timestamp videoId="UjHR0HJJbyw" time="2985" display="49:45" %}} - things like that um I have some to-dos here but I'm not going to focus as much time and energy on this until I finish  
{{% timestamp videoId="UjHR0HJJbyw" time="2991" display="49:51" %}} - all the rest of the content stuff uh some of the to-dos that I just mentioned before uh because all of that kind of  
{{% timestamp videoId="UjHR0HJJbyw" time="2997" display="49:57" %}} - needs to preedee this before I feel like I'll be where I want to be in terms of sustainability on uh kind of the time  
{{% timestamp videoId="UjHR0HJJbyw" time="3005" display="50:05" %}} - efficiency front all right well that just about  
{{% timestamp videoId="UjHR0HJJbyw" time="3011" display="50:11" %}} - does it here I'm just going over what we talked about in this ministry update um so I talked about how a lot of the  
{{% timestamp videoId="UjHR0HJJbyw" time="3017" display="50:17" %}} - things that I was planning to do kind of got pushed aside in a li of me working  
{{% timestamp videoId="UjHR0HJJbyw" time="3023" display="50:23" %}} - on some of the video Automation in the processing uh so that I could get all of the Bible basics part one videos up in  
{{% timestamp videoId="UjHR0HJJbyw" time="3030" display="50:30" %}} - the near future here and I wanted to do that uh because I wanted to finish most of the automation before I did uh the  
{{% timestamp videoId="UjHR0HJJbyw" time="3037" display="50:37" %}} - bulk of the video processing just to save time and so that's what I ended up doing in practice and so that's why it's  
{{% timestamp videoId="UjHR0HJJbyw" time="3043" display="50:43" %}} - been several months here um I kind of then went over uh kind of what the video  
{{% timestamp videoId="UjHR0HJJbyw" time="3049" display="50:49" %}} - processing workflows involved we looked at all of the files in this sort of directory structure that I have set up  
{{% timestamp videoId="UjHR0HJJbyw" time="3055" display="50:55" %}} - and then looked at what the videos look like on YouTube with the topic transition slides uh the black slides in  
{{% timestamp videoId="UjHR0HJJbyw" time="3061" display="51:01" %}} - between sections and then uh the accurate time stamps for everything that get automatically generated uh and then  
{{% timestamp videoId="UjHR0HJJbyw" time="3067" display="51:07" %}} - we also looked at the page internal timestamps on my website and how they  
{{% timestamp videoId="UjHR0HJJbyw" time="3073" display="51:13" %}} - actually let you a full text search transcript so that if you want to go uh click on a timestamp and then have the  
{{% timestamp videoId="UjHR0HJJbyw" time="3079" display="51:19" %}} - video play exactly where uh you want to hear the thing well now that actually works perfectly as well and so uh you  
{{% timestamp videoId="UjHR0HJJbyw" time="3087" display="51:27" %}} - know jumping back to the video and all that to set up that entire framework on my website and then uh after that I  
{{% timestamp videoId="UjHR0HJJbyw" time="3094" display="51:34" %}} - mentioned how I'm going to try to be more consistent here now that I have a lot more of this Automation in place it  
{{% timestamp videoId="UjHR0HJJbyw" time="3099" display="51:39" %}} - should be more sustainable for me to kind of do a video a week or every other week and stuff like that so hopefully we  
{{% timestamp videoId="UjHR0HJJbyw" time="3105" display="51:45" %}} - won't have gaps in video releases kind of as much as we have the last couple uh honestly the last couple years um I'm  
{{% timestamp videoId="UjHR0HJJbyw" time="3112" display="51:52" %}} - hoping now that I have everything in place to be much more consistent than we have been here here and then finally I  
{{% timestamp videoId="UjHR0HJJbyw" time="3117" display="51:57" %}} - talked about some of the upcoming stuff I'm planning on doing um so going to keep making those content releases as we  
{{% timestamp videoId="UjHR0HJJbyw" time="3123" display="52:03" %}} - keep uh plugging forward in our group study of the Systematic Theology on ichus uh as well as trying to finish off  
{{% timestamp videoId="UjHR0HJJbyw" time="3131" display="52:11" %}} - a bit more Automation in my video processing workflow uh so that I can have everything completely automated  
{{% timestamp videoId="UjHR0HJJbyw" time="3137" display="52:17" %}} - rather than just having I don't know maybe 80% of it automated like I have it right now and so those are the main  
{{% timestamp videoId="UjHR0HJJbyw" time="3143" display="52:23" %}} - things I'm going to be focusing on in the short term with that longer term goal of eventually getting that  
{{% timestamp videoId="UjHR0HJJbyw" time="3148" display="52:28" %}} - in-person Bible study set up uh kind of once I have all of the Automation in place so that uh I can sustainably do  
{{% timestamp videoId="UjHR0HJJbyw" time="3155" display="52:35" %}} - two or three videos a week like I'd like to do so that is uh what I'm planning on  
{{% timestamp videoId="UjHR0HJJbyw" time="3160" display="52:40" %}} - focusing on in the future um so I hope this video has been helpful and I don't know exactly when I'll make the next one  
{{% timestamp videoId="UjHR0HJJbyw" time="3166" display="52:46" %}} - of these um I I don't think it'll probably be uh you know in two weeks I think in maybe a month or two uh as I I  
{{% timestamp videoId="UjHR0HJJbyw" time="3173" display="52:53" %}} - finish getting through all of that uh all of that video content in the back blog that's going up here but I hope  
{{% timestamp videoId="UjHR0HJJbyw" time="3179" display="52:59" %}} - this uh kind of helped situate people with what progress has been made where my focus has been the last little bit  
{{% timestamp videoId="UjHR0HJJbyw" time="3185" display="53:05" %}} - and uh kind of what things to look forward to so thanks for watching and  
{{% timestamp videoId="UjHR0HJJbyw" time="3190" display="53:10" %}} - stay tuned for all the content videos that will be coming out in the next few weeks here  

{{% /transcript %}}

{{% section-navigation %}}
