#!/bin/bash

# Get the directory of the script
dirname="$(dirname "$(readlink -f "$0")")"

# Make sure script is being called correctly. If so, cd into dir to get file 
# names to delete.
if [ "$1" == "org" ]; then
  cd $dirname/org 
  echo -e "Deleting org files from spartan/...\n"
elif [ "$1" = "markdown" ]; then
  cd $dirname/markdown 
  echo -e "Deleting markdown files from spartan/...\n"
else
  echo -e "Improper use. Call as either:\n\t./uninstall.sh org\n\t./uninstall.sh markdown"
  exit 1
fi

# Assuming in directory spartan/example-site/org,
# OR the directory      spartan/example-site/markdown
# spartan/ is ../../
spartan="../../"
spartandir=`eval "cd $spartan;pwd;cd - > /dev/null"`

# Want to be able to use * to glob all files, hidden and not hidden,
# that are not . and .. -- this does that and also sets the 'dotglob'
# option.
GLOBIGNORE=".:.."

# Delete files from spartan/. See globbing note above.
for f in *
do
  # ignore static directory since we need to handle it separately
  if [ "$f" != "static" ]; then
    rm -rf "$spartandir/$f"
    echo "Delete $spartandir/$f"
  fi
done

echo -e "\nDeleting specific static files separately to preserve the theme's static assets...\n"

for f in static/*
do
  echo "$f"
done
