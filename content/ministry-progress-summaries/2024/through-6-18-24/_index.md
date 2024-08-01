---
title: Through 6/18/24
weight: 20
layout: content-page
video: https://www.youtube.com/watch?v=bb9cZ7WWrF4
playlist: https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb
---

{{< subjects >}}

{{< /subjects >}}

{{% section-navigation %}}

## Video {#video}

{{% video
videoId="bb9cZ7WWrF4"

videoPlaylist="https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb"

slides="https://www.bibledocs.org/slides/ministry-progress-summaries/2024/through-6-18-24"
%}}

## Summary {#summary}

This cycle I mostly spent time finishing remaining tasks in my command line application to automate video processing. Many of these things have been long-term goals of mine for a long time now, so it is nice to see everything finally come together.

## Timestamps {#timestamps}

{{% timestamp videoId="bb9cZ7WWrF4" time="0" display="0:00" %}} - Intro and outline  
{{% timestamp videoId="bb9cZ7WWrF4" time="56" display="00:56" %}} - Review  
{{% timestamp videoId="bb9cZ7WWrF4" time="190" display="03:10" %}} - Automated silence removal  
{{% timestamp videoId="bb9cZ7WWrF4" time="456" display="07:36" %}} - Automated topic transition scaffolding  
{{% timestamp videoId="bb9cZ7WWrF4" time="762" display="12:42" %}} - Automated transcripts  
{{% timestamp videoId="bb9cZ7WWrF4" time="961" display="16:01" %}} - The upshot of all this  
{{% timestamp videoId="bb9cZ7WWrF4" time="1296" display="21:36" %}} - Consistent content posting the next little bit  
{{% timestamp videoId="bb9cZ7WWrF4" time="1446" display="24:06" %}} - Upcoming plans  
{{% timestamp videoId="bb9cZ7WWrF4" time="1500" display="25:00" %}} - Summary and outro  

{{% content %}}

## Content {#content}

<!-- --- -->

### Review {#review}

Last ministry progress summary, I said I had these three immediate short-term goals:

