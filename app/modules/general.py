import markdown
import os
import re
from .config import content_types

# Have to be more manual about this one, since Replit guesses wrong by default
# https://docs.replit.com/programming-ide/installing-packages
import slugify #upm package(python-slugify)

def build_list_of_files_to_process():
  content_path_base = 'content/'
  markdown_content_files = []
  for content_type in content_types:
    path = content_path_base + content_type
    for root, directories, files in os.walk(path):
        for file in files:
          # TODO: only run stuff on files that have been changed (according to Git changeset) = diff, unless the user changes something in config file to do a full run
            if ('.md' in file) and ('_index' not in file):
                markdown_content_files.append(os.path.join(root, file))
  return markdown_content_files

commented_out_slide_break_re_pattern = re.compile(r'<!-- --- -->')

content_section_re_pattern = re.compile(r'## (.+)\n(?:.|\n)+?{{% content %}}((?:.|\n)+?){{% /content %}}')

def get_content_sections_from_file(file_path):
  
  file_as_string = read_in_file(file_path)
  content_sections = []

  # First uncomment the slide breaks so that they will be active
  file_as_string = commented_out_slide_break_re_pattern.sub('---', file_as_string)

  # Narrow things down to only the content we want in slides = title and full text (but not transcript, etc.)
  content_section_re_pattern.sub(
    lambda match: construct_single_content_section(match, content_sections),
    file_as_string
  )

  return content_sections

# https://blog.finxter.com/python-regex-start-of-line-and-end-of-line/
h3_header_re_pattern = re.compile(r'^### (.+)', re.MULTILINE)
def construct_single_content_section(match_obj, content_sections):
  title = match_obj.group(1)
  full_text = match_obj.group(2)

  # Remove the header saying that this section is the full-text of the content. At this point, it will be the only h3 header in the full-text string
  # Also add a slide break for the title slide
  full_text = h3_header_re_pattern.sub('---', full_text)

  content_section = f'### {title}{full_text}'
  content_sections.append(content_section)
  return content_section

# https://stackoverflow.com/questions/49640513/
def read_in_file(file_path):
  with open(file_path, "r", encoding="utf8") as f:
    return f.read()

def convert_text_to_html(text):
  return markdown.markdown(text)

def build_output_file_path(file_path, content_section):
  # Get title. At this point, it will be the only h3 header
  slides_title = (h3_header_re_pattern.search(content_section)).group(1)
  output_file_path = file_path.replace('content', 'content/slides')
  output_file_path = output_file_path.replace('.md', f'/{slugify.slugify(slides_title)}.html')
  return output_file_path

def safe_open_w(path):
  '''
  Open "path" for writing, creating any parent directories as needed.

  https://stackoverflow.com/a/23794010
  '''
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w', encoding="utf8")

def build_slides(file_path, template, content_section):
  output_file_path = build_output_file_path(file_path, content_section)
  to_write = re.sub('markdown-content', content_section, template)
  with safe_open_w(output_file_path) as f:
    f.writelines(to_write)