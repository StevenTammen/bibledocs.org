import re

subject_tags_re_pattern = re.compile('<!-- Tags: ((?:.|\n)+?) -->')
html_comment_re_pattern = re.compile('[ ]?<!--((?:.|\n)+?)-->')

def process_subject_tags(content_section):
  content_section = subject_tags_re_pattern.sub(
      build_subject_links,
      content_section
    )
  return content_section

def build_subject_links(match_object):
  subject_tags = match_object.group(1)
  return f'<strong>Tags = {subject_tags}</strong>'

def strip_html_comments(content_section):
  content_section = html_comment_re_pattern.sub(
      '',
      content_section
    )
  return content_section
