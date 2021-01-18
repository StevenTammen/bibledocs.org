---
title: Settings
date: 2021-01-10T20:25:12-05:00
tags: []
subsection: meta
weight: 10
---


## Writing level

As explained at [/about-the-site/#level-appropriate](/about-the-site/#level-appropriate), this site offers most of its writing in two levels of technical complexity and prose difficulty.

While you can always go back and forth between the higher level version and lower level version for an individual page using the page level link found in the menu sidebar, most users will probably mostly be looking at content of the same level across pages. For this reason, you can set the writing level here globally, and all content lists across the site will then default to your chosen writing level.

<div id="writingLevelContainer">
	<div id="writingLevelDisplay"></div>
	<div><input id="higherLevel" onclick="javascript:toHigherWritingLevel();" type="button" value="View only higher level writings" /></div>
	<div><input id="lowerLevel" onclick="javascript:toLowerWritingLevel();" type="button" value="View only lower level writings" /></div>
</div>

<style>
	#writingLevelContainer {
		border: 1px solid black;
		border-radius: 5px;
	}
	
	#writingLevelContainer input {
		width: 240px;
	}
	
	#writingLevelContainer > div {
		padding: 10px;
	}

	#writingLevelDisplay {
		font-weight: bold;
	}
</style>

Keep in mind that if you clear your browser cookies, your preferences here will be lost, and you'll have to select them again.

## STEP Bible app embedded windows

As explained at [/about-the-site/#step-bible-app-embedded-windows](/about-the-site/#step-bible-app-embedded-windows), this site offers the option of viewing most verse quotations in embedded windows from a Bible software application. This allows for a lot of advanced functionality (built right into the webpages of this site), but it does add some complexity that some people may not want. For this reason, this site also offers a simpler option where verse quotations appear as plain text.

While you can always go back and forth between these two display options using the page level link found in the menu sidebar, most users will probably mostly be interested in having the same display preference active across pages. For this reason, you can set the display option here globally, and all pages across the site will then default to your chosen scripture display setting.

<div id="scriptureDisplayContainer">
	<div id="scriptureDisplayDisplay"></div>
	<div><input id="embedded" onclick="javascript:toEmbeddedDisplay();" type="button" value="View scripture in embedded windows" /></div>
	<div><input id="plaintext" onclick="javascript:toPlaintextDisplay();" type="button" value="View scripture in plain text" /></div>
</div>

<style>
	#scriptureDisplayContainer {
		border: 1px solid black;
		border-radius: 5px;
	}
	
	#scriptureDisplayContainer input {
		width: 280px;
	}
	
	#scriptureDisplayContainer > div {
		padding: 10px;
	}

	#scriptureDisplayDisplay {
		font-weight: bold;
	}
</style>

Keep in mind that if you clear your browser cookies, your preferences here will be lost, and you'll have to select them again.

## Reftagger settings

You can use the below control panel to change settings relating to the verse tagging used on this site. Of particular note, you can change the Bible version used, as well as toggle whether or not you include links to Logos Bible Software in the tagging. If you do, clicking on the L in the box next to a link will open the tagged passage in Logos. This is very useful if you are a user of Logos (but if you are not, it reduces visual clutter to disable this option, which is why it is off by default).

Keep in mind that if you clear your browser cookies, your preferences here will be lost, and you'll have to select them again.

<!-- Reftagger Control Panel -->
<div id="lbsRefTaggerCP" style="border: 1px solid black; border-radius: 5px;">
	<div id="lbsHeader" style="padding: 10px;">
		<a href="https://faithlife.com/products/reftagger">Bible Options</a>
	</div>
	<div id="lbsVersionContainer" style="padding: 10px;">
		<select id="lbsVersion">
			<option value="AB">AMP</option>
			<option value="ASV">ASV</option>
			<option value="DAR">DARBY</option>
			<option value="ESV">ESV</option>
			<option value="GW">GW</option>
			<option value="HCSB">HCSB</option>
			<option value="KJV">KJV</option>
			<option value="LEB">LEB</option>
			<option value="MESSAGE">MESSAGE</option>
			<option value="NASB">NASB</option>
			<option value="NCV">NCV</option>
			<option value="NIV">NIV</option>
			<option value="NIRV">NIRV</option>
			<option value="NKJV">NKJV</option>
			<option value="NLT">NLT</option>
			<option value="TNIV">TNIV</option>
			<option value="YLT">YLT</option>
		</select>
	</div>
	<div id="lbsLibronixContainer" style="padding: 10px;">
		<input id="lbsUseLibronixLinks" type="checkbox"/>
		<label for="lbsUseLibronixLinks">Show Logos Links</label>
	</div>
	<div id="lbsSaveContainer" style="padding: 10px;">
		<input id="lbsSave" onclick="javascript:refTagger.lbsSavePrefs()" type="button" value="Save" />
	</div>
</div>
<!-- End RefTagger Control Panel. For more info visit https://faithlife.com/products/reftagger. -->



<script type="text/javascript">
	function setCookie(cname,cvalue,exdays) {
	  var d = new Date();
	  d.setTime(d.getTime() + (exdays*24*60*60*1000));
	  var expires = "expires=" + d.toGMTString();
	  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
	}

	function getCookie(cname) {
	  var name = cname + "=";
	  var decodedCookie = decodeURIComponent(document.cookie);
	  var ca = decodedCookie.split(';');
	  for(var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
		  c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
		  return c.substring(name.length, c.length);
		}
	  }
	  return "";
	}

	function toHigherWritingLevel() {
		setCookie('writingLevel', 'higher', 1825);
		displayWritingLevel();
	}

	function toLowerWritingLevel() {
		setCookie('writingLevel', 'lower', 1825);
		displayWritingLevel();
	}

	function displayWritingLevel() {
		var writingLevel=getCookie("writingLevel");
		var displayDiv = document.getElementById("writingLevelDisplay");
		if(writingLevel == "higher")
		{
			displayDiv.innerHTML = "Current writing level: higher";
		}
		else if(writingLevel == "lower")
		{
			displayDiv.innerHTML = "Current writing level: lower";
		}
		// if user hasn't set cookie, set cookie and display higher level version
		else { // level = ""
			setCookie('writingLevel', 'higher', 1825);
			displayDiv.innerHTML = "Current writing level: higher";
		}
	}
	
	function toEmbeddedDisplay() {
		setCookie('scriptureDisplay', 'embedded', 1825);
		displayScriptureDisplay();
	}

	function toPlaintextDisplay() {
		setCookie('scriptureDisplay', 'plaintext', 1825);
		displayScriptureDisplay();
	}

	function displayScriptureDisplay() {
		var scriptureDisplay=getCookie("scriptureDisplay");
		var displayDiv = document.getElementById("scriptureDisplayDisplay");
		if(scriptureDisplay == "embedded")
		{
			displayDiv.innerHTML = "Current scripture display setting: embedded windows";
		}
		else if(scriptureDisplay == "plaintext")
		{
			displayDiv.innerHTML = "Current scripture display setting: plain text";
		}
		// if user hasn't set cookie, set cookie and display embedded windows
		else { // scriptureDisplay = ""
			setCookie('scriptureDisplay', 'embedded', 1825);
			displayDiv.innerHTML = "Current scripture display setting: embedded windows";
		}
	}
	
	displayWritingLevel();
	displayScriptureDisplay()
</script>