import re

nt_re_pattern = re.compile('{{% nt (.*) %}}(?:.|\n)+?{{% /nt %}}')
ot_re_pattern = re.compile('{{% ot (.*) %}}(?:.|\n)+?{{% /ot %}}')

type_re_pattern = re.compile('t="(.*?)"')
passage_re_pattern = re.compile('p="(.*?)"')
height_re_pattern = re.compile('h="(.*?)"')

passage_formatting_re_pattern = re.compile('([a-z]+)([0-9]+)')

def replace_nt_step_bible_shortcodes(content_section):
  content_section = nt_re_pattern.sub(
      build_nt_iframe,
      content_section
    )
  return content_section

def build_nt_iframe(match_obj):

  parameters = match_obj.group(1)
  iframe_type = (type_re_pattern.search(parameters)).group(1)
  passage = (passage_re_pattern.search(parameters)).group(1)
  height = (height_re_pattern.search(parameters)).group(1)

  # Get passage ready to get plugged into the URL 
  # for the API hit
  passage = passage.replace(" ", "")
  passage = passage.replace(":", ".")
  passage = passage.replace("|", "|reference=")
  passage = passage_formatting_re_pattern.sub(
    format_passage,
    passage
  )

  iframe = ''
  if(iframe_type == "esv"):
    iframe = f'<iframe src="https://www.STEPBible.org/?q=version=ESV|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "nasb"):
    iframe = f'<iframe src="https://www.STEPBible.org/?q=version=NASB_th|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "comparison"):
    iframe = f'<iframe src="https://www.STEPBible.org/?q=version=ESV|version=NASB_th|version=NIV|version=HCSB|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "greek"):
    iframe = f'<iframe src="https://www.STEPBible.org/?q=version=THGNT|reference={passage}&options=VGN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "greek-i"):
    iframe = f'<iframe src="https://www.STEPBible.org/?q=version=THGNT|version=NASB_th|reference={passage}&options=VGN" width="100%" height="80%"></iframe>'
  else:
    raise Exception(f"The iframe type '{iframe_type}' is not valid")
  
  # Let shorter iframes take up less space if specified as such. 600px and 800px 
  # iframes we will always be splitting onto different slides (80% ~ 512px ish)
  if(height == "300px" or height == "400px"):
    iframe = iframe.replace("80%", height)

  return iframe

def format_passage(match_obj):
  book_name = match_obj.group(1)
  numbers = match_obj.group(2)
  return book_name + "." + numbers

def replace_ot_step_bible_shortcodes(content_section):
  content_section = ot_re_pattern.sub(
      build_ot_iframe,
      content_section
    )
  return content_section

def build_ot_iframe(match_obj):
  parameters = match_obj.group(1)
  iframe_type = (type_re_pattern.search(parameters)).group(1)
  passage = (passage_re_pattern.search(parameters)).group(1)

  # Get passage ready to get plugged into the URL 
  # for the API hit
  passage = passage.replace(" ", "")
  passage = passage.replace(":", ".")
  passage = passage.replace("|", "|reference=")
  passage = passage_formatting_re_pattern.sub(
    format_passage,
    passage
  )

  if(iframe_type == "esv"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=ESV|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "nasb"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=NASB_th|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "comparison"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=ESV|version=NASB_th|version=NIV|version=HCSB|reference={passage}&options=VN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "hebrew"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=THOT|reference={passage}&options=VUN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "hebrew-i"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=THOT|version=NASB_th|reference={passage}&options=VUN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "lxx"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=THOT|version=LXX|reference={passage}&options=VGN" width="100%" height="80%"></iframe>'
  elif(iframe_type == "lxx-i"):
    return f'<iframe src="https://www.STEPBible.org/?q=version=THOT|version=LXX|version=NASB_th|reference={passage}&options=VGN" width="100%" height="80%"></iframe>'
  else:
    raise Exception(f"The iframe type '{iframe_type}' is not valid")