#!/bin/bash

# Get the directory of the script
dirname="$(dirname "$(readlink -f "$0")")"

# Make sure script is being called correctly. If so, cd into dir to get file 
# names to delete.
if [ "$1" == "org" ]; then
  cd $dirname/org 
  echo -e "Deleting org files from site root...\n"
elif [ "$1" = "markdown" ]; then
  cd $dirname/markdown 
  echo -e "Deleting markdown files from site root...\n"
else
  echo -e "Improper use. Call as either:\n\t./uninstall.sh org\n\t./uninstall.sh markdown"
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

# Delete files from ROOT. See globbing note above.
for f in *
do
  if [ "$f" == "save-as-gitignore" ]; then
    rm -rf "$rootdir/.gitignore"
    echo "Delete $rootdir/.gitignore"
  else
    rm -rf "$rootdir/$f"
    echo "Delete $rootdir/$f"
  fi
done
