import os, shutil
from .config import content_types

slides_dir = 'content/slides'

# Clean out everything presently in the /slides directory
def clean_slides_directory():
  for files in os.listdir(slides_dir):
      path = os.path.join(slides_dir, files)
      try:
          shutil.rmtree(path)
      except OSError:
          os.remove(path)

# Build subdirectories for each of the content types in the /slides directory
def scaffold_slides_subdirectories_for_content_types():
  for content_type in content_types:
    path = os.path.join(slides_dir, content_type)
    os.mkdir(path)