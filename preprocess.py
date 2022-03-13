#  https://stackoverflow.com/questions/8953844/import-module-from-subfolder

from app.modules.general import read_in_file, build_list_of_files_to_process, get_content_sections_from_file, build_slides

from app.modules.setup import clean_slides_directory

from app.modules.footnotes import parse_footnotes

from app.modules.outlines import add_outline_to_beginning_and_end_of_slides

from app.modules.special_content_sections import replace_special_content_sections, render_markdown_and_split_across_slides

from app.modules.duplicate_headers import add_duplicate_headers_as_necessary

from app.modules.step_bible_iframes import replace_nt_step_bible_shortcodes, replace_ot_step_bible_shortcodes

from app.modules.html_comments import process_subject_tags, strip_html_comments

# Rather than separate markdown files, read directly from content on site?

# Put slide breaks in like <--! --- -->
# Then automatically split up special content sections across slides if there are slide breaks inside of them

# Compare adding eventual subject tags in HTML comments, and then having those get generated


template = read_in_file('app/templates/slides-template.html')

clean_slides_directory()
#scaffold_slides_subdirectories_for_content_types()

markdown_content_files = build_list_of_files_to_process()

for file_path in markdown_content_files:

  # Split out all the separate content sections within the file
  content_sections = get_content_sections_from_file(file_path)

  for content_section in content_sections:

    # Process subject tags, strip html comments
    content_section = process_subject_tags(content_section)
    content_section = strip_html_comments(content_section)

    # Add duplicate headers to slides, as necessary
    content_section = add_duplicate_headers_as_necessary(content_section)

    # Preprocess footnotes into littlefoot-ready HTML
    content_section = parse_footnotes(content_section)

    # Add outline
    content_section = add_outline_to_beginning_and_end_of_slides(content_section)

    # Convert shortcodes too STEP Bible iframes
    content_section = replace_nt_step_bible_shortcodes(content_section)
    content_section = replace_ot_step_bible_shortcodes(content_section)

    # Replace special content sections
    content_section = replace_special_content_sections(content_section)
    content_section = render_markdown_and_split_across_slides(content_section)

    # Write to output file
    build_slides(file_path, template, content_section)