- Setting up completely automatic silence removal in the video editing process (to further save me time---right now it is still a bit tedious, since I have to process segment by segment using a GUI tool). This will entail switching us away from Zoom, since Zoom recordings don't seem to play nice with the scriptable command-line tool I'd like to use, for some strange reason. I'm going have us try Microsoft Teams next, I think.
- Setting up further automation with the topic transitions in videos. I would like to automatically generate the topic transition video segments in a hands-off (completely automated) way. Right now I have to manually record the short segments one by one.
- Setting up a BibleDocs podcast on the podcasting platform [PodBean](https://www.podbean.com/), to include all the content from our Ichthys group Bible studies (at least that is the content stream I'll start with for podcasting---I will probably expand to others too, later). I need to support ripping mp3 audio off of the mp4 videos, and generating proper mp3 metadata/episode descriptions so that podcast episode timestamps will work properly on Apple Podcasts and Spotify (the two most dominant podcast apps, at present).

I'll be going over what progress I've made on these (and some other things besides).

<!-- --- -->

### Automated silence removal {#automated-silence-removal}

It turns out that there is a somewhat obscure recording setting on Zoom that I hadn't come across before called "Optimize for 3rd party video editor." Turning this setting on will cause Zoom recordings to take up much more hard disk space (e.g., hundreds of MBs for long records, rather than tens of MBs), but the videos are presumably less compressed will play nice with follow-on video processing steps (at least that is the idea, I think). Thus far, my experience has borne this out. In the tests I've run since turning this setting on, I've had no issues with my command line tool for removing silence in videos, even though it went kind of crazy with Zoom recordings before.

This is good news, since it means we won't have to switch away from Zoom in our group recordings. It turns out that other options I was considering (e.g., Microsoft Teams, Google Meet) do not allow for full-screen screen recording (since at least at time of writing, they inject a "people list" into the frame that you cannot remove), so wouldn't have worked nearly as well anyway. Becasue of this, I am thankful I figured out how to make the Zoom recordings work alright with the rest of my automated video processing workflow.

At any rate, after determining that we can in fact keep using Zoom, I wired up the silence removal step in my automated video processing command line tool, so that it will now get automatically run, rather than me manually have to process each segment like I was having to do before.

<!-- --- -->

### Automated topic transition scaffolding {#automated-topic-transition-scaffolding}

I also set up the part of my automated video processing workflow that automatically generates topic transition segments. Here's how it works at a high level:

- From the Markdown content file, I automatically parse out the content headers into `segments.xlsx`, and add any other miscellaneous headers that need adding (like Intro and outline, Summary and outro, etc.)
- Then using that list, I automatically build an HTML slideshow presentation (via [remark](https://github.com/gnab/remark)), with one slide for each content header that will be video-internal (so e.g., the very first section will not have a transition slide)
- After that, I turn the slideshow presentation into a series of 1920x1080 .png images using an NPM package called [decktape](https://github.com/astefanutti/decktape)
- Then I turn each image into a three-second-long 25-frames-per-second video file using [ffmpeg](https://ffmpeg.org/), and add "dummy" audio tracks to these short topic transition segments so that they can subsequently be successfully concatenated with all the main content recording segments using the [ffmpeg concat filter](https://ffmpeg.org/ffmpeg-filters.html#concat) to automatically combine all the video and audio streams across video files.

Basically, while I was previously make all these topic transition segments manually by hand (and then using a script to standardize them to all be three seconds long), now the entire thing is automated from front to back.

<!-- --- -->

### Automated transcripts {#automated-transcripts}

I also set up a process to utilize the Python package [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) to automatically pull YouTube's autogenerated transcripts into my Markdown content files, without any manual cleanup on my part.

Previously I was using some regular expressions and a rather sophisticated spreadsheet to do much the same (which took a good bit of the manual work out of it, but still required a few minutes of effort per video), but now it is all completely automatic.

<!-- --- -->

### The upshot of all this {#the-upshot-of-all-this}

That was all perhaps a bit technical. Long-time followers of this ministry will probably remember that I've been talking about getting to "content production mode" for literal years now, with there always being "process" things getting in the way of me getting there fully. Regardless of the nitty-gritty details, the point of everything I have just gone through is that there is no more process stuff holding me back on video content anymore! I mean, there are certainly some refinements I could make (such as automatically uploading videos using API keys and such for authentication), but really, where I am now is sufficient for me to finally throw that full content production switch to "ON" once for all.

If I were only doing videos, I'd now be done. However, that brings us to the third goal we discussed at the beginning of this update: supporting a podcast form of the content. While I have now finished the video automation side of things, I now need to work on the podcast automation side of things (and hosting and syndicating the podcast, etc.). Fortunately, this should be *far* easier than the video side of things, since the processing steps ought to be largely apples-to-apples, just with some minor tweaks here and there.

I am hoping I can knock it out rapidly to get out of this limbo phase we've been it. I'm taking time off work for a couple weeks in the near future in order to visit family, and historically, my "vacation time" has always been when I get the most software development work done in any given year. So I am optimistic.

<!-- --- -->

### Consistent content posting the next little bit {#consistent-content-posting-the-next-little-bit}

Podcast automation aside, since I've now finished the video side of things, I'm all set for getting through the backlog of recorded content and getting it all posted to YouTube/the site. I've made a pretty good dent already, and will be releasing a video a day (or thereabouts) for the next couple weeks at least.

Most of this content is from our group study of BB1: Theology but there is also a separate four-video playlist in there too. I recorded this other playlist several months back when a friend asked me some questions (so it falls into the Q&A > Reader Correspondence content type).

<!-- --- -->

### Upcoming plans {#upcoming-plans}

Podcast stuff.

That's really it for the moment, since I want to finish that before tackling anything else.

{{% /content %}}

{{% transcript %}}

## Video/audio transcript {#video-audio-transcript}

{{% timestamp videoId="bb9cZ7WWrF4" time="0" display="00:00" %}} - hey guys so right now I'm going to be making the ministry progress summary video here through June 18th  
{{% timestamp videoId="bb9cZ7WWrF4" time="7" display="00:07" %}} - 2024 so it's been a couple months here um I'll be going through a good bit of the programming things that I got done  
{{% timestamp videoId="bb9cZ7WWrF4" time="14" display="00:14" %}} - here so I have continued to chip away at the automation that I want to underpin all of the content production in the  
{{% timestamp videoId="bb9cZ7WWrF4" time="22" display="00:22" %}} - long term so we'll be talking about some of the to-dos I left for myself in the last Ministry progress summary and then  
{{% timestamp videoId="bb9cZ7WWrF4" time="29" display="00:29" %}} - I'll go through kind of how I addressed a couple of those as well as you know this third one here with the transcripts  
{{% timestamp videoId="bb9cZ7WWrF4" time="34" display="00:34" %}} - which was uh not so much on the list but I I added it because it was automation as well and then kind of what the upshot  
{{% timestamp videoId="bb9cZ7WWrF4" time="42" display="00:42" %}} - of all of this is in terms of video production and uh what it means in terms of content that will be posted here in  
{{% timestamp videoId="bb9cZ7WWrF4" time="49" display="00:49" %}} - the next couple weeks and then finally as per normal we'll close with what my plans are for the next little bit  
{{% timestamp videoId="bb9cZ7WWrF4" time="60" display="01:00" %}} - all right so before we get to the specifics of what I did this time I'm just going to briefly recap some of what  
{{% timestamp videoId="bb9cZ7WWrF4" time="66" display="01:06" %}} - my short-term goals were at the end of the last Ministry progress update so one of the first things that I wanted to get  
{{% timestamp videoId="bb9cZ7WWrF4" time="73" display="01:13" %}} - done uh moving forward at the end of the last one was setting up the automatic silence removal to work in my automated  
{{% timestamp videoId="bb9cZ7WWrF4" time="83" display="01:23" %}} - command line video processing project so up until now I have been manually processing ing all of the videos that I  
{{% timestamp videoId="bb9cZ7WWrF4" time="92" display="01:32" %}} - upload using a graphical user interface it's a it's a web app that lets you trim videos to automatically remove the  
{{% timestamp videoId="bb9cZ7WWrF4" time="99" display="01:39" %}} - silent parts and it does basically the same thing that my command line tool does and the reason why I was having to  
{{% timestamp videoId="bb9cZ7WWrF4" time="104" display="01:44" %}} - do that was because my commandline tool was not playing nice with the recordings from Zoom so that was one of the things  
{{% timestamp videoId="bb9cZ7WWrF4" time="111" display="01:51" %}} - that I wanted to fix and then I also wanted to set up further automation with the topic transitions in my videos so  
{{% timestamp videoId="bb9cZ7WWrF4" time="119" display="01:59" %}} - these are kind of the black screens the last several seconds that have the title for each section uh just giving a nice  
{{% timestamp videoId="bb9cZ7WWrF4" time="126" display="02:06" %}} - transition between the parts of the videos and I wanted to automatically generate these video segments rather  
{{% timestamp videoId="bb9cZ7WWrF4" time="133" display="02:13" %}} - than having to manually record them all and then standardize the length which is what I've been doing up until now I knew  
{{% timestamp videoId="bb9cZ7WWrF4" time="140" display="02:20" %}} - it was possible for me to automatically generate these video segments so that's what I wanted to set up and then finally  
{{% timestamp videoId="bb9cZ7WWrF4" time="146" display="02:26" %}} - I wanted to set up a podcast for all of the content as well so thus far all of the video content has been going up on  
{{% timestamp videoId="bb9cZ7WWrF4" time="155" display="02:35" %}} - YouTube obviously the web pag is on the website um but to support audio uh so this would be like on Spotify and apple  
{{% timestamp videoId="bb9cZ7WWrF4" time="162" display="02:42" %}} - podcast which are as far as I know the two most dominant podcasting platforms at the moment um I need to do some work  
{{% timestamp videoId="bb9cZ7WWrF4" time="169" display="02:49" %}} - to get the content ready to go up on the podcast platforms so these were the three things that I had sort of set off  
{{% timestamp videoId="bb9cZ7WWrF4" time="178" display="02:58" %}} - to work on in this last little bit and I'm going to go over what progress I made on these as well as the other  
{{% timestamp videoId="bb9cZ7WWrF4" time="185" display="03:05" %}} - things that I did that weren't so much on this list but were the other places where I spent my  
{{% timestamp videoId="bb9cZ7WWrF4" time="193" display="03:13" %}} - time so first off going to cover the automated silence removal sort of task that I left for myself and what progress  
{{% timestamp videoId="bb9cZ7WWrF4" time="200" display="03:20" %}} - I made on that so it turns out that there is a sort of obscure recording setting on Zoom that I hadn't come  
{{% timestamp videoId="bb9cZ7WWrF4" time="207" display="03:27" %}} - across before at the time that was trying to figure out how to make my video processing workflow work with the  
{{% timestamp videoId="bb9cZ7WWrF4" time="214" display="03:34" %}} - zoom recordings there's this setting called optimize for third-party video editor and this is on the recordings  
{{% timestamp videoId="bb9cZ7WWrF4" time="221" display="03:41" %}} - part of the settings interface in zoom and if you turn this on it will cause the zoom recordings to take up a lot  
{{% timestamp videoId="bb9cZ7WWrF4" time="228" display="03:48" %}} - more dis space so for my purposes if I have a video that's maybe 30 40 minutes long that will mean it's kind of  
{{% timestamp videoId="bb9cZ7WWrF4" time="234" display="03:54" %}} - hundreds of megabytes as opposed to tens um so definitely increases file size of the rec recordings but the videos are  
{{% timestamp videoId="bb9cZ7WWrF4" time="241" display="04:01" %}} - presumably less compressed and will play nice with follow on video processing steps so I happen to do a lot of my  
{{% timestamp videoId="bb9cZ7WWrF4" time="248" display="04:08" %}} - video processing with a library called ffmpeg but this would probably hold true for people who use I don't know things  
{{% timestamp videoId="bb9cZ7WWrF4" time="255" display="04:15" %}} - like Adobe Premiere Pro or D ventry resolve or any of the other uh what I would call more like normal uh uh video  
{{% timestamp videoId="bb9cZ7WWrF4" time="264" display="04:24" %}} - editors um presumably those will you would want to do this if you edit your videos that way as well um so I think  
{{% timestamp videoId="bb9cZ7WWrF4" time="273" display="04:33" %}} - it's mostly to get kind of a standard frame rate a reduce compression you can do all of that in post rather than  
{{% timestamp videoId="bb9cZ7WWrF4" time="279" display="04:39" %}} - having Zoom introduce any artifacts so uh this turned out to be exactly what I wanted and so uh my experience has borne  
{{% timestamp videoId="bb9cZ7WWrF4" time="287" display="04:47" %}} - out that this setting actually does prevent you know The Unwanted behavior that I was getting before and so in the  
{{% timestamp videoId="bb9cZ7WWrF4" time="294" display="04:54" %}} - test that I've run since I turned this on I haven't actually had issues with my command line tool for removing silence  
{{% timestamp videoId="bb9cZ7WWrF4" time="300" display="05:00" %}} - in the videos uh even though before it was kind of going crazy with the videos that I was getting out of Zoom like it  
{{% timestamp videoId="bb9cZ7WWrF4" time="305" display="05:05" %}} - wasn't working properly or the timing was all off or it was dropping sections and things like that U well with this  
{{% timestamp videoId="bb9cZ7WWrF4" time="312" display="05:12" %}} - setting turned on and and the bigger files getting safe to dis with presumably less compression and whatever  
{{% timestamp videoId="bb9cZ7WWrF4" time="319" display="05:19" %}} - whatever else they were doing to them that made them not play nice well with this setting turned on I actually  
{{% timestamp videoId="bb9cZ7WWrF4" time="324" display="05:24" %}} - haven't had any more problems uh integrating this with my automation on the command line since I'm using a  
{{% timestamp videoId="bb9cZ7WWrF4" time="331" display="05:31" %}} - specific command line tool to do this now this is good news since it means that we won't have to switch away from  
{{% timestamp videoId="bb9cZ7WWrF4" time="337" display="05:37" %}} - zoom in our group recordings it turns out that the other options I was considering so things like Microsoft  
{{% timestamp videoId="bb9cZ7WWrF4" time="344" display="05:44" %}} - teams Google meet things like that well these actually at present don't allow for full screen screen recording since  
{{% timestamp videoId="bb9cZ7WWrF4" time="353" display="05:53" %}} - uh they inject like a people list or participants list into the frame and you can't get rid of it like you you can't  
{{% timestamp videoId="bb9cZ7WWrF4" time="359" display="05:59" %}} - turn it off in settings you can't close out of it and so it just reduces uh what shows up in the recordings because if  
{{% timestamp videoId="bb9cZ7WWrF4" time="366" display="06:06" %}} - you have a normal 16 by9 aspect ratio screen well now you have the sidebar in your screen recording and you can't get  
{{% timestamp videoId="bb9cZ7WWrF4" time="373" display="06:13" %}} - rid of it and so I find that very undesirable I don't quite understand why these other uh platforms wouldn't let  
{{% timestamp videoId="bb9cZ7WWrF4" time="379" display="06:19" %}} - you record just your screen in the recording which is kind of irritating um but that is something very much in favor  
{{% timestamp videoId="bb9cZ7WWrF4" time="386" display="06:26" %}} - of using Zoom for these group meetings because recording wise it leads to much better recording quality because you can  
{{% timestamp videoId="bb9cZ7WWrF4" time="393" display="06:33" %}} - have it only focus on the content when you share your whole screen so for that reason we'd want to keep zoom and that's  
{{% timestamp videoId="bb9cZ7WWrF4" time="399" display="06:39" %}} - why I'm I'm thankful I managed to figure out how to make the zoom recordings work all right with the rest of my automated  
{{% timestamp videoId="bb9cZ7WWrF4" time="405" display="06:45" %}} - video processing workflow uh because this way uh we get to keep the benefits of Zoom like this uh while also me being  
{{% timestamp videoId="bb9cZ7WWrF4" time="415" display="06:55" %}} - able to uh automate all of the processing that I was previously having to do manually so at any rate um the  
{{% timestamp videoId="bb9cZ7WWrF4" time="422" display="07:02" %}} - upshot of all this is that after determining that uh we can in fact keep using Zoom I wired up the silence  
{{% timestamp videoId="bb9cZ7WWrF4" time="428" display="07:08" %}} - removal step in this command line tool that I've been working on to help me process the videos and so now all of  
{{% timestamp videoId="bb9cZ7WWrF4" time="435" display="07:15" %}} - these or sorry rather this uh silence removal script will get automatically run rather than me having to manually  
{{% timestamp videoId="bb9cZ7WWrF4" time="442" display="07:22" %}} - process each segment one by one like I was having to do before and so that should save me a lot of time on every  
{{% timestamp videoId="bb9cZ7WWrF4" time="448" display="07:28" %}} - new video now I just run something and it does it for all the videos rather than me having to do things more  
{{% timestamp videoId="bb9cZ7WWrF4" time="454" display="07:34" %}} - manually like I was doing previously so next we're going to talk about the automated topic transition  
{{% timestamp videoId="bb9cZ7WWrF4" time="464" display="07:44" %}} - scaffolding this was kind of the second of the big goals that I had uh coming out of the last progress update and so  
{{% timestamp videoId="bb9cZ7WWrF4" time="472" display="07:52" %}} - alongside wiring up the silence removal I also set up the part of my automated video processing workflow that AO  
{{% timestamp videoId="bb9cZ7WWrF4" time="479" display="07:59" %}} - automatically generates topic transition segments so that's those uh 3 second black slides that show up in between the  
{{% timestamp videoId="bb9cZ7WWrF4" time="487" display="08:07" %}} - video segments uh to kind of transition from one topic to the other you know like show the title of what's now being  
{{% timestamp videoId="bb9cZ7WWrF4" time="494" display="08:14" %}} - talked about and give it a bit of an audio Gap as well uh so that there's kind of like a smooth transition rather  
{{% timestamp videoId="bb9cZ7WWrF4" time="500" display="08:20" %}} - than it being like really abrupt from one thing to the others so here's kind of how I'm doing this at a high level  
{{% timestamp videoId="bb9cZ7WWrF4" time="506" display="08:26" %}} - this is a little technical but I mean it doesn't get too down into the weeds um so from the markdown file which is what  
{{% timestamp videoId="bb9cZ7WWrF4" time="513" display="08:33" %}} - I write my content in um I automatically parse out the headers that show up in the markdown file into an Excel  
{{% timestamp videoId="bb9cZ7WWrF4" time="520" display="08:40" %}} - spreadsheet which I talked about in the previous Ministry progress update video kind of explained how that works in the  
{{% timestamp videoId="bb9cZ7WWrF4" time="526" display="08:46" %}} - recordings uh process that I'm using and then I add any other miscellaneous headers that I need to like the intro  
{{% timestamp videoId="bb9cZ7WWrF4" time="532" display="08:52" %}} - and outline one or the summary and outro one uh for just like General kind of administrative things and then using  
{{% timestamp videoId="bb9cZ7WWrF4" time="540" display="09:00" %}} - that list in this Excel file I automatically build an HTML slido presentation uh uses this this package  
{{% timestamp videoId="bb9cZ7WWrF4" time="548" display="09:08" %}} - here called remark um this is a uh basically a JavaScript utility that takes markdown formatted markdown and  
{{% timestamp videoId="bb9cZ7WWrF4" time="556" display="09:16" %}} - turns it into HTML slido presentations and so I use that Library here to make slides out of all of the headers um that  
{{% timestamp videoId="bb9cZ7WWrF4" time="567" display="09:27" %}} - will be video internal so what that means is that the very first section won't have a transition slide because  
{{% timestamp videoId="bb9cZ7WWrF4" time="573" display="09:33" %}} - I'm not going to start the video with a transition slide right but all the other ones there'll be this nice transition  
{{% timestamp videoId="bb9cZ7WWrF4" time="579" display="09:39" %}} - from section to section so once I have that slideshow presentation I turn it into a series of 1920 by 1080 so that's  
{{% timestamp videoId="bb9cZ7WWrF4" time="588" display="09:48" %}} - 1080p PNG images using a npm package called dect tape so this was a bit interesting for me to set up because  
{{% timestamp videoId="bb9cZ7WWrF4" time="596" display="09:56" %}} - this is actually a JavaScript package um and my uh processing application is written in Python so I uh you know I am  
{{% timestamp videoId="bb9cZ7WWrF4" time="605" display="10:05" %}} - calling this via you know a shell execute command in Python like I'm not directly importing it into python or  
{{% timestamp videoId="bb9cZ7WWrF4" time="611" display="10:11" %}} - whatever because you can't mix languages like that but it works fine you know I just have to figure out how to set it up  
{{% timestamp videoId="bb9cZ7WWrF4" time="615" display="10:15" %}} - in npm and and get an npm environment set up so that I can use this as well uh when I'm running things on my computer U  
{{% timestamp videoId="bb9cZ7WWrF4" time="623" display="10:23" %}} - but this basically takes the slideshow presentation and then turns it into a series of images  
{{% timestamp videoId="bb9cZ7WWrF4" time="630" display="10:30" %}} - and then I turn those images into video files using FFM Peg that's the video processing tool I've mentioned uh  
{{% timestamp videoId="bb9cZ7WWrF4" time="638" display="10:38" %}} - several times before and so I uh need to ensure that the video files are 1920 x 1080 you know that's the dimensions of  
{{% timestamp videoId="bb9cZ7WWrF4" time="646" display="10:46" %}} - the images and so that's the dimensions of the video as well and it also needs to be 25 frames per second those are  
{{% timestamp videoId="bb9cZ7WWrF4" time="653" display="10:53" %}} - really important variables for lining up video files when you're trying to concatenate them all together you have  
{{% timestamp videoId="bb9cZ7WWrF4" time="659" display="10:59" %}} - to match resolution and frame rate so I am creating these myself and so I'm matching resolution and frame rate and  
{{% timestamp videoId="bb9cZ7WWrF4" time="666" display="11:06" %}} - I'm turning them into 3 second long video files and so these are the ones that will go in between all of the  
{{% timestamp videoId="bb9cZ7WWrF4" time="671" display="11:11" %}} - content sections and then the last thing you have to do is you have to add an audio track to these um because when  
{{% timestamp videoId="bb9cZ7WWrF4" time="678" display="11:18" %}} - you're using ffmpeg to stick all the videos together um there's this thing called the concat filter here and when  
{{% timestamp videoId="bb9cZ7WWrF4" time="686" display="11:26" %}} - you use this it looks something like this which probably won't mean very much to a lot of people um but when you are  
{{% timestamp videoId="bb9cZ7WWrF4" time="692" display="11:32" %}} - using the filter complex you have to align the video and audio streams and basically it only works if you have an  
{{% timestamp videoId="bb9cZ7WWrF4" time="700" display="11:40" %}} - audio stream and so for these topic transitions there is no audio you know like it's it's I'm not saying anything  
{{% timestamp videoId="bb9cZ7WWrF4" time="706" display="11:46" %}} - it's going to be silent transitions but I have to add an audio track so that when I'm sticking everything together  
{{% timestamp videoId="bb9cZ7WWrF4" time="711" display="11:51" %}} - that command will work properly and so basically uh to summarize all that really briefly so we get the headers and  
{{% timestamp videoId="bb9cZ7WWrF4" time="719" display="11:59" %}} - then we build slides with the headers and then we turn the slides into images and then we turn the images into video  
{{% timestamp videoId="bb9cZ7WWrF4" time="724" display="12:04" %}} - files and after all of that um that is the automatic creation of the topic transition segments and so those are the  
{{% timestamp videoId="bb9cZ7WWrF4" time="732" display="12:12" %}} - things that go in between the recording segments and doing all of this in an automatic fashion means that I don't  
{{% timestamp videoId="bb9cZ7WWrF4" time="739" display="12:19" %}} - have to do anything manually so before how I was doing this was I was manually recording each of these segments and  
{{% timestamp videoId="bb9cZ7WWrF4" time="744" display="12:24" %}} - then I was using a script to uh standardize them all to the same 3 second length but I was still having to  
{{% timestamp videoId="bb9cZ7WWrF4" time="749" display="12:29" %}} - manually record each one and now I'm building these dynamically with the software tool and so I don't have to do  
{{% timestamp videoId="bb9cZ7WWrF4" time="757" display="12:37" %}} - anything I just run something and all of this happens behind the scenes automatically all right so next going to  
{{% timestamp videoId="bb9cZ7WWrF4" time="766" display="12:46" %}} - be talking about automated transcripts so this actually wasn't one of the things on my list I can't recall if I  
{{% timestamp videoId="bb9cZ7WWrF4" time="773" display="12:53" %}} - ever mentioned it in the last progress update but um this is another thing that was a little bit closer to being  
{{% timestamp videoId="bb9cZ7WWrF4" time="780" display="13:00" %}} - completely automated so I was using regular expressions and a rather sophisticated spreadsheet a Google sheet  
{{% timestamp videoId="bb9cZ7WWrF4" time="787" display="13:07" %}} - that used some regular expression extraction and stuff uh to do uh kind of what I am now doing in Python code uh  
{{% timestamp videoId="bb9cZ7WWrF4" time="795" display="13:15" %}} - which is grabbing the transcript lines and um basically uh turning them into a specific format of short code so that I  
{{% timestamp videoId="bb9cZ7WWrF4" time="804" display="13:24" %}} - can use a page internal YouTube links on my website I I think you can see the last progress update where I go over how  
{{% timestamp videoId="bb9cZ7WWrF4" time="812" display="13:32" %}} - I implemented that in JavaScript um well I basically decided that I can do that in code and that saves me the hassle of  
{{% timestamp videoId="bb9cZ7WWrF4" time="822" display="13:42" %}} - having to uh process stuff manually with regular expressions and then paste it into a spreadsheet so I was already  
{{% timestamp videoId="bb9cZ7WWrF4" time="828" display="13:48" %}} - using um some tools to reduce most of the manual labor here um but now uh I just run the command just like the other  
{{% timestamp videoId="bb9cZ7WWrF4" time="837" display="13:57" %}} - things and it automatically pulls down the transcript off of a YouTube video and sticks it all together in the format  
{{% timestamp videoId="bb9cZ7WWrF4" time="845" display="14:05" %}} - that I need and puts it in the markdown content file so that when I have my web pages people can expand the transcript  
{{% timestamp videoId="bb9cZ7WWrF4" time="852" display="14:12" %}} - section and search through it if they want to jump to specific Parts in the video so the library that I'm using here  
{{% timestamp videoId="bb9cZ7WWrF4" time="858" display="14:18" %}} - it's called YouTube transcript API this one is fortunately actually python rather than the other one which was  
{{% timestamp videoId="bb9cZ7WWrF4" time="864" display="14:24" %}} - actually an npm package which was JavaScript um well because this is python I can it natively um now it is  
{{% timestamp videoId="bb9cZ7WWrF4" time="871" display="14:31" %}} - relying on B it's not tring about the right way to say this like a shadow API um it's an undocumented API this is how  
{{% timestamp videoId="bb9cZ7WWrF4" time="879" display="14:39" %}} - YouTube works like you hit this endpoint you get these things but it isn't like a a stable API so there is the possibility  
{{% timestamp videoId="bb9cZ7WWrF4" time="888" display="14:48" %}} - in the future that this project might no longer work the same way you know might have a breaking change if YouTube ever  
{{% timestamp videoId="bb9cZ7WWrF4" time="894" display="14:54" %}} - just decides to update the thing that this is depending on in the background which so far hasn't seemed to have  
{{% timestamp videoId="bb9cZ7WWrF4" time="901" display="15:01" %}} - happened and you know this has been around for I don't know a while now um so I'm optimistic that this will  
{{% timestamp videoId="bb9cZ7WWrF4" time="907" display="15:07" %}} - continue to work but uh just kind of random gwiz information but Point here is that now I also have transcripts  
{{% timestamp videoId="bb9cZ7WWrF4" time="914" display="15:14" %}} - completely automated so once I upload a video to YouTube YouTube will automatically generate a transcript I'm  
{{% timestamp videoId="bb9cZ7WWrF4" time="921" display="15:21" %}} - assuming it uses some form of voice recognition uh AI to you know figure out what the words are that you're saying  
{{% timestamp videoId="bb9cZ7WWrF4" time="928" display="15:28" %}} - you know has been a thing for a while although I'm sure the the AI is getting better and things like that um so it  
{{% timestamp videoId="bb9cZ7WWrF4" time="934" display="15:34" %}} - automatically generates transcripts uh to match the audio of the video file and so it is time like it is uh time matched  
{{% timestamp videoId="bb9cZ7WWrF4" time="943" display="15:43" %}} - and then I can download that information and combine it um using this library and then stick it in my own webpage file so  
{{% timestamp videoId="bb9cZ7WWrF4" time="951" display="15:51" %}} - that people can search the transcripts on my site and so the change here is that previously I was doing this sort of  
{{% timestamp videoId="bb9cZ7WWrF4" time="956" display="15:56" %}} - like half automated and now it is completely automated just like the other things all right so at this point you  
{{% timestamp videoId="bb9cZ7WWrF4" time="966" display="16:06" %}} - might be asking well what's the big deal what is the upshot of all of this and so people who have been longtime followers  
{{% timestamp videoId="bb9cZ7WWrF4" time="973" display="16:13" %}} - of this ministry probably know that I have been talking about kind of getting into content production mode for literal  
{{% timestamp videoId="bb9cZ7WWrF4" time="980" display="16:20" %}} - years now you know years plural um I have been saying you know I will start making more content more consistently  
{{% timestamp videoId="bb9cZ7WWrF4" time="987" display="16:27" %}} - once I get all of this process stuff done and so that was all this video processing things uh that I've been  
{{% timestamp videoId="bb9cZ7WWrF4" time="994" display="16:34" %}} - talking about here and honestly talking about for a couple years it's finally all coming together and so that has sort  
{{% timestamp videoId="bb9cZ7WWrF4" time="1001" display="16:41" %}} - of always been in the way from me giving myself permission to kind of shift the focus completely onto content because I  
{{% timestamp videoId="bb9cZ7WWrF4" time="1008" display="16:48" %}} - didn't want to you know start making a lot of content only to have to go back later and and um you know dig myself out  
{{% timestamp videoId="bb9cZ7WWrF4" time="1015" display="16:55" %}} - of a hole of applying these these changes to it uh so that if I wanted to have time stamps or topic transitions  
{{% timestamp videoId="bb9cZ7WWrF4" time="1023" display="17:03" %}} - between things i' have to go re-edit stuff in the future I wanted to have everything in place first before I go  
{{% timestamp videoId="bb9cZ7WWrF4" time="1030" display="17:10" %}} - crazy on the content side so that I don't have any processing that I am kind of causing for myself in the future um  
{{% timestamp videoId="bb9cZ7WWrF4" time="1037" display="17:17" %}} - so regardless of the nitty-gritty details here the point of everything I've just gone through is that there  
{{% timestamp videoId="bb9cZ7WWrF4" time="1043" display="17:23" %}} - actually isn't any more process of holding me back on the video content anymore the three things that I just  
{{% timestamp videoId="bb9cZ7WWrF4" time="1048" display="17:28" %}} - went over automating the silence removal part of it and automating the generation of  
{{% timestamp videoId="bb9cZ7WWrF4" time="1053" display="17:33" %}} - topic transition video segments and automating the transcript those were the last three things that I really have I  
{{% timestamp videoId="bb9cZ7WWrF4" time="1060" display="17:40" %}} - mean there are certainly some other refinements I could make so for example right now I'm still uploading the video  
{{% timestamp videoId="bb9cZ7WWrF4" time="1066" display="17:46" %}} - file to YouTube by hand I mean that takes all of a minute you know like I go to YouTube I upload the video I copy  
{{% timestamp videoId="bb9cZ7WWrF4" time="1071" display="17:51" %}} - paste the title and the description uh because I actually do automatically generate the description um as part of  
{{% timestamp videoId="bb9cZ7WWrF4" time="1078" display="17:58" %}} - my library so I just copy paste that from a text file and I mean it takes me only a minute or so but hypothetically  
{{% timestamp videoId="bb9cZ7WWrF4" time="1083" display="18:03" %}} - you could automate that too um but basically I've gotten rid of everything in the process that is actually timec  
{{% timestamp videoId="bb9cZ7WWrF4" time="1090" display="18:10" %}} - consuming in any way and so because of that um I think I am now in a position where I can finally throw that full  
{{% timestamp videoId="bb9cZ7WWrF4" time="1097" display="18:17" %}} - content production switch to on now that's speaking from the video perspective if I were only doing videos  
{{% timestamp videoId="bb9cZ7WWrF4" time="1103" display="18:23" %}} - given what I've just finished I'd be done but that kind of brings us to the third goal uh that we were discussing  
{{% timestamp videoId="bb9cZ7WWrF4" time="1111" display="18:31" %}} - from the end of last video you know what were my short-term goals well the third one was getting the podcast launched and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1118" display="18:38" %}} - so now that I'm mostly done with the video automation side of things I kind of need to work on the podcast  
{{% timestamp videoId="bb9cZ7WWrF4" time="1124" display="18:44" %}} - automation side of things and so that uh you know doing much of the similar you know adding a timestamp metadata to the  
{{% timestamp videoId="bb9cZ7WWrF4" time="1131" display="18:51" %}} - MP3 files that I'll upload to the podcast hosting platforms things like that I me you know and just hosting and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1137" display="18:57" %}} - syndicating the podcast more generally um but fortunately I think all of this should be a lot easier than the video  
{{% timestamp videoId="bb9cZ7WWrF4" time="1144" display="19:04" %}} - side of things because most of the processing steps ought to be pretty Apples to Apples here so if I've already  
{{% timestamp videoId="bb9cZ7WWrF4" time="1149" display="19:09" %}} - done it for the videos doing it again for the audio should be pretty easy um I mean there are some differences I'm sure  
{{% timestamp videoId="bb9cZ7WWrF4" time="1156" display="19:16" %}} - but um hosting this is really the thing that I have to figure out and making sure that um the timestamps and the  
{{% timestamp videoId="bb9cZ7WWrF4" time="1161" display="19:21" %}} - descriptions for each podcast episode play nice with all of the uh podcast websites like apple podcast and Spotify  
{{% timestamp videoId="bb9cZ7WWrF4" time="1168" display="19:28" %}} - but um I still need to figure this out and again that's because if I put this off  
{{% timestamp videoId="bb9cZ7WWrF4" time="1174" display="19:34" %}} - and I just make the video content for everything well moving forward in the future I'm going to have this huge  
{{% timestamp videoId="bb9cZ7WWrF4" time="1179" display="19:39" %}} - backlog of stuff I'd have to do and I want to kind of have everything in place so that before I start making lots and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1184" display="19:44" %}} - lots of content every new piece of content I do I will do all of this at the time that I make it and that way I  
{{% timestamp videoId="bb9cZ7WWrF4" time="1191" display="19:51" %}} - won't ever get behind um so I'm really hoping that I can knock this piece out rapidly so that we can get out of this  
{{% timestamp videoId="bb9cZ7WWrF4" time="1198" display="19:58" %}} - limbo phase that we've been in for a while now um I am taking time off work for a couple weeks in the near future  
{{% timestamp videoId="bb9cZ7WWrF4" time="1204" display="20:04" %}} - early July here um to visit family and historically for me my quote unquote vacation time when I'm taking time off  
{{% timestamp videoId="bb9cZ7WWrF4" time="1212" display="20:12" %}} - from my day job has actually always been when I've gotten the most software development work done in any given year  
{{% timestamp videoId="bb9cZ7WWrF4" time="1217" display="20:17" %}} - so I have you know several projects up on GitHub maybe four or five and I mean you could check this well maybe people  
{{% timestamp videoId="bb9cZ7WWrF4" time="1224" display="20:24" %}} - wouldn't know I know when I look at the dates that most of the times when I have a lot of commits you know if i' if I've  
{{% timestamp videoId="bb9cZ7WWrF4" time="1230" display="20:30" %}} - done a lot of work on something it always lines up when when I was on vacation basically so I mean so much for  
{{% timestamp videoId="bb9cZ7WWrF4" time="1237" display="20:37" %}} - rest and relaxation on vacation right but because I will have free time when I'm not focused on my day job um I am  
{{% timestamp videoId="bb9cZ7WWrF4" time="1245" display="20:45" %}} - optimistic that I'll be able to knock a lot of this out in the near future here so I mean I'm hoping if I buckle down  
{{% timestamp videoId="bb9cZ7WWrF4" time="1251" display="20:51" %}} - for maybe a week or something um I can get everything automated on the podcast side and figure out how  
{{% timestamp videoId="bb9cZ7WWrF4" time="1259" display="20:59" %}} - to basically do that last step in the process so that after uploading the video file I can upload the audio file  
{{% timestamp videoId="bb9cZ7WWrF4" time="1265" display="21:05" %}} - to the podcast host and everything else should just work and if I can get to that point then I'll have to work  
{{% timestamp videoId="bb9cZ7WWrF4" time="1272" display="21:12" %}} - through the backlog of the Bible basics content um that we have already recorded so there's 20 some odd videos there most  
{{% timestamp videoId="bb9cZ7WWrF4" time="1280" display="21:20" %}} - of those are up on YouTube and the ones that aren't um we'll get to in a second here um like next section in this update  
{{% timestamp videoId="bb9cZ7WWrF4" time="1288" display="21:28" %}} - um but but basically once I do that I will really be able to consistently move forward for each additional new piece of  
{{% timestamp videoId="bb9cZ7WWrF4" time="1295" display="21:35" %}} - content I make and that kind of brings us to the last main part of this update which is  
{{% timestamp videoId="bb9cZ7WWrF4" time="1303" display="21:43" %}} - talking about the content that I will be consistently posting in the next little bit here so uh that podcast automation  
{{% timestamp videoId="bb9cZ7WWrF4" time="1311" display="21:51" %}} - aside that we just talked about since I've now finished the video side of things I'm basically good to go for  
{{% timestamp videoId="bb9cZ7WWrF4" time="1316" display="21:56" %}} - getting through the backlog of recorded video content that we have and getting everything posted to YouTube and the  
{{% timestamp videoId="bb9cZ7WWrF4" time="1323" display="22:03" %}} - website so that would include things like the subject index links and tagging the the headers with passages and things  
{{% timestamp videoId="bb9cZ7WWrF4" time="1329" display="22:09" %}} - like that um I've made a pretty good dent on this already um so uh I will be releasing a video a day here or  
{{% timestamp videoId="bb9cZ7WWrF4" time="1337" display="22:17" %}} - thereabouts for the next couple weeks at least so I probably already got about 10 that are ready to go I'm just going to  
{{% timestamp videoId="bb9cZ7WWrF4" time="1342" display="22:22" %}} - space them out day by day and then I have maybe another 10 that I need to actually go finish um but now that I've  
{{% timestamp videoId="bb9cZ7WWrF4" time="1348" display="22:28" %}} - finished the automation or you know for example automatically generating the transition slides and pulling everything  
{{% timestamp videoId="bb9cZ7WWrF4" time="1354" display="22:34" %}} - together then I can actually go finish this backlog of videos because I'd sort of been holding off on finishing  
{{% timestamp videoId="bb9cZ7WWrF4" time="1361" display="22:41" %}} - everything until I had the automation so that I wouldn't waste time um kind of from a Time efficiency perspective and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1367" display="22:47" %}} - so most of this content is from the group study that we had on Bible basics part one theology um there's also a  
{{% timestamp videoId="bb9cZ7WWrF4" time="1374" display="22:54" %}} - separate four-part video playlist in there uh from when a friend ask me some questions and uh this particular  
{{% timestamp videoId="bb9cZ7WWrF4" time="1381" display="23:01" %}} - playlist will fall into the content type on the site corresponding to questions and answers reader correspondence so um  
{{% timestamp videoId="bb9cZ7WWrF4" time="1388" display="23:08" %}} - it ended up being kind of long actually you know a couple of those videos in that series are more than an hour um and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1393" display="23:13" %}} - I think it's it's interesting stuff it's about resuscitation and the afterlife and sleep as a euphemism for death and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1399" display="23:19" %}} - things like that um but that content will also go up here in the next couple weeks as I post through the backlog of  
{{% timestamp videoId="bb9cZ7WWrF4" time="1406" display="23:26" %}} - content that I already have recorded and so this is something that I've been promising for a while as well I said  
{{% timestamp videoId="bb9cZ7WWrF4" time="1411" display="23:31" %}} - once I get all that Automation in place I'll go ahead and post the backlog of stuff well thus far I haven't posted the  
{{% timestamp videoId="bb9cZ7WWrF4" time="1418" display="23:38" %}} - backlog of stuff because I haven't finished the automation but now that I've done that um I really will get  
{{% timestamp videoId="bb9cZ7WWrF4" time="1422" display="23:42" %}} - through this and so it'll probably be at least 15 videos over the next couple weeks here um all going up in the Bible  
{{% timestamp videoId="bb9cZ7WWrF4" time="1429" display="23:49" %}} - basic series and this other playlist I mentioned and that will get us to the point where I'm basically caught up from  
{{% timestamp videoId="bb9cZ7WWrF4" time="1434" display="23:54" %}} - a video perspective all the stuff that we've recorded will now be live on the website on YouTube and then once I  
{{% timestamp videoId="bb9cZ7WWrF4" time="1440" display="24:00" %}} - finish the podcast stuff we will truly be caught up and then I'll be ready to get going on all the new  
{{% timestamp videoId="bb9cZ7WWrF4" time="1448" display="24:08" %}} - stuff and so that kind of brings us to this last section that I always do on these Ministry updates and that's kind  
{{% timestamp videoId="bb9cZ7WWrF4" time="1454" display="24:14" %}} - of what am I planning on doing in the future here and short term I'm really going to try to put my head down and get  
{{% timestamp videoId="bb9cZ7WWrF4" time="1460" display="24:20" %}} - the podcast launched because I want to finish that before I tackle anything else and like I said I'm hopeful that  
{{% timestamp videoId="bb9cZ7WWrF4" time="1467" display="24:27" %}} - that will happen when I'm on vacation over the next several weeks but if not I I do still want this to be my top  
{{% timestamp videoId="bb9cZ7WWrF4" time="1474" display="24:34" %}} - priority because once I do this uh we can launch uh the new group study from the zoom Bible study for readers of IUS  
{{% timestamp videoId="bb9cZ7WWrF4" time="1483" display="24:43" %}} - if I launch inperson stuff at my house I'll be able to keep up uh with each new week and in-person studies like I'll  
{{% timestamp videoId="bb9cZ7WWrF4" time="1489" display="24:49" %}} - really be able to throw that content production switch like we've been talking about um and this is kind of the  
{{% timestamp videoId="bb9cZ7WWrF4" time="1494" display="24:54" %}} - last gatekeeper of that so this is really what I'm going to be focusing on finishing in the next little bit  
{{% timestamp videoId="bb9cZ7WWrF4" time="1502" display="25:02" %}} - here and so that's it for this one um I know not so much on the content side here although like I mentioned I will be  
{{% timestamp videoId="bb9cZ7WWrF4" time="1510" display="25:10" %}} - consistently posting the backlog of stuff that we've already done and uh for a lot of people maybe this wasn't that  
{{% timestamp videoId="bb9cZ7WWrF4" time="1516" display="25:16" %}} - interesting but for the long-term long uh sustainability of the content of this ministry I think a lot of the things  
{{% timestamp videoId="bb9cZ7WWrF4" time="1524" display="25:24" %}} - that kind of got done here will really help make this week by week much more sustainable um so getting that automated  
{{% timestamp videoId="bb9cZ7WWrF4" time="1532" display="25:32" %}} - silence removal the transition segment scaffolding the transcripts completely automated uh getting the podcast set up  
{{% timestamp videoId="bb9cZ7WWrF4" time="1539" display="25:39" %}} - as that last thing I have to do once I get all of this in place then every new week I will be able to create two or  
{{% timestamp videoId="bb9cZ7WWrF4" time="1546" display="25:46" %}} - three new videos uh two or three new podcast episodes you know which is the same as the videos but just the audio  
{{% timestamp videoId="bb9cZ7WWrF4" time="1553" display="25:53" %}} - I'm like I'll be able to do that and keep up a pace of maybe three or four videos a week which would be complet  
{{% timestamp videoId="bb9cZ7WWrF4" time="1558" display="25:58" %}} - compl impossible if I had to manually do anything with those videos I you know I do work a full-time job and I'm sure I'm  
{{% timestamp videoId="bb9cZ7WWrF4" time="1564" display="26:04" %}} - only going to get busier as I have other obligations so to make that possible I really have to automate a lot of things  
{{% timestamp videoId="bb9cZ7WWrF4" time="1570" display="26:10" %}} - and so getting all of this in place is that's what I'm shooting for here um is getting that two or three or four videos  
{{% timestamp videoId="bb9cZ7WWrF4" time="1577" display="26:17" %}} - a week um getting everything I need set up so that I can do that sustainably in the Long Haul and so I'm excited because  
{{% timestamp videoId="bb9cZ7WWrF4" time="1585" display="26:25" %}} - we're close and this is uh you know it's very much ress I've been working on this stuff for quite a long time now and  
{{% timestamp videoId="bb9cZ7WWrF4" time="1591" display="26:31" %}} - having it all come together is really encouraging so stay tuned um I hope in the next update here I will I will be  
{{% timestamp videoId="bb9cZ7WWrF4" time="1598" display="26:38" %}} - bearing news that I got the podcast set up and then you'll hear about my next plans after that but that will hopefully  
{{% timestamp videoId="bb9cZ7WWrF4" time="1605" display="26:45" %}} - be uh what gets covered in the next one  

{{% /transcript %}}

{{% section-navigation %}}
