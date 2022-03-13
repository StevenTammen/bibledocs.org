from .special_content_sections import special_content_section_functions

special_content_section_names = special_content_section_functions.keys()

def shortcode_relates_to_a_special_content_section(shortcode_tag):
  for scs_name in special_content_section_names:
    if(scs_name in shortcode_tag):
      return True
  return False

def add_duplicate_headers_as_necessary(content_section):

  lines = content_section.split('\n')

  # Start out just tracking the header for content
  # Outside of any special content sections
  header_stack = [""]

  check_next_non_blank_line = False

  for index in range(len(lines)):

    line = lines[index]

    # Ignore empty lines upfront.
    # Order is important here. If we don't short-ciruit on this case first with the continue,
    # We'd get index-ouf-of-bounds errors in other checks
    if(line == ""):
      continue
    
    # Handle lines that open shortcodes.
    # Only continue (=don't add header) if the first line in the shortcode is itself a header.
    # Cf. lookahead in regular expressions.
    if(line[0:3] == "{{%"):

      # We won't ever be out-of-bounds doing lookahead assuming valid files: 
      # there will never be shortcodes we open but don't close. We do need to 
      # ignore closing shortcodes though (hence the continue in that case)

      # Closing shortcode case
      if(line[4] == "/"):
        if(shortcode_relates_to_a_special_content_section(line)):
          header_stack.pop(len(header_stack) - 1)
        continue
      
      # Opening shortcode case
      else:
        if(shortcode_relates_to_a_special_content_section(line)):
          header_stack.append("");

      # Get first non-blank line in shortcode
      next_line = ""
      lookahead_offset = 1
      while(next_line == ""):
        next_line = lines[index + lookahead_offset]
        lookahead_offset = lookahead_offset + 1
      
      # The actual lookahead check: skip adding header if first thing in shortcode is a header
      if(next_line[0] == "#"):
        continue

    # If we get to the line following new line(s) after a slide break and it is not a header, then this means we need to duplicate the last header. This does that. Or nothing if this line is in fact a header.
    if(check_next_non_blank_line):
      if(line[0] != "#"):
        lines[index] = header_stack[-1] + "\n\n" + line
      else:
        header_stack[-1] = line
      check_next_non_blank_line = False
    
    # If the line is a header, update the current header
    elif(line[0] == "#"):
      header_stack[-1] = line

    # If the line is a slide break, we set a flag to check the next non blank line. We will then check if such a line is a header or not (see the other conditional case above)
    elif(line == "---"):
      check_next_non_blank_line = True
      
  return "\n".join(lines)
