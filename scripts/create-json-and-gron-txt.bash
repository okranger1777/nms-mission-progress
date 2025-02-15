#!/bin/bash

if [ $# -lt 1 ]; then
 echo "Usage: $0 [directory-containing-one-save.hg]"
 echo "Create a JSON export in the dir and expand the JSON into text for easy compare" 
 echo "This scripts requires 'libNOM.io.cli' and 'gron'"
 exit 1
fi

if [ ! -d "$1" ]; then
  echo "Could not find dir $1"
  exit 
fi

SDIR=${1%/}
SAVEFILE=$(basename `find $SDIR -name 's*hg'` 2>/dev/null)

if [ -z "$SAVEFILE" ]; then
  echo "Could not find save file, please copy from Steam $SAVEDIR"
  exit
fi


libNOM.io.cli Read -J True -Input "$SDIR/$SAVEFILE" > "$SDIR/export-${SDIR}.json"
gron "$SDIR/export-${SDIR}.json" > "$SDIR/${SDIR}.txt"

ls "$SDIR"
