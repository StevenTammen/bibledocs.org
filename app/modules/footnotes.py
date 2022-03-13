import re
from .general import convert_text_to_html

footnote_marker_pattern = re.compile(r' \[\^(.*)\]')
footnote_definition_pattern = re.compile(r'\n\n\[\^.*\]: (.*)')

def parse_footnotes(lines):

  footnote_markers = footnote_marker_pattern.findall(lines)
  footnote_definitions = footnote_definition_pattern.findall(lines)

  footnote_list_entries = []

  for index in range(len(footnote_markers)):
    footnote_list_entry = f'''
    <li class="footnote" id="fn-{footnote_markers[index]}">
      {convert_text_to_html(footnote_definitions[index])}
    </li>
    '''
    footnote_list_entries.append(footnote_list_entry)

  ordered_list_of_footnotes = '\n'.join(footnote_list_entries)
  footnote_list =f'''
<!-- Footnote List -->
<div class="footnotes">
  <ol>
    {ordered_list_of_footnotes}
  </ol>
</div>
  '''

  # Replace footnote references in the text with appropriate HTML
  lines = footnote_marker_pattern.sub(build_footnote_marker, lines)

  # Remove footnote definitions completely from the text
  lines = footnote_definition_pattern.sub('', lines)

  # Add footnote list onto the end
  lines = lines + '\n\n' + footnote_list

  return lines

def build_footnote_marker(match_obj):
  footnote_name = match_obj.group(1)
  return f' <sup id="fnref-{footnote_name}"><a href="#fn-{footnote_name}">1</a></sup>'