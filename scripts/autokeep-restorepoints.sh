#!/bin/bash
#set -x -e -u

if [ -z "${SAVEDIR}" ]; then
  echo 'Please set SAVEDIR such as SAVEDIR="$HOME/Library/Application Support/HelloGames/NMS/st_xxx"'
  exit
fi

if [ $# -lt 1 ]; then
  echo "Usage: $0 [save.hg]"
  exit
fi
SAVEFILE=$1

if [ ! -f "$SAVEDIR/$SAVEFILE" ]; then
  echo "$SAVEDIR/$SAVEFILE does not exist"
  exit
fi

SVD=tmp
mkdir -p "$SVD"
echo "Saving $SAVEDIR/$SAVEFILE to $SVD/ if it changes"

while true; do

  if cmp -s "$SAVEDIR/$SAVEFILE" "$SVD/latest/$SAVEFILE"; then
    if [ ! -z $debug ]; then
      date --utc +%Y-%m-%dT%H%M | tr -d '\n'
      echo " Files are identical"
    fi

  else
    NEWDIR=$(date --utc +%Y-%m-%dT%H%M)
    mkdir -p "$SVD/$NEWDIR"
    if [ ! -z $debug ]; then
      echo "Saving new copy, latest is now $SVD/$NEWDIR"
    fi
    cp "$SAVEDIR/$SAVEFILE" "$SVD/$NEWDIR"
    cp "$SAVEDIR/mf_${SAVEFILE}" "$SVD/$NEWDIR"
    rm "$SVD/latest"
    ln -s "$PWD/$SVD/$NEWDIR" "$SVD/latest"

  fi
  sleep 10
  
done
