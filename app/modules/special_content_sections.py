'''

Fix styling at top of special content sections when opening 3 layers (etc.) deep right from beginning
'''


import re
from .general import convert_text_to_html

# Call functions dynamically, by building callback function dictionary with decorators
# https://stackoverflow.com/a/54075852
special_content_section_functions = {}
def add_function(key):
  # this is the actual decorator
  def _add_function(func):
    special_content_section_functions[key] = func
    return func
  return _add_function

slide_break_re_pattern = re.compile('---\n')


@add_function('cautionary-note')
def build_cautionary_note_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content cautionary-note">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#cautionary-notes">Cautionary note</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('technical-discussion')
def build_technical_discussion_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content technical-discussion">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#technical-discussion">Technical discussion</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('sidenote')
def build_sidenote_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content sidenote">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#sidenotes">Sidenote</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('application')
def build_application_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content application">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#application">Application</a>\n' + '</strong>\n' + '<aside style="padding: 10px 40px; border-bottom: 1px solid black;">\n' + 'Please note: application is <em>personal</em>, depending upon <em>individual circumstances</em>. Therefore, it is <em>not</em> proper to turn anything in this section below into hard-and-fast rules. What is right for one person may not be right for another.\n' + '</aside>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('indirect-reasoning')
def build_indirect_reasoning_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content indirect-reasoning">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#indirect-reasoning">Indirect reasoning</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('example')
def build_example_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content example">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#examples">Example</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('post-hoc-note')
def build_post_hoc_note_section(match_obj):
  section_content = match_obj.group(2)
  opening_tag = f'<div class="special-content post-hoc-note">\n'
  header = '<strong>\n' + '<a href="/site/content-features/#post-hoc-notes">Post-hoc note</a>\n' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

text_re_pattern = re.compile('text="(.*?)"')
src_re_pattern = re.compile('src="(.*?)"')

@add_function('quote')
def build_quote_section(match_obj):
  
  parameters = match_obj.group(1)
  section_content = match_obj.group(2)
  
  opening_tag = f'<div class="special-content quote">\n'

  if(parameters != ""):
    src = (src_re_pattern.search(parameters)).group(1)
    text = (text_re_pattern.search(parameters)).group(1)
    header = '<strong>\n' + f'<a href="/site/content-features/#quotes">Quote</a> from <a href="{src}">{text}</a>\n' + '</strong>'
  else:
    header = '<strong>\n' + '<a href="/site/content-features/#quotes">Quote</a>\n' + '</strong>'
  
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

passage_re_pattern = re.compile('p="(.*?)"')

@add_function('scripture-h')
def build_scripture_h_section(match_obj):

  parameters = match_obj.group(1)
  section_content = match_obj.group(2)
  
  passage = (passage_re_pattern.search(parameters)).group(1)

  opening_tag = f'<div class="special-content scripture">\n'
  header = '<strong>' + f'{passage}' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('scripture-l')
def build_scripture_l_section(match_obj):
  parameters = match_obj.group(1)
  section_content = match_obj.group(2)
  
  passage = (passage_re_pattern.search(parameters)).group(1)

  opening_tag = f'<div class="special-content scripture">\n'
  header = '<strong>' + f'{passage}' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('original-translation')
def build_original_translation_section(match_obj):
  parameters = match_obj.group(1)
  section_content = match_obj.group(2)
  
  passage = (passage_re_pattern.search(parameters)).group(1)

  opening_tag = f'<div class="special-content scripture">\n'
  header = '<strong>' + f'{passage} | <a href="/site/content-features/#original-translations">Original translation</a>' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

@add_function('ichthys-translation')
def build_ichthys_translation_section(match_obj):
  parameters = match_obj.group(1)
  section_content = match_obj.group(2)
  
  passage = (passage_re_pattern.search(parameters)).group(1)

  opening_tag = f'<div class="special-content scripture">\n'
  header = '<strong>' + f'{passage} | <a href="/site/content-features/#ichthys-translations">Ichthys translation</a>' + '</strong>'
  closing_tag = '</div>\n'

  special_content_section = opening_tag + header + section_content + closing_tag

  return special_content_section

# We want lazy quantifiers rather than greedy quantifiers in the regex so that we don't overlap between sections.
# https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions
special_content_section_re_patterns = {section_name:
  re.compile('{{% ' + section_name + '(.*) %}}((?:.|\n)+?){{% /' + section_name + ' %}}') for section_name in special_content_section_functions }


# Assume no nesting of sections of the same type, since regex
# will return non-overlapping matches
def replace_special_content_sections(content_section):
  for section_name, pattern in special_content_section_re_patterns.items():
    content_section = pattern.sub(
      special_content_section_functions[section_name],
      content_section
    )
  return content_section

def render_markdown_and_split_across_slides(content_section):
  
  incoming_lines = content_section.split("\n")
  outgoing_lines = []

  markdown_to_render = ""
  scs_stack = []

  for line in incoming_lines:

    line_is_just_newline = len(line) == 0

    # Reset the markdown accumulator variable every time 
    # we get a newline and render the markdown chunk
    if(line_is_just_newline):
      if(markdown_to_render != ""):
        rendered_html = convert_text_to_html(markdown_to_render)
        outgoing_lines.append(rendered_html)
        markdown_to_render = ""
      outgoing_lines.append("")
      continue

    line_is_opening_scs = '<div' in line
    line_is_closing_scs = line == "</div>"
    line_is_slide_break = line == "---"
    line_is_other_html = line[0] == "<"

    # Starting a new special content section
    if(line_is_opening_scs):
      scs_stack.append(line)
      outgoing_lines.append(line)
    
    # Closing a special content section. Also serves as a markdown render trigger, just like newlines
    elif(line_is_closing_scs):

      if(markdown_to_render != ""):
        rendered_html = convert_text_to_html(markdown_to_render)
        outgoing_lines.append(rendered_html)
        markdown_to_render = ""
        
      # LIFO = stack. Things are added to end, so the "top of the stack" is the end of the list
      # We both push to there and pop from there, as here
      scs_stack.pop(len(scs_stack) - 1)
      outgoing_lines.append(line)
    
    # Duplicating special content section nesting across slide breaks
    elif(line_is_slide_break):
      closing_scs_tags = ""
      reopening_scs_tags = ""
      # Iterate from bottom of stack to top of stack. Here, that means earlier indices of list ot later ones
      for scs_opening_tag in scs_stack :
        closing_scs_tags = closing_scs_tags + "</div>\n"
        reopening_scs_tags = reopening_scs_tags + f"{scs_opening_tag}\n"
      outgoing_lines.append(closing_scs_tags + line + "\n" + reopening_scs_tags)
    
    # We render all markdown between newlines into html if we are 
    # inside a special content section
    elif((not (line_is_other_html or line_is_just_newline)) and len(scs_stack) > 0):
      markdown_to_render = markdown_to_render + "\n" + line

    # These trigger markdown render too
    elif(line_is_other_html):

      if(markdown_to_render != ""):
        rendered_html = convert_text_to_html(markdown_to_render)
        outgoing_lines.append(rendered_html)
        markdown_to_render = ""

      outgoing_lines.append(line)
    
    else:
      outgoing_lines.append(line)

  return "\n".join(outgoing_lines)