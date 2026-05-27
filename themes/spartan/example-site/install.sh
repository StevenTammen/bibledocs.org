#!/bin/bash

# Get the directory of the script
dirname="$(dirname "$(readlink -f "$0")")"

# Make sure script is being called correctly. If so, cd into dir to get file
# names to copy.
if [ "$1" == "org" ]; then
  cd $dirname/org 
  echo -e "Copying org files to spartan/...\n"
elif [ "$1" = "markdown" ]; then
  cd $dirname/markdown 
  echo -e "Copying markdown files to spartan/...\n"
else
  echo -e "Improper use. Call as either:\n\t./install.sh org\n\t./install.sh markdown"
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

# Copy files to spartan/. See globbing note above.
for f in *
do
  # ignore static directory since we need to handle it separately
  if [ "$f" != "static" ]; then
    cp -r "$f" "$spartandir/$f"
    echo "Create $spartandir/$f"
  fi
done

echo -e "\nCopying specific static files separately to preserve the theme's static assets...\n"

for f in static/*
do
  echo "$f"
done
