#!/bin/bash

# Get the directory of the script
dirname="$(dirname "$(readlink -f "$0")")"

# Make sure script is being called correctly. If so, cd into dir to get file
# names to copy.
if [ "$1" == "org" ]; then
  cd $dirname/org 
  echo -e "Copying org files to site root...\n"
elif [ "$1" = "markdown" ]; then
  cd $dirname/markdown 
  echo -e "Copying markdown files to site root...\n"
else
  echo -e "Improper use. Call as either:\n\t./install.sh org\n\t./install.sh markdown"
  exit 1
fi

# Assuming in directory ROOT/themes/spartan/quickstart/org,
# OR the directory      ROOT/themes/spartan/quickstart/markdown
# ROOT is ../../../../
root="../../../../"
rootdir=`eval "cd $root;pwd;cd - > /dev/null"`

# Want to be able to use * to glob all files, hidden and not hidden,
# that are not . and .. -- this does that and also sets the 'dotglob'
# option.
GLOBIGNORE=".:.."

# Copy files to ROOT. See globbing note above.
for f in *
do
  cp -r "$f" "$rootdir/$f"
  # Rename save-as-gitignore to set up .gitignore file properly
  if [ "$f" == "save-as-gitignore" ]; then
    mv "$rootdir/$f" "$rootdir/.gitignore"
    echo "Create $rootdir/.gitignore"
  else
    echo "Create $rootdir/$f"
  fi
done
