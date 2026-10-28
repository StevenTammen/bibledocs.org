---
date: 2026-10-27T09:00:00
layout: content-page
stags: 
title: "2026-10-27: Finalizing the content process (hopefully)"
---

Here, we describe the final changes to the weekly content processing workflow. At least for now.

<!--more-->

{{% section-navigation %}}

## Summary {#summary}

<!-- summary -->

Here, we describe the final changes to the weekly content processing workflow. At least for now.

<!-- summary -->

{{% content %}}

## Content {#content}

### Topics covered in our Zoom meeting

I relayed all the remaining information we hadn't covered before. At least, I think this was most all the rest.

#### Cleaning up recording segments

Deleting the duplicate one

Going over why source clip sections should be labeled `#-source-clip` (not `#-content`, etc.)

I moved the location of the most recent Ichthys Bible Study recordings. I built the slides on the wrong page to start with, but now everything is in the right place.

#### New procedure: Add rows in Meetings Spreadsheet even for weeks when we don't record for a formal study

Cases:

- Date + Study title of "Admin week = planning next steps for our study"
- Date + Study title of "Casual chat week = no study/formal recording"
- Date + Study title of "No meeting this week"

See the rows in the Meeting Spreadsheets that I've already added in this format.

#### Remove now-unused Dropbox links

I've removed any links in the Meeting Spreadsheets that were following the old linking format. We should now also remove the share links from Dropbox (go to https://www.dropbox.com/share/links, and we'll go from there).

Basically, we should remove anything that ends with `-pt#` that is not a summary points recording segment.

#### Going back and re-organizing all the past recording segments on Dropbox to nest them in an additional level of folders

See how we did things for `9-content` and `10-group-discussion` this last week. Go and do the same for all the recordings you've organized for the recent Crusades study, and the "Bare minimum to be saved" study. Do this before re-linking everything in the Meeting Spreadsheets (see below).

All recording segments should now be in a subfolder, even if they are the only one in the subfolder. The subfolders follow the same general naming convention as the mp4 recording files, except the folder for source clip sections is `#-source-clip`. (Folders of this sort will contain files like `1-1-overview.mp4`, `1-3-summary-points.mp4`, etc.)

#### Going back and re-linking all the past weeks in the Meeting Spreadsheets according to the new rules

Now, we want everything to be linked the new way:

1. Always link a section's folder on Dropbox rather than directly linking recording segments one by one
2. Unless the section is a source clip section, in which case directly link recording segments one by one (plus the page section)
3. Or unless there is only a single recording segment for the section (meaning if you linked a folder, there would only be the one thing it). In that case, just directly link the single recording segment.

So what you need to do is go add links in the new format for all the old weeks that had their links cleared out (there are only a handful of these). Any old weeks that still have their links are fine, and don't need modification.

#### I am changing up how we split up the weekly processing work again

I changed my mind about doing thumbnails first, and then video/podcast metadata, and then all the other post-processing like subject tags, passage tags, and review questions (that is, splitting the work up into three separate time-sensitive timelines, in order to support quick-turnaround week-of video/podcast generation). Put simply, I think that in the future trying to have a study one Saturday and then have the entire YouTube video and podcast episode made by the next Friday or sooner (so like only six days later) is... too fast, and would be impossible to sustain in practice without always feeling super stressed.

Basically, there are too many moving parts that would have to go back and forth between me and you and other freelancers to make that kind of weekly schedule work, and I just don't think it is worth it. So instead, the basic idea will be that you do your content processing within the week (more or less *whenever* during the week, without time pressure, so long as you finish before the next week's study), and then the formal video generation process for the content (which involves the other freelancers) can kick off the next week, and take however long is necessary, without needing to be rushed in the slightest. I hope that makes sense. Upshot: since now I won't even be trying to feed the thumbnails and video/podcast metadata to a freelancer in the same week (etc.), the timing does not need to be nearly so tight for you.

