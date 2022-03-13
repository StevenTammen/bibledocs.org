import re

markdown_header_re_pattern = re.compile('([#]+ .*)')
title_slide_break_re_pattern = re.compile('---\n')

def remove_duplicates_from_list_while_preserving_order(input_list):
  seen = set()
  seen_add = seen.add
  return [x for x in input_list if not (x in seen or seen_add(x))]

def add_outline_to_beginning_and_end_of_slides(lines):
  
  headers = markdown_header_re_pattern.findall(lines)

  # Remove duplicates = repeated slide headers
  headers = remove_duplicates_from_list_while_preserving_order(headers)

  outline_as_string = ''
  # Slide links start at 3, since we will not link to the title slide nor the outline itself
  slide_number = 3

  # The first header is the title slide, so we skip it
  for header in headers[1:]:
    
    # Get rid of number signs that indicate headers in Markdown
    header = header.replace('#', '').strip()

    outline_item = '- [' + header + '](#' + str(slide_number) + ')\n'

    # Add indentation if the header is h5 or h6.
    # Four spaces for h6
    if('######' in header):
      outline_item = '    ' + outline_item
    # And two spaces for h5
    elif('#####' in header):
      outline_item = '  ' + outline_item

    outline_as_string += outline_item
    slide_number += 1
  
  # Add a header to outline, and also a trailing new line
  outline_as_string = '---\n\n#### Outline\n\n' + outline_as_string + '\n'

  #settings_slide = '---\nReftagger control panel\n\n'

  # Actually add the newly-constructed outline to the markdown. Add it right after the title slide, and at the very end of the presentation
  # lines = title_slide_break_re_pattern.sub(settings_slide + outline_as_string + '---\n', lines, 1)
  
  lines = title_slide_break_re_pattern.sub(outline_as_string + '---\n', lines, 1)
  
  lines += "\n\n" + outline_as_string

  return lines