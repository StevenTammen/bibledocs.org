+++
title = "Settings"
date = 2020-09-04
+++

## Writing level

As explained at [/about-the-site/#level-appropriate](/about-the-site/#level-appropriate), this site offers most of its writing in two levels of technical complexity and prose difficulty.

While you can always go back and forth between the higher level version and lower level version for an individual page using the page level link found in the menu sidebar, most users will probably mostly be looking at content of the same level across pages. For this reason, you can set the writing level here globally, and all content lists across the site will then default to your chosen writing level.

<input id="higherLevel" onclick="javascript:setCookie('level', 'higher', 1825);" type="button" value="View only higher level writings" />
<br/><br>
<input id="lowerLevel" onclick="javascript:setCookie('level', 'lower', 1825);" type="button" value="View only lower level writings" />

Keep in mind that if you clear your browser cookies, your preferences here will be lost, and you'll have to select them again.

## Reftagger Control Panel

You can use this control panel to change settings relating to the verse tagging used on this site. Of particular note, you can change the Bible version used, as well as toggle whether or not you include links to Logos Bible Software in the tagging. If you do, clicking on the L in the box next to a link will open the tagged passage in Logos. This is very useful if you are a user of Logos (but if you are not, it reduces visual clutter to disable this option, which is why it is off by default).

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
