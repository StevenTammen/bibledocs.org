---
title: Through 2/21/23
weight: 30
layout: content-page
---

{{< subjects >}}

{{< /subjects >}}

{{% section-navigation %}}

## Video {#video}

{{% video
src="https://www.youtube.com/embed/wab28hfPOl8"

playlist="https://www.youtube.com/playlist?list=PLcqAebKsBWy_RPB-7ZFePE4eTotFZ-aJb"

video=""

audio=""

slides="https://www.bibledocs.org/slides/ministry-progress-summaries/2023/through-2-21-23/"
%}}

## Summary {#summary}

This cycle ran long on account of me being busy getting set up and established at some local church fellowships. That said, I got 16 (!) new content pages up on the site, making this the biggest content release since the beginning of this ministry. I'll see if I can keep up the pace as we move forward into the future. Prayers appreciated!

## Timestamps {#timestamps}

[00:00](https://www.youtube.com/watch?v=wab28hfPOl8&t=0s) - Intro  
[00:59](https://www.youtube.com/watch?v=wab28hfPOl8&t=59s) - Making these updates only as more content accumulates  
[02:58](https://www.youtube.com/watch?v=wab28hfPOl8&t=178s) - Squashed some bugs/made some framework improvements  
[06:15](https://www.youtube.com/watch?v=wab28hfPOl8&t=375s) - Got established at some local church fellowships  
[07:00](https://www.youtube.com/watch?v=wab28hfPOl8&t=420s) - New content  
[08:05](https://www.youtube.com/watch?v=wab28hfPOl8&t=485s) - Week 1: Does the Voice Agree with the Bible?  
[10:33](https://www.youtube.com/watch?v=wab28hfPOl8&t=633s) - Week 2: Does the Voice Bring Conviction?  
[13:51](https://www.youtube.com/watch?v=wab28hfPOl8&t=831s) - Week 3: Does the Voice Call You to Trust God?  
[16:03](https://www.youtube.com/watch?v=wab28hfPOl8&t=963s) - Week 4: Does the Voice Align with God's Character?  
[26:55](https://www.youtube.com/watch?v=wab28hfPOl8&t=1615s) - Week 5: Does the Voice Honor God?  
[29:07](https://www.youtube.com/watch?v=wab28hfPOl8&t=1747s) - Upcoming work  
[29:40](https://www.youtube.com/watch?v=wab28hfPOl8&t=1780s) - Outro  

{{% content %}}

## Content {#content}

<!-- --- -->

### Making these updates only as more content accumulates {#making-these-updates-only-as-more-content-accumulates}

For the first while here, I had been making these ministry updates every two weeks. The last couple dragged a bit, as I hadn't at that time had enough new content to really make them particularly interesting.

On that account, I decided to only make these once I have enough content accumulate for me to be able to do interesting updates. In principle, now that I'm truly entering production mode, this will probably end up back at right around every two weeks again (making this ~5 week gap an anomaly).

The reason why this latest update has been so slow in coming was because I was busy getting involved with some local fellowships, and then fleshing out the framework for me to write content relating to said fellowships. More on that later in the update.

I'm also going to try to make the progress update emails and posts on social media a bit less formulaic. Hopefully switching things up here and there will make it more engaging.

<!-- --- -->

### Squashed some bugs/made some framework improvements {#squashed-some-bugs-made-some-framework-improvements}

- Updated z-index of TOC sidebar to ensure that footnotes display over it, whenever applicable.
- Fixed a bug on [this page](https://www.bibledocs.org/questions-and-answers/self-generated/on-the-office-of-pastor-teacher-and-church-polity/additional-clarification-and-other-offices-in-the-church/). I had previously named the headers for the five subquestions and subanswers the same thing, causing the scrollspy behavior in the TOC to behave strangely.
- Fixed a bug in the preprocessor application wherein links in the subject index were getting added twice/duplicated: once for a discussion page itself (as is proper), and a second time when the discussion page got aggregated onto a content page (which is not proper).
- Fixed a bug in the preprocessor application related to studies that only have a single page, rather than a series of pages. I added conditionals and such throughout the processing to make it so that such single-page studies are properly processed too.
- Fixed an issue where Step Bible App iframes were causing the parent page to jump all over the place as they loaded, probably due to an update upstream of me with their API. I added some delay before they are shown, to let them fully load and do their worst in the way of scroll-stealing before I make them visible. This seems to have fixed it quite nicely.
- Changed the styling of scripture-related special content sections. I made them transparent (as opposed to the light brown they had been), but added a 1px solid black border. I think the new style looks quite nice.

<!-- --- -->

### Got established at some local church fellowships {#got-established-at-some-local-church-fellowships}

I've started going to a Sunday school class on Sunday mornings, as well as a Bible study on Wednesday nights.

As I get more involved, a good bit of my production will probably shift into things relating to these groups, at least for the time being.

<!-- --- -->

### New content {#new-content}

There is quite a lot this time (a full 16 new pages, to my count!), so we'll go through it bit by bit.

The study that the Sunday school class I've been attending has been going through is about how to discern the voice of God. In the Wednesday night Bible study, we are in Jeremiah at the moment.

I haven't started any writing of my own for the Jeremiah study yet, but plan to this week. I have, however written quite a lot relating to the Sunday school study.

<!-- --- -->

### Week 1: Does the Voice Agree with the Bible? {#week-1-does-the-voice-agree-with-the-bible}

- [Link to page](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-agree-with-the-bible/)
- [Link to discussion page: The Bible Is How We Know What Is from God](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-agree-with-the-bible/the-bible-is-how-we-know-what-is-from-god/)
- [Link to discussion page: Satan Is the Serpent of Genesis 3](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-agree-with-the-bible/satan-is-the-serpent-of-genesis-3/)

<!-- --- -->

### Week 2: Does the Voice Bring Conviction? {#week-2-does-the-voice-bring-conviction}

- [Link to page](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-bring-conviction/)
- [Link to discussion page: On the Human Capacity for Self-Deception](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-bring-conviction/on-the-human-capacity-for-self-deception/)
- [Link to discussion page: We Ought Not Have Unrealistic Expectations about Spiritual Conviction](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-bring-conviction/we-ought-not-have-unrealistic-expectations-about-spiritual-conviction/)
- [Link to discussion page: The Momentousness of Acts 2](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-bring-conviction/the-momentousness-of-acts-2/)
- [Link to discussion page: Conviction Is Not Based upon Emotion, but upon the Truth](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-bring-conviction/conviction-is-not-based-upon-emotion-but-upon-the-truth/)

<!-- --- -->

### Week 3: Does the Voice Call You to Trust God? {#week-3-does-the-voice-call-you-to-trust-god}

- [Link to page](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-call-you-to-trust-god/)
- [Link to discussion page: Faith Is Not Irrational](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-call-you-to-trust-god/faith-is-not-irrational/)

<!-- --- -->

### Week 4: Does the Voice Align with God's Character? {#week-4-does-the-voice-align-with-god-s-character}

- [Link to page](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-align-with-gods-character/)
- [Link to discussion page: Did Moses Do Wrong in Throwing the First Set of Tablets?](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-align-with-gods-character/did-moses-do-wrong-in-throwing-the-first-set-of-tablets/)
  - [Link to a new related Q&A: On the Emotion of Anger](https://www.bibledocs.org/questions-and-answers/reader-correspondence/on-the-emotion-of-anger/)
  - [Link to another new related Q&A: Does Ephesians 4:26 Teach That There Is a Form of Righteous Anger?](https://www.bibledocs.org/questions-and-answers/self-generated/does-ephesians-4-26-teach-that-there-is-a-form-of-righteous-anger/)
- [Link to discussion page: What Is Going on in Exodus 34:27-28?](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-align-with-gods-character/what-is-going-on-in-exodus-34-27-28/)

<!-- --- -->

### Week 5: Does the Voice Honor God? {#week-5-does-the-voice-honor-god}

- [Link to page](https://www.bibledocs.org/longer-topical-studies/central-baptist-winter-2022-2023-how-to-discern-the-voice-of-god/does-the-voice-honor-god/)

<!-- --- -->

### Upcoming work {#upcoming-work}

- In addition to continuing work on stuff related to the Sunday school study, I hope to start getting some stuff up related to the Jeremiah Bible study as well, week by week.

{{% /content %}}

{{% transcript %}}

## Video/audio transcript {#video-audio-transcript}



{{% /transcript %}}

{{% section-navigation %}}
