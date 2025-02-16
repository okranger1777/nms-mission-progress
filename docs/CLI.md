# libNOM CLI

Here is example usage on a Mac with the libNOM CLI installed and on your PATH.
Change the first two lines to match your environment.

If not using Steam, use `libNOM.io.cli -H` to determine the correct format option to use.

Tested with https://github.com/zencq/libNOM.io/releases/tag/0.14.0


```bash

SAVEDIR="$HOME/Library/Application Support/HelloGames/NMS/st_1234..."
SAVEFILE="save10.hg"

BACKDIR=backups/$(date +%s)
mkdir -p "$BACKDIR"
cp "$SAVEDIR/$SAVEFILE" "$BACKDIR"
cp "$SAVEDIR/mf_$SAVEFILE" "$BACKDIR"

FNAME=creative.json

# convert save to JSON
libNOM.io.cli Read -J True -Input "$SAVEDIR/$SAVEFILE" > "$HOME/Downloads/$FNAME"

# update script writes to out.json
./update-nms-mission-progress.py "$HOME/Downloads/$FNAME"

# write JSON to save file
cat out.json | libNOM.io.cli Write -O tmp -F Steam -I 1
mv tmp/*data "$SAVEDIR/$SAVEFILE"
mv tmp/*meta "$SAVEDIR/mf_$SAVEFILE"
```

## `create-json-and-gron-txt.bash`

The `create-json-and-gron-txt.bash` script also requires `libNOM.io.cli` and
can be used to create text files for two restore points:

```bash
cd tmp
mkdir before
cp "$SAVEDIR/save.hg" before
../scripts/create-json-and-gron-txt.bash before
# take actions in game and create a new restore point
mkdir after
cp "$SAVEDIR/save.hg" after
../scripts/create-json-and-gron-txt.bash after
diff before/before.txt after/after.txt 
```

The `gron` text files can also be compared in an editor such as VS Code.

## Other Scripts
See the `scripts` directory for other utility scripts. 

* `create-json-and-gron-txt [directory-containing-one-save.hg]` - Create a JSON export in the dir and expand the JSON into text for easy compare

* `enable-purple-warp.py` - Minimal changes to a JSON export to enable warp to Purple systems

* `hotkeys.py` - Set quick menu hot keys in a JSON export for Multi-Tool swap, Toggle Third-Person View, Photo Mode, etc.