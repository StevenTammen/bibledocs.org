---
title: Through 12/4/22
weight: 70
layout: content-page
---

{{< subjects >}}

{{< /subjects >}}

{{% section-navigation %}}

## Video {#video}

{{% video
src="https://www.youtube.com/embed/Pyau8RYPYsE"

playlist="https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb"

video=""

audio=""

slides="https://www.bibledocs.org/slides/ministry-progress-summaries/2022/through-12-4-22/"
%}}

## Summary {#summary}

Like in past cycles, there's a fair bit of setup stuff still going on. However, I did successfully write a bash script to automate video processing, and I've now also decided to formally put some of the video organization stuff I'm having a hard time motivating myself to do on the backburner, and instead turn to drafting some new written ministry content, at least for a time. So stay tuned for that!

## Timestamps {#timestamps}

[00:00](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=0s) - Intro  
[01:58](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=118s) - Some miscellaneous practical matters  
[07:03](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=423s) - Some thinking and decisions  
[11:00](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=660s) - Some conversations  
[14:35](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=875s) - Video processing shell script  
[17:40](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=1060s) - Upcoming work  
[21:56](https://www.youtube.com/watch?v=Pyau8RYPYsE&t=1316s) - Outro  

{{% content %}}

## Content {#content}

<!-- --- -->

### Some miscellaneous practical matters {#some-miscellaneous-practical-matters}

- I set up daily automated email reminders for things like remembering to take supplements, and so on. I'm trying to stick with a set of good habits better than I have been. This had been on my todo list for a long time, so I'm glad I finally got to it.
- I ordered some additional practical items to continue chipping away at my final plan for the house. I got a second low-input lag projector to use a computer monitor when walking on the treadmill (for when I am working on the computer), a 125" screen for it, a second standing desk with caster wheels to stick two 24" monitors on when I am speaking/presenting out in the living room (acting, in essence, like a speaking podium), and then two 24" monitors to actually go on this portable speaking podium when I am presenting.
- Once these items arrived, I moved the treadmill assembly from the master bedroom to the office, and assembled and then set up the new projector/screen that came. In doing these things, I had to rearrange most of the furniture in the master and the office (including my main large bookshelf = I had to take all the books off and redistribute things), so this process took quite a while, and in fact I'm still not completely setting everything back to rights.

<!-- --- -->

### Some thinking and decisions {#some-thinking-and-decisions}

- After some thought, I've decided to only record videos when sitting statically. I had recorded a few daily progress summaries when walking on the treadmill, and I think the motion is just a bit distracting when the webcam is on. This is somewhat a change of plans. I can work on writing up my content when walking on the treadmill, but when actually recording, when there is more opportunity cost (that I hadn't quite anticipated before), I'll just sit still.
- More importantly, I've decided to start posting some new written content since I've been procrastinating so hard on finishing all the video stuff. It has bee a massive struggle to motivate myself to knock out all the busywork, and I just think I need to get on with things.
  - I'm not abandoning all my plans with the video content, but will just try to space things out a bit more so I don't burnout so hard on the boring stuff. Hopefully this means that by the time of the next ministry progress summary, there will actually be new ministry content!

<!-- --- -->

### Some conversations {#some-conversations}

- I had a long discussion with a good friend about how to handle difficult Christian relationships -- when a friend or family member doesn't take theological disagreements well, and ends up being somewhat judgmental, such that any discussion of your different perspectives and the evidence for them in scripture leaves you feeling like you are constantly being attacked, rather than having a proper two-way conversation about the truth.
- I chimed in on a WhatsApp conversation about the parable of the talents and the parable of the minas, and applications relating to the themes contained in these parables.
- Another good friend and I had several long back-and-forths about the interpretation of Matthew 4:1-4 (Satan tempting Jesus to turn stones into bread), and what His restraint here (operating under kenosis) tells us about restraint in our own lives. (It turned into some other things too, but that was the initial and central topic).

<!-- --- -->

### Video processing shell script {#video-processing-shell-script}

After some research and trial and error, I succeeded in writing a Bash script to completely automate the four-step video processing workflow I have. These are the steps:

1. Convert single-ear audio to dual-ear audio using an [ffmpeg](https://ffmpeg.org/) command.
2. Normalize audio to the EBU-128 broadcasting loudness standard using the [ffmpeg normalize](https://github.com/slhck/ffmpeg-normalize) Python package.
3. Convert the variable frame rate video coming out of the screen recording software to 30 fps constant framerate (which allows for proper editing). This one is another [ffmpeg](https://ffmpeg.org/) command.
4. Remove silence using the [Auto-Editor](https://github.com/WyattBlue/auto-editor) Python package.

What the new script does is feed the output of one command into the next step automatically, and then cleans things up by moving the intermediate files into different backup directories after each step. So I can just run the command on the command line, and then come back a few minutes later and upload the final file(s) that remain (the script supports bulk processing files all at the same time too -- as many files as are in the directory you run it in). No babysitting necessary.

When I was working on this, I set up a bunch of useful Bash aliases too (been meaning to get around to this for a while), for making `cd`-ing around easier and faster, among other things.

Together these things reduce some of the time opportunity cost that goes into making videos and wrangling them on the command line, which should help a lot in in terms of long-term throughput sustainability.

<!-- --- -->

### Upcoming work {#upcoming-work}

- Change of plans since last time. All the boring documentation and video organizing stuff is going on the backburner until I have enough distance between me and them that I no longer wince just thinking about them. Or at least not nearly as much.
- Instead, I'll start working on building out some new written content. I know from past experience that I just find this much more interesting, so I think I'll have an easier time of things doing this, at least for a time. I have plenty of places to start, given all the theological conversations I have had over the last few years (over emails, WhatsApp, the forum, Discord, and in-person conversations that I later wrote up a bit -- for example).
- I think I'll hold off on a formal series for a while, and just get going here with whatever catches my eye out of my enormous backlog of possible topics. Setting out to do a series right now would require the very sort of organization that is making me drag my feet to begin with, so that can come in the future once I've recovered my tolerance for it some.

{{% /content %}}

{{% transcript %}}

## Video/audio transcript {#video-audio-transcript}



{{% /transcript %}}

{{% section-navigation %}}