We will still have one processing step with time pressure, and that is getting the recording segments organized (including group discussion sections). This is because this step is what gatekeeps setting up links in the Meeting Spreadsheets. Now that I am not going to be trying to make the videos within the six day window between studies, then even in the future (i.e., when the entire process is in place) we will still use Dropbox to link the raw recording segments so that people have the chance to review content before the new week's study, if they miss a week or whatever. (Before this new plan, I had been planning to not even have you set up Meeting Spreadsheet links to the recorded content until you would be able to link the full YouTube video version of the content).

But aside from this upfront organization, none of the rest of the content processing needs to be done in any special order or on any special timeline (so long as it is done before the afternoon of the next study meeting).

In short, the new process will be something like this:

1. You organize the recording segments, remove any unused group discussion sections, rename any other group discussion sections, and set up their parent shortcode parameters.
2. You message me, and I look over the group discussion titles (which should take me all of five minutes), and then push the content.
3. I message you back, and then you set up the Meeting Spreadsheet links
4. Then you do all the rest of the post-processing at your leisure, so long as you finish it before 3:00 PM EST on the next Saturday

#### Pre-processing for the next week will now be posted when I do the initial content push for a week (which will be immediately after you organize recording segments and rename/remove group discussion sections, as described above)

Turning Bible passage refs into scripture shortcodes is now something you will do not just for outline content, but for *all* content (i.e., also including my own own written content in summary points sections, follow-on topic sections, etc.). Make sure to skim every single bit of content I write now, to look for Bible passages on their own lines (which are the ones that should be filled in in this way).

Note that this is a departure from how things worked before, where it was only specific stuff you had to check for turning Bible passages into scripture shortcodes. Now it is everything.

This will start this upcoming week.

#### Go over updated Freelancer spreadsheet

You can ignore the VLOOKUPs tab, and just focus on the Ichthys Bible Study and Open Bible Study tabs.

Checkbox links to open the files work just like before. For now, you can just copy the same path down on all rows you add, since right now everything is being drafted on `combined-pages` (i.e., all sections are located in the same file, in practice).

The page titles are nested, showing hierarchy. This follows the Markdown header levels in the source file (aside from the top level, which is the title of the `combined-page` itself). Hopefully this is intuitive just by looking at it.

After the nested title columns, there is a column containing page layout. Each section on a `combined-page` has a page layout. They are pretty intuitive, and you should be able to get a feel for it by looking at how I've filled out the past sections so far. This page layout column is important because it determines what tasks need to be done to the content. Different types of pages require different processing steps.

After the page layout column come all the task columns. Some of these tasks are for me (the ones that are grey), and the rest are for you (the ones that are black). These task columns will be how you and I track what has or has not been done for various pages.

Since each row represents a page and each column represents a task, then each {Row, Column} cell represents a task for the specific page. There are four possible values that can be filled in for each {Row, Column} cell (that is, each task):

1. `N/A`
2. `To-do`
3. `Check`
4. `Done`

These have automatic color formatting (`N/A` = Grey, `To-do` = Yellow, `Check` = Orange, and `Done` = Green). In terms of what these things mean:

- `N/A` means that the task is *not* applicable on the current page. In practice, you can just ignore these.
- `To-do` means the task *is* applicable on the current page, and needs to be done.
- `Check` means the task may or may not be applicable on the current page, depending upon circumstances. For example, you only have to specify playlist metadata for `original-content-single-video-pages` if they have a nested group discussion page. If they don't, then there would be no playlist since it would just be the one video. What exactly controls whether something is needed or not can vary by task. That is, not every `Check` cell is gatekept by the same conditions.
  - If a `Check` turns out to be needed, turn it into a `To-do`. Otherwise, turn it into a `N/A`.
- `Done` means the task has been completed.

There is a special procedure for setting up the default task state for pages. Basically, you will copy the example row's formulas, paste them onto the new rows, then copy them again, and finally paste values only. In explicit steps:

- Select the leftmost formula cell on the example row
- Press `Ctrl + Shift + Right`
- Press `Ctrl + C`
- Select the leftmost cell on the top new row you added (you can have additional new rows under this one)
- Press `Shift + Down` repeatedly, until you have selected the leftmost cells of all new rows you added
- Press `Ctrl + V`
- Press `Ctrl + C`
- Press `Ctrl + Shift + V`

After setting up the default task state for the new rows (i.e., the new pages), we just work the tasks that we need to, according to the `To-do` and `Check` cells.

Thus far I have set up all the rows for content we have done so far, but for next week and following, this will be something you will set up yourself at the same time you organize the recording segments. Additionally, once I finalize the group discussion section titles and give you the green light to add rows to the Meeting Spreadsheets, you should come back and update the group discussion rows on the Freelancer Spreadsheet to have the final titles.

For the rows corresponding to content we've done so far, I've gone ahead and made all the relevant `To-do` and `Check` be either `Done` or `N/A`, as appropriate. Anything that has been left `To-do` is something I want you to go back and look at again. Some of these you may be able to immediately mark `Done` (particularly some of the content subject tags from earlier content, that I think you already did), but I just want you to go make sure all the statuses are right.

#### Catching up with the content backlog

Now that I have the work tracking in place, you can see that we still need to get the passage tags, subject tags, and review questions done for several of the past weeks. I'd like us to prioritize this highly, so that in the next couple weeks we can have confidence that we aren't at all behind. That will then let us thereafter focus on just keeping up week by week.

I am pretty confident that after what we've gone over today, this is the finalized content process, at least for the next few months. So now that we've got it all in place, I'd like us to battle-test it from week to week, basically ASAP. But that requires us only focusing on the new weekly content... which means we have to get all the old stuff done first.

I know I recently changed the requirements on you for Meeting Spreadsheet links and review questions (and so on), so apologies for the extra burden caused by that.

To help facilitate this catching up business, I am going to be having us skip the studies next weekend. That will give you more time to focus on getting caught up.

#### The new way of tracking how much I should pay you

Like we talked about before, I assigned dollar amounts to each type of page. This will mean that you won't have to manually keep track of hours as part of content processing, for any of the new stuff. We should look at these dollar amounts together, to make sure we both think what I picked make sense.

All the new weeks will be tracking payment this new way, but I still haven't paid you for the last part of the old stuff. If you would, check over the old tabs on the Freelancer Spreadsheet and fill in dates and hours for any work you haven't already. That way I will be able to pay you for the remaining parts of the old stuff, without what I owe you for all that getting lost in the chaos of switching to the new process.

#### Getting set up formally on Upwork

In the next little bit, I am going to be trying to get a BibleDocs project set up on the freelancing platform called [Upwork](https://www.upwork.com/). The short version is that once I start hiring more freelancers, I will want all payment to happen in the same place, so that expenditures for the project can be easily tracked.

Upshot: In the near future, I would like to also pay you through Upwork (as opposed to CashApp or Venmo or whatever, how we have done in the past). Unfortunately, that means you'll have to make an account and get set up on Upwork.

I will let you know once we get to this point, and then try to help you get set up.

I am planning to not push on this for a few weeks, so long as you are OK delaying payment that long. That will let us get comfortable with the full process for a bit, without introducing yet another new thing.

Since we've only done one external payment so far, if you are OK with it, I think I'd also like to go "re-do" that one in Upwork too, so that in the long-term, Upwork will be tracking absolutely everything. I'll work with you on that, when the time comes.

### Follow-on

#### Debugging why the checkboxes weren't opening files

The checkboxes use Google Apps Script to call protocol handler links to open the files in VSCode.

I think it might have been a permissions thing. I was using Firefox when I was showing you the updates to the Spreadsheets the other day, and the code wasn't executing properly in Firefox. But it works fine in Chrome.

Initial Googling suggests it shouldn't be a browser thing, but might be related to which Google profile is active, or sessions/cookies.

I don't know. Regardless, the checkboxes should still be opening files as per normal.

#### Updating the Freelancer Spreadsheet to only have the two steps

When I set up the Freelancer Spreadsheet the first time (including with all the VLOOKUPs), I had the post-processing split into the three sections... in the way I said we were moving away from. Whoops.

So after out meeting, I went back and updated the Freelancer Spreadsheet to now be organized in the right way.

{{% /content %}}

{{% section-navigation %}}
